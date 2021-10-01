---

copyright:
years: 2019, 2020
lastupdated: "2020-01-22"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Utilización de un registro de contenedor privado
{: #container_registry}

Si una imagen de software incluye activos que no son apropiados para incluir en un registro público, puede utilizar un registro de contenedor de Docker privado, por ejemplo {{site.data.keyword.open_shift}} Image Registry o {{site.data.keyword.ibm_cloud}} Container Registry, en los que el acceso está estrechamente controlado.
{:shortdesc}

Si aún no lo ha hecho, siga los pasos de [Desarrollo de un servicio periférico para dispositivos](../OH/docs/developing/developing.md) para crear y desplegar al menos un servicio periférico de ejemplo para asegurarse de que está familiarizado con el proceso básico.

En esta página se describen dos registros en los que puede almacenar imágenes de servicios periféricos:
* [Utilización del registro de imagen de {{site.data.keyword.open_shift}}](#ocp_image_registry)
* [Utilización de {{site.data.keyword.cloud_notm}} Container Registry](#ibm_cloud_container_registry)

También sirven como ejemplos de cómo puede utilizar cualquier registro de imágenes privado con {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}).

## Utilización del registro de imagen de {{site.data.keyword.open_shift}}
{: #ocp_image_registry}

### Antes de empezar

* Si aún no lo ha hecho, instale los mandatos de [CLI de IBM Cloud Pak (**cloudctl**) y CLI de cliente de OpenShift (**oc**)](../cli/cloudctl_oc_cli.md).

**Nota**: debido a que el registro local normalmente tiene un disco más pequeño, puede que se llene rápidamente. En algunos casos, esto puede afectar negativamente al centro de gestión hasta el punto que podría dejar de funcionar. Debido a esto, considere la posibilidad de utilizar los registros de imágenes locales de {{site.data.keyword.open_shift}} si la supervisión preventiva se implementa en el entorno; de lo contrario, utilice registros de imágenes externos.

### Procedimiento

**Nota**: para obtener más información sobre la sintaxis de mandato, consulte [Convenciones utilizadas en este documento](../getting_started/document_conventions.md).

1. Asegúrese de que está conectado al clúster de {{site.data.keyword.open_shift}} con privilegios de administrador de clúster.

   ```bash
   cloudctl login -a <URL-de-clúster> -u <usuario> -p <contraseña> -n kube-system --skip-ssl-validation
   ```
   {: codeblock}

2. Determine si se ha creado una ruta predeterminada para el registro de imagen de {{site.data.keyword.open_shift}} a la que se pueda acceder desde fuera del clúster:

   ```bash
   oc get route default-route -n openshift-image-registry --template='{{ .spec.host }}'
   ```
   {: codeblock}

   Si la respuesta del mandato indica que no se ha encontrado la **default-route**, créela (consulte [Exposing the registry](https://docs.openshift.com/container-platform/4.6/registry/securing-exposing-registry.html) para conocer los detalles):

   ```bash
   oc patch configs.imageregistry.operator.openshift.io/cluster --patch '{"spec":{"defaultRoute":true}}' --type=merge
   ```
   {: codeblock}

3. Recupere el nombre de ruta de repositorio que hay que utilizar:

   ```bash
   export OCP_DOCKER_HOST=`oc get route default-route -n openshift-image-registry --template='{{ .spec.host }}'`
   ```
   {: codeblock}

4. Cree un proyecto nuevo en el que almacenar las imágenes:

   ```bash
   export OCP_PROJECT=<su-nuevo-proyecto>    oc new-project $OCP_PROJECT
   ```
   {: codeblock}

5. Cree una cuenta de servicio con un nombre de su elección:

   ```bash
   export OCP_USER=<nombre-cuenta-servicio>    oc create serviceaccount $OCP_USER
   ```
   {: codeblock}

6. Añada un rol a la cuenta de servicio para el proyecto actual:

   ```bash
   oc policy add-role-to-user edit system:serviceaccount:$OCP_PROJECT:$OCP_USER
   ```
   {: codeblock}

7. Obtenga la señal asignada a la cuenta de servicio:

   ```bash
   export OCP_TOKEN=`oc serviceaccounts get-token $OCP_USER`
   ```
   {: codeblock}

8. Obtenga el certificado de {{site.data.keyword.open_shift}} y haga que Docker confíe en él:

   ```bash
   echo | openssl s_client -connect $OCP_DOCKER_HOST:443 -showcerts | sed -n "/-----BEGIN CERTIFICATE-----/,/-----END CERTIFICATE-----/p" > ca.crt
   ```
   {: codeblock}

   En {{site.data.keyword.linux_notm}}:

   ```bash
   mkdir -p /etc/docker/certs.d/$OCP_DOCKER_HOST    cp ca.crt /etc/docker/certs.d/$OCP_DOCKER_HOST    systemctl restart docker.service
   ```
   {: codeblock}

   En {{site.data.keyword.macOS_notm}}:

   ```bash
   mkdir -p ~/.docker/certs.d/$OCP_DOCKER_HOST    cp ca.crt ~/.docker/certs.d/$OCP_DOCKER_HOST
   ```
   {: codeblock}

   En {{site.data.keyword.macOS_notm}}, pulse sobre el icono de ballena en el lado derecho de la barra de menús del escritorio y seleccione **Reiniciar** para reiniciar Docker.

9. Inicie la sesión en el host de {{site.data.keyword.ocp}} Docker:

   ```bash
   echo "$OCP_TOKEN" | docker login -u $OCP_USER --password-stdin $OCP_DOCKER_HOST
   ```
   {: codeblock}

10. Configure almacenes de confianza adicionales para el acceso al registro de imágenes:   

    ```bash
    oc create configmap registry-config --from-file=<external-registry-address>=ca.crt -n openshift-config
    ```
    {: codeblock}

11. Edite el nuevo `registry-config`:

    ```bash
    oc edit image.config.openshift.io cluster
    ```
    {: codeblock}

12. Actualice la sección `spec:` con las líneas siguientes:

    ```bash
    spec:       additionalTrustedCA:        name: registry-config
    ```
    {: codeblock}

13. Construya la imagen con este formato de vía de acceso, por ejemplo:

   ```bash
   export BASE_IMAGE_NAME=myservice    docker build -t $OCP_DOCKER_HOST/$OCP_PROJECT/${BASE_IMAGE_NAME}_amd64:1.2.3 -f ./Dockerfile.amd64 .
   ```
   {: codeblock}

14. Como preparación para la publicación del servicio periférico, modifique el archivo **service.definition.json** de modo que la sección **deployment** correspondiente haga referencia a la vía de acceso del registro de imagen. Ahora puede crear los archivos de definición de servicio y de patrón de la manera siguiente:

   ```bash
   hzn dev service new -s $BASE_IMAGE_NAME -i $OCP_DOCKER_HOST/$OCP_PROJECT/$BASE_IMAGE_NAME
   ```
   {: codeblock}

   **&lt;base-image-name&gt;** debería ser el nombre de imagen base sin la arquitectura o la versión. A continuación puede editar las variables en el archivo **horizon/hzn.json** creado, según sea necesario.

   O, si ha creado su propio archivo de definición de servicio, asegúrese de que el campo **deployment.services.&lt;nombre-de-servicio&gt;.image** haga referencia a la vía de acceso de registro de imagen.

15. Cuando la imagen de servicio esté lista para publicarse, pulse la imagen en el registro de contenedor privado y publíquela en {{site.data.keyword.horizon}} Exchange.

   ```bash
   hzn exchange service publish -r "$OCP_DOCKER_HOST:$OCP_USER:$OCP_TOKEN" -f horizon/service.definition.json
   ```
   {: codeblock}

   El argumento **-r "$OCP_DOCKER_HOST:$OCP_USER:$OCP_TOKEN"** proporciona a los nodos periféricos de {{site.data.keyword.horizon_open}} las credenciales para poder extraer la imagen de servicio.

   El mandato lleva a cabo estas tareas:

   * Envía las imágenes de Docker al {{site.data.keyword.cloud_notm}} Container Registry y obtiene el resumen de la imagen en el proceso.
   * Firma el resumen y la información de despliegue con su clave privada.
   * Pone los metadatos de servicio (incluida la firma) en {{site.data.keyword.horizon}} Exchange.
   * Pone la clave pública en {{site.data.keyword.horizon}} Exchange bajo la definición de servicio para que los nodos periféricos de {{site.data.keyword.horizon}} puedan recuperar automáticamente la definición para verificar las firmas cuando sea necesario:
   * Pone al usuario y la señal de OpenShift en {{site.data.keyword.horizon}} Exchange bajo la definición de servicio para que los nodos periféricos de {{site.data.keyword.horizon}} puedan recuperar automáticamente las definiciones cuando sea necesario.
   
### Utilización del servicio en los nodos periféricos de {{site.data.keyword.horizon}}
{: #using_service}

Para permitir que los nodos periféricos extraigan las imágenes de servicio necesarias del registro de imágenes de {{site.data.keyword.ocp}}, debe configurar docker en cada nodo periférico para confiar en el certificado {{site.data.keyword.open_shift}}. Copie el archivo **ca.crt** en cada nodo periférico y, a continuación:

En {{site.data.keyword.linux_notm}}:

```bash
mkdir -p /etc/docker/certs.d/$OCP_DOCKER_HOST    cp ca.crt /etc/docker/certs.d/$OCP_DOCKER_HOST    systemctl restart docker.service
```
{: codeblock}

En {{site.data.keyword.macOS_notm}}:

```bash
mkdir -p ~/.docker/certs.d/$OCP_DOCKER_HOST    cp ca.crt ~/.docker/certs.d/$OCP_DOCKER_HOST
```
{: codeblock}

En {{site.data.keyword.macOS_notm}} reinicie Docker pulsando sobre el icono de ballena situado en el lado derecho de la barra de menús del escritorio y seleccionando **Reiniciar**.

Ahora {{site.data.keyword.horizon}} tiene todo lo que necesita para obtener esta imagen de servicio periférico del registro de imágenes de {{site.data.keyword.open_shift}} y desplegarlo en los nodos periféricos según se especifica en el patrón o la política de despliegue que ha creado.

## Utilización de {{site.data.keyword.cloud_notm}} Container Registry
{: #ibm_cloud_container_registry}

### Antes de empezar

* Instale la [herramienta CLI de {{site.data.keyword.cloud_notm}} (ibmcloud)](https://cloud.ibm.com/docs/cli?topic=cloud-cli-install-ibmcloud-cli).
* Asegúrese de tener nivel de acceso de **administrador de clúster** o **Administrador de equipo** en la cuenta de {{site.data.keyword.cloud_notm}}.

### Procedimiento

1. Inicie la sesión en {{site.data.keyword.cloud_notm}} y establezca su organización como destino:

   ```bash
   ibmcloud login -a cloud.ibm.com -u <nombre-de-usuario-de-Cloud> -p <contraseña-de-Cloud    ibmcloud target -o <ID-de-organización> -s <ID-de-espacio>
   ```
   {: codeblock}

   Si no conoce el ID de organización y el ID de espacio, puede iniciar la sesión en la [consola de{{site.data.keyword.cloud_notm}}](https://cloud.ibm.com/) para buscarlos o crearlos.

2. Cree una clave de API de Cloud:

   ```bash
   ibmcloud iam api-key-create <nombre-de-clave> -d "<descripción-de-clave>"
   ```
   {: codeblock}

   Guarde el valor de clave de API (visualizado en la línea que empieza por **API Key**) en un lugar seguro y establézcalo en esta variable de entorno:

   ```bash
   export CLOUD_API_KEY=<su-clave-de-API>
   ```
   {: codeblock}

   **Nota**: Esta clave de API es diferente de la clave de API de {{site.data.keyword.open_shift}} que ha creado para utilizar con el mandato `hzn`.

3. Obtenga el plug-in container-registry y cree su propio espacio de nombres de registro privado. (Este espacio de nombres de registro formará parte de la vía de acceso utilizada para identificar la imagen de Docker.)

   ```bash
   ibmcloud plugin install container-registry    export REGISTRY_NAMESPACE=<su-espacio-nombres-registro>    ibmcloud cr namespace-add $REGISTRY_NAMESPACE
   ```
   {: codeblock}

4. Inicie la sesión en el espacio de nombres de registro de Docker:

   ```bash
   ibmcloud cr login
   ```
   {: codeblock}

   Para obtener más información sobre cómo utilizar **ibmcloud cr**, consulte la [documentación web de CLI de ibmcloud cr](https://cloud.ibm.com/docs/services/Registry/). También puede ejecutar este mandato para ver información de ayuda:

   ```bash
   ibmcloud cr --help
   ```
   {: codeblock}

   Después de iniciar la sesión en el espacio de nombres privado en {{site.data.keyword.cloud_registry}} no es necesario que utilice `docker login` para iniciar la sesión en el registro. Puede utilizar vías de acceso de registro de contenedor parecidas a las siguientes dentro de los mandatos **docker push** y **docker pull**:

   ```bash
   us.icr.io/$REGISTRY_NAMESPACE/<nombre-de-imagen-base>_<arquitectura>:<versión>
   ```
   {: codeblock}

5. Construya la imagen con este formato de vía de acceso, por ejemplo:

   ```bash
   export BASE_IMAGE_NAME=myservice    docker build -t us.icr.io/$REGISTRY_NAMESPACE/${BASE_IMAGE_NAME}_amd64:1.2.3 -f ./Dockerfile.amd64 .
   ```
   {: codeblock}

6. Como preparación para la publicación del servicio periférico, modifique el archivo **service.definition.json** de modo que la sección **deployment** correspondiente haga referencia a la vía de acceso del registro de imagen. Ahora puede crear los archivos de definición de servicio y de patrón de la manera siguiente:

   ```bash
   hzn dev service new -s $BASE_IMAGE_NAME -i us.icr.io/$REGISTRY_NAMESPACE/$BASE_IMAGE_NAME
   ```
   {: codeblock}

   **&lt;base-image-name&gt;** debería ser el nombre de imagen base sin la arquitectura o la versión. A continuación puede editar las variables en el archivo **horizon/hzn.json** creado, según sea necesario.

   O, si ha creado su propio archivo de definición de servicio, asegúrese de que el campo **deployment.services.&lt;nombre-de-servicio&gt;.image** haga referencia a la vía de acceso de registro de imagen.

7. Cuando la imagen de servicio esté lista para publicarse, pulse la imagen en el registro de contenedor privado y publíquela en {{site.data.keyword.horizon}} Exchange.

   ```bash
   hzn exchange service publish -r "us.icr.io:iamapikey:$CLOUD_API_KEY" -f horizon/service.definition.json
   ```
   {: codeblock}

   El argumento **-r "us.icr.io:iamapikey:$CLOUD_API_KEY"** proporciona a los nodos periféricos de {{site.data.keyword.horizon_open}} las credenciales para poder extraer la imagen de servicio.

   El mandato lleva a cabo estas tareas:

   * Envía las imágenes de Docker al {{site.data.keyword.cloud_notm}} Container Registry y obtiene el resumen de la imagen en el proceso.
   * Firma el resumen y la información de despliegue con su clave privada.
   * Pone los metadatos de servicio (incluida la firma) en {{site.data.keyword.horizon}} Exchange.
   * Pone la clave pública en {{site.data.keyword.horizon}} Exchange bajo la definición de servicio para que los nodos periféricos de {{site.data.keyword.horizon}} puedan recuperar automáticamente la definición para verificar las firmas cuando sea necesario:
   * Pone la clave de API de {{site.data.keyword.cloud_notm}} en {{site.data.keyword.horizon}} bajo la definición de servicio para que los nodos periféricos de {{site.data.keyword.horizon}} puedan recuperar automáticamente la definición cuando sea necesario.

8. Verifique que la imagen de servicio se ha enviado a {{site.data.keyword.cloud_notm}} Container Registry:

   ```bash
   ibmcloud cr images
   ```
   {: codeblock}

9. Publique un patrón de despliegue o una política que desplegará el servicio en algunos nodos periféricos. Por ejemplo:

   ```bash
   hzn exchange pattern publish -f horizon/pattern.json
   ```
   {: codeblock}

Ahora {{site.data.keyword.horizon}} tiene todo lo que necesita para obtener esta imagen de servicio periférico de {{site.data.keyword.cloud_notm}} Container Registry y desplegarlo en nodos periféricos, como se especifica en el patrón o la política de despliegue que ha creado.
