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

* Führen Sie die Schritte unter [Edge-Einheit vorbereiten](adding_devices.md) aus, um sich zu registrieren und die Registrierung zurückzunehmen. 
* Auf Ihrem Raspberry Pi müssen eine USB-Soundkarte und ein Mikrofon installiert sein.  

## Edge-Einheit registrieren
{: #reg_edge_device}

Zur Ausführung dieses Beispiels für den `processtext`-Service auf Ihrem Edge-Knoten müssen Sie den Edge-Knoten für das Bereitstellungsmuster `IBM/pattern-ibm.processtext` registrieren.  

Führen Sie die Schritte im Abschnitt [Using the Offline Voice Assistant Example Edge Service with Deployment Pattern ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://github.com/open-horizon/examples/tree/master/edge/services/processtext#-using-the-offline-voice-assistant-example-edge-service-with-deployment-pattern) der Readme-Datei aus. 

## Zusätzliche Informationen
{: #additional_info}

Der Quellcode für das Beispiel `processtext` steht auch im Horizon-GitHub-Repository als Beispiel für die {{site.data.keyword.edge_devices_notm}}-Entwicklung zur Verfügung. Diese Quelle enthält den Code für alle Services, die auf den Edge-Knoten für dieses Beispiel ausgeführt werden.  

Zu diesen Services für [Open Horizon-Beispiele ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://github.com/open-horizon/examples/tree/master/edge/services/voice2audio) gehören die folgenden: 

* Der Service [voice2audio ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://github.com/open-horizon/examples/tree/master/edge/services/voice2audio) zeichnet einen fünf Sekunden langen Audioclip auf und publiziert ihn auf dem MQTT-Broker. 
* Der Service [audio2text ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://github.com/open-horizon/examples/tree/master/edge/services/audio2text) verwendet diesen Audioclip und konvertiert ihn mithilfe von PocketSphinx offline in Text. 
* Der Service [processtext ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://github.com/open-horizon/examples/tree/master/edge/services/processtext) verwendet den Text und versucht, den aufgezeichneten Befehl auszuführen. 
* Der Service [text2speech ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://github.com/open-horizon/examples/tree/master/edge/services/text2speech) gibt die Ausgabe des Befehls durch einen Lautsprecher wieder. 
* Der [mqtt_broker ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://github.com/open-horizon/examples/tree/master/edge/services/mqtt_broker) verwaltet die gesamte containerübergreifende Kommunikation. 

## Nächste Schritte
{: #what_next}

Anweisungen zum Erstellen und Publizieren Ihrer eigenen Version von Watson Speech-To-Text finden Sie in den Schritten im Verzeichnis `processtext` des [Open Horizon-Repositorys für Beispiele ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://github.com/open-horizon/examples/blob/master/edge/services/processtext/CreateService.md#-building-and-publishing-your-own-version-of-the-offline-voice-assistant-edge-service). 
