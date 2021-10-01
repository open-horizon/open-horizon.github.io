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

# Présentation de l'informatique Edge
{: #overviewofedge}

## Fonctionnalités d'{{site.data.keyword.edge_notm}}
{: #capabilities}

{{site.data.keyword.edge_notm}} (IEAM) couvre des secteurs d'activité et niveaux multiples qui sont optimisés à l'aide des technologies ouvertes et des normes en vigueur, telles que Docker et Kubernetes. Cela englobe les plateformes informatiques, les environnements d'entreprise et de cloud privés, les espaces de calcul réseau et les passerelles sur site, les contrôleurs et les serveurs, et les appareils intelligents.

<img src="../images/edge/01_IEAM_overview.svg" width="100%" alt="Présentation d'IEAM">

Fondamentalement, les clouds publics à grande échelle, les clouds hybrides, les centres de données gérés communs et les centres de données d'entreprise traditionnels continuent de fonctionner en tant que points d'agrégation pour les données, les analyses et le traitement des données de back end.

Les réseaux publics, privés et de diffusion de contenu sont en train de modifier de simples canaux de communication en environnements à plus forte valeur ajoutée pour les applications sous forme de cloud de réseau de périphérie. Les scénarios d'utilisation type d'{{site.data.keyword.ieam}} incluent :

* Informatique en nuage hybride
* Réseau 5G 
* Déploiement de serveur de périphérie
* Capacité des opérations de calcul des serveurs de périphérie
* Prise en charge et optimisation des terminaux IoT

IBM Multicloud Management Core 1.2 permet d'unifier les plateformes cloud de différents fournisseurs en un même tableau de bord cohérent, du site à la périphérie. {{site.data.keyword.ieam}} est une extension naturelle qui permet de distribuer et de gérer des charges de travail au-delà du réseau de périphérie sur des passerelles et des dispositifs de périphérie. De plus, IBM Multicloud Management Core 1.2 reconnaît les charges de travail provenant d'applications d'entreprise avec des composants de périphérie, d'environnements cloud privés et hybrides, et du cloud public et IBM Edge Computing Manager offre un nouvel environnement d'exécution pour permettre à l'intelligence artificielle (IA) distribuée d'atteindre les sources de données critiques.

Enfin, IBM Multicloud Manager-CE propose des outils d'IA pour l'apprentissage en profondeur accéléré, la reconnaissance visuelle et vocale et les analyses audio et vidéo, afin de prendre en charge toutes les résolutions, la plupart des formats audio et vidéo, les services de conversation et la reconnaissance.

## Risques liés à {{site.data.keyword.edge_notm}} et résolution
{: #risks}

Si {{site.data.keyword.ieam}} offre des opportunités uniques, il pose également des défis importants. Par exemple, il dépasse les frontières physiques des centres de données cloud, ce qui peut vous exposer à des risques de sécurité, d'adressabilité, de gestion, de propriété et de conformité. Plus important encore, il décuple les problèmes de mise à l'échelle des techniques de gestion du cloud.

Les réseaux de périphérie augmentent de manière significative le nombre de noeuds de traitement. Les passerelles de périphérie sont également appelées à augmenter à un rythme encore plus soutenu. Quant aux dispositifs de périphérie, ils sont multipliés par 3 ou 4 puissances de dix. Si DevOps (distribution continue et déploiement continu) est un élément capital de la gestion d'une infrastructure cloud à hypergrande échelle, zero-ops (opérations sans intervention humaine) est quant à lui essentiel pour gérer l'infrastructure à échelle encore plus massive d'{{site.data.keyword.ieam}}.

Il est indispensable de déployer, mettre à jour, surveiller et récupérer l'espace de calcul de périphérie sans aucune intervention humaine. Toutes ces activités et tous ces processus doivent être :

* entièrement automatisés ;
* capables de prendre des décisions indépendamment de l'allocation de travail ;
* capables de reconnaître et de s'adapter aux conditions changeantes sans aucune intervention. 

Toutes ces activités doivent être sécurisées, traçables et défendables.

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

Consultez les rubriques et groupes de rubriques ci-dessous pour en savoir plus sur l'utilisation d'{{site.data.keyword.edge_notm}} et le développement de services de périphérie :

* [Installation du concentrateur de gestion](../hub/offline_installation.md) : Apprenez à installer et à configurer l'infrastructure d'{{site.data.keyword.edge_devices_notm}} et à collecter les fichiers nécessaires à l'ajout de dispositifs de périphérie.

* [Installation des noeuds de périphérie](../devices/installing/installing_edge_nodes.md) : Apprenez à installer et à configurer l'infrastructure d'{{site.data.keyword.edge_devices_notm}} et à collecter les fichiers nécessaires à l'ajout de dispositifs de périphérie.
  
* [Utilisation de services de périphérie](../devices/developing/using_edge_services.md) : Apprenez à utiliser les services de périphérie d'{{site.data.keyword.edge_notm}}.

* [Développement de services de périphérie](../devices/developing/developing_edge_services.md) : Apprenez à utiliser les services de périphérie d'{{site.data.keyword.edge_notm}}.

* [Administration](../devices/administering_edge_devices/administering.md) : Apprenez à administrer les services de périphérie d'{{site.data.keyword.edge_notm}}. 
  
* [Sécurité](../devices/user_management/security.md) : Découvrez comment {{site.data.keyword.edge_notm}} garantit la sécurité contre les attaques et protège la confidentialité des participants.

* [Utilisation de la console de gestion](../devices/getting_started/accessing_ui.md) : Examinez les questions fréquemment posées pour obtenir rapidement des informations clés sur {{site.data.keyword.edge_notm}}.

* [Utilisation de l'interface de ligne de commande](../devices/getting_started/using_cli.md) : Examinez les questions fréquemment posées pour obtenir rapidement des informations clés sur {{site.data.keyword.edge_notm}}.

* [Interfaces API](../devices/installing/edge_rest_apis.md) : Examinez les questions fréquemment posées pour obtenir des informations clés sur {{site.data.keyword.edge_notm}}.

* [Traitement des incidents](../devices/troubleshoot/troubleshooting.md) : Lorsque vous rencontrez un problème lors de l'installation ou de l'utilisation d'{{site.data.keyword.edge_devices_notm}}, consultez les problèmes communs qui peuvent survenir et les conseils qui peuvent vous aider à les résoudre.
