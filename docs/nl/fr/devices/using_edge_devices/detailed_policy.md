---

copyright:
years: 2019, 2020
lastupdated: "2020-01-22"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Déploiement de services de périphérie
{: #detailed_deployment_policy}

Vous pouvez déployer des règles {{site.data.keyword.ieam}} d'{{site.data.keyword.edge_notm}} à l'aide de règles ou de patterns. Si vous souhaitez obtenir un aperçu plus complet des différents composants système, consultez les sections [Présentation de l'{{site.data.keyword.edge}}](../../getting_started/overview_ieam.md) et [Scénario d'utilisation d'une règle de déploiement](policy_user_cases.md). Pour avoir un exemple concret de règle, consultez la section [Processus CI-CD pour les services de périphérie](../developing/cicd_process.md).

Remarque : Vous pouvez également créer et gérer des règles ou des patterns de déploiement à partir de la console de gestion. Voir [Utilisation de la console de gestion](../getting_started/accessing_ui.md).

La présente section décrit les concepts de règle et de pattern et propose un scénario de cas d'utilisation.

Un administrateur ne pouvant pas gérer des milliers de noeuds de périphérie simultanément, il est impossible de passer à l'échelle supérieure avec des dizaines de milliers de noeuds de périphérie, voire plus. Pour atteindre ce niveau d'échelle, {{site.data.keyword.edge_devices_notm}} utilise des règles pour déterminer où et quand déployer de manière autonome des services et des modèles d'apprentissage automatique. 

Une règle s'exprime par le biais d'un langage flexible qui est ensuite appliqué aux règles de modèle, de noeud, de service et de déploiement. Le langage de règle définit des attributs (appelés `propriétés`) et formule des exigences spécifiques (appelées `contraintes`). L'ensemble permet à chaque partie du système de fournir des données d'entrée au moteur de déploiement d'{{site.data.keyword.edge_devices_notm}}. Avant de pouvoir déployer les services, les contraintes liées aux règles des modèles, des noeuds, des services et des déploiements doivent être vérifiées pour s'assurer que toutes les exigences sont respectées.

Etant donné que les noeuds (sur lesquels les services sont déployés) peuvent être associés à des exigences, la règle d'{{site.data.keyword.edge_devices_notm}} est présentée comme un système de règles bidirectionnel. Les noeuds ne sont pas considérés comme des esclaves dans le système de déploiement des règles d'{{site.data.keyword.edge_devices_notm}}. Par conséquent, les règles fournissent un meilleur contrôle sur le déploiement des services et des modèles que les patterns. Lorsqu'une règle est utilisée, {{site.data.keyword.edge_devices_notm}} recherche les noeuds sur lesquels peut être déployé un service donné et analyse les noeuds existants pour s'assurer qu'ils sont toujours conformes (dans la règle). Un noeud est conforme lorsque les règles du noeud, du service et du déploiement utilisées lors du déploiement initial du service sont toujours en vigueur, ou lorsque les modifications apportées à l'une de ces règles n'ont pas d'incidence sur la compatibilité des règles. L'utilisation d'une règle permet de mieux séparer les problématiques, en permettant aux propriétaires de noeuds de périphérie, aux développeurs de services et aux propriétaires d'entreprise d'articuler de manière indépendante leurs propres règles.

Les règles peuvent être utilisées comme solution de rechange aux patterns de déploiement. Vous pouvez publier des patterns sur le concentrateur d'{{site.data.keyword.ieam}} après qu'un développeur a publié un service de périphérie dans Horizon Exchange. L'interface de ligne de commande hzn intègre des fonctionnalités permettant de lister et de gérer des patterns dans Horizon Exchange, notamment des commandes pour lister, publier, vérifier, mettre à jour et supprimer des patterns de déploiement d'un service. Elle offre également le moyen de répertorier et de supprimer les clés cryptographiques qui sont associées à un pattern de déploiement spécifique.

* [Scénario d'utilisation d'une règle de déploiement](policy_user_cases.md)
* [Utilisation de patterns](using_patterns.md)
