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

# Management-Hub installieren
{: #hub_install_overview}
 
Bevor Sie die Knotentasks von {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) ausführen können, müssen Sie zunächst einen Management-Hub installieren und konfigurieren.

{{site.data.keyword.ieam}} stellt Edge-Computing-Funktionen bereit, um Ihnen das Management und die Bereitstellung von Workloads über einen Hub-Cluster auf fernen Instanzen von OpenShift® Container Platform 4.2 oder anderen auf Kubernetes basierenden Clustern zu ermöglichen.

{{site.data.keyword.ieam}} verwendet IBM Multicloud Management Core 1.2, um die Bereitstellung containerisierter Workloads auf Edge-Servern, Gateways und anderen Einheiten zu kontrollieren, die von Clustern mit OpenShift® Container Platform 4.2 an fernen Standorten gehostet werden.

{{site.data.keyword.ieam}} beinhaltet darüber hinaus eine Unterstützung für ein Edge-Computing-Managerprofil. Dieses unterstützte Profil kann Sie bei der Reduzierung der Ressourcennutzung von OpenShift® Container Platform 4.2 unterstützen, wenn OpenShift® Container Platform 4.2 zum Hosting eines fernen Edge-Servers installiert wird. Dieses Profil stellt die mindestens erforderlichen Services zur Unterstützung einer robusten fernen Managementlösung für diese Serverumgebungen und die unternehmenskritischen Anwendungen bereit, die von Ihnen an den entsprechenden Standorten gehostet werden. Mit diesem Profil können Sie weiterhin Benutzer authentifizieren, Protokoll- und Ereignisdaten erfassen und Workloads auf einem einfachen Workerknoten oder in einer Gruppe von Cluster-Workerknoten bereitstellen.

# Management-Hub installieren

Der {{site.data.keyword.edge_notm}}-Installationsprozess führt Sie durch die folgenden allgemeinen Installations- und Konfigurationsschritte.
{:shortdesc}

  - [Installationszusammenfassung](#sum)
  - [Dimensionierung](#size)
  - [Voraussetzungen](#prereq)
  - [Installationsprozess](#process)
  - [Konfiguration nach der Installation](#postconfig)
  - [Erforderliche Informationen und Dateien zusammenstellen](#prereq_horizon)
  - [Deinstallation durchführen](#uninstall)

## Installationszusammenfassung
{: #sum}

* Stellen Sie die folgenden Management-Hub-Komponenten bereit:
  * Exchange-API für {{site.data.keyword.edge_devices_notm}} 
  * Agbot für {{site.data.keyword.edge_devices_notm}} 
  * Cloud Sync Service (CSS) für {{site.data.keyword.edge_devices_notm}} 
  * {{site.data.keyword.edge_devices_notm}}-Benutzerschnittstelle 
* Überprüfen Sie, ob die Installation erfolgreich verlaufen ist. 
* Füllen Sie die Edge-Beispielservices mit Daten. 

## Dimensionierung
{: #size}

Diese Informationen zur Dimensionierung beziehen sich nur auf {{site.data.keyword.edge_notm}}-Services und gehen über die Dimensionierungsempfehlungen für {{site.data.keyword.edge_shared_notm}} hinaus, die Sie [hier dokumentiert](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/servers/cluster_sizing.html) finden.

### Anforderungen an die Datenbankspeicherung

* PostgreSQL Exchange
  * 10 GB Standard
* PostgreSQL AgBot
  * 10 GB Standard  
* MongoDB Cloud Sync Service
  * 50 GB Standard

### Rechenanforderungen

Die Services, die [Kubernetes-Rechenressourcen](https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container) nutzen, werden über die verfügbaren Workerknoten aufgeteilt. Es werden mindestens drei Workerknoten empfohlen.

* Diese Konfigurationsänderung unterstützen bis zu 10.000 Edge-Einheiten:

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

  Hinweis: Anweisungen für diese Änderungen werden im Abschnitt **Erweiterte Konfiguration** in der [README.md](README.md)-Datei beschrieben.

* Die Standardkonfiguration unterstützt bis zu 4000 Edge-Einheiten. Die Gesamtzahlen für die standardmäßigen Rechenressourcen sind wie folgt:

  * Anforderungen
     * Weniger als 5 GB RAM
     * Weniger als 1 CPU
  * Grenzwerte
     * 18 GB RAM
     * 18 CPUs


## Voraussetzungen
{: #prereq}

* Installieren Sie [{{site.data.keyword.edge_shared_notm}}](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/servers/install_edge.html)
* **Ein macOS- oder Ubuntu {{site.data.keyword.linux_notm}}-Host** 
* [OpenShift-Client-CLI (oc) 4.2 ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest-4.2/)
* **jq** [Laden Sie ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet") herunter](https://stedolan.github.io/jq/download/)
* **git**
* **Docker** 1.13+
* **make**
* Die folgenden CLIs, die von Ihrer {{site.data.keyword.mgmt_hub}}-Clusterinstallation unter `https://<CLUSTER_URL_HOST>/common-nav/cli` abgerufen werden können

    Hinweis: Möglicherweise müssen Sie die oben aufgeführte URL zweimal aufrufen, da die Navigation bei einem nicht authentifizierten Zugriff an eine Begrüßungsseite umgeleitet wird.

  * Kubernetes-CLI (**kubectl**)
  * Helm-CLI (**helm**)
  * IBM Cloud Pak-CLI (**cloudctl**)

Hinweis: Standardmäßig werden lokale Entwicklungsdatenbanken als Teil der Diagramminstallation bereitgestellt. Die [README.md](README.md)Datei enthält Anleitungen zur Bereitstellung Ihrer eigenen Datenbanken. Sie sind für die Sicherung (Backup) und Wiederherstellung der Datenbanken verantwortlich.

## Installationsprozess
{: #process}

1. Legen Sie die Umgebungsvariable **CLUSTER_URL** fest. Dieser Wert kann aus der Ausgabe der {{site.data.keyword.mgmt_hub}}-Installation abgerufen werden:

    ```
    export CLUSTER_URL=<CLUSTER-URL>
    ```
    {: codeblock}

    Alternativ können Sie nach dem Verbinden Ihres Clusters mit **oc login** Folgendes ausführen:

    ```
    export CLUSTER_URL=https://$(oc get routes icp-console -o jsonpath='{.spec.host}' -n kube-system)
    ```
    {: codeblock}

2. Verbinden Sie Ihren Cluster mit Clusteradministratorberechtigungen. Wählen Sie dabei **kube-system** als Namensbereich und **setzen Sie das Kennwort ein**, das Sie während der Installation des {{site.data.keyword.mgmt_hub}} in der Datei 'config.yaml' definiert haben:

    ```
    cloudctl login -a $CLUSTER_URL -u admin -p <icp-admin-kennwort> -n kube-system --skip-ssl-validation
    ```
    {: codeblock}

3. Definieren Sie den Image-Registry-Host und konfigurieren Sie die Docker-CLI so, dass sie dem selbst signierten Zertifikat vertraut:

    ```
    export REGISTRY_HOST=$(oc get routes -n openshift-image-registry default-route -o jsonpath='{.spec.host}')

    ```
    {: codeblock}

   Für macOS:

      1. Selbst signiertem Zertifikat vertrauen

      ```
      mkdir -p ~/.docker/certs.d/$REGISTRY_HOST && \
      echo | openssl s_client -showcerts -connect $REGISTRY_HOST:443 2>/dev/null | openssl x509 -outform PEM > ~/.docker/certs.d/$REGISTRY_HOST/ca.crt && \
      sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain ~/.docker/certs.d/$REGISTRY_HOST/ca.crt

      ```
      {: codeblock}
      
      2. Starten Sie den Docker-Service über die Menüleiste neu: 

   Für Ubuntu:

      1. Selbst signiertem Zertifikat vertrauen

      ```
      mkdir /etc/docker/certs.d/$REGISTRY_HOST && \
      echo | openssl s_client -showcerts -connect $REGISTRY_HOST:443 2>/dev/null | openssl x509 -outform PEM > /etc/docker/certs.d/$REGISTRY_HOST/ca.crt && \
      service docker restart

      ```
      {: codeblock}

4. Melden Sie sich wie folgt bei der Image-Registry von {{site.data.keyword.open_shift_cp}} an: 

      ```
      docker login $REGISTRY_HOST -u $(oc whoami) -p $(oc whoami -t)
      ```
      {: codeblock}

5. Entpacken Sie die komprimierte Installationsdatei für {{site.data.keyword.edge_devices_notm}}, die von IBM Passport Advantage heruntergeladen wurde:

    ```
    tar -zxvf ibm-ecm-4.1.0-x86_64.tar.gz && \
    cd ibm-ecm-4.1.0-x86_64
    ```
    {: codeblock}

6. Laden Sie den Archivinhalt in den Katalog und die Images in den Namensbereich 'ibmcom' der Registry:

    ```
    cloudctl catalog load-archive --archive ibm-ecm-prod-catalog-archive-4.1.0.tgz --registry $REGISTRY_HOST/ibmcom
    ```
    {: codeblock}

  Hinweis: In diesem Release unterstützt {{site.data.keyword.edge_devices_notm}} nur die Installation über die Befehlszeilenschnittstelle (CLI); die Installation über den Katalog wird nicht unterstützt.

7. Extrahieren Sie den Inhalt der komprimierten Datei 'charts' in das aktuelle Verzeichnis und verschieben Sie die Daten in das erstellte Verzeichnis:

    ```
    tar -O -zxvf ibm-ecm-prod-catalog-archive-4.1.0.tgz charts/ibm-ecm-prod-4.1.0.tgz | tar -zxvf - && \
    cd ibm-ecm-prod
    ```
    {: codeblock}

8. Definieren Sie eine Standardspeicherklasse, wenn noch keine festgelegt wurde:

   ```
   # oc get storageclass
   NAME                                 PROVISIONER                     AGE
   rook-ceph-block-internal             rook-ceph.rbd.csi.ceph.com      8h
   rook-ceph-cephfs-internal (default)  rook-ceph.cephfs.csi.ceph.com   8h
   rook-ceph-delete-bucket-internal     ceph.rook.io/bucket             8h
   ```
   
   Wenn keine Zeile mit der obigen Standardzeichenfolge **(default)** angezeigt wird, versehen Sie Ihren bevorzugten Standardspeicher mit folgendem Tag:

   ```
   oc patch storageclass <NAME_DER_BEVORZUGTEN_STANDARDSPEICHERKLASSE> -p '{"metadata": {"annotations": {"storageclass.kubernetes.io/is-default-class": "true"}}}'
   ```
   {: codeblock}

9. Lesen und berücksichtigen Sie Ihre Konfigurationsoptionen. Befolgen Sie anschließend den Abschnitt **Diagramm installieren** in der Datei [README.md](README.md).

  Das Script installiert die im obigen Abschnitt **Installationszusammenfassung** erwähnten Management-Hub-Komponenten, führt die Installationsprüfung aus und verweist Sie zurück auf den nachfolgenden Abschnitt **Konfiguration nach der Installation**.

## Konfiguration nach der Installation
{: #postconfig}

Führen Sie die folgenden Befehle auf dem Host aus, auf dem Sie die Erstinstallation ausgeführt haben. 

1. Melden Sie sich bei Ihrem Cluster an und befolgen Sie dabei die Schritte 1 und 2 im obigen Abschnitt **Installationsprozess**.
2. Installieren Sie die Befehlszeilenschnittstelle (CLI) **hzn** mit dem Installationsprogramm für das Ubuntu {{site.data.keyword.linux_notm}}- oder das macOS-Paket, das unter **horizon-edge-packages** im entsprechenden Verzeichnis (OS/ARCH) in dem in Schritt 5 des [Installationsprozesses](#process) extrahierten komprimierten Inhalt bereitgestellt wird: 
  * Beispiel für Ubuntu {{site.data.keyword.linux_notm}}:

    ```
    sudo dpkg -i horizon-edge-packages/linux/ubuntu/bionic/amd64/horizon-cli*.deb
    ```
    {: codeblock}

  * Beispiel für macOS:

    ```
    sudo installer -pkg horizon-edge-packages/macos/horizon-cli-*.pkg -target /
    ```
    {: codeblock}

3. Exportieren Sie die folgenden Variablen, die für die nächsten Schritte erforderlich sind:

    ```
    export EXCHANGE_ROOT_PASS=$(oc -n kube-system get secret edge-computing -o jsonpath="{.data.exchange-config}" | base64 --decode | jq -r .api.root.password)
    export HZN_EXCHANGE_URL=https://$(oc get routes icp-console -o jsonpath='{.spec.host}' -n kube-system)/ec-exchange/v1
    export HZN_EXCHANGE_USER_AUTH="root/root:$EXCHANGE_ROOT_PASS"
    export HZN_ORG_ID=IBM
    ```
    {: codeblock}

4. Erkennen Sie die {{site.data.keyword.open_shift_cp}}-Zertifizierungsstelle als vertrauenswürdig an:
    ```
    oc --namespace kube-system get secret cluster-ca-cert -o jsonpath="{.data['tls\.crt']}" | base64 --decode > /tmp/icp-ca.crt
    ```
    {: codeblock}

  * Beispiel für Ubuntu {{site.data.keyword.linux_notm}}:
     ```
     sudo cp /tmp/icp-ca.crt /usr/local/share/ca-certificates &&sudo update-ca-certificates
     ```
    {: codeblock}

  * Beispiel für macOS:

    ```
    sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain /tmp/icp-ca.crt
    ```
    {: codeblock}

5. Erstellen Sie ein Signierschlüsselpaar. Weitere Informationen finden Sie unter Schritt 5 im Abschnitt zum [Erstellung eines Edge-Service vorbereiten](../developing/service_containers.md).
    ```
    hzn key create <firmenname> <eigner@email>
    ```
    {: codeblock}

6. Führen Sie den folgenden Befehl aus, um zu überprüfen, ob die Installation mit der Exchange-API von {{site.data.keyword.edge_devices_notm}} kommunizieren kann:
    ```
    hzn exchange status
    ```
    {: codeblock}

7. Füllen Sie die Edge-Beispielservices mit Daten:

    ```
    curl https://raw.githubusercontent.com/open-horizon/examples/v4.1/tools/exchangePublishScript.sh | bash -s -- -c $(oc get -n kube-public configmap -o jsonpath="{.items[]..data.cluster_name}")
    ```
    {: codeblock}

8. Führen Sie die folgenden Befehle aus, um einige der Services und Richtlinien anzuzeigen, die in Exchange für {{site.data.keyword.edge_devices_notm}} erstellt wurden: 

    ```
    hzn exchange service list IBM/
    hzn exchange pattern list IBM/
    hzn exchange service listpolicy
    ```
    {: codeblock}

9. Erstellen Sie mithilfe der {{site.data.keyword.open_shift_cp}}-Managementkonsole eine LDAP-Verbindung, wenn Sie diesen Schritt noch nicht ausgeführt haben. Nachdem die LDAP-Verbindung hergestellt wurde, müssen Sie ein Team erstellen, diesem Team den Zugriff auf alle Namensbereiche erteilen und Benutzer zu diesem Team hinzufügen. Dadurch erhalten die einzelnen Benutzer die Berechtigung zum Erstellen von API-Schlüsseln. 

  Hinweis: API-Schlüssel werden für die Authentifizierung bei der Benutzerschnittstelle von {{site.data.keyword.edge_devices_notm}} verwendet. Weitere Informationen zu LDAP finden Sie unter [LDAP-Verbindung konfigurieren ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://www.ibm.com/support/knowledgecenter/SSFC4F_1.2.0/iam/3.4.0/configure_ldap.html). 


## Erforderliche Informationen und Dateien für Edge-Einheiten zusammenstellen
{: #prereq_horizon}

Mehrere Dateien werden dafür benötigt, den {{site.data.keyword.edge_devices_notm}}-Agenten auf Ihren Edge-Einheiten zu installieren und bei {{site.data.keyword.edge_devices_notm}} zu registrieren. In diesem Abschnitt werden Sie durch das Zusammenstellen dieser Dateien in eine TAR-Datei geführt. Diese TAR-Datei kann später für jede Ihrer Edge-Einheiten genutzt werden.

Es wird davon ausgegangen, dass Sie die Befehle **cloudctl** und **kubectl** bereits installiert und **ibm-edge-computing-4.1.0-x86_64.tar.gz** aus dem Installationsinhalt extrahiert haben, wie oben auf dieser Seite beschrieben.

1. Legen Sie die folgenden Umgebungsvariablen fest und befolgen Sie dabei die Schritte 1 und 2 im obigen Abschnitt **Installationsprozess**:

   ```
   export CLUSTER_URL=<cluster-url>
   export CLUSTER_USER=<icp-admin-benutzer>
   export CLUSTER_PW=<icp-admin-kennwort>
   ```
   {: codeblock}

2. Laden Sie die aktuelle Version von **edgeDeviceFiles.sh** herunter:

   ```
   curl -O https://raw.githubusercontent.com/open-horizon/examples/v4.0/tools/edgeDeviceFiles.sh
   chmod +x edgeDeviceFiles.sh
   ```
   {: codeblock}

3. Führen Sie das Script **edgeDeviceFiles.sh** aus, um die erforderlichen Dateien zusammenzustellen:

   ```
   ./edgeDeviceFiles.sh <edge-einheitentyp> -t
   ```
   {: codeblock}

   Befehlsargumente:
   * Unterstützte Werte für **<edge-einheitentyp>**: **32-Bit-ARM**, **64-Bit-ARM**, **x86_64-{{site.data.keyword.linux_notm}}** oder **{{site.data.keyword.macOS_notm}}**
   * **-t**: Erstellen Sie eine Datei **agentInstallFiles-&lt;edge-einhaitentyp&gt;.tar.gz**, die alle zusammengestellten Dateien enthält. Ist dieses Flag nicht gesetzt, werden die zusammengestellten Dateien im aktuellen Verzeichnis angeordnet.
   * **-k**: Erstellen Sie einen neuen API-Schlüssel mit dem Namen **$USER-Edge-Device-API-Key**. Ist dieses Flag nicht gesetzt, werden die vorhandenen API-Schlüssel auf einen Schlüssel mit dem Namen **$USER-Edge-Device-API-Key** geprüft und die Erstellung, wenn dieser Schlüssel bereits besteht, übersprungen.
   * **-d** **<distribution>**: Bei der Installation unter **64-Bit-ARM** oder **x86_64-Linux** können Sie **-d xenial** für die ältere Version von Ubuntu angeben anstelle des standardmäßigen 'Bionic'. Bei einer Installation unter **32-Bit-ARM** können Sie anstelle des Standard-Buster auch **-d stretch** angeben. Unter macOS wird das Flag '-d' ignoriert. 
   * **-f** **<verzeichnis>**: Geben Sie ein Verzeichnis an, in das die zusammengestellten Dateien verschoben werden sollen. Ist das Verzeichnis noch nicht vorhanden, wird es erstellt. Die Standardeinstellung ist das aktuelle Verzeichnis.

4. Der Befehl im vorangegangenen Schritt erstellt eine Datei mit dem Namen **agentInstallFiles-&lt;edge-einheitentype&gt;.tar.gz**. Wenn Sie über weitere Typen von Edge-Einheiten (unterschiedliche Architekturen) verfügen, wiederholen Sie den vorherigen Schritt für jeden Typ.

5. Beachten Sie den API-Schlüssel, der erstellt wurde und mit dem Befehl **edgeDeviceFiles.sh** angezeigt wird.

6. Sie sind jetzt über **cloudctl** angemeldet. Wenn Sie nun weitere API-Schlüssel erstellen müssen, die von Benutzern mit dem {{site.data.keyword.horizon}}-Befehl **hzn** verwendet werden sollen, gehen Sie folgendermaßen vor:

   ```
   cloudctl iam api-key-create "<name_des_api-schlüssels_auswählen>" -d "<beschreibung_des_api-schlüssels_auswählen>"
   ```
   {: codeblock}

   Suchen Sie in der Ausgabe des Befehls den Schlüsselwert in der Zeile, die mit **API Key** beginnt, und speichern Sie den Schlüsselwert zur späteren Verwendung. 

7. Wenn Sie bereit sind, Edge-Einheiten einzurichten, folgen Sie den Anweisungen unter [Erste Schritte mit {{site.data.keyword.edge_devices_notm}}](../getting_started/getting_started.md).

## Deinstallation durchführen
{: #uninstall}

Hinweis: Standardmäßig werden **lokale Datenbanken** konfiguriert, in diesem Fall löscht die Deinstallation ALLE persistenten Daten. Stellen Sie sicher, dass Sie Sicherungen von allen erforderlichen persistenten Daten (Sicherungsanweisungen sind in der README-Datei dokumentiert) durchgeführt haben, bevor Sie das Deinstallationsscript ausführen. Wenn Sie **ferne Datenbanken** konfiguriert haben, werden die Daten bei der Deinstallation nicht gelöscht und müssen bei Bedarf von Ihnen manuell entfernt werden.

Kehren Sie zur Position der Datei zurück, die im Rahmen der Installation entpackt wurde, und führen Sie das bereitgestellte Deinstallationsscript aus. Dieses Script deinstalliert das Helm-Release und alle zugehörigen Ressourcen. Melden Sie sich zunächst mit dem Befehl **cloudctl** als Clusteradministrator beim Cluster an und führen Sie dann Folgendes aus: 

```
ibm_cloud_pak/pak_extensions/uninstall/uninstall-edge-computing.sh <clustername>
```
{: codeblock}
