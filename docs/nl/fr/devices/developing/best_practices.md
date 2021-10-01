---

copyright:
years: 2019, 2020
lastupdated: "2020-02-13"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Pratiques de développement Edge natif
{: #edge_native_practices}

Vous allez créer des charges de travail qui s'exécuteront en périphérie de réseau, à savoir dans des installations situées en dehors des limites de votre centre de données informatique ou de votre environnement de cloud. Cela signifie que vous devrez tenir compte des conditions spécifiques à ces environnements. Ce modèle est désigné sous le nom de "modèle de programmation Edge natif".

## Meilleures pratiques en matière de développement des services de périphérie
{: #best_practices}

Les meilleures pratiques et instructions suivantes vous aident à concevoir et à développer des services de périphérie à utiliser avec {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}).
{:shortdesc}

L'automatisation de l'exécution des services en périphérie est en bien des points différente de celles des services cloud :

* Le nombre de noeuds de périphérie peut être beaucoup plus grand.
* Le réseau des noeuds de périphérie peut s'avérer peu fiable et beaucoup plus lent. Les noeuds de périphérie étant d'ordinaire configurés derrière les pare-feux, les connexions ne peuvent souvent pas être initiées du cloud vers les noeuds de périphérie.
* Les noeuds de périphérie ont des ressources limitées.
* L'élément moteur du fonctionnement des charges de travail en périphérie est la capacité à réduire la latence et à optimiser la bande passante du réseau. Par conséquent, la répartition de la charge de travail par rapport à la position des données constitue un facteur important. 
* En règle générale, les noeuds de périphérie résident dans des emplacements distantes et ne sont pas installés par le personnel des opérations. Une fois un noeud de périphérie installé, il se peut que personne ne soit disponible pour l'administrer.
* Les noeuds de périphérie sont généralement considérés comme des environnements moins sûrs que les serveurs cloud.

Ces différences se traduisent par l'utilisation de techniques différentes pour déployer et gérer des logiciels sur des noeuds de périphérie. {{site.data.keyword.edge_ieam}} est conçu pour la gestion des noeuds de périphérie. Lorsque vous créez des services, respectez les instructions ci-dessous pour vous assurer qu'ils sont conçus pour fonctionner avec des noeuds de périphérie.

## Instructions relatives au développement de services
{: #service_guidelines}


* **Modèle de programmation Cloud natif :** Le modèle de programmation Cloud natif s'inspire de nombreux principes de la programmation cloud native, y compris :

  * Le développement en composants et la conteneurisation de vos charges de travail – construisez votre application autour d'un ensemble de microservices, chacun étant conditionné par groupe logique, et équilibrez ce regroupement afin d'identifier l'emplacement où les différents conteneurs peuvent être les plus efficaces, sur des niveaux différents ou sur des noeuds de périphérie.
  * L'exposition des interfaces de programmation sur vos microservices qui permettent à d'autres parties de votre application de trouver les services dont elles dépendent.
  * La conception d'un couplage flexible entre les microservices pour leur permettre de fonctionner indépendamment les uns des autres et pour éviter d'établir des liens hypothétiques entre les services qui pourraient avoir des répercussions sur la mise à l'échelle, la reprise en ligne et la récupération.
  * Les processus d'intégration et de déploiement continus, associés aux pratiques de développement agile au sein d'une infrastructure DevOps.
  * Consultez les ressources ci-dessous pour en savoir plus sur les pratiques de programmation cloud native :
    * [10 KEY ATTRIBUTES OF CLOUD-NATIVE APPLICATIONS ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://thenewstack.io/10-key-attributes-of-cloud-native-applications/)
    * [Cloud Native Programming  ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://researcher.watson.ibm.com/researcher/view_group.php?id=9957)
    *	[Understanding cloud-native applications  ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://www.redhat.com/en/topics/cloud-native-apps)

* **Disponibilité des services** : Si votre conteneur de services nécessite et utilise d'autres conteneurs de services, votre service doit faire preuve de patience lorsque ces services sont absents. Par exemple, lorsque des conteneurs sont initialement démarrés, même s'ils sont démarrés en remontant à partir de la fin du graphique de dépendance, certains services peuvent démarrer plus rapidement d'autres. Dans ce cas, vos conteneurs de services doivent réessayer plusieurs fois en attendant que les dépendances soient entièrement fonctionnelles. De la même manière, si un conteneur de service est automatiquement mis à jour, il est ensuite redémarré. Vos services doivent être tolérants quant aux interruptions qui se produisent au niveau des services dont ils dépendent.
* **Portabilité** : L'informatique Edge concerne plusieurs niveaux du système, notamment les dispositifs et les clusters de périphérie, ainsi que les emplacements en mode réseau ou métro. L'emplacement final de votre charge de travail conteneurisée en périphérie dépendra de plusieurs facteurs, notamment sa dépendance à l'égard de certaines ressources, telles que les données des capteurs ou des régulateurs, les exigences en matière de latence et la capacité de calcul disponible. Votre charge de travail doit être conçue de manière à pouvoir être placée dans différents niveaux du système, en fonction des besoins du contexte d'exécution de votre application.
* **Orchestration de conteneur** : En plus du point ci-dessus sur la portabilité entre les niveaux, les dispositifs de périphérie devront être utilisés avec un contexte d'exécution Docker natif – sans aucune orchestration de conteneur locale. Les clusters de périphérie et les serveurs de périphérie réseau/métro seront configurés avec Kubernetes pour orchestrer la charge de travail selon les besoins de ressources concurrentes partagées. Vous devez implémenter votre conteneur de manière à éviter toute dépendance explicite sur Docker ou Kubernetes et permettre sa portabilité entre les différents niveaux de l'informatique Edge distribué. 
* **Externalisation des paramètres de configuration** : Utilisez le support intégré fourni par {{site.data.keyword.ieam}} pour externaliser les variables de configuration et les dépendances de ressources afin que celles-ci puissent être fournies et actualisées à l'aide des valeurs spécifiques au noeud sur lequel votre conteneur est déployé.
* **Considérations relatives à la taille** : Vos conteneurs de services doivent être aussi petits que possible afin que les services puissent être déployés sur des réseaux potentiellement lents ou sur des dispositifs de périphérie de petite taille. Pour vous aider à développer des conteneurs de services plus petits, appliquez les techniques suivantes :

  * Utilisez des langages de programmation qui vous aideront à développer des services plus petits :
    * Langages recommandés : go, rust, c, sh
    * Langages acceptables : c++, python, bash
    * Langages à prendre en considération : nodejs, Java et JVM, notamment scala
  * Utilisez des techniques qui vous aideront à générer des images Docker plus petites :
    * Utilisez alpine comme image de base pour {{site.data.keyword.linux_notm}}.
    * Pour installer des packages dans une image alpine, exécutez la commande `apk --no-cache --update add` pour ne pas avoir à stocker la mémoire cache du package, qui est inutile pour l'exécution.
    * Supprimez les fichiers de la même couche Dockerfile (commande) que celle à laquelle ont été ajoutés les fichiers. Si vous utilisez une autre ligne de commande Dockerfile pour supprimer les fichiers de l'image, vous augmenterez la taille de l'image de conteneur. Par exemple, vous pouvez utiliser `&&` pour regrouper les commandes visant à télécharger, utiliser et supprimer des fichiers, dans une même commande `RUN` Dockerfile.
    * N'incluez pas d'outils de génération dans votre image Docker d'exécution. Au rang des meilleures pratiques, il est conseillé d'utiliser la [génération Docker multi-étape (en anglais)![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://docs.docker.com/develop/develop-images/multistage-build/) pour générer les artefacts d'exécution. Choisissez ensuite les artefacts d'exécution requis, tels que les composants exécutables, et copiez-les dans votre image Docker d'exécution.
* **Conception de services autonomes** : Un service ayant besoin d'être envoyé vers des noeuds de périphérie sur le réseau et d'être démarré en toute autonomie, le conteneur de service doit inclure tout ce qui en dépend. Vous devez regrouper ces actifs, tels que les certificats requis, dans le conteneur. Ne soyez pas tributaire de la disponibilité des administrateurs pour ajouter les actifs requis au noeud de périphérie afin qu'un service s'exécute correctement.
* **Confidentialité des données** : Chaque fois que vous déplacez des données privées et sensibles sur le réseau, vous augmentez leur vulnérabilité face aux attaques et aux expositions. Parmi ses nombreux avantages, l'informatique Edge offre la possibilité de conserver les données à l'endroit où elles ont été créées. Conservez cet avantage en protégeant votre conteneur de manière appropriée. Idéalement, ne communiquez pas les données de votre conteneur à d'autres services. Si vous devez absolument transmettre ces données à d'autres services ou niveaux du système, essayez de retirer les données d'identification personnelle, les renseignements médicaux ou les renseignements financiers personnels en utilisant des techniques de brouillage ou d'anonymisation, ou en chiffrant les données avec une clé conservée exclusivement dans le contexte de votre service. 
* **Conception et configuration à des fins d'automatisation** : Les noeuds de périphérie, ainsi que les services qui s'exécutent sur les noeuds, doivent fonctionner au maximum sans intervention manuelle. {{site.data.keyword.ieam}} automatise le déploiement et la gestion des services, mais les services doivent être structurés pour permettre à {{site.data.keyword.ieam}} d'automatiser ces processus pour qu'ils s'opèrent sans intervention humaine. Pour vous aider à concevoir l'automatisation, suivez les instructions ci-dessous :
  * Limitez le nombre de variables d'entrée utilisateur pour un service. Les variables UserInput qui ne sont associées à aucune valeur par défaut dans la définition de service nécessitent que des valeurs soient définies pour chaque noeud de périphérie. Limitez le nombre de variables, ou évitez d'utiliser ces variables, dans la mesure du possible.  
  * Si un service requiert de nombreux paramètres, faites appel à un fichier de configuration pour définir les variables. Incluez une version par défaut du fichier de configuration dans le conteneur de services. Utilisez ensuite le système de gestion des modèles {{site.data.keyword.ieam}} pour permettre à l'administrateur de fournir son propre fichier de configuration et de l'actualiser au fil du temps.
  * **Optimisation des services de plateforme standard** : Les services de plateforme pré-implémentés peuvent répondre à un grand nombre des besoins de votre application. Au lieu de créer ces services de toutes pièces, pensez à réutiliser ceux qui existent et qui sont disponibles. Parmi les sources proposant ces services de plateforme figure IBM Cloud, qui offre un large éventail de fonctionnalités et dont beaucoup ont été développées en s'appuyant sur les pratiques de programmation cloud native, telles que :
    * **Gestion des données** : Utilisez IBM Cloud Pak for Data pour vos besoins en matière de base de données de stockage SQL et non SQL, de stockage en mode bloc ou objet, de services d'apprentissage automatique et d'intelligence artificielle et pour vos exigences en matière de data lake, ou lac de données. 
    * **Sécurité** : Pensez à IBM Cloud Pak for Security pour vos besoins en matière de chiffrement, d'analyse de code et de détection d'intrusion.
    * **Applications** : Pensez à IBM Cloud Pak for Applications pour vos besoins en matière d'application Web, d'infrastructure sans serveur et de structure d'application.
