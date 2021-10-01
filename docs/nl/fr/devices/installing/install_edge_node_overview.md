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

# Présentation des noeuds de périphérie
{: #hub_install_overview}

Un noeud de périphérie agit comme un portail utilisateur final pour communiquer avec les autres noeuds du système en cluster. Cela signifie qu'il s'agit d'un membre de cluster, mais qu'il ne fait pas partie de l'environnement de stockage général ni de l'environnement de calcul. Les noeuds de périphérie servent d'interface entre les clusters et le réseau extérieur. Les noeuds de périphérie exécutent généralement des applications client et des outils d'administration de cluster.

Les noeuds de périphérie facilitent les communications entre les utilisateurs finaux et les autres noeuds (par exemple, les noeuds master et worker). Ils permettent aux utilisateurs finaux de contacter les noeuds worker si besoin, en fournissant une interface réseau au cluster sans que la totalité du cluster soit ouverte aux communications.

IEAM permet de gérer les noeuds de périphérie afin de réduire les risques liés au déploiement et de gérer de façon totalement autonome le cycle de vie logiciel du service à l'aide des noeuds de cluster et de dispositif.

Ajoutez un graphique illustrant les étapes détaillées d'installation et de configuration d'un noeud de périphérie (avec les dispositifs et les clusters). 

## Etapes suivantes

Pour obtenir des instructions sur l'installation des noeuds, voir [Installation des noeuds de périphérie](installing_edge_nodes.md).

## Rubriques connexes

* [Installation des noeuds de périphérie](installing_edge_nodes.md)
* [Dispositifs de périphérie](../developing/edge_devices.md)
* [Clusters de périphérie](../developing/edge_clusters.md)
