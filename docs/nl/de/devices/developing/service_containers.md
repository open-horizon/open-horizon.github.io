---

copyright:
years: 2019,2020
lastupdated: "2020-01-28"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Erstellung eines Edge-Service vorbereiten
{: #service_containers}

Verwenden Sie {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}), um Services innerhalb von {{site.data.keyword.docker}}-Containern für Ihre Edge-Einheiten zu entwickeln. Zum Erstellen Ihrer Edge-Services können Sie jedes geeignete {{site.data.keyword.linux_notm}}-Basissystem, jede geeignete Programmiersprache sowie alle geeigneten Bibliotheken oder Dienstprogramme verwenden.
{:shortdesc}

Nachdem Sie Ihre Services mit einer Push-Operation übertragen, signiert und publiziert haben, verwendet {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) vollständig autonome Agenten auf Ihren Edge-Einheiten, um Ihre Services herunterzuladen, zu validieren, zu konfigurieren, zu installieren und zu überwachen.  

Edge-Services verwenden häufig Aufnahmeservices in der Cloud, um die Ergebnisse der Edge-Analyse zu speichern und weiter zu verarbeiten. Dieser Prozess umfasst auch den Entwicklungsworkflow für Edge- und Cloud-Code. 

{{site.data.keyword.ieam}} basiert auf dem Open-Source-Projekt [{{site.data.keyword.horizon_open}} ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://github.com/open-horizon/) und verwendet zum Ausführen einiger Prozesse den {{site.data.keyword.horizon}} {{site.data.keyword.linux_notm}}-Befehl `hzn`. 

## Vorbereitende Schritte
{: #service_containers_begin}

1. Konfigurieren Sie den Entwicklungshost zur Verwendung mit {{site.data.keyword.ieam}}. Installieren Sie dazu den {{site.data.keyword.horizon}}-Agenten auf Ihrem Host und registrieren Sie den Host bei {{site.data.keyword.horizon_exchange}}. Weitere Informationen finden Sie unter [{{site.data.keyword.horizon}}-Agent auf der Edge-Einheit installieren und beim 'Hello World'-Beispiel registrieren](../installing/registration.md).

2. Erstellen Sie eine [Docker Hub-ID ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://hub.docker.com/). Dieser Schritt ist erforderlich, da die Anweisungen in diesem Abschnitt die Publizierung des Service-Containers im Docker Hub beinhalten.

## Vorgehensweise
{: #service_containers_procedure}

Hinweis: Weitere Informationen zur Befehlssyntax finden Sie im Abschnitt [In diesem Dokument verwendete Konventionen](../../getting_started/document_conventions.md).

1. Als Sie die Schritte unter [{{site.data.keyword.horizon}}-Agent auf der Edge-Einheit installieren und beim 'Hello World'-Beispiel registrieren](../installing/registration.md) ausgeführt haben, haben Sie Ihre Exchange-Berechtigungsnachweise festgelegt. Überprüfen Sie, ob diese Berechtigungsnachweise noch korrekt festgelegt sind, indem Sie sicherstellen, dass der folgende Befehl keinen Fehler zurückgibt: 

  ```
    hzn exchange user list
    ```
  {: codeblock}

2. Wenn Sie {{site.data.keyword.macOS_notm}} als Entwicklungs-Host verwenden, müssen Sie Docker so konfigurieren, dass die Berechtigungsnachweise in `~/.docker` gespeichert werden. Gehen Sie dazu wie folgt vor:  

   1. Öffnen Sie den Docker-Dialog  **Preferences** (Vorgaben).
   2. Wählen Sie die Option **Securely store Docker logins in macOS keychain** (Docker-Anmeldungen sicher in macOS-Schlüsselkette speichern) ab.
  
     * Falls Sie dieses Feld nicht abwählen können, führen Sie die folgenden Schritte aus:
     
       1. Wählen Sie die Option **Include VM in Time Machine backups** (VM in Zeitmaschinenbackups einbeziehen) aus. 
       2. Wählen Sie die Option **Securely store Docker logins in macOS keychain** (Docker-Anmeldungen sicher in macOS-Schlüsselkette speichern) ab.
       3. (Optional) Wählen Sie die Option **Include VM in Time Machine backups** (VM in Zeitmaschinenbackups einbeziehen) ab.
       4. Klicken Sie auf **Apply & Restart** (Anwenden und erneut starten).
   3. Falls eine Datei namens `~/.docker/plaintext-passwords.json` vorhanden ist, entfernen Sie die Datei.   

3. Melden Sie sich beim Docker Hub mit der zuvor erstellten Docker Hub-ID an:

  ```
  export DOCKER_HUB_ID="<docker-hub-id>"
  echo "<docker-hub-kennwort>" | docker login -u $DOCKER_HUB_ID --password-stdin
  ```
  {: codeblock}

  Ausgabebeispiel:
  ```
  WARNING! Your password will be stored unencrypted in ~userName/.docker/config.json.
  Configure a credential helper to remove this warning. See
    https://docs.docker.com/engine/reference/commandline/login/#credentials-storeLogin Succeeded
    ```

4. Erstellen Sie ein kryptografisches Signierschlüsselpaar. Dadurch können Sie Services signieren, wenn Sie sie auf Exchange publizieren.  

   Hinweis: Dieser Schritt muss nur einmal ausgeführt werden.

  ```
  hzn key create "<companyname>" "<youremailaddress>"
  ```
  {: codeblock}
  
  Dabei wird `companyname` als Organisation laut x509 und `youremailaddress` als CN laut x509 verwendet. 

5. Installieren Sie einige Entwicklungstools:

  Unter **{{site.data.keyword.linux_notm}}**: 

  ```
  sudo apt install -y git jq make
  ```
  {: codeblock}

  Unter **{{site.data.keyword.macOS_notm}}**: 

  ```
  brew install git jq make
  ```
  {: codeblock}
  
  Hinweis: Nähere Informationen zur Installation von brew, falls erforderlich, finden Sie unter [Homebrew ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://brew.sh/).

## Nächste Schritte
{: #service_containers_what_next}

Verwenden Sie Ihre Berechtigungsnachweise und den Signierschlüssel, um die Entwicklungsbeispiele auszuführen. Diese Beispiele stellen dar, wie Sie einfache Edge-Services erstellen können, um sich mit den Grundlagen der Entwicklung für {{site.data.keyword.edge_devices_notm}} vertraut zu machen. 
