---

copyright:
  years: 2019, 2020
lastupdated: "2020-2-06"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Hello world
{: #policy}

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) utilise des règles pour mettre en place et gérer les déploiements de services et de modèles, donnant ainsi aux administrateurs la flexibilité et l'évolutivité nécessaires pour travailler avec un grand nombre de noeuds de périphérie. La règle {{site.data.keyword.ieam}} est une solution de rechange aux patterns de déploiement. Elle assure une meilleure séparation des problématiques, en permettant aux propriétaires de noeuds de périphérie, aux développeurs de code de service et aux propriétaires fonctionnels d'articuler les règles de manière indépendante.

Il s'agit d'un exemple "Hello, world" minimal qui vous présente les règles de déploiement d'{{site.data.keyword.edge_notm}}.

Types de règles Horizon :

* Règle de noeud (fournie lors de l'enregistrement par le propriétaire du noeud)
* Règle de service (applicable à un service publié dans Exchange)
* Règle de déploiement (parfois appelée règle métier, qui correspond plus ou moins à un pattern de déploiement)

Les règles exercent un plus grand contrôle sur la définition des accords entre les agents Horizon sur les noeuds de périphérie et les agbots Horizon.

## Utilisation d'une règle afin d'exécuter un exemple hello world
{: #helloworld_policy}

Voir [Using the Hello World Example Edge Service with Deployment Policy](https://github.com/open-horizon/examples/blob/master/edge/services/helloworld/PolicyRegister.md#using-the-hello-world-example-edge-service-with-deployment-policy).

## Rubriques connexes

* [Déploiement de services de périphérie](../using_edge_services/detailed_policy.md)
* [Scénario d'utilisation d'une règle de déploiement](../using_edge_services/policy_user_cases.md)
