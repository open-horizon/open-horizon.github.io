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

Empiece por instalar el agente de {{site.data.keyword.edge_notm}} en uno de estos tipos de
clústeres periféricos de kubernetes:

* [Instalación de agente en el clúster periférico de Kubernetes de {{site.data.keyword.ocp}}](#install_kube)
* [Instalación de agente en clústeres periféricos k3s y microk8s](#install_lite)

A continuación, despliegue un servicio periférico en el clúster periférico: 

* [Despliegue de servicios en el clúster periférico](#deploying_services)

Si necesita eliminar el agente:

* [Eliminación del agente del clúster periférico](#remove_agent)

## Instalación del agente en el clúster periférico de Kubernetes de {{site.data.keyword.ocp}}
{: #install_kube}

En esta sección se describe cómo instalar el agente de {{site.data.keyword.ieam}} en el clúster
periférico de {{site.data.keyword.ocp}}. Siga estos pasos en un host que tenga acceso de administrador
al clúster periférico:

1. Inicie la sesión en el clúster periférico como **admin**:

   ```bash
	oc login https://<API_ENDPOINT_HOST>:<PORT> -u <ADMIN_USER> -p <ADMIN_PASSWORD> --insecure-skip-tls-verify=true
   ```
   {: codeblock}

2. Establezca la variable de espacio de nombres de agente en el valor predeterminado
(o en el espacio de nombres en el que desee instalar explícitamente el agente):

   ```bash
   export AGENT_NAMESPACE=openhorizon-agent
   ```
   {: codeblock}

3. Establezca la clase de almacenamiento que desea que el agente utilice para una clase de almacenamiento
incorporada o en una que haya creado. Por ejemplo:

   ```bash
   export EDGE_CLUSTER_STORAGE_CLASS=rook-ceph-cephfs-internal
   ```
   {: codeblock}

4. Para configurar el registro de imágenes en el clúster periférico, realice los pasos 2 a 8 de
[Utilización del registro de imágenes de
OpenShift](../developing/container_registry.md##ocp_image_registry) con este cambio: en el paso 4, establezca OCP_PROJECT en:
**$AGENT_NAMESPACE**.

5. El script **agent-install.sh** almacenará el agente
{{site.data.keyword.ieam}} en el registro de contenedor de clúster periférico. Establezca
el usuario de registro, la contraseña y la vía de acceso de imagen completa (menos la etiqueta) que
se deben utilizar:

   ```bash
   export EDGE_CLUSTER_REGISTRY_USERNAME=$OCP_USER
   export EDGE_CLUSTER_REGISTRY_TOKEN="$OCP_TOKEN"
   export IMAGE_ON_EDGE_CLUSTER_REGISTRY=$OCP_DOCKER_HOST/$OCP_PROJECT/amd64_anax_k8s
   ```
   {: codeblock}

   **Nota:** La imagen de agente de {{site.data.keyword.ieam}} se almacena en
el registro de clúster periférico local, porque el clúster periférico kubernetes necesita acceso continuo a él,
en caso de que necesite reiniciarlo o moverlo a otro pod.

6. Exporte las credenciales de usuario de Horizon Exchange:

   ```bash
   export HZN_EXCHANGE_USER_AUTH=iamapikey:<clave-de-API>
   ```
   {: codeblock}

7. Obtenga el archivo **agentInstallFiles-x86_64-Cluster.tar.gz** y una clave de API del administrador. Éstos ya se deben haber creado en [Recopilar la información y los archivos necesarios para los clústeres periféricos](preparing_edge_cluster.md).  

8. Extraiga el script **agent-install.sh** del archivo tar:

   ```bash
   tar -zxvf agentInstallFiles-x86_64-Cluster.tar.gz agent-install.sh
   ```
   {: codeblock}

9. Ejecute el mandato **agent-install.sh** para instalar y configurar
el agente de Horizon y registrar el clúster periférico con la política:

   ```bash
   ./agent-install.sh -D cluster -z agentInstallFiles-x86_64-Cluster.tar.gz -d <id-nodo>
   ```
   {: codeblock}

   **Notas:**
   * Para ver todos los distintivos disponibles, ejecute: **./agent-install.sh -h**
   * Si se produce un error que hace que **agent-install.sh** no se complete, ejecute
**agent-uninstall.sh** (consulte [Eliminación del agente del
clúster periférico](#remove_agent)) y, a continuación, repita los pasos de esta sección.

10. Cambie el espacio de nombres/proyecto del agente y verifique que el pod de agente se esté ejecutando:

   ```bash
   oc project $AGENT_NAMESPACE
   oc get pods
   ```
   {: codeblock}

11. Ahora que el agente está instalado en el clúster periférico, puede ejecutar estos mandatos si desea
familiarizarse con los recursos de kubernetes asociados con el agente:

   ```bash
   oc get namespace $AGENT_NAMESPACE
   oc project $AGENT_NAMESPACE   # asegurarse de que es el espacio de nombres/proyecto actual
   oc get deployment -o wide
   oc get deployment agent -o yaml   # obtener detalles del despliegue
   oc get configmap openhorizon-agent-config -o yaml
   oc get secret openhorizon-agent-secrets -o yaml
   oc get pvc openhorizon-agent-pvc -o yaml   # volumen persistente
   ```
   {: codeblock}

12. A menudo, cuando un clúster periférico está registrado para la política, pero no tiene ninguna política
de nodo especificada por el usuario, ninguna de las políticas de despliegue desplegará servicios periféricos en él. Este
es el caso de los ejemplos de Horizon. Continúe con [Despliegue de servicios
en el clúster periférico](#deploying_services) para establecer la política de nodo para que se despliegue un servicio periférico
en este clúster periférico.

## Instalación de agente en clústeres periféricos k3s y microk8s
{: #install_lite}

En esta sección se describe cómo instalar el agente de {{site.data.keyword.ieam}} en
los clústeres Kubernetes ligeros y pequeños, k3s o microk8s:

1. Inicie la sesión en el clúster periférico como **root**.

2. Obtenga el archivo **agentInstallFiles-x86_64-Cluster.tar.gz** y una clave de API del administrador. Éstos ya se deben haber creado en [Recopilar la información y los archivos necesarios para los clústeres periféricos](preparing_edge_cluster.md).  

3. Extraiga el script **agent-install.sh** del archivo tar:

   ```bash
   tar -zxvf agentInstallFiles-x86_64-Cluster.tar.gz agent-install.sh
   ```
   {: codeblock}

4. Exporte las credenciales de usuario de Horizon Exchange:

   ```bash
   export HZN_EXCHANGE_USER_AUTH=iamapikey:<clave-de-API>
   ```
   {: codeblock}

5. El script **agent-install.sh** almacenará el agente de {{site.data.keyword.ieam}}
en el registro de imágenes de clúster periférico. Establezca la vía de acceso de imagen completa (menos la etiqueta)
que se debe utilizar. Por ejemplo:

   ```bash
   export IMAGE_ON_EDGE_CLUSTER_REGISTRY=$REGISTRY_ENDPOINT/openhorizon-agent/amd64_anax_k8s
   ```
   {: codeblock}

   **Nota:** La imagen de agente de {{site.data.keyword.ieam}} se almacena en
el registro de clúster periférico local, porque el clúster periférico kubernetes necesita acceso continuo a él,
en caso de que necesite reiniciarlo o moverlo a otro pod.

6. Indique a **agent-install.sh** que utilice la clase de almacenamiento predeterminada:


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

7. Ejecute el mandato **agent-install.sh** para instalar y configurar
el agente de Horizon y registrar el clúster periférico con la política:

   ```bash
   ./agent-install.sh -D cluster -z agentInstallFiles-x86_64-Cluster.tar.gz -d <id-nodo>
   ```
   {: codeblock}

   **Notas:**
   * Para ver todos los distintivos disponibles, ejecute: **./agent-install.sh -h**
   * Si se produce un error que hace que **agent-install.sh** no se complete, ejecute
**agent-uninstall.sh** (consulte [Eliminación de
agente de clúster periférico](#remove_agent)) antes de ejecutar el agent-install.sh de nuevo.

8. Verifique que el pod de agente esté en ejecución:

   ```bash
   kubectl get namespaces
   kubectl -n openhorizon-agent get pods
   ```
   {: codeblock}

9. A menudo, cuando un clúster periférico está registrado para la política, pero no tiene ninguna política
de nodo especificada por el usuario, ninguna de las políticas de despliegue desplegará servicios periféricos en él. Este
es el caso de los ejemplos de Horizon. Continúe con [Despliegue de servicios
en el clúster periférico](#deploying_services) para establecer la política de nodo para que se despliegue un servicio periférico
en este clúster periférico.

## Despliegue de servicios en el clúster periférico
{: #deploying_services}

El establecimiento de la política de nodo en este clúster periférico puede hacer que las políticas de
despliegue desplieguen servicios periféricos aquí. Esta sección muestra un ejemplo de cómo hacerlo.

1. Establezca algunos alias para que sea más cómodo ejecutar el mandato `hzn`.
(El mandato `hzn` está dentro del contenedor de agente, pero estos alias permiten ejecutar
`hzn` desde este host.)

   ```bash
   cat << 'END_ALIASES' >> ~/.bash_aliases
   alias getagentpod='kubectl -n openhorizon-agent get pods --selector=app=agent -o jsonpath={.items[*].metadata.name}'
   alias hzn='kubectl -n openhorizon-agent exec -i $(getagentpod) -- hzn'
   END_ALIASES
   source ~/.bash_aliases
   ```
   {: codeblock}

2. Verifique que el nodo periférico está configurado (registrado en el centro de gestión
de {{site.data.keyword.ieam}}):

   ```bash
   hzn node list
   ```
   {: codeblock}

3. Para probar el agente de clúster periférico, establezca la política de nodo con una propiedad
que haga que el servicio y el operador de helloworld de ejemplo se desplieguen en este nodo periférico: 

   ```bash
   cat << 'EOF' > operator-example-node.policy.json
   {
     "properties": [
       { "name": "openhorizon.example", "value": "operator" }
     ]
   }
   EOF

   cat operator-example-node.policy.json | hzn policy update -f-
   hzn policy list
   ```
   {: codeblock}

   **Nota:**
   * Dado que el mandato real **hzn** se está ejecutando dentro del contenedor de agente,
para cualquier submandato `hzn` que requiera un archivo de entrada, necesitará
pasar el archivo al mandato para que su contenido se transfiera al contenedor.

4. Después de un minuto, compruebe si hay un acuerdo y los contenedores de servicio y
operador periféricos en ejecución:

   ```bash
   hzn agreement list
   kubectl -n openhorizon-agent get pods
   ```
   {: codeblock}

5. Utilizando los ID de pod del mandato anterior, consulte el registro de operador y servicio periféricos:

   ```bash
   kubectl -n openhorizon-agent logs -f <id-pod-operador>
   # control-c to get out
   kubectl -n openhorizon-agent logs -f <id-pod-servicio>
   # control-c to get out
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
  cat <new-node-policy>.json | hzn policy update -f-
  hzn policy list
  ```
  {: codeblock}

   Después de un minuto o dos, los nuevos servicios se desplegarán en este clúster periférico.

* Nota: Con microk8s en algunos tipos de VM, es posible que los pods de servicio que
se están deteniendo (sustituyendo) queden atascados en el estado **Terminando**. Si
esto sucede, puede limpiarlos ejecutando:

  ```bash
  kubectl delete pod <pod-id> -n openhorizon-agent --force --grace-period=0
  pkill -fe <proceso-servicio>
  ```
  {: codeblock}

* Si desea utilizar un patrón, en lugar de una política, para ejecutar servicios en el clúster periférico:

  ```bash
  hzn unregister -f
  hzn register -n $HZN_EXCHANGE_NODE_AUTH -p <nombre-patrón>
  ```
  {: codeblock}

## Eliminación de agente de clúster periférico
{: #remove_agent}

Para anular el registro de un clúster periférico y eliminar el agente de
{{site.data.keyword.ieam}} de ese clúster, realice estos pasos:

1. Extraiga el script **agent-uninstall.sh** del archivo tar:

   ```bash
   tar -zxvf agentInstallFiles-x86_64-Cluster.tar.gz agent-uninstall.sh
   ```
   {: codeblock}

2. Exporte las credenciales de usuario de Horizon Exchange:

   ```bash
   export HZN_EXCHANGE_USER_AUTH=iamapikey:<clave-de-API>
   ```
   {: codeblock}

3. Elimine el agente:

   ```bash
   ./agent-uninstall.sh -u $HZN_EXCHANGE_USER_AUTH -d
   ```
   {: codeblock}

Nota: en ocasiones, la supresión del espacio de nombres se detiene en el estado "Terminando". En esta situación, consulte [Un espacio de nombres se ha atascado en el estado Terminando ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.1.1/troubleshoot/ns_terminating.html) para suprimir el espacio de nombres manualmente.
