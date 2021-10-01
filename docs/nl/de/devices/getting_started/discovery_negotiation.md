---

copyright:
years: 2019
lastupdated: "2019-06-28"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Erkennung und Verhandlung
{: #discovery_negotiation}

{{site.data.keyword.edge_devices_notm}} basiert auf dem {{site.data.keyword.horizon_open}}-Projekt und arbeitet hauptsächlich dezentral und verteilt. Autonome Agentenprozesse und Agbot-Prozesse (Agbot = Agreement Bot; Vereinbarungsbot) arbeiten zusammen, um das Software-Management für alle registrierten Edge-Knoten durchzuführen.
{:shortdesc}

Weitere Informationen zum {{site.data.keyword.horizon_open}}-Projekt finden Sie unter [{{site.data.keyword.horizon_open}}](https://github.com/open-horizon/).

Auf jedem Horizon-Edge-Knoten wird ein autonomer Agentenprozess ausgeführt, um die Richtlinien durchzusetzen, die vom Eigner der Edge-Maschine definiert wurden.

Gleichzeit verwenden autonome Agbot-Prozesse, die den einzelnen Bereitstellungsmustern für die Software zugeordnet sind, die für das zugewiesene Muster definierten Richtlinien zum Ermitteln der Edge-Knoten-Agenten, die für das betreffende Muster registriert sind. Diese autonomen Agbots und Agenten verhandeln auf Basis der vom Eigner der Edge-Maschine definierten Richtlinien formale Vereinbarungen für die Zusammenarbeit. Sobald Agbots und Agenten eine solche Vereinbarung getroffen haben, arbeiten sie beim Management der Softwarelebenszyklen für die zugehörigen Edge-Knoten zusammen.

Agbots und Agenten verwenden die folgenden zentralen Services, um sich gegenseitig zu erkennen, eine Vertrauensbeziehung herzustellen und auf sicherem Wege über {{site.data.keyword.edge_devices_notm}} zu kommunizieren:

* {{site.data.keyword.horizon_switch}} für die sichere und private Peer-to-Peer-Kommunikation zwischen Agbots und Agenten.
* {{site.data.keyword.horizon_exchange}} für die Durchführung der Erkennung.

<img src="../../images/edge/distributed.svg" width="90%" alt="Zentrale und dezentrale Services">

## {{site.data.keyword.horizon_exchange}}

{{site.data.keyword.horizon_exchange}} ermöglicht den Eignern von Edge-Maschinen die Registrierung der Edge-Knoten für das Software-Lifecycle-Management. Wenn Sie einen Edge-Knoten mit {{site.data.keyword.horizon_exchange}} für {{site.data.keyword.edge_devices_notm}} registrieren, geben Sie das Bereitstellungsmuster für den Edge-Knoten an. Ein Bereitstellungsmuster umfasst eine Gruppe von Richtlinien zum Management von Edge-Knoten, ein kryptografisch signiertes Softwaremanifest und alle zugehörigen Konfigurationseinstellungen. Das Bereitstellungsmuster muss unter {{site.data.keyword.horizon_exchange}} entworfen, entwickelt, getestet, signiert und publiziert werden.

Jeder Edge-Knoten muss bei {{site.data.keyword.horizon_exchange}} unter der Organisation des Eigners der Edge-Maschine registriert werden. Jeder Edge-Knoten wird mit einer ID und einem Sicherheitstoken registriert, die bzw. das nur für den betreffenden Knoten gilt. Knoten können zur Ausführung eines Softwarebereitstellungsmusters registriert werden, das von der zugehörigen Organisation bereitgestellt wird. Alternativ hierzu kann ein Muster verwendet werden, das von einer anderen Organisation bereitgestellt wird, wenn das Bereitstellungsmuster öffentlich verfügbar gemacht wird.

Wenn ein Bereitstellungsmuster in {{site.data.keyword.horizon_exchange}} publiziert wird, dann wird mindestens ein Agbot zugewiesen, um das Bereitstellungsmuster und alle zugehörigen Richtlinien zu verwalten. Diese Agbots dienen zur Ermittlung aller Edge-Knoten, die für das Bereitstellungsmuster registriert wurden. Wenn ein registrierter Edge-Knoten gefunden wird, dann verhandeln die Agbots mit den lokalen Agentenprozessen über die für den Edge-Knoten zu verwendende Vorgehensweise.

Obwohl {{site.data.keyword.horizon_exchange}} dazu dient, den Agbots die Erkennung der Edge-Knoten zu ermöglichen, die einem registrierten Bereitstellungsmuster zugeordnet sind, ist {{site.data.keyword.horizon_exchange}} nicht direkt in den Software-Management-Prozess für den Edge-Knoten eingebunden. Agbots und Agenten führen den Software-Management-Prozess selbst aus. {{site.data.keyword.horizon_exchange}} verfügt auf dem Edge-Knoten nicht über Berechtigungen und kann auch den Kontakt zu den Edge-Knoten-Agenten nicht einleiten.

## {{site.data.keyword.horizon_switch}}

Agbots führen in regelmäßigen Zeitabständen Abfragen bei {{site.data.keyword.horizon_exchange}} durch, um alle Edge-Knoten zu ermitteln, die für ihr Bereitstellungsmuster registriert wurden. Wenn ein Agbot einen Edge-Knoten erkennt, der für sein Bereitstellungsmuster registriert wurde, dann verwendet der Agbot den Service {{site.data.keyword.horizon}} Switchboard, um eine private Nachricht an den Agenten dieses Knotens zu senden. Diese Nachricht enthält eine Anforderung an den Agenten, beim Software-Lifecycle-Management des Edge-Knotens mit dem Agbot zusammenzuarbeiten. Der Agent fragt in der Zwischenzeit seine private Mailbox in {{site.data.keyword.horizon_switch}} ab, um festzustellen, ob Agbot-Nachrichten eingegangen sind. Wurde eine Nachricht empfangen, dann wird sie vom Agenten entschlüsselt, überprüft und zum Akzeptieren der Anforderung beantwortet.

Zusätzlich zur Abfrage von {{site.data.keyword.horizon_exchange}} fragt jeder Agbot auch die eigene private Mailbox in {{site.data.keyword.horizon_switch}} ab. Wenn der Agbot eine akzeptierte Anforderung des Agenten empfängt, ist die Verhandlung abgeschlossen.

Agenten und Agbots nutzen öffentliche Schlüssel gemeinsam mit {{site.data.keyword.horizon_switch}}, um so eine sichere und private Kommunikation zu ermöglichen. Durch diese Verschlüsselung dient {{site.data.keyword.horizon_switch}} lediglich als Mailbox-Manager. Alle Nachrichten werden durch den Absender verschlüsselt, bevor sie an {{site.data.keyword.horizon_switch}} gesendet werden. {{site.data.keyword.horizon_switch}} ist nicht in der Lage, die Nachrichten zu entschlüsseln. Der Empfänger kann jedoch jede Nachricht entschlüsseln, die mit seinem öffentlichen Schlüssel verschlüsselt wurde. Der Empfänger verwendet den öffentlichen Schlüssel des Absenders auch, um seine Antworten an den Absender zu verschlüsseln.

**Hinweis:** Da die gesamte Kommunikation über {{site.data.keyword.horizon_switch}} vermittelt wird, werden die IP-Adressen der Edge-Knoten keinem Agbot angezeigt, solange der Agent der einzelnen Edge-Knoten diese Informationen nicht sichtbar macht. Der Agent macht diese Informationen erst dann sichtbar, wenn Agent und Agbot erfolgreich eine Vereinbarung verhandelt haben.

## Software-Lifecycle-Management

Wenn ein Edge-Knoten bei {{site.data.keyword.horizon_exchange}} für ein bestimmtes Bereitstellungsmuster registriert wird, kann ein Agbot für dieses Bereitstellungsmuster den Agenten auf dem Edge-Knoten finden. Der Agbot für das Bereitstellungsmuster verwendet {{site.data.keyword.horizon_exchange}}, um den Agenten zu suchen. {{site.data.keyword.horizon_switch}} wird vom Agbot verwendet, um mit dem Agenten über die Zusammenarbeit beim Software-Management zu verhandeln.

Der Edge-Knoten-Agent empfängt die Anforderung für die Zusammenarbeit vom Agbot und wertet den Vorschlag aus, um sicherzustellen, dass er mit den Richtlinien übereinstimmt, die vom Edge-Knoten-Eigner definiert wurden. Der Agent überprüft die kryptografischen Signaturen unter Verwendung der lokal installierten Schlüsseldateien. Wenn der Vorschlag den lokalen Richtlinien entspricht und somit akzeptabel ist und wenn die Signaturen verifiziert werden konnten, akzeptiert der Agent den Vorschlag und Agent und Agbot gehen eine Vereinbarung ein. 

Nachdem die Vereinbarung zustande gekommen ist, arbeiten Agbot und Agent zusammen, um den Softwarelebenszyklus des Bereitstellungsmusters auf dem Edge-Knoten zu verwalten. Der Agbot stellt während der Entwicklung des Bereitstellungsmusters Details zur Verfügung und überwacht den Edge-Knoten auf deren Einhaltung. Der Agent führt den lokalen Software-Download auf den Edge-Knoten durch, überprüft die Signatur der Software und führt die Software (bei erfolgreicher Überprüfung) aus und überwacht sie. Bei Bedarf aktualisiert der Agent die Software und stoppt die Ausführung der Software, wenn dies erforderlich ist.

Weitere Informationen zum Software-Management-Prozess finden Sie im Abschnitt zum [Edge-Software-Management](edge_software_management.md).
