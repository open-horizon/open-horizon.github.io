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

# Présentation
{: #Overview}

L'informatique Edge consiste à placer les applications d'entreprise au plus près de la création des données.
{:shortdesc}

* [Avantages de l'informatique Edge](#edge_benefits)
* [Exemples](#examples)
* [Concepts](#concepts)
  
L'informatique Edge est un nouveau paradigme technologique qui permet d'élargir votre modèle d'exploitation par le biais de la virtualisation de votre cloud au-delà d'un centre de données ou d'un centre de cloud computing. L'informatique Edge déplace la charge de travail des applications d'un emplacement centralisé vers des emplacements distants, tels qu'un atelier, un entrepôt, un centre de distribution, un magasin de vente au détail, un centre de transport, et plus encore. En principe, l'informatique en périphérie permet de déplacer des charges de travail d'application partout où l'informatique est nécessaire hors de vos centres de données et de votre environnement d'hébergement cloud.

{{site.data.keyword.ieam}} offre des fonctionnalités d'informatique Edge pour vous aider à gérer et à déployer des charges de travail d'un cluster concentrateur vers des instances distantes d'{{site.data.keyword.open_shift_cp}} ou d'autres clusters Kubernetes.

{{site.data.keyword.ieam}} inclut également une prise en charge du {{site.data.keyword.edge_profile}}. Ce profil peut vous aider à réduire l'utilisation des ressources d'{{site.data.keyword.open_shift_cp}} lorsqu'il {{site.data.keyword.open_shift_cp}} est installé pour héberger un cluster de périphérie distant. Le profil installe uniquement les services minimum requis pour assurer une gestion à distance solide de ces environnements de serveurs et des applications critiques pour l'entreprise que vous y hébergez. Grâce à ce profil, vous pouvez continuer à authentifier les utilisateurs, à collecter les données d'événements et de journaux, et à déployer des charges de travail dans un noeud unique ou dans un ensemble de noeuds worker en cluster.

## Avantages de l'informatique Edge
{: #edge_benefits}

* Changement à valeur ajoutée pour votre organisation : Les charges de travail des applications sont déplacées vers des noeuds de périphérie afin de prendre en charge les opérations dans les emplacements à distance où les données sont collectées au lieu d'envoyer les données au centre de données central pour traitement.

* Moins de dépendance vis-à-vis du personnel informatique : L'utilisation d'{{site.data.keyword.ieam}} peut vous aider à réduire les dépendances en personnel informatique. Utilisez {{site.data.keyword.ieam}} pour déployer et gérer des charges de travail critiques sur des clusters de périphérie de manière sécurisée et fiable sur des centaines d'emplacements distants à partir d'un emplacement central. Cette fonctionnalité élimine la nécessité de recourir à un personnel informatique à temps plein dans chaque emplacement distant pour la gestion des charges de travail sur site.

## Exemples
{: #examples}

L'informatique Edge consiste à placer les applications d'entreprise au plus près de la création des données. Premier exemple : si vous travaillez dans une usine, l'atelier peut utiliser des capteurs pour enregistrer des points de données fournissant des informations sur la manière dont fonctionne votre usine. Les capteurs peuvent enregistrer le nombre de pièces assemblées par heure, le temps nécessaire à un élévateur pour revenir à sa position de départ ou la température de fonctionnement d'une machine de fabrication. Ces informations peuvent vous aider à déterminer si votre rendement est maximal, à identifier vos niveaux de qualité ou à anticiper les défaillances d'une machine et contacter la maintenance préventive.

Deuxième exemple : si des employés à distance travaillent dans des situations ou des conditions dangereuses, telles que des environnements chauds ou bruyants, à proximité de gaz d'échappement ou de fumées, avec des machines lourdes, vous pouvez avoir besoin de surveiller ces conditions de travail. Vous pouvez alors recueillir des informations de diverses sources qui peuvent être utilisées dans les emplacements distants. Ces données peuvent être utilisées par les responsables afin de les aider à déterminer quand ils doivent dire aux employés de faire une pause, de s'hydrater ou d'arrêter l'équipement.

Troisième exemple : vous utilisez des caméras vidéo pour surveiller certaines propriétés, telles que le trafic piétonnier vers des magasins de vente au détail, des restaurants ou des lieux d'événements, pour servir de système de sécurité et enregistrer les actes de vandalisme ou autres activités indésirables, ou pour identifier des situations d'urgence. Si vous collectez également des données à partir des vidéos, vous pouvez utiliser l'informatique Edge pour traiter les analyses vidéo en local et aider les employés à réagir au plus vite. Les employés de restaurant peuvent anticiper le nombre de plats à préparer, les gestionnaires de vente au détail peuvent déterminer s'ils doivent ouvrir plus de caisses et le personnel de sécurité peut répondre aux situations d'urgence ou alerter les secours plus rapidement.

Dans tous ces cas, l'envoi de données vers un centre de cloud computing ou un centre de données peut ralentir le traitement des données. Cette perte de temps peut avoir des conséquences néfastes lorsque vous devez faire face à des situations délicates.

Si les données enregistrées ne nécessitent pas de traitement particulier ou de traitement sous contrainte de temps, vous risquez d'engager des frais importants en termes de stockage et de réseau pour rien.

De plus, si les données collectées sont sensibles, par exemple des informations personnelles, vous risquez d'exposer ces données chaque fois que vous les déplacez.

Enfin, si l'une de vos connexions réseau n'est pas fiable, vous courez également le risque d'interrompre des opérations critiques.

## Concepts
{: #concepts}

**Dispositif de périphérie** : Appareil, par exemple, une machine d'assemblage dans un atelier, un distributeur automatique de billets, une caméra intelligente ou une automobile, qui possède une capacité de calcul intégrée à partir de laquelle effectuer des tâches utiles et collecter ou produire des données.

**Passerelle de périphérie** : Cluster de périphérie qui offre des services permettant d'exécuter des fonctions réseau, telles que la conversion de protocole, la terminaison de réseau, la tunnellisation, la protection par pare-feu ou les connexions sans fil. Une passerelle de périphérie sert de point de connexion entre un dispositif ou un cluster de périphérie et le cloud ou un réseau plus grand.

**Noeud de périphérie** : Tout dispositif, cluster ou passerelle de périphérie où s'exécute l'informatique Edge.

**Cluster de périphérie** : Ordinateur distant qui exécute les charges de travail des applications et les services partagés de l'entreprise. Un cluster de périphérie peut être utilisé pour se connecter à un dispositif de périphérie ou un autre serveur de périphérie, ou servir de passerelle de périphérie pour la connexion au cloud ou à un réseau plus vaste.

**Service de périphérie** : Service conçu spécialement pour être déployé sur un cluster, une passerelle ou un dispositif de périphérie. La reconnaissance visuelle, les données acoustiques et la reconnaissance vocale sont des exemples de services de périphérie potentiels.

**Charge de travail de périphérie** : Tout service, microservice ou logiciel qui exécute des tâches utiles sur un noeud de périphérie.

Les réseaux publics, privés et de diffusion de contenu sont en train de modifier de simples canaux de communication en environnements à plus forte valeur ajoutée pour les applications sous forme de cloud de réseau de périphérie. Les scénarios d'utilisation type d'{{site.data.keyword.ieam}} incluent :

* Déploiement de noeuds de périphérie
* Capacité des opérations de calcul des noeuds de périphérie
* Prise en charge et optimisation des noeuds de périphérie

{{site.data.keyword.ieam}} permet d'unifier les plateformes cloud de différents fournisseurs en un même tableau de bord cohérent, du site à la périphérie. {{site.data.keyword.ieam}} est une extension naturelle qui permet de distribuer et de gérer des charges de travail au-delà du réseau de périphérie sur des passerelles et des dispositifs de périphérie. {{site.data.keyword.ieam}} reconnaît également les charges de travail provenant d'applications d'entreprise avec des composants de périphérie, d'environnements cloud privés et hybride, et du cloud public. {{site.data.keyword.ieam}} offre un nouvel environnement d'exécution pour permettre à l'intelligence artificielle (IA) distribuée d'atteindre les sources de données critiques.

Enfin, {{site.data.keyword.ieam}} propose des outils d'IA pour l'apprentissage en profondeur accéléré, la reconnaissance visuelle et vocale et les analyses audio et vidéo, afin de prendre en charge toutes les résolutions, la plupart des formats audio et vidéo, les services de conversation et la reconnaissance.

## Etapes suivantes

- [Exigences relatives au dimensionnement et au système](cluster_sizing.md)
- [Installation du concentrateur de gestion](hub.md)
