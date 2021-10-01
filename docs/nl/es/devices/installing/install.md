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

# Instalación del centro de gestión
{: #hub_install_overview}
 
Debe instalar y configurar un centro de gestión antes de pasar a las tareas de nodo de {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}).

{{site.data.keyword.ieam}} ofrece funciones de computación periférica
para ayudarle a gestionar y desplegar cargas de trabajo de un clúster de hub en
instancias remotas de OpenShift ® Container Platform 4.2 u otros clústeres basados en Kubernetes.

{{site.data.keyword.ieam}} utiliza IBM Multicloud Management Core 1.2 para controlar el despliegue
de cargas de trabajo contenerizadas en los servidores, las pasarelas y los dispositivos periféricos
alojados por los clústeres de OpenShift® Container Platform 4.2 en ubicaciones remotas.

Además, {{site.data.keyword.ieam}} incluye soporte para un perfil de gestor
de computación periférica. Este perfil soportado
puede ayudarle a reducir el uso de recursos de OpenShift® Container Platform 4.2 cuando se instala
OpenShift® Container Platform 4.2 para utilizarlo en el alojamiento de un servidor periférico
remoto. Este perfil coloca los servicios mínimos que se necesitan para dar soporte a una gestión remota robusta de estos entornos de servidor y a las aplicaciones críticas de empresa que se alojan allí. Con este perfil, todavía puede autenticar usuarios, recopilar datos de registro y de sucesos y desplegar cargas de trabajo en un único nodo o en un conjunto de nodos de trabajador en clúster.

# Instalación del centro de gestión

