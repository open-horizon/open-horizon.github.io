---

copyright:
years: 2020
lastupdated: "2020-06-03"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Instalar Common Services

## Requisitos previos
{: #prereq}

### {{site.data.keyword.ocp_tm}}
Asegúrese de tener una instalación de {{site.data.keyword.open_shift_cp}} soportada y del
[tamaño apropiado](cluster_sizing.md). Incluyendo los servicios de registro y almacenamiento instalados y en funcionamiento en
el clúster. Para obtener más información sobre la instalación de
{{site.data.keyword.open_shift_cp}}, consulte la documentación de
{{site.data.keyword.open_shift}} para ver las versiones soportadas a continuación:

* [Documentación de {{site.data.keyword.open_shift_cp}} 4.3 ![Se abre en otro separador](../images/icons/launch-glyph.svg "Se abre en otro separador")](https://www.ibm.com/links?url=https%3A%2F%2Fdocs.openshift.com%2Fcontainer-platform%2F4.3%2Fwelcome%2Findex.html)
* [Documentación de {{site.data.keyword.open_shift_cp}} 4.4 ![Se abre en otro separador](../images/icons/launch-glyph.svg "Se abre en otro separador")](https://www.ibm.com/links?url=https%3A%2F%2Fdocs.openshift.com%2Fcontainer-platform%2F4.4%2Fwelcome%2Findex.html)

### Otros requisitos previos

* Docker 1.13+
* [CLI de cliente de {{site.data.keyword.open_shift}} (oc) 4.4 ![Se abre en otro separador](../images/icons/launch-glyph.svg "Se abre en otro separador")](https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest-4.4/)

## Proceso de instalación

1. [Descargue
el paquete deseado de IBM Passport Advantage](part_numbers.md) en el entorno de instalación
y desempaquete el soporte de instalación:
    ```
    tar -zxvf ibm-eam-{{site.data.keyword.semver}}-x86_64.tar.gz
    cd ibm-eam-{{site.data.keyword.semver}}-x86_64
    ```
    {: codeblock}

2. Prepare el directorio que va a utilizar la instalación y copie el archivo zip de licencia que
se debe aceptar como parte de la instalación:

    ```
    mkdir -p /opt/common-services-3.2.7/ibm-eam-{{site.data.keyword.semver}}-licenses && \
    cp ibm-eam-{{site.data.keyword.semver}}-licenses.zip /opt/common-services-3.2.7/ibm-eam-{{site.data.keyword.semver}}-licenses
    ```
    {: codeblock}

3. Asegúrese de que el servicio Docker se está ejecutando y desempaquete/cargue las imágenes de Docker del archivo tar de instalación:

    ```
    systemctl enable docker
    systemctl start docker
    tar -zvxf common-services-boeblingen-2004-x86_64.tar.gz -O | sudo docker load
    ```
    {: codeblock}

    **Nota:** pueden transcurrir unos minutos antes de que se muestre la salida
ya que está desempaquetando varias imágenes

4. Prepare y efectúe la extración de la configuración de instalación:

    ```
    cd /opt/common-services-3.2.7 && \
    sudo docker run --rm -v $(pwd):/data:z -e LICENSE=accept -v $(pwd)/ibm-eam-{{site.data.keyword.semver}}-licenses:/installer/cfc-files/license:z --security-opt label:disable ibmcom/icp-inception-amd64:3.2.7 cp -r cluster /data
    ```
    {: codeblock}

5. Establezca una nueva ubicación de KUBECONFIG y **rellene la información de clúster
adecuada** en el mandato **oc login** siguiente (obtenido de la instalación
de clúster de {{site.data.keyword.open_shift}}) y copie el archivo **$KUBECONFIG**
en el directorio de configuración de instalación:

    ```
    export KUBECONFIG=$(pwd)/myclusterconfig
    ```
    {: codeblock}

    ```
    oc login https://<API_ENDPOINT_HOST>:<PORT> -u <ADMIN_USER> -p <ADMIN_PASSWORD> --insecure-skip-tls-verify=true && \
    cp $KUBECONFIG $(pwd)/cluster/kubeconfig && \
    cd cluster
    ```
    {: codeblock}

6. Actualice el archivo config.yaml:

   * Determine en qué nodos desea configurar que se planifique
{{site.data.keyword.common_services}}, evitando utilizar los nodos **master**:

     ```
     # oc get nodes
     NAME               STATUS   ROLES    AGE  VERSION
     master0.test.com   Ready    master   8h   v1.17.1
     master1.test.com   Ready    master   8h   v1.17.1
     master2.test.com   Ready    master   8h   v1.17.1
     worker0.test.com   Ready    worker   8h   v1.17.1
     worker1.test.com   Ready    worker   8h   v1.17.1
     worker2.test.com   Ready    worker   8h   v1.17.1
    ```

     Dentro de cluster/config.yaml (**master** se refiere aquí a un conjunto de servicios específicos que forman parte de {{site.data.keyword.common_services}} y **no** se refiere al rol de nodo **maestro**):

     ```
     # A list of OpenShift nodes that used to run services components
     cluster_nodes:
       master:
         - worker0.test.com
       proxy:
         - worker0.test.com
       management:
         - worker0.test.com
     ```
     Nota: el valor de los parámetros maestro, proxy y de gestión es una matriz y puede tener varios nodos;
se puede utilizar el mismo nodo para cada parámetro. La configuración que figura más arriba es para una instalación **mínima**, para una instalación de **producción** incluya tres nodos de trabajador para cada parámetro.

   * Elija la **storage_class** preferida para los datos persistentes
para utilizar el almacenamiento dinámico:

     ```
     # oc get storageclass
     NAME                               PROVISIONER                     AGE
     rook-ceph-block-internal           rook-ceph.rbd.csi.ceph.com      8h
     rook-ceph-cephfs-internal          rook-ceph.cephfs.csi.ceph.com   8h
     rook-ceph-delete-bucket-internal   ceph.rook.io/bucket             8h
     ```

     Dentro de cluster/config.yaml:

     ```
     # Storage Class
storage_class: rook-ceph-cephfs-internal
     ```

     Consulte lo siguiente para conocer las [opciones de almacenamiento dinámico de {{site.data.keyword.open_shift}} soportadas e instrucciones de configuración ![Se abre en otro separador](../images/icons/launch-glyph.svg "Se abre en otro separador")](https://docs.openshift.com/container-platform/4.4/storage/understanding-persistent-storage.html)

   * Defina una contraseña **default_admin_password** alfanumérica de más de 32 caracteres o más:

     ```
     # default_admin_password:
     # password_rules:
     #   - '^([a-zA-Z0-9\-]{32,})$'
     default_admin_password: <SU-CONTRASEÑA-DE-ADMINISTRADOR-DE-32-CARACTERES-O-MÁS>
     ```

   * Añada una línea que defina **cluster_name** para identificar exclusivamente el clúster:

     ```
     cluster_name: <INSERTE_SU_NOMBRE_DE_CLÚSTER_EXCLUSIVO>
     ```

     Nota: Sin esta definición se elegirá un valor predeterminado del nombre
**mycluster**. Este es un paso importante para nombrar adecuadamente el clúster
ya que **nombre_clúster** se utilizará para definir varios componentes para
{{site.data.keyword.edge_notm}}

7. Abra la ruta predeterminada al registro de imágenes de {{site.data.keyword.open_shift}} interno:

    ```
    oc patch configs.imageregistry.operator.openshift.io/cluster --type merge -p '{"spec":{"defaultRoute":true}}'
    ```
    {: codeblock}

8. Instale {{site.data.keyword.common_services}}

    ```
    sudo docker run -t --net=host -e LICENSE=accept -v $(pwd)/../ibm-eam-{{site.data.keyword.semver}}-licenses:/installer/cfc-files/license:z -v $(pwd):/installer/cluster:z -v /var/run:/var/run:z -v /etc/docker:/etc/docker:z --security-opt label:disable ibmcom/icp-inception-amd64:3.2.7 install-with-openshift
    ```
    {: codeblock}
    **Nota:** El tiempo de instalación variará en función de las velocidades de red,
se espera que no se vea ninguna salida durante algún tiempo durante la tarea 'Carga de imágenes'.

Tome nota del URL de la salida de instalación porque se necesitará para el paso siguiente de
[Instalar {{site.data.keyword.ieam}}](offline_installation.md).
