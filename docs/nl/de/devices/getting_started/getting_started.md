---

copyright:
years: 2019
lastupdated: "2019-08-01"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Erste Schritte
{: #getting_started}

Informieren Sie sich in den folgenden Abschnitten über die ersten Schritte mit {{site.data.keyword.edge_devices_notm}} einschließlich der Vorgehensweise zum Management der Edge-Software und -Services.
{:shortdesc}

Weitere Informationen zur Installation der erforderlichen Software für {{site.data.keyword.edge_devices_notm}}-Einheiten finden Sie in den folgenden Abschnitten:

* [Edge-Einheit vorbereiten](../installing/adding_devices.md)
* [{{site.data.keyword.horizon_agent}} auf der Edge-Einheit installieren und beim 'Hello World'-Beispiel registrieren](../installing/registration.md)
* [Weitere Beispiele für Edge-Services](../installing/additional_examples.md)
  * [Beispiel für den Prozentsatz der CPU-Belastung des Hosts (cpu2evtstreams)](../installing/cpu_load_example.md)
  * [Hello World](policy.md)
  * [Edge-Verarbeitung für Software-Defined Radio (SDR)](../installing/software_defined_radio_ex.md)
  * [Offline-Sprachsteuerung (processtext)](../installing/offline_voice_assistant.md)
  * [Watson Speech-To-Text](../installing/watson_speech.md)
* [Informationen zum Befehl 'hzn'](../installing/exploring_hzn.md)

## Funktionsweise von {{site.data.keyword.edge_devices_notm}} im Überblick
{: #overview}

{{site.data.keyword.edge_devices_notm}} wurde speziell für das Edge-Knoten-Management konzipiert, um die Bereitstellungsrisiken zu minimieren und den Softwarelebenszyklus von Services auf Edge-Knoten vollkommen autonom zu verwalten.
{:shortdesc}

## {{site.data.keyword.edge_devices_notm}}-Architektur

{: #iec4d_arch}

Andere Edge-Computing-Lösungen bauen im Allgemeinen auf einer der folgenden Architekturstrategien auf: 

* Leistungsfähige zentrale Stelle für die Umsetzung der geltenden Richtlinien durch die Edge-Knoten-Software.
* Weitergabe der Zuständigkeit für die Einhaltung der geltenden Richtlinien durch die Software an die Edge-Knoten-Eigner. Diese müssen die Softwareaktualisierungen überwachen und mit manuellen Maßnahmen dafür sorgen, dass ihre Edge-Knoten die geltenden Richtlinien erfüllen.

Im ersten Fall wird die Berechtigung zentral gebündelt, wodurch ein Single Point of Failure entsteht, der einen Angriffspunkt bietet, über den die Kontrolle über den gesamten Edge-Knoten-Bestand erreicht werden kann. Bei der zweiten Lösung kann es zu einem hohen Prozentsatz an Edge-Knoten kommen, auf denen nicht die neuesten Softwareaktualisierungen installiert sind. Wenn nicht alle Edge-Knoten mit der neuesten Version arbeiten oder nicht über alle verfügbaren Fixes verfügen, dann kann sich dadurch eine Sicherheitslücke ergeben, die von Angreifern genutzt werden kann. Beide Ansätze basieren normalerweise auf einer zentralen Berechtigungsstelle, die den Ausgangspunkt für die Einrichtung von Vertrauensbeziehungen bildet.

<p align="center">
<img src="../../images/edge/overview_illustration.svg" width="70%" alt="Darstellung der globalen Reichweite des Edge-Computings">
</p>

Im Gegensatz zu diesen Lösungsansätzen arbeitet {{site.data.keyword.edge_devices_notm}} dezentral. {{site.data.keyword.edge_devices_notm}} verwaltet die Einhaltung der geltenden Richtlinien durch die Service-Software automatisch auf den Edge-Knoten, ohne dass hierzu ein manueller Eingriff des Benutzers erforderlich ist. Auf jedem Edge-Knoten werden dezentrale und vollständig autonom arbeitende Agentenprozesse ausgeführt, die anhand der während der Maschinenregistrierung bei {{site.data.keyword.edge_devices_notm}} festgelegten Richtlinien gesteuert werden. Dezentrale und ebenfalls vollständig autonome Agbots (Agreement Bots; Vereinbarungsbots) werden normalerweise an einem zentralen Standort ausgeführt, können jedoch an jedem beliebigen Standort und auch auf den Edge-Knoten ausgeführt werden. Wie die Agentenprozesse werden auch die Agbots mithilfe von Richtlinien gesteuert. Die Agenten und Agbots übernehmen den größten Teil des Software-Lifecycle-Managements des Edge-Service für die Edge-Knoten und die Einhaltung der Richtlinien durch die Software auf den Edge-Knoten. 

Aus Gründen der Effizienz umfasst {{site.data.keyword.edge_devices_notm}} zwei zentrale Services (Exchange und Switchboard). Diese Services verfügen nicht über zentrale Berechtigungen über die autonomen Agentenprozesse und Agbot-Prozesse. Stattdessen stellen diese Services einfache Erkennungsservices und Services zur gemeinsamen Nutzung von Metadaten (Exchange) sowie einen privaten Mailbox-Service zur Unterstützung der Peer-to-Peer-Kommunikation (Switchboard) bereit. Diese Services unterstützen die vollständig autonome Ausführung der Agenten und Agbots.

Als weitere Komponente unterstützt die {{site.data.keyword.edge_devices_notm}}-Konsole Administratoren dabei, Richtlinien festzulegen und den Status der Edge-Knoten zu überwachen. 

Jeder der fünf {{site.data.keyword.edge_devices_notm}}-Komponententypen (Agenten, Agbots, Exchange, Switchboard und Konsole) hat einen eingeschränkten Verantwortungsbereich. Keine der Komponenten verfügt über die erforderlichen Berechtigungen oder Berechtigungsnachweise, die ihr die Ausführung von Aktionen außerhalb ihres jeweiligen Zuständigkeitsbereichs ermöglichen würden. Durch die Aufteilung der Zuständigkeiten und das Scoping der Berechtigungen und Berechtigungsnachweise bietet {{site.data.keyword.edge_devices_notm}} ein Risikomanagement für die Edge-Knoten-Bereitstellung.

## Erkennung und Verhandlung
{: #discovery_negotiation}

{{site.data.keyword.edge_devices_notm}} basiert auf dem Projekt [1 von {{site.data.keyword.horizon_open}} ![Wird auf einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird auf einer neuen Registerkarte geöffnet")](https://github.com/open-horizon/) und ist überwiegend dezentral organisiert und verteilt. Autonome Agentenprozesse und Agbot-Prozesse (Agbot = Agreement Bot; Vereinbarungsbot) arbeiten zusammen, um das Software-Management für alle registrierten Edge-Knoten durchzuführen.


Auf jedem Horizon-Edge-Knoten wird ein autonomer Agentenprozess ausgeführt, um die Richtlinien durchzusetzen, die vom Eigner der Edge-Einheit definiert wurden. 

Autonome Agbots überwachen die Bereitstellungsmuster und Richtlinien im Exchange und ermitteln die Edge-Knoten-Agenten, die noch nicht konform sind. Agbots schlagen den Edge-Knoten Vereinbarungen vor, damit sie die Konformitätsstandards erfüllen. Wenn ein Agbot und ein Agent eine Vereinbarung treffen, arbeiten sie zusammen, um den Softwarelebenszyklus von Edge-Services auf dem Edge-Knoten zu verwalten. 

Agbots und Agenten verwenden die folgenden zentralen Services, um sich gegenseitig zu erkennen, eine Vertrauensbeziehung herzustellen und auf sicherem Wege über {{site.data.keyword.edge_devices_notm}} zu kommunizieren:

* {{site.data.keyword.horizon_exchange}} für die Durchführung der Erkennung.
* {{site.data.keyword.horizon_switch}} für die sichere und private Peer-to-Peer-Kommunikation zwischen Agbots und Agenten.

<img src="../../images/edge/distributed.svg" width="90%" alt="Zentrale und dezentrale Services">

### {{site.data.keyword.horizon_exchange}}
{: #iec4d_exchange}

{{site.data.keyword.horizon_exchange}} ermöglicht den Eignern von Edge-Einheiten die Registrierung der Edge-Knoten für das Software-Lifecycle-Management. Wenn Sie einen Edge-Knoten mit {{site.data.keyword.horizon_exchange}} für {{site.data.keyword.edge_devices_notm}} registrieren, geben Sie das Bereitstellungsmuster oder die Richtlinie für den Edge-Knoten an. (Im Prinzip ist ein Bereitstellungsmuster einfach eine vordefinierte und benannte Gruppe von Richtlinien für die Verwaltung von Edge-Knoten.) Die Muster und Richtlinien müssen im {{site.data.keyword.horizon_exchange}} entworfen, entwickelt, getestet, signiert und publiziert werden. 

Jeder Edge-Knoten wird mit einer eindeutigen ID und einem Sicherheitstoken registriert. Knoten können für die Verwendung von Mustern oder Richtlinien registriert werden, die von ihrer eigenen Organisation bereitgestellt werden. Alternativ hierzu kann ein Muster verwendet werden, das von einer anderen Organisation bereitgestellt wird. 

Wenn ein Muster oder eine Richtlinie auf dem {{site.data.keyword.horizon_exchange}} publiziert wird, versuchen die Agbots, alle Edge-Knoten zu erkennen, die von dem neuen oder aktualisierten Muster oder der neuen oder aktualisierten Richtlinie betroffen sind. Wird ein registrierter Edge-Knoten gefunden, verhandelt ein Agbot mit dem Edge-Knoten-Agenten. 

Obwohl {{site.data.keyword.horizon_exchange}} dazu dient, den Agbots die Erkennung der Edge-Knoten zu ermöglichen, die für die Verwendung von Mustern oder Richtlinien registriert sind, ist {{site.data.keyword.horizon_exchange}} nicht direkt in den Software-Management-Prozess für den Edge-Knoten eingebunden. Agbots und Agenten führen den Software-Management-Prozess selbst aus. {{site.data.keyword.horizon_exchange}} verfügt auf dem Edge-Knoten nicht über Berechtigungen und kann auch den Kontakt zu den Edge-Knoten-Agenten nicht einleiten. 

### {{site.data.keyword.horizon_switch}}
{: #horizon_switch}

Wenn ein Agbot einen Edge-Knoten erkennt, der von einem neuen oder aktualisieren Muster oder einer neuen oder aktualisierten Richtlinie betroffen ist, verwendet der Agbot den Service {{site.data.keyword.horizon}} Switchboard, um eine private Nachricht an den Agenten dieses Knotens zu senden. Diese Nachricht besteht aus einem Vorschlag für die Vereinbarung, beim Software-Lifecycle-Management des Edge-Knotens mit dem Agbot zusammenzuarbeiten. Wenn der Agent die Nachricht des Agbots in seiner privaten Mailbox in {{site.data.keyword.horizon_switch}} empfängt, entschlüsselt er den Vorschlag wertet ihn aus. Wenn sich der Vorschlag im Rahmen seiner eigenen Knotenrichtlinie befindet, sendet der Knoten eine Zustimmungsnachricht an den Agbot. Andernfalls weist der Knoten den Vorschlag zurück. Wenn der Agbot die Zustimmung zu der Vereinbarung in seiner privaten Mailbox in {{site.data.keyword.horizon_switch}} empfängt, ist die Aushandlung abgeschlossen. 

Agenten und Agbots veröffentlichen öffentliche Schlüssel in {{site.data.keyword.horizon_switch}}, um so eine sichere und private Kommunikation mit absoluter vorwärts gerichteter Sicherheit zu ermöglichen. Durch diese Verschlüsselung dient {{site.data.keyword.horizon_switch}} lediglich als Mailbox-Manager. Es kann die Nachrichten nicht entschlüsseln.

Hinweis: Da die gesamte Kommunikation über {{site.data.keyword.horizon_switch}} vermittelt wird, werden die IP-Adressen der Edge-Knoten keinem Agbot angezeigt, solange der Agent der einzelnen Edge-Knoten diese Informationen nicht sichtbar macht. Der Agent macht diese Informationen erst dann sichtbar, wenn Agent und Agbot erfolgreich eine Vereinbarung verhandelt haben.

## Edge-Software-Lifecycle-Management
{: #edge_lifecycle}

Nachdem ein Agbot und ein Agent eine Vereinbarung für ein bestimmtes Muster oder eine bestimmte Gruppe von Richtlinien getroffen haben, arbeiten sie zusammen, um den Softwarelebenszyklus des Musters oder der Gruppe von Richtlinien auf dem Edge-Knoten zu verwalten. Der Agbot überwacht die Entwicklung des Musters oder der Richtlinie im Zeitverlauf und überwacht den Edge-Knoten auf seine Konformität. Der Agent führt den lokalen Software-Download auf den Edge-Knoten durch, überprüft die Signatur der Software und führt die Software (bei erfolgreicher Verifizierung) aus und überwacht sie. Bei Bedarf aktualisiert der Agent die Software und stoppt die Ausführung der Software, wenn dies erforderlich ist.

Der Agent lädt die angegebenen Docker-Container-Images für den Edge-Service aus den entsprechenden Registrys herunter und überprüft die Imagesignaturen des Containers. Nach Abschluss dieses Vorgangs startet der Agent die Container in umgekehrter Reihenfolge der Abhängigkeiten mit der im Muster oder der Richtlinie angegebenen Konfiguration. Wenn die Container aktiv sind, überwacht der lokale Agent die Container. Wird die Ausführung eines Containers unvorhergesehen gestoppt, startet der Agent den Container erneut, damit das Muster oder die Richtlinie auf dem Edge-Knoten konform bleibt. 

Der Agent besitzt eine eingeschränkte Fehlertoleranz. Wenn ein Container wiederholt und in schneller Abfolge abstürzt, stoppt der Agent die Versuche, den ständig ausfallenden Service neu zu starten, und storniert die Vereinbarung. 

### {{site.data.keyword.horizon}}-Serviceabhängigkeiten
{: #service_dependencies}

Ein Edge-Service kann in seinen Metadaten Abhängigkeiten von anderen Edge-Services angeben. Wenn ein Edge-Service infolge eines Musters oder einer Richtlinie auf einem Edge-Knoten bereitgestellt wird, stellt der Agent auch alle Edge-Services (in umgekehrter Reihenfolge der Abhängigkeiten) bereit, die für den ersten Edge-Service benötigt werden. Es wird eine beliebige Anzahl von Ebenen der Serviceabhängigkeiten unterstützt. 

### {{site.data.keyword.horizon}}-Docker-Vernetzung
{: #docker_networking}

{{site.data.keyword.horizon}} verwendet die Docker-Vernetzungsfunktionen zur Isolierung von Docker-Containern, sodass nur Services, die die Container benötigen, auf diese Container zugreifen können. Wenn ein Service-Container gestartet wird, der von einem anderen Service abhängig ist, wird der Service-Container mit dem privaten Netz des abhängigen Service-Containers verbunden. Dies ermöglicht die Ausführung von Edge-Services, die von verschiedenen Organisationen entwickelt wurden, da jeder Edge-Service auf andere Services zugreifen kann, die nur in seinen Metadaten aufgelistet sind. 
