---

copyright:
  years: 2020
lastupdated: "2020-04-9"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Instalación del agente
{: #importing_clusters}

**Nota**: la instalación de agente de {{site.data.keyword.ieam}} necesita acceso de administrador de clúster en el clúster periférico.

Empiece por instalar el agente de {{site.data.keyword.edge_notm}} en uno de estos tipos de clústeres periféricos de Kubernetes:

* [Instalación de agente en el clúster periférico de Kubernetes de {{site.data.keyword.ocp}}](#install_kube)
* [Instalación de agente en clústeres periféricos k3s y microk8s](#install_lite)

A continuación, despliegue un servicio periférico en el clúster periférico:

* [Despliegue de servicios en el clúster periférico](#deploying_services)

Si necesita eliminar el agente:

* [Eliminación de agente de clúster periférico](../using_edge_services/removing_agent_from_cluster.md)

## Instalación del agente en el clúster periférico de Kubernetes de {{site.data.keyword.ocp}}
{: #install_kube}

Este contenido describe cómo instalar el agente de {{site.data.keyword.ieam}} en el clúster periférico de {{site.data.keyword.ocp}}. Siga estos pasos en un host que tenga acceso de administrador al clúster periférico:

1. Inicie la sesión en el clúster periférico como **admin**:

   ```bash
   oc login https://<host_punto_final_api>:<puerto> -u <usuario_admin> -p <contraseña_admin> --insecure-skip-tls-verify=true
   ```
   {: codeblock}

2. Si no ha completado los pasos recogidos en [Creación de la clave de API](../hub/prepare_for_edge_nodes.md), hágalo ahora. Este proceso crea una clave de API, localiza algunos archivos y recopila valores de variables de entorno que son necesarios al configurar nodos periféricos. Establezca las mismas variables de entorno en este clúster periférico:

  ```bash
  export HZN_EXCHANGE_USER_AUTH=iamapikey:<clave-api>   export HZN_ORG_ID=<su-organización-exchange>   export HZN_FSS_CSSURL=https://<ingreso-centro-gestión-ieam>/edge-css/
  ```
  {: codeblock}

3. Establezca la variable de espacio de nombres de agente en el valor predeterminado (o en el espacio de nombres en el que desee instalar explícitamente el agente):

   ```bash
   export AGENT_NAMESPACE=openhorizon-agent
   ```
   {: codeblock}

4. Establezca la clase de almacenamiento que desea que utilice el agente, que puede ser una clase de almacenamiento incorporada o una que haya creado. Puede ver las clases de almacenamiento disponibles con el primero de los dos mandatos siguientes y, a continuación, sustituir el nombre del que desea utilizar en el segundo mandato. Se debe etiquetar una clase de almacenamiento como `(default)`:

   ```bash
   oc get storageclass    export EDGE_CLUSTER_STORAGE_CLASS=<rook-ceph-cephfs-internal>
   ```
   {: codeblock}

5. Determine si se ha creado una ruta predeterminada para el registro de imagen de {{site.data.keyword.open_shift}} a la que se pueda acceder desde fuera del clúster:

   ```bash
   oc get route default-route -n openshift-image-registry --template='{{ .spec.host }}'
   ```
   {: codeblock}

   Si la respuesta del mandato indica que no se ha encontrado la **default-route**, deberá exponerla (consulte [Exposing the registry](https://docs.openshift.com/container-platform/4.6/registry/securing-exposing-registry.html) para conocer los detalles):

   ```bash
   oc patch configs.imageregistry.operator.openshift.io/cluster --patch '{"spec":{"defaultRoute":true}}' --type=merge
   ```
   {: codeblock}

6. Recupere el nombre de ruta de repositorio que hay que utilizar:

   ```bash
   export OCP_IMAGE_REGISTRY=`oc get route default-route -n openshift-image-registry --template='{{ .spec.host }}'`
   ```
   {: codeblock}

7. Cree un proyecto nuevo en el que almacenar las imágenes:

   ```bash
   export OCP_PROJECT=$AGENT_NAMESPACE    oc new-project $OCP_PROJECT
   ```
   {: codeblock}

8. Cree una cuenta de servicio con un nombre de su elección:

   ```bash
   export OCP_USER=<nombre-cuenta-servicio>
   oc create serviceaccount $OCP_USER
   ```
   {: codeblock}

9. Añada un rol a la cuenta de servicio para el proyecto actual:

   ```bash
   oc policy add-role-to-user edit system:serviceaccount:$OCP_PROJECT:$OCP_USER
   ```
   {: codeblock}

10. Establezca la señal de la cuenta de servicio en la siguiente variable de entorno:

   ```bash
   export OCP_TOKEN=`oc serviceaccounts get-token $OCP_USER`
   ```
   {: codeblock}

11. Obtenga el certificado de {{site.data.keyword.open_shift}} y permita que Docker confíe en el mismo:

   ```bash
   echo | openssl s_client -connect $OCP_IMAGE_REGISTRY:443 -showcerts | sed -n "/-----BEGIN CERTIFICATE-----/,/-----END CERTIFICATE-----/p" > ca.crt
   ```
   {: codeblock}

   En {{site.data.keyword.linux_notm}}:

   ```bash
   mkdir -p /etc/docker/certs.d/$OCP_IMAGE_REGISTRY    cp ca.crt /etc/docker/certs.d/$OCP_IMAGE_REGISTRY    systemctl restart docker.service
   ```
   {: codeblock}

   En {{site.data.keyword.macOS_notm}}:

   ```bash
   mkdir -p ~/.docker/certs.d/$OCP_IMAGE_REGISTRY    cp ca.crt ~/.docker/certs.d/$OCP_IMAGE_REGISTRY
   ```
   {: codeblock}

   En {{site.data.keyword.macOS_notm}}, utilice el icono utilice el escritorio de Docker en el lado derecho de la barra de menús del escritorio para reiniciar Doker pulsando **Reiniciar** en el menú desplegable.

12. Inicie la sesión en el host de {{site.data.keyword.ocp}} Docker:

   ```bash
   echo "$OCP_TOKEN" | docker login -u $OCP_USER --password-stdin $OCP_IMAGE_REGISTRY
   ```
   {: codeblock}

13. Configure almacenes de confianza adicionales para el acceso al registro de imágenes:   

    ```bash
    oc create configmap registry-config --from-file=$OCP_IMAGE_REGISTRY=ca.crt -n openshift-config
    ```
    {: codeblock}

14. Edite el nuevo `registry-config`:

    ```bash
    oc edit image.config.openshift.io cluster
    ```
    {: codeblock}

15. Actualice la sección `spec:`:

    ```bash
    spec:       additionalTrustedCA:        name: registry-config
    ```
    {: codeblock}

16. El script **agent-install.sh** almacena el agente de {{site.data.keyword.ieam}} en el registro de contenedor de clúster periférico. Establezca el usuario de registro, la contraseña y la vía de acceso de imagen completa (menos el código):

   ```bash
   export EDGE_CLUSTER_REGISTRY_USERNAME=$OCP_USER    export EDGE_CLUSTER_REGISTRY_TOKEN="$OCP_TOKEN"    export IMAGE_ON_EDGE_CLUSTER_REGISTRY=$OCP_IMAGE_REGISTRY/$OCP_PROJECT/amd64_anax_k8s
   ```
   {: codeblock}

   **Nota**: La imagen de agente de {{site.data.keyword.ieam}} se almacena en el registro de clúster periférico local porque el clúster periférico Kubernetes necesita acceso continuo a él, en caso de que necesite reiniciarlo o moverlo a otro pod.

17. Descargue el script **agent-install.sh** desde Cloud Sync Service (CSS) y conviértalo en un ejecutable:

   ```bash
   curl -u "$HZN_ORG_ID/$HZN_EXCHANGE_USER_AUTH" -k -o agent-install.sh $HZN_FSS_CSSURL/api/v1/objects/IBM/agent_files/agent-install.sh/data   chmod +x agent-install.sh
   ```
   {: codeblock}

18. Ejecute **agent-install.sh** para obtener los archivos necesarios de CSS, instale y configure el agente de {{site.data.keyword.horizon}} y registre el clúster periférico en la política:

   ```bash
   ./agent-install.sh -D cluster -i 'css:'
   ```
   {: codeblock}

   **Notas**:
   * Para ver todos los distintivos disponibles, ejecute: **./agent-install.sh -h**
   * Si un error hace que **agent-install.sh** falle, corrija el error y ejecute de nuevo **agent-install.sh**. Si esto no funciona, ejecute **agent-uninstall.sh** (consulte [Eliminación de agente de clúster periférico](../using_edge_services/removing_agent_from_cluster.md)) antes de ejecutar **agent-install.sh** de nuevo.

19. Vaya al espacio de nombres de agente (también conocido como proyecto) y verifique que el pod de agente está en ejecución:

   ```bash
   oc project $AGENT_NAMESPACE    oc get pods
   ```
   {: codeblock}

20. Ahora que el agente está instalado en el clúster periférico, puede ejecutar estos mandatos si desea familiarizarse con los recursos de Kubernetes asociados con el agente:

   ```bash
   oc get namespace $AGENT_NAMESPACE    oc project $AGENT_NAMESPACE   # asegurarse de que es el espacio de nombres/proyecto actual    oc get deployment -o wide    oc get deployment agent -o yaml   # obtener detalles del despliegue    oc get configmap openhorizon-agent-config -o yaml    oc get secret openhorizon-agent-secrets -o yaml    oc get pvc openhorizon-agent-pvc -o yaml   # volumen persistente
   ```
   {: codeblock}

21. A menudo, cuando un clúster periférico está registrado para la política, pero no tiene política de nodo especificada por el usuario, ninguna de las políticas de despliegue desplegará servicios periféricos en él. Este es el caso de los ejemplos de Horizon. Continúe con [Despliegue de servicios en el clúster periférico](#deploying_services) para establecer la política de nodo para que se despliegue un servicio periférico en este clúster periférico.

## Instalación de agente en clústeres periféricos k3s y microk8s
{: #install_lite}

Este contenido describe cómo instalar el agente de {{site.data.keyword.ieam}} en clústeres Kubernetes ligeros y pequeños, [k3s](https://k3s.io/) o [microk8s](https://microk8s.io/):

1. Inicie la sesión en el clúster periférico como **root**.

2. Si no ha completado los pasos recogidos en [Creación de la clave de API](../hub/prepare_for_edge_nodes.md), hágalo ahora. Este proceso crea una clave de API, localiza algunos archivos y recopila valores de variables de entorno que son necesarios al configurar nodos periféricos. Establezca las mismas variables de entorno en este clúster periférico:

  ```bash
  export HZN_EXCHANGE_USER_AUTH=iamapikey:<clave-api>   export HZN_ORG_ID=<su-organización-exchange>   export HZN_FSS_CSSURL=https://<ingreso-centro-gestión-ieam>/edge-css/
  ```
  {: codeblock}

3. Copie el script **agent-install.sh** en el clúster periférico nuevo.

4. El script **agent-install.sh** almacenará el agente de {{site.data.keyword.ieam}} en el registro de imágenes de clúster periférico. Establezca la vía de acceso de imagen completa (menos la etiqueta) que se debe utilizar. Por ejemplo:

   * En k3s:

      ```bash
      REGISTRY_ENDPOINT=$(kubectl get service docker-registry-service | grep docker-registry-service | awk '{print $3;}'):5000       export IMAGE_ON_EDGE_CLUSTER_REGISTRY=$REGISTRY_ENDPOINT/openhorizon-agent/amd64_anax_k8s
      ```
      {: codeblock}

   * En microk8s:

      ```bash
      export IMAGE_ON_EDGE_CLUSTER_REGISTRY=localhost:32000/openhorizon-agent/amd64_anax_k8s
      ```
      {: codeblock}

   **Nota**: La imagen de agente de {{site.data.keyword.ieam}} se almacena en el registro de clúster periférico local porque el clúster periférico Kubernetes necesita acceso continuo a él, en caso de que necesite reiniciarlo o moverlo a otro pod.

5. Indique a **agent-install.sh** que utilice la clase de almacenamiento predeterminada:

   * En k3s:

      ```bash
      export EDGE_CLUSTER_STORAGE_CLASS=local-path
      ```
      {: codeblock}

   * En microk8s:

      ```bash
      export EDGE_CLUSTER_STORAGE_CLASS=microk8s-hostpath
      ```
      {: codeblock}

6. Ejecute **agent-install.sh** para obtener los archivos necesarios de CSS (Cloud Sync Service), instale y configure el agente de {{site.data.keyword.horizon}} y registre el clúster periférico en la política:

   ```bash
   ./agent-install.sh -D cluster -i 'css:'
   ```
   {: codeblock}

   **Notas**:
   * Para ver todos los distintivos disponibles, ejecute: **./agent-install.sh -h**
   * Si se produce un error que hace que **agent-install.sh** no se complete correctamente, corrija el error que se visualiza y vuelva a ejecutar **agent-install.sh**. Si esto no funciona, ejecute **agent-uninstall.sh** (consulte [Eliminación de agente de clúster periférico](../using_edge_services/removing_agent_from_cluster.md)) antes de ejecutar **agent-install.sh** de nuevo.

7. Verifique que el pod de agente esté en ejecución:

   ```bash
   kubectl get namespaces    kubectl -n openhorizon-agent get pods
   ```
   {: codeblock}

8. Normalmente, cuando un clúster periférico está registrado para la política, pero no tiene ninguna política de nodo especificada por el usuario, ninguna de las políticas de despliegue despliega servicios periféricos en él. Se trata de un comportamiento previsto. Continúe con [Despliegue de servicios en el clúster periférico](#deploying_services) para establecer la política de nodo para que se despliegue un servicio periférico en este clúster periférico.

## Despliegue de servicios en el clúster periférico
{: #deploying_services}

El establecimiento de la política de nodo en este clúster periférico puede hacer que las políticas de despliegue desplieguen servicios periféricos aquí. Este contenido muestra un ejemplo de cómo hacerlo.

1. Establezca algunos alias para que sea más cómodo ejecutar el mandato `hzn`. (El mandato `hzn` está dentro del contenedor de agente, pero estos alias permiten ejecutar `hzn` desde este host.)

   ```bash
   cat << 'END_ALIASES' >> ~/.bash_aliases    alias getagentpod='kubectl -n openhorizon-agent get pods --selector=app=agent -o jsonpath={.items[*].metadata.name}'    alias hzn='kubectl -n openhorizon-agent exec -i $(getagentpod) -- hzn'    END_ALIASES    source ~/.bash_aliases
   ```
   {: codeblock}

2. Verifique que el nodo periférico está configurado (registrado en el centro de gestión de {{site.data.keyword.ieam}}):

   ```bash
   hzn node list
   ```
   {: codeblock}

3. Para probar el agente de clúster periférico, establezca la política de nodo con una propiedad que despliegue el operador y servicio de helloworld de ejemplo en este nodo periférico:

   ```bash
   cat << 'EOF' > operator-example-node.policy.json    {
     "properties": [
       { "name": "openhorizon.example", "value": "operator" }      ]
   }    EOF

   cat operator-example-node.policy.json | hzn policy update -f-    hzn policy list
   ```
   {: codeblock}

   **Nota**:
   * Puesto que el mandato real **hzn** se está ejecutando dentro del contenedor de agente, para cualquier mandato `hzn` que necesite un archivo de entrada, debe pasar el archivo al mandato para que su contenido se transfiera al contenedor.

4. Después de un minuto, compruebe si hay un acuerdo y los contenedores de servicio y operador periféricos en ejecución:

   ```bash
   hzn agreement list    kubectl -n openhorizon-agent get pods
   ```
   {: codeblock}

5. Utilizando los ID de pod del mandato anterior, consulte el registro de operador y servicio periféricos:

   ```bash
   kubectl -n openhorizon-agent logs -f <id-pod-operador>    # control-c to get out    kubectl -n openhorizon-agent logs -f <id-pod-servicio>    # control-c to get out
   ```
   {: codeblock}

6. También puede ver las variables de entorno que el agente pasa al servicio periférico:

   ```bash
   kubectl -n openhorizon-agent exec -i <id-pod-servicio> -- env | grep HZN_
   ```
   {: codeblock}

### Cambio de los servicios que se despliegan en el clúster periférico
{: #changing_services}

* Para cambiar los servicios que se despliegan en el clúster periférico, cambie la política de nodo:

  ```bash
  cat <new-node-policy>.json | hzn policy update -f-   hzn policy list
  ```
  {: codeblock}

   Después de un minuto o dos, los nuevos servicios se desplegarán en este clúster periférico.

* **Nota**: En algunas máquinas virtuales con microk8s, es posible que los pods de servicio que se están deteniendo (sustituyendo) se detengan en estado **Terminando**. Si sucede esto, ejecute:

  ```bash
  kubectl delete pod <pod-id> -n openhorizon-agent --force --grace-period=0   pkill -fe <proceso-servicio>
  ```
  {: codeblock}

* Si desea utilizar un patrón, en lugar de una política, para ejecutar servicios en el clúster periférico:

  ```bash
  hzn unregister -f   hzn register -n $HZN_EXCHANGE_NODE_AUTH -p <nombre-patrón>
  ```
  {: codeblock}
