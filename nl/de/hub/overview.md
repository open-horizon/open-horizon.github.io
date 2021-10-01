---

copyright:
years: 2020
lastupdated: "2020-05-18"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Übersicht
{: #Overview}

Mit Edge-Computing können Sie Ihre Unternehmensanwendungen dorthin verlagern, wo Ihre Daten erstellt werden.
{:shortdesc}

* [Vorteile von Edge-Computing](#edge_benefits)
* [Beispiele](#examples)
* [Konzepte](#concepts)
  
Beim Edge-Computing handelt es sich um ein wichtiges Konzept für die Zukunft, mit dem Sie das Modell Ihres Systembetriebs erweitern können, indem Sie Ihre Cloud über ein Rechenzentrum oder Cloud-Computing-Zentrum hinaus virtualisieren. Beim Edge-Computing werden die Anwendungsworkloads von einem zentralen Standort an ferne Standorte verlagert, z. B. in Fabriken, Warenlagern, Verteilungszentren, Einzelhandelsgeschäfte, Transportzentren und andere Einrichtungen. Das Edge-Computing bietet Ihnen die Möglichkeiten zur Verlagerung Ihrer Anwendungsworkloads an einen beliebigen Standort, an dem Datenverarbeitungsoperationen außerhalb Ihrer Rechenzentren und Ihrer Cloud-Hosting-Umgebung benötigt werden.

{{site.data.keyword.ieam}} bietet Ihnen Edge-Computing-Funktionen, um Ihnen das Management und die Bereitstellung von Workloads über einen Hub-Cluster auf fernen Instanzen von {{site.data.keyword.open_shift_cp}} oder anderen auf Kubernetes basierenden Clustern zu ermöglichen.

{{site.data.keyword.ieam}} bietet außerdem Unterstützung für ein {{site.data.keyword.edge_profile}}. Dieses unterstützte Profil kann Sie bei der Reduzierung der Ressourcennutzung von {{site.data.keyword.open_shift_cp}} unterstützen, wenn {{site.data.keyword.open_shift_cp}} zum Hosting eines fernen Edge-Clusters installiert wird. Dieses Profil stellt die mindestens erforderlichen Services zur Unterstützung einer robusten fernen Managementlösung für diese Serverumgebungen und die unternehmenskritischen Anwendungen bereit, die von Ihnen an den entsprechenden Standorten gehostet werden. Mit diesem Profil können Sie weiterhin Benutzer authentifizieren, Protokoll- und Ereignisdaten erfassen und Workloads auf einem einfachen Workerknoten oder in einer Gruppe von Cluster-Workerknoten bereitstellen.

## Vorteile von Edge-Computing
{: #edge_benefits}

* Wertschöpfende Änderungen für Ihre Organisation: Die Verlagerung von Anwendungsworkloads auf Edge-Knoten zur Unterstützung des Systembetriebs an fernen Standorten, an denen die Daten erfasst werden, anstatt der Übertragung dieser Daten zur Verarbeitung an ein zentrales Rechenzentrum.

* Reduzierung der Abhängigkeiten von IT-Personal: Mit {{site.data.keyword.ieam}} wird es möglich, die Abhängigkeiten von Ihrem IT-Personal zu reduzieren. Mit {{site.data.keyword.ieam}} können Sie kritische Workloads auf Edge-Clustern für hunderte ferner Standorte über einen zentralen Standort sicher und zuverlässig bereitstellen und verwalten. Durch diese Funktionalität wird der Bedarf an IT-Vollzeitpersonal an jedem fernen Standort für die Verwaltung der Workloads vor Ort beseitigt.

## Beispiele
{: #examples}

Mit Edge-Computing können Sie Ihre Unternehmensanwendungen dorthin verlagern, wo Ihre Daten erstellt werden. Wenn Sie z. B. eine Fabrik betreiben, dann kann die Betriebseinrichtung Ihrer Fabrik mit Sensoren ausgestattet werden, die die Aufzeichnung einer beliebigen Anzahl von Datenpunkten ermöglichen, die Details zum Betriebsstatus Ihrer Anlage liefern. Diese Sensoren können beispielsweise die Anzahl der Teile, die pro Stunde zusammengebaut werden, die Zeitdauer, die von einer Stapelvorrichtung benötigt wird, um an ihre Ausgangsposition zurückzukehren, oder die Betriebstemperatur einer Fertigungsmaschine aufzeichnen. Die anhand dieser Datenpunkte gewonnenen Informationen sind z. B. nützlich, um zu ermitteln, ob Ihr Betrieb mit optimaler Effizienz arbeitet. Des Weiteren können Sie anhand dieser Informationen feststellen, welche Qualitätsstufen sie erreichen, oder voraussagen, wann eine Maschine voraussichtlich ausfallen wird und Instandhaltungsarbeiten erforderlich werden.

Ein weiteres Beispiel stellen Arbeiter an fernen Standorten dar, deren Job das Arbeiten in gefährlichen Umgebungen erforderlich macht, in denen die Überwachung der Umgebungsbedingungen erforderlich ist. Hierzu gehören z. B. Umgebungen mit starker Hitze- oder Lärmentwicklung, Umgebungen in der Nähe von Abgasen oder bei der Produktion entstehenden gasförmigen Kontaminationen oder im Bereich schwerer Maschinen. Sie können Informationen aus verschiedenen Quellen erfassen, die an den fernen Standorten verwendet werden können. Die Daten dieser Überwachungsaktivitäten können vom Aufsichtspersonal verwendet werden, um festzustellen, wann die Arbeiter zur Unterbrechung Ihrer Arbeit für Pausen, zur ausreichenden Flüssigkeitsversorgung oder zur Abschaltung der entsprechenden Betriebseinrichtung angewiesen werden müssen.

In einem weiteren Beispiel können Sie Videokameras verwenden, um bestimmte Einrichtungen (z. B. zur Erkennung von Fußgängerverkehr in Einzelhandelsunternehmen, Restaurants oder Unterhaltungseinrichtungen) zu überwachen, die Sicherheit durch die Aufzeichnung von Vandalismus oder anderer unerwünschter Aktivitäten zu verbessern oder Notfallsituationen zeitnah zu erkennen. Wenn Sie auch Videodaten aufzeichnen wollen, dann können Sie das Edge-Computing zur lokalen Verarbeitung von Videoanalysen verwenden, um Ihren Mitarbeitern das schnellere Reagieren auf bestimmte Vorfälle zu ermöglichen. Restaurantmitarbeiter können besser abschätzen, welche Menge an Nahrungsmitteln vorbereitet werden muss, Einzelhandelsmanager können feststellen, ob zusätzliche Kassen geöffnet werden müssen, und das Sicherheitspersonal kann schneller auf Notfallsituationen reagieren oder die zuständigen Notfalldienste benachrichtigen.

In allen diesen Fällen kann es bei der Übertragung der aufgezeichneten Daten an ein Cloud-Computing-Zentrum oder Rechenzentrum zu zusätzlichen Latenzzeiten bei der Datenverarbeitung kommen. Dieser Zeitverlust kann sich negativ auswirken, wenn es darauf ankommt, auf kritische Situationen oder bestimmte Ereignisse zügig zu reagieren.

Wenn es sich bei den aufgezeichneten Daten um Daten handelt, für die keine spezielle oder zeitkritische Verarbeitung erforderlich ist, dann können erhebliche Netz- und Speicherkosten entstehen, wenn diese normalen Daten unnötigerweise übertragen werden.

Des Weiteren bedeutet für sensible Daten wie beispielsweise personenbezogene Daten die Verlagerung vom Standort ihrer Erstellung an andere Standorte immer ein erhöhtes Risiko, dass diese Daten unbefugtem Zugriff ausgesetzt werden.

Darüber hinaus besteht bei Verwendung unzuverlässiger Netzverbindungen das Risiko, dass kritische Operationen unterbrochen werden.

## Konzepte
{: #concepts}

**Edge-Einheit**: Eine Komponente der Betriebsausrüstung (z. B. eine Montagemaschine in einer Fabrik, ein Geldautomat, eine intelligente Kamera oder ein Automobil) mit integrierter Rechenkapazität, über die sinnvolle Arbeiten ausgeführt und Daten erfasst oder generiert werden können.

**Edge-Gateway**: Ein Edge-Cluster, der über Services für Netzfunktionen wie Protokollumsetzung, Netzabschluss, Tunnelung, Firewallschutz oder Herstellung drahtloser Verbindungen verfügt. Ein Edge-Gateway dient als Verbindungspunkt zwischen einer Edge-Einheit oder einem Edge-Cluster und der Cloud oder einem größeren Netz.

**Edge-Knoten**: Eine Edge-Einheit, ein Edge-Cluster oder ein Edge-Gateway, auf der bzw. dem das Edge-Computing ausgeführt wird.

**Edge-Cluster**: Ein Computer an einer fernen Betriebsstätte, auf dem Workloads für Unternehmensanwendungen und gemeinsam genutzte Services ausgeführt werden. Ein Edge-Cluster kann verwendet werden, um eine Verbindung zu einer Edge-Einheit oder zu einem anderen Edge-Cluster herzustellen oder um als Edge-Gateway für die Herstellung einer Verbindung zur Cloud oder zu einem größeren Netz zu dienen.

**Edge-Service**: Ein Service, der speziell zur Bereitstellung auf einem Edge-Cluster, Edge-Gateway oder einer Edge-Einheit vorgesehen ist. Edge-Services dienen zur Ausführung verschiedener Aufgaben, z. B. zur Durchführung der visuellen Erkennung, zur Gewinnung akustischer Einsichten sowie zur Spracherkennung.

**Edge-Workload**: Jeder Service, Mikroservice oder jede Softwarekomponente, die während der Ausführung sinnvolle Aufgaben auf einem Edge-Knoten ausführt.

Öffentliche und private Netze sowie Netze zur Bereitstellung von Inhalten wandeln sich von einfachen Übertragungskomponenten in höherwertige Hosting-Umgebungen für Anwendungen in Gestalt der Edge-Netz-Cloud. Typische Anwendungsfälle für {{site.data.keyword.ieam}}:

* Bereitstellung von Edge-Knoten
* Rechenoperationsleistung von Edge-Knoten
* Unterstützung und Optimierung von Edge-Knoten

{{site.data.keyword.ieam}} führt Cloudplattformen der verschiedensten Hersteller in einem einheitlichen Dashboard zusammen, das den gesamten Bereich von lokal bis Edge abdeckt. {{site.data.keyword.ieam}} ist eine natürliche Erweiterung, mit der es möglich wird, die Verteilung und das Management von Workloads über das Edge-Netz hinaus auf Edge-Gateways und Edge-Einheiten auszudehnen. {{site.data.keyword.ieam}} erkennt auch Workloads aus Unternehmensanwendungen mit Edge-Komponenten, privaten und hybriden Cloudumgebungen sowie der öffentlichen Cloud. Dabei stellt {{site.data.keyword.ieam}} eine neue Ausführungsumgebung für verteilte künstliche Intelligenz (KI) bereit, um kritische Datenquellen zu erreichen.

Darüber hinaus bietet {{site.data.keyword.ieam}} KI-Tools für beschleunigtes Deep Learning, visuelle Erkennung und Spracherkennung sowie Video- und Tonanalysen und ermöglicht so eine Inferenzierung bei allen Auflösungen und mit den meisten Formaten von Video- und Audiodialogsystemen sowie Entdeckungen.

## Weitere Schritte

- [Dimensionierung und Systemvoraussetzungen](cluster_sizing.md)
- [Management-Hub installieren](hub.md)
