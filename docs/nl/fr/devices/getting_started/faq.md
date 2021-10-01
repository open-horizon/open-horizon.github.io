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

Vous trouverez dans cette section les réponses aux questions les plus fréquentes au sujet d'{{site.data.keyword.edge_devices_notm}}.
{:shortdesc}

  * [Le logiciel {{site.data.keyword.edge_devices_notm}} est-il en open source ?](#open_sourced)
  * [Comment puis-je développer et déployer des services de périphérie sous {{site.data.keyword.edge_devices_notm}} ?](#dev_dep)
  * [Quelles plateformes matérielles de noeud de périphérie {{site.data.keyword.edge_devices_notm}} prend-il en charge ?](#hw_plat)
  * [Puis-je exécuter n'importe quelle distribution {{site.data.keyword.linux_notm}} sur mes noeuds de périphérie {{site.data.keyword.edge_devices_notm}} ?](#lin_dist)
  * [Quels sont les langages de programmation et environnements pris en charge par {{site.data.keyword.edge_devices_notm}} ?](#pro_env)
  * [Existe-t-il une documentation détaillée pour les API REST fournies par les composants dans {{site.data.keyword.edge_devices_notm}} ?](#rest_doc)
  * [{{site.data.keyword.edge_devices_notm}} utilise-t-il Kubernetes ?](#use_kube)
  * [{{site.data.keyword.edge_devices_notm}} utilise-t-il MQTT ?](#use_mqtt)
  * [Combien cela prend-il de temps après avoir enregistré un noeud de périphérie pour que des accords se forment et que les conteneurs correspondants commencent à fonctionner ?](#agree_run)
  * [Le logiciel {{site.data.keyword.horizon}} et tous les autres logiciels ou données associés à {{site.data.keyword.edge_devices_notm}} peuvent-ils être retirés d'un hôte de noeud de périphérie ?](#sw_rem)
  * [Existe-t-il un tableau de bord permettant de visualiser les accords et les services qui sont actifs sur un noeud de périphérie ?](#db_node)
  * [Que se passe-t-il si le téléchargement d'une image de conteneur est interrompu par une panne de réseau ?](#image_download)
  * [Comment IEAM est-il sécurisé ?](#ieam_secure)
  * [Comment gérer l'IA en périphérie avec des modèles vs l'IA sur le Cloud ?](#ai_cloud)

## Le logiciel {{site.data.keyword.edge_devices_notm}} est-il en open source ?
{: #open_sourced}

{{site.data.keyword.edge_devices_notm}} est un produit IBM. Toutefois, ses composants de base reposent largement sur l'utilisation du projet open source [Open Horizon - EdgeX Project Group ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://wiki.edgexfoundry.org/display/FA/Open+Horizon+-+EdgeX+Project+Group). De nombreux exemples et exemples de programmes disponibles dans le projet {{site.data.keyword.horizon}} fonctionnent avec {{site.data.keyword.edge_devices_notm}}. Pour plus d'informations sur le projet, voir [Open Horizon - EdgeX Project Group ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://wiki.edgexfoundry.org/display/FA/Open+Horizon+-+EdgeX+Project+Group).

## Puis-je développer et déployer des services de périphérie sous {{site.data.keyword.edge_devices_notm}} ?
{: #dev_dep}

Voir [Utilisation de services de périphérie](../developing/using_edge_services.md).

## Quelles plateformes matérielles de noeud de périphérie {{site.data.keyword.edge_devices_notm}} prend-il en charge ?
{: #hw_plat}

{{site.data.keyword.edge_devices_notm}} est compatible avec différentes architectures matérielles via le package binaire {{site.data.keyword.linux_notm}} Debian pour {{site.data.keyword.horizon}} ou via les conteneurs Docker. Pour plus d'informations, voir [Installation du logiciel {{site.data.keyword.horizon}}](../installing/installing_edge_nodes.md).

## Puis-je exécuter n'importe quelle distribution {{site.data.keyword.linux_notm}} sur mes noeuds de périphérie avec {{site.data.keyword.edge_devices_notm}} ?
{: #lin_dist}

Oui, et non.

Vous pouvez développer un logiciel de périphérie qui utilise n'importe quelle distribution {{site.data.keyword.linux_notm}} comme image de base des conteneurs Docker (avec l'instruction Dockerfile `FROM`) si cette base fonctionne sur le noyau hôte {{site.data.keyword.linux_notm}} de vos machines de périphérie. Autrement dit, vous pouvez utiliser n'importe quelle distribution pour vos conteneurs à condition que Docker puisse l'exécuter sur vos hôtes de périphérie.

Toutefois, le système d'exploitation hôte de votre machine de périphérie doit pouvoir exécuter une version récente de Docker ainsi que le logiciel {{site.data.keyword.horizon}}. Actuellement, le logiciel {{site.data.keyword.horizon}} est fourni uniquement sous forme de package Debian pour les machines de périphérie s'exécutant sous {{site.data.keyword.linux_notm}}. Pour les machines Apple Macintosh, une version de conteneur Docker est fournie. L'équipe de développement {{site.data.keyword.horizon}} utilise principalement les distributions Apple Macintosh, ou les distributions Ubuntu ou Raspbian {{site.data.keyword.linux_notm}}.

## Quels sont les langages de programmation et environnements pris en charge par {{site.data.keyword.edge_devices_notm}} ?
{: #pro_env}

{{site.data.keyword.edge_devices_notm}} est compatible avec presque tous les langages de programmation et bibliothèques logicielles que vous pouvez configurer pour s'exécuter dans un conteneur Docker approprié sur vos noeuds de périphérie.

Si votre logiciel nécessite un accès à un matériel spécifique ou à des services de systèmes d'exploitation, vous pouvez avoir besoin d'indiquer les arguments `docker run` équivalents pour prendre en charge cet accès. Vous pouvez spécifier les arguments pris en charge au sein de la section `deployment` du fichier de définition de votre conteneur Docker.

## Existe-t-il une documentation détaillée pour les API REST fournies par les composants dans {{site.data.keyword.edge_devices_notm}} ?
{: #rest_doc}

Oui. Pour plus d'informations, voir [API {{site.data.keyword.edge_devices_notm}}](../installing/edge_rest_apis.md). 

## {{site.data.keyword.edge_devices_notm}} utilise-t-il Kubernetes ?
{: #use_kube}

Oui. {{site.data.keyword.edge_devices_notm}} utilise les services kubernetes [{{site.data.keyword.open_shift_cp}} ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://docs.openshift.com/container-platform/4.4/welcome/index.html).

## {{site.data.keyword.edge_devices_notm}} utilise-t-il MQTT ?
{: #use_mqtt}

{{site.data.keyword.edge_devices_notm}} n'utilise pas MQTT (Message Queuing Telemetry Transport) pour prendre en charge ses propres fonctions internes, mais les programmes que vous déployez sur vos machines de périphérie sont libres d'utiliser MQTT pour leurs propres fins. Des exemples de programme utilisant MQTT et d'autres technologies ({{site.data.keyword.message_hub_notm}} basé sur Apache, par exemple) sont mis à votre disposition pour transférer des données vers et depuis les machines de périphérie.

## Combien cela prend-il de temps après avoir enregistré un noeud de périphérie pour que des accords se forment et que les conteneurs correspondants commencent à fonctionner ?
{: #agree_run}

Normalement, quelques secondes suffisent pour que l'agent et un agbot distant finalisent un accord de déploiement de logiciel. Une fois l'accord conclu, l'agent {{site.data.keyword.horizon}} télécharge (`docker pull`) vos conteneurs dans la machine de périphérie, vérifie leurs signatures cryptographiques avec {{site.data.keyword.horizon_exchange}}, puis les exécute. En fonction de la taille de vos conteneurs et de leur temps de démarrage, cela peut nécessiter entre quelques secondes et plusieurs minutes avant que la machine de périphérie ne soit totalement opérationnelle.

Une fois que vous avez enregistré une machine de périphérie, vous pouvez exécuter la commande `hzn node list` pour afficher l'état d'{{site.data.keyword.horizon}} sur votre machine de périphérie. Lorsque la commande `hzn node list` indique que l'état est `configured`, les agbots {{site.data.keyword.horizon}} sont en mesure de découvrir la machine de périphérie et commencent à former des accords.

Pour observer les phases du processus de négociation d'un accord, utilisez la commande `hzn agreement list`.

Lorsque toute une liste d'accords a été finalisée, exécutez la commande `docker ps` pour afficher les conteneurs en cours d'exécution. Vous pouvez également émettre `docker inspect <container>` pour en savoir plus sur le déploiement d'un conteneur `<container>` spécifique.

## Le logiciel {{site.data.keyword.horizon}} et tous les autres logiciels ou données associés à {{site.data.keyword.edge_devices_notm}} peuvent-ils être retirés d'un hôte de noeud de périphérie ?
{: #sw_rem}

Oui. Si votre machine de périphérie est enregistrée, vous pouvez annuler son enregistrement à l'aide de la commande suivante : 
```
hzn unregister -f -r
```
{: codeblock}

Lorsque la machine de périphérie est désenregistrée, retirez le logiciel {{site.data.keyword.horizon}} installé, comme suit :
```
sudo apt purge -y bluehorizon horizon horizon-cli
```
{: codeblock}

## Existe-t-il un tableau de bord permettant de visualiser les accords et les services qui sont actifs sur un noeud de périphérie ?
{: #db_node}

Vous pouvez utiliser l'interface utilisateur Web d'{{site.data.keyword.edge_devices_notm}} pour visualiser vos noeuds et vos services.

En outre, la commande `hzn` vous permet d'obtenir des informations sur les accords et les services actifs via l'API REST de l'agent {{site.data.keyword.horizon}} sur le noeud de périphérie. Exécutez les commandes suivantes pour extraire les informations appropriées à l'aide de l'interface de ligne de commande :
```
hzn node list
hzn agreement list
docker ps
```
{: codeblock}

## Que se passe-t-il si le téléchargement d'une image de conteneur est interrompu par une panne de réseau ?
{: #image_download}

L'API Docker est utilisée pour télécharger les images de conteneur. Si elle interrompt le téléchargement, elle envoie un message d'erreur à l'agent. En retour, l'agent annule la tentative de téléchargement en cours. Lorsque l'agbot détecte l'annulation, il effectue une nouvelle tentative de déploiement avec l'agent. Lors de la tentative suivante, l'API Docker reprend le téléchargement là où il s'était arrêté. Ce processus se poursuit jusqu'à ce que l'image soit totalement téléchargée et que le déploiement puisse avoir lieu. L'API de liaison Docker est responsable de l'extraction de l'image, et en cas d'échec, l'accord est annulé.

## Comment IEAM est-il sécurisé ?
{: #ieam_secure}

* {{site.data.keyword.ieam}} automatise et utilise l'authentification par clé publique/privée signée cryptographiquement des dispositifs de périphérie lorsqu'il communique avec le concentrateur de gestion {{site.data.keyword.ieam}} à des fins de provisionnement. La communication est toujours établie et contrôlée par le dispositif de périphérie. 
* Le système est associé aux données d'identification du noeud et du service.
* La vérification et l'authenticité logicielle reposent sur le hachage.

Lire l'article [Security at the Edge ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://www.ibm.com/cloud/blog/security-at-the-edge).

## Comment gérer l'IA en périphérie avec des modèles vs l'IA sur le Cloud ?
{: #ai_cloud}

En règle générale, l'intelligence artificielle (IA) en périphérie permet de faire des déductions instantanées avec un temps d'attente inférieur à 0 seconde, afin d'apporter des réponses en temps réel en fonction du scénario d'utilisation et du matériel (par exemple, RaspberryPi, Intel x86 et Nvidia Jetson nano). Avec le système de gestion des modèles d'{{site.data.keyword.ieam}}, vous pouvez déployer des modèles d'IA actualisés sans aucun temps d'indisponibilité.

Lire l'article [Models Deployed at the Edge ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://www.ibm.com/cloud/blog/models-deployed-at-the-edge).
