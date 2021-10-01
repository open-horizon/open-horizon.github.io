---

copyright:
years: 2019
lastupdated: "2019-06-24"
 
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Sicherheit und Datenschutz
{: #security_privacy}

Das auf {{site.data.keyword.horizon}} basierende Produkt {{site.data.keyword.edge_devices_notm}} bietet bestmöglichen Schutz gegen potenzielle Angriffe und sichert die Privatsphäre seiner Teilnehmer. {{site.data.keyword.edge_devices_notm}} verwendet geografisch verteilte autonome Agentenprozesse und Agbot-Prozesse (Agbot = Agreement Bot; Vereinbarungsbot) für das Edge-Software-Management und zur Aufrechterhaltung der Anonymität.
{:shortdesc}

Zur Aufrechterhaltung der Anonymität nutzen die Agentenprozesse und Agbot-Prozesse während des gesamten Erkennungs- und Verhandlungsprozesses für {{site.data.keyword.edge_devices_notm}} nur die öffentlichen Schlüssel gemeinsam. Alle Parteien in {{site.data.keyword.edge_devices_notm}} stufen die anderen beteiligten Parteien standardmäßig als nicht vertrauenswürdige Entität ein. Die Parteien nutzen Informationen nur dann gemeinsam und arbeiten auch nur dann zusammen, wenn eine Vertrauensbeziehung hergestellt werden kann, die Verhandlungen zwischen den Parteien abgeschlossen sind und eine formale Vereinbarung getroffen werden kann.

## Verteilte Steuerebene
{: #dc_pane}

Im Gegensatz zu normalen zentralen IoT-Plattformen (IoT = Internet of Things; Internet der Dinge) und cloudbasierten Steuersystemen arbeitet die Steuerebene von {{site.data.keyword.edge_devices_notm}} vorwiegend dezentral. Jede Rolle innerhalb des Systems verfügt über einen eingeschränkten Kompetenzrahmen, sodass jede Rolle nur über das Minimum an Berechtigungen verfügt, das zur Ausführung der zugeordneten Tasks erforderlich ist. Keine einzelne Berechtigungsstelle kann die Kontrolle über das gesamte System erlangen. Ein Benutzer oder eine Rolle kann sich nicht den Zugriff auf alle Knoten des Systems verschaffen, indem ein einzelner Host oder eine einzelne Softwarekomponente manipuliert wird.

Die Steuerebene wird mit drei verschiedenen Softwareentitäten implementiert:
* {{site.data.keyword.horizon}}-Agenten
* {{site.data.keyword.horizon}}-Agbots
* {{site.data.keyword.horizon_exchange}}

{{site.data.keyword.horizon}}-Agenten und -Agbots stellen die primären Entitäten dar und arbeiten autonom, um die Edge-Knoten zu verwalten. Mit dem Service {{site.data.keyword.horizon_exchange}} werden Aufgaben wie die Erkennung, die Verhandlung und die sichere Kommunikation zwischen Agenten und Agbots ausgeführt.

### Agenten
{: #agents}

{{site.data.keyword.horizon}}-Agenten sind in einer größeren Anzahl vorhanden als alle anderen Akteure in {{site.data.keyword.edge_devices_notm}}. Auf jedem der verwalteten Edge-Knoten wird ein Agent ausgeführt. Jeder Agent verfügt nur über die Berechtigung, diesen einen Edge-Knoten zu verwalten, auf dem er ausgeführt wird. Der Agent macht seinen öffentlichen Schlüssel in {{site.data.keyword.horizon_exchange}} zugänglich und verhandelt mit den fernen Agbot-Prozessen das Management der Software auf dem lokalen Knoten. Der Agent erwartet nur von den Agbots, die für die Bereitstellungsmuster in der Organisation des Agenten verantwortlich sind, den Empfang von Kommunikationsnachrichten.

Ein manipulierter Agent verfügt über keinerlei Berechtigung, die ihm die Manipulation anderer Edge-Knoten oder weiterer Systemkomponenten ermöglichen würde. Wenn das Hostbetriebssystem oder der Agentenprozess eines Edge-Knotens gehackt oder anderweitig manipuliert wird, dann beschränkt sich dieses Problem ausschließlich auf den jeweiligen Edge-Knoten. Alle anderen Komponenten des {{site.data.keyword.edge_devices_notm}}-Systems bleiben davon unberührt.

Der Edge-Knoten-Agent kann die wichtigste Komponente eines Edge-Knotens darstellen, hat jedoch die wenigsten Möglichkeiten zur Manipulation der Sicherheit des {{site.data.keyword.edge_devices_notm}}-Gesamtsystems. Der Agent ist verantwortlich für das Herunterladen der Software auf einen Edge-Knoten, die Überprüfung der Software und die Ausführung und Verknüpfung der Software mit anderen Software- und Hardwarekomponenten auf dem Edge-Knoten. Innerhalb des übergreifenden systemweiten Sicherheitskonzepts für {{site.data.keyword.edge_devices_notm}} verfügt der Agent nicht über die Berechtigung, die über den Edge-Knoten hinausgeht, auf dem der Agent ausgeführt wird.

### Agbots
{: #agbots}

{{site.data.keyword.horizon}}-Agbot-Prozesse können überall ausgeführt werden. Standardmäßig werden diese Prozesse automatisch ausgeführt. Agbot-Instanzen sind die Akteure, die in {{site.data.keyword.horizon}} am zweithäufigsten vorhanden sind. Jeder Agbot ist ausschließlich für die Bereitstellungsmuster verantwortlich, die ihm zugeordnet sind. Bereitstellungsmuster bestehen primär aus Richtlinien und aus einem Software-Service-Manifest. Eine einzelne Agbot-Instanz kann mehrere Bereitstellungsmuster für eine Organisation verwalten.

Bereitstellungsmuster werden von Entwicklern im Kontext einer {{site.data.keyword.edge_devices_notm}}-Benutzerorganisation veröffentlicht. Die Bereitstellungsmuster werden den {{site.data.keyword.horizon}}-Agenten von Agbots bereitgestellt. Wenn ein Edge-Knoten bei {{site.data.keyword.horizon_exchange}} registriert wird, dann wird dem Edge-Knoten ein Bereitstellungsmuster für die Organisation zugewiesen. Der Agent dieses Edge-Knotens akzeptiert Angebote nur von Agbots, die dieses spezielle Bereitstellungsmuster der betreffenden Organisation vorweisen können. Der Agbot stellt ein Vehikel für die Lieferung von Bereitstellungsmustern dar, das Bereitstellungsmuster selbst muss jedoch für die Richtlinien akzeptabel sein, die auf dem Edge-Knoten vom Eigner des Edge-Knotens festgelegt wurden. Das Bereitstellungsmuster muss die Validierung der Signatur erfolgreich durchlaufen, da es andernfalls vom Agenten nicht akzeptiert wird.

Ein manipulierter Agbot kann versuchen, schädliche Vereinbarungen mit Edge-Knoten vorzuschlagen und versuchen, ein schädliches Bereitstellungsmuster auf den Edge-Knoten bereitzustellen. Die Edge-Knoten-Agenten akzeptieren Vereinbarungen allerdings nur für die Bereitstellungsmuster, die die Agenten über die Registrierung angefordert haben und die in Hinblick auf die Richtlinien, die auf dem Edge-Knoten definiert wurden, akzeptabel sind. Der Agent verwendet seinen öffentlichen Schlüssel auch zur Validierung der kryptografischen Signatur des Musters, bevor das Muster von ihm akzeptiert wird.

Obwohl die Agbot-Prozesse die Softwareinstallation und die Implementierung von Wartungsaktualisierungen orchestrieren, verfügt der Agbot nicht über die Berechtigung, mit der ein Edge-Knoten oder ein Agent zum Akzeptieren der Software gezwungen werden könnte, die vom Agbot angeboten wird. Der Agent jedes einzelnen Edge-Knotens entscheidet darüber, welche Software akzeptiert oder zurückgewiesen werden soll. Der Agent trifft diese Entscheidung auf Basis der öffentlichen Schlüssel, die von ihm installiert wurden, und auf Basis der Richtlinien, die vom Eigner des Edge-Knotens definiert wurden, als der Eigner den Edge-Knoten bei {{site.data.keyword.horizon_exchange}} registriert hat.

## {{site.data.keyword.horizon_exchange}}
{: #exchange}

Bei {{site.data.keyword.horizon_exchange}} handelt es sich um einen zentralen, jedoch geografisch replizierten und mit einer Lastausgleichsfunktion versehenen Service, der den verteilten Agenten und Agbots die Kontaktaufnahme und die Verhandlung über eine Vereinbarung ermöglicht. Weitere Informationen hierzu finden Sie im Abschnitt [{{site.data.keyword.edge}} im Überblick](../../getting_started/overview_ieam.md).

{{site.data.keyword.horizon_exchange}} hat auch die Funktion einer gemeinsam genutzten Datenbank für Benutzermetadaten, Organisationen, Edge-Knoten und alle publizierten Services, Richtlinien und Bereitstellungsmuster.

Entwickler publizieren die JSON-Metadaten zu den Implementierungen der Software-Services, Richtlinien und Bereitstellungsmuster, die von ihnen erstellt wurden, in {{site.data.keyword.horizon_exchange}}. Diese Informationen werden hashverschlüsselt und vom Entwickler kryptografisch signiert. Edge-Knoten-Eigner müssen öffentliche Schlüssel für die Software während der Edge-Knoten-Registrierung installieren, sodass der lokale Agent die Schlüssel zur Validierung der Signaturen verwenden kann.

Eine manipulierte Instanz von {{site.data.keyword.horizon_exchange}} kann böswillig falsche Informationen für Agentenprozesse und Agbot-Prozesse anbieten, die Auswirkungen sind jedoch minimal, da entsprechende Verifizierungsmechanismen in das System integriert wurden. {{site.data.keyword.horizon_exchange}} verfügt nicht über die Berechtigungsnachweise, die zur böswilligen Signierung der Metadaten erforderlich sind. Eine manipulierte Instanz von {{site.data.keyword.horizon_exchange}} kann andere Benutzer oder Organisationen nicht mit einer Spoofing-Attacke angreifen. {{site.data.keyword.horizon_exchange}} arbeitet als Warehouse für die Artefakte, die von den Entwicklern und von den Edge-Knoten-Eignern publiziert werden, um bei der Aktivierung von Agbots während der Erkennungs- und Verhandlungsprozesse verwendet zu werden.

{{site.data.keyword.horizon_exchange}} vermittelt und sichert außerdem die gesamte Kommunikation zwischen den Agenten und den Agbots. Das Produkt implementiert einen Mailboxmechanismus, bei dem die Teilnehmer Nachrichten hinterlassen können, die für andere Teilnehmer bestimmt sind. Zum Empfang von Nachrichten müssen die Teilnehmer eine Abfrage an Horizon Switchboard absetzen, um festzustellen, ob ihre Mailbox Nachrichten enthält.

Agenten und Agbots nutzen darüber hinaus ihre öffentlichen Schlüssel gemeinsam mit {{site.data.keyword.horizon_exchange}}, um so eine sichere und private Kommunikation zu ermöglichen. Wenn Teilnehmer mit einem anderen Teilnehmer kommunizieren müssen, dann verwendet der Absender den öffentlichen Schlüssel des gewünschten Empfängers, um den Empfänger zu identifizieren. Der Sender verwendet diesen öffentlichen Schlüssel, um eine Nachricht an den Empfänger zu verschlüsseln. Der Empfänger kann dann die Antwort mit dem öffentlichen Schlüssel des Absenders verschlüsseln.

Dieser Ansatz stellt sicher, dass Horizon Exchange keine Nachrichten abhören kann, da dem Switchboard die dazu erforderlichen, gemeinsam genutzten Schlüssel zur Entschlüsselung der Nachrichten fehlen. Nur die vorgesehenen Empfänger können die Nachrichten entschlüsseln. Eine beschädigte Instanz von Horizon Exchange kann die Kommunikation von Teilnehmern nicht einsehen und ist nicht in der Lage, schädliche Kommunikationselemente in die Dialoge zwischen den Teilnehmern einzufügen.

## Denial-of-Service-Attacken
{: #denial}

{{site.data.keyword.horizon}} verwendet zentralisierte Services. Zentralisierte Services in typischen IoT-Systemen (IoT = Internet of Things; Internet der Dinge) sind im Allgemeinen anfällig gegenüber Denial-of-Service-Attacken. In {{site.data.keyword.edge_devices_notm}} werden diese zentralisierten Services ausschließlich für die Erkennung, Verhandlung und Aktualisierung verwendet. Die verteilten und autonomen Agentenprozesse und Agbot-Prozesse verwenden die zentralisierten Services nur dann, wenn die Prozesse Erkennungs-, Verhandlungs- und Aktualisierungstasks ausführen müssen. In allen anderen Bereichen kann das System, wenn Vereinbarungen getroffen werden, weiterhin normal arbeiten, und zwar auch dann, wenn diese zentralisierten Services offline sind. Dieses Verhalten stellt sicher, dass {{site.data.keyword.edge_devices_notm}} auch dann aktiv bleibt, wenn die zentralisierten Services angegriffen werden.

## Asymmetrische Verschlüsselung
{: #asym_crypt}

Der überwiegende Teil der Verschlüsselung in {{site.data.keyword.edge_devices_notm}} basiert auf der asymmetrischen Verschlüsselung. Bei dieser Form der Verschlüsselung müssen Sie und Ihre Entwickler ein Schlüsselpaar mit `hzn key`-Befehlen generieren und den privaten Schlüssel zum kryptografischen Signieren aller Softwarekomponenten oder Services verwenden, die publiziert werden sollen. Sie müssen Ihren öffentlichen Schlüssel auf den Edge-Knoten installieren, auf denen die Software oder der Service ausgeführt werden muss, sodass die kryptografische Signatur der Software bzw. des Service überprüft werden kann.

Agenten und Agbots führen eine kryptografische Signierung ihrer Nachrichten an den Kommunikationspartner durch, indem sie den privaten Schlüssel verwenden. Der öffentliche Schlüssel des Kommunikationspartners wird verwendet, um die empfangenen Nachrichten zu überprüfen. Die Agenten und Agbots verschlüsseln ihre Nachrichten außerdem mit dem öffentlichen Schlüssel der anderen Partei, um sicherzustellen, dass nur der vorgesehene Empfänger die Nachricht entschlüsseln kann.

Wenn der private Schlüssel und die Berechtigungsnachweise für einen Agenten, Agbot oder Benutzer manipuliert wurden, dann werden nur die Artefakte zugänglich gemacht, die sich unter der Kontrolle der jeweiligen Entität befinden. 

## Zusammenfassung
{: #summary}

Durch Verwendung von Hashwerten, kryptografischen Signaturen und der Verschlüsselung sichert {{site.data.keyword.edge_devices_notm}} den überwiegenden Teil der Plattform gegen unbefugte Zugriffe. Durch die überwiegend dezentrale Konzeption von {{site.data.keyword.edge_devices_notm}} werden Sicherheitslücken für die meisten Attacken vermieden, die normalerweise auf älteren IoT-Plattformen möglich sind. Durch die Beschränkung des Kompetenzrahmens und den Einfluss der Teilnehmerrollen isoliert {{site.data.keyword.edge_devices_notm}} den potenziellen Schaden durch einen manipulierten Host oder eine manipulierte Softwarekomponente in der betroffenen Systemkomponente. Sogar externe Attacken im großen Stil, die gegen die zentralen Services der {{site.data.keyword.horizon}}-Services ausgeführt werden, die in {{site.data.keyword.edge_devices_notm}} eingesetzt werden, haben so nur minimale Auswirkungen auf die Teilnehmer, die bereits über eine Vereinbarung verfügen. Die Teilnehmer, die über eine aktive Vereinbarung verfügen, können während eines Ausfalls normal weiterarbeiten.
