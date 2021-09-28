---

copyright:
years: 2021
lastupdated: "2021-02-20"
 
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

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}), basé sur [Open Horizon](https://github.com/open-horizon), utilise plusieurs technologies de sécurité différentes pour s'assurer qu'il est protégé contre les attaques et qu'il protège la confidentialité. {{site.data.keyword.ieam}} fait appel à des processus d'agent autonome répartis géographiquement pour la gestion des logiciels de périphérie. Par conséquent, le concentrateur de gestion et les agents d'{{site.data.keyword.ieam}} représentent des cibles potentielles exposées aux violations de sécurité. Ce document explique comment {{site.data.keyword.ieam}} atténue ou élimine les menaces.
{:shortdesc}

## Concentrateur de gestion
Le concentrateur de gestion d'{{site.data.keyword.ieam}}  est déployé sur une plateforme de conteneur OpenShift. Il hérite ainsi de tous les avantages inhérents au mécanisme de sécurité. La totalité du trafic réseau du concentrateur de gestion d'{{site.data.keyword.ieam}} transite par un point d'entrée sécurisé par TLS. La communication réseau du concentrateur de gestion entre les composants du concentrateur de gestion d'{{site.data.keyword.ieam}} s'exécute sans TLS.

## Plan régulateur sécurisé
{: #dc_pane}

Le concentrateur de gestion et les agents distribués d'{{site.data.keyword.ieam}} communiquent via le plan régulateur pour déployer des charges de travail et des modèles sur des noeuds de périphérie. Contrairement aux plateformes IoT (Internet of Things) et systèmes de contrôle cloud centralisés standard, le plan de contrôle {{site.data.keyword.ieam}} est en grande partie décentralisé. Chaque acteur du système a une portée d'autorité limitée. Chacun d'entre eux ne possède donc que le niveau minimum d'autorité nécessaire à l'accomplissement de ses tâches. Aucun acteur ne peut exercer un contrôle sur l'ensemble du système. En outre, un seul acteur ne peut pas accéder à tous les noeuds de périphérie du système en compromettant un noeud de périphérie, un hôte ou un composant logiciel.

Le plan régulateur est implémenté via trois entités logicielles différentes :
* Les agents {{site.data.keyword.horizon}}
* Les agbots {{site.data.keyword.horizon}}
* Open {{site.data.keyword.horizon_exchange}}

Les agents et les agbots {{site.data.keyword.horizon}} sont les principaux acteurs du plan régulateur. {{site.data.keyword.horizon_exchange}} permet la reconnaissance et la communication sécurisée entre les agents et les agbots. Ensemble, ils offrent une protection au niveau des messages à l'aide d'un algorithme appelé Perfect Forward Secrecy.

Par défaut, les agents et agbots communiquent avec Exchange via TLS 1.3. Cependant, TLS lui-même n'assure pas une sécurité suffisante. {{site.data.keyword.ieam}} chiffre tous les messages de contrôle circulant entre les agents et les agbots avant de les envoyer via le réseau. Chaque agent et chaque agbot génère une paire de clés RSA 2048 bits et publie sa clé publique dans Exchange. La clé privée est stockée dans le stockage root protégé de chaque acteur. D'autres acteurs du système utilisent la clé publique du récepteur de message pour chiffrer une clé symétrique permettant de chiffrer les messages du plan régulateur. De cette façon, seul le récepteur désigné à l'origine peut déchiffrer la clé symétrique et par conséquent le message lui-même. L’utilisation de Perfect Forward Secrecy dans le plan régulateur offre  une sécurité supplémentaire, par exemple en évitant les attaques de  l'homme du milieu que TLS n'empêche pas.

### Agents
{: #agents}

{{site.data.keyword.horizon_open}} les agents sont plus nombreux que tous les autres acteurs dans {{site.data.keyword.ieam}}. Un agent s'exécute sur chacun des noeuds de périphérie gérés. Chaque agent est autorisé à gérer uniquement ce noeud de périphérie. Un agent compromis n'est pas autorisé à affecter d'autres noeuds de périphérie, ni aucun autre composant du système. Chaque noeud possède des données d'identification uniques qui sont stockées dans son propre espace de stockage root protégé. Dans {{site.data.keyword.horizon_exchange}}, un noeud ne peut accéder qu'à ses propres ressources. Lorsqu'un noeud est enregistré, à l'aide de la commande `hzn register`, il est possible de fournir un jeton d'authentification. Toutefois, il convient de permettre à l'agent de générer son propre jeton de sorte qu'aucune personne n'ait connaissance des données d'identification de noeud, ce qui réduit le risque de compromettre le noeud de périphérie.

L'agent est protégé des attaques réseau, car il ne comporte pas de ports d'écoute sur le réseau hôte. Toutes les communications entre l'agent et le concentrateur de gestion sont effectuées par l'agent qui interroge le concentrateur de gestion. En outre, les utilisateurs sont vivement encouragés à protéger les noeuds de périphérie à l'aide d'un pare-feu réseau qui empêche l'intrusion jusque sur l'hôte du noeud. En dépit de ces protections, si le système d'exploitation de l'agent ou le processus de l'agent lui-même est piraté ou compromis, seul ce noeud de périphérie est alors compromis. Toutes les autres parties du système {{site.data.keyword.ieam}} restent inchangées.

L'agent est responsable du téléchargement et du démarrage des charges de travail conteneurisées. Pour garantir que l'image de conteneur téléchargée et sa configuration ne sont pas compromises, l'agent vérifie la signature numérique de l'image de conteneur et la signature numérique de la configuration de déploiement. Lorsqu'un conteneur est stocké dans un registre de conteneur, le registre fournit une signature numérique pour l'image (par exemple, un hachage SHA256). Le registre de conteneur gère les clés utilisées pour créer la signature. Lorsqu'un service {{site.data.keyword.ieam}} est publié à l'aide de la commande `hzn exchange service publish`, il obtient la signature d'image et la stocke avec le service publié dans le {{site.data.keyword.horizon_exchange}}. La signature numérique de l'image est transmise à l'agent via le plan régulateur sécurisé, ce qui permet à l'agent de vérifier la signature de l'image du conteneur par rapport à l'image téléchargée. Si la signature de l'image ne correspond pas à l'image, l'agent ne démarre pas le conteneur. Le processus est similaire pour la configuration du conteneur, à une exception près. La commande `hzn exchange service publish` signe la configuration de conteneur et stocke la signature dans le {{site.data.keyword.horizon_exchange}}. Dans ce cas, l'utilisateur (qui publie le service) doit fournir la paire de clés RSA utilisée pour créer la signature. La commande `hzn key create` peut être utilisée pour générer des clés à cette fin si l'utilisateur ne dispose encore d'aucune clé. La clé publique est stockée dans l'échange avec la signature de la configuration de conteneur et transmise à l'agent via le plan de contrôle sécurisé. L'agent peut alors utiliser la clé publique pour vérifier la configuration du conteneur. Si vous préférez utiliser une paire de clés différente pour chaque configuration de conteneur, la clé privée utilisée pour signer cette configuration de conteneur peut être supprimée à ce stade, car elle n'est plus nécessaire. Pour plus d'informations sur la publication d'une charge de travail, voir [Développement de services de périphérie](../developing/developing_edge_services.md).

Lorsqu'un modèle est déployé sur un nœud de périphérie, l'agent télécharge le modèle et vérifie la signature du modèle pour s'assurer qu'il n'a pas été altéré en transit. La clé de signature et de vérification est créée lorsque le modèle est publié sur le concentrateur de gestion. L'agent stocke le modèle dans l'espace de stockage protégé racine sur l'hôte. Des donnée d'identification sont fournies à chaque service lorsqu'il est démarré par l'agent. Le service utilise ces données pour s'identifier et activer l'accès aux modèles pour lesquels il a une autorisation. Chaque objet de modèle dans {{site.data.keyword.ieam}} indique la liste des services qui peuvent accéder au modèle. Chaque service reçoit de nouvelles données d'identification chaque fois qu'il est redémarré par {{site.data.keyword.ieam}}. L'objet de modèle n'est pas chiffré par {{site.data.keyword.ieam}}. Comme l'objet de modèle est traité comme un sac de bits par {{site.data.keyword.ieam}}, une implémentation de service peut chiffrer le modèle si nécessaire. Pour plus d'informations sur l'utilisation du système de gestion des modèles MMS, voir [Détails concernant la gestion des modèles](../developing/model_management_details.md).

### Agbots
{: #agbots}

Le concentrateur de gestion {{site.data.keyword.ieam}} comprend plusieurs instances d'un agbot. Elles sont chargées de lancer le déploiement de charges de travail sur tous les noeuds de périphérie enregistrés auprès du concentrateur de gestion. Les agbots examinent régulièrement les règles de déploiement et les modèles qui ont été publiés dans Exchange, en veillant à ce que les services de ces modèles et de ces règles soient déployés sur tous les noeuds de périphérie appropriés. Lorsqu'un agbot lance une demande de déploiement, il envoie la demande via le plan régulateur sécurisé. La demande de déploiement contient tous les éléments nécessaires à l'agent pour vérifier la charge de travail et sa configuration, s'il décide d'accepter la demande. Pour plus d'informations de sécurité sur les actions de l'agent, voir  [Agents](security_privacy.md#agents). L'agbot indique également au MMS où et quand déployer des modèles. Pour plus d'informations de sécurité sur la gestion des modèles, voir [Agents](security_privacy.md#agents).

Un agbot compromis peut tenter de proposer des déploiements de charge de travail malveillants, mais le déploiement proposé doit être conforme aux exigences de sécurité définies dans la section de l'agent. Même si l'agbot lance le déploiement de la charge de travail, il n'a pas le droit de créer des configurations de charges de travail et de conteneur, et ne peut donc pas proposer ses propres charges de travail malveillantes.

## {{site.data.keyword.horizon_exchange}}
{: #exchange}

{{site.data.keyword.horizon_exchange}} est un serveur API REST centralisé et répliqué, avec équilibrage de charge. Il fonctionne comme une base de données partagée de métadonnées pour les utilisateurs, les organisations, les noeuds de périphérie, les services publiés, les règles et les modèles. Il permet également aux agents distribués et aux agbots de déployer des charges de travail conteneurisées en fournissant le stockage pour le plan régulateur sécurisé, jusqu'à ce que les messages puissent être récupérés. {{site.data.keyword.horizon_exchange}} ne peut pas lire les messages de contrôle car il ne possède pas la clé RSA privée permettant de déchiffrer le message. Un {{site.data.keyword.horizon_exchange}} compromis est par conséquent incapable d'espionner le trafic du plan régulateur. Pour plus d'informations sur le rôle d'Exchange, voir [Présentation d'{{site.data.keyword.edge}}](../getting_started/overview_ieam.md).

## Services en mode privilégié
{: #priv_services}
Sur une machine hôte, certaines tâches ne peuvent être exécutées que par un compte disposant de droits d'accès de l'utilisateur root. L'équivalent pour les conteneurs est un mode privilégié. Bien que les conteneurs n'ont généralement pas besoin de mode privilégié sur l'hôte, certains cas d'utilisation sont requis. Dans {{site.data.keyword.ieam}} , vous avez la possibilité de spécifier qu'un service d'application doit être déployé avec l'exécution de processus privilégié activée. Par défaut, elle est désactivée. Vous devez l'activer explicitement dans la [configuration de déploiement](https://open-horizon.github.io/anax/deployment_string.html) du fichier de définition de service respectif pour chaque service devant s'exécuter dans ce mode. De plus, tout nœud sur lequel vous souhaitez déployer ce service doit également autoriser explicitement les conteneurs en mode privilégié. Cela garantit que les propriétaires de nœud ont un certain contrôle sur les services en cours d'exécution sur leurs nœuds de périphérie. Pour obtenir un exemple de la manière d'activer la règle de mode privilégié sur un nœud de périphérie, voir [stratégie de nœud privilégiée](https://github.com/open-horizon/anax/blob/master/cli/samples/privileged_node_policy.json). Si la définition de service ou l'une de ses dépendances requiert un mode privilégié, la stratégie de nœud doit également autoriser le mode privilégié, sinon aucun des services ne sera déployé sur le nœud. Pour une discussion approfondie du mode privilégié, voir [Qu'est-ce que le mode privilégié et est-ce que j'en ai besoin ?](https://wiki.lfedge.org/pages/viewpage.action?pageId=44171856).

## Attaque par déni de service 
{: #denial}

Le concentrateur de gestion {{site.data.keyword.ieam}} est un service centralisé. Les services centralisés dans des environnements cloud typiques sont généralement vulnérables aux attaques par déni de service. L'agent n'a besoin d'une connexion que lorsqu'il est enregistré pour la première fois sur le concentrateur ou lorsqu'il négocie le déploiement d'une charge de travail. Dans tous les autres cas, l'agent continue à fonctionner normalement, même s'il est déconnecté du concentrateur de gestion {{site.data.keyword.ieam}}.  Cela garantit que l'agent {{site.data.keyword.ieam}} demeure actif sur le noeud de périphérie, même si le concentrateur de gestion est mis en danger.

## Système de gestion de modèle
{: #malware}

{{site.data.keyword.ieam}} n'effectue pas de recherche de logiciels malveillants ou de virus sur les données qui sont téléchargées vers le MMS. Assurez-vous que toutes les données téléchargées ont été lues avant de les télécharger vers MMS.

## Données au repos
{: #drest}

{{site.data.keyword.ieam}} ne chiffre pas les données au repos. Le chiffrement des données au repos doit être implémenté avec un utilitaire convenant au système d'exploitation hôte sur lequel le concentrateur de gestion ou l'agent {{site.data.keyword.ieam}} est en cours d'exécution.

## Normes de sécurité
{: #standards}

Les normes de sécurité suivantes sont utilisées dans {{site.data.keyword.ieam}} :
* TLS 1.2 (HTTPS) est utilisé pour le chiffrement des données en transit vers et depuis le concentrateur de gestion.
* Le chiffrement AES 256 bits est utilisé pour les données en transit, en particulier les messages transitant via le plan régulateur sécurisé.
* Les paires de clés RSA 2048 bits sont utilisées pour les données en transit, en particulier la clé symétrique AES 256 qui transite via le plan régulateur sécurisé.
* Les clés RSA fournies par un utilisateur pour signer les configurations de déploiement du conteneur lors de l'utilisation de la commande **hzn exchange service publish**.
* La paire de clés RSA générée par la commande **hzn key create** si l'utilisateur choisit d'utiliser cette commande. La taille en bits de cette clé est 4096 par défaut, mais elle peut être modifiée par l'utilisateur.

## Récapitulatif
{: #summary}

{{site.data.keyword.edge_notm}} utilise des hachages, des signatures cryptographiques et le chiffrement pour garantir la sécurité contre les accès indésirables. Etant en grande partie décentralisé, {{site.data.keyword.ieam}} évite le risque d'exposition à la plupart des attaques qui sont généralement détectées dans les environnements d'informatique en périphérie. En restreignant les droits des rôles de participants, {{site.data.keyword.ieam}} limite les dommages potentiels causés par un hôte compromis ou un composant logiciel compromis à cette partie du système. Même les attaques externes de grande envergure sur les services centralisés des services {{site.data.keyword.horizon}} qui sont utilisés dans {{site.data.keyword.ieam}} ont un impact minime sur l'exécution des charges de travail au niveau de la périphérie.
