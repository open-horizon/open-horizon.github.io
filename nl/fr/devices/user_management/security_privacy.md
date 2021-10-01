---

copyright:
years: 2019
lastupdated: "2019-06-24"
 
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Sécurité et confidentialité
{: #security_privacy}

{{site.data.keyword.edge_devices_notm}}, basé sur {{site.data.keyword.horizon}}, garantit une protection optimale contre les attaques et protège la confidentialité des participants. {{site.data.keyword.edge_devices_notm}} s'appuie sur des processus autonomes agent et agbot géographiquement distribués pour la gestion des logiciels de périphérie et la préservation de l'anonymat.
{:shortdesc}

Pour préserver l'anonymat, les processus agent et agbot partagent uniquement leurs clés publiques pendant tout le processus de découverte et de négociation pour {{site.data.keyword.edge_devices_notm}}. Toutes les parties prenantes d'{{site.data.keyword.edge_devices_notm}} traitent les autres parties comme une entité non approuvée par défaut. Les parties partagent les informations et collaborent uniquement lorsque la confiance est établie, que les négociations entre les parties sont terminées et qu'un accord officiel a été conclu.

## Plan régulateur distribué
{: #dc_pane}

Contrairement aux plateformes Internet des objets centralisées et aux systèmes de contrôle basés sur le cloud, le plan régulateur d'{{site.data.keyword.edge_devices_notm}} est principalement décentralisé. Chaque rôle au sein du système a un pouvoir restreint afin que chacun des rôles dispose du niveau minimum d'autorité requis pour effectuer les tâches associées. Aucune autorité unique ne peut exercer un contrôle sur l'ensemble du système. Un utilisateur ou un rôle ne peut pas accéder à tous les noeuds du système en compromettant un hôte unique ou un composant logiciel.

Le plan régulateur est implémenté via trois entités logicielles différentes :
* Agents {{site.data.keyword.horizon}}
* Agbots {{site.data.keyword.horizon}}
* {{site.data.keyword.horizon_exchange}}

Les agents et les agbots {{site.data.keyword.horizon}} sont les entités principales et agissent de manière autonome pour gérer les noeuds de périphérie. {{site.data.keyword.horizon_exchange}} facilite la découverte, la négociation et la sécurisation des communications entre les agents et les agbots.

### Agents
{: #agents}

Les agents {{site.data.keyword.horizon}} sont les premiers acteurs les plus courants dans {{site.data.keyword.edge_devices_notm}}. Un agent s'exécute sur chacun des noeuds de périphérie gérés. Chaque agent a le droit de gérer uniquement ce noeud de périphérie. L'agent indique sa clé publique dans {{site.data.keyword.horizon_exchange}}, et négocie avec les processus agbot distants au sujet de la gestion logicielle du noeud local. L'agent s'attend uniquement à recevoir des communications des agbots chargés des patterns de déploiement au sein de l'organisation de l'agent.

Un agent compromis n'a pas le pouvoir d'affecter un autre noeud de périphérie, ni aucun autre composant du système. Si le système d'exploitation hôte, ou le processus agent sur un noeud de périphérie, est piraté ou plus généralement compromis, seul ce noeud de périphérie est concerné. Les autres parties du système {{site.data.keyword.edge_devices_notm}} ne sont pas affectées.

L'agent du noeud de périphérie peut être le composant le plus puissant d'un noeud de périphérie, et il est le moins à même de compromettre la sécurité du système {{site.data.keyword.edge_devices_notm}} tout entier. L'agent est chargé de télécharger le logiciel sur un noeud de périphérie, de vérifier le logiciel, puis d'exécuter et d'associer le logiciel aux autres éléments logiciels et matériels sur le noeud de périphérie. Toutefois, dans le cadre du système de sécurité global pour {{site.data.keyword.edge_devices_notm}}, l'agent ne possède pas de pouvoir au-delà du noeud de périphérie sur lequel l'agent est en cours d'exécution.

### Agbots
{: #agbots}

Les processus agbot {{site.data.keyword.horizon}} peuvent s'exécuter n'importe où. Par défaut, ces processus s'exécutent automatiquement. Les instances d'agbot sont les deuxièmes acteurs les plus courants dans {{site.data.keyword.horizon}}. Chaque agbot est responsable uniquement des patterns de déploiement qui lui sont attribués. Les patterns de déploiement se composent principalement de règles et d'un manifeste de service logiciel. Une même instance d'agbot peut gérer plusieurs patterns de déploiement pour une organisation.

Les patterns de déploiement sont publiés par les développeurs dans le contexte d'une organisation utilisateur {{site.data.keyword.edge_devices_notm}}. Ils sont servis par les agbots aux agents {{site.data.keyword.horizon}}. Lorsqu'un noeud de périphérie est enregistré avec {{site.data.keyword.horizon_exchange}}, un pattern de déploiement destiné à l'organisation est affecté au noeud de périphérie. L'agent installé sur ce noeud de périphérie accepte uniquement les offres provenant des agbots qui présentent ce pattern de déploiement spécifique de cette organisation spécifique. L'agbot est un vecteur de distribution des patterns de déploiement, mais le pattern de déploiement lui-même doit être conforme aux règles définies sur le noeud de périphérie par son propriétaire. La signature du pattern de déploiement doit être validée, faute de quoi le pattern n'est pas accepté par l'agent.

Un agbot compromis peut tenter de proposer des accords malveillants aux noeuds de périphérie, puis de déployer un pattern de déploiement malveillant sur ceux-ci. Toutefois, les agents de noeud de périphérie acceptent uniquement les accords qui concernent des patterns de déploiement demandés par les agents via l'enregistrement et conformes aux règles définies sur le noeud de périphérie. L'agent utilise également sa clé publique pour valider la signature cryptographique du pattern avant d'accepter ce dernier.

Bien que les processus agbot orchestrent l'installation des logiciels et les mises à jour de maintenance, l'agbot n'a pas le pouvoir de forcer un noeud de périphérie ou un agent à accepter le logiciel qu'il lui propose. L'agent placé sur chaque noeud de périphérie décide des logiciels à accepter ou à refuser. Il prend cette décision en fonction des clés publiques qu'il a installées et des règles définies par le propriétaire du noeud de périphérie au moment de son enregistrement auprès de {{site.data.keyword.horizon_exchange}}.

## {{site.data.keyword.horizon_exchange}}
{: #exchange}

{{site.data.keyword.horizon_exchange}} est un service centralisé, géographiquement répliqué à charge équilibrée, qui permet aux agents et agbots distribués de se joindre et de négocier des accords. Pour plus d'informations, voir [Présentation d'{{site.data.keyword.edge}}](../../getting_started/overview_ieam.md).

{{site.data.keyword.horizon_exchange}} sert également de base de métadonnées partagée pour les utilisateurs, les organisations, les noeuds de périphérie et tous les services, règles et patterns de déploiement publiés.

Les développeurs publient les métadonnées JSON sur les implémentations de service logiciel, les règles et les patterns de déploiement qu'ils créent dans {{site.data.keyword.horizon_exchange}}. Ces informations sont hachées et signées cryptographiquement par le développeur. Les propriétaires de noeud de périphérie doivent installer des clés publiques pour le logiciel au moment de l'enregistrement du noeud de périphérie afin que l'agent local puisse utiliser les clés pour valider les signatures.

Un réseau {{site.data.keyword.horizon_exchange}} compromis peut fournir de fausses informations aux processus agent et agbot, mais l'impact serait minime du fait des mécanismes de vérification intégrés au système. {{site.data.keyword.horizon_exchange}} ne possède pas les données d'identification requises pour signer malicieusement les métadonnées. Un réseau {{site.data.keyword.horizon_exchange}} compromis ne peut pas usurper un utilisateur ou une organisation. {{site.data.keyword.horizon_exchange}} agit en tant qu'entrepôt pour les artefacts qui sont publiés par les développeurs, et par les propriétaires de noeud de périphérie, afin de pouvoir les utiliser lors de l'activation des agbots lors des processus de découverte et de négociation.

{{site.data.keyword.horizon_exchange}} joue aussi un rôle de médiateur et sécurise l'ensemble des communications entre les agents et les agbots. Il implémente un mécanisme de boîte aux lettres où les participants peuvent laisser des messages qui sont adressés à d'autres participants. Pour recevoir les messages, les participants doivent interroger la carte de commutateur Horizon pour voir si leur boîte aux lettres contient des messages.

De plus, les agents et les agbots partagent leurs clés publiques avec {{site.data.keyword.horizon_exchange}} afin d'offrir des communications sécurisées et privées. Lorsqu'un participant doit communiquer avec un autre, l'expéditeur utilise la clé publique du destinataire prévu pour identifier le destinataire. L'expéditeur utilise cette clé publique afin de chiffrer le message du destinataire. Le destinataire peut ensuite chiffrer sa réponse en utilisant la clé publique de l'expéditeur.

Cette approche permet de s'assurer que le réseau Horizon Exchange n'est pas capable d'écouter les messages de façon clandestine, car il ne possède pas les clés partagées nécessaires pour déchiffrer les messages. Seuls les destinataires prévus peuvent déchiffrer les messages. Un réseau Horizon Exchange corrompu n'a aucun moyen d'écouter les communications de participants et n'a aucun moyen d'introduire des communications malveillantes dans les conversations des participants.

## Attaque par déni de service 
{: #denial}

{{site.data.keyword.horizon}} s'appuie sur des services centralisés. Les services centralisés des systèmes type de l'internet des objets sont généralement vulnérables aux attaques par déni de service. Sous {{site.data.keyword.edge_devices_notm}}, ces services sont utilisés uniquement à des fins de découverte, de négociation et de mise à jour des tâches. Les processus autonomes agent et agbot distribués font appel aux services centralisés uniquement lorsqu'ils ont besoin d'effectuer des tâches de découverte, de négociation et de mise à jour. Dans les autres cas, lorsque des accords sont formés, le système peut continuer à fonctionner normalement même lorsque ces services centralisés sont hors ligne. Ce comportement garantit qu'{{site.data.keyword.edge_devices_notm}} reste actif en cas d'attaques sur les services centralisés.

## Cryptographie asymétrique
{: #asym_crypt}

L'essentiel de la cryptographie sous {{site.data.keyword.edge_devices_notm}} est basé sur la cryptographie à clé asymétrique. Avec cette forme de cryptographie, vous et vos développeurs devez générer une paire de clés à l'aide des commandes `hzn key` et utiliser votre clé privée pour signer cryptographiquement tous les logiciels ou services que vous voulez publier. Vous devez installer votre clé publique sur les noeuds de périphérie sur lesquels le logiciel ou le service doit être exécuté afin que la signature cryptographique de ce logiciel ou de ce service puisse être vérifiée.

Les agents et les agbots signent cryptographiquement leurs messages respectifs à l'aide de leurs clés privés, et utilisent la clé publique correspondante pour vérifier les messages qu'ils reçoivent. Les agents et les agbots chiffrent également leurs messages avec la clé publique de l'autre partie pour s'assurer que seul le destinataire prévu peut déchiffrer le message.

Si la clé privée et les données d'identification d'un agent, d'un agbot ou d'un utilisateur sont corrompues, seuls les artefacts qui sont sous le contrôle de cette entité sont exposés à un risque. 

## Récapitulatif
{: #summary}

Grâce à l'utilisation de hachages, de signatures cryptographiques et de chiffrement, {{site.data.keyword.edge_devices_notm}} sécurise la plupart des composants de la plateforme contre les accès non autorisés. Etant essentiellement décentralisé, {{site.data.keyword.edge_devices_notm}} évite de s'exposer à la plupart des attaques rencontrées dans les plateformes Internet des objets traditionnelles. En réduisant le pouvoir et l'influence des rôles des participants, {{site.data.keyword.edge_devices_notm}} maîtrise les risques éventuels causés par un hôte compromis, ou un composant logiciel compromis, sur cette partie du système. Même les attaques externes lancées à grande échelle sur les services centralisés des services {{site.data.keyword.horizon}} utilisés dans {{site.data.keyword.edge_devices_notm}} ont un impact minimal sur les participants qui font déjà partie d'un accord. Les participants qui ont déjà passé un accord continuent à fonctionner normalement malgré les interruptions.
