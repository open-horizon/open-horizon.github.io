---

copyright:
years: 2019
lastupdated: "2019-07-05"

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

La présente rubrique fournit des informations détaillées sur les pratiques et les concepts de développement logiciel relatifs à {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}).
{:shortdesc}

## Introduction
{: #developing_intro}

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) est construit sur le logiciel open source [Open Horizon - EdgeX Project Group](https://wiki.edgexfoundry.org/display/FA/Open+Horizon+-+EdgeX+Project+Group).

Avec {{site.data.keyword.ieam}}, vous pouvez développer n'importe quel conteneur de services pour vos machines de périphérie. Vous pouvez ensuite les signer de manière cryptographique et publier votre code. Enfin, vous pouvez définir des règles au sein d'un {{site.data.keyword.edge_deploy_pattern}} pour gérer l'installation, la surveillance et la mise à jour des logiciels. Une fois ces tâches terminées, vous pouvez visualiser les {{site.data.keyword.horizon_agents}} et les {{site.data.keyword.horizon_agbots}} qui concluent des accords pour participer à la gestion du cycle de vie des logiciels. Ces composants gèrent ensuite les détails du cycle de vie sur vos {{site.data.keyword.edge_nodes}} de manière totalement autonome en fonction du pattern de déploiement enregistré auprès de chaque noeud de périphérie. {{site.data.keyword.ieam}} peut également utiliser des règles pour déterminer où et quand déployer de manière autonome des services et des modèles d'apprentissage automatique. Les règles peuvent être utilisées comme solution de rechange aux patterns de déploiement.

Le processus de développement logiciel d'{{site.data.keyword.ieam}} se concentre sur la sécurité et l'intégrité du système, tout en simplifiant les efforts nécessaires à la gestion logicielle active sur vos noeuds de périphérie. {{site.data.keyword.ieam}} peut également utiliser des règles pour déterminer où et quand déployer de manière autonome des services et des modèles d'apprentissage automatique. Les règles peuvent être utilisées comme solution de rechange aux patterns de déploiement. Vous pouvez générer des procédures de publication {{site.data.keyword.ieam}} dans votre intégration continue et votre pipeline de déploiement. Lorsque les agents autonomes distribués détectent des modifications apportées au logiciel ou à une règle, par exemple dans le {{site.data.keyword.edge_deploy_pattern}} ou la règle de déploiement, ils agissent de façon indépendante pour mettre à jour le logiciel ou appliquer les règles à l'ensemble des machines de périphérie, où qu'elles se trouvent.

## Services et patterns de déploiement
{: #services_deploy_patterns}

Les {{site.data.keyword.edge_services}} représentent les blocs de développement des patterns de déploiement. Chaque service peut contenir un ou plusieurs conteneurs Docker. Chaque conteneur Docker peut à son tour contenir un ou plusieurs processus à exécution longue. Ces processus peuvent être écrits dans presque n'importe quel langage de programmation, et utiliser n'importe quelle bibliothèque ou n'importe quel utilitaire. Toutefois, les processus doivent être développés et exécutés dans le contexte d'un conteneur Docker. Cette souplesse d'utilisation signifie qu'il n'y a quasi aucune contrainte sur le code qu'{{site.data.keyword.ieam}} peut gérer pour vous. Lorsqu'un conteneur s'exécute, il est isolé dans un bac à sable sécurisé. Ce bac à sable limite l'accès aux unités matérielles, à certains services du système d'exploitation, au système de fichier hôte, ainsi qu'aux réseaux de machines de périphérie hôte. Pour plus d'informations sur les contraintes liées aux bacs à sable, voir [Bac à sable](#sandbox).

L'exemple de code `cpu2evtstreams` consiste en un conteneur Docker qui utilise deux autres services de périphérie locaux. Ceux-ci se connectent via des réseaux virtuels Docker privés locaux à l'aide d'API REST HTTP. Ils se nomment `cpu` et `gps`. L'agent déploie chacun des services sur un réseau privé séparé avec chaque service ayant déclaré une dépendance sur le service. Un réseau est créé pour `cpu2evtstreams` et `cpu`, et un autre est créé pour `cpu2evtstreams` et `gps`. Si un quatrième service partageant également le service `cpu` existe dans le pattern de déploiement, un autre réseau privé est créé spécifiquement pour `cpu` et le quatrième service. Dans {{site.data.keyword.ieam}}, cette stratégie réseau limite l'accès des services uniquement à ceux qui sont répertoriés dans `requiredServices` lorsque les autres services sont publiés. Le diagramme suivant illustre le pattern de déploiement `cpu2evtstreams` lorsque le pattern s'exécute sur un noeud de périphérie :

<img src="../images/edge/07_What_is_an_edge_node.svg" style="margin: 3%" alt="Services dans un pattern">

**Remarque** : l'installation d'IBM Event Streams est nécessaire seulement pour certains exemples.

Les deux réseaux virtuels permettent au conteneur de service `cpu2evtstreams` d'accéder aux interfaces de programmation REST fournies par les conteneurs de services `cpu` et `gps`. Ces deux conteneurs gèrent l'accès aux services du système d'exploitation et aux unités matérielles. Bien que les API REST soient utilisées, il existe de nombreuses autres formes de communication possibles pour permettre aux services de partager et de contrôler les données.

Souvent, le pattern de codage le plus efficace pour les noeuds de périphérie implique le déploiement de plusieurs petits services déployables et configurables de façon indépendante. Par exemple, les patterns de l'internet des objets ont souvent des services de bas niveau qui ont besoin d'accéder au matériel du noeud de périphérie, tels que des détecteurs ou des régulateurs. Ces services offrent un accès partagé à ce matériel pour les autres services à utiliser.

Ce pattern est pratique lorsque le matériel nécessite un accès exclusif pour pouvoir fournir une fonction utile. Le service de bas niveau peut correctement gérer cet accès. Le rôle des conteneurs de services `cpu` et `gps` repose sur le même principe que celui du logiciel du pilote de périphérie dans le système d'exploitation de l'hôte, mais à un niveau plus élevé. Le fait de segmenter le code en plusieurs petits services indépendants, certains se spécialisant dans l'accès matériel de bas niveau, permet de séparer les problématiques. Chaque composant est libre d'évoluer et d'être mis à jour de manière autonome. Des applications tierces peuvent également être déployées en toute sécurité avec votre pile de logiciels intégrés propriétaire en leur permettant d'accéder de manière sélective à un matériel spécifique ou à d'autres services.

Par exemple, un pattern de déploiement de contrôleur industriel peut être composé d'un service de bas niveau pour surveiller des capteurs d'utilisation d'énergie et d'autres services de bas niveau. Ces derniers peuvent quant à eux être utilisés pour contrôler les régulateurs qui alimentent les unités surveillées. De plus, le pattern de déploiement peut comporter un autre conteneur de services de niveau supérieur qui utilise les services du capteur et du régulateur. Ce service de niveau supérieur peut utiliser les services pour alerter les opérateurs ou pour mettre automatiquement les unités hors tension en cas de relevés de consommation électrique anormaux. Ce pattern de déploiement peut également inclure un service historique qui enregistre et archive les données du capteur et du régulateur, et faire éventuellement une analyse des données. D'autres composants peuvent être utiles pour ce type de pattern de déploiement, notamment un service de localisation GPS.

Chaque conteneur de service individuel peut être mis à jour de manière indépendante avec cette conception. Chaque service individuel peut également être reconfiguré et inséré dans d'autres patterns de déploiement utiles, sans aucun changement de code. Si besoin, un service d'analyse tiers peut être ajouté au pattern. Ce service tiers peut avoir accès uniquement à un ensemble spécifique d'API en lecture seule, qui limite l'interaction du service avec les régulateurs sur la plateforme.

Vous pouvez également choisir d'exécuter toutes les tâches de cet exemple de contrôleur industriel dans un même conteneur de services. Toutefois, cette solution n'est pas forcément la meilleure, sachant qu'une collection de services indépendants et interconnectés plus petits permet généralement des mises à jour logicielles plus rapides et plus flexibles. Les collections de petits services s'avèrent également plus robustes. Pour en savoir plus sur la conception de vos patterns de déploiement, voir [Pratiques de développement natif Edge](best_practices.md).

## Bac à sable
{: #sandbox}

Le bac à sable dans lequel les services sont exécutés limite l'accès aux API fournies par vos conteneurs de services. Pour ce faire, chaque service est déployé dans un ou plusieurs réseaux privés virtuels. Seuls les services qui déclarent explicitement des dépendances sur vos services sont autorisés à y accéder. Consultez [Définition de service](#service_definition) pour savoir comment configurer le nom DNS de votre conteneur sur son réseau privé virtuel. Les autres processus sur l'hôte n'ont normalement pas accès à ces services. De la même manière, les autres hôtes distants n'ont normalement pas accès à aucun de ces services à moins que le service ne publie explicitement un port sur l'interface réseau externe de l'hôte.

## Services utilisant d'autres services
{: #using_services}

Les services de périphérie utilisent souvent les interfaces de programmation fournies par d'autres services de périphérie pour l'acquisition de données ou l'émission de commandes de contrôle. Ces interfaces de programmation sont généralement des API REST HTTP, telles que celles mises à disposition par les services `cpu` et `gps` de bas niveau dans l'exemple `cpu2evtstreams`. Toutefois, ces interfaces peuvent être celles de votre choix, par exemple la mémoire partagée, ou le protocole TCP ou UDP, et peuvent être avec ou sans chiffrement. Compte tenu que les communications se déroulent généralement dans un seul noeud de périphérie et que les messages ne sortent pas de cet hôte, le chiffrement est souvent inutile.

Outre l'utilisation d'une API REST, vous pouvez utiliser une interface de publication et d'abonnement, telle que l'interface fournie par MQTT. Lorsqu'un service fournit des données par intermittence, il est généralement plus simple d'utiliser une interface de publication et d'abonnement que d'interroger à plusieurs reprises une API REST, d'autant plus que les API REST peuvent dépasser le délai d'attente imparti. Prenons l'exemple d'un service qui surveille un bouton matériel et qui fournit une API afin de permettre à d'autres services de détecter lorsqu'une pression bouton se produit. Si une API REST est utilisée, l'appelant ne peut pas appeler l'API et attendre qu'une réponse soit envoyée lorsque le bouton est activé. Si le bouton reste longtemps sans aucune pression, le délai d'attente de l'API REST risque d'expirer. Le fournisseur d'API devrait alors répondre immédiatement pour éviter qu'une erreur ne se produise. L'appelant doit appeler l'API fréquemment et de manière répétée pour être sûr de ne manquer aucune pression de bouton. Une bien meilleure solution consiste pour l'appelant à s'abonner à une rubrique appropriée sur un service et bloc de publication et d'abonnement. Ensuite, l'appelant peut attendre une publication, qui peut se produire dans un avenir lointain. Le fournisseur d'API peut se charger de la surveillance du bouton matériel et publier ensuite uniquement les changements d'état de cette rubrique, notamment `button pressed`, ou `button released`.

MQTT figure parmi les outils de publication et d'abonnement les plus populaires. Vous pouvez déployer un courtier MQTT en tant que service de périphérie, et exiger que vos services l'utilisent. MQTT est aussi fréquemment utilisé comme service cloud. Par exemple, la plateforme IBM Watson IoT, utilise MQTT pour communiquer avec les terminaux IoT. Pour plus d'informations, voir [IBM Watson IoT Platform](https://www.ibm.com/cloud/watson-iot-platform). Certains exemples de projet {{site.data.keyword.horizon_open}} font appel à MQTT. Pour plus d'informations, voir [{{site.data.keyword.horizon_open}} examples](https://github.com/open-horizon/examples).

Un autre outil de publication et d'abonnement relativement connu est Apache Kafka, aussi fréquemment utilisé comme service cloud. {{site.data.keyword.message_hub_notm}}, qui est utilisé par l'exemple `cpu2evtstreams` pour envoyer des données à {{site.data.keyword.cloud_notm}}, est également basé sur Kafka. Pour plus d'informations, voir [{{site.data.keyword.message_hub_notm}}](https://www.ibm.com/cloud/event-streams).

N'importe quel conteneur de service de périphérie peut fournir ou utiliser d'autres services de périphérie locaux sur le même hôte, ainsi que les services de périphérie fournis sur des hôtes voisins sur le réseau local. Les conteneurs peuvent communiquer avec des systèmes centralisés dans un centre de données d'entreprise distant ou fournisseur de cloud. En votre qualité d'auteur de service, vous déterminez avec qui et comment vos services communiquent.

Vous jugerez peut-être utile de revoir l'exemple `cpu2evtstreams` afin de voir comment l'exemple de code utilise les deux autres services locaux. Notamment la manière dont l'exemple de code indique les dépendances sur les deux services locaux, déclare et utilise les variables de configuration, et communique avec Kafka. Pour plus d'informations, voir [Exemple `cpu2evtstreams`](cpu_msg_example.md).

## Définition de service
{: #service_definition}

**Remarque** : consultez [Conventions utilisées dans ce document](../getting_started/document_conventions.md) pour plus d'informations sur la syntaxe de commande.

Dans chaque projet {{site.data.keyword.ieam}} se trouve un fichier `horizon/service.definition.json`. Ce fichier définit le service de périphérie pour deux raisons. La première est de vous aider à simuler l'exécution de votre service par l'outil `hzn dev`, comme dans l'{{site.data.keyword.horizon_agent}}. Cette simulation se révèle particulièrement utile pour élaborer des instructions de déploiement particulières, telles que des liaisons de port ou l'accès à l'unité matérielle. Elle permet également de vérifier les communications entre les conteneurs de services sur les réseaux privés virtuels Docker que l'agent crée pour vous. La seconde est de vous aider à publier votre service dans {{site.data.keyword.horizon_exchange}}. Dans les exemples fournis, le fichier `horizon/service.definition.json` est soit inclus avec l'exemple de référentiel GitHub, soit généré par la commande `hzn dev service new`.

Ouvrez le fichier `horizon/service.definition.json` qui contient les métadonnées {{site.data.keyword.horizon}} de l'un des exemples d'implémentation de service, notamment [cpu2evtstreams](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/cpu2evtstreams/horizon/service.definition.json).

Chaque service publié dans {{site.data.keyword.horizon}} doit posséder un paramètre `url` qui l'identifie de manière unique dans votre organisation. Cette zone n'est pas une URL. En fait, la zone `url` forme un identificateur unique global, lorsqu'il est combiné au nom de votre organisation et une implémentation spécifique des zones `version` et `arch`. Vous pouvez éditer le fichier `horizon/service.definition.json` pour fournir des valeurs appropriées pour `url` et `version`. Pour la valeur `version`, utilisez une valeur de style de gestion des versions. Utilisez ces nouvelles valeurs lorsque vous exécutez la commande push, que vous signez et que vous publiez vos conteneurs de services. Une autre solution consiste à modifier le fichier `horizon/hzn.json` pour que les outils remplacent les valeurs de variables qui s'y trouvent, au lieu des références de variable utilisées dans le fichier `horizon/service.definition.json`.

La section `requiredServices` du fichier `horizon/service.definition.json` détaille toutes les dépendances de service, telles que les autres services de périphérie utilisés par ce conteneur. L'outil `hzn dev dependency fetch` permet d'ajouter des dépendances à cette liste, afin que vous n'ayez plus besoin d'éditer la liste manuellement. Lorsque les dépendances ont été ajoutées, lorsque l'agent exécute le conteneur, ces autres services `requiredServices` sont exécutés automatiquement chaque fois (lorsque, par exemple, vous utilisez `hzn dev service start` ou que vous enregistrez un noeud auprès d'un pattern de déploiement qui contient ce service). Pour plus d'informations sur les services requis, voir [cpu2evtstreams](cpu_msg_example.md).

Dans la section `userInput`, vous affectez les variables de configuration que votre service peut utiliser pour se configurer pour un déploiement particulier. Vous indiquez ici les noms de variables, les types de données et les valeurs par défaut, et vous avez la possibilité de fournir une description en format contrôlable de visu pour chacun d'entre eux. Lorsque vous utilisez la commande `hzn dev service start` ou que vous enregistrez un noeud de périphérie avec un pattern de déploiement qui contient ce service, vous devez spécifier un fichier `userinput.json` pour définir les valeurs des variables dépourvues de valeur par défaut. Pour plus d'informations sur les variables de configuration `userInput` et les fichiers `userinput.json`, voir [cpu2evtstreams](cpu_msg_example.md).

Le fichier `horizon/service.definition.json` inclut également une section `deployment`, vers la fin du fichier. La section de déploiement contient une mappe appelée `services` qui définit le nom DNS et la configuration de chaque image de conteneur qui met en œuvre le service logique. Le nom DNS de chaque service défini dans la mappe `services` est le même que la clé de la mappe qui définit la configuration du conteneur. Le nom DNS est utilisé par d'autres conteneurs pour lancer les API distantes hébergées par ce conteneur. Le nom DNS de chaque conteneur doit être unique dans un groupe de conteneurs collaborant. Par exemple, si ce conteneur fournit une API REST que d'autres conteneurs peuvent utiliser, les applications dans d'autres conteneurs peuvent lancer cette API REST à l'aide de la commande `curl http://<dns-name>/<your-rest-api-uri>`. Le fait de ne pas garantir l'unicité du nom DNS entraîne un comportement non déterministe lors de l'accès à des API distantes hébergées par des conteneurs ayant des noms en conflit sur le même réseau virtuel privé. La zone `image` associée à chaque nom fournit une référence vers l'image du conteneur Docker correspondant, comme dans DockerHub ou certains registres de conteneurs privés. D'autres zones de la section `deployment` peuvent être utilisées pour modifier la manière dont l'agent indique à Docker d'exécuter le conteneur. Pour plus d'informations, voir la [configuration de déploiement {{site.data.keyword.horizon}}](https://github.com/open-horizon/anax/blob/master/docs/deployment_string.md).

## Etape suivante
{: #developing_what_next}

Pour plus d'informations sur le développement de code d'un noeud de périphérie, consultez la documentation suivante :

* [Pratiques de développement natif Edge](best_practices.md)

   Consultez les grands principes et les meilleures pratiques concernant le développement logiciel de services de périphérie pour {{site.data.keyword.ieam}}.

* [Utilisation d'{{site.data.keyword.cloud_registry}}](container_registry.md)

  {{site.data.keyword.ieam}} vous permet de placer vos conteneurs de services dans le registre de conteneurs sécurisés privé d'IBM plutôt que sur le Docker Hub public. Par exemple, si vous avez une image logicielle qui comporte des actifs qui n'ont pas lieu d'être dans un registre public, vous pouvez faire appel à un registre de conteneurs Docker privé, tel qu'{{site.data.keyword.cloud_registry}}.

* [API](../api/edge_rest_apis.md)

  {{site.data.keyword.ieam}} fournit des API RESTful pour collaborer et permet aux développeurs et utilisateurs de votre organisation de contrôler ces composants.

* [Mise à jour d'un service de périphérie avec restauration de la version précédente](../using_edge_services/service_rollbacks.md)

  Consultez des détails supplémentaires sur la manière de déployer une nouvelle version d'un service de périphérie et les meilleures pratiques de développement logiciel visant à mettre à jour les paramètres de restauration dans le pattern ou les règles de déploiement.
