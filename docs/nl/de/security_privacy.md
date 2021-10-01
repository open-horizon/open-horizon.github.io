---

copyright:
years: 2021
lastupdated: "2021-02-20"
 
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

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}), basierend auf [Open Horizon](https://github.com/open-horizon), verwendet mehrere Sicherheitstechnologien, um sicherzustellen, dass es sicher vor Angriffen ist und die Privatsphäre geschützt wird. {{site.data.keyword.ieam}} verwendet geografisch verteilte autonome Agentenprozesse für das Edge-Software-Management. Infolgedessen stellen sowohl der {{site.data.keyword.ieam}}-Management-Hub als auch die Agenten potenzielle Ziele für Sicherheitsverstöße dar. In diesem Dokument erfahren Sie, wie {{site.data.keyword.ieam}} Sicherheitsrisiken abschwächt oder beseitigt.
{:shortdesc}

## Management-Hub
Der {{site.data.keyword.ieam}}-Management-Hub wird in einer Instanz von OpenShift Container Platform bereitgestellt und übernimmt daher alle Vorteile des inhärenten Sicherheitsmechanismus. Der gesamte Netzverkehr des {{site.data.keyword.ieam}}-Management-Hubs fließt durch einen mit TLS geschützten Eingangspunkt. Die Netzkommunikation des Management-Hubs zwischen den Komponenten des {{site.data.keyword.ieam}}-Management-Hubs erfolgt ohne TLS.

## Sichere Steuerebene
{: #dc_pane}

Der {{site.data.keyword.ieam}}-Management-Hub und die verteilten Agenten kommunizieren zur Bereitstellung von Workloads und Modellen für die Edge-Knoten über die Steuerebene. Im Gegensatz zu den typischen zentralisierten Plattformen für das Internet der Dinge (Internet of Things, IoT) und zu cloudbasierten Steuersystemen ist die Steuerebene von {{site.data.keyword.ieam}} größtenteils dezentral organisiert. Jeder Akteur innerhalb des Systems verfügt über einen eingeschränkten Kompetenzrahmen, sodass jeder Akteur nur über das Minimum an Berechtigungen verfügt, das er zur Ausführung seiner Tasks benötigt. Kein einzelner Akteur kann die Kontrolle über das gesamte System erlangen. Darüber hinaus kann sich ein einzelner Akteur  nicht den Zugriff auf alle Edge-Knoten des Systems verschaffen, indem ein einzelner Edge-Knoten, ein einzelner Host oder eine einzelne Softwarekomponente manipuliert wird.

Die Steuerebene wird mit drei verschiedenen Softwareentitäten implementiert:
* Open {{site.data.keyword.horizon}}-Agenten
* Open {{site.data.keyword.horizon}}-Agbots
* Open {{site.data.keyword.horizon_exchange}}

Open {{site.data.keyword.horizon}}-Agenten und -Agbots sind die Hauptakteure innerhalb der Steuerebene. Mit dem Service {{site.data.keyword.horizon_exchange}} werden Aufgaben wie die Erkennung und die sichere Kommunikation zwischen Agenten und Agbots ausgeführt. Zusammen stellen diese Elemente den Schutz auf Nachrichtenebene mithilfe eines Algorithmus bereit, der als 'absolute vorwärts gerichtete Sicherheit' (Perfect Forward Secrecy) bezeichnet wird.

Agenten und Agbots kommunizieren mit Exchange standardmäßig über TLS 1.3. TLS selbst bietet jedoch nicht genügend Sicherheit. {{site.data.keyword.ieam}} verschlüsselt alle Steuernachrichten, die zwischen Agenten und Agbots fließen, bevor sie über das Netz gesendet werden. Jeder Agent und Agbot generiert ein 2048-Bit-RSA-Schlüsselpaar und veröffentlicht seinen öffentlichen Schlüssel in Exchange. Der private Schlüssel wird jeweils im Speicher des Akteurs abgelegt, auf den nur der Rootbenutzer Zugriff hat. Andere Akteure im System entschlüsseln mit dem öffentlichen Schlüssel des Nachrichtenempfängers einen symmetrischen Schlüssel, der zum Verschlüsseln der Steuerebenennachrichten verwendet wird. Dies stellt sicher, dass nur der vorgesehene Empfänger den symmetrischen Schlüssel und somit die eigentliche Nachricht entschlüsseln kann. Die Verwendung der absoluten vorwärts gerichteten Sicherheit in der Steuerebene bietet eine zusätzliche Sicherheit, beispielsweise durch eine Verhinderung von Man-in-the-Middle-Attacken, die von TLS nicht abgewehrt werden.

### Agenten
{: #agents}

{{site.data.keyword.horizon_open}}-Agenten sind in einer größeren Anzahl vorhanden als alle anderen Akteure in {{site.data.keyword.ieam}}. Auf jedem der verwalteten Edge-Knoten wird ein Agent ausgeführt. Jeder Agent ist ausschließlich zur Verwaltung dieses Edge-Knotens berechtigt. Ein manipulierter Agent verfügt über keinerlei Berechtigung, die ihm die Manipulation anderer Edge-Knoten oder weiterer Systemkomponenten ermöglichen würde. Jeder Knoten besitzt eindeutige Berechtigungsnachweise, die in seinem eigenen Speicher abgelegt sind, auf den nur der Rootbenutzer Zugriff hat. {{site.data.keyword.horizon_exchange}} stellt sicher, dass ein Knoten ausschließlich auf seine eigenen Ressourcen zugreifen kann. Beim Registrieren eines Knotens mit dem Befehl `hzn register` kann ein Authentifizierungstoken angegeben werden. Es hat sich jedoch das Verfahren bewährt, dem Agenten das Generieren eines eigenen Tokens zu erlauben, damit kein Benutzer die Knotenberechtigungsnachweise kennt, was das Risiko für eine Manipulation des Edge-Knotens verringert.

Da der Agent im Hostnetz keine Empfangsports besitzt, ist er vor Netzattacken geschützt. Die gesamte Kommunikation zwischen dem Agenten und dem Management-Hub erfolgt dadurch, dass der Agent den Management-Hub abfragt. Außerdem wird Benutzern dringend dazu geraten, Edge-Knoten durch eine Netzfirewall zu schützen, die unbefugte Zugriffe auf den Host des Knotens verhindert. Für den Fall, dass das Betriebssystem des Agentenhosts oder der Agentenprozess selbst trotz dieser Zugriffsschutzmechanismen gehackt oder anderweitig manipuliert wird, betrifft die Manipulation ausschließlich diesen einen Edge-Knoten. Alle anderen Komponenten des {{site.data.keyword.ieam}}-Systems bleiben davon unberührt.

Für den Download und Start von containerisierten Workloads ist der Agent verantwortlich. Um zu gewährleisten, dass der heruntergeladene Container-Image und seine Konfiguration nicht manipuliert wurden, überprüft der Agent die digitale Signatur des Container-Image und die digitale Signatur der Bereitstellungskonfiguration. Sobald ein Container in einer Container-Registry gespeichert wird, stellt die Registry eine digitale Signatur für das Image (z. B. einen SHA256-Hashwert) zur Verfügung. Die Container-Registry verwaltet die Schlüssel, die zum Erstellen der Signatur verwendet werden. Wenn ein {{site.data.keyword.ieam}}-Service mit dem Befehl `hzn exchange service publish` publiziert wird, ruft er die Imagesignatur ab und speichert sie zusammen mit dem publizierten Service in {{site.data.keyword.horizon_exchange}}. Die digitale Signatur des Image wird über die sichere Steuerebene an den Agenten übergeben; mit ihrer Hilfe kann der Agent die Container-Imagesignatur anhand des heruntergeladenen Image prüfen. Falls die Imagesignatur nicht mit dem Image übereinstimmt, wird der Container vom Agenten nicht gestartet. Für die Containerkonfiguration ist der Prozess von einer Ausnahme abgesehen ähnlich. Der Befehl `hzn exchange service publish` signiert die Containerkonfiguration und speichert die Signatur in {{site.data.keyword.horizon_exchange}}. In diesem Fall muss der Benutzer (der den Service publiziert) das RSA-Schlüsselpaar bereitstellen, das zum Erstellen der Signatur verwendet wurde. Mit dem Befehl `hzn key create` können für diesen Zweck Schlüssel generiert werden, falls der Benutzer noch nicht über Schlüssel verfügt. Der öffentliche Schlüssel wird in Exchange mit der Signatur der Containerkonfiguration gespeichert und über die sichere Steuerebene an den Agenten übergeben. Der Agent kann dann mithilfe des öffentlichen Schlüssels die Containerkonfiguration prüfen. Wenn Sie für jede Containerkonfiguration ein unterschiedliches Schlüsselpaar verwenden möchten, kann der private Schlüssel, der zum Signieren dieser Containerkonfiguration verwendet wird, jetzt verworfen werden, da er nicht mehr benötigt wird. Näheres über das Publizieren einer Workload enthält der Abschnitt [Edge-Services entwickeln](../developing/developing_edge_services.md).

Wenn ein Modell in einem Edge-Knoten implementiert wird, lädt der Agent das Modell herunter und verstuft die Signatur des Modells, um sicherzustellen, dass es nicht auf der Durchreise manipuliert wurde. Die Signatur und der Prüfschlüssel werden erstellt, wenn das Modell auf dem Management-Hub veröffentlicht wird. Der Agent speichert das Modell im stammgeschützten Speicher auf dem Host. Für jeden Service wird ein Berechtigungsnachweis bereitgestellt, wenn er vom Agenten gestartet wird. Mithilfe dieses Berechtigungsnachweises identifiziert sich der Service selbst und erhält Zugriff auf die Modelle, auf die er zugreifen darf. Jedes Modellobjekt in {{site.data.keyword.ieam}} gibt die Liste der Services an, die auf das Modell zugreifen können. Jeder Service erhält immer dann einen neuen Berechtigungsnachweis, wenn er durch {{site.data.keyword.ieam}} erneut gestartet wird. Das Modellobjekt wird durch {{site.data.keyword.ieam}} nicht verschlüsselt. Da das Modellobjekt von {{site.data.keyword.ieam}} wie eine große Menge Bit behandelt wird, kann eine Serviceimplementierung das Modell bei Bedarf verschlüsseln. Weitere Informationen zur Verwendung des MMS finden Sie unter [Model Management-Details](../developing/model_management_details.md).

### Agbots
{: #agbots}

Der {{site.data.keyword.ieam}}-Management-Hub enthält mehrere Instanzen von Agbots, die dafür zuständig sind, die Bereitstellung von Workloads auf allen beim Management-Hub registrierten Edge-Knoten einzuleiten. Agbots prüfen laufend die in Exchange publizierten Bereitstellungsrichtlinien und -muster, wodurch sichergestellt wird, dass die Services in diesen Mustern und Richtlinien auf allen richtigen Edge-Knoten bereitgestellt werden. Sobald ein Agbot eine Bereitstellungsanforderung einleitet, sendet er die Anforderung über die sichere Steuerebene. Die Bereitstellungsanforderung enthält alle Elemente, die der Agent zum Prüfen der Workload und ihrer Konfiguration benötigt, wenn er die Anforderung gegebenenfalls akzeptiert. Weitere sicherheitsbezogene Details über die Aktivität des Agenten finden Sie unter [Agenten](security_privacy.md#agents). Der Agbot teilt dem MMS außerdem mit, wo und wann Modelle bereitgestellt werden sollen. Sicherheitsbezogene Details über die Verwaltung von Modellen finden Sie unter [Agenten](security_privacy.md#agents).

Ein manipulierter Agbot kann versuchen, schädliche Workloadbereitstellungen vorzuschlagen. Die vorgeschlagene Bereitstellung muss jedoch die Sicherheitsanforderungen erfüllen, die im Agentenabschnitt aufgeführt sind. Auch wenn der Agbot die Workloadbereitstellung einleitet, ist er nicht zur Erstellung von Workloads und Containerkonfigurationen berechtigt und kann daher keine eigenen schädlichen Workloads vorschlagen.

## {{site.data.keyword.horizon_exchange}}
{: #exchange}

{{site.data.keyword.horizon_exchange}} ist ein zentralisierter und replizierter REST-API-Server mit Lastausgleich. Er hat die Funktion einer gemeinsam genutzten Datenbank von Metadaten für Benutzer, Organisationen, Edge-Knoten, publizierte Services, Richtlinien und Muster. Darüber hinaus ermöglicht er den verteilten Agenten und Agbots die Bereitstellung von containerisierten Workloads, indem er den Speicher für die sichere Steuerebene bietet, bis die Nachrichten abgerufen werden können. {{site.data.keyword.horizon_exchange}} ist nicht in der Lage, die Steuernachrichten zu lesen, weil der Server nicht über den privaten RSA-Schlüssel zum Entschlüsseln der Nachricht verfügt. Eine manipulierte {{site.data.keyword.horizon_exchange}}-Instanz kann daher den Datenverkehr auf Steuerebene nicht ausspähen. Weitere Informationen zur Rolle von Exchange finden Sie im Abschnitt [{{site.data.keyword.edge}} im Überblick](../getting_started/overview_ieam.md).

## Services für privilegierten Modus
{: #priv_services}
Auf einer Hostmaschine können einige Tasks nur von einem Konto mit Rootzugriff ausgeführt werden. Das Äquivalent für Container ist privilegierter Modus. Während Container im Allgemeinen keinen privilegierten Modus auf dem Host benötigen, gibt es einige Anwendungsfälle, in denen dies erforderlich ist. In {{site.data.keyword.ieam}} haben Sie die Möglichkeit, anzugeben, dass ein Service mit aktivierter privilegierter Prozessausführung implementiert werden soll. Die Protokollierung ist standardmäßig inaktiviert. Sie müssen sie explizit in der [Implementierungskonfiguration](https://open-horizon.github.io/anax/deployment_string.html) der jeweiligen Servicedefinitionsdatei für jeden Service aktivieren, der in diesem Modus ausgeführt werden muss. Außerdem muss jeder Knoten, auf dem Sie diesen Service implementieren möchten, auch explizit Container für privilegierte Modi zulassen. Auf diese Weise wird sichergestellt, dass die Knoteneigner eine gewisse Kontrolle darüber haben, welche Services auf ihren Edge-Knoten ausgeführt werden. Ein Beispiel für die Aktivierung der Richtlinie für den privilegierten Modus auf einem Edge-Knoten finden Sie unter [privilegierte Knotenrichtlinie](https://github.com/open-horizon/anax/blob/master/cli/samples/privileged_node_policy.json). Wenn die Servicedefinition oder eine ihrer Abhängigkeiten den privilegierten Modus erfordert, muss die Knotenrichtlinie auch den privilegierten Modus zulassen, oder aber keiner der Services wird nicht auf dem Knoten implementiert. Eine eingehende Beschreibung des privilegierten Modus' finden Sie unter [Was ist der privilegierte Modus und benötige ich ihn?](https://wiki.lfedge.org/pages/viewpage.action?pageId=44171856).

## Denial-of-Service-Attacken
{: #denial}

Der {{site.data.keyword.ieam}}-Management-Hub ist ein zentralisierter Service. Zentralisierte Services in typischen cloudbasierten Umgebungen sind im Allgemeinen anfällig für Denial-of-Service-Attacken. Der Agent benötigt nur dann eine Verbindung, wenn er zum ersten Mal beim Hub registriert wird oder wenn er die Bereitstellung einer Workload vereinbart. In allen anderen Situationen wird der Agent auch dann weiter normal betrieben, wenn er keine Verbindung zum {{site.data.keyword.ieam}}-Management-Hub hat.  Dies stellt sicher, dass der {{site.data.keyword.ieam}}-Agent auf dem Edge-Knoten auch dann aktiv bleibt, wenn der Management-Hub angegriffen wird.

## Model Management-System
{: #malware}

{{site.data.keyword.ieam}} führt keine Malware- oder Virenprüfung für Daten durch, die in das MMS hochgeladen werden. Stellen Sie sicher, dass alle hochgeladenen Daten geprüft werden, bevor Sie sie in das MMS hochladen.

## Ruhende Daten
{: #drest}

Ruhende Daten werden von {{site.data.keyword.ieam}} nicht verschlüsselt. Die Verschlüsselung von ruhenden Daten sollte in Form eines Dienstprogramms implementiert werden, das für das Hostbetriebssystem geeignet ist, unter dem der {{site.data.keyword.ieam}}-Management-Hub oder -Agent ausgeführt wird.

## Sicherheitsstandards
{: #standards}

In {{site.data.keyword.ieam}} werden die folgenden Sicherheitsstandards genutzt:
* TLS 1.2 (HTTPS) wird zur Verschlüsselung von Daten bei der Übertragung an den und vom Management-Hub verwendet.
* Die AES-256-Bit-Verschlüsselung wird für Daten bei der Übertragung eingesetzt, insbesondere für Nachrichten, die über die sichere Steuerebene gesendet werden.
* 2048-Bit-RSA-Schlüsselpaare werden für Daten bei der Übertragung verwendet, insbesondere für den symmetrischen AES-256-Schlüssel, der über die sichere Steuerebene gesendet wird.
* Von einem Benutzer bereitgestellte RSA-Schlüssel werden bei Verwendung des Befehls **hzn exchange service publish** zum Signieren von Containerbereitstellungskonfigurationen eingesetzt.
* Ein durch den Befehl **hzn key create** generiertes RSA-Schlüsselpaar, wenn der Benutzer diesen Befehl veerwendet. Dieser Schlüssel ist standardmäßig 4096 Bit groß, kann jedoch vom Benutzer geändert werden.

## Zusammenfassung
{: #summary}

{{site.data.keyword.edge_notm}} nutzt Hashwerte, kryptografische Signaturen und die Verschlüsselung, um die Sicherheit vor einem unbefugten Zugriff zu gewährleisten. Durch die überwiegend dezentrale Konzeption von {{site.data.keyword.ieam}} werden Sicherheitslücken für die meisten Attacken vermieden, die normalerweise in Edge-Computing-Umgebungen möglich sind. Durch die Beschränkung des Kompetenzrahmens für die Teilnehmerrollen isoliert {{site.data.keyword.ieam}} den potenziellen Schaden durch einen manipulierten Host oder eine manipulierte Softwarekomponente in der betroffenen Systemkomponente. Sogar externe Attacken im großen Stil, die gegen die zentralen Services der {{site.data.keyword.horizon}}-Services ausgeführt werden, die in {{site.data.keyword.ieam}} eingesetzt werden, haben so nur minimale Auswirkungen auf die Ausführung von Workloads in der Peripherie.
