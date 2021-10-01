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

# Découverte et négociation
{: #discovery_negotiation}

{{site.data.keyword.edge_devices_notm}}, basé sur le projet {{site.data.keyword.horizon_open}}, est essentiellement décentralisé et distribué. Les processus agent et agbot (bot d'accord) autonomes collaborent à la gestion logicielle de tous les noeuds de périphérie enregistrés.
{:shortdesc}

Pour plus d'informations sur le projet {{site.data.keyword.horizon_open}}, voir [{{site.data.keyword.horizon_open}}](https://github.com/open-horizon/).

Un processus d'agent autonome s'exécute sur chaque noeud de périphérie Horizon pour appliquer les règles qui sont définies par le propriétaire de la machine de périphérie.

En parallèle, les processus d'agbot autonome, qui sont affectés à chaque pattern de déploiement logiciel, utilisent les règles qui sont définies pour le pattern affecté pour rechercher les agents de noeud de périphérie qui sont enregistrés auprès du pattern. Indépendamment, ces agbots et agents autonomes respectent les règles du propriétaire de la machine de périphérie pour négocier les accords formels de collaboration. Chaque fois que les agbots et les agents concluent un accord, ils participent à la gestion du cycle de vie des logiciels des noeuds de périphérie correspondants.

Les agbots et les agents utilisent les services centralisés suivants pour se trouver, établir un climat de confiance et communiquer en toute sécurité sur {{site.data.keyword.edge_devices_notm}} :

* La {{site.data.keyword.horizon_switch}}, qui permet d'établir des communications privées sécurisées d'égal à égal entre les agbots et les agents.
* {{site.data.keyword.horizon_exchange}}, qui facilite la découverte.

<img src="../../images/edge/distributed.svg" width="90%" alt="Les services centralisés et décentralisés">

## {{site.data.keyword.horizon_exchange}}

{{site.data.keyword.horizon_exchange}} permet aux propriétaires de machines de périphérie d'enregistrer les noeuds de périphérie pour la gestion du cycle de vie des logiciels. Lorsque vous enregistrez un noeud de périphérie auprès d'{{site.data.keyword.horizon_exchange}} pour {{site.data.keyword.edge_devices_notm}}, vous indiquez le pattern de déploiement du noeud de périphérie. Un pattern de déploiement contient un ensemble de règles pour la gestion du noeud de périphérie, un manifeste du logiciel signé cryptographiquement et les configurations associées. Le pattern de déploiement doit être conçu, développé, testé et publié sur {{site.data.keyword.horizon_exchange}}.

Chaque noeud de périphérie doit être enregistré auprès d'{{site.data.keyword.horizon_exchange}} sous l'organisation du propriétaire de la machine de périphérie. Chaque noeud de périphérie est enregistré avec un ID et un jeton de sécurité applicables uniquement à ce noeud. Les noeuds peuvent être enregistrés pour exécuter un pattern de déploiement logiciel fourni par leur propre organisation, ou une autre organisation lorsque le pattern est accessible au public.

Lorsqu'un pattern de déploiement est publié dans {{site.data.keyword.horizon_exchange}}, un ou plusieurs agbots sont affectés à la gestion de ce pattern de déploiement et de toutes les règles associées. Ces agbots s'emploient à découvrir les noeuds de périphérie qui sont enregistrés auprès du pattern de déploiement. Lorsqu'un noeud de périphérie enregistré est détecté, les agbots négocient avec les processus d'agent local du noeud de périphérie.

Même si {{site.data.keyword.horizon_exchange}} permet aux agbots de rechercher les noeuds de périphérie qui correspondent à un pattern de déploiement enregistré, {{site.data.keyword.horizon_exchange}} n'est pas directement impliqué dans le processus de gestion logicielle du noeud de périphérie. Les agbots et les agents traitent le processus de gestion des logiciels. {{site.data.keyword.horizon_exchange}} ne dispose pas d'autorisations sur le noeud de périphérie et n'établit aucun contact avec les agents du noeud de périphérie.

## {{site.data.keyword.horizon_switch}}

Les agbots interrogent périodiquement {{site.data.keyword.horizon_exchange}} pour répertorier tous les noeuds de périphérie enregistrés pour leur pattern de déploiement. Lorsqu'un agbot découvre un noeud de périphérie qui est enregistré auprès de son pattern de déploiement, il utilise la carte de commutateur {{site.data.keyword.horizon}} pour envoyer un message privé à l'agent sur ce noeud. Ce message est en fait une demande de collaboration à la gestion du cycle de vie des logiciels sur le noeud de périphérie. Pendant ce temps, l'agent consulte sa boîte aux lettres privée sur la {{site.data.keyword.horizon_switch}} pour voir si des messages de l'agbot ont été reçus. Lorsqu'un message est reçu, l'agent le déchiffre, le valide et accepte la demande.

Outre le fait d'interroger {{site.data.keyword.horizon_exchange}}, chaque agent interroge sa boîte aux lettres privée dans la {{site.data.keyword.horizon_switch}}. Lorsque l'agbot reçoit l'acceptation de la demande de la part d'un agent, la négociation prend fin.

Les agents et les agbots partagent les clés publiques avec la {{site.data.keyword.horizon_switch}} pour leur permettre de communiquer de manière sûre et privée. Grâce à ce chiffrement, la {{site.data.keyword.horizon_switch}} sert uniquement de gestionnaire de boîte aux lettres. Tous les messages sont chiffrés par l'expéditeur avant d'être envoyés à la {{site.data.keyword.horizon_switch}}. La {{site.data.keyword.horizon_switch}} est incapable de déchiffrer les messages. Toutefois, le destinataire peut déchiffrer n'importe quel message chiffré avec sa clé publique. Il utilise également la clé publique de l'expéditeur pour chiffrer les réponses du destinataire à l'expéditeur.

**Remarque :** Toutes les communications passant par la {{site.data.keyword.horizon_switch}}, les adresses IP des noeuds de périphérie ne sont révélées à aucun agbot tant que l'agent sur chacun des noeuds de périphérie n'a pas choisi de révéler cette information. L'agent révèle l'information lorsque l'agent et l'agbot ont conclu avec succès un accord.

## Gestion du cycle de vie des logiciels

Lorsqu'un noeud de périphérie est enregistré auprès d'{{site.data.keyword.horizon_exchange}} pour un pattern de déploiement particulier, un agbot pour ce pattern de déploiement peut rechercher l'agent sur le noeud de périphérie. L'agbot associé au pattern de déploiement utilise {{site.data.keyword.horizon_exchange}} pour trouver l'agent et la {{site.data.keyword.horizon_switch}} pour négocier avec l'agent au sujet d'une collaboration à la gestion logicielle.

L'agent du noeud de périphérie reçoit la demande de collaboration de la part de l'agbot et évalue la proposition afin de vérifier que celle-ci satisfait aux règles définies par le propriétaire du noeud de périphérie. L'agent vérifie les signatures cryptographiques à l'aide des fichiers de clés installés en local. Si la proposition est conforme aux règles locales et que les signatures sont vérifiées, l'agent accepte la proposition et l'agent et l'agbot concluent l'accord. 

Une fois l'accord en place, l'agbot et l'agent collaborent à la gestion du cycle de vie des logiciels du pattern de déploiement sur le noeud de périphérie. L'agbot fournit des détails au fur et à mesure que le pattern de déploiement évolue, et surveille la conformité du noeud de périphérie. L'agent télécharge localement le logiciel sur le noeud de périphérie, vérifie la signature du logiciel et, si tout correspond, exécute et surveille le logiciel. Si nécessaire, l'agent met à jour le logiciel et l'arrête s'il y a lieu.

Pour plus d'informations sur le processus de gestion des logiciels, voir [Gestion des logiciels de périphérie](edge_software_management.md).
