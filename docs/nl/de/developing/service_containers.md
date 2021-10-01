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

{{site.data.keyword.ieam}} basiert auf dem Open-Source-Projekt [{{site.data.keyword.horizon_open}}](https://github.com/open-horizon/) und verwendet den Befehl `hzn` {{site.data.keyword.horizon}} {{site.data.keyword.linux_notm}}, um einige Prozesse auszuführen.

## Vorbereitende Schritte
{: #service_containers_begin}

1. Konfigurieren Sie den Entwicklungshost zur Verwendung mit {{site.data.keyword.ieam}}. Installieren Sie dazu den {{site.data.keyword.horizon}}-Agenten auf Ihrem Host und registrieren Sie den Host bei {{site.data.keyword.horizon_exchange}}. Weitere Informationen finden Sie unter [{{site.data.keyword.horizon}}-Agent auf der Edge-Einheit installieren und beim 'Hello World'-Beispiel registrieren](../installing/registration.md).

2. Erstellen Sie eine [Docker Hub](https://hub.docker.com/)-ID. Dieser Schritt ist erforderlich, da die Anweisungen in diesem Abschnitt die Publizierung des Service-Containers im Docker Hub beinhalten.

## Vorgehensweise
{: #service_containers_procedure}

**Hinweis:** Weitere Informationen zur Befehlssyntax finden Sie im Abschnitt [In diesem Dokument verwendete Konventionen](../getting_started/document_conventions.md).

1. Als Sie die Schritte unter [{{site.data.keyword.horizon}}-Agent auf der Edge-Einheit installieren und beim 'Hello World'-Beispiel registrieren](../installing/registration.md) ausgeführt haben, haben Sie Ihre Exchange-Berechtigungsnachweise festgelegt. Überprüfen Sie, ob diese Berechtigungsnachweise noch korrekt festgelegt sind, indem Sie sicherstellen, dass der folgende Befehl keinen Fehler zurückgibt:

  ```
  hzn exchange user list
  ```
  {: codeblock}

2. Wenn Sie {{site.data.keyword.macOS_notm}} als Entwicklungshost verwenden, setzen Sie die Berechtigungsnachweise für die Docker-Hub-Registry in `~/.docker/plaintext-passwords.json` ein:

  ```
  export DOCKER_HUB_ID="&amp;TWBLT;yourdockerhubid&gt;" export DOCKER_HUB_PW="&amp;TWBLT;yourdockerhubpassword&gt;" echo "{ \"auths\": { \"https://index.docker.io/v1/\": { \"auth\": \"$(printf "${DOCKER_HUB_ID:?}:${DOCKER_HUB_PW:?}" | base64) \"}}}" &gt; ~/.docker/plaintext-passwords.json

  ```
  {: codeblock}

3. Melden Sie sich beim Docker Hub mit der zuvor erstellten Docker Hub-ID an:

  ```
  export DOCKER_HUB_ID="&amp;TWBLT;yourdockerhubid&gt;" export DOCKER_HUB_PW="&amp;TWBLT;yourdockerhubpassword&gt;" echo "$DOCKER_HUB_PW" | docker login -u $DOCKER_HUB_ID --password-stdin
  ```
  {: codeblock}

  Ausgabebeispiel:
  ```
  WARNING! Your password will be stored unencrypted in ~userName/.docker/config.json.
  Configure a credential helper to remove this warning. See     https://docs.docker.com/engine/reference/commandline/login/#credentials-store

  Login Succeeded
  ```

4. Erstellen Sie ein kryptografisches Signierschlüsselpaar. Dadurch können Sie Services signieren, wenn Sie sie auf Exchange publizieren. 

   **Hinweis:** Dieser Schritt muss nur einmal ausgeführt werden.

  ```
  hzn key create "<unternehmensname>" "<ihre_e-mail-adresse>"
  ```
  {: codeblock}
  
  Dabei wird `unternehmensname` als Organisation laut x509 und `ihre_e-mail-adresse` als CN laut x509 verwendet.

5. Installieren Sie einige Entwicklungstools:

  Unter **{{site.data.keyword.linux_notm}}** (für Ubuntu-/Debian-Distributionen):

  ```
  sudo apt install -y git jq make
  ```
  {: codeblock}

  Unter **{{site.data.keyword.macOS_notm}}**:

  ```
  brew install git jq make
  ```
  {: codeblock}
  
  **Hinweis**: Details zur Installation von Brew finden Sie unter [homebrew](https://brew.sh/), falls erforderlich.

## Nächste Schritte
{: #service_containers_what_next}

* Verwenden Sie Ihre Berechtigungsnachweise und den Signierschlüssel, um die [Entwicklungsbeispiele](../OH/docs/developing/developing.md) auszuführen. Diese Beispiele stellen dar, wie Sie einfache Edge-Services erstellen können, um sich mit den Grundlagen der Entwicklung für {{site.data.keyword.edge_notm}} vertraut zu machen.
* Wenn Sie bereits über ein Docker-Image verfügen, das von {{site.data.keyword.edge_notm}} für Edge-Knoten bereitgestellt werden soll, lesen Sie den Abschnitt [Image in Edge-Service umwandeln](transform_image.md).
