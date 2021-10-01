---

copyright:
  years: 2019, 2020
lastupdated: "2020-02-13"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Utilización de CP4MCM con IEAM
{: #using_cp4mcm}

Siga estos pasos de instalación para configurar y habilitar el uso de {{site.data.keyword.edge_shared_notm}}. Esta instalación admite {{site.data.keyword.edge_servers_notm}} y {{site.data.keyword.edge_devices_notm}}.
{:shortdesc}

## Requisitos previos
{: #prereq}

Asegúrese de haber[dimensionado adecuadamente](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/servers/cluster_sizing.html) el clúster de {{site.data.keyword.icp_server_notm}}.

* Docker 1.13+
* [CLI cliente de OpenShift (oc) 4.2 ![Se abre en otro separador](../images/icons/launch-glyph.svg "Se abre en otro separador")](https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest-4.2/)

## Proceso de instalación

1. Descargue los paquetes **ibm-cp4mcm-core** y **ibm-ecm** para {{site.data.keyword.edge_servers_notm}} o {{site.data.keyword.edge_devices_notm}} de IBM Passport Advantage en el entorno de instalación, según qué producto haya comprado.

2. Prepare el directorio que se va a utilizar para la instalación y desempaquete el archivo zip de la licencia que se va a aceptar como parte de la instalación:

    ```
    mkdir -p /opt/ibm-multicloud-manager-1.2 && \
    tar -C /opt/ibm-multicloud-manager-1.2 -zxvf ibm-ecm-4.0.0-x86_64.tar.gz ibm-ecm-4.0.0-x86_64/ibm-ecm-licenses-4.0.zip
    ```
    {: codeblock}

3. Asegúrese de que el servicio Docker se está ejecutando y desempaquete/cargue las imágenes de Docker del archivo tar de instalación:

    ```
    tar -zvxf ibm-cp4mcm-core-1.2-x86_64.tar.gz -O | sudo docker load
    ```
    {: codeblock}

4. Prepare y efectúe la extración de la configuración de instalación:

    ```
    cd /opt/ibm-multicloud-manager-1.2 && \
    sudo docker run --rm -v $(pwd):/data:z -e LICENSE=accept -v $(pwd)/ibm-ecm-4.0.0-x86_64:/installer/cfc-files/license:z --security-opt label:disable ibmcom/mcm-inception-amd64:3.2.3 cp -r cluster /data
    ```
    {: codeblock}

5. Especifique una ubicación de KUBECONFIG nueva y **Cumplimente la información de clúster adecuada** en el mandato **oc login** que figura a continuación (obtenido de la instalación del clúster de OpenShift) y copie el archivo **$KUBECONFIG** en el directorio de configuración de la instalación:

    ```
    export KUBECONFIG=$(pwd)/myclusterconfig
    ```
    {: codeblock}

    ```
    oc login https://<API_ENDPOINT_HOST>:<PORT> -u <ADMIN_USER> -p <ADMIN_PASSWORD> --insecure-skip-tls-verify=true && \
    cp $KUBECONFIG /opt/ibm-multicloud-manager-1.2/cluster/kubeconfig && \
    cd cluster
    ```
    {: codeblock}

6. Actualice el archivo config.yaml:

  * Determine en qué nodos desea configurar la planificación de los servicios de {{site.data.keyword.edge_shared_notm}}. Se recomienda encarecidamente evitar el uso de los nodos **maestros**:

     ```
     # oc get nodes
     NAME               STATUS   ROLES    AGE  VERSION
     master0.test.com   Ready    master   8h   v1.14.6+c07e432da
     master1.test.com   Ready    master   8h   v1.14.6+c07e432da
     master2.test.com   Ready    master   8h   v1.14.6+c07e432da
     worker0.test.com   Ready    worker   8h   v1.14.6+c07e432da
     worker1.test.com   Ready    worker   8h   v1.14.6+c07e432da
     worker2.test.com   Ready    worker   8h   v1.14.6+c07e432da
     ```

     Dentro de cluster/config.yaml (**master** se refiere aquí a un conjunto de servicios específicos que forman parte de {{site.data.keyword.edge_servers_notm}} y **no** se refiere al rol de nodo **maestro**):

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

   * Elija la **storage_class** para datos persistentes:

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
**mycluster**. Si también va a instalar {{site.data.keyword.edge_devices_notm}}, este es un paso importante para dar un nombre adecuado al clúster. **cluster_name** se utilizará para definir varios componentes para ese producto.

7. Abra la ruta predeterminada en el registro de imágenes de OpenShift interno:

    ```
    oc patch configs.imageregistry.operator.openshift.io/cluster --type merge -p '{"spec":{"defaultRoute":true}}'
    ```
    {: codeblock}

8. Instale {{site.data.keyword.edge_shared_notm}}:

    ```
    sudo docker run -t --net=host -e LICENSE=accept -v $(pwd)/../ibm-ecm-4.0.0-x86_64:/installer/cfc-files/license:z -v $(pwd):/installer/cluster:z -v /var/run:/var/run:z -v /etc/docker:/etc/docker:z --security-opt label:disable ibmcom/mcm-inception-amd64:3.2.3 install-with-openshift
    ```
    {: codeblock}

<!--## Importing a cluster to be managed
There is a known issue with importing clusters, we are working on providing functional documentation steps for this process.

## Next steps
If this installation was done as part of a prerequisite for {{site.data.keyword.edge_devices_notm}}, [return to continue that installation](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/devices/installing/install.html).-->
