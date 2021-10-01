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

{{site.data.keyword.ieam}} est basé sur le projet [{{site.data.keyword.horizon_open}}](https://github.com/open-horizon/) open source et utilise la commande `hzn` {{site.data.keyword.horizon}} {{site.data.keyword.linux_notm}} pour exécuter certains processus.

## Avant de commencer
{: #service_containers_begin}

1. Configurez l'hôte de développement que vous souhaitez utiliser avec {{site.data.keyword.ieam}} en installant l'agent {{site.data.keyword.horizon}} sur votre hôte et en enregistrant ce dernier auprès d'{{site.data.keyword.horizon_exchange}}. Voir [Installation de l'agent {{site.data.keyword.horizon}} sur votre dispositif de périphérie et enregistrement à l'aide de l'exemple Hello world](../installing/registration.md).

2. Créez un ID [Docker Hub](https://hub.docker.com/). Cette opération est nécessaire, car les instructions de cette section impliquent la publication de votre image de conteneur de services dans Docker Hub.

## Procédure
{: #service_containers_procedure}

**Remarque** : consultez [Conventions utilisées dans ce document](../getting_started/document_conventions.md) pour plus d'informations sur la syntaxe de commande.

1. Lorsque vous avez suivi les étapes de la rubrique [Installation de l'agent {{site.data.keyword.horizon}} sur votre dispositif de périphérie et enregistrement à l'aide de l'exemple Hello world](../installing/registration.md), vous avez défini les données d'identification d'Exchange. Vérifiez que celles-ci sont toujours correctes en testant la commande ci-dessous :

  ```
  hzn exchange user list
  ```
  {: codeblock}

2. Si vous utilisez {{site.data.keyword.macOS_notm}} comme hôte de développement, placez vos données d'identification de registre de concentrateur Docker dans `~/.docker/plaintext-passwords.json` :

  ```
  export DOCKER_HUB_ID="&amp;TWBLT;yourdockerhubid&gt;" export DOCKER_HUB_PW="&amp;TWBLT;yourdockerhubpassword&gt;" echo "{ \"auths\": { \"https://index.docker.io/v1/\": { \"auth\": \"$(printf "${DOCKER_HUB_ID:?}:${DOCKER_HUB_PW:?}" | base64)\" } } }" &gt; ~/.docker/plaintext-passwords.json

  ```
  {: codeblock}

3. Connectez-vous à Docker Hub avec l'ID Docker Hub précédemment créé :

  ```
  export DOCKER_HUB_ID="&amp;TWBLT;yourdockerhubid&gt;" export DOCKER_HUB_PW="&amp;TWBLT;yourdockerhubpassword&gt;" echo "$DOCKER_HUB_PW" | docker login -u $DOCKER_HUB_ID --password-stdin
  ```
  {: codeblock}

  Exemple de sortie :
  ```
  WARNING! Your password will be stored unencrypted in ~userName/.docker/config.json.
  Configure a credential helper to remove this warning. See     https://docs.docker.com/engine/reference/commandline/login/#credentials-store

  Login Succeeded
  ```

4. Créez une paire de clés de signature cryptographique. Ceci vous permet de signer vos services lorsque vous les publiez sur Exchange. 

   **Remarque** : vous n'avez besoin d'effectuer cette étape qu'une seule fois.

  ```
  hzn key create "<companyname>" "<youremailaddress>"
  ```
  {: codeblock}
  
  Où `companyname` est utilisé en tant qu'organisation x509 et `youremailaddress` en tant que nom commun x509.

5. Installez les outils de développement suivants :

  Sur **{{site.data.keyword.linux_notm}}** (pour les distributions Ubuntu/Debian) :

  ```
  sudo apt install -y git jq make
  ```
  {: codeblock}

  Sous **{{site.data.keyword.macOS_notm}}** :

  ```
  brew install git jq make
  ```
  {: codeblock}
  
  **Remarque** : si vous avez besoin de plus de détails sur l'installation de brew, voir [homebrew](https://brew.sh/).

## Etape suivante
{: #service_containers_what_next}

* Utilisez vos données d'identification et votre clé de signature pour mener à bien ces [exemples de développement](../OH/docs/developing/developing.md). Ceux-ci vous expliquent comment générer des services de périphérie simples et à comprendre les bases du développement sous {{site.data.keyword.edge_notm}}.
* Si vous avez déjà une image Docker que vous souhaitez que {{site.data.keyword.edge_notm}} déploie sur des noeuds de périphérie, consultez la section [Transformation de l'image en service de périphérie](transform_image.md).
