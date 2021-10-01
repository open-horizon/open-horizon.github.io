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

# Gestion des logiciels de périphérie
{: #edge_software_mgmt}

{{site.data.keyword.edge_devices_notm}} s'appuie sur des processus autonomes géographiquement distribués pour gérer le cycle de vie logiciel de l'ensemble des noeuds de périphérie.
{:shortdesc}

Les processus autonomes qui traitent la gestion logicielle des noeuds de périphérie font appel à {{site.data.keyword.horizon_exchange}} et à la {{site.data.keyword.horizon_switch}} pour se trouver sur Internet, sans révéler leurs informations. Une fois qu'ils se sont trouvés, le processus utilise {{site.data.keyword.horizon_exchange}} et la {{site.data.keyword.horizon_switch}} pour négocier les relations, puis pour collaborer à la gestion logicielle du noeud de périphérie. Pour plus d'informations, voir [Découverte et négociation](discovery_negotiation.md).

Le logiciel {{site.data.keyword.horizon}} installé sur n'importe quel hôte peut jouer le rôle d'agent de noeud de périphérie et/ou d'agbot.

## Agbot (bot d'accord)

Des instances d'agbot sont créées de manière centralisée pour gérer chaque pattern de déploiement logiciel d'{{site.data.keyword.edge_devices_notm}} qui est publié dans {{site.data.keyword.horizon_exchange}}. Vous, ou l'un de vos développeurs, pouvez également exécuter des processus agbot sur n'importe quelle machine ayant accès à {{site.data.keyword.horizon_exchange}} et à la {{site.data.keyword.horizon_switch}}.

Lorsqu'un agbot est démarré et configuré pour gérer un pattern de déploiement logiciel spécifique, l'agbot est enregistré avec {{site.data.keyword.horizon_exchange}} et commence à interroger les noeuds de périphérie qui sont enregistrés pour exécuter le même pattern de déploiement. Lorsqu'un noeud de périphérie est détecté, l'agbot envoie à l'agent local situé sur ce noeud de périphérie une demande de collaboration à la gestion des logiciels.

Lorsqu'un accord est trouvé, l'agbot envoie les informations suivantes à l'agent :

* Les détails de règle qui sont contenus dans le pattern de déploiement.
* La liste des services et versions {{site.data.keyword.horizon}} qui sont inclus dans le pattern de déploiement.
* Toutes les dépendances qui existent entre ces services.
* La possibilité de partage des services. Un service peut être défini en tant que `exclusive`, `singleton` ou `multiple`.
* Les détails concernant chaque conteneur de chaque service. Ces détails incluent les informations suivantes : 
  * Le registre Docker où le conteneur est enregistré, tel que le registre DockerHub public ou un registre privé.
  * Les données d'identification des registres privés.
  * Les détails relatifs à l'environnement shell pour la configuration et la personnalisation.
  * Les hachages signés cryptographiquement du conteneur et de sa configuration.

L'agbot continue à surveiller les éventuelles modifications du pattern de déploiement logiciel dans {{site.data.keyword.horizon_exchange}}, par exemple la publication d'une nouvelle version des services {{site.data.keyword.horizon}} pour le pattern. Si des modifications sont détectées, l'agbot renvoie les demandes à chacun des noeuds de périphérie enregistrés pour le pattern afin de collaborer à la gestion de la transition vers la nouvelle version logicielle.

En outre, l'agbot contrôle régulièrement chacun des noeuds de périphérie enregistrés pour le pattern de déploiement pour s'assurer que toutes les règles du pattern sont appliquées. Si ce n'est pas le cas, l'agbot peut arrêter l'accord ayant été négocié. Par exemple, si le noeud de périphérie arrête d'envoyer des données ou des pulsations pendant une période prolongée, l'agbot peut annuler l'accord.  

### Agent de noeud de périphérie

Un agent de noeud de périphérie est créé lorsque le package logiciel {{site.data.keyword.horizon}} est installé sur une machine de périphérie. Pour plus d'informations sur l'installation du logiciel, voir [Installation du logiciel {{site.data.keyword.horizon}}](../installing/adding_devices.md).

Lorsque, par la suite, vous enregistrez votre noeud de périphérie auprès d'{{site.data.keyword.horizon_exchange}}, vous devez fournir les informations suivantes :

* L'adresse URL {{site.data.keyword.horizon_exchange}}.
* Le nom et le jeton d'accès du noeud de périphérie.
* Le pattern de déploiement logiciel qui est exécuté sur le noeud de périphérie. Vous devez renseigner à la fois le nom de l'organisation et celui du pattern pour pouvoir identifier le pattern.

Pour en savoir plus sur l'enregistrement, voir [Enregistrement de votre machine de périphérie](../installing/registration.md).

Une fois le noeud de périphérie enregistré, l'agent local interroge la {{site.data.keyword.horizon_switch}} afin de rechercher les demandes de collaboration des processus agbot distants. Lorsque l'agent est détecté par un agbot pour son pattern de déploiement configuré, l'agbot envoie une demande de négociation à l'agent de noeud de périphérie pour collaborer à la gestion du cycle de vie des logiciels pour le noeud de périphérie. Lorsqu'un accord est trouvé, l'agbot envoie les informations au noeud de périphérie.

L'agent extrait les conteneurs Docker spécifiés des registres appropriés. Il vérifie ensuite les hachages du conteneur et les signatures cryptographiques. L'agent démarre ensuite les conteneurs dans l'ordre de dépendance inverse avec les configurations d'environnement spécifiées. Lorsque les conteneurs sont exécutés, l'agent local surveille les conteneurs. Si un conteneur s'arrête de manière inattendue, l'agent relance le conteneur pour essayer de maintenir intact le pattern de déploiement sur le noeud de périphérie.

### Dépendances du service {{site.data.keyword.horizon}}

Bien que l'agent {{site.data.keyword.horizon}} travaille à démarrer et à gérer les conteneurs dans le pattern de déploiement affecté, les dépendances entre les services doivent être gérées dans le code du conteneur de service. Même si les conteneurs sont démarrés dans l'ordre de dépendance inverse, {{site.data.keyword.horizon}} n'est pas en mesure de s'assurer que les fournisseurs de service sont entièrement démarrés et prêts à fournir le service avant que les consommateurs de service ne soient démarrés. Les consommateurs doivent gérer de façon stratégique le démarrage potentiellement lent des services dont ils dépendent. Compte tenu du risque de défaillance, voire de désactivation, du service qui fournit les conteneurs, les consommateurs de service doivent également gérer l'absence des services qu'ils utilisent. 

L'agent local détecte lorsqu'un service tombe en panne, et démarre le service avec le même nom de réseau, sur le réseau privé Docker. Un léger temps d'indisponibilité survient au cours du processus de relance. Le service consommateur doit aussi traiter ce léger temps d'arrêt, faute de quoi il risque également de ne pas pouvoir continuer.

L'agent a une tolérance limitée pour les défaillances. Si un conteneur tombe en panne rapidement et de façon répétée, l'agent peut renoncer à redémarrer les services qui sont perpétuellement défaillants, et peut annuler l'accord.

### Mise en réseau Docker {{site.data.keyword.horizon}}

{{site.data.keyword.horizon}} utilise les fonctionnalités de mise en réseau Docker pour isoler les conteneurs Docker qui fournissent des services. Cet isolement garantit que seuls les consommateurs autorisés ont accès aux conteneurs. Chacun des conteneurs est démarré dans l'ordre de dépendance inverse, à savoir les producteurs en premier et les consommateurs en dernier, sur un réseau virtuel Docker privé. Chaque fois qu'un conteneur de service consommateur est démarré, le conteneur est lié au réseau privé pour son conteneur producteur. Les conteneurs producteurs ne sont accessibles que par les consommateurs dont les dépendances sur le producteur sont connues par {{site.data.keyword.horizon}}. Compte tenu de la façon dont les réseaux Docker sont implémentés, tous les conteneurs sont accessibles à partir des interpréteurs de commandes de l'hôte. 

Si vous avez besoin d'obtenir l'adresse IP d'un conteneur, utilisez la commande `docker inspect <containerID>` pour récupérer la valeur `IPAddress` affectée. Vous pouvez atteindre n'importe quel conteneur à partir des interpréteurs de commandes de votre hôte.

## Sécurité et confidentialité

Bien que les agents du noeud de périphérie et les agbots du pattern de déploiement puissent se découvrir mutuellement, les composants respectent la confidentialité tant qu'un accord de collaboration n'a pas été officiellement conclu. Les identités de l'agent et de l'agbot ainsi que toutes les communications sont chiffrées. Les collaborations autour de la gestion logicielle sont également chiffrées. Tous les logiciels gérés sont signés cryptographiquement. Pour en savoir plus sur les aspects de confidentialité et de sécurité d'{{site.data.keyword.edge_devices_notm}}, voir [Sécurité et confidentialité](../user_management/security_privacy.md).
