---

copyright:
years: 2020
lastupdated: "2020-05-18"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Edge-Knotendateien zusammenstellen
{: #prereq_horizon}

Für die Installation des {{site.data.keyword.edge_notm}}-Agenten ({{site.data.keyword.ieam}}-Agenten) auf Ihren Edge-Einheiten und Edge-Clustern und die entsprechende Registrierung bei {{site.data.keyword.ieam}} werden verschiedene Dateien benötigt. In diesen Informationen erfahren Sie, wie die Dateien gebündelt werden, die Sie für Ihre Edge-Knoten benötigen. Führen Sie die angegebenen Schritte auf einem Admin-Host aus, der mit dem {{site.data.keyword.ieam}}-Management-Hub verbunden ist.

Bei den folgenden Schritten wird davon ausgegangen, dass Sie die Befehle [IBM Cloud Pak CLI (**cloudctl**) und OpenShift-Client-CLI (**oc**)](../cli/cloudctl_oc_cli.md) installiert haben und dass Sie die Schritte aus dem Verzeichnis **ibm-eam-{{site.data.keyword.semver}}-bundle** des nicht gepackten Installationsmediums ausführen. Dieses Script sucht die erforderlichen {{site.data.keyword.horizon}}-Pakete in der Datei **agent/edge-packages-{{site.data.keyword.semver}}.tar.gz** und erstellt die erforderlichen Konfigurations- und Zertifikatsdateien für den Edge-Knoten.

1. Melden Sie sich bei Ihrem Management-Hub-Cluster mit Administratorberechtigungsnachweisen und dem Namespace an, in den Sie {{site.data.keyword.ieam}} installiert haben:
   ```bash
   cloudctl login -a &amp;TWBLT;Cluster-URL&gt; -u &amp;TWBLT;Cluster-Admin-Benutzer&gt; -p &amp;TWBLT;Cluster-Admin-Kennwort&gt; -n &amp;TWBLT;Namespace&gt; --skip-ssl-validation
   ```
   {: codeblock}

2. Legen Sie die folgenden Umgebungsvariablen fest:

   ```bash
   export CLUSTER_URL=https://$(oc get cm management-ingress-ibmcloud-cluster-info -o jsonpath='{.data.cluster_ca_domain}') oc --insecure-skip-tls-verify=true -n kube-public get secret ibmcloud-cluster-ca-cert -o jsonpath="{.data.ca\.crt}" | base64 --decode &gt; ieam.crt export HZN_MGMT_HUB_CERT_PATH="$PWD/ieam.crt" export HZN_FSS_CSSURL=${CLUSTER_URL}/edge-css
   ```
   {: codeblock}

   Definieren Sie die folgenden Umgebungsvariablen für die Docker-Authentifizierung, indem Sie Ihren eigenen Berechtigungsschlüssel (**ENTITLEMENT_KEY**) angeben:
   ```
   export REGISTRY_USERNAME=cp    export REGISTRY_PASSWORD=<ENTITLEMENT_KEY>
   ```
   {: codeblock}

   **Hinweis:** Rufen Sie Ihren Berechtigungsschlüssel bei [My IBM Key](https://myibm.ibm.com/products-services/containerlibrary) ab.

3. Wechseln Sie in das Verzeichnis **agent**, in dem sich die Datei **edge-packages-{{site.data.keyword.semver}}.tar.gz** befindet:

   ```bash
   cd agent
   ```
   {: codeblock}

4. Es gibt zwei bevorzugte Methoden zum Zusammenstellen der Dateien für die Installation des Edge-Knotens mithilfe des Scripts **edgeNodeFiles.sh**. Wählen Sie abhängig von Ihren Anforderungen eine der folgenden Methoden aus:

   * Führen Sie das Script **edgeNodeFiles.sh** aus, um die erforderlichen Dateien zu erfassen und in die CSS-Komponente "CSS Cloud Sync Service" (CSS) des Model Management Systems (MMS) zu setzen.

     **Hinweis:** Das Script **edgeNodeFiles.sh** wurde als Teil des Pakets 'horizon-cli' installiert und sollte in Ihrem Pfad enthalten sein.

     ```bash
     HZN_EXCHANGE_USER_AUTH='' edgeNodeFiles.sh ALL -c -p edge-packages-{{site.data.keyword.semver}} -r cp.icr.io/cp/ieam
     ```
     {: codeblock}

     Verwenden Sie auf jedem Edge-Knoten das Flag **-i 'css:'** für das Script  **agent-install.sh**, damit die benötigten Dateien aus der CSS-Komponente abgerufen werden können.

     **Hinweis:** Wenn Sie [SDO-fähige Edge-Einheiten](../installing/sdo.md) verwenden wollen, müssen Sie dieses Format des Befehls `edgeNodeFiles.sh` ausführen.

   * Alternativ können Sie mit **edgeNodeFiles.sh** die Dateien in einer TAR-Datei bündeln:

     ```bash
     edgeNodeFiles.sh ALL -t -p edge-packages-{{site.data.keyword.semver}} -r cp.icr.io/cp/ieam
     ```
     {: codeblock}

     Kopieren Sie die TAR-Datei auf jeden Edge-Knoten und verwenden Sie das Flag **-z** für das Script **agent-install.sh**, um die benötigten Dateien aus der TAR-Datei abzurufen.

     Installieren Sie das Paket **horizon-cli** auf diesem Host, wenn es dort noch nicht installiert ist. Ein Beispiel für diesen Prozess finden Sie im Abschnitt [Konfiguration nach der Installation](post_install.md#postconfig).

     Suchen Sie nach den Scripts **agent-install.sh** und **agent-uninstall.sh**, die als Teil des Pakets **horizon-cli** installiert worden sind.    Diese Scripts werden während der Einrichtung auf jedem Edge-Knoten benötigt (das Script **agent-uninstall.sh** unterstützt gegenwärtig nur Edge-Cluster):
    * {{site.data.keyword.linux_notm}} Beispiel:

     ```
     ls /usr/horizon/bin/agent-{install,uninstall}.sh
     ```
     {: codeblock}

    * Beispiel für macOS:

     ```
     ls /usr/local/bin/agent-{install,uninstall}.sh
     ```
     {: codeblock}

**Hinweis:** Für das Script **edgeNodeFiles.sh** gibt es weitere Flags, mit denen gesteuert werden kann, welche Dateien zusammenzustellen sind und wo sie abgelegt werden sollen. Führen Sie das folgende Script aus, um alle verfügbaren Flags anzuzeigen: **edgeNodeFiles.sh -h**

## Weitere Schritte

Vor der Einrichtung von Edge-Knoten müssen von Ihnen oder einem Knotentechniker ein API-Schlüssel erstellt und weitere Umgebungsvariablenwerte zusammengestellt werden. Führen Sie die Schritte im Abschnitt [API-Schlüssel erstellen](prepare_for_edge_nodes.md) aus.
