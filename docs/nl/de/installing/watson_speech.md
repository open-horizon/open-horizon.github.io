---

copyright:
years: 2019
lastupdated: "2020-2-25"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Watson Speech-To-Text
{: #watson-speech}

Dieser Service ist für das Wort 'Watson' empfangsbereit. Wenn der Service dieses Wort erkennt, zeichnet er einen Audioclip auf und sendet ihn an eine Instanz von Speech-To-Text.  Stoppwörter werden (optional) entfernt und der transkribierte Text wird an {{site.data.keyword.event_streams}} gesendet.

## Vorbereitende Schritte

Vergewissern Sie sich, dass Ihr System die folgenden Anforderungen erfüllt:

* Führen Sie die Schritte unter [Edge-Einheit vorbereiten](adding_devices.md) aus, um sich zu registrieren und die Registrierung zurückzunehmen.
* Auf Ihrem Raspberry Pi müssen eine USB-Soundkarte und ein Mikrofon installiert sein. 

Damit dieser Service ordnungsgemäß ausgeführt werden kann, sind eine Instanz von {{site.data.keyword.event_streams}} sowie IBM Speech to Text erforderlich. Anweisungen zum Bereitstellen einer Instanz von Event Streams finden Sie unter [Beispiel für den Prozentsatz der CPU-Belastung des Hosts (cpu2evtstreams)](../using_edge_services/cpu_load_example.md).  

Stellen Sie sicher, dass die erforderlichen Umgebungsvariablen für {{site.data.keyword.event_streams}} festgelegt sind.

```
echo "$EVTSTREAMS_API_KEY, $EVTSTREAMS_BROKER_URL"
```
{: codeblock}

Das von dem Beispiel verwendete Event Streams-Thema ist standardmäßig `myeventstreams`. Sie können jedoch ein beliebiges Thema verwenden, indem Sie die folgende Umgebungsvariable festlegen:

```
export EVTSTREAMS_TOPIC=<ihr_themaname>
```
{: codeblock}

## Instanz von IBM Speech to Text bereitstellen
{: #deploy_watson}

Wenn eine Instanz momentan bereitgestellt ist, müssen Sie die Zugriffsinformationen abrufen und die Umgebungsvariablen festlegen oder die folgenden Schritte ausführen:

1. Wechseln Sie zu IBM Cloud.
2. Klicken Sie auf **Ressource erstellen**.
3. Geben Sie im Suchfenster den Begriff `Speech to Text` ein.
4. Wählen Sie die Kachel `Speech to Text` aus.
5. Wählen Sie eine Region und einen Preistarif aus, geben Sie einen Servicenamen ein und klicken Sie auf **Erstellen**, um die Instanz einzurichten.
6. Klicken Sie nach Abschluss der Einrichtung auf die Instanz, notieren Sie die Berechtigungsnachweise 'API Key' (API-Schlüssel) und 'URL' und exportieren Sie sie als die folgende Umgebungsvariable:

    ```
    export STT_IAM_APIKEY=<speech-to-text-api-schlüssel>     export STT_URL=<speech-to-text-url>
    ```
    {: codeblock}

7. Anweisungen zum Testen des Speech-To-Text-Service finden Sie im Abschnitt 'Erste Schritte'.

## Edge-Einheit registrieren
{: #watson_reg}

Zur Ausführung dieses Beispiels für den watsons2text-Service auf Ihrem Edge-Knoten müssen Sie den Edge-Knoten für das Bereitstellungsmuster `IBM/pattern-ibm.watsons2text-arm` registrieren. Führen Sie die Schritte im Abschnitt [Watson Sprache-Text für IBM Event Streams Service mit Bereitstellungsmuster verwenden](https://github.com/open-horizon/examples/tree/master/edge/evtstreams/watson_speech2text#-using-the-ibm-watson-speech-to-text-to-ibm-event-streams-service-with-deployment-pattern) der Readme-Datei aus.

## Zusätzliche Informationen

Der Quellcode für das Beispiel `processtect` steht auch im Horizon-GitHub-Repository als Beispiel für die {{site.data.keyword.edge_notm}}-Entwicklung zur Verfügung. Diese Quelle enthält den Code für alle vier Services, die auf den Edge-Knoten für dieses Beispiel ausgeführt werden. 

Hierbei handelt es sich um die folgenden Services:

* Der Service [hotworddetect](https://github.com/open-horizon/examples/tree/master/edge/services/hotword_detection) ist empfangsbereit und erkennt das Stichwort Watson und zeichnet anschließend einen Audioclip auf und veröffentlicht ihn für den mqtt-Broker.
* Der Service [watsons2text](https://github.com/open-horizon/examples/tree/master/edge/evtstreams/watson_speech2text) empfängt einen Audioclip und sendet ihn an den IBM Speech to Text-Service und veröffentlicht den entschlüsselten Text an den mqtt-Broker.
* Der Service [stopwordremoval](https://github.com/open-horizon/examples/tree/master/edge/services/stopword_removal) wird ausgeführt, wenn ein WSGI-Server ein JSON-Objekt, wie z. B. {"text": "how are you today"}, ausführt und allgemeine Stoppwörter entfernt und {"result": "how you today"} zurückgibt.
* Der Service [mqtt2kafka](https://github.com/open-horizon/examples/tree/master/edge/services/mqtt2kafka) veröffentlicht Daten in {{site.data.keyword.event_streams}}, wenn er etwas über das mqtt-Thema empfängt, in dem er subskribiert ist.
* Der [mqtt_broker](https://github.com/open-horizon/examples/tree/master/edge/services/mqtt_broker) ist für die gesamte Kommunikation zwischen den Containern verantwortlich.

## Nächste Schritte

* Anweisungen zum Erstellen und Veröffentlichen einer eigenen Version des Offline-Voice-Assistant-Edge-Service finden Sie unter [Offline Voice Assistant Edge-Service](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/watson_speech2text/CreateService.md#-building-and-publishing-your-own-version-of-the-watson-speech-to-text-to-ibm-event-streams-service). Befolgen Sie die Schritte im Verzeichnis `watson_speech2text` des Open Horizon-Repositorys für Beispiele.

* Weitere Informationen finden Sie unter [Repository für Open Horizon-Beispiele](https://github.com/open-horizon/examples).
