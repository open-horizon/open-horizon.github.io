---

copyright:
years: 2020
lastupdated: "2020-04-09"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Image in Edge-Service umwandeln
{: #transform_image}

Dieses Beispiel führt Sie durch die Schritte zum Publizieren eines bereits vorhandenen Docker-Images als Edge-Service, zum Erstellen des zugehörigen Bereitstellungsmusters und zum Registrieren der Edge-Knoten für die Ausführung dieses Bereitstellungsmusters.
{:shortdesc}

## Vorbereitende Schritte
{: #quickstart_ex_begin}

Führen Sie die vorausgesetzten Schritte unter [Erstellung eines Edge-Service vorbereiten](service_containers.md) aus. Danach sollten die folgenden Umgebungsvariablen definiert, die folgenden Befehle installiert und die folgenden Dateien vorhanden sein:

```bash
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID" which git jq ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem cat /etc/default/horizon
```
{: codeblock}

## Vorgehensweise
{: #quickstart_ex_procedure}

**Hinweis:** Weitere Informationen zur Befehlssyntax finden Sie im Abschnitt [In diesem Dokument verwendete Konventionen](../getting_started/document_conventions.md).

1. Erstellen Sie ein Projektverzeichnis.

  1. Wechseln Sie auf dem Entwicklungshost in das Verzeichnis für das vorhandene Docker-Projekt. **Wenn Sie nicht über ein vorhandenes Docker-Projekt verfügen, aber dennoch mit diesem Beispiel fortfahren wollen**, können Sie die folgenden Befehle verwenden um eine einfache Dockerfile zu erstellen, die mit dem Rest dieses Verfahrens verwendet werden kann:

    ```bash
    cat << EndOfContent > Dockerfile     FROM alpine:latest     CMD while :; do echo "Hello, world."; sleep 3; done     EndOfContent
    ```
    {: codeblock}

  2. Erstellen Sie Edge-Service-Metadaten für Ihr Projekt:

    ```bash
    hzn dev service new -s myservice -V 1.0.0 -i $DOCKER_HUB_ID/myservice --noImageGen
    ```
    {: codeblock}

    Dieser Befehl erstellt die Datei **horizon/service.definition.json** zur Beschreibung Ihres Service und die Datei **horizon/pattern.json** zur Beschreibung des Bereitstellungsmusters. Sie können diese Dateien öffnen und ihren Inhalt durchsuchen.

2. Erstellen und testen Sie Ihren Service

  1. Erstellen Sie Ihr Docker-Image. Der Name des Images muss mit der in der Datei **horizon/service.definition.json** referenzierten Angabe übereinstimmen.

    ```bash
    eval $(hzn util configconv -f horizon/hzn.json)     export ARCH=$(hzn architecture)     sudo docker build -t "${DOCKER_IMAGE_BASE}_$ARCH:$SERVICE_VERSION" .
    unset DOCKER_IMAGE_BASE SERVICE_NAME SERVICE_VERSION
    ```
    {: codeblock}

  2. Führen Sie diesen Service-Container-Image in der simulierten {{site.data.keyword.horizon}}-Agentenumgebung aus:

    ```bash
    hzn dev service start -S
    ```
    {: codeblock}

  3. Überprüfen Sie, ob Ihr Service-Container ausgeführt wird:

    ```bash
    sudo docker ps
    ```
    {: codeblock}

  4. Zeigen Sie die Umgebungsvariablen an, die an den Container übergeben wurden, als er gestartet wurde. (Dies sind dieselben Umgebungsvariablen, die der vollständige Agent an den Service-Container übergibt.)

    ```bash
    sudo docker inspect $(sudo docker ps -q --filter name=myservice) | jq '.[0].Config.Env'
    ```
    {: codeblock}

  5. Zeigen Sie das Protokoll des Service-Containers wie folgt an:

    Unter **{{site.data.keyword.linux_notm}}**:

    ```bash
    sudo tail -f /var/log/syslog | grep myservice[[]
    ```
    {: codeblock}

    Unter **{{site.data.keyword.macOS_notm}}**:

    ```bash
    sudo docker logs -f $(sudo docker ps -q --filter name=myservice)
    ```
    {: codeblock}

  6. Stoppen Sie den Service wie folgt:

    ```bash
    hzn dev service stop
    ```
    {: codeblock}

3. Publizieren Sie Ihren Service in {{site.data.keyword.edge_notm}}. Sie haben bestätigt, dass Ihr Service-Code in der simulierten Agentenumgebung erwartungsgemäß ausgeführt wird. Publizieren Sie den Service nun in {{site.data.keyword.horizon_exchange}}, damit er für die Bereitstellung auf den Edge-Knoten verfügbar ist.

  Der folgende **publish**-Befehl verwendet die Datei **horizon/service.definition.json** und Ihr Schlüsselpaar, um den Service zu signieren und in {{site.data.keyword.horizon_exchange}} zu publizieren. Außerdem wird Ihr Image mit einer Push-Operation in den Docker Hub übertragen.

  ```bash
  hzn exchange service publish -f horizon/service.definition.json   hzn exchange service list
  ```
  {: codeblock}

4. Publizieren Sie ein Bereitstellungsmuster für den Service. Dieses Bereitstellungsmuster kann von Edge-Knoten verwendet werden, um {{site.data.keyword.edge_notm}} zu veranlassen, den Service auf den Edge-Knoten bereitzustellen:

  ```bash
  hzn exchange pattern publish -f horizon/pattern.json     hzn exchange pattern list
  ```
  {: codeblock}

5. Registrieren Sie den Edge-Knoten für die Ausführung des Bereitstellungsmusters.

  1. Auf dieselbe Weise, in der Sie zuvor die Edge-Knoten bei öffentlichen Bereitstellungsmustern aus der **IBM** Organisation registriert haben, müssen Sie Ihren Edge-Knoten nun für das Bereitstellungsmuster registrieren, das Sie unter der eigenen Organisation publiziert haben.

    ```bash
    hzn register -p pattern-myservice-$(hzn architecture) -s myservice --serviceorg $HZN_ORG_ID
    ```
    {: codeblock}

  2. Listen Sie den Edge-Service des Docker-Containers auf, der als Ergebnis gestartet wurde:

    ```bash
    sudo docker ps
    ```
    {: codeblock}

  3. Zeigen Sie die Ausgabe des Edge-Service 'myservice' an:

    ```bash
    sudo hzn service log -f myservice
    ```
    {: codeblock}

6. Zeigen Sie den Knoten, den Service und das Muster, den bzw. das Sie erstellt haben, in der {{site.data.keyword.edge_notm}}-Konsole an. Sie können die URL der Konsole wie folgt anzeigen:

  ```bash
  echo "$(awk -F '=|edge-exchange' '/^HZN_EXCHANGE_URL/ {print $2}' /etc/default/horizon)edge"
  ```
  {: codeblock}

7. Heben Sie die Registrierung Ihres Edge-Knotens auf und stoppen Sie den Service **myservice**:

  ```bash
  hzn unregister -f
  ```
  {: codeblock}

## Nächste Schritte
{: #quickstart_ex_what_next}

* Unter [Edge-Services bereitstellen](../using_edge_services/detailed_policy.md) finden Sie weitere Beispiele für Edge-Services, mit denen Sie arbeiten können.
