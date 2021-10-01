---

copyright:
  years: 2020
lastupdated: "2020-04-9"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Installation du concentrateur de gestion
{: #hub_install_overview}
 
Vous devez installer et configurer un concentrateur de gestion pour pouvoir effectuer les tâches du noeud {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}).

{{site.data.keyword.ieam}} offre des fonctionnalités d'informatique Edge pour vous aider à gérer et à déployer des charges de travail d'un cluster concentrateur vers des instances distantes d'OpenShift® Container Platform 4.2 ou d'autres clusters basés sur Kubernetes.

{{site.data.keyword.ieam}} s'appuie sur IBM Multicloud Management Core 1.2 pour contrôler le déploiement des charges de travail conteneurisées sur des serveurs, des passerelles et des dispositifs de périphérie hébergés par des clusters OpenShift® Container Platform 4.2 dans des emplacements distants.

{{site.data.keyword.ieam}} inclut également une prise en charge du profil Edge Computing Manager. Ce profil peut vous aider à réduire l'utilisation des ressources d'OpenShift® Container Platform 4.2 lorsqu'il est installé pour héberger un serveur de périphérie distant. Le profil installe uniquement les services minimum requis pour assurer une gestion à distance solide de ces environnements de serveurs et des applications critiques pour l'entreprise que vous y hébergez. Grâce à ce profil, vous pouvez continuer à authentifier les utilisateurs, à collecter les données d'événements et de journaux, et à déployer des charges de travail dans un noeud unique ou dans un ensemble de noeuds worker en cluster.

# Installation du concentrateur de gestion

