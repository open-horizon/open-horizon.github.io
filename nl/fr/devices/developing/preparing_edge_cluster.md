---

copyright:
years: 2020
lastupdated: "2020-4-24"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Préparation d'un cluster de périphérie
{: #preparing_edge_cluster}

## Avant de commencer

Considérez les points suivants avant de commencer à travailler avec les clusters de périphérie :

* [Prérequis](#preparing_clusters)
* [Collecte des informations et des fichiers nécessaires aux clusters de périphérie](#gather_info)

## Prérequis
{: #preparing_clusters}

Avant d'installer un agent sur un cluster de périphérie :

1. Installez Kubectl dans l'environnement dans lequel s'exécute le script d'installation de l'agent.
2. Installez l'interface de ligne de commande {{site.data.keyword.open_shift}} Client (oc) dans l'environnement dans lequel s'exécute le script d'installation de l'agent.
3. Obtenez un accès administrateur au cluster pour pouvoir créer les ressources de cluster pertinentes.
4. Préparez un registre de cluster de périphérie dans lequel héberger l'image Docker.
5. Installez les commandes **cloudctl** et **kubectl** ainsi que le fichier **ibm-edge-computing-4.1-x86_64.tar.gz** décompressé. Voir [Processus d'installation](../installing/install.md#process).

## Collecte des informations et des fichiers nécessaires aux clusters de périphérie
{: #gather_info}

Vous avez besoin de plusieurs fichiers pour installer et enregistrer vos clusters de périphérie auprès d'{{site.data.keyword.edge_notm}}. Cette section explique comment collecter ces fichiers dans un fichier tar, qui peut ensuite être utilisé sur chacun de vos clusters de périphérie.

1. Définissez les variables d'environnement **CLUSTER_URL** :

    ```
    export CLUSTER_URL=<cluster-url>
   export USER=<your-icp-admin-user>
   export PW=<your-icp-admin-password>
    ```
    {: codeblock}

    Sinon, une fois connecté à votre cluster avec **oc login**, exécutez la commande suivante :

    ```
    export CLUSTER_URL=https://$(oc get routes icp-console -o jsonpath='{.spec.host}')
    ```
    {: codeblock}
    
2. Utilisez les privilèges d'administrateur de cluster pour vous connecter à votre cluster, puis sélectionnez **kube-system** comme espace de nom et indiquez le mot de passe que vous avez défini dans le fichier config.yaml lors du [processus d'installation](../installing/install.md#process) du {{site.data.keyword.mgmt_hub}} :

    ```
    cloudctl login -a $CLUSTER_URL -u admin -p <your-icp-admin-password> -n kube-system --skip-ssl-validation
    ```
    {: codeblock}    

3. Définissez le nom d'utilisateur et le mot de passe du registre, ainsi que le nom complet de l'image dans le registre du cluster de périphérie via les variables d'environnement. La valeur de IMAGE_ON_EDGE_CLUSTER_REGISTRY respecte le format suivant :

    ```
    <registry-name>/<repo-name>/<image-name>.
    ```
    {: codeblock} 

    Si vous utilisez le concentrateur Docker comme registre, indiquez la valeur au format suivant :
    
    ```
    <docker-repo-name>/<image-name>
    ```
    {: codeblock}
    
    Par exemple :
    
    ```
    export EDGE_CLUSTER_REGISTRY_USER=<your-edge-cluster-registry-username>
    export EDGE_CLUSTER_REGISTRY_PW=<your-edge-cluster-registry-password>
    export IMAGE_ON_EDGE_CLUSTER_REGISTRY=<full-image-name-on-your-edge-cluster registry>
    ```
    {: codeblock}
    
4. Téléchargez la version la plus récente du script **edgeDeviceFiles.sh** :

   ```
   curl -O https://raw.githubusercontent.com/open-horizon/examples/master/tools/edgeDeviceFiles.sh chmod +x edgeDeviceFiles.sh
   ```
   {: codeblock}

5. Exécutez le script **edgeDeviceFiles.sh** pour collecter les fichiers requis :

   ```
   ./edgeDeviceFiles.sh x86_64-Cluster -t -r -o <hzn-org-id> -n <node-id> <other flags>
   ```
   {: codeblock}
    
   Un fichier appelé agentInstallFiles-x86_64-Cluster..tar.gz est créé. 
    
**Arguments de commande**
   
Remarque : Spécifiez x86_64-Cluster pour installer l'agent sur un cluster de périphérie.
   
|Arguments de commande|Résultat|
|-----------------|------|
|t                |Crée un fichier **agentInstallFiles-&lt;edge-device-type&gt;.tar.gz** qui contient tous les fichiers que vous avez collectés. Si cet indicateur n'est pas défini, les fichiers collectés sont placés dans le répertoire de travail.|
|f                |Indique le répertoire dans lequel déplacer les fichiers collectés. Si ce répertoire n'existe pas encore, il est créé. Le répertoire de travail est le répertoire par défaut.|
|r                |**EDGE_CLUSTER_REGISTRY_USER**, **EDGE_CLUSTER_REGISTRY_PW** et **IMAGE_ON_EDGE_CLUSTER_REGISTRY** doivent être définis dans une variable d'environnement (étape 1) si vous utilisez cet indicateur. Dans la version 4.1, il s'agit d'un indicateur obligatoire.|
|o                |Spécifie **HZN_ORG_ID**. Cette valeur sert à l'enregistrement du cluster de périphérie.|
|n                |Spécifie **NODE_ID**, qui doit correspondre à la valeur du nom de votre cluster de périphérie. Cette valeur sert à l'enregistrement du cluster de périphérie.|
|s                |Spécifie la classe de stockage du cluster à utiliser par la réservation de volume persistant. La classe de stockage par défaut est "gp2".|
|i                |Version de l'image d'agent à déployer sur le cluster de périphérie.|


Lorsque vous êtes prêt à installer l'agent sur le cluster de périphérie, voir [Installation d'un agent et enregistrement d'un cluster de périphérie](importing_clusters.md).

<!--DELETE DOWN TO    
   The following flags are only supported for x86_64-Cluster:

    * **-r**: specify edge cluster registry if edge cluster is not using Openshift image registry. "EDGE_CLUSTER_REGISTRY_USER", "EDGE_CLUSTER_REGISTRY_PW" and "EDGE_CLUSTER_REGISTRY_REPONAME" need to be set in environment variable (step 1) if using this flag.
    * **-s**: specify cluster storage class to be used by persistent volume claim. Default storage class is "gp2".
    * **-i**: agent image version to be deployed on edge cluster
    * **-o**: specify HZN_ORG_ID. This value is used for edge cluster registration.
    * **-n**: specify NODE_ID. NODE_ID should be the value of your edge cluster name. This value is used for edge cluster registration. 

4. The command in the previous step creates a file that is called **agentInstallFiles-&lt;edge-device-type&gt;.tar.gz**. If you have other types of edge devices (different architectures), repeat the previous step for each type.

5. Take note of the API key that was created and displayed by the **edgeDeviceFiles.sh** command.

6. Now that you are logged in via **cloudctl**, if you need to create additional API keys for users to use with the {{site.data.keyword.horizon}} **hzn** command:

   ```
   cloudctl iam api-key-create "<choose-an-api-key-name>" -d "<choose-an-api-key-description>"
   ```
   {: codeblock}

   In the output of the command look for the key value in the line that starts with **API Key** and save the key value for future use.

7. When you are ready to set up edge devices, follow [Getting started using {{site.data.keyword.edge_devices_notm}}](../getting_started/getting_started.md).

Lily - is the pointer in step 7 above still correct?-->

## Etapes suivantes

* [Installation d'un agent et enregistrement d'un cluster de périphérie](importing_clusters.md)

## Rubriques connexes

* [Clusters de périphérie](edge_clusters.md)
* [Prise en main d'{{site.data.keyword.edge_notm}}](../getting_started/getting_started.md)
* [Processus d'installation](../installing/install.md#process)
