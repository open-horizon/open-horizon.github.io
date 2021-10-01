---

copyright:
years: 2019
lastupdated: "2019-07-04"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Exemples de pattern de déploiement
{: #deploy_pattern_ex}

Les exemples de programmes ci-dessous, que vous pouvez charger en tant que patterns de déploiement, sont mis à votre disposition pour vous aider à en savoir davantage sur la mise en route des patterns de déploiement {{site.data.keyword.edge_devices_notm}}.
{:shortdesc}

Essayez d'enregistrer chacun de ces exemples préintégrés pour en savoir plus sur l'utilisation des patterns de déploiement.

Pour enregistrer un noeud de périphérie pour l'un des exemples suivants, vous devez tout d'abord retirer tous les enregistrements existants sur votre noeud de périphérie. Exécutez les commandes ci-dessous sur votre noeud de périphérie pour retirer tous les enregistrements de patterns de déploiement :
```
 hzn unregister
 hzn node list | jq .configstate.state
```
{: codeblock}

Sortie de l'exemple :
```
"unconfigured"
```
{: codeblock}

Si le résultat de la commande affiche `"unconfiguring"` au lieu de `"unconfigured"`, patientez quelques instants et recommencez. Cette commande ne nécessite généralement que quelques secondes. Réexécutez la commande jusqu'à ce que la sortie affiche `"unconfigured"`.

## Exemples
{: #pattern_examples}

* [Hello, world ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://github.com/open-horizon/examples/blob/master/edge/services/helloworld)
  Exemple `"Hello, world."` simple pour vous présenter les patterns de déploiement {{site.data.keyword.edge_devices_notm}}.

* [Pourcentage de charge de travail de l'unité centrale hôte](cpu_load_example.md)
  Exemple de pattern de déploiement qui utilise des données de pourcentage de charge de travail de l'unité centrale et les met à disposition via {{site.data.keyword.message_hub_notm}}.

* [Radio logicielle](software_defined_radio_ex.md)
  Exemple complet qui utilise une station radio, extrait les paroles, puis les convertit en texte. Cet exemple effectue une analyse des sentiments sur le texte et met à disposition les résultats et les données via une interface utilisateur à partir de laquelle vous pouvez afficher les détails des données pour chaque noeud de périphérie. Utilisez cet exemple pour en découvrir davantage sur le traitement de périphérie.
