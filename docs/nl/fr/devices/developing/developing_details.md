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

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) est basé sur le logiciel open source [Open Horizon - EdgeX Project Group ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://wiki.edgexfoundry.org/display/FA/Open+Horizon+-+EdgeX+Project+Group).

Avec {{site.data.keyword.ieam}}, vous pouvez développer n'importe quel conteneur de services pour vos machines de périphérie. Vous pouvez ensuite les signer de manière cryptographique et publier votre code. Enfin, vous pouvez définir des règles au sein d'un {{site.data.keyword.edge_deploy_pattern}} pour gérer l'installation, la surveillance et la mise à jour des logiciels. Une fois ces tâches terminées, vous pouvez visualiser les {{site.data.keyword.horizon_agents}} et les {{site.data.keyword.horizon_agbots}} qui concluent des accords pour participer à la gestion du cycle de vie des logiciels. Ces composants gèrent ensuite les détails du cycle de vie sur vos {{site.data.keyword.edge_nodes}} de manière totalement autonome en fonction du pattern de déploiement enregistré auprès de chaque noeud de périphérie. {{site.data.keyword.ieam}} peut également utiliser des règles pour déterminer où et quand déployer de manière autonome des services et des modèles d'apprentissage automatique. Les règles peuvent être utilisées comme solution de rechange aux patterns de déploiement.

Le processus de développement logiciel d'{{site.data.keyword.ieam}} se concentre sur la sécurité et l'intégrité du système, tout en simplifiant les efforts nécessaires à la gestion logicielle active sur vos noeuds de périphérie. {{site.data.keyword.ieam}} peut également utiliser des règles pour déterminer où et quand déployer de manière autonome des services et des modèles d'apprentissage automatique. Les règles peuvent être utilisées comme solution de rechange aux patterns de déploiement. Vous pouvez générer des procédures de publication {{site.data.keyword.ieam}} dans votre intégration continue et votre pipeline de déploiement. Lorsque les agents autonomes distribués détectent des modifications apportées au logiciel ou à une règle, par exemple dans le {{site.data.keyword.edge_deploy_pattern}} ou la règle de déploiement, ils agissent de façon indépendante pour mettre à jour le logiciel ou appliquer les règles à l'ensemble des machines de périphérie, où qu'elles se trouvent.

## Services et patterns de déploiement
{: #services_deploy_patterns}

Les {{site.data.keyword.edge_services}} représentent les blocs de développement des patterns de déploiement. Chaque service peut contenir un ou plusieurs conteneurs Docker. Chaque conteneur Docker peut à son tour contenir un ou plusieurs processus à exécution longue. Ces processus peuvent être écrits dans presque n'importe quel langage de programmation, et utiliser n'importe quelle bibliothèque ou n'importe quel utilitaire. Toutefois, les processus doivent être développés et exécutés dans le contexte d'un conteneur Docker. Cette souplesse d'utilisation signifie qu'il n'y a quasi aucune contrainte sur le code qu'{{site.data.keyword.ieam}} peut gérer pour vous. Lorsqu'un conteneur s'exécute, il est isolé dans un bac à sable sécurisé. Ce bac à sable limite l'accès aux unités matérielles, à certains services du système d'exploitation, au système de fichier hôte, ainsi qu'aux réseaux de machines de périphérie hôte. Pour plus d'informations sur les contraintes liées aux bacs à sable, voir [Bac à sable](#sandbox).

L'exemple de code `cpu2evtstreams` consiste en un conteneur Docker qui utilise deux autres services de périphérie locaux. Ceux-ci se connectent via des réseaux virtuels Docker privés locaux à l'aide d'API REST HTTP. Ils se nomment `cpu` et `gps`. L'agent déploie chacun des services sur un réseau privé séparé avec chaque service ayant déclaré une dépendance sur le service. Un réseau est créé pour `cpu2evtstreams` et `cpu`, et un autre est créé pour `cpu2evtstreams` et `gps`. Si un quatrième service partageant également le service `cpu` existe dans le pattern de déploiement, un autre réseau privé est créé spécifiquement pour `cpu` et le quatrième service. Dans {{site.data.keyword.ieam}}, cette stratégie réseau limite l'accès des services uniquement à ceux qui sont répertoriés dans `requiredServices` lorsque les autres services sont publiés. Le diagramme suivant illustre le pattern de déploiement `cpu2evtstreams` lorsque le pattern s'exécute sur un noeud de périphérie :

<img src="../../images/edge/07_What_is_an_edge_node.svg" width="70%" alt="Services dans un pattern">

Remarque : L'installation d'IBM Event Streams est nécessaire seulement pour certains exemples.

Les deux réseaux virtuels permettent au conteneur de service `cpu2evtstreams` d'accéder aux interfaces de programmation REST fournies par les conteneurs de services `cpu` et `gps`. Ces deux conteneurs gèrent l'accès aux services du système d'exploitation et aux unités matérielles. Bien que les API REST soient utilisées, il existe de nombreuses autres formes de communication possibles pour permettre aux services de partager et de contrôler les données.

Souvent, le pattern de codage le plus efficace pour les noeuds de périphérie implique le déploiement de plusieurs petits services déployables et configurables de façon indépendante. Par exemple, les patterns de l'internet des objets ont souvent des services de bas niveau qui ont besoin d'accéder au matériel du noeud de périphérie, tels que des détecteurs ou des régulateurs. Ces services offrent un accès partagé à ce matériel pour les autres services à utiliser.

Ce pattern est pratique lorsque le matériel nécessite un accès exclusif pour pouvoir fournir une fonction utile. Le service de bas niveau peut correctement gérer cet accès. Le rôle des conteneurs de services `cpu` et `gps` repose sur le même principe que celui du logiciel du pilote de périphérie dans le système d'exploitation de l'hôte, mais à un niveau plus élevé. Le fait de segmenter le code en plusieurs petits services indépendants, certains se spécialisant dans l'accès matériel de bas niveau, permet de séparer les problématiques. Chaque composant est libre d'évoluer et d'être mis à jour de manière autonome. Des applications tierces peuvent également être déployées en toute sécurité avec votre pile de logiciels intégrés propriétaire en leur permettant d'accéder de manière sélective à un matériel spécifique ou à d'autres services.

Par exemple, un pattern de déploiement de contrôleur industriel peut être composé d'un service de bas niveau pour surveiller des capteurs d'utilisation d'énergie et d'autres services de bas niveau. Ces derniers peuvent quant à eux être utilisés pour contrôler les régulateurs qui alimentent les unités surveillées. De plus, le pattern de déploiement peut comporter un autre conteneur de services de niveau supérieur qui utilise les services du capteur et du régulateur. Ce service de niveau supérieur peut utiliser les services pour alerter les opérateurs ou pour mettre automatiquement les unités hors tension en cas de relevés de consommation électrique anormaux. Ce pattern de déploiement peut également inclure un service historique qui enregistre et archive les données du capteur et du régulateur, et faire éventuellement une analyse des données. D'autres composants peuvent être utiles pour ce type de pattern de déploiement, notamment un service de localisation GPS.

Chaque conteneur de service individuel peut être mis à jour de manière indépendante avec cette conception. Chaque service individuel peut également être reconfiguré et inséré dans d'autres patterns de déploiement utiles, sans aucun changement de code. Si besoin, un service d'analyse tiers peut être ajouté au pattern. Ce service tiers peut avoir accès uniquement à un ensemble spécifique d'API en lecture seule, qui limite l'interaction du service avec les régulateurs sur la plateforme.

Vous pouvez également choisir d'exécuter toutes les tâches de cet exemple de contrôleur industriel dans un même conteneur de services. Toutefois, cette solution n'est pas forcément la meilleure, sachant qu'une collection de services indépendants et interconnectés plus petits permet généralement des mises à jour logicielles plus rapides et plus flexibles. Les collections de petits services s'avèrent également plus robustes. Pour en savoir plus sur la conception de vos patterns de déploiement, voir [Pratiques de développement Edge natif](best_practices.md).

## Bac à sable
{: #sandbox}

Le bac à sable dans lequel s'exécutent les patterns de déploiement limite l'accès aux API fournies par vos conteneurs de services. Seuls les services qui mentionnent explicitement les dépendances sur vos services sont autorisés à y accéder. Les autres processus sur l'hôte n'ont normalement pas accès à ces services. De la même manière, les autres hôtes distants n'ont normalement pas accès à aucun de ces services à moins que le service ne publie explicitement un port sur l'interface réseau externe de l'hôte.

## Services utilisant d'autres services
{: #using_services}

Les services de périphérie utilisent souvent les interfaces de programmation fournies par d'autres services de périphérie pour l'acquisition de données ou l'émission de commandes de contrôle. Ces interfaces de programmation sont généralement des API REST HTTP, telles que celles mises à disposition par les services `cpu` et `gps` de bas niveau dans l'exemple `cpu2evtstreams`. Toutefois, ces interfaces peuvent être celles de votre choix, par exemple la mémoire partagée, ou le protocole TCP ou UDP, et peuvent être avec ou sans chiffrement. Compte tenu que les communications se déroulent généralement dans un seul noeud de périphérie et que les messages ne sortent pas de cet hôte, le chiffrement est souvent inutile.

Outre l'utilisation d'une API REST, vous pouvez utiliser une interface de publication et d'abonnement, telle que l'interface fournie par MQTT. Lorsqu'un service fournit des données par intermittence, il est généralement plus simple d'utiliser une interface de publication et d'abonnement que d'interroger à plusieurs reprises une API REST, d'autant plus que les API REST peuvent dépasser le délai d'attente imparti. Prenons l'exemple d'un service qui surveille un bouton matériel et qui fournit une API afin de permettre à d'autres services de détecter lorsqu'une pression bouton se produit. Si une API REST est utilisée, l'appelant ne peut pas appeler l'API et attendre qu'une réponse soit envoyée lorsque le bouton est activé. Si le bouton reste longtemps sans aucune pression, le délai d'attente de l'API REST risque de dépasser le délai d'attente. Le fournisseur d'API devrait alors répondre immédiatement pour éviter qu'une erreur ne se produise. L'appelant doit appeler l'API fréquemment et de manière répétée pour être sûr de ne manquer aucune pression de bouton. Une bien meilleure solution consiste pour l'appelant à s'abonner à une rubrique appropriée sur un service et bloc de publication et d'abonnement. Ensuite, l'appelant peut attendre une publication, qui peut se produire dans un avenir lointain. Le fournisseur d'API peut se charger de la surveillance du bouton matériel et publier ensuite uniquement les changements d'état de cette rubrique, notamment `button pressed`, ou `button released`.

MQTT figure parmi les outils de publication et d'abonnement les plus populaires. Vous pouvez déployer un courtier MQTT en tant que service de périphérie, et exiger que vos services l'utilisent. MQTT est aussi fréquemment utilisé comme service cloud. Par exemple, la plateforme IBM Watson IoT, utilise MQTT pour communiquer avec les terminaux IoT. Pour plus d'informations, voir [IBM Watson IoT Platform ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://www.ibm.com/cloud/watson-iot-platform). Certains exemples de projet {{site.data.keyword.horizon_open}} font appel à MQTT. Pour plus d'informations, voir [{{site.data.keyword.horizon_open}} examples](https://github.com/open-horizon/examples).

Un autre outil de publication et d'abonnement relativement connu est Apache Kafka, aussi fréquemment utilisé comme service cloud. {{site.data.keyword.message_hub_notm}}, qui est utilisé par l'exemple `cpu2evtstreams` pour envoyer des données à {{site.data.keyword.cloud_notm}}, est également basé sur Kafka. Pour plus d'informations, voir [{{site.data.keyword.message_hub_notm}} ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://www.ibm.com/cloud/event-streams).

N'importe quel conteneur de service de périphérie peut fournir ou utiliser d'autres services de périphérie locaux sur le même hôte, ainsi que les services de périphérie fournis sur des hôtes voisins sur le réseau local. Les conteneurs peuvent communiquer avec des systèmes centralisés dans un centre de données d'entreprise distant ou fournisseur de cloud. En votre qualité d'auteur de service, vous déterminez avec qui et comment vos services communiquent.

Vous jugerez peut-être utile de revoir l'exemple `cpu2evtstreams` afin de voir comment l'exemple de code utilise les deux autres services locaux. Notamment la manière dont l'exemple de code indique les dépendances sur les deux services locaux, déclare et utilise les variables de configuration, et communique avec Kafka. Pour plus d'informations, voir [Exemple `cpu2evtstreams`](cpu_msg_example.md).

## Définition de service
{: #service_definition}

Remarque : Pour plus d'informations sur la syntaxe de commande, voir [Conventions de ce guide](../../getting_started/document_conventions.md).

Dans chaque projet {{site.data.keyword.ieam}} se trouve un fichier `horizon/service.definition.json`. Ce fichier définit le service de périphérie pour deux raisons. La première est de vous aider à simuler l'exécution de votre service par l'outil `hzn dev`, comme dans l'{{site.data.keyword.horizon_agent}}. Cette simulation se révèle particulièrement utile pour élaborer des instructions de déploiement particulières, telles que des liaisons de port ou l'accès à l'unité matérielle. Elle permet également de vérifier les communications entre les conteneurs de services sur les réseaux privés virtuels Docker que l'agent crée pour vous. La seconde est de vous aider à publier votre service dans {{site.data.keyword.horizon_exchange}}. Dans les exemples fournis, le fichier `horizon/service.definition.json` est soit inclus avec l'exemple de référentiel GitHub, soit généré par la commande `hzn dev service new`.

Ouvrez le fichier `horizon/service.definition.json` qui contient les métadonnées {{site.data.keyword.horizon}} de l'un des exemples d'implémentation de service, notamment [cpu2evtstreams](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/cpu2evtstreams/horizon/service.definition.json).

Chaque service publié dans {{site.data.keyword.horizon}} doit posséder un paramètre `url` qui l'identifie de manière unique dans votre organisation. Cette zone n'est pas une URL. En fait, la zone `url` forme un identificateur unique global, lorsqu'il est combiné au nom de votre organisation et une implémentation spécifique des zones `version` et `arch`. Vous pouvez éditer le fichier `horizon/service.definition.json` pour fournir des valeurs appropriées pour `url` et `version`. Pour la valeur `version`, utilisez une valeur de style de gestion des versions. Utilisez ces nouvelles valeurs lorsque vous exécutez la commande push, que vous signez et que vous publiez vos conteneurs de services. Une autre solution consiste à modifier le fichier `horizon/hzn.json` pour que les outils remplacent les valeurs de variables qui s'y trouvent, au lieu des références de variable utilisées dans le fichier `horizon/service.definition.json`.

La section `requiredServices` du fichier `horizon/service.definition.json` détaille toutes les dépendances de service, telles que les autres services de périphérie utilisés par ce conteneur. L'outil `hzn dev dependency fetch` permet d'ajouter des dépendances à cette liste, afin que vous n'ayez plus besoin d'éditer la liste manuellement. Lorsque les dépendances ont été ajoutées, lorsque l'agent exécute le conteneur, ces autres services `requiredServices` sont exécutés automatiquement chaque fois (lorsque, par exemple, vous utilisez `hzn dev service start` ou que vous enregistrez un noeud auprès d'un pattern de déploiement qui contient ce service). Pour plus d'informations sur les services requis, voir [cpu2evtstreams](cpu_msg_example.md).

Dans la section `userInput`, vous affectez les variables de configuration que votre service peut utiliser pour se configurer pour un déploiement particulier. Vous indiquez ici les noms de variables, les types de données et les valeurs par défaut, et vous avez la possibilité de fournir une description en format contrôlable de visu pour chacun d'entre eux. Lorsque vous utilisez la commande `hzn dev service start` ou que vous enregistrez un noeud de périphérie avec un pattern de déploiement qui contient ce service, vous devez spécifier un fichier `userinput.json` pour définir les valeurs des variables dépourvues de valeur par défaut. Pour plus d'informations sur les variables de configuration `userInput` et les fichiers `userinput.json`, voir [cpu2evtstreams](cpu_msg_example.md).

Le fichier `horizon/service.definition.json` inclut également une section `deployment`, vers la fin du fichier. Les zones de cette section nomment chaque image de conteneur Docker qui implémente votre service logique. Le nom de chaque enregistrement qui est utilisé ici dans le tableau `services` est le nom utilisé par les autres conteneurs pour identifier le conteneur sur le réseau privé virtuel partagé. Si ce conteneur fournit une API REST devant être utilisée par les autres conteneurs, vous pouvez accéder à cette interface du conteneur de consommation à l'aide de la commande `curl http://<name>/<your-rest-api-uri>`. La zone `image` associée à chaque nom fournit une référence vers l'image du conteneur Docker correspondant, comme dans DockerHub ou certains registres de conteneurs privés. D'autres zones de la section `deployment` peuvent être utilisées pour modifier la manière dont l'agent indique à Docker d'exécuter le conteneur. Pour plus d'informations, voir [{{site.data.keyword.horizon}} deployment strings ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://github.com/open-horizon/anax/blob/master/doc/deployment_string.md).

## Interaction avec {{site.data.keyword.horizon_exchange}}
{: #horizon_exchange}

Lorsque vous générez et publiez les exemples de programme, vous interagissez avec {{site.data.keyword.horizon_exchange}} pour publier vos services, vos règles et vos patterns de déploiement. Vous utilisez également {{site.data.keyword.horizon_exchange}} pour enregistrer vos noeuds de périphérie de sorte qu'ils exécutent un pattern de déploiement spécifique. {{site.data.keyword.horizon_exchange}} joue le rôle de référentiel pour les informations partagées, ce qui vous permet de communiquer indirectement avec d'autres composants d'{{site.data.keyword.ieam}}. En tant que développeur, vous devez connaître le fonctionnement d'{{site.data.keyword.horizon_exchange}}.

Ce diagramme illustre les agents qui doivent s'exécuter dans chaque noeud de périphérie, ainsi que les agbots qui doivent être configurés pour chaque pattern de déploiement dans le cloud ou dans un centre de données d'entreprise centralisé.

En règle générale, les développeurs {{site.data.keyword.ieam}} utilisent la commande `hzn` pour interagir avec {{site.data.keyword.horizon_exchange}}. Plus précisément, la commande `hzn exchange` est utilisée pour toutes les interactions avec {{site.data.keyword.horizon_exchange}}. Vous pouvez taper `hzn exchange --help` pour afficher toutes les sous-commandes qui peuvent suivre `hzn exchange` sur la ligne de commande. Puis, vous pouvez utiliser `hzn exchange <subcommand> --help` pour obtenir plus de détails sur la sous-commande `<subcommand>` de votre choix.

Les commandes ci-dessous sont particulièrement utiles pour interroger {{site.data.keyword.horizon_exchange}} :

* Vérifier que vos données d'identification utilisateur fonctionnent dans {{site.data.keyword.horizon_exchange}} : `hzn exchange user list`
* Vérifier la version logicielle d'{{site.data.keyword.horizon_exchange}} : `hzn exchange version`
* Vérifier le statut en cours d'{{site.data.keyword.horizon_exchange}} : `hzn exchange status`
* Répertorier tous les noeuds de périphérie qui sont créés sous votre organisation : `hzn exchange node list`
* Récupérer les détails d'un noeud de périphérie spécifique : `hzn exchange node list <node-id>`
  Remplacez l'ID de noeud `<node-id>` par la valeur d'ID du noeud de périphérie.
* Répertorier tous les services qui sont publiés sous votre organisation : `hzn exchange service list`
* Répertorier tous les services publics qui sont publiés sous une organisation : `hzn exchange service list '<org>/*'`
* Récupérer les détails d'un service publié particulier : `hzn exchange service list <org/service>`
* Répertorier tous les patterns de déploiement qui sont publiés sous votre organisation : `hzn exchange pattern list`
* Répertorier tous les patterns de déploiement qui sont publiés sous une organisation : `hzn exchange pattern list '<org>/*'`
* Répertorier tous les détails d'un service publié particulier : `hzn exchange pattern list <org/pattern>`

## Agents et agbots
{: #agents_agbots}

Il est essentiel de bien maîtriser le rôle des agents et des agbots, ainsi que la façon dont ils communiquent. Ces connaissances peuvent vous aider lors du diagnostic et de la résolution de problème, le cas échéant.

Les agents et les agbots ne communiquent jamais directement entre eux. L'agent de chaque noeud de périphérie doit installer sa propre boîte aux lettres dans la {{site.data.keyword.horizon_switch}} et crée une ressource de noeud dans {{site.data.keyword.horizon_exchange}}. Ensuite, lorsqu'il veut exécuter un pattern de déploiement particulier, il s'enregistre auprès de ce pattern dans {{site.data.keyword.horizon_exchange}}.

Les agbots surveillent les patterns et interrogent sans cesse {{site.data.keyword.horizon_exchange}} pour recherches les noeuds de périphérie qui s'enregistrent auprès du pattern. Lorsqu'un nouveau noeud de périphérie s'enregistre afin d'utiliser un pattern, un agbot contacte l'agent local sur le noeud de périphérie correspondant. L'agbot utilise pour cela la {{site.data.keyword.horizon_switch}}. A présent, tout ce que peut connaître l'agbot sur l'agent est sa clé publique. Il ne connaît pas l'adresse IP du noeud de périphérie ni quoi que ce soit d'autre sur le noeud de périphérie hormis le fait qu'il est enregistré auprès du pattern de déploiement spécifique. L'agbot communique avec l'agent via la {{site.data.keyword.horizon_switch}} afin de lui proposer de collaborer à la gestion du cycle de vie du logiciel de ce pattern de déploiement sur ce noeud de périphérie.

L'agent associé à chaque noeud de périphérie surveille la {{site.data.keyword.horizon_switch}} pour voir si la boîte aux lettres contient des messages. Lorsque l'agent reçoit une proposition d'un agbot, il l'évalue en fonction des règles définies par le propriétaire du noeud de périphérie au moment de la configuration du noeud de périphérie et décide d'accepter ou non la proposition.

Lorsqu'une proposition de pattern de déploiement est acceptée, l'agent procède à l'extraction des conteneurs de services appropriés à partir du registre Docker approprié, vérifie les signatures du service, le configure et l'exécute.

Toutes les communications entre les agents et les agbots qui passent par la {{site.data.keyword.horizon_switch}} sont chiffrées par les deux parties. Même si ces messages sont stockés dans la {{site.data.keyword.horizon_switch}} centrale, la {{site.data.keyword.horizon_switch}} n'est pas en mesure de déchiffrer ni d'écouter secrètement ces conversations.

## Déploiement des mises à jour logicielles de service
{: #deploy_edge_updates}

Après avoir déployé votre logiciel sur l'ensemble de vos noeuds de périphérie, vous pouvez mettre à jour le code si vous le souhaitez. Les mises à jour logicielles peuvent être effectuées avec {{site.data.keyword.ieam}}. En règle générale, vous n'avez rien à faire sur les noeuds de périphérie pour mettre à jour le logiciel qui s'exécute dessus. Dès que vous signez et publiez une mise à jour, les agbots et les agents qui s'exécutent sur chaque noeud de périphérie se coordonnent afin de déployer la version la plus récente de votre pattern de déploiement sur chaque noeud de périphérie qui est enregistré auprès du pattern de déploiement mis à jour. L'un des avantages offerts par {{site.data.keyword.ieam}} est la facilité avec laquelle le pipeline de mise à jour logicielle est appliqué à l'ensemble des noeuds de périphérie.

Pour publier une nouvelle version logicielle, effectuez les étapes suivantes : 

* Editez le code de service pour cette mise à jour.
* Editez le numéro de version sémantique du code.
* Regénérez vos conteneurs de services.
* A l'aide de la commande push, envoyez vos conteneurs de services mis à jour vers le registre Docker approprié.
* Signez et publiez les services mis à jour dans {{site.data.keyword.horizon_exchange}}.
* Republiez votre pattern de déploiement dans {{site.data.keyword.horizon_exchange}}. Utilisez le même nom et référencez les nouveaux numéros de version de service.

Les agbots {{site.data.keyword.horizon}} détectent rapidement les modifications apportées au pattern de déploiement. Les agbots contactent alors chacun des agents dont le noeud de périphérie est enregistré afin d'exécuter le pattern de déploiement. L'agbot et l'agent se coordonnent pour télécharger les nouveaux conteneurs, arrêter et retirer les anciens conteneurs, et démarrer les nouveaux.

Il résulte de ce processus que chaque noeud de périphérie enregistré pour exécuter le pattern de déploiement mis à jour exécute rapidement la nouvelle version du conteneur de service, quel que soit l'emplacement géographique du noeud de périphérie.

## Etape suivante
{: #developing_what_next}

Pour plus d'informations sur le développement de code d'un noeud de périphérie, consultez la documentation suivante :

[Pratiques de développement Edge natif](best_practices.md)

Consultez les grands principes et les meilleures pratiques concernant le développement logiciel de services de périphérie pour {{site.data.keyword.ieam}}.

[Utilisation d'{{site.data.keyword.cloud_registry}}](container_registry.md)

{{site.data.keyword.ieam}} vous permet de placer vos conteneurs de services dans le registre de conteneurs sécurisés privé d'IBM plutôt que sur le Docker Hub public. Par exemple, si vous avez une image logicielle qui comporte des actifs qui n'ont pas lieu d'être dans un registre public, vous pouvez faire appel à un registre de conteneurs Docker privé, tel qu'{{site.data.keyword.cloud_registry}}.

[Interfaces API](../installing/edge_rest_apis.md)

{{site.data.keyword.ieam}} fournit des API RESTful permettant aux composants de collaborer et aux développeurs et utilisateurs de votre organisation de contrôler ces composants.
