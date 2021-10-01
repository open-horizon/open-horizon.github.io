---

copyright:
years: 2019, 2020
lastupdated: "2020-02-10"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Composants

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) est livré avec plusieurs composants.
{:shortdesc}

Consultez le tableau suivant pour obtenir une description des composants d'{{site.data.keyword.ieam}} :

|Composant|Version|Description|
|---------|-------|----|
|[IBM Cloud Platform Common Services](https://www.ibm.com/docs/en/cpfs)|3.6.x|Il s'agit d'un ensemble de composants de base installés automatiquement dans le cadre de l'installation de l'opérateur {{site.data.keyword.ieam}}.|
|Agbot|{{site.data.keyword.anax_ver}}|Instances de bot d'accord (agbot) qui sont créées au niveau central et sont responsables du déploiement des charges de travail et des modèles d'apprentissage automatique sur {{site.data.keyword.ieam}}.|
|MMS |1.5.3-338|Le système de gestion des modèles (MMS) facilite le stockage, la distribution et la sécurité des modèles, des données et d'autres packages de métadonnées requis par les services de périphérie. Les noeuds de périphérie peuvent ainsi envoyer et recevoir des modèles et des métadonnées depuis et vers le Cloud, en toute simplicité.|
|API Exchange|2.87.0-531|Exchange offre une interface de programmation REST qui regroupe toutes les définitions (patterns, règles, services, etc.) utilisées par les autres composants dans {{site.data.keyword.ieam}}.|
|Console de gestion|1,5.0-578|Interface utilisateur Web utilisée par les administrateurs d'{{site.data.keyword.ieam}} pour afficher et gérer les autres composants d'{{site.data.keyword.ieam}}.|
|Secure Device Onboard|1.11.11-441|Le composant SDO permet d'utiliser une technologie créée par Intel pour simplifier et sécuriser la configuration des dispositifs de périphérie et les associer à un concentreur de gestion de dispositifs.|
|Agent de cluster|{{site.data.keyword.anax_ver}}|Il s'agit d'une image de conteneur, qui est installée en tant qu'agent dans les clusters de périphérie pour permettre à {{site.data.keyword.ieam}} de gérer la charge de travail des nœuds.|
|Agent de dispositif|{{site.data.keyword.anax_ver}}|Composant installé sur des dispositifs de périphérie pour permettre à {{site.data.keyword.ieam}} de gérer la charge de travail du noeud.|
|Gestionnaire des secrets|1,0,0-168|Le gestionnaire de secrets est le référentiel des secrets déployés sur les périphériques, permettant aux services de recevoir en toute sécurité les informations d'identification utilisées pour s'authentifier auprès de leurs dépendances en amont.|
