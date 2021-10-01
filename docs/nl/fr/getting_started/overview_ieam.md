---

copyright:
years: 2020
lastupdated: "2020-05-11"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Présentation d'{{site.data.keyword.edge_notm}}
{: #overviewofedge}

Cette section fournit une présentation d'{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}).

## Fonctionnalités d'{{site.data.keyword.ieam}}
{: #capabilities}

{{site.data.keyword.ieam}} fournit des fonctions d'informatique Edge pour vous aider à gérer et déployer des charges de travail à partir d'un cluster de concentrateur de gestion vers des dispositifs de périphérie et des instances distantes d'OpenShift Container Platform ou d'autres clusters basés sur Kubernetes.

## Architecture

L'informatique Edge a pour but de mobiliser toutes les disciplines qui ont été créées pour le cloud computing hybride afin de prendre en charge les opérations distantes des fonctions d'informatique Edge. C'est pour cela qu'à été conçu {{site.data.keyword.ieam}}.

Le déploiement d'{{site.data.keyword.ieam}} inclut le concentrateur de gestion qui s'exécute dans une instance d'OpenShift Container Platform, installée dans votre centre de données. Le concentrateur de gestion centralise la gestion de tous vos noeuds de périphérie distants (dispositifs et clusters de périphérie).

Ces noeuds de périphérie peuvent être installés dans des emplacements distants sur site pour pouvoir disposer de vos charges de travail d'application en local, sur les lieux de l’exécution physique de vos opérations métier critiques (exemples : usines, entrepôts, points de vente au détail , centres de distribution, etc.).

Le diagramme ci-dessous illustre la topologie de haut niveau pour une configuration d'informatique Edge standard :

<img src="../OH/docs/images/edge/01_OH_overview.svg" style="margin: 3%" alt="IEAM overview">

Le concentrateur de gestion {{site.data.keyword.ieam}} a été spécialement conçu pour gérer les noeuds de périphérie afin de réduire les risques liés au déploiement, et pour gérer de façon entièrement autonome le cycle de vie des logiciels sur les noeuds de périphérie. Un programme d'installation Cloud installe et gère les composants du concentrateur de gestion {{site.data.keyword.ieam}}. Les développeurs logiciels développent et publient des services de périphérie sur le concentrateur de gestion. Les administrateurs définissent les règles de déploiement qui contrôlent l'emplacement de déploiement des services de périphérie. {{site.data.keyword.ieam}} gère tout le reste.

# Composants
{: #components}

Pour plus d'informations sur les composants fournis avec {{site.data.keyword.ieam}}, voir [Composants](components.md).

## Etapes suivantes

Pour plus d'informations sur l'utilisation de {{site.data.keyword.ieam}} et le développement de services de périphérie, consultez les rubriques répertoriées dans la section {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) [Page d'accueil](../kc_welcome_containers.html).
