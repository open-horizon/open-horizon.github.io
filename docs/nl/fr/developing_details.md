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

# Informations relatives au développement
{: #developing}

La présente rubrique fournit des informations détaillées sur les pratiques et les concepts de développement logiciel relatifs à {{site.data.keyword.edge_notm}} ({{site.data.keyword.edge_abbr}}).
{:shortdesc}

## Introduction
{: #developing_intro}

{{site.data.keyword.edge_notm}} ({{site.data.keyword.edge_abbr}}) est construit sur le logiciel libre[ Open Horizon](https://www.lfedge.org/projects/openhorizon/) .

Avec {{site.data.keyword.ieam}}, vous pouvez développer n'importe quel conteneur de services pour vos machines de périphérie. Vous pouvez alors signer la configuration de conteneur et la publier. Enfin, vous pouvez déployer vos conteneurs de service à l'aide d'une stratégie ou d'un modèle de déploiement pour régir l'installation, la surveillance et la mise à jour des logiciels. Une fois ces tâches terminées, vous pouvez visualiser les {{site.data.keyword.horizon_agents}} et les {{site.data.keyword.horizon_agbots}} qui concluent des accords pour participer à la gestion du cycle de vie des logiciels. Ces composants gèrent de manière autonome les détails du cycle de vie du logiciel sur votre {{site.data.keyword.edge_nodes}}. {{site.data.keyword.ieam}} peut également utiliser des règles pour déployer de manière autonome des modèles d'apprentissage automatique. Pour plus d'informations sur le déploiement du modèle d'apprentissage automatique, voir [Système de gestion de modèle](model_management_system.md).

Le processus de développement logiciel d'{{site.data.keyword.ieam}} se concentre sur la sécurité et l'intégrité du système, tout en simplifiant les efforts nécessaires à la gestion logicielle active sur vos noeuds de périphérie. Vous pouvez générer des procédures de publication {{site.data.keyword.ieam}} dans votre intégration continue et votre pipeline de déploiement. Lorsque les agents autonomes répartis découvrent des changements publiés dans le logiciel ou une règle, tels que dans la {{site.data.keyword.edge_deploy_pattern}} ou la stratégie de déploiement, les agents autonomes agissent indépendamment pour mettre à jour le logiciel et appliquer vos règles à l'ensemble de votre flotte de machines de bord, où qu'elles soient situées.

## Services
{: #services_deploy_patterns}

{{site.data.keyword.edge_services}} sont les blocs de construction des solutions de bord. Chaque service peut contenir un ou plusieurs conteneurs Docker. Chaque conteneur Docker peut à son tour contenir un ou plusieurs processus à exécution longue. Ces processus peuvent être écrits dans presque n'importe quel langage de programmation, et utiliser n'importe quelle bibliothèque ou n'importe quel utilitaire. Toutefois, les processus doivent être développés et exécutés dans le contexte d'un conteneur Docker. Cette souplesse d'utilisation signifie qu'il n'y a quasi aucune contrainte sur le code qu'{{site.data.keyword.ieam}} peut gérer pour vous. Lorsqu'un conteneur s'exécute, il est isolé dans un bac à sable sécurisé. Ce bac à sable restreint l'accès aux périphériques matériels, à certains services du système d'exploitation, au système de fichiers hôte, aux réseaux de machines de bord de l'hôte et, surtout, aux autres services exécutés sur le nœud de périphérie. Pour plus d'informations sur les contraintes liées aux bacs à sable, voir [Bac à sable](#sandbox).

L'exemple de code `cpu2evtstreams` est constitué d'un conteneur Docker qui utilise deux autres services de périphérie. Ceux-ci se connectent via des réseaux virtuels Docker privés locaux à l'aide d'API REST HTTP. Ils se nomment `cpu` et `gps`. L'agent déploie chacun des services sur un réseau privé séparé avec chaque service ayant déclaré une dépendance sur le service. Un réseau est créé pour `cpu2evtstreams` et `cpu`, et un autre est créé pour `cpu2evtstreams` et `gps`. S'il existe un quatrième service dans ce déploiement qui partage également le service `cpu` , un autre réseau privé est créé pour simplement `cpu` et le quatrième service. Dans {{site.data.keyword.ieam}}, cette stratégie réseau limite l'accès des services uniquement à ceux qui sont répertoriés dans `requiredServices` lorsque les autres services sont publiés. Le diagramme suivant présente le déploiement de `cpu2evtstreams` lorsque le canevas s'exécute sur un nœud de périphérie :

<img src="../images/edge/07_What_is_an_edge_node.svg" style="margin: 3%" alt="Services dans un pattern">

Remarque : L'installation d'IBM Event Streams est nécessaire seulement pour certains exemples.

Les deux réseaux virtuels permettent au conteneur de service `cpu2evtstreams` d'accéder aux interfaces de programmation REST fournies par les conteneurs de services `cpu` et `gps`. Ces deux conteneurs gèrent l'accès aux services du système d'exploitation et aux unités matérielles. Bien que les API REST soient utilisées, il existe de nombreuses autres formes de communication possibles pour permettre aux services de partager et de contrôler les données.

Souvent, le pattern de codage le plus efficace pour les noeuds de périphérie implique le déploiement de plusieurs petits services déployables et configurables de façon indépendante. Par exemple, les patterns de l'internet des objets ont souvent des services de bas niveau qui ont besoin d'accéder au matériel du noeud de périphérie, tels que des détecteurs ou des régulateurs. Ces services offrent un accès partagé à ce matériel pour les autres services à utiliser.

Ce pattern est pratique lorsque le matériel nécessite un accès exclusif pour pouvoir fournir une fonction utile. Le service de bas niveau peut correctement gérer cet accès. Le rôle des conteneurs de services `cpu` et `gps` repose sur le même principe que celui du logiciel du pilote de périphérie dans le système d'exploitation de l'hôte, mais à un niveau plus élevé. Le fait de segmenter le code en plusieurs petits services indépendants, certains se spécialisant dans l'accès matériel de bas niveau, permet de séparer les problématiques. Chaque composant est libre d'évoluer et d'être mis à jour de manière autonome. Des applications tierces peuvent également être déployées en toute sécurité avec votre pile de logiciels intégrés propriétaire en leur permettant d'accéder de manière sélective à un matériel spécifique ou à d'autres services.

Par exemple, un déploiement de contrôleur industriel peut être composé d'un service de bas niveau pour surveiller des capteurs d'utilisation d'énergie et d'autres services de bas niveau. Ces derniers peuvent quant à eux être utilisés pour contrôler les régulateurs qui alimentent les unités surveillées. De plus, le déploiement peut également comporter un autre conteneur de services de niveau supérieur qui utilise les services du capteur et du mécanisme d'accès. Ce service de niveau supérieur peut utiliser les services pour alerter les opérateurs ou pour mettre automatiquement les unités hors tension en cas de relevés de consommation électrique anormaux. Ce déploiement peut également inclure un service historique qui enregistre et archive les données du capteur et du régulateur, et faire éventuellement une analyse des données. D'autres composants peuvent être utiles pour ce type de déploiement, notamment un service de localisation GPS.

Chaque conteneur de service individuel peut être versionné de manière indépendante avec cette conception. Chaque service individuel peut également être reconfiguré et inséré dans d'autres déploiement utiles, sans aucun changement de code. Si besoin, un service d'analyse tiers peut être ajouté au déploiement. Ce service tiers peut avoir accès uniquement à un ensemble spécifique d'API en lecture seule, qui limite l'interaction du service avec les régulateurs sur la plateforme.

Vous pouvez également choisir d'exécuter toutes les tâches de cet exemple de contrôleur industriel dans un même conteneur de services. Toutefois, cette solution n'est pas forcément la meilleure, sachant qu'une collection de services indépendants et interconnectés plus petits permet généralement des mises à jour logicielles plus rapides et plus flexibles. Les collections de petits services s'avèrent également plus robustes. Pour plus d'informations sur la conception d'un déploiement, voir [Pratiques de développement Edge natif](best_practices.md).

## Bac à sable
{: #sandbox}

Le bac à sable dans lequel s'exécutent les déploiements limite l'accès aux API fournies par d'autres conteneurs de services. Seuls les services qui déclarent explicitement des dépendances sur vos services sont autorisés à y accéder. Les autres processus sur l'hôte sont incapables d'accéder à ces services. De la même manière, les autres hôtes distants sont incapables d'accéder à aucun de vos services à moins que votre service ne publie explicitement un port sur l'interface réseau externe de l'hôte. Les restrictions de contrôle d'accès du bac à sable sont déterminées par l'adressabilité du réseau et non par une liste de contrôle d'accès gérée. Ceci est accompagné par la création de réseaux virtuels pour chaque service, et seuls les conteneurs de service autorisés à communiquer sont connectés au même réseau. Cela atténue la nécessité de configurer le contrôle d'accès sur chaque nœud de périphérie.

## Services utilisant d'autres services
{: #using_services}

Les services de périphérie utilisent souvent les interfaces de programmation fournies par d'autres services de périphérie pour l'acquisition de données ou l'émission de commandes de contrôle. Ces interfaces de programmation sont généralement des API REST HTTP, telles que celles mises à disposition par les services `cpu` et `gps` de bas niveau dans l'exemple `cpu2evtstreams`. Toutefois, ces interfaces peuvent être celles de votre choix, par exemple la mémoire partagée, ou le protocole TCP ou UDP, et peuvent être avec ou sans chiffrement. Compte tenu que les communications se déroulent généralement dans un seul noeud de périphérie et que les messages ne sortent pas de cet hôte, le chiffrement est souvent inutile.

Outre l'utilisation d'une API REST, vous pouvez utiliser une interface de publication et d'abonnement, telle que l'interface fournie par MQTT. Lorsqu'un service fournit des données par intermittence, il est généralement plus simple d'utiliser une interface de publication et d'abonnement que d'interroger à plusieurs reprises une API REST, d'autant plus que les API REST peuvent dépasser le délai d'attente imparti. Prenons l'exemple d'un service qui surveille un bouton matériel et qui fournit une API afin de permettre à d'autres services de détecter lorsqu'une pression bouton se produit. Si une API REST est utilisée, l'appelant ne peut pas appeler l'API et attendre qu'une réponse soit envoyée lorsque le bouton est activé. Si le bouton reste longtemps sans aucune pression, le délai d'attente de l'API REST risque d'expirer. Le fournisseur d'API devrait alors répondre immédiatement pour éviter qu'une erreur ne se produise. L'appelant doit appeler l'API fréquemment et de manière répétée pour être sûr de ne manquer aucune pression de bouton. Une bien meilleure solution consiste pour l'appelant à s'abonner à une rubrique appropriée sur un service et bloc de publication et d'abonnement. Ensuite, l'appelant peut attendre une publication, qui peut se produire dans un avenir lointain. Le fournisseur d'API peut se charger de la surveillance du bouton matériel et publier ensuite uniquement les changements d'état de cette rubrique, notamment `button pressed`, ou `button released`.

MQTT figure parmi les outils de publication et d'abonnement les plus populaires. Vous pouvez déployer un courtier MQTT en tant que service de périphérie, et exiger que vos services l'utilisent. MQTT est aussi fréquemment utilisé comme service cloud. Par exemple, la plateforme IBM Watson IoT, utilise MQTT pour communiquer avec les terminaux IoT. Pour plus d'informations, voir [IBM Watson IoT Platform](https://www.ibm.com/cloud/watson-iot-platform). Certains exemples de projet {{site.data.keyword.horizon_open}} font appel à MQTT. Pour plus d'informations, voir [{{site.data.keyword.horizon_open}} examples](https://github.com/open-horizon/examples).

Un autre outil de publication et d'abonnement relativement connu est Apache Kafka, aussi fréquemment utilisé comme service cloud. {{site.data.keyword.message_hub_notm}}, qui est utilisé par l'exemple `cpu2evtstreams` pour envoyer des données à {{site.data.keyword.cloud_notm}}, est également basé sur Kafka. Pour plus d'informations, voir [{{site.data.keyword.message_hub_notm}}](https://www.ibm.com/cloud/event-streams).

N'importe quel conteneur de service de périphérie peut fournir ou utiliser d'autres services de périphérie locaux sur le même hôte, ainsi que les services de périphérie fournis sur des hôtes voisins sur le réseau local. Les conteneurs peuvent communiquer avec des systèmes centralisés dans un centre de données d'entreprise distant ou fournisseur de cloud. En votre qualité d'auteur de service, vous déterminez avec qui et comment vos services communiquent. Lors de la communication avec les services du fournisseur de cloud, utilisez des secrets pour contenir les données d'identification d'authentification comme décrit dans [Développement de secrets](developing_secrets.md).

Vous jugerez peut-être utile de revoir l'exemple `cpu2evtstreams` afin de voir comment l'exemple de code utilise les deux autres services locaux. Notamment la manière dont l'exemple de code indique les dépendances sur les deux services locaux, déclare et utilise les variables de configuration, et communique avec Kafka. Pour plus d'informations, voir [Exemple `cpu2evtstreams`](cpu_msg_example.md).

## Services en mode privilégié
{: #priv_services}
Sur une machine hôte, certaines tâches ne peuvent être exécutées que par un compte disposant de droits d'accès de l'utilisateur root. L'équivalent pour les conteneurs est un mode privilégié. Bien que les conteneurs n'ont généralement pas besoin de mode privilégié sur l'hôte, certains cas d'utilisation sont requis. Dans {{site.data.keyword.ieam}}, vous avez la possibilité de spécifier qu'un service doit être déployé avec l'exécution de processus privilégié activée. Par défaut, elle est désactivée. Vous devez l'activer explicitement dans la [configuration de déploiement](https://open-horizon.github.io/anax/deployment_string.html) du fichier de définition de service respectif pour chaque service devant s'exécuter dans ce mode. De plus, tout nœud sur lequel vous souhaitez déployer ce service doit également autoriser explicitement les conteneurs en mode privilégié. Cela garantit que les propriétaires de nœud ont un certain contrôle sur les services en cours d'exécution sur leurs nœuds de périphérie. Pour obtenir un exemple de la manière d'activer la règle de mode privilégié sur un nœud de périphérie, voir [stratégie de nœud privilégiée](https://github.com/open-horizon/anax/blob/master/cli/samples/privileged_node_policy.json). Si la définition de service ou l'une de ses dépendances requiert un mode privilégié, la stratégie de nœud doit également autoriser le mode privilégié, sinon aucun des services ne sera déployé sur le nœud. Pour une discussion approfondie du mode privilégié, voir [Qu'est-ce que le mode privilégié et est-ce que j'en ai besoin ?](https://wiki.lfedge.org/pages/viewpage.action?pageId=44171856).


## Définition de service
{: #service_definition}

Remarque : Pour plus d'informations sur la syntaxe de commande, voir [Conventions de ce guide](../getting_started/document_conventions.md).

Dans chaque projet {{site.data.keyword.ieam}} se trouve un fichier `horizon/service.definition.json`. Ce fichier définit votre service de périphérie pour deux objectifs. L'un de ces objectifs est de vous permettre de simuler l'exécution de votre service à l'aide de l'outil `hzn dev` . Cet outil simule un environnement d'agent réel, y compris le [bac à sable réseau](#sandbox). Cette simulation se révèle particulièrement utile pour élaborer des instructions de déploiement particulières, telles que des liaisons de port ou l'accès à l'unité matérielle. Elle permet également de vérifier les communications entre les conteneurs de services sur les réseaux privés virtuels Docker que l'agent crée pour vous. L'autre raison de ce fichier est de vous permettre de publier votre service sur le {{site.data.keyword.horizon_exchange}}. Dans les exemples fournis, le fichier `horizon/service.definition.json` est soit inclus avec l'exemple de référentiel GitHub, soit généré par la commande `hzn dev service new`.

Ouvrez le fichier `horizon/service.definition.json` qui contient les métadonnées {{site.data.keyword.horizon}} de l'un des exemples d'implémentation de service, notamment [cpu2evtstreams](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/cpu2evtstreams/horizon/service.definition.json).

Chaque service publié dans {{site.data.keyword.horizon}} doit avoir un nom qui l'identifie de manière unique au sein de votre organisation. Le nom est placé dans la zone `url` et forme un identificateur global unique, lorsqu'il est combiné avec votre nom d'organisation, ainsi qu'une `version` et une `architecture`d'implémentation spécifiques. Pour une description complète de la définition de service, voir [Définition de service](https://github.com/open-horizon/anax/blob/master/docs/service_def.md). L'exemple [cpu2evtstreams](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/cpu2evtstreams/horizon/service.definition.json) exploite certaines fonctions supplémentaires d'une définition de service de base, telles que les services et les variables de service requis.

La section `requiredServices` du fichier `horizon/service.definition.json` détaille les dépendances de service que ce service utilise. L'outil `hzn dev dependency fetch` vous permet d'ajouter des dépendances à cette liste, de sorte que vous n'avez pas besoin d'éditer manuellement la liste. Une fois les dépendances ajoutées, lorsque l'agent exécute le conteneur, les autres `requiredServices` sont exécutés automatiquement (par exemple, lorsque vous utilisez `hzn dev service start` ou lorsque vous enregistrez un nœud sur lequel ce service est déployé). Pour plus d'informations sur les services requis, voir [Définition de service](https://github.com/open-horizon/anax/blob/master/docs/service_def.md) et [cpu2evtstreams](cpu_msg_example.md).

Dans la section `userInput`, vous déclarez les variables de service que votre service peut consommer pour se configurer pour un déploiement particulier. Vous déclarez ici les noms de variables, les types de données et les valeurs par défaut, et vous avez la possibilité de fournir une description en format contrôlable de visu pour chacun d'entre eux. Lorsque vous utilisez `hzn dev service start` ou lorsque vous enregistrez un nœud de périphérie sur lequel ce service est déployé, vous devez configurer ces variables de service. L'exemple [cpu2evtstreams](cpu_msg_example.md) effectue cette opération en fournissant un fichier `userinput.json` lors de l'enregistrement du nœud. Il est également possible de définir des variables de service à distance via la commande CLI `hzn exchange node update -f <userinput-settings-file>`. Pour plus d'informations sur les variables de service, voir [Définition de service](https://github.com/open-horizon/anax/blob/master/docs/service_def.md) et [cpu2evtstreams](cpu_msg_example.md).

Le fichier `horizon/service.definition.json` inclut également une section `deployment`, vers la fin du fichier. Les zones de cette section nomment chaque conteneur Docker qui implémente votre service logique. Le nom de chaque conteneur dans le tableau `services` est le nom DNS utilisé par d'autres conteneurs pour identifier le conteneur sur le réseau privé virtuel partagé. Si ce conteneur fournit une API REST devant être utilisée par les autres conteneurs, vous pouvez accéder à cette interface du conteneur de consommation à l'aide de la commande `curl http://<name>/<your-rest-api-uri>`. La zone `image` associée à chaque nom fournit une référence vers l'image du conteneur Docker correspondant, comme dans DockerHub ou certains registres de conteneurs privés. D'autres zones de la section `déploiement` peuvent être utilisées pour configurer le conteneur avec les options d'exécution utilisées par Docker pour exécuter le conteneur. Pour plus d'informations, voir la [configuration de déploiement {{site.data.keyword.horizon}}](https://github.com/open-horizon/anax/blob/master/docs/deployment_string.md).

## Etape suivante
{: #developing_what_next}

Pour plus d'informations sur le développement de code d'un noeud de périphérie, consultez la documentation suivante :

* [Pratiques de développement natif Edge](best_practices.md)

   Consultez les grands principes et les meilleures pratiques concernant le développement logiciel de services de périphérie pour {{site.data.keyword.ieam}}.

* [Utilisation d'{{site.data.keyword.cloud_registry}}](container_registry.md)

  {{site.data.keyword.ieam}} vous permet de placer vos conteneurs de services dans le registre de conteneurs sécurisés privé d'IBM plutôt que sur le Docker Hub public. Par exemple, si vous avez une image logicielle qui comporte des actifs qui n'ont pas lieu d'être dans un registre public, vous pouvez faire appel à un registre de conteneurs Docker privé, tel qu'{{site.data.keyword.cloud_registry}}.

* [API](../api/index.md)

  {{site.data.keyword.ieam}} fournit des API RESTful pour collaborer et permet aux développeurs et utilisateurs de votre organisation de contrôler ces composants.

* [Mise à jour d'un service de périphérie avec restauration de la version précédente](../using_edge_services/service_rollbacks.md)

  Consultez des détails supplémentaires sur la manière de déployer une nouvelle version d'un service de périphérie et les meilleures pratiques de développement logiciel visant à mettre à jour les paramètres de restauration dans le pattern ou les règles de déploiement.
