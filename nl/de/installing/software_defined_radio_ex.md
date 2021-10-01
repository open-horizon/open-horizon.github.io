---

copyright:
years: 2020
lastupdated: "2020-02-5" 

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Edge-Verarbeitung für Software-Defined Radio (SDR)
{: #defined_radio_ex}

Im vorliegenden Beispiel wird SDR (Software-Defined Radio; softwaredefinierte Hochfrequenzsignalverarbeitung) als Beispiel für die Edge-Verarbeitung erläutert. Mit SDR können Sie Rohdaten über das gesamte Funkspektrum zur Verarbeitung an einen Cloud-Server senden. Der Edge-Knoten verarbeitet die Daten lokal und sendet dann eine reduzierte Menge höherwertiger Daten zur weiteren Verarbeitung an einen Cloud-Verarbeitungsservice.
{:shortdesc}

Im folgenden Diagramm wird die Architektur dieses SDR-Beispiels dargestellt:

<img src="../OH/docs/images/edge/08_sdrarch.svg" style="margin: 3%" alt="Example architecture">

Die Edge-Verarbeitung für Software-Defined Radio (SDR) ist ein mit allen Funktionen versehenes Beispiel, mit dem Audiodaten einer Funkstation genutzt, Sprachdaten extrahiert und die extrahierten Sprachdaten in Text umgewandelt werden können. Das Beispiel führt Stimmungsanalysen für den Text aus und stellt die gewonnenen Daten und Ergebnisse über eine Benutzerschnittstelle bereit, in der Sie die Details zu den Daten aller Edge-Knoten anzeigen können. Verwenden Sie dieses Beispiel, um mehr über die Edge-Verarbeitung zu erfahren.

Mit SDR werden Funksignale über Digitalschaltungen in der CPU eines Computers empfangen und an die dafür vorgesehene Gruppe spezialisierter Analogschaltkreise weitergeleitet. Diese Analogschaltkreise werden normalerweise durch die Bandbreite des Funkspektrums beschränkt, das empfangen werden kann. Ein analoger Funkempfänger, der Signale von Funkstationen mit Frequenzmodulation (FM) empfangen kann, ist z. B. nicht in der Lage, Funksignale aus einem anderen Bereich des Funkspektrums zu empfangen. Mit SDR kann auf große Teile dieses Spektrums zugegriffen werden. Falls Sie nicht über die SDR-Hardware verfügen, können Sie Testdaten verwenden. Wenn Sie die Testdaten verwenden, wird das Audiomaterial aus dem Internet-Datenstrom so verwendet, als würde es über FM (Frequenzmodulation) übertragen und auf Ihrem Edge-Knoten empfangen werden.

Bevor Sie diese Task ausführen, müssen Sie Ihre Edge-Einheit registrieren und die Registrierung wieder zurücknehmen. Führen Sie dazu die unter [Agent installieren](registration.md) beschriebenen Schritte aus.

Dieser Code besteht aus den folgenden primären Komponenten.

|Komponente|Beschreibung|
|---------|-----------|
|[sdr-Service](https://github.com/open-horizon/examples/tree/master/edge/services/sdr)|Dieser Low-Level-Service wird für den Zugriff auf die Hardware des Edge-Knotens verwendet.|
|[ssdr2evtstreams-Service](https://github.com/open-horizon/examples/tree/master/edge/evtstreams/sdr2evtstreams)|Dieser High-Level-Service dient zum Empfangen von Daten des Low-Level-Service 'sdr' und zur Ausführung lokaler Analysen der Daten auf dem Edge-Knoten. Der Service 'sdr2evtstreams' sendet die verarbeiteten Daten dann an die Cloud-Back-End-Software.|
|[Cloud-Backend-Software](https://github.com/open-horizon/examples/tree/master/cloud/sdr)|Die Cloud-Back-End-Software dient zum Empfangen von Daten der Edge-Knoten zur weiterführenden Analyse. Die Back-End-Implementierung kann anschließend eine Übersicht der Edge-Knoten und weitere Daten in einer webbasierten Benutzerschnittstelle bereitstellen.|
{: caption="Tabelle 1. Primäre SDR-Komponenten für {{site.data.keyword.message_hub_notm}}" caption-side="top"}

## Einheit registrieren

Obwohl dieser Service in jeder beliebigen Edge-Einheit mithilfe von Testdaten ausgeführt werden kann, sollten Sie bei Verwendung einer Edge-Einheit wie Raspberry Pi mit der SDR-Hardware zunächst ein Kernelmodul für die Unterstützung Ihrer SDR-Hardware konfigurieren. Sie müssen dieses Modul manuell konfigurieren. Docker-Container können in ihrem Kontext eine andere Linux-Distribution einrichten, der Container kann jedoch keine Kernelmodule installieren. 

Führen Sie die folgenden Schritte aus, um dieses Modul zu konfigurieren:

1. Erstellen Sie als Rootbenutzer eine Datei mit dem Namen `/etc/modprobe.d/rtlsdr.conf`.
   ```
   sudo nano /etc/modprobe.d/rtlsdr.conf
   ```
   {: codeblock}

2. Fügen Sie die folgenden Zeilen zur Datei hinzu:
   ```
   blacklist rtl2830      blacklist rtl2832      blacklist dvb_usb_rtl28xxu
   ```
   {: codeblock}

3. Speichern Sie die Datei und führen Sie einen Neustart durch, bevor Sie fortfahren:
   ```
   sudo reboot
   ```
   {: codeblock}   

4. Legen Sie den folgenden API-Schlüssel für {{site.data.keyword.message_hub_notm}} in Ihrer Umgebung fest. Dieser Schlüssel wird zur Verwendung im vorliegenden Beispiel erstellt und verwendet, um die verarbeiteten Daten, die von Ihrem Edge-Knoten erfasst wurden, für die SDR-Benutzerschnittstelle von IBM bereitzustellen.
   ```
   export EVTSTREAMS_API_KEY=X2e8cSjbDAMk-ztJLaoi3uffy8qsQTnZttUjcHCfm7cp     export EVTSTREAMS_BROKER_URL=broker-3-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-5-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-4-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-1-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-0-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-2-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093
   ```
   {: codeblock}

5. Zur Ausführung dieses Beispiels für den Service 'sdr2evtstreams' auf Ihrem Edge-Knoten müssen Sie den Edge-Knoten für das Bereitstellungsmuster 'IBM/pattern-ibm.cpu2evtstreams' registrieren. Führen Sie die Schritte unter [Voraussetzungen für die Verwendung von SDR für IBM Event Streams-Beispiel-Edge-Service](https://www.ibm.com/links?url=https%3A%2F%2Fgithub.com%2Fopen-horizon%2Fexamples%2Ftree%2Fmaster%2Fedge%2Fevtstreams%2Fsdr2evtstreams) aus.

6. Überprüfen Sie die Beispiel-Webbenutzerschnittstelle, um festzustellen, ob Ihr Edge-Knoten Ergebnisse sendet. 

## SDR-Implementierungsdetails

### Low-Level-Service 'sdr'
{: #sdr}

In der niedrigsten Ebene des Software-Stacks für diesen Service ist die Implementierung des Service `sdr` enthalten. Dieser Service dient zum Zugriff auf die lokale SDR-Hardware über die gängige Bibliothek `librtlsdr`, die abgeleiteten Dienstprogramme `rtl_fm` und `rtl_power` sowie den Dämon `rtl_rpcd`. Weitere Informationen zu der Bibliothek `librtlsdr` finden Sie unter [librtlsdr](https://github.com/librtlsdr/librtlsdr).

Der Service `sdr` steuert die SDR-Hardware direkt und dient zur Anpassung der Hardware an eine bestimmte Frequenz, über die die übertragenen Daten empfangen werden, oder zur Messung der Signalstärke in einem angegebenen Spektrum. Ein typischer Arbeitsablauf für den Service umfasst die Anpassung des Systems an eine bestimmte Frequenz zum Empfang von Daten einer Station, die mit dieser Frequenz sendet. Anschließend kann der Service die erfassten Daten verarbeiten.

### High-Level-Service 'sdr2evtstreams'
{: #sdr2evtstreams}

Die Implementierung des High-Level-Service `sdr2evtstreams` verwendet die REST-API des Service `sdr` und die REST-API des Service `gps` und als Übertragungsmedium das lokale private virtuelle Docker-Netz. Der Service `sdr2evtstreams` empfängt Daten aus dem Service `sdr` und führt für die Daten lokal bestimmte Inferenzen durch, um die besten Stationen für Sprachdaten auszuwählen. Anschließend verwendet der Service `sdr2evtstreams` Kafka, um Audioclips mithilfe von {{site.data.keyword.message_hub_notm}} in der Cloud zu publizieren.

### IBM Functions
{: #ibm_functions}

IBM Functions orchestriert die Cloudseite der SDR-Beispielanwendung. IBM Functions basiert auf OpenWhisk und ermöglicht Ihnen die serverunabhängige Datenverarbeitung. Die serverunabhängige Datenverarbeitung ermöglicht die Bereitstellung von Codekomponenten ohne eine unterstützende Infrastruktur wie z. B. ein Betriebssystem oder ein Programmiersprachensystem. Mit IBM Functions können Sie sich auf die Entwicklung des eigenen Codes konzentrieren und die Skalierung, Sicherheitsaspekte und die kontinuierliche Wartung aller anderen Komponenten IBM überlassen. Es muss keine Hardware bereitgestellt werden und es sind auch keine virtuellen Maschinen (VMs) und Container erforderlich.

Codekomponenten für die serverunabhängige Datenverarbeitung sind so konfiguriert, dass sie als Reaktion auf bestimmte Ereignisse ausgelöst (ausgeführt) werden. Im vorliegenden Beispiel wird als Auslöserereignis der Empfang von Nachrichten Ihrer Edge-Knoten in {{site.data.keyword.message_hub_notm}} eingesetzt, wenn Audioclips von Edge-Knoten in {{site.data.keyword.message_hub_notm}} publiziert werden. Die Beispielaktionen werden ausgelöst, um die Daten einzulesen und entsprechend zu reagieren. Mit dem Service IBM Watson Speech-To-Text (STT) werden die eingehenden Audiodaten in Text konvertiert. Anschließend wird dieser Text an den Service IBM Watson Natural Language Understanding (NLU) gesendet, um die Stimmung zu analysieren, die in den im Text enthaltenen Substantiven ausgedrückt wird. Weitere Informationen finden Sie im Abschnitt [Aktionscode für IBM Funktionen](https://github.com/open-horizon/examples/blob/master/cloud/sdr/data-processing/ibm-functions/actions/msgreceive.js).

### IBM Datenbank
{: #ibm_database}

Der IBM Functions-Aktionscode wird mit der Speicherung der berechneten Stimmungsergebnisse in IBM Datenbanken abgeschlossen. Die Web-Server- und die Client-Software stellen diese Daten dann über die Datenbank in den Web-Browsern der Benutzer bereit.

### Webschnittstelle
{: #web_interface}

Die Webbenutzerschnittstelle für die SDR-Anwendung ermöglicht Benutzern das Durchsuchen der Stimmungsdaten, die über IBM Datenbanken dargestellt werden. Diese Benutzerschnittstelle dient auch zur Darstellung einer Übersicht, in der die Edge-Knoten enthalten sind, von denen die Daten stammen. Die Übersicht wird mit Daten aus dem von IBM bereitgestellten Service `gps` erstellt, der vom Edge-Knoten-Code des Service `sdr2evtstreams` benutzt wird. Der Service `gps` kann entweder als Schnittstelle zu GPS-Hardwarekomponenten oder zum Empfangen von Standortinformationen vom Einheiteneigner dienen. Sind keine GPS-Hardwarekomponenten und auch keine Standortinformationen vom Einheiteneigner verfügbar, kann der Service `gps` den Standort des Edge-Knotens anhand der IP-Adresse des Edge-Knotens abschätzen, um den geografischen Standort zu ermitteln. Mit diesem Service kann `sdr2evtstreams` Standortdaten für die Cloud bereitstellen, wenn der Service Audioclips sendet. Weitere Informationen finden Sie im Abschnitt [Web-UI-Code für softwaredefinierte Funkanwendung](https://github.com/open-horizon/examples/tree/master/cloud/sdr/ui/sdr-app).

Der Code für IBM Functions, IBM Datenbanken und die Webbenutzerschnittstelle kann optional in IBM Cloud bereitgestellt werden, falls Sie eine eigene Beispielwebbenutzerschnittstelle für SDR erstellen wollen. Sie können dies mit einem einzelnen Befehl ausführen, nachdem Sie [ein kostenpflichtiges Konto erstellt haben](https://cloud.ibm.com/login). Weitere Informationen finden Sie im Abschnitt [Inhalt des Implementierungsrepositorys](https://www.ibm.com/links?url=https%3A%2F%2Fgithub.com%2Fopen-horizon%2Fexamples%2Ftree%2Fmaster%2Fcloud%2Fsdr%2Fdeploy%2Fibm). 

**Hinweis:** Für diesen Bereitstellungsprozess sind gebührenpflichtige Services erforderlich, deren Gebühren über Ihr {{site.data.keyword.cloud_notm}}-Konto abgerechnet werden.

## Nächste Schritte

Wenn Sie eigene Software auf einem Edge-Knoten bereitstellen wollen, müssen Sie eigene Edge-Services und zugehörige Bereitstellungsmuster oder Bereitstellungsrichtlinien erstellen. Weitere Informationen finden Sie unter [Edge-Service für Einheiten entwickeln](../OH/docs/developing/developing.md).
