---

copyright:
years: 2020
lastupdated: "2020-4-8"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Edge-Cluster
{: #edge_clusters}

Dieser Abschnitt ist noch in Bearbeitung. Der Inhalt stammt aus from:https://www-03preprod.ibm.com/support/knowledgecenter/SSFKVV_4.1/servers/overview.html.

Mit Edge-Computing können Sie Ihre Unternehmensanwendungen dorthin verlagern, wo Ihre Daten erstellt werden.
{:shortdesc}

  * [Überblick](#overview)
  * [Vorteile von Edge-Computing](#edge_benefits)
  * [Beispiele](#examples)
  * [Architektur](#edge_arch)
  * [Konzepte](#concepts)

## Überblick
{: #overview}

Beim Edge-Computing handelt es sich um ein wichtiges Konzept für die Zukunft, mit dem Sie das Modell Ihres Systembetriebs erweitern können, indem Sie Ihre Cloud über ein Rechenzentrum oder Cloud-Computing-Zentrum hinaus virtualisieren. Beim Edge-Computing werden die Anwendungsworkloads von einem zentralen Standort an ferne Standorte verlagert, z. B. in Fabriken, Warenlagern, Verteilungszentren, Einzelhandelsgeschäfte, Transportzentren und andere Einrichtungen. Das Edge-Computing bietet Ihnen die Möglichkeiten zur Verlagerung Ihrer Anwendungsworkloads an einen beliebigen Standort, an dem Datenverarbeitungsoperationen außerhalb Ihrer Rechenzentren und Ihrer Cloud-Hosting-Umgebung benötigt werden.

{{site.data.keyword.edge_servers_notm}} bietet Ihnen Edge-Computing-Funktionen, um Ihnen das Management und die Bereitstellung von Workloads über einen Hub-Cluster auf fernen Instanzen von {{site.data.keyword.icp_server}} oder anderen auf Kubernetes basierenden Clustern zu ermöglichen.

{{site.data.keyword.edge_servers_notm}} verwendet {{site.data.keyword.mcm_core_notm}}, um die Bereitstellung containerisierter Workloads auf Edge-Servern, Gateways und anderen Einheiten zu kontrollieren, die von {{site.data.keyword.icp_server}}-Clustern an fernen Standorten gehostet werden.

{{site.data.keyword.edge_servers_notm}} bietet außerdem Unterstützung für ein {{site.data.keyword.edge_profile}}. Dieses unterstützte Profil kann Sie bei der Reduzierung der Ressourcennutzung von {{site.data.keyword.icp_server}} unterstützen, wenn {{site.data.keyword.icp_server}} zum Hosting eines fernen Edge-Servers installiert wird. Dieses Profil stellt die mindestens erforderlichen Services zur Unterstützung einer robusten fernen Managementlösung für diese Serverumgebungen und die unternehmenskritischen Anwendungen bereit, die von Ihnen an den entsprechenden Standorten gehostet werden. Mit diesem Profil können Sie weiterhin Benutzer authentifizieren, Protokoll- und Ereignisdaten erfassen und Workloads auf einem einfachen Workerknoten oder in einer Gruppe von Cluster-Workerknoten bereitstellen.

## Vorteile von Edge-Computing
{: #edge_benefits}

* Wertschöpfende Änderungen für Ihre Organisation: Die Verlagerung von Anwendungsworkloads auf Edge-Knoten zur Unterstützung des Systembetriebs an fernen Standorten, an denen die Daten erfasst werden, anstatt der Übertragung dieser Daten zur Verarbeitung an ein zentrales Rechenzentrum.

* Reduzierung der Abhängigkeiten von IT-Personal: Mit {{site.data.keyword.edge_servers_notm}} wird es möglich, die Abhängigkeiten von Ihrem IT-Personal zu reduzieren. Mit {{site.data.keyword.edge_servers_notm}} können Sie kritische Workloads für hunderte ferner Standorte über einen zentralen Standort sicher und zuverlässig bereitstellen und verwalten, ohne dass hierzu IT-Personal in Vollzeit an allen fernen Standorten zum lokalen Management der Workloads bereitgestellt werden muss.

## Beispiele
{: #examples}

Mit Edge-Computing können Sie Ihre Unternehmensanwendungen dorthin verlagern, wo Ihre Daten erstellt werden. Wenn Sie z. B. eine Fabrik betreiben, dann kann die Betriebseinrichtung Ihrer Fabrik mit Sensoren ausgestattet werden, die die Aufzeichnung einer beliebigen Anzahl von Datenpunkten ermöglichen, die Details zum Betriebsstatus Ihrer Anlage liefern. Diese Sensoren können beispielsweise die Anzahl der Teile, die pro Stunde zusammengebaut werden, die Zeitdauer, die von einer Stapelvorrichtung benötigt wird, um an ihre Ausgangsposition zurückzukehren, oder die Betriebstemperatur einer Fertigungsmaschine aufzeichnen. Die anhand dieser Datenpunkte gewonnenen Informationen sind z. B. nützlich, um zu ermitteln, ob Ihr Betrieb mit optimaler Effizienz arbeitet. Des Weiteren können Sie anhand dieser Informationen feststellen, welche Qualitätsstufen sie erreichen, oder voraussagen, wann eine Maschine voraussichtlich ausfallen wird und Instandhaltungsarbeiten erforderlich werden.

Ein weiteres Beispiel stellen Arbeiter an fernen Standorten dar, deren Job das Arbeiten in gefährlichen Umgebungen erforderlich macht, in denen die Überwachung der Umgebungsbedingungen erforderlich ist. Hierzu gehören z. B. Umgebungen mit starker Hitze- oder Lärmentwicklung, Umgebungen in der Nähe von Abgasen oder bei der Produktion entstehenden gasförmigen Kontaminationen oder im Bereich schwerer Maschinen. Sie können Informationen aus verschiedenen Quellen erfassen, die an den fernen Standorten verwendet werden können. Die Daten dieser Überwachungsaktivitäten können vom Aufsichtspersonal verwendet werden, um festzustellen, wann die Arbeiter zur Unterbrechung Ihrer Arbeit für Pausen, zur ausreichenden Flüssigkeitsversorgung oder zur Abschaltung der entsprechenden Betriebseinrichtung angewiesen werden müssen.

In einem weiteren Beispiel können Sie Videokameras verwenden, um bestimmte Einrichtungen (z. B. zur Erkennung von Fußgängerverkehr in Einzelhandelsunternehmen, Restaurants oder Unterhaltungseinrichtungen) zu überwachen, die Sicherheit durch die Aufzeichnung von Vandalismus oder anderer unerwünschter Aktivitäten zu verbessern oder Notfallsituationen zeitnah zu erkennen. Wenn Sie auch Videodaten aufzeichnen wollen, dann können Sie das Edge-Computing zur lokalen Verarbeitung von Videoanalysen verwenden, um Ihren Mitarbeitern das schnellere Reagieren auf bestimmte Vorfälle zu ermöglichen. Restaurantmitarbeiter können besser abschätzen, welche Menge an Nahrungsmitteln vorbereitet werden muss, Einzelhandelsmanager können feststellen, ob zusätzliche Kassen geöffnet werden müssen, und das Sicherheitspersonal kann schneller auf Notfallsituationen reagieren oder die zuständigen Notfalldienste benachrichtigen.

In allen diesen Fällen kann es bei der Übertragung der aufgezeichneten Daten an ein Cloud-Computing-Zentrum oder Rechenzentrum zu zusätzlichen Latenzzeiten bei der Datenverarbeitung kommen. Dieser Zeitverlust kann sich negativ auswirken, wenn es darauf ankommt, auf kritische Situationen oder bestimmte Ereignisse zügig zu reagieren.

Wenn es sich bei den aufgezeichneten Daten um Daten handelt, für die keine spezielle oder zeitkritische Verarbeitung erforderlich ist, dann können erhebliche Netz- und Speicherkosten entstehen, wenn diese normalen Daten unnötigerweise übertragen werden.

Des Weiteren bedeutet für sensible Daten wie beispielsweise personenbezogene Daten die Verlagerung vom Standort ihrer Erstellung an andere Standorte immer ein erhöhtes Risiko, dass diese Daten unbefugtem Zugriff ausgesetzt werden.

Darüber hinaus besteht bei Verwendung unzuverlässiger Netzverbindungen das Risiko, dass kritische Operationen unterbrochen werden.

## Architektur
{: #edge_arch}

Das Ziel besteht beim Edge-Computing im Schutz der Bereiche, die für das hybride Cloud-Computing erstellt wurden, um so den fernen Betrieb der Edge-Computing-Einrichtungen zu unterstützen. {{site.data.keyword.edge_servers_notm}} wurde für diesen Zweck entworfen.

Eine typische Bereitstellung von {{site.data.keyword.edge_servers_notm}} umfasst eine Instanz von {{site.data.keyword.icp_server}}, die im Rechenzentrum Ihres Hub-Clusters installiert wird. Diese {{site.data.keyword.icp_server}}-Instanz wird zum Hosten eines {{site.data.keyword.mcm_core_notm_novers}}-Controllers im Hub-Cluster verwendet. Der Hub-Cluster wird verwendet, um das Management Ihrer fernen Edge-Server durchzuführen. {{site.data.keyword.edge_servers_notm}} verwendet {{site.data.keyword.mcm_core_notm_novers}} zum Verwalten und Bereitstellen von Workloads aus dem Hub-Cluster auf den fernen Kubernetes-basierten Edge-Servern, wenn die lokale Verarbeitung erforderlich ist.

Diese Edge-Server können an fernen lokalen Standorten installiert werden, um Ihre Anwendungsworkloads dort zu verarbeiten, wo auch der unternehmenskritische Betrieb physisch stattfindet, also in Ihren Fabriken, Warenlagern, Einzelhandelsverkaufsstellen, Verteilzentren und anderen Einrichtungen. Eine Instanz von {{site.data.keyword.icp_server}} und von {{site.data.keyword.mcm_core_notm_novers}} {{site.data.keyword.klust}} sind an jedem der fernen Standorte erforderlich, an dem ein Edge-Server gehostet werden soll. Die {{site.data.keyword.mcm_core_notm_novers}} {{site.data.keyword.klust}}-Instanz wird zum fernen Management der Edge-Server verwendet.

Im folgenden Diagramm wird die allgemeine Topologie für eine typische Edge-Computing-Konfiguration dargestellt, in der {{site.data.keyword.icp_server}} und {{site.data.keyword.mcm_core_notm_novers}} verwendet wird:

<img src="../images/edge/edge_server_data_center.svg" alt="{{site.data.keyword.edge_servers_notm}}-Topologie" width="50%">

Im folgenden Diagramm wird eine typische allgemeine Architektur für ein {{site.data.keyword.edge_servers_notm}}-System dargestellt:

<img src="../images/edge/edge_server_manage_hub.svg" alt="{{site.data.keyword.edge_servers_notm}}-Architektur" width="50%">

Die folgenden Diagramme enthalten die allgemeine Architektur für die typischen Bereitstellungen von {{site.data.keyword.edge_servers_notm}}-Komponenten:

* Hub-Cluster

  <img src="../images/edge/multicloud_managed_hub.svg" alt="{{site.data.keyword.edge_servers_notm}}-Hub-Cluster" width="20%">

  Der {{site.data.keyword.mcm_core_notm_novers}}-Hub-Cluster fungiert als Management-Hub. Der Hub-Cluster wird in der Regel mit allen {{site.data.keyword.icp_server}}-Komponenten konfiguriert, die zum Betrieb Ihres Unternehmens erforderlich sind. Zu diesen erforderlichen Komponenten gehören alle Komponenten, die zur Unterstützung des Betriebs erforderlich sind und die auf Ihren fernen Edge-Servern ausgeführt werden. 

* Ferner Edge-Server

  <img src="../images/edge/edge_managed_cluster.svg" alt="{{site.data.keyword.edge_servers_notm}} - Verwalteter Cluster" width="20%">

  Jeder ferne Edge-Server stellt einen von {{site.data.keyword.mcm_core_notm_novers}} verwalteten Cluster dar, der ein installiertes {{site.data.keyword.klust}} umfasst. Jeder ferne Edge-Server kann mit jedem der gehosteten {{site.data.keyword.icp_server}}-Standardservices konfiguriert werden, die für das ferne Betriebszentrum erforderlich sind und nicht bestimmten Einschränkungen durch die Edge-Server-Ressourcen unterliegen.

  Wenn Ressourcenengpässe zu Einschränkungen beim Einsatz eines Edge-Servers führen, kann die Mindestkonfiguration für {{site.data.keyword.icp_server}} mithilfe von {{site.data.keyword.edge_profile}} dennoch bereitgestellt werden. Wenn die Konfiguration mit dem {{site.data.keyword.edge_profile}} für den Edge-Server verwendet wird, dann kann eine typische Topologie wie folgt dargestellt werden:

  <img src="../images/edge/multicloud_managed_cluster.svg" alt="{{site.data.keyword.edge_profile}} - Verwaltete Clustertopologie" width="70%">

  Die Komponenten innerhalb dieser Topologie dienen primär als Proxy für Ihre Partnereinheiten im Hub-Cluster und können zum Auslagern von Arbeitslasten auf den Hub-Cluster verwendet werden. Die Edge-Server-Komponenten dienen auch zur Ausführung lokaler Datenverarbeitungsoperationen, während die Verbindungen zwischen dem fernen Edge-Server und dem Hub-Cluster vorübergehend unterbrochen sind, z. B. durch unzuverlässige Netzkonnektivität zwischen den Standorten.

## Konzepte
{: #concepts}

**Edge-Computing**: Ein Modell für die verteilte Datenverarbeitung, das Rechenleistung außerhalb der traditionellen Rechenzentren und Cloudrechenzentren nutzt. In einem Edge-Computing-Modell werden Workloads näher am Erstellungsort der zugehörigen Daten und damit näher an dem Ort platziert, an dem die Aktionen ausgeführt werden, die in Beantwortung der Analyseergebnisse für diese Daten ausgeführt werden. Durch die Platzierung von Daten und Workloads auf Einheiten am Rand (engl. Edge) des Netzes können die Latenzzeit und der Bedarf an Netzbandbreiten reduziert, die Vertraulichkeit sensibler Daten besser geschützt und der Systembetrieb auch während eines Netzausfalls aufrecht erhalten werden.

**Edge-Einheit**: Eine Komponente der Betriebseinrichtung eines Unternehmens (z. B. eine Montagemaschine in einer Fabrik, ein Geldautomat, eine intelligente Kamera oder ein Automobil), die über integrierte Rechenleistung verfügt, über die sinnvolle Arbeiten ausgeführt und Daten erfasst oder generiert werden können.

**Edge-Gateway**: Ein Edge-Server, der über Services verfügt, die Netzfunktionen wie beispielsweise die Protokollumsetzung, den Netzabschluss, die Tunnelung sowie den Firewallschutz oder die Herstellung drahtloser Verbindungen ausführen. Ein Edge-Gateway dient als Verbindungspunkt zwischen einer Edge-Einheit oder einem Edge-Server und der Cloud oder einem größeren Netz.

**Edge-Knoten**: Eine Edge-Einheit, ein Edge-Server oder ein Edge-Gateway, auf der bzw. dem das Edge-Computing ausgeführt wird.

**Edge-Server**: Ein Computer an einer fernen Betriebsstätte, auf dem Workloads für Unternehmensanwendungen und gemeinsam genutzte Services ausgeführt werden. Ein Edge-Server kann verwendet werden, um eine Verbindung zu einer Edge-Einheit oder zu einem anderen Edge-Server herzustellen oder um als Edge-Gateway für die Herstellung einer Verbindung zur Cloud oder zu einem größeren Netz zu dienen.

**Edge-Service**: Ein Service, der speziell zur Bereitstellung auf einem Edge-Server, Edge-Gateway oder einer Edge-Einheit vorgesehen ist. Edge-Services dienen zur Ausführung verschiedener Aufgaben, z. B. zur Durchführung der visuellen Erkennung, zur Gewinnung akustischer Einsichten sowie zur Spracherkennung.

**Edge-Workload**: Jeder Service, Mikroservice oder jede Softwarekomponente, die während der Ausführung sinnvolle Aufgaben auf einem Edge-Knoten ausführt.

- [Hardwarevoraussetzungen und -empfehlungen](cluster_sizing.md)
- [Gemeinsam genutzte Komponenten von {{site.data.keyword.edge_notm}} installieren](install_edge.md)
{: childlinks}
