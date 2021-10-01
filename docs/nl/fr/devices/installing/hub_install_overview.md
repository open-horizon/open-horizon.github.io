---

copyright:
years: 2020
lastupdated: "2020-4-24"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Présentation du concentrateur de gestion
{: #hub_install_overview}
 
Vous devez installer et configurer un concentrateur de gestion pour pouvoir effectuer les tâches du noeud IBM Edge Application Manager (IEAM).

IEAM offre des fonctionnalités d'informatique Edge pour vous aider à gérer et à déployer des charges de travail d'un cluster concentrateur vers des instances d'OpenShift® Container Platform 4.3 ou d'autres clusters Kubernetes.

IEAM s'appuie sur IBM Multicloud Management Core 1.2 pour contrôler le déploiement des charges de travail conteneurisées sur des serveurs, des passerelles et des dispositifs de périphérie hébergés par des clusters OpenShift® Container Platform 4.3 dans des emplacements distants.

IEAM inclut également une prise en charge du profil Edge Application Manager. Ce profil peut vous aider à réduire l'utilisation des ressources d'OpenShift® Container Platform 4.3 lorsqu'il est installé pour héberger un serveur de périphérie distant. Le profil installe uniquement les services minimum requis pour assurer une gestion à distance solide de ces environnements de serveurs et des applications critiques pour l'entreprise que vous y hébergez. Grâce à ce profil, vous pouvez continuer à authentifier les utilisateurs, à collecter les données d'événements et de journaux, et à déployer des charges de travail dans un noeud unique ou dans un ensemble de noeuds worker en cluster.

Ajoutez un graphique illustrant les étapes détaillées d'installation et de configuration d'un concentrateur. 

## Etapes suivantes

Pour plus d'informations sur l'installation d'un concentrateur de gestion, voir [Installation du concentrateur de gestion](install.md).

## Rubriques connexes

* [Installation des noeuds de périphérie](installing_edge_nodes.md)
* [Clusters de périphérie](../developing/edge_clusters.md)
* [Dispositifs de périphérie](../developing/edge_devices.md)
