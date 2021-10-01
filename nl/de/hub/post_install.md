---

copyright:
years: 2020
lastupdated: "2020-10-28"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Konfiguration nach der Installation

## Voraussetzungen

* [IBM Cloud Pak-CLI (**cloudctl**) und OpenShift-Client-CLI (**oc**)](../cli/cloudctl_oc_cli.md)
* [**jq**](https://stedolan.github.io/jq/download/)
* [**git**](https://git-scm.com/downloads)
* [**Docker**](https://docs.docker.com/get-docker/) Version 1.13 oder höher
* **make**

## Installationsprüfung

1. Führen Sie die Schritte unter [{{site.data.keyword.ieam}} installieren](online_installation.md) aus.
2. Vergewissern Sie sich, dass für alle Pods im {{site.data.keyword.ieam}}-Namensbereich als Status entweder **Running** (Aktiv) oder **Completed** (Abgeschlossen) angegeben ist:

   ```
   oc get pods
   ```
   {: codeblock}

   Dies ist ein Beispiel dafür, was mit lokalen Datenbanken und mit installiertem lokalem Secrets Manager angezeigt werden sollte. Es kann von einigen Initialisierungsneustarts ausgegangen werden, bei mehreren Neustarts wird jedoch normalerweise ein Problem angezeigt.:
   ```
   $oc get pods NAME READY STATUS STARTS AGE create-agbotdb-cluster-j4fnb 0/1 Abgeschlossen 0 88m create-exchangedb-cluster-hzlxm 0/1 Abgeschlossen 0 88m ibm-common-service-operator-68b46458dc-nv2mn 1/1 Running 0 103m ibm-eamhub-controller-manager-7xdts 1/1 Running 0 103m ibm-edge-agbot-5546dfd7f4-sck6h 1/1 Running 0 81m ibm-edge-agbotdb-keeper-0 1/1 Running 0 88m ibm-edge-agbotdb-keeper-1 1/1 Running 0 87m ibm-edge-agbotdb-keeper-2 1/1 Running 0 86m ibm-edge-agbotdb-proxy-7447f6658f-7wvdh 1/1 Running 0 88m    ibm-edge-agbotdb-proxy-7447f6658f-8r56d 1/1 Running 0 88m ibm-edge-agbotdb-proxy-7447f6658f-g4hls 1/1 Running 0 88m ibm-edge-agbotdb-sentinel-5766f666f4-5qm9x 1/1 Running 0 88m ibm-edge-agbotdb-sentinel-5766f666f4-5whgr 1/1 Running 0 88m ibm-edge-agbotdb-sentinel-5766f666f4-9xjpr 1/1 Running 0 88m ibm-edge-css-5c59c9d6b6-kqfnn 1/1 Running 0 81m ibm-edge-css-5c59c9d6b6-sp84w 1/1 Running 0 81m
   ibm-edge-css-5c59c9d6b6-wf84s                  1/1     Running     0          81m    ibm-edge-cssdb-server-0                        1/1     Running     0          88m    ibm-edge-exchange-b6647db8d-k97r8              1/1     Running     0          81m    ibm-edge-exchange-b6647db8d-kkcvs              1/1     Running     0          81m    ibm-edge-exchange-b6647db8d-q5ttc              1/1     Running     0          81m    ibm-edge-exchangedb-keeper-0                   1/1     Running     1          88m    ibm-edge-exchangedb-keeper-1                   1/1     Running     0          85m    ibm-edge-exchangedb-keeper-2                   1/1     Running     0          84m    ibm-edge-exchangedb-proxy-6bbd5b485-cx2v8      1/1     Running     0          88m    ibm-edge-exchangedb-proxy-6bbd5b485-hs27d      1/1     Running     0          88m    ibm-edge-exchangedb-proxy-6bbd5b485-htldr      1/1     Running     0          88m    ibm-edge-exchangedb-sentinel-6d685bf96-hz59z   1/1     Running     1          88m    ibm-edge-exchangedb-sentinel-6d685bf96-m4bdh   1/1     Running     0          88m    ibm-edge-exchangedb-sentinel-6d685bf96-mxv2b   1/1     Running     1          88m    ibm-edge-sdo-0                                 1/1     Running     0          81m    ibm-edge-ui-545d694f6c-4rnrf                   1/1     Running     0          81m    ibm-edge-ui-545d694f6c-97ptz                   1/1     Running     0          81m    ibm-edge-ui-545d694f6c-f7bf6                   1/1     Running     0          81m
   ibm-edge-vault-0 1/1 Running 0 81m ibm-edge-vault-bootstrap-k8km9 0/1 Abgeschlossen 0 80m
   ```
   {: codeblock}

   **Hinweise:**
   * Weitere Informationen zu Pods im Status **Pending** (Anstehend) aufgrund von Ressourcen- oder Planungsproblemen finden Sie auf der Seite [Clusterdimensionierung](cluster_sizing.md). Dazu gehören Informationen zur Reduzierung der Planungsaufwände für Komponenten.
   * Weitere Informationen zu anderen Fehlern finden Sie im Abschnitt [Fehlerbehebung](../admin/troubleshooting.md).
3. Vergewissern Sie sich, dass alle Pods im Namensbereich **ibm-common-services** entweder den Status **Running** (Aktiv) oder **Completed** (Abgeschlossen) aufweisen:

   ```
   oc get pods -n ibm-common-services
   ```
   {: codeblock}

4. Melden Sie sich an, extrahieren Sie das Agentenpaket und extrahieren Sie es mit Ihrem Berechtigungsschlüssel über die [Entitled Registry](https://myibm.ibm.com/products-services/containerlibrary):
    ```
    docker login cp.icr.io --username cp &amp;TWBAMP;&amp;TWBAMP; \     docker rm -f ibm-eam-{{site.data.keyword.semver}}-bundle; \     docker create --name ibm-eam-{{site.data.keyword.semver}}-bundle cp.icr.io/cp/ieam/ibm-eam-bundle:{{site.data.keyword.anax_ver}} bash &amp;TWBAMP;&amp;TWBAMP; \     docker cp ibm-eam-{{site.data.keyword.semver}}-bundle:/ibm-eam-{{site.data.keyword.semver}}-bundle.tar.gz ibm-eam-{{site.data.keyword.semver}}-bundle.tar.gz &amp;TWBAMP;&amp;TWBAMP; \     tar -zxvf ibm-eam-{{site.data.keyword.semver}}-bundle.tar.gz &amp;TWBAMP;&amp;TWBAMP; \     cd ibm-eam-{{site.data.keyword.semver}}-bundle/tools
    ```
    {: codeblock}
5. Validieren Sie den Installationsstatus:
    ```
    ./service_healthcheck.sh
    ```
    {: codeblock}

    Nachfolgend sehen Sie eine Beispielausgabe:
    ```
    $ ./service_healthcheck.sh     ==Running service verification tests for IBM Edge Application Manager==     SUCCESS: IBM Edge Application Manager Exchange API is operational     SUCCESS: IBM Edge Application Manager Cloud Sync Service is operational     SUCCESS: IBM Edge Application Manager Agbot database heartbeat is current     SUCCESS: IBM Edge Application Manager SDO API is operational     SUCCESS: IBM Edge Application Manager UI is properly requiring valid authentication     ==All expected services are up and running==
    ```

   * Falls der Befehl **service_healthcheck.sh** mit Fehlern beendet wird, Sie bei der Ausführung der nachfolgenden Befehle Probleme feststellen oder zur Laufzeit Probleme auftreten, helfen Ihnen die Informationen im Abschnitt [Fehlerbehebung](../admin/troubleshooting.md).

## Konfiguration nach der Installation
{: #postconfig}

Die folgenden Schritte müssen auf einem Host ausgeführt werden, der die Installation der **hzn**-CLI unterstützt. Die CLI kann derzeit auf einem Host mit Linux auf Debian/apt-Basis, mit amd64 Red Hat/rpm Linux oder mit macOS  installiert werden. Bei den folgenden Schritten werden dieselben Datenträger verwendet, die im Abschnitt zur Installationsprüfung bei PPA heruntergeladen wurden.

1. Installieren Sie die CLI **hzn** mithilfe der Anweisungen für Ihre unterstützte Plattform:
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

2. Führen Sie das Script für den Installationsabschluss aus. Dieses Script übernimmt die gesamte erforderliche Initialisierung für die Erstellung Ihrer ersten Organisation. (Organisationen sind der Mechanismus, mit dem  {{site.data.keyword.ieam}} Ressourcen und Benutzer voneinander abgrenzt, um Multi-Tenant-Funktionalität zu ermöglichen. Für den Anfang ist diese erste Organisation ausreichend. Sie können später weitere Organisationen konfigurieren. Weitere Informationen finden Sie unter [Multi-Tenant-Funktionalität](../admin/multi_tenancy.md)).

   **Hinweis**: **IBM** und **root** sind Organisationen zur internen Verwendung und können nicht als ursprüngliche Organisation ausgewählt werden. Ein Organisationsname darf keine Unterstriche (_), Kommata (,), Leerzeichen (), einfache Anführungszeichen (') oder Fragezeichen (?) enthalten..

   ```
   ./post_install.sh <gewünschter_organisationsname>
   ```
   {: codeblock}

3. Führen Sie den folgenden Befehl aus, um den Link {{site.data.keyword.ieam}}-Managementkonsole für Ihre Installation zu drucken:
   ```
   echo https://$(oc get cm management-ingress-ibmcloud-cluster-info -o jsonpath='{.data.cluster_ca_domain}')/edge
   ```
   {: codeblock}

## Authentifizierung 

Die Benutzerauthentifizierung ist erforderlich, wenn Sie auf die {{site.data.keyword.ieam}}-Managementkonsole zugreifen. Ein erstes Administratorkonto wurde von dieser Installation erstellt und kann mit dem folgenden Befehl ausgedruckt werden:
```
echo "$(oc -n ibm-common-services get secret platform-auth-idp-credentials -o jsonpath='{.data.admin_username}' | base64 --decode) // $(oc -n ibm-common-services get secret platform-auth-idp-credentials -o jsonpath='{.data.admin_password}' | base64 --decode)"
```
{: codeblock}

Sie können dieses Administratorkonto für die Erstauthentifizierung verwenden und zusätzlich [LDAP konfigurieren](https://www.ibm.com/support/knowledgecenter/SSHKN6/iam/3.x.x/configure_ldap.html), indem Sie auf den Link für die Managementkonsole zugreifen, der mit dem folgenden Befehl ausgegeben wird:
```
echo https://$(oc get cm management-ingress-ibmcloud-cluster-info -o jsonpath='{.data.cluster_ca_domain}')
```
{: codeblock}

Nachdem die LDAP-Verbindung hergestellt wurde, müssen Sie ein Team erstellen, diesem Team den Zugriff auf den  Namensbereich erteilen, für den der {{site.data.keyword.edge_notm}}-Operator bereitgestellt worden ist, und Benutzer zu diesem Team hinzufügen. Dadurch erhalten die einzelnen Benutzer die Berechtigung zum Erstellen von API-Schlüsseln.

API-Schlüssel werden für die Authentifizierung mit der {{site.data.keyword.edge_notm}}-CLI verwendet, und die Berechtigungen, die API-Schlüsseln zugeordnet sind, sind mit dem Benutzer identisch, mit dem sie generiert werden.

Wenn Sie keine LDAP-Verbindung erstellt haben, können Sie trotzdem API-Schlüssel mit den ursprünglichen Administratorberechtigungsnachweisen erstellen, beachten Sie jedoch, dass der API-Schlüssel über **Clusteradministrator**-Berechtigungen verfügt.

## Weitere Schritte

Führen Sie den Prozess auf der Seite [Edge-Knoten-Dateien zusammenstellen](gather_files.md) aus, um Installationsmedien für Ihre Edge-Knoten vorzubereiten.
