---

copyright:
years: 2020
lastupdated: "2020-02-06"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# CPU-Auslastung für {{site.data.keyword.message_hub_notm}}
{: #cpu_load_ex}

'Prozentsatz der CPU-Belastung des Hosts' ist ein Beispiel für ein Bereitstellungsmuster, das die Daten zum Prozentsatz der CPU-Belastung nutzt und diese über IBM Event Streams verfügbar macht. 

Dieser Edge-Service fragt wiederholt die CPU-Belastung der Edge-Einheit ab und sendet die zurückgegebenen Daten an [IBM Event Streams ![Wird auf einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird auf einer neuen Registerkarte geöffnet")](https://www.ibm.com/cloud/event-streams). Dieser Edge-Service kann auf jedem beliebigen Edge-Knoten ausgeführt werden, da er keine spezielle Sensorhardware benötigt. 

Bevor Sie diese Task ausführen, müssen Sie eine Registrierung durchführen und die Registrierung zurücknehmen. Führen Sie dazu die unter [Horizon-Agent auf der Edge-Einheit installieren und beim 'Hello World'-Beispiel registrieren](registration.md) beschriebenen Schritte aus.

Damit Sie mehr Erfahrungen mit einem realistischeres Szenario sammeln können, veranschaulicht das Beispiel 'cpu2evtstreams' weitere Aspekte eines normalen Edge-Service, wie beispielsweise die folgenden:

* Dynamische Daten der Edge-Einheit abfragen
* Daten der Edge-Einheit analysieren (`cpu2evtstreams` berechnet beispielsweise einen gleitenden Durchschnitt der CPU-Belastung) 
* Verarbeitete Daten an einen zentralen Datenaufnahmeservice senden
* Übernahme von Berechtigungsnachweisen für den Ereignisstrom automatisieren, sodass die Datenübertragung sicher authentifiziert wird. 

## Vorbereitende Schritte
{: #deploy_instance}

Bevor Sie den Edge-Service 'cpu2evtstreams' bereitstellen können, muss eine Instanz von {{site.data.keyword.message_hub_notm}} in der Cloud ausgeführt werden, um die Daten des Edge-Service zu empfangen. Jedes Mitglied Ihrer Organisation kann eine einzelne {{site.data.keyword.message_hub_notm}}-Instanz gemeinsam nutzen. Wenn die Instanz bereits bereitgestellt ist, müssen Sie die Zugriffsinformationen abrufen und die
Umgebungsvariablen festlegen. 

### {{site.data.keyword.message_hub_notm}} in {{site.data.keyword.cloud_notm}} bereitstellen 
{: #deploy_in_cloud}

1. Wechseln Sie zu {{site.data.keyword.cloud_notm}}. 

2. Klicken Sie auf **Ressource erstellen**. 

3. Geben Sie im Suchfenster den Begriff `Event Streams` ein. 

4. Wählen Sie die Kachel **Event Streams** aus. 

5. Geben Sie unter **Event Streams** einen Servicenamen ein, wählen Sie einen Standort und einen Preistarif aus und klicken Sie auf **Erstellen**, um die Instanz einzurichten. 

6. Klicken Sie auf die Instanz, wenn die Einrichtung abgeschlossen ist. 

7. Erstellen Sie ein Thema. Klicken Sie dazu auf das Pluszeichen (+) und geben Sie der Instanz den Namen `cpu2evtstreams`. 

8. Sie können Berechtigungsnachweise in Ihrem Terminal erstellen oder Berechtigungsnachweise abrufen wenn sie bereits erstellt sind. Klicken Sie auf **Serviceberechtigungsnachweise > Neue Berechtigungsnachweise**, um Berechtigungsnachweise zu erstellen. Erstellen Sie eine Datei mit dem Namen `event-streams.cfg`, in der die neuen Berechtigungsnachweise ähnlich wie im folgenden Codeblock formatiert sind. Obwohl diese Berechtigungsnachweise nur einmal erstellt werden müssen, sollten Sie diese Datei zur zukünftigen Verwendung durch Sie selbst oder Ihre Teammitglieder speichern, falls diese Zugriff auf {{site.data.keyword.event_streams}} benötigen. 

   ```
    EVTSTREAMS_API_KEY="<Wert des API-Schlüssels>"
    EVTSTREAMS_BROKER_URL="<alle Werte für 'kafka_brokers_sasl' in einer einzelnen Zeichenfolge, getrennt durch Kommas>"
    ```
   {: codeblock}
        
   Beispiel für das Teilfenster zum Anzeigen der Berechtigungsnachweise: 

   ```
   EVTSTREAMS_BROKER_URL=broker-4-x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-3-  x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-2-x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-0-x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-1-x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-5-x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093
   ```
   {: codeblock}

9. Legen Sie die folgenden Umgebungsvariablen in der Shell fest, nachdem Sie die Datei `event-streams.cfg` erstellt haben: 

   ```
   eval export $(cat event-streams.cfg)
   ```
   {: codeblock}

### {{site.data.keyword.message_hub_notm}} in {{site.data.keyword.cloud_notm}} testen
{: #testing}

1. Installieren Sie `kafkacat` (https://linuxhostsupport.com/blog/how-to-install-apache-kafka-on-ubuntu-16-04/).

2. Geben Sie in einem Terminal den folgenden Befehl ein, um das Thema `cpu2evtstreams` zu subskribieren: 

    ```
    kafkacat -C -q -o end -f "%t/%p/%o/%k: %s\n" -b $EVTSTREAMS_BROKER_URL -X api.version.request=true -X security.protocol=sasl_ssl -X sasl.mechanisms=PLAIN -X sasl.username=token -X sasl.password=$EVTSTREAMS_API_KEY -t cpu2evtstreams
    ```
    {: codeblock}

3. Publizieren Sie in einem zweiten Terminal Testinhalte im Thema `cpu2evtstreams`, um sie in der ursprünglichen Konsole anzuzeigen. Beispiel:

    ```
    echo 'hi there' | kafkacat -P -b $EVTSTREAMS_BROKER_URL -X api.version.request=true -X security.protocol=sasl_ssl -X sasl.mechanisms=PLAIN -X sasl.username=token -X sasl.password=$EVTSTREAMS_API_KEY -t cpu2evtstreams
    ```
    {: codeblock}

## Edge-Einheit registrieren
{: #reg_device}

Zur Ausführung dieses Beispiels für den cpu2evtstreams-Service auf Ihrem Edge-Knoten müssen Sie den Edge-Knoten für das Bereitstellungsmuster `IBM/pattern-ibm.cpu2evtstreams` registrieren. Führen Sie die Schritte im **ersten** Abschnitt unter [Horizon CPU To {{site.data.keyword.message_hub_notm}} ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/cpu2evtstreams/README.md) aus. 

## Zusätzliche Informationen
{: #add_info}

Der Quellcode für das CPU-Beispiel ist im [{{site.data.keyword.horizon_open}}-Beispielrepository ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://github.com/open-horizon/examples) als Beispiel für die Entwicklung von Edge-Services für {{site.data.keyword.edge_devices_notm}} verfügbar. Diese Quelle enthält den Code
für alle drei Services, die auf dem Edge-Knoten für dieses Beispiel ausgeführt werden. 

  * Den Service 'cpu', der die Daten zum Prozentsatz der CPU-Belastung als REST-Service auf einem lokalen privaten Docker-Netz bereitstellt. Weitere Einzelheiten hierzu finden Sie in den Informationen zum [Horizon-Service für die Prozentsätze zur CPU-Belastung ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://github.com/open-horizon/examples/tree/master/edge/services/cpu_percent).
  * Den Service 'gps', der (sofern verfügbar) Standortinformationen von GPS-Hardwarekomponenten oder von einem Standort bereitstellt, der aus der IP-Adresse des Edge-Knotens abgeleitet wurde. Die Standortdaten werden als REST-Service in einem lokalen privaten Docker-Netz bereitgestellt. Weitere Einzelheiten hierzu finden Sie in den Informationen zum [Horizon-GPS-Service ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://github.com/open-horizon/examples/tree/master/edge/services/gps).
  * Den Service 'cpu2evtstreams', der die REST-APIs verwendet, die von den anderen beiden Services zur Verfügung gestellt werden. Dieser Service sendet die kombinierten Daten an einen {{site.data.keyword.message_hub_notm}}-Kafka-Broker in der Cloud. Weitere Einzelheiten zu dem Service finden Sie in den Informationen zum [{{site.data.keyword.horizon}}-Service zum Senden von Daten zur CPU-Belastung an {{site.data.keyword.message_hub_notm}} ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/cpu2evtstreams/cpu2evtstreams.md). 
  * Weitere Informationen zu {{site.data.keyword.message_hub_notm}} finden Sie unter [Event Streams - Überblick ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://www.ibm.com/cloud/event-streams?mhsrc=ibmsearch_a&mhq=event%20streams). 

## Nächste Schritte
{: #cpu_next}

Wenn Sie eigene Software auf einem Edge-Knoten bereitstellen wollen, müssen Sie eigene Edge-Services und zugehörige Bereitstellungsmuster oder Bereitstellungsrichtlinien erstellen. Weitere Informationen finden Sie unter [Edge-Services mit {{site.data.keyword.edge_devices_notm}} entwickeln](../developing/developing.md). 
