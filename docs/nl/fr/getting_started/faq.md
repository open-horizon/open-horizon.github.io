---

copyright:
years: 2020
lastupdated: "2020-04-21"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Foire aux questions
{: #faqs}

Vous trouverez ici les réponses à des questions fréquemment posées (FAQ) sur {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}).
{:shortdesc}

  * [Existe-t-il un moyen de créer un environnement autonome à des fins de développement ?](#one_click)
  * [Le logiciel {{site.data.keyword.ieam}} est-il en open source ?](#open_sourced)
  * [Comment puis-je utiliser {{site.data.keyword.ieam}} pour développer et déployer des services de périphérie ?](#dev_dep)
  * [Quelles plateformes matérielles de noeud de périphérie {{site.data.keyword.ieam}} prend-il en charge ?](#hw_plat)
  * [Puis-je exécuter n'importe quelle distribution {{site.data.keyword.linux_notm}} sur mes noeuds de périphérie {{site.data.keyword.ieam}} ?](#lin_dist)
  * [Quels sont les langages de programmation et environnements pris en charge par {{site.data.keyword.ieam}} ?](#pro_env)
  * [Existe-t-il une documentation détaillée pour les API REST fournies par les composants dans {{site.data.keyword.ieam}} ?](#rest_doc)
  * [{{site.data.keyword.ieam}} utilise-t-il Kubernetes ?](#use_kube)
  * [{{site.data.keyword.ieam}} utilise-t-il MQTT ?](#use_mqtt)
  * [Après avoir enregistré un noeud de périphérie, combien de temps faut-il normalement pour que les accords soient créés et que les conteneurs correspondants commencent à s'exécuter ?](#agree_run)
  * [Le logiciel {{site.data.keyword.horizon}} et tous les autres logiciels ou données associés à {{site.data.keyword.ieam}} peuvent-ils être retirés d'un hôte de noeud de périphérie ?](#sw_rem)
  * [Existe-t-il un tableau de bord permettant de visualiser les accords et les services qui sont actifs sur un noeud de périphérie ?](#db_node)
  * [Que se passe-t-il si le téléchargement d'une image de conteneur est interrompu par une panne de réseau ?](#image_download)
  * [Comment {{site.data.keyword.ieam}} est-il sécurisé ?](#ieam_secure)
  * [Comment gérer l'IA en périphérie avec des modèles vs l'IA sur le Cloud ?](#ai_cloud)

## Existe-t-il un moyen de créer un environnement autonome à des fins de développement ?
{: #one_click}

Vous pouvez installer le concentrateur de gestion open source (sans la console de gestion {{site.data.keyword.ieam}}) à l'aide du programme d'installation "tout-en-un" pour les développeurs. Le programme d'installation tout-en-un crée un concentrateur de gestion complet mais minimal, qui ne convient pas à un usage en production. Il configure également un exemple de noeud de périphérie. Cet outil permet aux développeurs de composants open source de démarrer rapidement sans qu'il soit nécessaire de configurer un {{site.data.keyword.ieam}} concentrateur de gestion de production complet. Pour plus d'informations sur le programme d'installation tout-en-un, voir [Open Horizon - Devops](https://github.com/open-horizon/devops/tree/master/mgmt-hub).

## Le logiciel {{site.data.keyword.ieam}} est-il en open source ?
{: #open_sourced}

{{site.data.keyword.ieam}} est un produit IBM. Toutefois, ses composants de base reposent largement sur l'utilisation du projet open source [Open Horizon - EdgeX Project Group](https://wiki.edgexfoundry.org/display/FA/Open+Horizon+-+EdgeX+Project+Group). De nombreux exemples et exemples de programmes disponibles dans le projet {{site.data.keyword.horizon}} fonctionnent avec {{site.data.keyword.ieam}}. Pour plus d'informations sur le projet, voir [Open Horizon - EdgeX Project Group](https://wiki.edgexfoundry.org/display/FA/Open+Horizon+-+EdgeX+Project+Group).

## Comment développer et déployer des services de périphérie avec {{site.data.keyword.ieam}} ?
{: #dev_dep}

Voir [Utilisation de services de périphérie](../using_edge_services/using_edge_services.md).

## Quelles plateformes matérielles de noeud de périphérie {{site.data.keyword.ieam}} prend-il en charge ?
{: #hw_plat}

{{site.data.keyword.ieam}} est compatible avec différentes architectures matérielles via le package binaire {{site.data.keyword.linux_notm}} Debian pour {{site.data.keyword.horizon}} ou via les conteneurs Docker. Pour plus d'informations, voir [Installation du logiciel {{site.data.keyword.horizon}}](../installing/installing_edge_nodes.md).

## Puis-je exécuter n'importe quelle distribution {{site.data.keyword.linux_notm}} sur mes noeuds de périphérie avec {{site.data.keyword.ieam}} ?
{: #lin_dist}

Oui, et non.

Vous pouvez développer un logiciel de périphérie qui utilise n'importe quelle distribution {{site.data.keyword.linux_notm}} comme image de base des conteneurs Docker (s'il utilise l'instruction Dockerfile `FROM`), si cette base fonctionne sur le noyau hôte {{site.data.keyword.linux_notm}} sur vos noeuds de périphérie. Autrement dit, vous pouvez utiliser n'importe quelle distribution pour vos conteneurs à condition que Docker puisse l'exécuter sur vos hôtes de périphérie.

Toutefois, le système d'exploitation de l'hôte de votre noeud de périphérie doit pouvoir exécuter une version récente de Docker et pouvoir exécuter le logiciel {{site.data.keyword.horizon}}. Actuellement, le logiciel {{site.data.keyword.horizon}} est fourni uniquement sous forme de packages Debian et RPM pour les noeuds de périphérie qui exécutent {{site.data.keyword.linux_notm}}. Pour les machines Apple Macintosh, une version de conteneur Docker est fournie. L'équipe de développement {{site.data.keyword.horizon}} utilise principalement les distributions Apple Macintosh, ou les distributions Ubuntu ou Raspbian {{site.data.keyword.linux_notm}}.

En outre, l'installation du package RPM a été testée sur des noeuds de périphérie configurés avec Red Hat Enterprise Linux (RHEL) Version 8.2.

## Quels sont les langages de programmation et environnements pris en charge par {{site.data.keyword.ieam}} ?
{: #pro_env}

{{site.data.keyword.ieam}} est compatible avec presque tous les langages de programmation et bibliothèques logicielles que vous pouvez configurer pour s'exécuter dans un conteneur Docker approprié sur vos noeuds de périphérie.

Si votre logiciel nécessite un accès à un matériel spécifique ou à des services de systèmes d'exploitation, vous pouvez avoir besoin d'indiquer les arguments `docker run` équivalents pour prendre en charge cet accès. Vous pouvez spécifier les arguments pris en charge au sein de la section `deployment` du fichier de définition de votre conteneur Docker.

## Existe-t-il une documentation détaillée pour les API REST fournies par les composants dans {{site.data.keyword.ieam}} ?
{: #rest_doc}

Oui. Pour plus d'informations, voir [API {{site.data.keyword.ieam}}](../api/edge_rest_apis.md). 

## {{site.data.keyword.ieam}} utilise-t-il Kubernetes ?
{: #use_kube}

Oui. {{site.data.keyword.ieam}} utilise les services [{{site.data.keyword.open_shift_cp}})](https://docs.openshift.com/container-platform/4.6/welcome/index.md) Kubernetes.

## {{site.data.keyword.ieam}} utilise-t-il MQTT ?
{: #use_mqtt}

{{site.data.keyword.ieam}} n'utilise pas MQTT (Message Queuing Telemetry Transport) pour prendre en charge ses propres fonctions internes. Néanmoins, les programmes que vous déployez sur vos noeuds de périphérie sont libres d'utiliser MQTT pour leurs propres fins. Il existe des exemples de programmes utilisant MQTT et d'autres technologies (par exemple, {{site.data.keyword.message_hub_notm}}, basé sur Apache Kafka) pour transporter des données vers et depuis des noeuds de périphérie.

## Combien cela prend-il de temps après avoir enregistré un noeud de périphérie pour que des accords se forment et que les conteneurs correspondants commencent à fonctionner ?
{: #agree_run}

Normalement, quelques secondes suffisent pour que l'agent et un agbot distant finalisent un accord de déploiement de logiciel. Ensuite, l'agent {{site.data.keyword.horizon}} télécharge (avec `docker pull`) vos conteneurs vers le noeud de périphérie. Vérifiez leurs signatures cryptographiques avec {{site.data.keyword.horizon_exchange}}, puis exécutez-les. Selon la taille de vos conteneurs, et le temps nécessaire à leur démarrage et leur activation, un délai allant de quelques secondes à plusieurs minutes peut s'écouler avant que le noeud de périphérie ne soit entièrement opérationnel.

Lorsque vous avez enregistré un noeud de périphérie, vous pouvez exécuter la commande `hzn node list` pour afficher l'état d'{{site.data.keyword.horizon}} sur votre noeud de périphérie. Lorsque la commande `hzn node list` indique que l'état est `configured` (configuré), les agbots {{site.data.keyword.horizon}} peuvent reconnaître le noeud de périphérie et commencer à créer des contrats.

Pour observer les phases du processus de négociation d'un accord, utilisez la commande `hzn agreement list`.

Lorsque toute une liste d'accords a été finalisée, exécutez la commande `docker ps` pour afficher les conteneurs en cours d'exécution. Vous pouvez également émettre `docker inspect <container>` pour en savoir plus sur le déploiement d'un conteneur `<container>` spécifique.

## Le logiciel {{site.data.keyword.horizon}} et tous les autres logiciels ou données associés à {{site.data.keyword.ieam}} peuvent-ils être retirés d'un hôte de noeud de périphérie ?
{: #sw_rem}

Oui. Si votre noeud de périphérie est enregistré, annulez son enregistrement en exécutant la commande suivante : 
```
hzn unregister -f -r
```
{: codeblock}

Une fois le noeud de périphérie désenregistré, vous pouvez retirer le logiciel {{site.data.keyword.horizon}} installé. Par exemple, pour les systèmes basés sur Debian, exécutez la commande suivante :
```
sudo apt purge -y bluehorizon horizon horizon-cli
```
{: codeblock}

## Existe-t-il un tableau de bord permettant de visualiser les accords et les services qui sont actifs sur un noeud de périphérie ?
{: #db_node}

Vous pouvez utiliser l'interface utilisateur Web d'{{site.data.keyword.ieam}} pour visualiser vos noeuds et vos services.

En outre, la commande `hzn` vous permet d'obtenir des informations sur les accords et les services actifs via l'API REST de l'agent {{site.data.keyword.horizon}} sur le noeud de périphérie. Exécutez les commandes suivantes pour extraire les informations appropriées à l'aide de l'interface de ligne de commande :

```
hzn node list hzn agreement list docker ps
```
{: codeblock}

## Que se passe-t-il si le téléchargement d'une image de conteneur est interrompu par une panne de réseau ?
{: #image_download}

L'API Docker est utilisée pour télécharger les images de conteneur. Si elle interrompt le téléchargement, elle envoie un message d'erreur à l'agent. En retour, l'agent annule la tentative de téléchargement en cours. Lorsque l'agbot détecte l'annulation, il effectue une nouvelle tentative de déploiement avec l'agent. Lors de la tentative suivante, l'API Docker reprend le téléchargement là où il s'était arrêté. Ce processus se poursuit jusqu'à ce que l'image soit totalement téléchargée et que le déploiement puisse avoir lieu. L'API de liaison de Docker est responsable de l'extraction de l'image. En cas d'échec, l'accord est annulé.

## Comment {{site.data.keyword.ieam}} est-il sécurisé ?
{: #ieam_secure}

* {{site.data.keyword.ieam}} automatise et utilise l'authentification par clé publique/privée signée cryptographiquement des dispositifs de périphérie lorsqu'il communique avec le concentrateur de gestion {{site.data.keyword.ieam}} à des fins de provisionnement. La communication est toujours initiée et contrôlée par le noeud de périphérie.
* Le système est associé aux données d'identification du noeud et du service.
* La vérification et l'authenticité logicielle reposent sur le hachage.

Lire l'article [Security at the Edge](https://www.ibm.com/cloud/blog/security-at-the-edge).

## Comment gérer l'IA en périphérie avec des modèles vs l'IA sur le Cloud ?
{: #ai_cloud}

En général, l'IA en périphérie vous permet d'exécuter une analyse machine instantanée avec un temps d'attente inférieur à la seconde, ce qui permet une réponse en temps réel basée sur le cas d'utilisation et le matériel (par exemple, RaspberryPi, Intel x86 et Nvidia Jetson nano). Avec le système de gestion des modèles d'{{site.data.keyword.ieam}}, vous pouvez déployer des modèles d'IA actualisés sans aucun temps d'indisponibilité.

Lire l'article [Models Deployed at the Edge](https://www.ibm.com/cloud/blog/models-deployed-at-the-edge).
