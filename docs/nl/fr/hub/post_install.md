---

copyright:
years: 2020
lastupdated: "2020-10-28"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Configuration après l'installation

## Prérequis

* [Interface de ligne de commande d'IBM Cloud Pak (**cloudctl**) et interface de ligne de commande du client OpenShift (**oc**)](../cli/cloudctl_oc_cli.md)
* [**jq**](https://stedolan.github.io/jq/download/)
* [**git**](https://git-scm.com/downloads)
* [**docker**](https://docs.docker.com/get-docker/) version 1.13 ou ultérieure
* **make**

## Vérification de l'installation

1. Effectuez les étapes de la section [Installation {{site.data.keyword.ieam}}](online_installation.md)
2. Vérifiez que l'état de tous les pods de l'espace de nom {{site.data.keyword.ieam}} est **En cours d'exécution** ou **Terminé** :

   ```
   oc get pods
   ```
   {: codeblock}

   Voici un exemple de ce qui doit être vu avec les bases de données locales et le gestionnaire de secrets locaux installé. Quelques redémarrages d'initialisation sont attendus, mais des redémarrages multiples indiquent généralement un problème.. :
   ```
   $ oc get pods    NAME                                           READY   STATUS      RESTARTS   AGE    create-agbotdb-cluster-j4fnb                   0/1     Completed   0          88m    create-exchangedb-cluster-hzlxm                0/1     Completed   0          88m    ibm-common-service-operator-68b46458dc-nv2mn   1/1     Running     0          103m    ibm-eamhub-controller-manager-7bf99c5fc8-7xdts 1/1     Running     0          103m    ibm-edge-agbot-5546dfd7f4-4prgr                1/1     Running     0          81m    ibm-edge-agbot-5546dfd7f4-sck6h                1/1     Running     0          81m    ibm-edge-agbotdb-keeper-0                      1/1     Running     0          88m    ibm-edge-agbotdb-keeper-1                      1/1     Running     0          87m    ibm-edge-agbotdb-keeper-2                      1/1     Running     0          86m    ibm-edge-agbotdb-proxy-7447f6658f-7wvdh        1/1     Running     0          88m    ibm-edge-agbotdb-proxy-7447f6658f-8r56d        1/1     Running     0          88m    ibm-edge-agbotdb-proxy-7447f6658f-g4hls        1/1     Running     0          88m    ibm-edge-agbotdb-sentinel-5766f666f4-5qm9x     1/1     Running     0          88m    ibm-edge-agbotdb-sentinel-5766f666f4-5whgr     1/1     Running     0          88m    ibm-edge-agbotdb-sentinel-5766f666f4-9xjpr     1/1     Running     0          88m    ibm-edge-css-5c59c9d6b6-kqfnn                  1/1     Running     0          81m    ibm-edge-css-5c59c9d6b6-sp84w                  1/1     Running     0          81m
   ibm-edge-css-5c59c9d6b6-wf84s                  1/1     Running     0          81m    ibm-edge-cssdb-server-0                        1/1     Running     0          88m    ibm-edge-exchange-b6647db8d-k97r8              1/1     Running     0          81m    ibm-edge-exchange-b6647db8d-kkcvs              1/1     Running     0          81m    ibm-edge-exchange-b6647db8d-q5ttc              1/1     Running     0          81m    ibm-edge-exchangedb-keeper-0                   1/1     Running     1          88m    ibm-edge-exchangedb-keeper-1                   1/1     Running     0          85m    ibm-edge-exchangedb-keeper-2                   1/1     Running     0          84m    ibm-edge-exchangedb-proxy-6bbd5b485-cx2v8      1/1     Running     0          88m    ibm-edge-exchangedb-proxy-6bbd5b485-hs27d      1/1     Running     0          88m    ibm-edge-exchangedb-proxy-6bbd5b485-htldr      1/1     Running     0          88m    ibm-edge-exchangedb-sentinel-6d685bf96-hz59z   1/1     Running     1          88m    ibm-edge-exchangedb-sentinel-6d685bf96-m4bdh   1/1     Running     0          88m    ibm-edge-exchangedb-sentinel-6d685bf96-mxv2b   1/1     Running     1          88m    ibm-edge-sdo-0                                 1/1     Running     0          81m    ibm-edge-ui-545d694f6c-4rnrf                   1/1     Running     0          81m    ibm-edge-ui-545d694f6c-97ptz                   1/1     Running     0          81m    ibm-edge-ui-545d694f6c-f7bf6                   1/1     Running     0          81m
   Ibm-edge-vault-0 1/1 En cours d'exécution 0 81m ibm-edge-vault-bootstrap-k8km9 0/1 Terminé 0 80 m
   ```
   {: codeblock}

   **Remarques** :
   * Pour plus d'informations sur les pods dont l'état est **En attente** en raison de problèmes de ressources ou de planification, consultez la page [Dimensionnement du cluster](cluster_sizing.md). Elle inclut des informations sur la façon de réduire les coûts de planification des composants.
   * Pour plus d'informations sur toute autre erreur, voir [dépannage](../admin/troubleshooting.md).
3. Vérifiez que l'état de tous les pods de l'espace de nom **ibm-common-services** est **En cours d'exécution** ou **Terminé** :

   ```
   oc get pods -n ibm-common-services
   ```
   {: codeblock}

4. Connectez-vous, tirez et extrayez le paquet d'agents avec votre clé d'habilitation via le [registre d'habilitation](https://myibm.ibm.com/products-services/containerlibrary) :
    ```
    docker login cp.icr.io --username cp &amp;TWBAMP;&amp;TWBAMP; \     docker rm -f ibm-eam-{{site.data.keyword.semver}}-bundle; \     docker create --name ibm-eam-{{site.data.keyword.semver}}-bundle cp.icr.io/cp/ieam/ibm-eam-bundle:{{site.data.keyword.anax_ver}} bash &amp;TWBAMP;&amp;TWBAMP; \     docker cp ibm-eam-{{site.data.keyword.semver}}-bundle:/ibm-eam-{{site.data.keyword.semver}}-bundle.tar.gz ibm-eam-{{site.data.keyword.semver}}-bundle.tar.gz &amp;TWBAMP;&amp;TWBAMP; \     tar -zxvf ibm-eam-{{site.data.keyword.semver}}-bundle.tar.gz &amp;TWBAMP;&amp;TWBAMP; \     cd ibm-eam-{{site.data.keyword.semver}}-bundle/tools
    ```
    {: codeblock}
5. Validez l'état de l'installation :
    ```
    ./service_healthcheck.sh
    ```
    {: codeblock}

    Voir l'exemple de sortie suivant :
    ```
    $ ./service_healthcheck.sh ==Running service verification tests for IBM Edge Application Manager== SUCCESS: IBM Edge Application Manager Exchange API is operational  SUCCESS: IBM Edge Application Manager Cloud Sync Service is operational SUCCESS: IBM Edge Application Manager Agbot database heartbeat is current SUCCESS: IBM Edge Application Manager SDO API is operational SUCCESS: IBM Edge Application Manager UI is properly requiring valid authentication ==All expected services are up and running==
    ```

   * En cas d'échecs de la commande **service_healthcheck.sh**, si vous rencontrez des problèmes lors de l'exécution des commandes ci-dessous ou en cas de problèmes lors de l'exécution, voir la rubrique  [Traitement des incidents](../admin/troubleshooting.md).

## Configuration après l'installation
{: #postconfig}

Le processus suivant doit s'exécuter sur un hôte prenant en charge l'installation de l'interface de ligne de commande **hzn**, qui peut actuellement être installée sur un hôte Debian/apt Linux, amd64 Red Hat/rpm Linux ou macOS. Ces étapes utilisent le même support que ceux qui ont été téléchargés à partir de PPA dans la section Vérification de l'installation.

1. Installez l'interface de ligne de commande **hzn** à l'aide des instructions correspondant à votre plateforme prise en charge :
  * Accédez au répertoire **agent** et décompressez les fichiers de l'agent :
    ```
    cd ibm-eam-{{site.data.keyword.semver}}-bundle/agent &amp;TWBAMP;&amp;TWBAMP; \ tar -zxvf edge-packages-{{site.data.keyword.semver}}.tar.gz
    ```
    {: codeblock}

    * Exemple Debian {{site.data.keyword.linux_notm}} :
      ```
      sudo apt-get install ./edge-packages-{{site.data.keyword.semver}}/linux/deb/amd64/horizon-cli*.deb
      ```
      {: codeblock}

    * Exemple Red Hat {{site.data.keyword.linux_notm}} :
      ```
      sudo dnf install -yq ./edge-packages-{{site.data.keyword.semver}}/linux/rpm/x86_64/horizon-cli-*.x86_64.rpm
      ```
      {: codeblock}

    * Exemple macOS :
      ```
      sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain edge-packages-{{site.data.keyword.semver}}/macos/pkg/x86_64/horizon-cli.crt && \       sudo installer -pkg edge-packages-{{site.data.keyword.semver}}/macos/pkg/x86_64/horizon-cli-*.pkg -target /
      ```
      {: codeblock}

2. Exécutez le script de post-installation. Ce script effectue toutes les opérations d'initialisation nécessaires pour créer votre première organisation. (Les organisations sont la méthode utilisée par {{site.data.keyword.ieam}} pour séparer les ressources et les utilisateurs pour activer le partage de services. Au départ, cette première organisation est suffisante. Vous pouvez configurer d'autres organisations ultérieurement. Pour plus d'informations, voir [Multi-location](../admin/multi_tenancy.md)).

   **Remarque** : **IBM** et **root** sont des organisations à usage interne et ne peuvent pas être choisies comme organisation initiale. Le nom d'une organisation ne peut pas contenir de caractères de soulignement (_), de virgules (,), d'espaces ( ), de guillemets simples (') ou de points d'interrogation ( ?)..

   ```
   ./post_install.sh <choisir-nom-org>
   ```
   {: codeblock}

3. Exécutez la commande suivante pour imprimer le lien de la console de gestion {{site.data.keyword.ieam}} pour votre installation :
   ```
   echo https://$(oc get cm management-ingress-ibmcloud-cluster-info -o jsonpath='{.data.cluster_ca_domain}')/edge
   ```
   {: codeblock}

## Authentification 

L'authentification utilisateur est requise lors de l'accès à la console de gestion {{site.data.keyword.ieam}}. Un compte administrateur initial a été créé par cette installation et peut être imprimé à l'aide de la commande suivante :
```
echo "$(oc -n ibm-common-services get secret platform-auth-idp-credentials -o jsonpath='{.data.admin_username}' | base64 --decode) // $(oc -n ibm-common-services get secret platform-auth-idp-credentials -o jsonpath='{.data.admin_password}' | base64 --decode)"
```
{: codeblock}

Vous pouvez utiliser ce compte administrateur pour l'authentification initiale, et pouvez également [configurer LDAP](https://www.ibm.com/support/knowledgecenter/SSHKN6/iam/3.x.x/configure_ldap.html) en accédant au lien de la console de gestion imprimé par la commande suivante :
```
echo https://$(oc get cm management-ingress-ibmcloud-cluster-info -o jsonpath='{.data.cluster_ca_domain}')
```
{: codeblock}

Lorsque vous avez établi une connexion LDAP, créez une équipe, accordez à l'équipe l'accès à l'espace de nom dans lequel l'opérateur {{site.data.keyword.edge_notm}} a été déployé et ajoutez des utilisateurs à cette équipe. Chaque utilisateur se voit alors accorder le droit de créer des clés d'interface de programmation.

Les clés d'API sont utilisées pour l'authentification avec l'interface de ligne de commande {{site.data.keyword.edge_notm}} et les droits associés aux clés d'API sont identiques à ceux de l'utilisateur avec lequel ils sont générés.

Si vous n'avez pas créé de connexion LDAP, vous pouvez toujours créer des clés d'API à l'aide des données d'identification initiales de l'administrateur, mais vous devez savoir que la clé d'API dispose des privilèges **Administrateur de cluster**.

## Etape suivante

Suivez le processus sur la page [Collecte de fichiers de nœuds de périphérie](gather_files.md) pour préparer le support d'installation de vos nœuds de périphérie.
