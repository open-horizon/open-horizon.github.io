---

copyright:
years: 2020
lastupdated: "2020-05-11"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Edge-Computing im Überblick
{: #overviewofedge}

## Leistungsspektrum von {{site.data.keyword.edge_notm}}
{: #capabilities}

{{site.data.keyword.edge_notm}} (IEAM) ist branchenübergreifend ausgelegt und bietet mehrere Stufen (sog. Tiers), die mit offenen Technologien und den aktuellen Standards optimiert werden, wie beispielsweise Docker und Kubernetes. Dazu gehören IT-Plattformen, private Cloudumgebungen und Unternehmensumgebungen, Computing-Räume im Netz und lokale Gateways, Controller und Server sowie intelligente Einheiten.

<img src="../images/edge/01_IEAM_overview.svg" width="100%" alt="IEAM-Überblick">

Als zentrale Komponenten dienen extrem große öffentliche Clouds, Hybrid-Clouds, benachbarte verwaltete Rechenzentren und herkömmliche Unternehmensrechenzentren weiterhin als Aggregationspunkte für Daten, Analysen und die Back-End-Datenverarbeitung.

Öffentliche und private Netze sowie Netze zur Bereitstellung von Inhalten wandeln sich von einfachen Übertragungskomponenten in höherwertige Hosting-Umgebungen für Anwendungen in Gestalt der Edge-Netz-Cloud. Typische Anwendungsfälle für {{site.data.keyword.ieam}}:

* Hybrid-Cloud-Computing
* 5G-Netzbetrieb 
* Bereitstellung von Edge-Servern
* Kapazität für die Rechenoperationen von Edge-Servern 
* Unterstützung und Optimierung von IoT-Einheiten 

IBM Multicloud Management Core 1.2 führt Cloudplattformen der verschiedensten Hersteller in einem einheitlichen Dashboard zusammen, das den gesamten Bereich von lokal bis Edge abdeckt. {{site.data.keyword.ieam}} ist eine natürliche Erweiterung, mit der es möglich wird, die Verteilung und das Management von Workloads über das Edge-Netz hinaus auf Edge-Gateways und Edge-Einheiten auszudehnen. IBM Multicloud Management Core 1.2 erkennt darüber hinaus Workloads aus Unternehmensanwendungen mit Edge-Komponenten, privaten und hybriden Cloudumgebungen sowie der öffentlichen Cloud. Dabei stellt IBM Edge Computing Manager eine neue Ausführungsumgebung für verteilte künstliche Intelligenz (KI) bereit, um kritische Datenquellen zu erreichen.

IBM Multicloud Manager-CE bietet außerdem KI-Tools für beschleunigtes Deep Learning, optische Erkennung und Spracherkennung sowie Video- und Tonanalysen, die die Inferenzierung bei allen Auflösungen und mit den meisten Formaten von Video- und Audiodialogsystemen sowie die Erkennung ermöglichen.

## Risiken von {{site.data.keyword.edge_notm}} und deren Minimierung
{: #risks}

Obwohl {{site.data.keyword.ieam}} einzigartige Möglichkeiten schafft, birgt es auch Herausforderungen. So geht Edge-Computing beispielsweise über die physischen Begrenzungen von Cloudrechenzentren hinaus, was zu Problemen bei der Sicherheit, der Adressierbarkeit, der Verwaltung, der Eigentumsrechte und der Einhaltung von Vorschriften führen kann. Wichtiger noch: Es vervielfacht die Skalierungsproblme der cloudbasierten Managementtechniken. 

Durch Edge-Netze wird die Anzahl der Rechenknoten um eine Größenordnung erhöht. Durch Edge-Gateways wird diese Anzahl zusätzlich um eine weitere Größenordnung erhöht. Durch Edge-Geräte wird diese Anzahl um 3-4 Größenordnungen erhöht. Wenn DevOps (Continuous Delivery und Continuous Deployment) für die Verwaltung einer extrem großen Cloudinfrastruktur kritisch ist, ist ZeroOps (Operationen ohne manuelle Eingriffe) kritisch für die Verwaltung der enormen Größe, die {{site.data.keyword.ieam}} darstellt. 

Die vollautomatische Bereitstellung, Aktualisierung, Überwachung und Wiederherstellung des Edge-Computing-Raums ohne Bedienereingriff ist eine Grundbedingung. Alle diese Aktivitäten und Prozesse müssen folgende Voraussetzungen erfüllen:

* Vollständige Automatisierung
* Fähigkeit zum Treffen unabhängiger Entscheidungen zur Zuordnung von Arbeiten
* Fähigkeit zur Erkennung geänderter Bedingungen und zur Durchführung entsprechender Wiederherstellungsoperationen ohne Eingriff 

Darüber hinaus müssen diese Aktivitäten geschützt, tracefähig und rechtssicher sein. 

<!--{{site.data.keyword.edge_devices_notm}} delivers edge node management that minimizes deployment risks and manages the service software lifecycle on edge nodes fully autonomously. This function creates the capacity to achieve meaningful insights more rapidly from data that is captured closer to its source. {{site.data.keyword.edge_notm}} is available for infrastructure or servers, including distributed devices.
{:shortdesc}

Intelligent devices are being integrated into the tools that are used to conduct business at an ever-increasing rate. Device compute capacity is creating new opportunities for data analysis where data originates and actions are taken. {{site.data.keyword.edge_notm}} innovations fuel improved quality, enhance performance, and drive deeper, more meaningful user interactions. 

{{site.data.keyword.edge_notm}} can:

* Solve new business problems by using Artificial Intelligence (AI)
* Increase capacity and resiliency
* Improve security and privacy protections
* Leverage 5G networks to reduce latency

{{site.data.keyword.edge_notm}} can capture the potential of untapped data that is created by the unprecedented growth of connected devices, which opens new business opportunities, increases operational efficiency, and improves customer experiences. {{site.data.keyword.edge_notm}} brings Enterprise applications closer to where data is created and actions need to be taken, and it allows Enterprises to leverage AI and analyze data in near-real time.

## {{site.data.keyword.edge_notm}} benefits
{: #benefits}

{{site.data.keyword.edge_notm}} helps solve speed and scale challenges by using the computational capacity of edge devices, gateways, and networks. This function retains the principles of dynamic allocation of resources and continuous delivery that are inherent to cloud computing. With {{site.data.keyword.edge_notm}}, businesses have the potential to virtualize the cloud beyond data centers. Workloads that are created in the cloud can be migrated towards the edge, and where appropriate, data that is generated at the edge can be cleansed and optimized and brought back to the cloud.

{{site.data.keyword.edge_devices_notm}} spans industries and multiple tiers that are optimized with open technologies and prevailing standards like Docker and Kubernetes. This includes computing platform, both private cloud and Enterprise environments, network compute spaces and on-premises gateways, controllers and servers, and intelligent devices.

Centrally, the hyper-scale public clouds, hybrid clouds, colocated managed data centers and traditional Enterprise data centers continue to serve as aggregation points for data, analytics, and back-end data processing.

Public, private, and content-delivery networks are transforming from simple pipes to higher-value hosting environments for applications in the form of the edge network cloud.

{{site.data.keyword.edge_devices_notm}} offers: 

* Integrated offerings that provide faster insights and actions, secure and continuous operations.
* The industry's first policy-based, autonomous edge computing platform
that intelligently manages workload life cycles in a secure and flexible way.
* Open technology and ecosystems compatibility to provide robust support and innovation for industry-wide ecosystems and partners.
* Scalable solutions for wide-ranging deployment on edge devices, servers, gateways, and network elements.

## {{site.data.keyword.edge_notm}} capabilities
{: #capabilities}

* Hybrid cloud computing
* 5G networking 
* Edge server deployment
* Edge servers compute operations capacity
* IoT devices support and optimization

## {{site.data.keyword.edge_notm}} risks and resolution
{: #risks}

Although {{site.data.keyword.edge_notm}} creates unique opportunities, it also presents challenges. For example, it transcends cloud data center's physical boundaries, which can expose security, addressability, management, ownership, and compliance issues. More importantly, it multiplies the scaling issues of cloud-based management techniques.

Edge networks increase the number of compute nodes by an order of magnitude. Edge gateways increase that by another order of magnitude. Edge devices increase that number by 3 to 4 orders of magnitude. If DevOps (continuous delivery and continuous deployment) is critical to managing a hyper-scale cloud infrastructure, then zero-ops (operations with no human intervention) is critical to managing at the massive scale that {{site.data.keyword.edge_notm}} represents.

It is critical to deploy, update, monitor, and recover the edge compute space without human intervention. All of these activities and processes must be fully automated, capable of making decisions independently about work allocation, and able to recognize and recover from changing conditions without intervention. All of these activities must be secure, traceable, and defensible.

## Extending multi-cloud deployments to the edge
{: #extend_deploy}

{{site.data.keyword.mcm_core_notm}} unifies cloud platforms from multiple vendors into a consistent dashboard from on-premises to the edge. {{site.data.keyword.edge_devices_notm}} is a natural extension that enables the distribution and management of workloads beyond the edge network to edge gateways and edge devices.

{{site.data.keyword.mcm_core_notm}} recognizes workloads from Enterprise applications with edge components, private and hybrid cloud environments, and public cloud; where {{site.data.keyword.edge_notm}} provides a new execution environment for distributed AI to reach critical data sources.

{{site.data.keyword.mcm_ce_notm}} delivers AI tools for accelerated deep learning, visual and speech recognition, and video and acoustic analytics, which enables inferencing on all resolutions and most formats of video and audio conversation services and discovery.

## {{site.data.keyword.edge_devices_notm}} architecture
{: #iec4d_arch}

Other edge computing solutions typically focus on one of the following architectural strategies:

* A powerful centralized authority for enforcing edge node software compliance.
* Passing the software compliance responsibility down to the edge node owners, who are required to monitor for software updates, and manually bring their own edge nodes into compliance.

The former focuses authority centrally, creating a single point of failure, and a target that attackers can exploit to control the entire fleet of edge nodes. The latter solution can result in large percentages of the edge nodes not having the latest software updates installed. If edge nodes are not all on the latest version or have all of the available fixes, the edge nodes can be vulnerable to attackers. Both approaches also typically rely upon the central authority as a basis for the establishment of trust.

<p align="center">
<img src="../images/edge/overview_illustration.svg" width="70%" alt="Illustration of the global reach of edge computing.">
</p>

In contrast to those solution approaches, {{site.data.keyword.edge_devices_notm}} is decentralized. {{site.data.keyword.edge_devices_notm}} manages service software compliance automatically on edge nodes without any manual intervention. On each edge node, decentralized and fully autonomous agent processes run governed by the policies that are specified during the machine registration with {{site.data.keyword.edge_devices_notm}}. Decentralized and fully autonomous agbot (agreement bot) processes typically run in a central location, but can run anywhere, including on edge nodes. Like the agent processes, the agbots are governed by policies. The agents and agbots handle most of the edge service software lifecycle management for the edge nodes and enforce software compliance on the edge nodes.

For efficiency, {{site.data.keyword.edge_devices_notm}} includes two centralized services, the exchange and the switchboard. These services have no central authority over the autonomous agent and agbot processes. Instead, these services provide simple discovery and metadata sharing services (the exchange) and a private mailbox service to support peer-to-peer communications (the switchboard). These services support the fully autonomous work of the agents and agbots.

Lastly, the {{site.data.keyword.edge_devices_notm}} console helps administrators set policy and monitor the status of the edge nodes.

Each of the five {{site.data.keyword.edge_devices_notm}} component types (agents, agbots, exchange, switchboard, and console) has a constrained area of responsibility. Each component has no authority or credentials to act outside their respective area of responsibility. By dividing responsibility and scoping authority and credentials, {{site.data.keyword.edge_devices_notm}} offers risk management for edge node deployment.

WRITER NOTE: content from https://www-03preprod.ibm.com/support/knowledgecenter/SSFKVV_4.1/hub/offline_installation.html

Merge the content in this section with the above content.

## {{site.data.keyword.edge_devices_notm}}
{: #edge_devices}

{{site.data.keyword.edge_devices_notm}} provides you with a new architecture for edge node management. It is designed specifically to minimize the risks that are inherent in the deployment of either a global or local fleet of edge nodes. You can also use {{site.data.keyword.edge_devices_notm}} to manage the service software lifecycle on edge nodes fully autonomously.
{:shortdesc}

{{site.data.keyword.edge_devices_notm}} is built on the {{site.data.keyword.horizon_open}} project. For more information about the project, see [{{site.data.keyword.horizon_open}} ![Opens in a new tab](../../images/icons/launch-glyph.svg "Opens in a new tab")](https://github.com/open-horizon).-->

Weitere Informationen zur Verwendung von {{site.data.keyword.edge_notm}} und zur Entwicklung von Edge-Services finden Sie in den folgenden Abschnitten und Themengruppen:

* [Management-Hub installieren](../hub/offline_installation.md): Hier erfahren Sie, wie die {{site.data.keyword.edge_devices_notm}}-Infrastruktur installiert und konfiguriert wird und wie die Dateien zusammengestellt werden, die zum Hinzufügen von Edge-Einheiten benötigt werden.

* [Edge-Knoten installieren](../devices/installing/installing_edge_nodes.md): Hier erfahren Sie, wie die {{site.data.keyword.edge_devices_notm}}-Infrastruktur installiert und konfiguriert wird und wie die Dateien zusammengestellt werden, die zum Hinzufügen von Edge-Einheiten benötigt werden.
  
* [Edge-Services verwenden](../devices/developing/using_edge_services.md):
  Hier erhalten Sie weiterführende Informationen zur Verwendung der {{site.data.keyword.edge_notm}}-Edge-Services.

* [Edge-Services entwickeln](../devices/developing/developing_edge_services.md):
  Hier erhalten Sie weiterführende Informationen zur Verwendung der {{site.data.keyword.edge_notm}}-Edge-Services.

* [Verwaltung](../devices/administering_edge_devices/administering.md):
  Hier erhalten Sie weiterführende Informationen zur Verwaltung der {{site.data.keyword.edge_notm}}-Edge-Services. 
  
* [Sicherheit](../devices/user_management/security.md):
  Hier erhalten Sie weiterführende Informationen dazu, wie {{site.data.keyword.edge_notm}} gegen Angriffe geschützt wird und die Privatsphäre der Teilnehmer sichert.

* [Managementkonsole verwenden](../devices/getting_started/accessing_ui.md):
  Informieren Sie sich über die häufig gestellten Fragen (FAQs = Frequently Asked Questions), um sich schnell mit den wichtigsten Informationen zu {{site.data.keyword.edge_notm}} vertraut zu machen.

* [Befehlszeilenschnittstelle verwenden](../devices/getting_started/using_cli.md):
  Informieren Sie sich über die häufig gestellten Fragen (FAQs = Frequently Asked Questions), um sich schnell mit den wichtigsten Informationen zu {{site.data.keyword.edge_notm}} vertraut zu machen.

* [APIs](../devices/installing/edge_rest_apis.md):
  Informieren Sie sich über die häufig gestellten Fragen (FAQs = Frequently Asked Questions), um sich schnell mit den wichtigsten Informationen zu {{site.data.keyword.edge_notm}} vertraut zu machen.

* [Fehlerbehebung](../devices/troubleshoot/troubleshooting.md):
  Wenn bei der Einrichtung oder Nutzung von {{site.data.keyword.edge_devices_notm}} Probleme auftreten, erhalten Sie hier Informationen zu allgemeinen Problemen, die auftreten können, und Tipps zur Behebung dieser Fehler.
