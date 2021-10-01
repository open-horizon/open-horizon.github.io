---

copyright:
years: 2019
lastupdated: "2019-11-12"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Offline-Sprachsteuerung
{: #offline-voice-assistant}

Die Offline-Sprachsteuerung zeichnet jede Minute einen fünf Sekunden langen Audioclip auf, konvertiert diesen Audioclip lokal auf der Edge-Einheit in Text und weist die Hostmaschine an, den Befehl auszuführen und die Ausgabe zu sprechen. 

## Vorbereitende Schritte
{: #before_beginning}

Vergewissern Sie sich, dass Ihr System die folgenden Anforderungen erfüllt:

* Führen Sie die Schritte unter [Edge-Einheit vorbereiten](../installing/adding_devices.md) aus, um sich zu registrieren und die Registrierung zurückzunehmen.
* Auf Ihrem Raspberry Pi müssen eine USB-Soundkarte und ein Mikrofon installiert sein. 

## Edge-Einheit registrieren
{: #reg_edge_device}

Zur Ausführung dieses Beispiels für den `processtext`-Service auf Ihrem Edge-Knoten müssen Sie den Edge-Knoten für das Bereitstellungsmuster `IBM/pattern-ibm.processtext` registrieren. 

Führen Sie die Schritte im Abschnitt "Offline Voice Assistant-Beispiel-Edge Service mit Bereitstellungsmuster verwenden" [Offline Voice Assistant-Beispiel-Edge Service mit Bereitstellungsmuster verwenden](https://github.com/open-horizon/examples/tree/master/edge/services/processtext#-using-the-offline-voice-assistant-example-edge-service-with-deployment-pattern) in der Readme-Datei aus.

## Zusätzliche Informationen
{: #additional_info}

Der Quellcode für das Beispiel `processtext` steht auch im Horizon-GitHub-Repository als Beispiel für die {{site.data.keyword.edge_notm}}-Entwicklung zur Verfügung. Diese Quelle enthält den Code für alle Services, die auf den Edge-Knoten für dieses Beispiel ausgeführt werden. 

Diese [Open Horizon-Beispiel](https://github.com/open-horizon/examples/tree/master/edge/services/voice2audio)-Services beinhalten:

* Der Service [voice2audio](https://github.com/open-horizon/examples/tree/master/edge/services/voice2audio) zeichnet den Fünf-Sekunden-Audioclip auf und veröffentlicht ihn an den mqtt-Broker.
* Der Service [audio2text](https://github.com/open-horizon/examples/tree/master/edge/services/audio2text) verwendet den Audioclip und konvertiert ihn mithilfe von PocketSphinx in Offline-Text.
* Der Service [processtext](https://github.com/open-horizon/examples/tree/master/edge/services/processtext) verwendet den Text und versucht, den aufgezeichneten Befehl auszuführen.
* Der Service [text2speech](https://github.com/open-horizon/examples/tree/master/edge/services/text2speech) spielt die Ausgabe des Befehls über einen Lautsprecher.
* Der [mqtt_broker](https://github.com/open-horizon/examples/tree/master/edge/services/mqtt_broker) verwaltet die gesamte Kommunikation zwischen den Containern.

## Nächste Schritte
{: #what_next}

Anweisungen zum Erstellen und Veröffentlichen einer eigenen Watson-Sprache-Text-Version finden Sie in den Verzeichnisschritten `processtext` im Repository [Open Horizon-Beispiele](https://github.com/open-horizon/examples/blob/master/edge/services/processtext/CreateService.md#-building-and-publishing-your-own-version-of-the-offline-voice-assistant-edge-service). 
