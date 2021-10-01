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

# Clusters de périphérie
{: #edge_clusters}

Contenu en cours d'élaboration, issu de la page : https://www-03preprod.ibm.com/support/knowledgecenter/SSFKVV_4.1/servers/overview.html

L'informatique Edge consiste à placer les applications d'entreprise au plus près de la création des données.
{:shortdesc}

  * [Présentation](#overview)
  * [Avantages de l'informatique Edge](#edge_benefits)
  * [Exemples](#examples)
  * [Architecture](#edge_arch)
  * [Concepts](#concepts)

## Présentation
{: #overview}

L'informatique Edge est un nouveau paradigme technologique qui permet d'élargir votre modèle d'exploitation par le biais de la virtualisation de votre cloud au-delà d'un centre de données ou d'un centre de cloud computing. L'informatique Edge déplace la charge de travail des applications d'un emplacement centralisé vers des emplacements distants, tels qu'un atelier, un entrepôt, un centre de distribution, un magasin de vente au détail, un centre de transport, et plus encore. En substance, l'informatique Edge vous permet de déplacer des charges de travail d'applications là où les calculs sont requis en dehors de vos centres de données et de votre environnement d'hébergement cloud.

{{site.data.keyword.edge_servers_notm}} offre des fonctionnalités d'informatique Edge pour vous aider à gérer et à déployer des charges de travail d'un cluster concentrateur vers des instances distantes d'{{site.data.keyword.icp_server}} ou d'autres clusters Kubernetes.

{{site.data.keyword.edge_servers_notm}} utilise {{site.data.keyword.mcm_core_notm}} pour contrôler le déploiement des charges de travail conteneurisées sur des serveurs, des passerelles et des dispositifs de périphérie hébergés par des clusters {{site.data.keyword.icp_server}} dans des emplacements distants.

{{site.data.keyword.edge_servers_notm}} inclut également une prise en charge du {{site.data.keyword.edge_profile}}. Ce profil peut vous aider à réduire l'utilisation des ressources d'{{site.data.keyword.icp_server}} lorsqu'{{site.data.keyword.icp_server}} est installé pour héberger un serveur de périphérie distant. Le profil installe uniquement les services minimum requis pour assurer une gestion à distance solide de ces environnements de serveurs et des applications critiques pour l'entreprise que vous y hébergez. Grâce à ce profil, vous pouvez continuer à authentifier les utilisateurs, à collecter les données d'événements et de journaux, et à déployer des charges de travail dans un noeud unique ou dans un ensemble de noeuds worker en cluster.

## Avantages de l'informatique Edge
{: #edge_benefits}

* Changement à valeur ajoutée pour votre organisation : Les charges de travail des applications sont déplacées vers des noeuds de périphérie afin de prendre en charge les opérations dans les emplacements à distance où les données sont collectées au lieu d'envoyer les données au centre de données central pour traitement.

* Moins de dépendance vis-à-vis du personnel informatique : L'utilisation d'{{site.data.keyword.edge_servers_notm}} peut vous aider à réduire les dépendances en personnel informatique. Avec {{site.data.keyword.edge_servers_notm}}, vous pouvez déployer et gérer de manière fiable et sécurisée les charges de travail critiques sur les serveurs de périphérie vers plusieurs centaines d'emplacements distants à partir d'un emplacement central et ce, sans avoir besoin d'une équipe informatique dédiée à plein temps sur chaque emplacement pour la gestion des charges de travail sur site.

## Exemples
{: #examples}

L'informatique Edge consiste à placer les applications d'entreprise au plus près de la création des données. Premier exemple : si vous travaillez dans une usine, l'atelier peut utiliser des capteurs pour enregistrer des points de données fournissant des informations sur la manière dont fonctionne votre usine. Les capteurs peuvent enregistrer le nombre de pièces assemblées par heure, le temps nécessaire à un élévateur pour revenir à sa position de départ ou la température de fonctionnement d'une machine de fabrication. Ces informations peuvent vous aider à déterminer si votre rendement est maximal, à identifier vos niveaux de qualité ou à anticiper les défaillances d'une machine et contacter la maintenance préventive.

Deuxième exemple : si des employés à distance travaillent dans des situations ou des conditions dangereuses, telles que des environnements chauds ou bruyants, à proximité de gaz d'échappement ou de fumées, avec des machines lourdes, vous pouvez avoir besoin de surveiller ces conditions de travail. Vous pouvez alors recueillir des informations de diverses sources qui peuvent être utilisées dans les emplacements distants. Ces données peuvent être utilisées par les responsables afin de les aider à déterminer quand ils doivent dire aux employés de faire une pause, de s'hydrater ou d'arrêter l'équipement.

Troisième exemple : vous utilisez des caméras vidéo pour surveiller certaines propriétés, telles que le trafic piétonnier vers des magasins de vente au détail, des restaurants ou des lieux d'événements, pour servir de système de sécurité et enregistrer les actes de vandalisme ou autres activités indésirables, ou pour identifier des situations d'urgence. Si vous collectez également des données à partir des vidéos, vous pouvez utiliser l'informatique Edge pour traiter les analyses vidéo en local et aider les employés à réagir au plus vite. Les employés de restaurant peuvent anticiper le nombre de plats à préparer, les gestionnaires de vente au détail peuvent déterminer s'ils doivent ouvrir plus de caisses et le personnel de sécurité peut répondre aux situations d'urgence ou alerter les secours plus rapidement.

Dans tous ces cas, l'envoi de données vers un centre de cloud computing ou un centre de données peut ralentir le traitement des données. Cette perte de temps peut avoir des conséquences néfastes lorsque vous devez faire face à des situations délicates.

Si les données enregistrées ne nécessitent pas de traitement particulier ou de traitement sous contrainte de temps, vous risquez d'engager des frais importants en termes de stockage et de réseau pour rien.

De plus, si les données collectées sont sensibles, par exemple des informations personnelles, vous risquez d'exposer ces données chaque fois que vous les déplacez.

Enfin, si l'une de vos connexions réseau n'est pas fiable, vous courez également le risque d'interrompre des opérations critiques.

## Architecture
{: #edge_arch}

L'informatique Edge a pour but de mobiliser toutes les disciplines qui ont été créées pour le cloud computing hybride afin de prendre en charge les opérations distantes des fonctions d'informatique Edge. C'est pour cela qu'à été conçu {{site.data.keyword.edge_servers_notm}}.

Un déploiement type d'{{site.data.keyword.edge_servers_notm}} inclut une instance d'{{site.data.keyword.icp_server}} qui est installée sur votre centre de données de cluster concentrateur. Cette instance {{site.data.keyword.icp_server}} est utilisée pour héberger un contrôleur {{site.data.keyword.mcm_core_notm_novers}} dans le cluster concentrateur. Le cluster concentrateur représente le lieu où se déroule la gestion de tous les serveurs de périphérie à distance. {{site.data.keyword.edge_servers_notm}} utilise {{site.data.keyword.mcm_core_notm_novers}} pour gérer et déployer les charges de travail à partir du cluster concentrateur vers les serveurs de périphérie Kubernetes à distance lorsque des opérations distantes sont requises.

Ces serveurs de périphérie peuvent être installés dans des emplacements sur site distants pour que les charges de travail des applications soient au plus proche de l'emplacement où se produisent physiquement vos opérations métier sensibles, par exemple vos usines, vos entrepôts, vos points de vente, vos centres de distribution, etc. Une instance d'{{site.data.keyword.icp_server}} et d'{{site.data.keyword.mcm_core_notm_novers}} {{site.data.keyword.klust}} sont requises sur chacun des emplacements distants où vous voulez héberger un serveur de périphérie. {{site.data.keyword.mcm_core_notm_novers}} {{site.data.keyword.klust}} permet de gérer à distance les serveurs de périphérie.

Le diagramme ci-dessous illustre la topologie de haut niveau pour une configuration d'informatique Edge standard qui utilise {{site.data.keyword.icp_server}} et {{site.data.keyword.mcm_core_notm_novers}} :

<img src="../images/edge/edge_server_data_center.svg" alt="{{site.data.keyword.edge_servers_notm}} - Topologie" width="50%">

Le diagramme ci-dessous illustre l'architecture de haut niveau standard pour un système {{site.data.keyword.edge_servers_notm}} :

<img src="../images/edge/edge_server_manage_hub.svg" alt="{{site.data.keyword.edge_servers_notm}} - Architecture" width="50%">

Les diagrammes ci-dessous illustrent l'architecture de haut niveau pour le déploiement standard des composants {{site.data.keyword.edge_servers_notm}} :

* Cluster concentrateur

  <img src="../images/edge/multicloud_managed_hub.svg" alt="{{site.data.keyword.edge_servers_notm}} - Cluster concentrateur" width="20%">

  Le cluster concentrateur {{site.data.keyword.mcm_core_notm_novers}} joue le rôle d'un concentrateur de gestion. Le cluster concentrateur est généralement configuré avec tous les composants {{site.data.keyword.icp_server}} nécessaires à la gestion de votre entreprise. Parmi ces composants figurent les composants requis pour prendre en charge les opérations qui s'exécutent sur vos serveurs de périphérie distants.

* Serveur de périphérie distant

  <img src="../images/edge/edge_managed_cluster.svg" alt="{{site.data.keyword.edge_servers_notm}} - Cluster géré" width="20%">

  Chaque serveur de périphérie distant constitue un cluster géré d'{{site.data.keyword.mcm_core_notm_novers}} qui comporte un {{site.data.keyword.klust}} installé. Chaque serveur de périphérie distant peut être configuré avec n'importe lequel des services hébergés {{site.data.keyword.icp_server}} standard nécessaires au centre d'opérations distant et non limités par les ressources du serveur de périphérie.

  Si les contraintes sur les ressources constituent un frein au serveur de périphérie, la configuration minimum d'{{site.data.keyword.icp_server}} peut être obtenue à l'aide du {{site.data.keyword.edge_profile}}. Si la configuration du {{site.data.keyword.edge_profile}} est utilisée pour le serveur de périphérie, la topologie type peut ressembler à celle illustrée dans le diagramme suivant :

  <img src="../images/edge/multicloud_managed_cluster.svg" alt="{{site.data.keyword.edge_profile}} - Topologie en cluster géré" width="70%">

  Les composants de cette topologie agissent principalement en qualité de proxy vis-à-vis de leurs homologues au sein du cluster concentrateur et peuvent décharger des tâches vers le cluster concentrateur. De plus, les composants du serveur de périphérie effectuent un traitement local complet tandis que les connexions entre le serveur de périphérie distant et le cluster concentrateur sont provisoirement déconnectées, par exemple en cas de connectivité réseau non fiable entre les emplacements.

## Concepts
{: #concepts}

**Informatique Edge** : Modèle informatique qui tire profit de la capacité de calcul disponible en dehors des centres de données traditionnels et dans le cloud. Un modèle d'informatique Edge place une charge de travail au plus proche de là où les données associées sont créées et les mesures appropriées sont prises après analyse de ces données. Le fait d'installer les données et la charge de travail sur des dispositifs de périphérie diminue le temps d'attente, réduit les besoins sur la bande passante du réseau, améliore la protection des informations sensibles et autorise les opérations pendant les interruptions réseau.

**Dispositif de périphérie** : Appareil, par exemple une machine d'assemblage dans un atelier, un distributeur automatique de billets, une caméra intelligente, une automobile, qui possède une capacité de calcul intégrée à partir de laquelle effectuer des tâches utiles et collecter et produire des données.

**Passerelle de périphérie** : Serveur de périphérie qui offre des services permettant d'exécuter des fonctions réseau, telles que la conversion de protocole, la terminaison de réseau, la tunnellisation, la protection par pare-feu ou les connexions sans fil. Une passerelle de périphérie sert de point de connexion entre un dispositif ou serveur de périphérie et le cloud ou un réseau plus grand.

**Noeud de périphérie** : Tout dispositif, serveur ou passerelle de périphérie où s'exécute l'informatique Edge.

**Serveur de périphérie** : Ordinateur distant qui exécute les charges de travail des applications et les services partagés de l'entreprise. Un serveur de périphérie peut être utilisé pour se connecter à un dispositif de périphérie ou un autre serveur de périphérie, ou servir de passerelle de périphérie pour la connexion au cloud ou à un réseau plus vaste.

**Service de périphérie** : Service conçu spécialement pour être déployé sur un serveur, une passerelle ou un dispositif de périphérie. La reconnaissance visuelle, les données acoustiques et la reconnaissance vocale sont des exemples de services de périphérie potentiels.

**Charge de travail de périphérie** : Tout service, microservice ou logiciel qui exécute des tâches utiles sur un noeud de périphérie.

- [Exigences et recommandations relatives au matériel](cluster_sizing.md)
- [Installation des composants partagés {{site.data.keyword.edge_notm}}](install_edge.md)
{: childlinks}
