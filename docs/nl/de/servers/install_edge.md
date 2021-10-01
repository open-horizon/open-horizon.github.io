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

# CP4MCM mit IEAM verwenden
{: #using_cp4mcm}

Führen Sie diese Installationsschritte aus, um die Verwendung von {{site.data.keyword.edge_shared_notm}} zu konfigurieren und zu aktivieren. Diese Installation unterstützt sowohl {{site.data.keyword.edge_servers_notm}} als auch {{site.data.keyword.edge_devices_notm}}.
{:shortdesc}

## Voraussetzungen
{: #prereq}

Stellen Sie sicher, dass Sie Ihren Cluster für {{site.data.keyword.icp_server_notm}} [angemessen dimensioniert](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/servers/cluster_sizing.html) haben.

* Docker 1.13+
* [OpenShift-Client-CLI (oc) 4.2 ![Wird in einer neuen Registerkarte geöffnet](../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest-4.2/)

## Installationsprozess

1. Laden Sie die Pakete **ibm-cp4mcm-core** und **ibm-ecm** für {{site.data.keyword.edge_servers_notm}} oder {{site.data.keyword.edge_devices_notm}} von IBM Passport Advantage auf Ihre Installationsumgebung herunter, je nachdem, welches Produkt gekauft wurde.

2. Bereiten Sie das Verzeichnis für die Verwendung durch die Installation vor und entpacken Sie die komprimierte Lizenzdatei, die als Teil der Installation akzeptiert werden soll:

    ```
    mkdir -p /opt/ibm-multicloud-manager-1.2 && \
    tar -C /opt/ibm-multicloud-manager-1.2 -zxvf ibm-ecm-4.0.0-x86_64.tar.gz ibm-ecm-4.0.0-x86_64/ibm-ecm-licenses-4.0.zip
    ```
    {: codeblock}

3. Stellen Sie sicher, dass der Docker-Service ausgeführt wird, und entpacken/laden Sie die Docker-Images aus der Installations-TAR-Datei:

    ```
    tar -zvxf ibm-cp4mcm-core-1.2-x86_64.tar.gz -O | sudo docker load
    ```
    {: codeblock}

4. Bereiten Sie die Installationskonfiguration vor und extrahieren Sie sie:

    ```
    cd /opt/ibm-multicloud-manager-1.2 && \
    sudo docker run --rm -v $(pwd):/data:z -e LICENSE=accept -v $(pwd)/ibm-ecm-4.0.0-x86_64:/installer/cfc-files/license:z --security-opt label:disable ibmcom/mcm-inception-amd64:3.2.3 cp -r cluster /data
    ```
    {: codeblock}

5. Geben Sie eine neue KUBECONFIG-Position an und **setzen Sie die entsprechenden Clusterinformationen** im nachstehenden Befehl **oc login** ein (die Sie aus der OpenShift-Clusterinstallation abgerufen haben). Kopieren Sie die Datei **$KUBECONFIG** in das Konfigurationsverzeichnis der Installation:

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

6. Aktualisieren Sie die Datei 'config.yaml':

  * Ermitteln Sie, welche Knoten so konfiguriert werden sollen, dass die {{site.data.keyword.edge_shared_notm}}-Services für sie terminiert werden können. Es wird dringend empfohlen, die Verwendung der **Master**-Knoten zu vermeiden:

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

     In der Datei 'cluster/config.yaml' (**Master** bezieht sich hier auf einen spezifischen Satz von Services, die Teil von {{site.data.keyword.edge_servers_notm}} sind, **nicht** auf die Rolle des **Master**-Knotens):

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
     Hinweis: Der Wert der Parameter Master, Proxy und Management ist ein Array, das mehrere Knoten haben kann; derselbe Knoten kann für jeden Parameter verwendet werden. Die oben genannte Konfiguration ist für die **Minimal**-Installation für eine **Produktions**-Installation und umfasst drei Workerknoten für jeden Parameter.

   * Wählen Sie Ihre bevorzugte Speicherklasse (**storage_class**) für persistente Daten aus:

     ```
     # oc get storageclass
     NAME                               PROVISIONER                     AGE
     rook-ceph-block-internal           rook-ceph.rbd.csi.ceph.com      8h
     rook-ceph-cephfs-internal          rook-ceph.cephfs.csi.ceph.com   8h
     rook-ceph-delete-bucket-internal   ceph.rook.io/bucket             8h
     ```

     In der Datei 'cluster/config.yaml':

     ```
# Storage Class
storage_class: rook-ceph-cephfs-internal
     ```

   * Definieren Sie ein aus mindestens 32 alphanumerischen Zeichen bestehendes Standardadministratorkennwort (**default_admin_password**):

     ```
     # default_admin_password:
     # password_rules:
     #   - '^([a-zA-Z0-9\-]{32,})$'
     default_admin_password: <YOUR-32-CHARACTER-OR-LONGER-ADMIN-PASSWORD>
     ```

   * Fügen Sie eine Zeile hinzu, die den Clusternamen **cluster_name** definiert, um den Cluster eindeutig zu identifizieren:

     ```
     cluster_name: <INSERT_YOUR_UNIQUE_CLUSTER_NAME>
     ```

     Hinweis: Ohne diese Definition wird ein Standardwert für den Namen von **mycluster** gewählt. Wenn Sie auch {{site.data.keyword.edge_devices_notm}} installieren, ist dies ein wichtiger Schritt, um Ihren Cluster angemessen zu benennen. Der Clustername **cluster_name** wird verwendet, um mehrere Komponenten für dieses Produkt zu definieren.

7. Öffnen Sie die Standardroute in die interne OpenShift-Image-Registry:

    ```
    oc patch configs.imageregistry.operator.openshift.io/cluster --type merge -p '{"spec":{"defaultRoute":true}}'
    ```
    {: codeblock}

8. Installieren Sie {{site.data.keyword.edge_shared_notm}}:

    ```
    sudo docker run -t --net=host -e LICENSE=accept -v $(pwd)/../ibm-ecm-4.0.0-x86_64:/installer/cfc-files/license:z -v $(pwd):/installer/cluster:z -v /var/run:/var/run:z -v /etc/docker:/etc/docker:z --security-opt label:disable ibmcom/mcm-inception-amd64:3.2.3 install-with-openshift
    ```
    {: codeblock}

<!--## Importing a cluster to be managed
There is a known issue with importing clusters, we are working on providing functional documentation steps for this process.

## Next steps
If this installation was done as part of a prerequisite for {{site.data.keyword.edge_devices_notm}}, [return to continue that installation](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/devices/installing/install.html).-->
