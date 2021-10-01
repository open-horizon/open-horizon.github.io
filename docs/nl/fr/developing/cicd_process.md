---

copyright:
years: 2020
lastupdated: "2020-03-18"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Processus CI-CD pour les services de périphérie
{: #edge_native_practices}

Un ensemble de services de périphérie évolutifs est essentiel pour utiliser efficacement {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}), et un processus d'intégration continue et de déploiement continu (CI/CD) en est la condition nécessaire. 

Servez-vous des informations ci-dessous pour déterminer les blocs de construction mis à votre disposition afin de créer votre propre processus CI/CD. Puis, pour en savoir plus sur ce processus, accédez au référentiel [`open-horizon/examples`](https://github.com/open-horizon/examples).

## Variables de configuration
{: #config_variables}

En tant que développeur de services de périphérie, tenez compte de la taille du conteneur de service en cours de développement. Vous devrez peut-être segmenter vos fonctions de services en conteneurs distincts. Dans ce cas, les variables de configuration utilisées à des fins de test peuvent servir à simuler les données qui proviennent d'un conteneur qui n'est pas encore développé. Dans le [fichier de définition de service cpu2evtstreams](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/cpu2evtstreams/horizon/service.definition.json), vous pouvez voir des variables d'entrée telles que **PUBLISH** et **MOCK**. Si vous examinez le code `service.sh`, vous constatez qu'il utilise les variables de configuration suivantes, entre autres, pour contrôler son comportement. La variable **PUBLISH** vérifie si le code tente d'envoyer des messages à IBM Event Streams. La variable **MOCK** vérifie si service.sh tente de contacter les API REST et ses services dépendants (cpu et gps) ou si `service.sh` crée des données fictives.

Au moment du déploiement de service, vous pouvez substituer les valeurs par défaut des variables de configuration en les spécifiant dans la définition de noeud ou dans la commande `hzn register`.

## Compilation croisée
{: #cross_compiling}

Vous pouvez utiliser Docker pour développer un service conteneurisé sur plusieurs architectures à partir d'une seule machine amd64. De la même manière, vous pouvez développer des services de périphérie avec des langages de programmation compilés compatibles avec la compilation croisée, tels que Go. Par exemple, si vous codez depuis votre appareil Mac (architecture amd64) pour un appareil arm (un Raspberry Pi), vous devrez peut-être développer un conteneur Docker avec des paramètres comme GOARCH pour cibler arm. Cette configuration peut éviter les erreurs de déploiement. Voir [open-horizon gps service](https://github.com/open-horizon/examples/tree/master/edge/services/gps).

## Tests
{: #testing}

Des tests fréquents et automatisés constituent un élément important du processus de développement. Pour en faciliter l'utilisation, vous pouvez vous servir de la commande `hzn dev service start` pour exécuter votre service dans un environnement d'agent Horizon simulé. Cette approche est également utile dans les environnements devops dans lesquels l'installation et l'enregistrement de l'agent Horizon complet peuvent se révéler problématiques. En effet, cette méthode automatise les tests dans le référentiel `open-horizon examples` avec la cible **make test**. Voir [make test target](https://github.com/open-horizon/examples/blob/305c4f375aafb09733f244ec9a899ce136b6d311/edge/services/helloworld/Makefile#L30).


Exécutez **make test** pour concevoir et exécuter le service qui utilise la commande **hzn dev service start**. Une fois démarré, [serviceTest.sh](https://github.com/open-horizon/examples/blob/master/tools/serviceTest.sh) surveille les journaux de service pour localiser les données qui indiquent que le service s'exécute correctement.

## Déploiement de test
{: #testing_deployment}

Lorsque vous développez une nouvelle version de service, il est recommandé d'effectuer un test complet en grandeur réelle. Vous pouvez pour cela déployer votre service sur les noeuds de périphérie ; toutefois, s'agissant d'un test, il se peut que vous ne souhaitiez pas déployer tout de suite votre service sur l'ensemble de vos noeuds de périphérie.

Créez une règle de déploiement ou un pattern qui ne fait référence qu'à votre nouvelle version de service. Enregistrez ensuite vos noeuds de tests auprès de cette règle ou de ce pattern. Si vous avez recours à une règle, l'une des options consiste à définir une propriété sur un noeud de périphérie, par exemple, "name": "mode", "value": "testing", puis d'ajouter cette contrainte à votre règle de déploiement ("mode == testing"). Vous avez ainsi la garantie que seuls les noeuds réservés à des fins de test reçoivent la nouvelle version de votre service.

**Remarque **: vous pouvez également créer une politique ou un modèle de déploiement à partir de la console de gestion. Voir [Utilisation de la console de gestion](../console/accessing_ui.md).

## Déploiement de production
{: #production_deployment}

Après avoir transféré la nouvelle version de votre service d'un environnement de test à un environnement de production, il se peut que vous rencontriez des problèmes qui ne s'étaient pas posés pendant la phase de test. Dans ce cas, les paramètres de restauration de votre pattern ou de votre règle de déploiement peuvent se révéler forts utiles. Vous avez la possibilité d'indiquer plusieurs versions antérieures de votre service dans la section `serviceVersions` d'un pattern ou d'une règle de déploiement. Indiquez la version que vous souhaitez restaurer pour chacun de vos noeuds de périphérie en cas d'erreur avec la nouvelle version. Outre l'affectation d'une priorité, vous pouvez indiquer le nombre et la durée des tentatives avant de passer à une version du service avec une priorité inférieure. Pour connaître la syntaxe spécifique, voir [cet exemple de règle de déploiement](https://github.com/open-horizon/anax/blob/master/cli/samples/business_policy.json).

## Affichage de vos noeuds de périphérie
{: #viewing_edge_nodes}

Après avoir déployé une nouvelle version de service sur les noeuds, il est important de pouvoir surveiller la santé de vos noeuds de périphérie en toute simplicité. Utilisez la {{site.data.keyword.gui}} d'{{site.data.keyword.ieam}} pour cette tâche. Par exemple, lorsque vous exécutez le processus de [Déploiement de test](#testing_deployment) ou de [Déploiement de production](#production_deployment), vous pouvez facilement rechercher les noeuds qui génèrent des erreurs lors de l'utilisation de votre règle de déploiement ou de vos noeuds.

## Migration de services
{: #migrating_services}

Il se peut qu'à un moment ou à un autre vous ayez besoin de transférer des services, des patterns ou des règles d'une instance d'{{site.data.keyword.ieam}} à une autre. De même, il se peut que vous ayez besoin de transférer des services d'une organisation Exchange à une autre. Par exemple, cela peut se produire si vous avez installé une nouvelle instance d'{{site.data.keyword.ieam}} dans un environnement hôte différent. Vous pouvez également avoir besoin de transférer des services si vous disposez de deux instances d'{{site.data.keyword.ieam}}, l'une dédiée au développement et l'autre à la production. Pour faciliter ce processus, utilisez le script [`loadResources`](https://github.com/open-horizon/examples/blob/master/tools/loadResources) qui se trouve dans le référentiel des exemples open-horizon.

## Test de demande d'extraction automatisé avec Travis
{: #testing_with_travis}

Vous pouvez automatiser le test chaque fois qu'une demande d'extraction est ouverte dans votre référentiel GitHub en utilisant l'outil d'intégration [Travis CI](https://travis-ci.com). 

Lisez les informations ci-dessous pour en savoir plus sur la façon de tirer avantage de Travis et des techniques fournies dans le référentiel GitHub des exemples open-horizon. 

Dans le référentiel des exemples, Travis CI permet de concevoir, de tester et de publier des échantillons. Dans le fichier [`.travis.yml`](https://github.com/open-horizon/examples/blob/master/.travis.yml), un environnement virtuel est configuré pour s'exécuter en tant que machine Linux amd64 avec hzn, Docker et [qemu](https://github.com/multiarch/qemu-user-static) et être ainsi compatible avec plusieurs architectures.

Dans ce scénario, kafkacat est également installé pour permettre à cpu2evtstreams d'envoyer des données à IBM Event Streams. A l'instar de la ligne de commande, Travis peut faire appel à des variables d'environnement de type `EVTSTREAMS_TOPIC` et `HZN_DEVICE_ID` pour utiliser les exemples de services de périphérie. La commande HZN_EXCHANGE_URL est configurée de manière à pointer vers l'environnement de préproduction d'Exchange pour publier les services modifiés. 

Le script [travis-find](https://github.com/open-horizon/examples/blob/master/tools/travis-find) est ensuite utilisé pour identifier les services qui ont été modifiés par la demande d'extraction ouverte.

Si un exemple a été modifié, la cible `test-all-arches` qui se trouve dans le fichier **makefile** de ce service s'exécute. Lorsque les conteneurs qemu des architectures prises en charge sont exécutés, les versions d'architecture croisée s'exécutent avec la cible **makefile** en définissant la variable d'environnement `ARCH` juste avant la génération et le test. 

La commande `hzn dev service start` exécute le service de périphérie et le fichier [serviceTest.sh](https://github.com/open-horizon/examples/blob/master/tools/serviceTest.sh) surveille les journaux de service pour déterminer si le service fonctionne correctement.

Voir [helloworld Makefile](https://github.com/open-horizon/examples/blob/afd4a5822aede44616eb5da7cd9dafd4d78f12ec/edge/services/helloworld/Makefile#L24) pour afficher la cible makefile `test-all-arches` dédiée.

Le scénario ci-dessous montre un test de bout en bout plus approfondi. Si l'un des exemples modifiés comporte `cpu2evtstreams`, une instance d'IBM Event Streams peut être surveillée en arrière-plan et HZN_DEVICE_ID faire l'objet d'une vérification. Il peut réussir le test et être ajouté à la liste de tous les services fonctionnels si l'ID de noeud **travis-test** est identifié dans les données qui sont lues à partir de la rubrique cpu2evtstreams. Pour ce faire, une clé d'API et une URL de courtier IBM Event Streams doivent être configurées comme variables d'environnement secrètes.

Une fois le PR fusionné, le processus est répété et la liste des services fonctionnels est utilisée pour identifier ceux qui peuvent être publiés dans Exchange. Les variables d'environnement secrètes Travis qui sont utilisées dans cet exemple incluent tous les éléments nécessaires pour envoyer, signer et publier des services dans Exchange. Cela inclut les données d'identification Docker, HZN_EXCHANGE_USER_AUTH et une paire de clés de signature cryptographique accessible à l'aide de la commande `hzn key create`. Afin de sauvegarder les clés de signature en tant que variables d'environnement sécurisées, celles-ci doivent être encodées au format base64.

La liste des services ayant réussi le test fonctionnel est utilisée pour identifier les services qui doivent être publiés avec la cible `Makefile` de publication dédiée. Voir [helloworld sample](https://github.com/open-horizon/examples/blob/afd4a5822aede44616eb5da7cd9dafd4d78f12ec/edge/services/helloworld/Makefile#L45).

Les services ayant été générés et testés, cette cible publie le service, la règle de service, le pattern et la règle de déploiement de toutes les architectures dans Exchange. 

**Remarque** :  vous pouvez également effectuer plusieurs de ces tâches à partir de la console de gestion. Voir [Utilisation de la console de gestion](../console/accessing_ui.md).

