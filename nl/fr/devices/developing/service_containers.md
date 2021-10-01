---

copyright:
years: 2019,2020
lastupdated: "2020-01-28"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Préparation de la création d'un service de périphérie
{: #service_containers}

Utilisez {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) pour développer des services dans les conteneurs {{site.data.keyword.docker}} associés à vos dispositifs de périphérie. Vous pouvez créer vos services de périphérie à l'aide de n'importe quel environnement approprié (bases, langages de programmation, bibliothèques ou utilitaires {{site.data.keyword.linux_notm}}).
{:shortdesc}

Une fois que vous avez envoyé par commande push, signé et publié vos services, {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) a recours à des agents entièrement autonomes sur vos dispositifs de périphérie pour télécharger, valider, configurer, installer et surveiller vos services. 

Les services de périphérie font souvent appel aux services d'ingestion de données cloud pour stocker et traiter les résultats des analyses de périphérie. Ce processus inclut le flux de travail de développement pour le code de cloud et de périphérie.

{{site.data.keyword.ieam}} s'appuie sur le projet [{{site.data.keyword.horizon_open}} ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://github.com/open-horizon/) en open source et utilise la commande `hzn` {{site.data.keyword.horizon}} {{site.data.keyword.linux_notm}} pour exécuter certains processus. 

## Avant de commencer
{: #service_containers_begin}

1. Configurez l'hôte de développement que vous souhaitez utiliser avec {{site.data.keyword.ieam}} en installant l'agent {{site.data.keyword.horizon}} sur votre hôte et en enregistrant ce dernier auprès d'{{site.data.keyword.horizon_exchange}}. Voir [Installation de l'agent {{site.data.keyword.horizon}} sur votre dispositif de périphérie et enregistrement à l'aide de l'exemple Hello world](../installing/registration.md).

2. Créez un ID [Docker Hub ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://hub.docker.com/). Cette opération est nécessaire, car les instructions de cette section impliquent la publication de votre image de conteneur de services dans Docker Hub.

## Procédure
{: #service_containers_procedure}

Remarque : Pour plus d'informations sur la syntaxe de commande, voir [Conventions de ce guide](../../getting_started/document_conventions.md).

1. Lorsque vous avez suivi les étapes de la rubrique [Installation de l'agent {{site.data.keyword.horizon}} sur votre dispositif de périphérie et enregistrement à l'aide de l'exemple Hello world](../installing/registration.md), vous avez défini les données d'identification d'Exchange. Vérifiez que celles-ci sont toujours correctes en testant la commande ci-dessous :

  ```
  hzn exchange user list
  ```
  {: codeblock}

2. Si vous utilisez {{site.data.keyword.macOS_notm}} comme hôte de développement, configurez Docker pour qu'il stocke les données d'identification dans `~/.docker`:

   1. Ouvrez la boîte de dialogue **Preferences** de Docker.
   2. Décochez l'option **Securely store Docker logins in macOS keychain**.
  
     * Si vous ne pouvez pas la décocher, procédez comme suit :
     
       1. Cochez l'option **Include VM in Time Machine backups**. 
       2. Décochez l'option **Securely store Docker logins in macOS keychain**.
       3. (Facultatif) Décochez **Include VM in Time Machine backups**.
       4. Cliquez sur **Apply & Restart**.
   3. Si un fichier `~/.docker/plaintext-passwords.json` existe, supprimez-le.   

3. Connectez-vous à Docker Hub avec l'ID Docker Hub précédemment créé :

  ```
  export DOCKER_HUB_ID="<dockerhubid>"
  echo "<dockerhubpassword>" | docker login -u $DOCKER_HUB_ID --password-stdin
  ```
  {: codeblock}

  Exemple de sortie :
  ```
  WARNING! Your password will be stored unencrypted in ~userName/.docker/config.json.
  Configure a credential helper to remove this warning. See
    https://docs.docker.com/engine/reference/commandline/login/#credentials-store

  Login Succeeded
  ```

4. Créez une paire de clés de signature cryptographique. Celle-ci permet de signer vos services lorsque vous les publiez sur Exchange. 

   Remarque : Vous n'avez besoin de faire cette étape qu'une seule fois.

  ```
  hzn key create "<companyname>" "<youremailaddress>"
  ```
  {: codeblock}
  
  Où `companyname` est utilisé en tant qu'organisation x509 et `youremailaddress` en tant que nom commun x509.

5. Installez les outils de développement suivants :

  Sous **{{site.data.keyword.linux_notm}}** :

  ```
  sudo apt install -y git jq make
  ```
  {: codeblock}

  Sous **{{site.data.keyword.macOS_notm}}** :

  ```
  brew install git jq make
  ```
  {: codeblock}
  
  Remarque : Si vous avez besoin de plus de détails sur l'installation de brew, voir [homebrew ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://brew.sh/).

## Etape suivante
{: #service_containers_what_next}

Utilisez vos données d'identification et votre clé de signature pour mener à bien ces exemples de développement. Ceux-ci vous expliquent comment générer des services de périphérie simples et à comprendre les bases du développement sous {{site.data.keyword.edge_devices_notm}}.
