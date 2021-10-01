---

copyright:
  years: 2019
lastupdated: "2019-06-28"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Présentation du fonctionnement d'{{site.data.keyword.edge_devices_notm}}
{: #overview}

{{site.data.keyword.edge_devices_notm}} a été spécialement conçu pour gérer les noeuds de périphérie afin de réduire les risques liés au déploiement, et pour gérer de façon entièrement autonome le cycle de vie des logiciels sur les noeuds de périphérie.
{:shortdesc}

## Architecture d'{{site.data.keyword.edge_devices_notm}}
{: #iec4d_arch}

D'autres solutions d'informatique Edge mettent généralement l'accent sur l'une des stratégies architecturales suivantes :

* Une puissante autorité centralisée visant à garantir la conformité logicielle des noeuds de périphérie.
* Le transfert de la responsabilité de conformité logicielle aux propriétaires de noeuds de périphérie, qui ont pour obligation de surveiller les mises à jour logicielles et mettre leurs propres noeuds de périphérie manuellement en conformité.

La première solution est axée sur une autorité centralisée, ce qui crée un point de défaillance unique et une cible susceptible d'être exploitée par les pirates pour contrôler l'ensemble des noeuds de périphérie. La seconde peut avoir comme conséquence un pourcentage élevé de noeuds de périphérie ne disposant pas de la mise à jour logicielle la plus récente. Si les noeuds de périphérie ne sont pas tous associés à la version la plus récente ou ne disposent pas tous des correctifs disponibles, les noeuds de périphérie peuvent être exposés aux pirates. Les deux approches s'appuient généralement sur l'autorité centrale comme base pour l'élaboration de la confiance.

<p align="center">
<img src="../../images/edge/overview_illustration.svg" width="70%" alt="Illustration de la portée mondiale de l'informatique Edge.">
</p>

Contrairement aux approches ci-dessus, {{site.data.keyword.edge_devices_notm}} est décentralisé. {{site.data.keyword.edge_devices_notm}} gère de façon totalement automatisée la conformité logicielle du service sur les noeuds de périphérie. Sur chacun des noeuds de périphérie, les processus agent décentralisés et entièrement autonomes sont exécutés conformément aux règles définies au moment de l'enregistrement de la machine avec {{site.data.keyword.edge_devices_notm}}. Les processus agbot (accord de bot) décentralisés et entièrement autonomes sont quant à eux généralement exécutés dans un emplacement central, mais peuvent être exécutés n'importe où, y compris sur des noeuds de périphérie. A l'instar des processus d'agent, les agbots sont régis par les règles. Les agents et les agbots assument la majeure partie de la gestion du cycle de vie des logiciels du service de périphérie pour les noeuds de périphérie et forcent l'application de la conformité logicielle aux noeuds de périphérie.

Pour plus d'efficacité, {{site.data.keyword.edge_devices_notm}} comporte deux services centralisés, le réseau Exchange et la carte de commutateur. Ces services n'ont aucune autorité centrale sur les processus agent et agbot autonomes. Au lieu de cela, ils fournissent des services simples de découverte et de partage de métadonnées (Exchange) ainsi qu'un service de boîte aux lettres visant à prendre en charge les communications d'égal à égal (la carte de commutateur). Ces services visent à soutenir le travail autonome des agents et des agbots.

Enfin, la console {{site.data.keyword.edge_devices_notm}} aide les administrateurs à définir une règle et à surveiller l'état des noeuds de périphérie.

Chacun des cinq types de composant {{site.data.keyword.edge_devices_notm}} (agent, agbot, exchange, carte de commutateur et console) est associé à un domaine de responsabilité limité. Les composants n'ont aucun pouvoir qui leur permette d'agir en dehors de leur domaine de compétence respectif. En divisant la responsabilité et en déterminant le pouvoir et les droits d'accès, {{site.data.keyword.edge_devices_notm}} offre une saine gestion des risques pour le déploiement des noeuds de périphérie.

## Découverte et négociation
{: #discovery_negotiation}

{{site.data.keyword.edge_devices_notm}}, qui s'appuie sur le projet [1{{site.data.keyword.horizon_open}} ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://github.com/open-horizon/), est principalement décentralisé et distribué. Les processus agent et agbot (bot d'accord) autonomes collaborent à la gestion logicielle de tous les noeuds de périphérie enregistrés.

Un processus d'agent autonome s'exécute sur chaque noeud de périphérie Horizon pour appliquer les règles qui sont définies par le propriétaire du dispositif de périphérie.

Les agbots autonomes surveillent les patterns de déploiement et les règles dans le réseau Exchange, et recherchent les agents de noeud de périphérie qui ne sont pas encore conformes. Les agbots proposent des accords aux noeuds de périphérie afin de les rendre conformes. Lorsqu'un agbot et un agent parviennent à un accord, ils coopèrent pour gérer le cycle de vie logiciel des services de périphérie sur le noeud de périphérie.

Les agbots et les agents utilisent les services centralisés suivants pour se trouver, établir un climat de confiance et communiquer en toute sécurité sur {{site.data.keyword.edge_devices_notm}} :

* {{site.data.keyword.horizon_exchange}}, qui facilite la découverte.
* La {{site.data.keyword.horizon_switch}}, qui permet d'établir des communications privées sécurisées d'égal à égal entre les agbots et les agents.

<img src="../../images/edge/distributed.svg" width="90%" alt="Les services centralisés et décentralisés">

### {{site.data.keyword.horizon_exchange}}
{: #iec4d_exchange}

{{site.data.keyword.horizon_exchange}} permet aux propriétaires de dispositifs de périphérie d'enregistrer les noeuds de périphérie auprès de la gestion du cycle de vie des logiciels. Lorsque vous enregistrez un noeud de périphérie auprès d'{{site.data.keyword.horizon_exchange}} pour {{site.data.keyword.edge_devices_notm}}, vous indiquez le pattern de déploiement ou la règle du noeud de périphérie. (A la base, un pattern de déploiement est simplement un ensemble de règles prédéfinies pour la gestion des noeuds de périphérie.) Les patterns et les règles doivent être conçus, développés, testés, signés et publiés dans le réseau {{site.data.keyword.horizon_exchange}}.

Chaque noeud de périphérie est enregistré avec un ID unique et un jeton de sécurité. Les noeuds peuvent être enregistrés pour exécuter un pattern ou des règles fournis par leur propre organisation, ou un pattern fourni par une autre organisation.

Lorsqu'un pattern ou une règle est publié(e) dans {{site.data.keyword.horizon_exchange}}, les agbots s'emploient à identifier les noeuds de périphérie qui sont concernés par les règles ou patterns nouveaux ou actualisés. Lorsqu'un noeud de périphérie enregistré est détecté, un agbot négocie avec l'agent du noeud de périphérie.

Même si {{site.data.keyword.horizon_exchange}} permet aux agbots de rechercher les noeuds de périphérie qui sont enregistrés pour utiliser des patterns ou des règles, {{site.data.keyword.horizon_exchange}} n'est pas directement impliqué dans le processus de gestion logicielle du noeud de périphérie. Les agbots et les agents traitent le processus de gestion des logiciels. {{site.data.keyword.horizon_exchange}} ne dispose pas d'autorisations sur le noeud de périphérie et n'établit aucun contact avec les agents du noeud de périphérie.

### {{site.data.keyword.horizon_switch}}
{: #horizon_switch}

Lorsqu'un agbot découvre un noeud de périphérie qui est concerné par des patterns ou des règles, nouveaux ou actualisés, l'agbot utilise la carte de commutateur {{site.data.keyword.horizon}} pour envoyer un message privé à l'agent sur ce noeud. Ce message est une proposition d'accord visant à collaborer à la gestion du cycle de vie des logiciels sur le noeud de périphérie. Lorsque l'agent reçoit le message de l'agbot dans sa boîte aux lettres sur la {{site.data.keyword.horizon_switch}}, il le déchiffre et étudie la proposition. Si celle-ci concerne sa propre règle de noeud, le noeud envoie un message d'acceptation à l'agbot. Dans le cas contraire, le noeud rejette la proposition. Lorsque l'agbot reçoit l'aval dans sa boîte aux lettres privées de la {{site.data.keyword.horizon_switch}}, la négociation prend fin.

Les agents et les agbots publient les clés publiques dans la {{site.data.keyword.horizon_switch}} pour permettre une communication privée et sécurisée au moyen d'une confidentialité persistante parfaite. Grâce à ce chiffrement, la {{site.data.keyword.horizon_switch}} sert uniquement de gestionnaire de boîte aux lettres. Elle est incapable de déchiffrer les messages.

Remarque : Toutes les communications passant par la {{site.data.keyword.horizon_switch}}, les adresses IP des noeuds de périphérie ne sont révélés à aucun agbot tant que l'agent sur chacun des noeuds de périphérie n'a pas choisi de révéler cette information. L'agent révèle l'information lorsque l'agent et l'agbot ont conclu avec succès un accord.

## Gestion du cycle de vie des logiciels de périphérie
{: #edge_lifecycle}

Après qu'un accord a été conclu entre l'agbot et l'agent concernant un pattern ou un ensemble de règles spécifique, ils collaborent à la gestion du cycle de vie logiciel du pattern ou de la règle sur le noeud de périphérie. L'agbot surveille l'évolution du pattern ou de la règle au fil du temps, et vérifie la conformité du noeud de périphérie. L'agent télécharge localement le logiciel sur le noeud de périphérie, vérifie la signature du logiciel, et si tout correspond, exécute et surveille le logiciel. Si nécessaire, l'agent met à jour le logiciel et l'arrête s'il y a lieu.

L'agent collecte les images de conteneur Docker du service de périphérie spécifié à partir des registres appropriés et vérifie les signatures de l'image de conteneur. L'agent démarre ensuite les conteneurs dans l'ordre de dépendance inverse avec la configuration spécifiée dans le pattern ou la règle. Lorsque les conteneurs sont exécutés, l'agent local surveille les conteneurs. Si un conteneur s'arrête de manière inattendue, l'agent relance le conteneur pour essayer de maintenir la conformité du pattern ou de la règle sur le noeud de périphérie.

L'agent a une tolérance limitée pour les défaillances. Si un conteneur tombe en panne rapidement et de façon répétée, l'agent cesse de redémarrer les services qui sont perpétuellement défaillants et annule l'accord.

### Dépendances du service {{site.data.keyword.horizon}}
{: #service_dependencies}

Un service de périphérie peut indiquer dans ses métadonnées les dépendances sur les autres services de périphérie qu'il utilise. Lorsqu'un service de périphérie est déployé sur un noeud de périphérie à la suite d'un pattern ou d'une règle, l'agent déploie également tous les services de périphérie dont il a besoin (dans l'ordre de dépendance inverse). De nombreux niveaux de dépendances de service sont pris en charge.

### Mise en réseau Docker {{site.data.keyword.horizon}}
{: #docker_networking}

{{site.data.keyword.horizon}} utilise les fonctionnalités de mise en réseau Docker pour isoler les conteneurs Docker de sorte que seuls les services qui en ont besoin puissent s'y connecter. Lorsqu'un conteneur de service qui dépend d'un autre service est démarré, il est rattaché au réseau privé du conteneur de service dépendant. Cela facilite l'exécution des services de périphérie créés par différentes organisations car chaque service de périphérie peut accéder aux autres services répertoriés uniquement dans ses métadonnées.