El proceso de instalación de {{site.data.keyword.edge_notm}} le lleva a través de los pasos de instalación y configuración de nivel alto siguientes:
{:shortdesc}

  - [Resumen de la instalación](#sum)
  - [Dimensionamiento](#size)
  - [Requisitos previos](#prereq)
  - [Proceso de instalación](#process)
  - [Configuración posterior a la instalación](#postconfig)
  - [Recopilar la información y los archivos necesarios](#prereq_horizon)
  - [Desinstalación](#uninstall)

## Resumen de la instalación
{: #sum}

* Despliegue los siguientes componentes de centro de gestión:
  * API de Exchange de {{site.data.keyword.edge_devices_notm}}.
  * Agbot de {{site.data.keyword.edge_devices_notm}}.
  * CSS (servicio de sincronización de nube) de {{site.data.keyword.edge_devices_notm}}.
  * Interfaz de usuario de {{site.data.keyword.edge_devices_notm}}.
* Verifique que la instalación ha sido satisfactoria.
* Rellene los servicios periféricos de ejemplo.

## Dimensionamiento
{: #size}

Esta información de dimensionamiento es para {{site.data.keyword.edge_notm}} sólo servicios y está por encima y más allá de las recomendaciones de dimensionamiento para {{site.data.keyword.edge_shared_notm}} que puede encontrar [documentadas aquí](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/servers/cluster_sizing.html).

### Requisitos de almacenamiento de la base de datos

* PostgreSQL Exchange
  * Valor predeterminado de 10 GB
* PostgreSQL AgBot
  * Valor predeterminado de 10 GB  
* MongoDB Cloud Sync Service
  * Valor predeterminado de 50 GB

### Requisitos de cálculo

Los servicios que optimizan los [recursos de cálculo de Kubernetes](https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container) se planificarán entre los nodos de trabajador disponibles. Se recomienda un mínimo de tres nodos de trabajador.

* Estos cambios de configuración darán soporte a 10.000 dispositivos periféricos como máximo:

  ```
  exchange:
    replicaCount: 5
    dbPool: 18
    cache:
      idsMaxSize: 11000
    resources:
      limits:
        cpu: 5
  ```

  Nota: las instrucciones para realizar estos cambios se describen en la sección
**Configuración avanzada** en el archivo [README.md](README.md).

* La configuración predeterminada soporta un máximo de 4.000 dispositivos periféricos y
los totales de gráficas para los recursos de cálculo predeterminados son:

  * Solicitudes
     * Menos de 5 GB de RAM
     * Menos de 1 CPU
  * Límites
     * 18 GB de RAM
     * 18 CPU


## Requisitos previos
{: #prereq}

* Instale [{{site.data.keyword.edge_shared_notm}}](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/servers/install_edge.html)
* **Un host {{site.data.keyword.linux_notm}} macOS o Ubuntu**
* [CLI cliente de OpenShift (oc) 4.2 ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest-4.2/)
* **jq** [Download ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://stedolan.github.io/jq/download/)
* **git**
* **docker** 1.13+
* **make**
* Las CLI siguientes, que se pueden obtener en la instalación de clúster de {{site.data.keyword.mgmt_hub}} en `https://<CLUSTER_URL_HOST>/common-nav/cli`

    Nota: Es posible que tenga que ir a al URL anterior dos veces porque el acceso no autenticado vuelve
a dirigir la navegación a una página de bienvenida

  * CLI de Kubernetes (**kubectl**)
  * CLI de Helm (**helm**)
  * CLI de IBM Cloud Pak (**cloudctl**)

Nota: de forma predeterminada, las bases de datos de desarrollo locales se suministran
como parte de la instalación de gráfica. Consulte el archivo [README.md](README.md) para obtener instrucciones sobre el suministro de sus propias bases de datos. El usuario es responsable de realizar una copia de seguridad o de restaurar las bases de datos.

## Proceso de instalación
{: #process}

1. Establezca la variable de entorno **CLUSTER_URL**, este valor se puede obtener de la salida de la instalación de {{site.data.keyword.mgmt_hub}}:

    ```
    export CLUSTER_URL=<URL_DE_CLÚSTER>
    ```
    {: codeblock}

    De forma alternativa, después de conectar con el clúster con **oc login**, puede ejecutar:

    ```
    export CLUSTER_URL=https://$(oc get routes icp-console -o jsonpath='{.spec.host}' -n kube-system)
    ```
    {: codeblock}

2. Conéctese al clúster con privilegios de administrador de clúster, seleccionando **kube-system** como espacio de nombres y **cumplimente la contraseña** que ha definido en config.yaml durante la instalación de {{site.data.keyword.mgmt_hub}}:

    ```
    cloudctl login -a $CLUSTER_URL -u admin -p <su-contraseña-de-administrador-de-icp> -n kube-system --skip-ssl-validation
    ```
    {: codeblock}

3. Defina el host de registro de imagen, configure la CLI de Docker para que confíe en el certificado autofirmado:

    ```
    export REGISTRY_HOST=$(oc get routes -n openshift-image-registry default-route -o jsonpath='{.spec.host}')

    ```
    {: codeblock}

   Para macOS:

      1. Confíe en el certificado

      ```
      mkdir -p ~/.docker/certs.d/$REGISTRY_HOST && \
      echo | openssl s_client -showcerts -connect $REGISTRY_HOST:443 2>/dev/null | openssl x509 -outform PEM > ~/.docker/certs.d/$REGISTRY_HOST/ca.crt && \
      sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain ~/.docker/certs.d/$REGISTRY_HOST/ca.crt

      ```
      {: codeblock}
      
      2. Reinicie el servicio Docker desde la barra de menús

   Para Ubuntu:

      1. Confíe en el certificado

      ```
      mkdir /etc/docker/certs.d/$REGISTRY_HOST && \
      echo | openssl s_client -showcerts -connect $REGISTRY_HOST:443 2>/dev/null | openssl x509 -outform PEM > /etc/docker/certs.d/$REGISTRY_HOST/ca.crt && \
      service docker restart

      ```
      {: codeblock}

4. Inicie la sesión en el registro de imagen de {{site.data.keyword.open_shift_cp}}:

      ```
      docker login $REGISTRY_HOST -u $(oc whoami) -p $(oc whoami -t)
      ```
      {: codeblock}

5. Desempaquete el archivo comprimido de instalación de {{site.data.keyword.edge_devices_notm}} descargado de IBM Passport Advantage:

    ```
    tar -zxvf ibm-ecm-4.1.0-x86_64.tar.gz && \
    cd ibm-ecm-4.1.0-x86_64
    ```
    {: codeblock}

6. Cargue el contenido del archivador en el catálogo y las imágenes en el espacio de nombres ibmcom del registro:

    ```
    cloudctl catalog load-archive --archive ibm-ecm-prod-catalog-archive-4.1.0.tgz --registry $REGISTRY_HOST/ibmcom
    ```
    {: codeblock}

  Nota: {{site.data.keyword.edge_devices_notm}} sólo soporta una instalación controlada por CLI;
la instalación desde el catálogo no está soportada para este release.

7. Extraiga el contenido del archivo comprimido de gráfico en el directorio actual y muévalo al
directorio creado:

    ```
    tar -O -zxvf ibm-ecm-prod-catalog-archive-4.1.0.tgz charts/ibm-ecm-prod-4.1.0.tgz | tar -zxvf - && \
    cd ibm-ecm-prod
    ```
    {: codeblock}

8. Defina una clase de almacenamiento predeterminada si es que no se ha establecido una:

   ```
   # oc get storageclass
   NAME                                 PROVISIONER                     AGE
   rook-ceph-block-internal             rook-ceph.rbd.csi.ceph.com      8h
   rook-ceph-cephfs-internal (default)  rook-ceph.cephfs.csi.ceph.com   8h
   rook-ceph-delete-bucket-internal     ceph.rook.io/bucket             8h
   ```
   
   Si no ve una línea con la serie **(default)** más arriba, etiquete el almacenamiento predeterminado preferido con:

   ```
   oc patch storageclass <NOMBRE_DE_CLASE_DE_ALMACENAMIENTO_PREDETERMINADO_PREFERIDO> -p '{"metadata": {"annotations": {"storageclass.kubernetes.io/is-default-class": "true"}}}'
   ```
   {: codeblock}

9. Lea y tome en consideración las opciones de configuración y a continuación siga la sección **Instalación de la gráfica** del archivo [README.md](README.md).

  El script instala los componentes de centro de gestión mencionados en la sección
**Resumen de instalación** anterior, ejecuta la verificación de instalación y,
a continuación, vuelve a hacer referencia a la sección **Configuración posterior a la instalación**
siguiente.

## Configuración posterior a la instalación
{: #postconfig}

Ejecute los mandatos siguientes desde el mismo host en el que ha ejecutado la instalación inicial:

1. Consulte los pasos 1 y 2 de la sección **Proceso de instalación** que figura más arriba para iniciar la sesión en el clúster
2. Instale la CLI de **hzn** con los instaladores de paquete Ubuntu {{site.data.keyword.linux_notm}} o macOS que se encuentran en **horizonon-edge-packages** en el directorio OS/ARCH adecuado del contenido comprimido extraído en el paso 5 del [Proceso de instalación](#process) que figura más arriba:
  * Ejemplo de Ubuntu {{site.data.keyword.linux_notm}}:

    ```
    sudo dpkg -i horizon-edge-packages/linux/ubuntu/bionic/amd64/horizon-cli*.deb
    ```
    {: codeblock}

  * Ejemplo de macOS:

    ```
    sudo installer -pkg horizon-edge-packages/macos/horizon-cli-*.pkg -target /
    ```
    {: codeblock}

3. Exporte las variables siguientes que son necesarias para los pasos siguientes:

    ```
    export EXCHANGE_ROOT_PASS=$(oc -n kube-system get secret edge-computing -o jsonpath="{.data.exchange-config}" | base64 --decode | jq -r .api.root.password)
    export HZN_EXCHANGE_URL=https://$(oc get routes icp-console -o jsonpath='{.spec.host}' -n kube-system)/ec-exchange/v1
    export HZN_EXCHANGE_USER_AUTH="root/root:$EXCHANGE_ROOT_PASS"
    export HZN_ORG_ID=IBM
    ```
    {: codeblock}

4. Confíe en la entidad emisora de certificados de {{site.data.keyword.open_shift_cp}}:
    ```
    oc --namespace kube-system get secret cluster-ca-cert -o jsonpath="{.data['tls\.crt']}" | base64 --decode > /tmp/icp-ca.crt
    ```
    {: codeblock}

  * Ejemplo de Ubuntu {{site.data.keyword.linux_notm}}:
     ```
     sudo cp /tmp/icp-ca.crt /usr/local/share/ca-certificates &&sudo update-ca-certificates
     ```
    {: codeblock}

  * Ejemplo de macOS:

    ```
    sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain /tmp/icp-ca.crt
    ```
    {: codeblock}

5. Cree un par de claves de firma. Para obtener más información, consulte el Paso 5 en [Preparación para crear un servicio periférico](../developing/service_containers.md).
    ```
    hzn key create <nombre_empresa> <correo_electrónico@propietario>
    ```
    {: codeblock}

6. Confirme que la configuración se puede comunicar con la API de {{site.data.keyword.edge_devices_notm}} Exchange:
    ```
    hzn exchange status
    ```
    {: codeblock}

7. Llene los servicios periféricos de ejemplo:

    ```
    curl https://raw.githubusercontent.com/open-horizon/examples/v4.1/tools/exchangePublishScript.sh | bash -s -- -c $(oc get -n kube-public configmap -o jsonpath="{.items[]..data.cluster_name}")
    ```
    {: codeblock}

8. Ejecute los mandatos siguientes para ver algunos de los servicios y políticas que se han creado en {{site.data.keyword.edge_devices_notm}} Exchange:

    ```
    hzn exchange service list IBM/
    hzn exchange pattern list IBM/
    hzn exchange service listpolicy
    ```
    {: codeblock}

9. Si aún no se ha configurado, cree una conexión LDAP utilizando la consola de gestión de {{site.data.keyword.open_shift_cp}}. Después de establecer una conexión LDAP, cree un equipo, otorgue a ese equipo acceso a cualquier espacio de nombres y añada usuarios a ese equipo. Esto otorga a los usuarios individuales el permiso para crear claves de API.

  Nota: las claves de API se utilizan para la autenticación con la CLI de
{{site.data.keyword.edge_devices_notm}}. Para obtener más información acerca de LDAP, consulte [Configuración de la conexión de LDAP ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://www.ibm.com/support/knowledgecenter/SSFC4F_1.2.0/iam/3.4.0/configure_ldap.html).


## Recopilar la información y los archivos necesarios para dispositivos periféricos
{: #prereq_horizon}

Se necesitarán algunos archivos para instalar el agente de {{site.data.keyword.edge_devices_notm}} en los dispositivos periféricos y registrarlos con {{site.data.keyword.edge_devices_notm}}. Esta sección le guiará a través de la recopilación de estos archivos en un archivo tar, que luego se puede utilizar en cada uno de los dispositivos periféricos.

Se supone que ya ha instalado los mandatos
**cloudctl** y **kubectl** y ha extraído
**ibm-edge-computing-4.1.0-x86_64.tar.gz** del contenido de instalación,
tal como se ha descrito anteriormente en esta página.

1. Consulte los pasos 1 y 2 en la sección **Proceso de instalación** para establecer las variables de entorno siguientes:

   ```
   export CLUSTER_URL=<url-clúster>
   export CLUSTER_USER=<su-usuario-admin-icp>
   export CLUSTER_PW=<su-contraseña-admin-icp>
   ```
   {: codeblock}

2. Descargue la versión más reciente de **edgeDeviceFiles.sh**:

   ```
   curl -O https://raw.githubusercontent.com/open-horizon/examples/v4.0/tools/edgeDeviceFiles.sh
   chmod +x edgeDeviceFiles.sh
   ```
   {: codeblock}

3. Ejecute el script **edgeDeviceFiles.sh** para recopilar los archivos necesarios:

   ```
   ./edgeDeviceFiles.sh <tipo-de-dispositivo-periférico> -t
   ```
   {: codeblock}

   Argumentos del mandato:
   * Valores de **<tipo-de-dispositivo-periférico>** soportados: **32-bit-ARM** , **64-bit-ARM**, **x86_64-{{site.data.keyword.linux_notm}}** o **{{site.data.keyword.macOS_notm}}**
   * **-t**: crear un archivo **agentInstallFiles-&lt;tipo-de-dispositivo-periférico&gt;.tar.gz** que contenga todos los archivos recopilados. Si este distintivo no se ha establecido, los archivos recopilados se colocan en el directorio actual.
   * **-k**: crear una clave de API nueva llamada **$USER-Edge-Device-API-Key**. Si este distintivo no está establecido, se busca una clave llamada **$USER-Edge-Device-API-Key** entre las claves de API existentes y la creación se omite si la clave ya existe.
   * **-d** **<distribución>**: cuando se instala en **64-bit-ARM** o **x86_64-Linux**, puede especificar **-d xenial** para la versión más antigua de Ubuntu, en lugar del valor predeterminado bionic. Cuando se instala en **32-bit-ARM** puede especificar **-d stretch** en lugar del buster predeterminado. El distintivo -d se pasa por alto con macOS.
   * **-f** **<directorio>**: especifique un directorio al que mover los archivos recopilados. Si el directorio no existe, se creará. El valor predeterminado es el directorio actual

4. El mandato en el paso anterior creará un archivo llamado **agentInstallFiles-&lt;tipo-de-dispositivo-periférico&gt;.tar.gz**. Si tiene tipos adicionales de dispositivos periféricos (arquitecturas diferentes), repita el paso anterior para cada tipo.

5. Tome nota de la clave de API que se ha creado y que se visualiza mediante el mandato **edgeDeviceFiles.sh**.

6. Ahora que ha iniciado la sesión a través de **cloudctl**, si necesita crear claves de API adicionales para que los usuarios las utilicen con el mandato **hzn** de {{site.data.keyword.horizon}}:

   ```
   cloudctl iam api-key-create "<elija-un-nombre-de-clave-de-API>" -d "<elija-una-descripción-de-clave-de-API>"
   ```
   {: codeblock}

   En la salida del mandato, busque el valor de la clave en la línea que empieza con **API Key** y guarde el valor de la clave para un uso futuro.

7. Cuando esté preparado para configurar los dispositivos periféricos, siga [Cómo empezar a utilizar {{site.data.keyword.edge_devices_notm}}](../getting_started/getting_started.md).

## Desinstalación
{: #uninstall}

Nota: de forma predeterminada, se configuran **bases de datos locales**, en esta caso
la desinstalación suprime TODOS los datos persistentes. Asegúrese de que ha realizado copias de seguridad de
todos los datos persistentes necesarios (las instrucciones de copia de seguridad se documentan en el README)
antes de ejecutar el script uninstal. Si ha configurado **bases de datos remotas**, dichos
datos no se suprimen durante una desinstalación y deberá eliminarlos manualmente si es necesario.

Vuelva a la ubicación de la gráfica desempaquetado como parte de la instalación y ejecute el script de desinstalación proporcionado. Este script desinstalará el release helm y todos los recursos asociados. En primer lugar, inicie la sesión en el clúster como administrador de clúster mediante **cloudctl** y a continuación ejecute:

```
ibm_cloud_pak/pak_extensions/uninstall/uninstall-edge-computing.sh <nombre-clúster>
```
{: codeblock}
