{:shortdesc: .shortdesc}
{:new_window: target="_blank"}

# Glossar
*Letzte Aktualisierung: 6. Mai 2021*

Dieses Glossar enthält Begriffe und Definitionen für {{site.data.keyword.edge}}.
{:shortdesc}

In diesem Glossar werden die folgenden Querverweise verwendet:

- *Siehe* verweist von einem nicht bevorzugten Begriff auf den bevorzugten Begriff oder von einer Abkürzung auf die ausgeschriebene Form.
- *Siehe auch* verweist auf einen verwandten Begriff oder einen Begriff mit gegenteiliger Bedeutung.

<!--If you do not want letter links at the top of your glossary, delete the text between these comment tags.-->

[A](#glossa) [B](#glossb) [C](#glossc) [D](#glossd) [E](#glosse) [F](#glossf) [G](#glossg) [H](#glossh) [I](#glossi) [K](#glossk) [L](#glossl) [M](#glossm) [N](#glossn) [O](#glosso) [P](#glossp) [R](#glossr) [S](#glosss) [T](#glosst) [V](#glossv) [W](#glossw)

<!--end letter link tags-->

## A
{: #glossa}

### API-Schlüssel
{: #x8051010}

Ein eindeutiger Code, der an eine API weitergeleitet wird, um eine aufrufende Anwendung oder einen Benutzer zu identifizieren. Ein API-Schlüssel wird verwendet, um zu überwachen und zu kontrollieren, wie die API verwendet wird, z. B. um zu vermeiden, dass die API böswillig oder missbräuchlich verwendet wird.

### Anwendung
{: #x2000166}

Ein oder mehr Computerprogramme oder Softwarekomponenten, die eine Funktion zur direkten Unterstützung eines bestimmten Geschäftsprozesses oder Prozesses bereitstellen.

### Verfügbarkeitszone
{: #x7018171}

Ein von Bedienern zugeordnetes, funktional unabhängiges Segment der Netzinfrastruktur.

## B
{: #glossb}

### Bootknoten
{: #x9520233}

Ein Knoten, der für die Ausführung der Installation, der Konfiguration, der Knotenskalierung und für Clusteraktualisierungen verwendet wird.

### Geschäftsrichtlinie
{: #x62309388}

(veraltet) Der vorherige Begriff für die Implementierungsrichtlinie.

## C
{: #glossc}

### Katalog
{: #x2000504}

Ein zentraler Ort, an dem Sie nach Paketen in einem Cluster suchen und sie installieren können.

### Cluster
{: #x2017080}

Eine Gruppe von Ressourcen, Workerknoten, Netzen und Speichereinheiten, die dafür sorgen, dass Apps verfügbar sind und in Containern bereitgestellt werden können.

### Einschränkungen
{: #x62309387}

Logische Ausdrücke in Bezug auf Eigenschaften. Einschränkungen werden zur Steuerung und Verwaltung der Softwareimplementierung auf Edge-Knoten verwendet.

### Container
{: #x2010901}

Ein Systemkonstrukt, das es Benutzern ermöglicht, gleichzeitig separate logische Betriebssysteminstanzen auszuführen. Container verwenden Layers von Dateisystemen, um die Imagegrößen zu minimieren und eine Wiederverwendung zu ermöglichen. Siehe auch [Image](#x2024928), [Layer](#x2028320), [Registry](#x2064940).

### Container-Image
{: #x8941555}

In Docker: Eigenständig ausführbare Software (einschließlich Code- und Systemtools), die zum Ausführen einer Anwendung verwendet werden kann.

### Containerorchestrierung
{: #x9773849}

Der Prozess der Lebenszyklusverwaltung von Containern, einschließlich Einrichtung, Bereitstellung und Verfügbarkeit.

## D
{: #glossd}

### Bereitstellung
{: #x2104544}

Ein Prozess, bei dem Pakete oder Images abgerufen und an einer definierten Position installiert werden, damit sie getestet oder ausgeführt erden können.

### Bereitstellungsmuster
{: #x623093810}

Eine Liste bestimmter implementierbarer Services. Muster sind eine Vereinfachung des allgemeineren und leistungsfähigeren Richtlinienmechanismus. Edge-Knoten können sich mit einem Bereitstellungsmuster registrieren, um die Implementierung des Servicepakets des Musters zu veranlassen.

### Bereitstellungsrichtlinie
{: #x62309386}

Eine Gruppe von Eigenschaften und Bedingungen, die sich auf die Implementierung eines bestimmten Service zusammen mit einer Kennung für die zu implementierende Serviceversion und andere Informationen beziehen, z. B., wie die Rollbacks gehandhabt werden sollen, wenn Fehler auftreten.

### DevOps
{: #x5784896}

Eine Softwaremethodik für die Integration von Anwendungsentwicklung und IT-Operationen, mit deren Hilfe Teams Code schneller an die Produktion übergeben und anhand von Rückmeldungen vom Markt kontinuierlich verbessern können.

### Docker
{: #x7764788}

Eine offene Plattform, die Entwickler und Systemadministratoren verwenden können, um verteilte Anwendungen zu erstellen, auszuliefern und auszuführen.

## E
{: #glosse}

### Edge-Computing
{: #x9794155}

Ein Modell für die verteilte Datenverarbeitung, das Rechenleistung außerhalb der traditionellen Rechenzentren und Cloudrechenzentren nutzt. In einem Edge-Computing-Modell werden Workloads näher am Erstellungsort der zugehörigen Daten und damit näher an dem Ort platziert, an dem die Aktionen ausgeführt werden, die in Beantwortung der Analyseergebnisse für diese Daten ausgeführt werden. Durch die Platzierung von Daten und Workloads auf Einheiten am Rand (engl. Edge) des Netzes können die Latenzzeit und der Bedarf an Netzbandbreiten reduziert, die Vertraulichkeit sensibler Daten besser geschützt und der Systembetrieb auch während eines Netzausfalls aufrecht erhalten werden.

### Edge-Einheit
{: #x2026439}

Eine Komponente der Betriebseinrichtung eines Unternehmens (z. B. eine Montagemaschine in einer Fabrik, ein Geldautomat, eine intelligente Kamera oder ein Automobil), die über integrierte Rechenleistung verfügt, über die sinnvolle Arbeiten ausgeführt und Daten erfasst oder generiert werden können.

### Edge-Gateway
{: #x9794163}

Ein Edge-Cluster, der über Services verfügt, die Netzfunktionen wie beispielsweise die Protokollumsetzung, den Netzabschluss, die Tunnelung sowie den Firewallschutz oder die Herstellung drahtloser Verbindungen ausführen. Ein Edge-Gateway dient als Verbindungspunkt zwischen einer Edge-Einheit oder einem Edge-Cluster und der Cloud oder einem größeren Netz.

### Edge-Knoten
{: #x8317015}

Eine Edge-Einheit, ein Edge-Cluster oder ein Edge-Gateway, auf der bzw. dem das Edge-Computing ausgeführt wird.

### Edge-Cluster
{: #x2763197}

Ein Computer an einer fernen Betriebsstätte, auf dem Workloads für Unternehmensanwendungen und gemeinsam genutzte Services ausgeführt werden. Ein Edge-Cluster kann verwendet werden, um eine Verbindung zu einer Edge-Einheit oder zu einem anderen Edge-Cluster herzustellen oder um als Edge-Gateway für die Herstellung einer Verbindung zur Cloud oder zu einem größeren Netz zu dienen.

### Edge-Service
{: #x9794170}

Ein Service, der speziell zur Bereitstellung auf einem Edge-Cluster, Edge-Gateway oder einer Edge-Einheit vorgesehen ist. Edge-Services dienen zur Ausführung verschiedener Aufgaben, z. B. zur Durchführung der visuellen Erkennung, zur Gewinnung akustischer Einsichten sowie zur Spracherkennung.

### Edge-Workload
{: #x9794175}

Jeder Service, Mikroservice oder jede Softwarekomponente, die während der Ausführung sinnvolle Aufgaben auf einem Edge-Knoten ausführt.

### Endpunkt
{: #x2026820}

Eine Zieladresse im Netz, die von Kubernetes-Ressourcen zugänglich gemacht wird, z. B. als Service oder Ingress.

## F
{: #glossf}

## G
{: #glossg}

### Grafana
{: #x9773864}

Eine Open-Source-Analyse- und -Visualisierungsplattform zum Überwachen, Durchsuchen, Analysieren und Darstellen von Metriken.

## H
{: #glossh}

### HA
{: #x2404289}

Siehe [Hochverfügbarkeit](#x2284708).

### Helm Chart
{: #x9652777}

Ein Helm-Paket, das Informationen für die Installation einer Gruppe von Kubernetes-Ressourcen in einem Kubernetes-Cluster enthält.

### Helm-Release
{: #x9756384}

Eine Instanz eines Helm Charts, die in einem Kubernetes-Cluster ausgeführt wird.

### Helm-Repository
{: #x9756389}

Eine Sammlung von Charts.

### Hochverfügbarkeit
{: #x2284708}

Die Fähigkeit von IT-Services, Ausfälle zu vermeiden und die Verarbeitung gemäß einem vordefinierten Service-Level aufrechtzuerhalten. Solche Ausfälle decken sowohl geplante Ereignisse (wie z. B. Wartung und Sicherungen) als auch ungeplante Ereignisse (wie z. B. Software- und Hardwarefehler, Stromausfälle sowie Stör- und Katastrophenfälle) ab. Siehe auch [Fehlertoleranz](#x2847028).

## I
{: #glossi}

### IBM Cloud Pak
{: #x9773840}

Ein Paket mit mindestens einem auf Unternehmen abgestimmten, sicheren IBM Certified Container-Angebot, dessen Lebenszyklus verwaltet wird. Diese Angebote werden zu Paketen zusammengefasst und in die IBM Cloud-Umgebung integriert.

### Image
{: #x2024928}

Ein Dateisystem und seine Ausführungsparameter, die in einer Containerlaufzeit zum Erstellen eines Containers verwendet werden. Das Dateisystem besteht aus einer Reihe von Layern, die während der Laufzeit kombiniert und während des Builds des Images in aufeinanderfolgende Aktualisierungen erstellt werden. Das Image behält seinen Status bei der Ausführung des Containers nicht. Siehe auch [Container](#x2010901), [Layer](#x2028320), [Registry](#x2064940).

### Image-Registry
{: #x3735328}

Eine zentrale Position für die Verwaltung von Images.

### Ingress
{: #x7907732}

Eine Sammlung von Regeln, die eingehende Verbindungen zu den Kubernetes-Cluster-Services zulassen.

### Isolation
{: #x2196809}

Der Prozess, bei dem die Workloadbereitstellungen auf dedizierte virtuelle und physische Ressourcen beschränkt werden, um eine Multi-Tenancy-Unterstützung zu erreichen.

## K
{: #glossk}

### Klusterlet
{: #x9773879}

In IBM Multicloud Manager der für einen einzelnen Kubernetes-Cluster verantwortliche Agent.

### Kubernetes
{: #x9581829}

Ein Open-Source-Orchestrierungstool für Container.

## L
{: #glossl}

### Layer
{: #x2028320}

Eine geänderte Version eines übergeordneten Images. Images bestehen aus Layern, bei denen die geänderte Version zum Erstellen des neuen Images auf dem übergeordneten Image angeordnet wird. Siehe auch [Container](#x2010901), [Image](#x2024928).

### Lastausgleichsfunktion
{: #x2788902}

Software oder Hardware, die die Workload über mehrere Server verteilt, um sicherzustellen, dass die Server nicht überlastet werden. Die Lastausgleichsfunktion leitet Benutzer auch an einen anderen Server weiter, wenn der ursprüngliche Server ausfällt.

## M
{: #glossm}

### Managementkonsole
{: #x2398932}

Die grafische Benutzerschnittstelle für {{site.data.keyword.edge_notm}}.

### Management-Hub
{: #x3954437}

Der Cluster, der die zentralen Komponenten von {{site.data.keyword.edge_notm}} hostet.

### Marketplace
{: #x2118141}

Eine Liste der aktivierten Services, über die die Benutzer Ressourcen bereitstellen können.

### Masterknoten
{: #x4790131}

Ein Knoten, der Management-Services zur Verfügung stellt und die Workerknoten in einem Cluster steuert. Masterknoten sind Hosts für Prozesse, die für die Ressourcenzuordnung, die Statusverwaltung, die Zeitplanung und die Überwachung verantwortlich sind.

### Mikroservice
{: #x8379238}

Eine Gruppe kleiner, unabhängiger Architekturkomponenten, die jeweils einem bestimmten Zweck dienen und über eine einfache gemeinsame API kommunizieren.

### Multicloud
{: #x9581814}

Ein Cloud-Computing-Modell, bei dem ein Unternehmen eine kombinierte On-Premises-, Private-Cloud- und Public-Cloud-Architektur verwendet.

## N
{: #glossn}

### Namespace
{: #x2031005}

Ein virtueller Cluster in einem Kubernetes-Cluster, der zum Organisieren und Aufteilen von Ressourcen für mehrere Benutzer verwendet werden kann.

### Network File System
{: #x2031282}

Ein Protokoll, das es einem Computer ermöglicht, über ein Netz so auf Dateien zuzugreifen, als ob sie sich auf den lokalen Platten befänden.

### NFS
{: #x2031508}

Informationen hierzu finden Sie unter [Network File System](#x2031282).

### Knotenrichtlinie
{: #x62309384}

Eine Gruppe von Eigenschaften und Bedingungen, die sich auf einen Edge-Knoten beziehen (entweder ein eigenständiger Linux-Edge-Knoten oder ein Kubernetes-Cluster-Knoten).

## O
{: #glosso}

### Org
{: #x7470494}

Siehe [Organisation](#x2032585).

### Organisation
{: #x2032585}

Das oberste Metaobjekt in der {{site.data.keyword.edge_notm}}-Infrastruktur, das die Objekte eines Kunden darstellt.

## P
{: #glossp}

### Muster
{: #x62309389}

Siehe [Bereitstellungsmuster](#x623093810).

### Persistenter Datenträger
{: #x9532496}

Netzspeicher in einem Cluster, der von einem Administrator eingerichtet wird.

### Anforderung eines persistenten Datenträgers
{: #x9520297}

Das Anfordern von Clusterspeicher.

### Pod
{: #x8461823}

Eine Gruppe von Containern, die in einem Kubernetes-Cluster ausgeführt werden. Ein Pod ist eine ausführbare Arbeitseinheit, bei der es sich entweder um eine eigenständige Anwendung oder um einen Mikroservice handelt.

### Pod-Sicherheitsrichtlinie
{: #x9520302}

Eine Richtlinie, die zur Einrichtung einer Steuerung auf Clusterebene der für einen Pod verfügbaren Funktionen und Zugriffsrechte dient.

### policy
{: #x62309382}

Eine Sammlung von null oder mehr Eigenschaften und null oder mehr Einschränkungen, manchmal mit zusätzlichen Datenfeldern. Siehe [Knotenrichtlinie](#x62309384), [Servicerichtlinie](#x62309385) und [Implementierungsrichtlinie](#x62309386).

### Prometheus
{: #x9773892}

Ein Open-Source-Systemüberwachungs- und -Alerting-Toolkit.

### Eigenschaften
{: #x62309381}

Name/Wert-Paare, die häufig verwendet werden, um Knotenattribute (wie Modell, Seriennummer, Rolle, Funktionalität, angeschlossene Hardware usw.) oder Attribute eines Service oder einer Implementierung zu beschreiben. Siehe [Richtlinie](#x62309382).

### Proxy-Knoten
{: #x6230938}

Ein Knoten, der externe Anforderungen an die Services überträgt, die in einem Cluster erstellt werden.

## R
{: #glossr}

### RBAC
{: #x5488132}

Siehe [Rollenbasierte Zugriffssteuerung](#x2403611).

### Registry
{: #x2064940}

Ein öffentlicher oder privater Container-Image-Speicher- und -Verteilungsservice. Siehe auch [Container](#x2010901), [Image](#x2024928).

### Repo
{: #x7639721}

Siehe [Repository](#x2036865).

### Repository
{: #x2036865}

Ein persistenter Speicherbereich für Daten und andere Anwendungsressourcen.

### Ressource
{: #x2004267}

Eine physische oder logische Komponente, die für eine Anwendungs- oder Serviceinstanz eingerichtet oder reserviert werden kann. Zu den Beispielen für Ressourcen gehören Datenbanken und Konten, Prozessoren, Speicher und Speichergrenzwerte.

### Rollenbasierte Zugriffssteuerung
{: #x2403611}

Der Prozess, bei dem die integralen Komponenten eines Systems auf der Basis von Benutzerauthentifizierung, Rollen und Berechtigungen eingeschränkt werden.

## S
{: #glosss}

### Service-Broker
{: #x7636561}

Eine Komponente eines Service, die einen Katalog von Angeboten und Serviceplänen implementiert und die Aufrufe zum Bereitstellen und zum Aufheben der Bereitstellung sowie zum Binden und Aufheben der Bindung interpretiert.

### Servicerichtlinie
{: #x62309385}

Eine Gruppe von Eigenschaften und Einschränkungen, die sich auf einen bestimmten implementierbaren Service beziehen.

### Speicherknoten
{: #x3579301}

Ein Knoten, der zum Bereitstellen des Back-End-Speichers und des Dateisystems zum Speichern der Daten in einem System verwendet wird.

### Syslog
{: #x3585117}

Siehe [Systemprotokoll](#x2178419).

### Systemprotokoll
{: #x2178419}

Ein Protokoll, das von Cloud Foundry-Komponenten erstellt wird.

## T
{: #glosst}

### Team
{: #x3135729}

Eine Entität, die Benutzer und Ressourcen gruppiert.

## V
{: #glossv}

### VSAN
{: #x4592600}

Siehe [Virtual Storage Area Network](#x4592596).

## W
{: #glossw}

### Workerknoten
{: #x5503637}

In einem Cluster eine physische oder virtuelle Maschine, die die Bereitstellungen und Services enthält, aus denen eine App besteht.

### Workload
{: #x2012537}

Eine Gruppe von virtuellen Servern, die einen vom Kunden definierten gemeinsamen Zweck erfüllen. Eine Workload kann im Allgemeinen als mehrschichtige Anwendung angesehen werden. Jede Workload wird mit einer Gruppe von Richtlinien verknüpft, die die Leistungs- und Energieverbrauchsziele definieren.
