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

# Common Services installieren

## Voraussetzungen
{: #prereq}

### {{site.data.keyword.ocp_tm}}
Stellen Sie sicher, dass Sie über eine [für Ihre Anforderungen ausreichend dimensionierte](cluster_sizing.md) und unterstützte {{site.data.keyword.open_shift_cp}}-Installation verfügen, die auch für die Registry und die Speicherservices ausgelegt ist, die in Ihrem Cluster ausgeführt werden. Weitere Informationen zur Installation von {{site.data.keyword.open_shift_cp}} finden Sie in der {{site.data.keyword.open_shift}}-Dokumentation zu den folgenden unterstützten Versionen:

* [Dokumentation zu {{site.data.keyword.open_shift_cp}} 4.3 ![Wird auf einer neuen Registerkarte geöffnet](../images/icons/launch-glyph.svg "Wird auf einer neuen Registerkarte geöffnet")](https://www.ibm.com/links?url=https%3A%2F%2Fdocs.openshift.com%2Fcontainer-platform%2F4.3%2Fwelcome%2Findex.html)
* [Dokumentation zu {{site.data.keyword.open_shift_cp}} 4.4 ![Wird auf einer neuen Registerkarte geöffnet](../images/icons/launch-glyph.svg "Wird auf einer neuen Registerkarte geöffnet")](https://www.ibm.com/links?url=https%3A%2F%2Fdocs.openshift.com%2Fcontainer-platform%2F4.4%2Fwelcome%2Findex.html)

### Weitere Voraussetzungen

* Docker 1.13+
* [{{site.data.keyword.open_shift}}-Client-CLI (oc) 4.4 ![Wird auf einer neuen Registerkarte geöffnet](../images/icons/launch-glyph.svg "Wird auf einer neuen Registerkarte geöffnet")](https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest-4.4/)

## Installationsprozess

1. Laden Sie das gewünschte [Paket von IBM Passport Advantage](part_numbers.md) in Ihre Installationsumgebung herunter und entpacken Sie die Installationsmedien:
    ```
    tar -zxvf ibm-eam-{{site.data.keyword.semver}}-x86_64.tar.gz
    cd ibm-eam-{{site.data.keyword.semver}}-x86_64
    ```
    {: codeblock}

2. Bereiten Sie das für die Installation vorgesehene Verzeichnis vor und kopieren Sie die komprimierte Lizenzdatei mit den Lizenzbestimmungen, die im Rahmen der Installation zu akzeptieren sind:

    ```
    mkdir -p /opt/common-services-3.2.7/ibm-eam-{{site.data.keyword.semver}}-licenses && \
    cp ibm-eam-{{site.data.keyword.semver}}-licenses.zip /opt/common-services-3.2.7/ibm-eam-{{site.data.keyword.semver}}-licenses
    ```
    {: codeblock}

3. Stellen Sie sicher, dass der Docker-Service ausgeführt wird, und entpacken/laden Sie die Docker-Images aus der Installations-TAR-Datei:

    ```
    systemctl enable docker
    systemctl start docker
    tar -zvxf common-services-boeblingen-2004-x86_64.tar.gz -O | sudo docker load
    ```
    {: codeblock}

    **Hinweis:** Es kann einige Minuten dauern, bis die Ausgabe angezeigt wird, da mehrere Images entpackt werden.

4. Bereiten Sie die Installationskonfiguration vor und extrahieren Sie sie:

    ```
    cd /opt/common-services-3.2.7 && \
    sudo docker run --rm -v $(pwd):/data:z -e LICENSE=accept -v $(pwd)/ibm-eam-{{site.data.keyword.semver}}-licenses:/installer/cfc-files/license:z --security-opt label:disable ibmcom/icp-inception-amd64:3.2.7 cp -r cluster /data
    ```
    {: codeblock}

5. Legen Sie eine neue KUBECONFIG-Position fest und **setzen Sie die entsprechenden Clusterinformationen** (bekannt aus der Ausgabe zur {{site.data.keyword.open_shift}}-Clusterinstallation) im nachstehenden Befehl **oc login** ein. Kopieren Sie die Datei **$KUBECONFIG** in das Konfigurationsverzeichnis der Installation:

    ```
    export KUBECONFIG=$(pwd)/myclusterconfig
    ```
    {: codeblock}

    ```
    oc login https://<API-ENDPUNKT-HOST>:<PORT> -u <ADMIN-BENUTZER> -p <ADMIN-KENNWORT> --insecure-skip-tls-verify=true && \
    cp $KUBECONFIG $(pwd)/cluster/kubeconfig && \
    cd cluster
    ```
    {: codeblock}

6. Aktualisieren Sie die Datei 'config.yaml':

   * Legen Sie die Knoten fest, für deren Planung {{site.data.keyword.common_services}} konfiguriert werden soll. Vermeiden Sie dabei die Verwendung der **Masterknoten**.

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

     In der Datei 'cluster/config.yaml' (**Master** bezieht sich hier auf einen spezifischen Satz von Services, die Teil von {{site.data.keyword.common_services}} sind, **nicht** auf die Rolle **Master** für einen Knoten):

     ```
     # Eine Liste von OpenShift-Knoten für die Ausführung von Servicekomponenten
     cluster_nodes:
       master:
         - worker0.test.com
       proxy:
         - worker0.test.com
       management:
         - worker0.test.com
     ```
     Hinweis: Der Wert der Parameter 'master', 'proxy' und 'management' ist ein Array, das mehrere Knoten beinhalten kann. Für jeden einzelnen Parameter kann derselbe Knoten verwendet werden. Die zuvor angegebene Konfiguration ist für die **Minimal**installation für eine **Produktion**sumgebung vorgesehen und umfasst drei Workerknoten für jeden Parameter.

   * Wählen Sie Ihre bevorzugte Speicherklasse (**storage_class**) für persistente Daten aus, um dynamischen Speicher zu nutzen:

     ```
     # oc get storageclass
     NAME                               PROVISIONER                     AGE
     rook-ceph-block-internal           rook-ceph.rbd.csi.ceph.com      8h
     rook-ceph-cephfs-internal          rook-ceph.cephfs.csi.ceph.com   8h
     rook-ceph-delete-bucket-internal   ceph.rook.io/bucket             8h
     ```

     In der Datei 'cluster/config.yaml':

     ```
# Speicherklasse
storage_class: rook-ceph-cephfs-internal
     ```

     Informieren Sie sich über [unterstützte {{site.data.keyword.open_shift}}-Optionen für dynamischen Speicher und Konfigurationsanweisungen![Wird auf einer neuen Registerkarte geöffnet](../images/icons/launch-glyph.svg "Wird auf einer neuen Registerkarte geöffnet")](https://docs.openshift.com/container-platform/4.4/storage/understanding-persistent-storage.html).

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

     Hinweis: Ohne diese Definition wird ein Standardwert für den Namen von **mycluster** gewählt. Verwenden Sie unbedingt einen geeigneten Namen für Ihren Cluster. Der Clustername (**clustername**) wird für die Definition mehrerer Komponenten in {{site.data.keyword.edge_notm}} verwendet.

7. Öffnen Sie die Standardroute in die interne {{site.data.keyword.open_shift}}-Image-Registry:

    ```
    oc patch configs.imageregistry.operator.openshift.io/cluster --type merge -p '{"spec":{"defaultRoute":true}}'
    ```
    {: codeblock}

8. Installieren Sie {{site.data.keyword.common_services}}:

    ```
    sudo docker run -t --net=host -e LICENSE=accept -v $(pwd)/../ibm-eam-{{site.data.keyword.semver}}-licenses:/installer/cfc-files/license:z -v $(pwd):/installer/cluster:z -v /var/run:/var/run:z -v /etc/docker:/etc/docker:z --security-opt label:disable ibmcom/icp-inception-amd64:3.2.7 install-with-openshift
    ```
    {: codeblock}
    **Hinweis:** Die Installationszeit hängt von der Netzgeschwindigkeit ab. Voraussichtlich ist bei der Task zum Laden von Images für eine gewisse Zeit keine Ausgabe zu sehen.

Notieren Sie sich die URL aus der Installationsausgabe. Diese URL wird für den nächsten Schritt, die [Installation von {{site.data.keyword.ieam}}](offline_installation.md), benötigt.