Le processus d'installation d'{{site.data.keyword.edge_notm}} vous accompagne tout au long des étapes d'installation et de configuration ci-dessous :
{:shortdesc}

  - [Récapitulatif de l'installation](#sum)
  - [Dimensionnement](#size)
  - [Prérequis](#prereq)
  - [Processus d'installation](#process)
  - [Configuration après l'installation](#postconfig)
  - [Collecte des informations et fichiers nécessaires](#prereq_horizon)
  - [Désinstallation](#uninstall)

## Récapitulatif de l'installation
{: #sum}

* Déployez les composants du concentrateur de gestion suivants :
  * Interface de programmation d'{{site.data.keyword.edge_devices_notm}} Exchange
  * Agbot d'{{site.data.keyword.edge_devices_notm}}
  * Service de synchronisation Cloud (CSS) d'{{site.data.keyword.edge_devices_notm}}
  * Interface utilisateur d'{{site.data.keyword.edge_devices_notm}}
* Vérifiez que l'installation a réussi.
* Renseignez les exemples de services de périphérie.

## Dimensionnement
{: #size}

Les informations de dimensionnement ci-dessous concernent uniquement les services d'{{site.data.keyword.edge_notm}}, indépendamment des recommandations de dimensionnement associées aux {{site.data.keyword.edge_shared_notm}}, [disponibles ici](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/servers/cluster_sizing.html).

### Exigences relatives au stockage des bases de données

* PostgreSQL Exchange
  * 10 Go par défaut
* PostgreSQL AgBot
  * 10 Go par défaut  
* Service de synchronisation MongoDB Cloud
  * 50 Go par défaut

### Exigences relatives au calcul

Les services qui tirent parti des [ressources de calcul de Kubernetes](https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container) sont planifiés dans les différents noeuds worker disponibles. Au moins trois noeuds worker sont recommandés.

* Les changements de configuration suivants permettent de prendre en charge jusqu'à 10 000 dispositifs de périphérie :

  ```
  exchange:
    replicaCount: 5
    dbPool: 18
    cache:
      idsMaxSize: 11000
    resources:
      limits:
        cpu: 5
  ```

  Remarque : Les instructions permettant d'effectuer ces changements sont disponibles dans la section **Configuration avancée** du fichier [README.md](README.md).

* La configuration par défaut prend en charge jusqu'à 4 000 dispositifs de périphérie et les valeurs totales des chartes relatives aux ressources de calcul par défaut sont les suivantes :

  * Demandes
     * Moins de 5 Go de RAM
     * Moins d'une unité centrale
  * Limites
     * 18 Go de RAM
     * 18 unités centrales


## Prérequis
{: #prereq}

* Installer les [{{site.data.keyword.edge_shared_notm}}](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/servers/install_edge.html)
* **Hôte {{site.data.keyword.linux_notm}} macOS ou Ubuntu**
* [Interface de ligne de commande client OpenShift (oc) 4.2 ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest-4.2/)
* **jq** [Téléchargement ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://stedolan.github.io/jq/download/)
* **git**
* **docker** 1.13+
* **make**
* Les interfaces de ligne de commande suivantes, qui peuvent être obtenues depuis votre installation sur cluster {{site.data.keyword.mgmt_hub}} à l'adresse `https://<CLUSTER_URL_HOST>/common-nav/cli`

    Remarque : Vous devrez peut-être accéder à l'URL ci-dessus deux fois, car un accès non identifié redirige la navigation vers une page d'accueil.

  * Interface de ligne de commande Kubernetes (**kubectl**)
  * Interface de ligne de commande Helm (**helm**)
  * Interface de ligne de commande IBM Cloud (**cloudctl**)

Remarque : Par défaut, les bases de données de développement locales sont mises à disposition dans le cadre de l'installation des chartes. Suivez les instructions du fichier [README.md](README.md) pour mettre à disposition vos propres bases de données. Vous êtes responsable de la sauvegarde ou de la restauration de vos bases de données.

## Processus d'installation
{: #process}

1. Définissez la variable d'environnement **CLUSTER_URL** dont la valeur peut être obtenue dans la sortie d'installation du {{site.data.keyword.mgmt_hub}} :

    ```
    export CLUSTER_URL=<CLUSTER_URL>
    ```
    {: codeblock}

    Sinon, une fois connecté à votre cluster avec **oc login**, exécutez la commande suivante :

    ```
    export CLUSTER_URL=https://$(oc get routes icp-console -o jsonpath='{.spec.host}' -n kube-system)
    ```
    {: codeblock}

2. Connectez-vous à votre cluster avec les privilèges d'administrateur, en sélectionnant **kube-system** comme espace de nom et en indiquant le **mot de passe** que vous avez défini dans le fichier config.yaml lors de l'installation du {{site.data.keyword.mgmt_hub}} :

    ```
    cloudctl login -a $CLUSTER_URL -u admin -p <your-icp-admin-password> -n kube-system --skip-ssl-validation
    ```
    {: codeblock}

3. Définissez l'hôte de registre d'images, configurez l'interface CLI Docker pour valider le certificat auto-signé :

    ```
    export REGISTRY_HOST=$(oc get routes -n openshift-image-registry default-route -o jsonpath='{.spec.host}')

    ```
    {: codeblock}

   Pour macOS :

      1. Approuvez le certificat

      ```
      mkdir -p ~/.docker/certs.d/$REGISTRY_HOST && \
      echo | openssl s_client -showcerts -connect $REGISTRY_HOST:443 2>/dev/null | openssl x509 -outform PEM > ~/.docker/certs.d/$REGISTRY_HOST/ca.crt && \
      sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain ~/.docker/certs.d/$REGISTRY_HOST/ca.crt

      ```
      {: codeblock}
      
      2. Redémarrez le service Docker depuis la barre de menus.

   Pour Ubuntu :

      1. Approuvez le certificat

      ```
      mkdir /etc/docker/certs.d/$REGISTRY_HOST && \
      echo | openssl s_client -showcerts -connect $REGISTRY_HOST:443 2>/dev/null | openssl x509 -outform PEM > /etc/docker/certs.d/$REGISTRY_HOST/ca.crt && \
      service docker restart

      ```
      {: codeblock}

4. Connectez-vous au registre d'images {{site.data.keyword.open_shift_cp}} :

      ```
      docker login $REGISTRY_HOST -u $(oc whoami) -p $(oc whoami -t)
      ```
      {: codeblock}

5. Décomprimez le fichier compressé d'installation {{site.data.keyword.edge_devices_notm}} téléchargé depuis IBM Passport Advantage :

    ```
    tar -zxvf ibm-ecm-4.1.0-x86_64.tar.gz && \
    cd ibm-ecm-4.1.0-x86_64
    ```
    {: codeblock}

6. Chargez le contenu de l'archive dans le catalogue, et les images dans l'espace de nom ibmcom du registre :

    ```
    cloudctl catalog load-archive --archive ibm-ecm-prod-catalog-archive-4.1.0.tgz --registry $REGISTRY_HOST/ibmcom
    ```
    {: codeblock}

  Remarque : Cette édition d'{{site.data.keyword.edge_devices_notm}} ne prend en charge que l'installation à partir d'une ligne de commande et non à partir du catalogue.

7. Extrayez le contenu du fichier compressé vers le répertoire en cours et déplacez-le vers le répertoire créé :

    ```
    tar -O -zxvf ibm-ecm-prod-catalog-archive-4.1.0.tgz charts/ibm-ecm-prod-4.1.0.tgz | tar -zxvf - && \
    cd ibm-ecm-prod
    ```
    {: codeblock}

8. Définissez une classe de stockage par défaut, si ce n'est pas déjà fait :

   ```
   # oc get storageclass
   NAME                                 PROVISIONER                     AGE
   rook-ceph-block-internal             rook-ceph.rbd.csi.ceph.com      8h
   rook-ceph-cephfs-internal (default)  rook-ceph.cephfs.csi.ceph.com   8h
   rook-ceph-delete-bucket-internal     ceph.rook.io/bucket             8h
   ```
   
   Si la ligne comportant la chaîne **(default)** ci-dessus n'apparaît pas, indiquez votre stockage par défaut comme suit :

   ```
   oc patch storageclass <PREFERRED_DEFAULT_STORAGE_CLASS_NAME> -p '{"metadata": {"annotations": {"storageclass.kubernetes.io/is-default-class": "true"}}}'
   ```
   {: codeblock}

9. Consultez les options de configuration, puis suivez les instructions du fichier [README.md](README.md) à la section **Installation de la charte**.

  Le script installe les composants du concentrateur de gestion spécifiés dans la section **Récapitulatif de l'installation**, vérifie l'installation, puis vous renvoie vers la section **Configuration après l'installation** ci-dessous.

## Configuration après l'installation
{: #postconfig}

Exécutez les commande ci-dessous à partir du même hôte que celui sur lequel vous avez initialement exécuté l'installation :

1. Reportez-vous aux étapes 1 et 2 de la section **Processus d'installation** ci-dessus pour vous connecter à votre cluster.
2. Installez l'interface CLI **hzn** avec le programme d'installation Ubuntu {{site.data.keyword.linux_notm}} ou macOS, qui se trouve sous **Horizon-edge-packages**, dans le répertoire OS/ARCH approprié à partir du contenu compressé extrait à l'étape 5 du [processus d'installation](#process) ci-dessus :
  * Exemple Ubuntu {{site.data.keyword.linux_notm}} :

    ```
    sudo dpkg -i horizon-edge-packages/linux/ubuntu/bionic/amd64/horizon-cli*.deb
    ```
    {: codeblock}

  * Exemple macOS :

    ```
    sudo installer -pkg horizon-edge-packages/macos/horizon-cli-*.pkg -target /
    ```
    {: codeblock}

3. Exportez les variables ci-dessous qui sont nécessaires pour les étapes suivantes :

    ```
    export EXCHANGE_ROOT_PASS=$(oc -n kube-system get secret edge-computing -o jsonpath="{.data.exchange-config}" | base64 --decode | jq -r .api.root.password)
    export HZN_EXCHANGE_URL=https://$(oc get routes icp-console -o jsonpath='{.spec.host}' -n kube-system)/ec-exchange/v1
    export HZN_EXCHANGE_USER_AUTH="root/root:$EXCHANGE_ROOT_PASS"
    export HZN_ORG_ID=IBM
    ```
    {: codeblock}

4. Approuvez l'autorité de certification {{site.data.keyword.open_shift_cp}} :
    ```
    oc --namespace kube-system get secret cluster-ca-cert -o jsonpath="{.data['tls\.crt']}" | base64 --decode > /tmp/icp-ca.crt
    ```
    {: codeblock}

  * Exemple Ubuntu {{site.data.keyword.linux_notm}} :
     ```
     sudo cp /tmp/icp-ca.crt /usr/local/share/ca-certificates &&sudo update-ca-certificates
     ```
    {: codeblock}

  * Exemple macOS :

    ```
    sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain /tmp/icp-ca.crt
    ```
    {: codeblock}

5. Créez une paire de clés de signature. Pour plus d'informations, reportez-vous à l'étape 5 de la rubrique [Préparation de la création d'un service de périphérie](../developing/service_containers.md).
    ```
    hzn key create <company-name> <owner@email>
    ```
    {: codeblock}

6. Confirmez que l'installation peut communiquer avec l'interface de programmation Exchange d'{{site.data.keyword.edge_devices_notm}} :
    ```
    hzn exchange status
    ```
    {: codeblock}

7. Renseignez les exemples de services de périphérie :

    ```
    curl https://raw.githubusercontent.com/open-horizon/examples/v4.1/tools/exchangePublishScript.sh | bash -s -- -c $(oc get -n kube-public configmap -o jsonpath="{.items[]..data.cluster_name}")
    ```
    {: codeblock}

8. Exécutez les commandes suivantes pour voir certains des services et certaines des règles qui ont été créés dans le réseau Exchange d'{{site.data.keyword.edge_devices_notm}} :

    ```
    hzn exchange service list IBM/
    hzn exchange pattern list IBM/
    hzn exchange service listpolicy
    ```
    {: codeblock}

9. Si ce n'est pas déjà fait, créez une connexion LDAP en vous servant de la console de gestion d'{{site.data.keyword.open_shift_cp}}. Une fois la connexion LDAP établie, créez une équipe, accordez-lui un accès à un espace de nom et ajoutez les utilisateurs de votre choix à cette équipe. Chaque utilisateur se voit alors accorder le droit de créer des clés d'interface de programmation.

  Remarque : Les clés d'interface de programmation sont utilisées pour l'authentification avec l'interface de ligne de commande d'{{site.data.keyword.edge_devices_notm}}. Pour plus d'informations sur LDAP, voir [Configuring LDAP connection ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://www.ibm.com/support/knowledgecenter/SSFC4F_1.2.0/iam/3.4.0/configure_ldap.html).


## Collecte des informations et des fichiers nécessaires aux dispositifs de périphérie
{: #prereq_horizon}

Plusieurs fichiers sont nécessaires pour installer l'agent d'{{site.data.keyword.edge_devices_notm}} sur vos dispositifs de périphérie et les enregistrer auprès d'{{site.data.keyword.edge_devices_notm}}. Cette section explique comment collecter ces fichiers dans un fichier tar, qui peut ensuite être utilisé sur chacun de vos dispositifs de périphérie.

On suppose que vous avez déjà installé les commandes **cloudctl** et **kubectl** et extrait le contenu du fichier d'installation **ibm-edge-computing-4.1.0-x86_64.tar.gz**, tel que décrit plus haut dans cette page.

1. Reportez-vous aux étapes 1 et 2 de la section **Processus d'installation** ci-dessus pour définir les variables d'environnement suivantes :

   ```
   export CLUSTER_URL=<cluster-url>
   export CLUSTER_USER=<your-icp-admin-user>
   export CLUSTER_PW=<your-icp-admin-password>
   ```
   {: codeblock}

2. Téléchargez la version la plus récente du script **edgeDeviceFiles.sh** :

   ```
   curl -O https://raw.githubusercontent.com/open-horizon/examples/v4.0/tools/edgeDeviceFiles.sh
   chmod +x edgeDeviceFiles.sh
   ```
   {: codeblock}

3. Exécutez le script **edgeDeviceFiles.sh** pour collecter les fichiers requis :

   ```
   ./edgeDeviceFiles.sh <edge-device-type> -t
   ```
   {: codeblock}

   Arguments de commande :
   * Valeurs **<edge-device-type>** prises en charge : **32-bit-ARM** , **64-bit-ARM**, **x86_64-{{site.data.keyword.linux_notm}}**, ou **{{site.data.keyword.macOS_notm}}**
   * **-t** : crée un fichier **agentInstallFiles-&lt;edge-device-type&gt;.tar.gz** contenant tous les fichiers que vous avez collectés. Si cet indicateur n'est pas défini, les fichiers collectés sont placés dans le répertoire de travail.
   * **-k** : crée une clé d'interface de programmation nommée **$USER-Edge-Device-API-Key**. Si cet indicateur n'est pas défini, la clé d'interface de programmation **$USER-Edge-Device-API-Key** fait l'objet d'une recherche parmi les clés existantes et le processus est ignoré si la clé est trouvée.
   * **-d** **<distribution>** : lors d'une installation sous **64-bit-ARM** ou **x86_64-Linux**, vous pouvez spécifier **-d xenial** comme étant la version la plus ancienne d'Ubuntu, au lieu de la version Bionic par défaut. Lors de l'installation sous **32-bits-ARM**, vous pouvez spécifier **-d stretch** au lieu de l'objet buster par défaut. L'indicateur -d est ignoré avec macOS.
   * **-f** **<directory>** : indique le répertoire dans lequel stocker les fichiers collectés. Si ce répertoire n'existe pas, il est créé. Le répertoire de travail est défini par défaut.

4. La commande de l'étape précédente crée un fichier appelé **agentInstallFiles-&lt;edge-device-type&gt;.tar.gz**. Si vous avez d'autres types de dispositifs (architectures différentes), répétez l'étape pour chacun des types.

5. Notez la clé d'interface de programmation qui a été créée par la commande **edgeDeviceFiles.sh**.

6. Maintenant que vous êtes connecté via **cloudctl**, si vous avez besoin de créer des clés d'interface de programmation supplémentaires pour les utilisateurs qui exécutent la commande {{site.data.keyword.horizon}} **hzn** :

   ```
   cloudctl iam api-key-create "<choose-an-api-key-name>" -d "<choose-an-api-key-description>"
   ```
   {: codeblock}

   Dans la sortie de la commande, recherchez la valeur de la clé dans la ligne qui commence par **clé d'API** et sauvegardez-la pour la réutiliser plus tard.

7. Lorsque vous êtes prêt à configurer les dispositifs de périphérie, suivez les instructions de la rubrique [Prise en main d'{{site.data.keyword.edge_devices_notm}}](../getting_started/getting_started.md).

## Désinstallation
{: #uninstall}

Remarque : Des **bases de données locales** sont configurées par défaut et le processus de désinstallation se traduira par la suppression de TOUTES les données persistantes. Assurez-vous d'avoir sauvegardé toutes les données persistantes requises (voir les instructions de sauvegarde dans le fichier README) avant d'exécuter le script de désinstallation. Si vous avez configuré des **bases de données distantes**, les données ne sont pas supprimées lors du processus de désinstallation et doivent être retirées manuellement si besoin.

Revenez à l'emplacement de la charte décompressée dans le cadre de l'installation et exécutez le script de désinstallation fourni. Celui-ci désinstallera la version Helm et toutes les ressources associées. Tout d'abord, connectez-vous au cluster en tant qu'administrateur de cluster via **cloudctl**, et exécutez la commande suivante :

```
ibm_cloud_pak/pak_extensions/uninstall/uninstall-edge-computing.sh <cluster-name>
```
{: codeblock}
