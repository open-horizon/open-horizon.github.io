---

copyright:
years: 2020
lastupdated: "2020-10-13"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# API-Schlüssel erstellen
{: #prepare_for_edge_nodes}

Hier erfahren Sie, wie ein API-Schlüssel erstellt wird und wie bestimmte Dateien und Umgebungsvariablenwerte abgerufen werden können, die Sie bei der Einrichtung von Edge-Knoten benötigen. Führen Sie diese Schritte auf einem Host aus, der eine Verbindung zu Ihrem {{site.data.keyword.ieam}}-Management-Hub-Cluster herstellen kann.

## Vorbereitende Schritte

* Falls **cloudctl** noch nicht installiert ist, führen Sie die Anweisungen im Abschnitt  [cloudctl, oc und kubectl installieren](../cli/cloudctl_oc_cli.md) aus.
* Erfragen Sie bei Ihrem {{site.data.keyword.ieam}}-Administrator die Informationen, die Sie zur Anmeldung beim Management-Hub über **cloudctl** benötigen.

## Vorgehensweise

Wenn Sie eine LDAP-Verbindung konfiguriert haben, können Sie die Berechtigungsnachweise für die hinzugefügten Benutzer zum Anmelden und Erstellen von API-Schlüsseln verwenden, oder Sie können die anfänglichen Administratorberechtigungsnachweise, die mit dem folgenden Befehl ausgegeben werden, verwenden:
```
echo "$(oc -n ibm-common-services get secret platform-auth-idp-credentials -o jsonpath='{.data.admin_username}' | base64 --decode) // $(oc -n ibm-common-services get secret platform-auth-idp-credentials -o jsonpath='{.data.admin_password}' | base64 --decode)"
```
{: codeblock}

1. Verwenden Sie die Befehlszeilenschnittstelle `cloudctl`, um sich beim {{site.data.keyword.ieam}}-Management-Hub anzumelden. Geben Sie den Benutzer an, für den Sie einen API-Schlüssel erstellen möchten:

   ```bash
   cloudctl login -a <cluster-url> -u <benutzer> -p <kennwort> --skip-ssl-validation
   ```
   {: codeblock}

2. Jeder Benutzer, der Edge-Knoten einrichtet, muss einen API-Schlüssel besitzen. Sie können denselben API-Schlüssel zur Einrichtung aller Edge-Knoten verwenden (der Schlüssel wird nicht auf den Edge-Knoten gespeichert). Erstellen Sie einen API-Schlüssel:

   ```bash
   cloudctl iam api-key-create "<name_des_api-schlüssels_auswählen>" -d "<beschreibung_des_api-schlüssels_auswählen>"
   ```
   {: codeblock}

   Suchen Sie in der Ausgabe des Befehls den Schlüsselwert in der Zeile, die mit **API Key** beginnt. Speichern Sie den Schlüsselwert zur zukünftigen Verwendung, da Sie ihn später nicht mehr aus dem System abfragen können.

3. Lassen Sie sich von Ihrem {{site.data.keyword.ieam}}-Administrator beim Festlegen der folgenden Umgebungsvariablen helfen:

  ```bash
  export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-schlüssel>   export HZN_ORG_ID=<ihre_exchange-organisation>   mgmtHubIngress=$(oc get cm management-ingress-ibmcloud-cluster-info -o jsonpath='{.data.cluster_ca_domain}')   export HZN_FSS_CSSURL=https://$mgmtHubIngress/edge-css/   echo "export HZN_FSS_CSSURL=$HZN_FSS_CSSURL"
  ```
  {: codeblock}

## Weitere Schritte

Nachdem Sie die Einrichtung der Edge-Knoten vorbereitet haben, können Sie nun die Schritte im Abschnitt  [Edge-Knoten installieren](../installing/installing_edge_nodes.md) ausführen.

