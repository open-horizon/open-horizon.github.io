---

copyright:
years: 2020
lastupdated: "2020-2-2"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Surveillance des noeuds et services de périphérie
{: #monitoring_edge_nodes_and_services}

[Connectez-vous à la console de gestion](../console/accessing_ui.md) pour surveiller des services et noeuds de périphérie {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}).

* Surveiller les noeuds de périphérie :
  * Le tableau de bord Noeuds est la première page qui s'affiche, et inclut un graphique en anneau qui indique l'état de tous les noeuds de périphérie.
  * Pour afficher tous les noeuds correspondant à un état particulier, cliquez sur cette couleur dans le graphique en anneau. Par exemple, pour afficher tous les noeuds de périphérie comportant des erreurs (le cas échéant), cliquez sur la couleur utilisée pour signaler l'état **Comporte une erreur** (une légende des couleurs décrit les couleurs affectées aux différents états).
  * La liste des noeuds comportant des erreurs s'affiche. Pour explorer en aval un noeud et afficher l'erreur qui vous intéresse, cliquez sur le nom du noeud.
  * Dans la page des détails du noeud qui s'affiche, la section **Erreurs d'agent de noeud** affiche les services comportant des erreurs, le message d'erreur spécifique et l'horodatage.
* Surveiller les services de périphérie :
  * Dans l'onglet **Services**, cliquez sur le service à explorer, qui affiche la page des détails du service de périphérie.
  * Dans la section **Déploiement** de la page des détails, vous pouvez voir les règles et les patterns qui déploient ce service sur des noeuds de périphérie.
* Surveiller les services de périphérie sur un noeud de périphérie :
  * Dans l'onglet **Noeuds**, basculez vers la vue de liste et cliquez sur le noeud de périphérie à explorer.
  * Dans la page des détails du noeud, la section **Services** indique les services de périphérie qui sont en cours d'exécution sur ce noeud de périphérie.
