---

copyright:
years: 2019, 2020
lastupdated: "2020-02-13"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Bewährte Verfahren bei der Edge-nativen Entwicklung
{: #edge_native_practices}

Sie erstellen Workloads, die in der Edge betrieben werden, in Recheneinrichtungen, die außerhalb der normalen Beschränkungen Ihres IT-Rechenzentrums oder der Cloudumgebung liegen. Das bedeutet, dass Sie die einzigartigen Bedingungen solcher Umgebungen berücksichtigen müssen. Dies wird als Edge-natives Programmiermodell bezeichnet.

## Bewährte Verfahren bei der Entwicklung von Edge-Services
{: #best_practices}

Die folgenden bewährten Verfahren (Best Practices) und Richtlinien unterstützen Sie beim Entwerfen und Entwickeln von Edge-Services für die Verwendung mit {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}).
{:shortdesc}

Die Automatisierung der Ausführung von Services in der Peripherie eines Systems (im Edge-Bereich) unterscheidet sich wie folgt von der Automatisierung von Services in der Cloud: 

* Die Anzahl der Edge-Knoten kann erheblich höher sein.
* Die Netze, über die die Verbindungen zu den Edge-Knoten hergestellt werden, können weniger zuverlässig und deutlich langsamer sein. Edge-Knoten befinden sich häufig hinter Firewalls, sodass die Herstellung von Verbindungen von der Cloud zu den Edge-Knoten normalerweise nicht möglich ist.
* Für Edge-Knoten gelten Ressourcenbeschränkungen.
* Eine Motivation für Betriebsworkloads an der Edge ist die Möglichkeit, die Latenz zu reduzieren und die Netzbandbreite zu optimieren. Dies macht die Verteilung der Workloads in Relation zum Erstellungsort der Daten zu einem wichtigen Faktor. 
* Edge-Knoten befinden sich normalerweise an fernen Standorten und werden daher nicht von den IT-Mitarbeitern eingerichtet. Nach der Einrichtung eines Edge-Knotens stehen möglicherweise keine Mitarbeiter für die Verwaltung des Knotens zur Verfügung. 
* Edge-Knoten gelten im Allgemeinen auch als weniger vertrauenswürdig als Cloud-Server.

Aufgrund dieser Unterschiede sind bei der Bereitstellung und der Verwaltung der Software auf Edge-Knoten unterschiedliche Verfahren erforderlich. {{site.data.keyword.edge_ieam}} wurde speziell für das Management von Edge-Knoten entworfen. Wenn Sie Services erstellen, sollten Sie die folgenden Richtlinien berücksichtigen, um sicherzustellen, dass diese Services für das Arbeiten mit Edge-Knoten geeignet sind. 

## Richtlinien zur Entwicklung von Services
{: #service_guidelines}


* **Cloud-natives Programmiermodell:** Das Edge-native Programmiermodell übernimmt viele der Prinzipien aus der Cloud-nativen Programmierung, darunter:

  * Aufteilen der Workloads in Komponenten und Containerisieren - konstruieren Sie Ihre Anwendung um einen Satz von Mikroservices, jeweils verpackt in logisch zusammenhängende Gruppen. Sorgen Sie jedoch für ein Gleichgewicht dieser Gruppen, damit erkennbar wird, welche unterschiedlichen Container am besten auf den verschiedenen Schichten oder Edge-Knoten arbeiten könnten.
  * Machen Sie APIs für Ihre Mikroservices zugänglich, die es anderen Teilen Ihrer Anwendung ermöglichen, die Services zu finden, von denen sie abhängig sind.
  * Konstruieren Sie lose Kopplungen zwischen Mikroservices, um ihnen die Möglichkeit zu geben, unabhängig voneinander zu arbeiten, und um statusabhängige Annahmen zu vermeiden, die zu Affinitäten zwischen Services führen, welche andernfalls die elastische Skalierung, Failover und Wiederherstellung behindern würden.
  * Richten Sie kontinuierliche Integration und kontinuierliche Bereitstellung (Continuous Delivery und Continuous Deployment, CI/CD), gekoppelt mit Praktiken der agilen Entwicklung, innerhalb eines DevOps-Frameworks ein.
  * Nutzen Sie vielleicht die folgenden Ressourcen, um weitere Informationen zu den Praktiken der Cloud-nativen Programmierung zu erhalten:
    * [10 SCHLÜSSELATTRIBUTE VON CLOUD-NATIVEN ANWENDUNGEN ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://thenewstack.io/10-key-attributes-of-cloud-native-applications/)
    * [Cloud-native Programmierung ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://researcher.watson.ibm.com/researcher/view_group.php?id=9957)
    *	[Informationen zu Cloud-nativen Anwendungen ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://www.redhat.com/en/topics/cloud-native-apps)

* **Serviceverfügbarkeit:** Wenn für Ihren Service-Container der Einsatz anderer Service-Container erforderlich ist, muss Ihr Service in Situationen, in denen diese Services nicht verfügbar sind, eine gewisse Toleranz aufweisen. Wenn Container beispielsweise erstmals gestartet werden, können auch dann, wenn sie von einer Position am Ende des Abhängigkeitsdiagramms gestartet werden (Aufwärtsrichtung), Unterschiede bei der Geschwindigkeit des Startvorgangs der Services bestehen. In diesem Fall müssen Ihre Service-Container den Startvorgang unter Umständen mehrmals wiederholen, während sie darauf warten, dass die Abhängigkeiten voll funktionsfähig werden. Ähnliches gilt, wenn ein abhängiger Service-Container, der automatisch aktualisiert wird, erneut gestartet wird. Es hat sich bewährt, für Ihre Services eine gewisse Toleranz gegenüber Unterbrechungen von Services vorzusehen, von denen sie abhängig sind. 
* **Portierbarkeit:** Die Edge-Computing-Landschaft umfasst mehrere Schichten des Systems, einschließlich Edge-Einheiten, Edge-Clustern und Netz- oder Metro-Edge-Positionen. Wo Ihre containerisierte Edge-Workload letztlich angeordnet wird, hängt von einer Kombination von Faktoren ab, darunter der Abhängigkeit von bestimmten Ressourcen wie Sensordaten und Aktuatoren, Anforderungen an die Endlatenz sowie verfügbarer Rechenkapazität. Die Workload sollte so konzipiert sein, dass sie in verschiedenen Schichten des Systems angeordnet werden kann, je nach dem Bedarf des Kontextes, in dem Ihre Anwendung verwendet werden wird.
* **Containerorchestrierung:** Dies bezieht sich weiterhin auf den vorangehenden Aspekt zur mehrschichtigen Portierbarkeit: Gewöhnlich werden Edge-Einheiten mit nativer Docker-Laufzeit betrieben, ohne lokale Containerorchestrierung. Edge-Cluster und Netz-/Metro-Edges werden mit Kubernetes konfiguriert, um die Workload für Anforderungen gemeinsam genutzter, konkurrierender Ressourcen zu orchestrieren. Stellen Sie Ihre Container vorzugsweise so bereit, dass explizite Abhängigkeiten von Docker oder Kubernetes vermieden werden und die Portierbarkeit auf unterschiedliche Schichten der verteilten Edge-Computing-Landschaft ermöglicht wird. 
* **Externalisieren von Konfigurationsparametern:** Verwenden Sie die integrierte Unterstützung, die von {{site.data.keyword.ieam}} bereitgestellt wird, um Konfigurationsvariablen und Ressourcenabhängigkeiten zu externalisieren, sodass diese bereitgestellt und auf Werte aktualisiert werden können, die für den Knoten spezifisch sind, auf dem Ihr Container bereitgestellt wird.
* **Hinweise zur Größe:** Ihre Service-Container sollten möglichst klein sein, sodass die Services auch über Netze mit möglicherweise geringer Übertragungsgeschwindigkeit oder auf Edge-Einheiten mit geringer Kapazität bereitgestellt werden können. Verwenden Sie die folgenden Verfahren, um kleinere Service-Container zu entwickeln: 

  * Verwenden Sie Programmiersprachen, die zur Erstellung kleinerer Services geeignet sind:
    * Ideal: go, rust, c, sh
    * OK: c++, python, bash
    * Erwägen Sie die Verwendung von Node.js-, Java- und JVM-basierten Sprachen wie z. B. scala
  * Verwenden Sie Verfahren, die zur Erstellung kleinerer Docker-Images geeignet sind:
    * Verwenden Sie Alpine als Basisimage für {{site.data.keyword.linux_notm}}.
    * Verwenden Sie zur Installation von Paketen in einem Alpine-basierten Image den Befehl `apk --no-cache --update add`, um die Speicherung des Paketcaches zu vermeiden, der für den Laufzeitbetrieb nicht benötigt wird.
    * Löschen Sie Dateien in derselben Dockerfile-Ebene (Befehl), in der die Dateien hinzugefügt werden. Wenn Sie eine separate Dockerfile-Befehlszeile verwenden, um die Dateien aus dem Image zu löschen, erhöhen Sie dadurch die Größe des Container-Images. Sie können z. B. `&&` verwenden, um die Befehle zum Herunterladen, zur Verwendung und zum anschließenden Löschen von Dateien zu Gruppen zusammenzufassen, und zwar mit einem einzigen Dockerfile-Befehl `RUN`.
    * Integrieren Sie keine Build-Tools in Ihr Docker-Laufzeitimage. Verwenden Sie als bewährtes Verfahren einen [mehrstufigen Docker-Build ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://docs.docker.com/develop/develop-images/multistage-build/), um die Laufzeitartefakte zu erstellen. Kopieren Sie anschließend die erforderlichen Laufzeitartefakte wie beispielsweise die ausführbaren Komponenten, selektiv in das Docker-Laufzeitimage. 
* **Erstellen Sie Services, die in sich abgeschlossen sind:** Da Services über ein Netz an die Edge-Knoten gesendet und dort autonom gestartet werden müssen, muss der Service-Container alle Komponenten enthalten, die für die Bereitstellung des Service benötigt werden. Diese Assets müssen im Container gebündelt werden (z. B. alle erforderlichen Zertifikate). Verlassen Sie sich bei der Ausführung der Aufgaben, mit denen alle Assets, die zur erfolgreichen Ausführung des Service erforderlich sind, zu dem Edge-Knoten hinzugefügt werden, nicht auf die Verfügbarkeit von Administratoren.
* **Datenschutz:** Mit jedem Mal, wo Sie private oder sensible Daten im Netz verschieben, erhöhen Sie die Anfälligkeit dieser Daten für Angriffe und Expositionen. Einer der Hauptvorteile des Edge-Computing ist die Möglichkeit, die Daten dort zu belassen, wo sie entstehen. Nutzen Sie diese Gelegenheit und schützen Sie Ihren Container. Idealerweise übertragen Sie diese Daten nicht an andere Services. Wenn es unumgänglich ist, Daten an andere Services oder Schichten des Systems zu übertragen, versuchen Sie, persönliche Identifikationsinformationen (PII), persönliche Gesundheitsdaten (PHI) oder persönliche Finanzdaten (PFI) durch Verbergungs- oder Anonymisierungsverfahren oder durch Verschlüsselung mit einem Schlüssel, dessen Eigner sich vollständig innerhalb der Grenzen Ihres Service befinden, für Angreifer unbrauchbar zu machen. 
* **Berücksichtigen Sie beim Entwurf und der Konfiguration die Automatisierung:** Edge-Knoten und die Services, die auf diesen Knoten ausgeführt werden, müssen der ZeroOps-Zielsetzung so weit wie möglich angenähert werden. {{site.data.keyword.ieam}} automatisiert die Bereitstellung und das Management von Services. Dazu müssen die Services jedoch so strukturiert sein, dass {{site.data.keyword.ieam}} in der Lage ist, diese Prozesse ohne Bedienereingriff voll automatisch durchzuführen. Berücksichtigen Sie die folgenden Richtlinien, um das Design auf die Zielsetzung der Automatisierung auszurichten:
  * Begrenzen Sie die Anzahl der Benutzereingabevariablen für einen Service. Für alle Benutzereingabevariablen, für die in der Servicedefinition keine Standardwerte definiert sind, müssen die Werte in jedem Edge-Knoten angegeben werden. Begrenzen Sie die Anzahl der Variablen oder vermeiden Sie die Verwendung von Services mit Variablen, sofern dies möglich ist.   
  * Wenn für einen Service zahlreiche Einstellungen konfiguriert werden müssen, sollten Sie eine Konfigurationsdatei verwenden, um die Variablen zu definieren. Nehmen Sie eine Standardversion der Konfigurationsdatei in den Service-Container auf. Verwenden Sie anschließend das {{site.data.keyword.ieam}} Model Management System, um dem Administrator zu ermöglichen, eine eigene Konfigurationsdatei bereitzustellen und im Lauf der Zeit zu aktualisieren.

  * **Nutzung von Standard-Plattformservices:** Viele Anforderungen Ihrer Anwendung können durch vorimplementierte Plattformservices erfüllt werden. Anstatt solche Funktionalitäten in Ihrer Anwendung von Grund auf neu einzurichten, erwägen Sie die Verwendung dessen, was bereits erstellt wurde und Ihnen zur Verfügung steht. Eine Quelle für solche Plattformservices ist IBM Cloud Pak, das einen weiten Bereich von Funktionalitäten abdeckt, von denen viele ihrerseits mithilfe Cloud-nativer Programmierung erstellt wurden, darunter:
    * **Datenmanagement:** Erwägen Sie IBM Cloud Pak for Data für Ihre Anforderungen in Bezug auf SQL- und Nicht-SQL-, Blockspeicher- und Objektspeicherdatenbanken, auf maschinelles Lernen, KI-Services und Data Lakes. 
    * **Sicherheit:** Erwägen Sie IBM CloudPak for Security für Ihre Anforderungen in Bezug auf Verschlüsselung, Code-Scanning und Erkennung von Angriffen von außen.
    * **Anwendungen:** Erwägen Sie IBM Cloud Pak for Applications für Ihre Anforderungen in Bezug auf Webanwendungen, Serverunabhängigkeit und Anwendungsframeworks.
