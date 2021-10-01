---

copyright:
years: 2020
lastupdated: "2020-10-13"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Création de votre clé d'API
{: #prepare_for_edge_nodes}

Ce contenu explique comment créer une clé d'API et collecter quelques fichiers et valeurs de variables d'environnement nécessaires lorsque vous configurez des noeuds de périphérie. Procédez comme suit sur un hôte qui peut se connecter à votre cluster de concentrateur de gestion {{site.data.keyword.ieam}}.

## Avant de commencer

* Si vous n'avez pas encore installé **cloudctl**, voir [Installation de cloudctl, oc et kubectl](../cli/cloudctl_oc_cli.md).
* Contactez votre administrateur {{site.data.keyword.ieam}} pour obtenir les informations dont vous avez besoin pour vous connecter au concentrateur de gestion via **cloudctl**.

## Procédure

Si vous avez configuré une connexion LDAP, vous pouvez utiliser les données d'identification des utilisateurs ajoutés pour vous connecter et créer des clés d'API, ou vous pouvez utiliser les données d'identification d'administrateur initiales imprimées à l'aide de la commande suivante :
```
echo "$(oc -n ibm-common-services get secret platform-auth-idp-credentials -o jsonpath='{.data.admin_username}' | base64 --decode) // $(oc -n ibm-common-services get secret platform-auth-idp-credentials -o jsonpath='{.data.admin_password}' | base64 --decode)"
```
{: codeblock}

1. Utilisez `cloudctl` pour vous connecter au concentrateur de gestion {{site.data.keyword.ieam}}. Indiquez l'utilisateur pour lequel vous souhaitez créer une clé d'API :

   ```bash
   cloudctl login -a <cluster-url> -u <user> -p <password> --skip-ssl-validation
   ```
   {: codeblock}

2. Chaque utilisateur qui met en place des noeuds de périphérie doit disposer d'une clé d'API. Vous pouvez utiliser la même clé d'API pour configurer tous vos noeuds de périphérie (elle n'est pas sauvegardée sur les noeuds de périphérie). Créez une clé d'API :

   ```bash
   cloudctl iam api-key-create "<choose-an-api-key-name>" -d "<choose-an-api-key-description>"
   ```
   {: codeblock}

   Recherchez la valeur de la clé dans la sortie de la commande. Il s'agit de la ligne commençant par **API Key**. Sauvegardez la valeur de clé pour une utilisation ultérieure car vous ne pouvez pas la demander ultérieurement au système.

3. Contactez votre administrateur {{site.data.keyword.ieam}} pour obtenir de l'aide sur la définition de ces variables d'environnement :

  ```bash
  export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>   export HZN_ORG_ID=<your-exchange-organization>   mgmtHubIngress=$(oc get cm management-ingress-ibmcloud-cluster-info -o jsonpath='{.data.cluster_ca_domain}')   export HZN_FSS_CSSURL=https://$mgmtHubIngress/edge-css/   echo "export HZN_FSS_CSSURL=$HZN_FSS_CSSURL"
  ```
  {: codeblock}

## Etapes suivantes

Lorsque vous êtes prêt à configurer des noeuds de périphérie, procédez comme indiqué dans [Installation des noeuds de périphérie](../installing/installing_edge_nodes.md).

