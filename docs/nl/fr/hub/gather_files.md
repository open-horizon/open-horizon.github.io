---

copyright:
years: 2020
lastupdated: "2020-05-18"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Collecte de fichiers de noeuds de périphérie
{: #prereq_horizon}

Plusieurs fichiers sont nécessaires pour installer l'agent {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) sur vos dispositifs et vos clusters de périphérie et les enregistrer auprès d'{{site.data.keyword.ieam}}. Ce contenu vous permet de regrouper les fichiers nécessaires pour vos noeuds de périphérie. Effectuez les étapes ci-dessous sur un hôte admin connecté au concentrateur de gestion d'{{site.data.keyword.ieam}}.

Les étapes suivantes supposent que vous avez installé les commandes [IBM Cloud Pak CLI (**cloudctl**) et OpenShift client CLI (**oc**)](../cli/cloudctl_oc_cli.md), et que vous exécutez les étapes à partir du répertoire de support d'installation décompressé **ibm-eam-{{site.data.keyword.semver}}-bundle**. Ce script recherche les packages {{site.data.keyword.horizon}} requis dans le fichier **agent/edge-packages-{{site.data.keyword.semver}}.tar.gz** et crée les fichiers de certificat et de configuration de noeuds de périphérie requis.

1. Connectez-vous à votre cluster de concentrateur de gestion avec des données d'identification d'administrateur et l'espace de nom dans lequel vous avez installé {{site.data.keyword.ieam}} :
   ```bash
   cloudctl login -a &amp;TWBLT;cluster-url&gt; -u &amp;TWBLT;cluster-admin-user&gt; -p &amp;TWBLT;cluster-admin-password&gt; -n &amp;TWBLT;namespace&gt; --skip-ssl-validation
   ```
   {: codeblock}

2. Définissez les variables d'environnement suivantes :

   ```bash
   export CLUSTER_URL=https://$(oc get cm management-ingress-ibmcloud-cluster-info -o jsonpath='{.data.cluster_ca_domain}')    oc --insecure-skip-tls-verify=true -n kube-public get secret ibmcloud-cluster-ca-cert -o jsonpath="{.data.ca\.crt}" | base64 --decode &gt; ieam.crt    export HZN_MGMT_HUB_CERT_PATH="$PWD/ieam.crt"    export HZN_FSS_CSSURL=${CLUSTER_URL}/edge-css
   ```
   {: codeblock}

   Définissez les variables d'environnement d'authentification Docker suivantes, en fournissant vos propres variables **ENTITLEMENT_KEY** :
   ```
   export REGISTRY_USERNAME=cp   export REGISTRY_PASSWORD=<ENTITLEMENT_KEY>
   ```
   {: codeblock}

   **Remarque :** obtenez votre clé d'autorisation via [Ma clé IBM](https://myibm.ibm.com/products-services/containerlibrary).

3. Accédez au répertoire **agent** où se trouve **edge-packages-{{site.data.keyword.semver}}.tar.gz** :

   ```bash
   cd agent
   ```
   {: codeblock}

4. Il y a deux manières de rassembler les fichiers pour l'installation des nœuds de périphérie à l'aide du script **edgeNodeFiles.sh**. Choisissez l'une des méthodes suivantes en fonction de vos besoins :

   * Exécutez le script **edgeNodeFiles.sh** pour regrouper les fichiers nécessaires et les placer dans le composant CSS (CSS Cloud Sync Service) du système de gestion de modèles (MMS).

     **Remarque** : le **script edgeNodeFiles.sh** a été installé dans le cadre du package horizon-cli et doit se trouver dans votre chemin.

     ```bash
     HZN_EXCHANGE_USER_AUTH='' edgeNodeFiles.sh ALL -c -p edge-packages-{{site.data.keyword.semver}} -r cp.icr.io/cp/ieam
     ```
     {: codeblock}

     Sur chaque noeud de périphérie, utilisez l'indicateur **-i'css:'** de **agent-install.sh** pour obtenir les fichiers nécessaires à partir de CSS.

     **Remarque** : si vous envisagez d'utiliser des [dispositifs de périphérie SDO](../installing/sdo.md), vous devez exécuter cette forme de la commande `edgeNodeFiles.sh`.

   * Vous pouvez également utiliser **edgeNodeFiles.sh** pour regrouper les fichiers dans un fichier tar :

     ```bash
     edgeNodeFiles.sh ALL -t -p edge-packages-{{site.data.keyword.semver}} -r cp.icr.io/cp/ieam
     ```
     {: codeblock}

     Copiez le fichier tar sur chaque noeud de périphérie et utilisez l'indicateur **-z** de **agent-install.sh** pour obtenir les fichiers nécessaires à partir du fichier tar.

     Si vous n'avez pas encore installé le package **horizon-cli** sur cet hôte, installez-le maintenant. Reportez-vous à [ Configuration après l'installation](post_install.md#postconfig) pour voir un exemple de ce processus.

     Localisez les scripts **agent-install.sh** et **agent-uninstall.sh** qui ont été installés avec le package **horizon-cli**.    Ces scripts sont requis sur chaque noeud de périphérie pendant la configuration (actuellement, **agent-uninstall.sh** ne prend en charge que les clusters de périphérie):
    * Exemple de {{site.data.keyword.linux_notm}} :

     ```
     ls /usr/horizon/bin/agent-{install,uninstall}.sh
     ```
     {: codeblock}

    * Exemple macOS :

     ```
     ls /usr/local/bin/agent-{install,uninstall}.sh
     ```
     {: codeblock}

**Remarque** : **edgeNodeFiles.sh** dispose d'un plus grand nombre d'indicateurs pour contrôler les fichiers collectés et indiquer où ils doivent être placés. Pour afficher tous les indicateurs disponibles, exécutez **edgeNodeFiles.sh -h**

## Etapes suivantes

Avant la configuration des noeuds de périphérie, vous ou vos techniciens de noeud devez créer une clé d'API et collecter d'autres valeurs de variables d'environnement. Suivez les étapes de la section [Création de votre clé d'API](prepare_for_edge_nodes.md).
