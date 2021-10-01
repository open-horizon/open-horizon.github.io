---

copyright:
years: 2021
lastupdated: "2021-03-23"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Upgrades
{: #hub_upgrade_overview}

## Zusammenfassung zum Upgrade
{: #sum}
* Die aktuelle Version des {{site.data.keyword.ieam}}-Management-Hubs ist {{site.data.keyword.semver}}.
* {{site.data.keyword.ieam}} {{site.data.keyword.semver}} wird unter {{site.data.keyword.ocp}} Version 4.6 unterstützt.

Upgrades auf denselben Operator Lifecycle Manager (OLM) für {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) Management Hub und [IBM Cloud Platform Common Services](https://www.ibm.com/docs/en/cpfs) erfolgen automatisch über OLM, das auf Ihrem {{site.data.keyword.open_shift_cp}} ({{site.data.keyword.ocp}}) Cluster vorinstalliert wird.

{{site.data.keyword.ieam}} Kanäle werden durch **untergeordnete Version** definiert (z. B. v4.2 und v4.3) und **Patchversionen** (z. B. 4.2.x) automatisch aktualisiert. Bei Upgrades für **ältere Versionen** müssen Sie die Kanäle manuell ändern, um das Upgrade einzuleiten. Wenn Sie ein Upgrade für eine **untergeordnete Version** einleiten möchten, muss die neueste **Patch-Version** der vorherigen **untergeordneten Version**verfügbar sein. Das Upgrade wird dann dann durch das Umschalten der Kanäle eingeleitet.

**Hinweise:**
* Downgrade wird nicht unterstützt
* Upgrade von {{site.data.keyword.ieam}} 4.1.x auf 4.2.x wird nicht unterstützt
* Hinweis: Wenn Sie jegliche `InstallPlans`in Ihrem Projekt für die manuelle Genehmigung konfiguriert haben, gilt dies aufgrund eines [bekannten {{site.data.keyword.ocp}}-Problems](https://access.redhat.com/solutions/5493011) auch für alle anderen `InstallPlans` in diesem Projekt. Sie müssen die Aktualisierung des Operators manuell genehmigen, um fortfahren zu können.

### Upgrade für {{site.data.keyword.ieam}} Management Hub von 4.2.x auf 4.3.x durchführen

1. Führen Sie vor dem Upgrade eine Sicherung aus. Weitere Informationen finden Sie unter [Sicherung und Wiederherstellung](../admin/backup_recovery.md).
2. Navigieren Sie zur {{site.data.keyword.ocp}} Webkonsole für Ihren Cluster.
3. Wechseln Sie zu **Operatoren** &gt; **Installierte Operatoren**.
4. Suchen Sie nach **{{site.data.keyword.ieam}}** und klicken Sie auf das Ergebnis **{{site.data.keyword.ieam}} Management Hub** (Management Hub).
5. Navigieren Sie zur Registerkarte **Subskription** .
6. Klicken Sie auf den Link **v4.2** im Abschnitt **Kanal** .
7. Klicken Sie auf das Optionsfeld, um Ihren aktiven Kanal auf **v4.3** zu schalten, um das Upgrade einzuleiten.

Um zu überprüfen, ob das Upgrade abgeschlossen ist, finden Sie weitere Informationen in den [Schritten 1 bis 5 im Abschnitt zur Installationsüberprüfung nach der Installation](post_install.md).

Informationen zum Aktualisieren von Beispielservices finden Sie in den [Schritten 1 bis 3 im Abschnitt zur Konfiguration der Nachinstallation](post_install.md).

## Edge-Knoten aktualisieren

Vorhandene {{site.data.keyword.ieam}}-Knoten werden nicht automatisch aktualisiert. Die Version {{site.data.keyword.ieam}} 4.2.1 Agentenversion (2.28.0-338) wird mit einem {{site.data.keyword.ieam}} {{site.data.keyword.semver}} Management-Hub unterstützt. Damit der {{site.data.keyword.edge_notm}} Agent auf Ihren Edge-Einheiten und Edge-Clustern aktualisiert werden kann, müssen Sie zuerst die {{site.data.keyword.semver}} Edge-Knoten-Dateien in den Cloud-Sync-Service (CSS) platzieren.

Führen Sie die Schritte 1-3 unter **Installation der neuesten CLI in Ihrer Umgebung** aus, auch wenn Sie Ihre Edge-Knoten zu diesem Zeitpunkt nicht aktualisieren möchten. Dadurch wird sichergestellt, dass neue Edge-Knoten mit dem neuesten {{site.data.keyword.ieam}} {{site.data.keyword.semver}} -Agentencode installiert werden.

### Neueste CLI in Ihrer Umgebung installieren
1. Melden Sie sich an, extrahieren Sie das Agentenpaket und extrahieren Sie es mit Ihrem Berechtigungsschlüssel über die [Entitled Registry](https://myibm.ibm.com/products-services/containerlibrary):
    ```
    docker login cp.icr.io --username cp &amp;TWBAMP;&amp;TWBAMP; \     docker rm -f ibm-eam-{{site.data.keyword.semver}}-bundle; \     docker create --name ibm-eam-{{site.data.keyword.semver}}-bundle cp.icr.io/cp/ieam/ibm-eam-bundle:{{site.data.keyword.anax_ver}} bash &amp;TWBAMP;&amp;TWBAMP; \     docker cp ibm-eam-{{site.data.keyword.semver}}-bundle:/ibm-eam-{{site.data.keyword.semver}}-bundle.tar.gz ibm-eam-{{site.data.keyword.semver}}-bundle.tar.gz &amp;TWBAMP;&amp;TWBAMP; \     tar -zxvf ibm-eam-{{site.data.keyword.semver}}-bundle.tar.gz &amp;TWBAMP;&amp;TWBAMP; \     cd ibm-eam-{{site.data.keyword.semver}}-bundle/tools
    ```
    {: codeblock}
2. Installieren Sie die CLI **hzn** mithilfe der Anweisungen für Ihre unterstützte Plattform:
  * Navigieren Sie zum Verzeichnis **agent** und entpacken Sie die Agentendateien:
    ```
    cd ibm-eam-{{site.data.keyword.semver}}-bundle/agent &amp;TWBAMP;&amp;TWBAMP; \ tar -zxvf edge-packages-{{site.data.keyword.semver}}.tar.gz
    ```
    {: codeblock}

    * Beispiel für Debian {{site.data.keyword.linux_notm}}:
      ```
      sudo apt-get install ./edge-packages-{{site.data.keyword.semver}}/linux/deb/amd64/horizon-cli*.deb
      ```
      {: codeblock}

    * Beispiel für Red Hat {{site.data.keyword.linux_notm}}:
      ```
      sudo dnf install -yq ./edge-packages-{{site.data.keyword.semver}}/linux/rpm/x86_64/horizon-cli-*.x86_64.rpm
      ```
      {: codeblock}

    * Beispiel für macOS:
      ```
      sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain edge-packages-{{site.data.keyword.semver}}/macos/pkg/x86_64/horizon-cli.crt && \       sudo installer -pkg edge-packages-{{site.data.keyword.semver}}/macos/pkg/x86_64/horizon-cli-*.pkg -target /
      ```
      {: codeblock}
3. Führen Sie die Schritte in [Dateien des Edge-Knotens zusammenstellen](../hub/gather_files.md) aus, um die Agenteninstallationsdateien in das CSS zu übertragen.

### Upgrade für Agents auf Edge-Knoten durchführen
1. Melden Sie sich bei Ihrem Edge-Knoten als **Root** auf einer Einheit oder als **Admin** in Ihrem Cluster an und legen Sie die Horizon-Umgebungsvariablen fest:
```bash
export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-schlüssel>   export HZN_ORG_ID=<ihre_exchange-organisation>   export HZN_FSS_CSSURL=https://<ieam-management-hub-ingress>/edge-css/
```
{: codeblock}

2. Legen Sie die erforderlichen Umgebungsvariablen auf der Basis Ihres Clustertyps fest (überspringen Sie diesen Schritt, wenn Sie eine Aktualisierung für eine Einheit durchführen):

  * **In OCP-Edge-Clustern:**
  
    Legen Sie die Speicherklasse fest, die vom Agenten verwendet werden soll:
    
    ```bash
    oc get storageclass    export EDGE_CLUSTER_STORAGE_CLASS=<rook-ceph-cephfs-internal>
    ```
    {: codeblock}

    Legen Sie für den Registry-Benutzernamen den von Ihnen erstellten Namen des Servicekontos fest:
    ```bash     oc get serviceaccount -n openhorizon-agent     export EDGE_CLUSTER_REGISTRY_USERNAME=<servicekontoname>
    ```
    {: codeblock}

    Legen Sie das Registry-Token fest: 
    ```bash     export EDGE_CLUSTER_REGISTRY_TOKEN=`oc serviceaccounts get-token $EDGE_CLUSTER_REGISTRY_USERNAME`
    ```
    {: codeblock}

  * **Auf k3s:**
  
    Weisen Sie **agent-install.sh** an, die Standardspeicherklasse zu verwenden:
    
    ```bash
    export EDGE_CLUSTER_STORAGE_CLASS=local-path
    ```
    {: codeblock}

  * **Auf microk8s:**
  
    Weisen Sie **agent-install.sh** an, die Standardspeicherklasse zu verwenden:
    
    ```bash
    export EDGE_CLUSTER_STORAGE_CLASS=microk8s-hostpath
    ```
    {: codeblock}

3. Extrahieren Sie das Script **agent-install.sh** aus CSS:
```bash
curl -u $HZN_ORG_ID/$HZN_EXCHANGE_USER_AUTH $HZN_FSS_CSSURL/api/v1/objects/IBM/agent_files/agent-install.sh/data -o agent-install.sh --insecure && chmod +x agent-install.sh
```
{: codeblock}

4. Führen Sie das Script **agent-install.sh** aus, um die aktualisierten Dateien aus CSS abzurufen und den Agenten für Horizon zu konfigurieren:
  *  **Auf Edge-Einheiten:**
    ```bash     sudo -s -E ./agent-install.sh -i 'css:' -s
    ```
    {: codeblock}

  *  **In Edge-Clustern:**
    ```bash     ./agent-install.sh -D cluster -i 'css:' -s
    ```
    {: codeblock}

**Hinweis:** Geben Sie beim Ausführen der Agenteninstallation die Option '-s' an, um die Registrierung zu überspringen. Dadurch verbleibt der Edge-Knoten in demselben Status, den er vor dem Upgrade aufwies.

## Bekannte Probleme und häufig gestellte Fragen
{: #FAQ}

### {{site.data.keyword.ieam}} 4.2
* Es gibt ein bekanntes Problem mit der {{site.data.keyword.ieam}} 4.2.0 lokalen cssdb mongo-Datenbank, die zu Datenverlust führt, wenn der Pod neu geplant wird. Wenn Sie lokale Datenbanken verwenden (Standardeinstellung), lassen Sie das Upgrade von {{site.data.keyword.ieam}} {{site.data.keyword.semver}} vor dem Aktualisieren Ihres {{site.data.keyword.ocp}} -Clusters auf 4.6 durchführen. Weitere Informationen hierzu finden Sie auf der Seite [Bekannte Probleme](../getting_started/known_issues.md).

* Ich habe für meinen {{site.data.keyword.ocp}}-Cluster nur Upgrades bis Version 4.4 durchgeführt und das automatische Upgrade scheint blockiert zu sein.

  * Führen Sie die folgenden Schritte aus, um dieses Problem zu beheben:
  
    1) Erstellen Sie eine Sicherung der aktuellen Inhalte Ihres {{site.data.keyword.ieam}}-Management-Hubs.  Die Dokumentation zum Erstellen von Sicherungen finden Sie im folgenden Abschnitt: [Datensicherung und -wiederherstellung](../admin/backup_recovery.md).
    
    2) Führen Sie für Ihren {{site.data.keyword.ocp}}-Cluster ein Upgrade auf Version 4.6 durch.
    
    3) Aufgrund eines bekannten Problems bei der lokalen Mongo-Datenbank **cssdb** für {{site.data.keyword.ieam}} 4.2.0 wird die Datenbank durch das Upgrade in **Schritt 2** reinitialisiert.
    
      * Wenn Sie die MMS-Funktionalität von {{site.data.keyword.ieam}} nutzen und Bedenken bezüglich Datenverlust haben, können Sie die Sicherung verwenden, die Sie in **Schritt 1** erstellt haben, und die Schritte der **Wiederherstellungsprozedur** auf der Seite [Datensicherung und -wiederherstellung](../admin/backup_recovery.md) befolgen. (**Hinweis:** Die Wiederherstellungsprozedur hat Ausfallzeiten zur Folge.)
      
      * Führen Sie alternativ die folgenden Schritte aus, um den {{site.data.keyword.ieam}}-Operator zu deinstallieren und erneut zu installieren, wenn Sie die MMS-Funktionalität nicht genutzt haben, keine Bedenken bezüglich des Verlusts von MMS-Daten haben oder ferne Datenbanken verwenden:
      
        1) Navigieren Sie zur Seite 'Installierte Operatoren' für Ihren {{site.data.keyword.ocp}}-Cluster.
        
        2) Suchen Sie den Operator für den IEAM-Management-Hub und öffnen Sie die entsprechende Seite.
        
        3) Wählen Sie im Aktionsmenü auf der linken Seite die Option zum Deinstallieren des Operators aus.
        
        4) Navigieren Sie zur Seite 'OperatorHub' und installieren Sie den Operator für den IEAM-Management-Hub erneut.

* Wird {{site.data.keyword.ocp}} Version 4.5 unterstützt?

  * Der {{site.data.keyword.ieam}}-Management-Hub wurde nicht für {{site.data.keyword.ocp}} Version 4.5 getestet und wird nicht unterstützt.  Es empfiehlt sich, ein Upgrade auf {{site.data.keyword.ocp}} Version 4.6 durchzuführen.

* Gibt es eine Möglichkeit, diese Version des {{site.data.keyword.ieam}}-Management-Hubs abzulehnen?

  * Der {{site.data.keyword.ieam}}-Management-Hub Version 4.2.0 wird mit Release von Version {{site.data.keyword.semver}} nicht mehr unterstützt.
