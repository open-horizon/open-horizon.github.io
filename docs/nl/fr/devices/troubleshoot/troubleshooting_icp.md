---

copyright:
years: 2019
lastupdated: "2019-09-18"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Conseils relatifs au traitement des incidents dans l'environnement {{site.data.keyword.icp_notm}} 
{: #troubleshooting_icp}

Prenez connaissance des questions suivantes pour vous aider à résoudre les problèmes les plus courants dans les environnements {{site.data.keyword.icp_notm}} au sujet d'{{site.data.keyword.edge_devices_notm}}. Ces conseils peuvent vous aider à résoudre les problématiques communes et obtenir des informations en vue de déceler les causes premières.
{:shortdesc}

## Vos données d'identification {{site.data.keyword.edge_devices_notm}} sont-elles configurées correctement pour l'environnement {{site.data.keyword.icp_notm}} ?
{: #setup_correct}

Vous avez besoin d'un compte utilisateur {{site.data.keyword.icp_notm}} pour effectuer une action dans cet environnement {{site.data.keyword.edge_devices_notm}}. Vous avez également besoin d'une clé d'interface de programmation créée à partir de ce compte.

Pour vérifier vos données d'identification {{site.data.keyword.edge_devices_notm}} dans cet environnement, exécutez la commande suivante :

   ```
   hzn exchange user list
   ```
   {: codeblock}

Si une entrée au format JSON, indiquant un ou plusieurs utilisateurs, est renvoyée par Exchange, les données d'identification {{site.data.keyword.edge_devices_notm}} sont correctement configurées.

Si la réponse renvoyée est une erreur, prenez les mesures nécessaires pour dépanner la configuration de vos données d'identification.

Si le message d'erreur indique une clé d'interface de programmation incorrecte, créez une clé qui utilise les commandes ci-dessous.

Voir [Collecte des informations et fichiers nécessaires](../developing/software_defined_radio_ex_full.md#prereq-horizon).
