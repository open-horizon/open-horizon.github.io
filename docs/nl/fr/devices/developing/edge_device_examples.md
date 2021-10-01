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

# Exemples de développement de services de périphérie
{: #edge_devices_ex}

Vous trouverez ci-dessous des exemples de développement afin de vous aider à en savoir plus sur la conception de services de périphérie pour {{site.data.keyword.edge_devices_notm}}.
{:shortdesc}

## Exemples
{: #edge_devices_ex_examples}

Chacun de ces exemples de développement aborde des aspects complémentaires du développement de services de périphérie. Pour bénéficier de la meilleure expérience d'apprentissage possible, suivez les exemples dans l'ordre dans lequel ils sont présentés.

* [Livraison d'un conteneur Docker existant en tant que service de périphérie](quickstart_example.md) : Illustre le déploiement d'une image Docker existante en tant que service de périphérie.

* [Création d'un service de périphérie Hello world](developingstart_example.md) : Fournit les bases du développement, du test, de la publication et du déploiement d'un service de périphérie.

* [Unité centrale vers le service {{site.data.keyword.message_hub_notm}}](cpu_msg_example.md) : Montre comment définir les paramètres de configuration d'un service de périphérie, comment spécifier que le service de périphérie nécessite d'autres services de périphérie et comment envoyer des données vers un service de réception des données cloud.

* [Code complet de radio logicielle](software_defined_radio_ex_full.md) : Exemple complet d'une application de périphérie qui accède aux données du détecteur matériel, effectue une opération logique d'IA à la périphérie, centralise les résultats dans un service de réception des données, procède à de nouvelles analyses d'IA à la périphérie et fournit une interface utilisateur pour visualiser les résultats.

* [Service de périphérie utilisant le système de gestion des modèles](mms.md) : Explique comment développer un service de périphérie qui utilise le service de gestion des modèles. Ce dernier fournit de manière asynchrone les mises à jour de fichier vers les services de périphérie sur les noeuds de périphérie, par exemple pour mettre à jour dynamiquement un modèle d'apprentissage automatique chaque fois que le modèle évolue.
