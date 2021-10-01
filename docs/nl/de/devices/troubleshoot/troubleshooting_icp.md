---

copyright:
years: 2019
lastupdated: "2019-09-18"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Tipps zur Fehlerbehebung in der {{site.data.keyword.icp_notm}}-Umgebung
{: #troubleshooting_icp}

Lesen Sie die folgenden Informationen, um die Behebung allgemeiner Fehler in {{site.data.keyword.icp_notm}}-Umgebungen, die bei {{site.data.keyword.edge_devices_notm}} auftreten können, zu vereinfachen. Die Tipps und Anleitungen zu den einzelnen Fragen können Sie bei der Behebung allgemeiner Probleme und beim Ermitteln von Informationen zur Klärung der Fehlerursache unterstützen.
{:shortdesc}

   * [Sind die Berechtigungen für {{site.data.keyword.edge_devices_notm}} ordnungsgemäß für die Verwendung in der {{site.data.keyword.icp_notm}}-Umgebung konfiguriert? ](#setup_correct)

### Sind die Berechtigungen für {{site.data.keyword.edge_devices_notm}} ordnungsgemäß für die Verwendung in der {{site.data.keyword.icp_notm}}-Umgebung konfiguriert?
{: #setup_correct}

Sie benötigen ein {{site.data.keyword.icp_notm}}-Benutzerkonto, um Aktionen in {{site.data.keyword.edge_devices_notm}} in dieser Umgebung ausführen zu können. Darüber hinaus benötigen Sie einen API-Schlüssel, der aus diesem Konto erstellt wurde. 

Führen Sie den folgenden Befehl aus, um Ihre Berechtigungsnachweise für {{site.data.keyword.edge_devices_notm}} in dieser Umgebung zu überprüfen: 

   ```
    hzn exchange user list
    ```
   {: codeblock}

Wenn Exchange einen für JSON-formatierten Eintrag zurückgibt, in dem mindestens ein Benutzer angegeben wird, sind die Berechtigungsnachweise für {{site.data.keyword.edge_devices_notm}} ordnungsgemäß konfiguriert. 

Wird eine Fehlerantwort zurückgegeben, können Sie entsprechende Schritte ausführen, um die Konfigurationsfehler bei den Berechtigungsnachweisen zu suchen. 

Wenn die Fehlernachricht angibt, dass ein falscher API-Schlüssel vorliegt, können Sie mit den folgenden Befehlen einen neuen API-Schlüssel erstellen. 

**Hinweis:** Legen Sie zuerst für alle Umgebungsvariablen, denen in diesen Befehlen das Präfix `$` vorangestellt ist, die korrekten Werte fest. 

   ```
   cloudctl login -a $ICP_URL -u $USER -p $PW -n kube-public --skip-ssl-validation
   cloudctl iam api-key-create "$KEY_NAME" -d "$KEY_DESC"
   ```
   {: codeblock}

Wenn die Fehlernachricht angibt, dass das Zertifikat nicht gültig ist, können Sie den folgenden Befehl verwenden, um ein neues selbst signiertes Zertifikat zu erstellen: 

   ```
     kubectl -n kube-public get secret ibmcloud-cluster-ca-cert -o jsonpath="{.data['ca\.crt']}" | base64 --decode > icp.crt
     ```
   {: codeblock}

Weisen Sie anschließend das Betriebssystem an, diesem Zertifikat zu vertrauen. Führen Sie auf einer Linux-Maschine den folgenden Befehl aus: 

   ```
sudo cp icp.crt /usr/local/share/ca-certificates &&  sudo update-ca-certificates
       ````
   {: codeblock}

Führen Sie auf einer MacOS-Maschine den folgenden Befehl aus: 

   ```
       sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain icp.crt
       ```
   {: codeblock}
