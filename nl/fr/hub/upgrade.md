---

copyright:
years: 2021
lastupdated: "2021-03-23"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Mises à niveau
{: #hub_upgrade_overview}

## Résumé de la mise à niveau
{: #sum}
* La version actuelle du {{site.data.keyword.ieam}}concentrateur de gestion est {{site.data.keyword.semver}}.
* {{site.data.keyword.ieam}} {{site.data.keyword.semver}} est pris en charge sur {{site.data.keyword.ocp}} version 4.6.

Les mises à niveau vers le même canal Operator Lifecycle Manager (OLM) pour {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}})
Management Hub et [IBM Cloud Platform Common Services](https://www.ibm.com/docs/en/cpfs) se font automatiquement par le biais d'OLM qui est
préinstallé sur votre
cluster de {{site.data.keyword.open_shift_cp}} ({{site.data.keyword.ocp}}).

Les {{site.data.keyword.ieam}} canaux sont définis par **version mineure** (par exemple, v4.2 et v4.3) et mettent automatiquement à jour les **versions de correctifs** (par exemple, 4.2.x). Pour les mises à niveau de **version mineure**, vous devez modifier manuellement les canaux pour lancer la mise à niveau. Pour lancer une mise à niveau de **version mineure**, vous devez être à la dernière **version de correctif** disponible de la **version mineure**précédente, puis les canaux de commutation initieront la mise à niveau.

**Remarques :**
* La rétrogradation n'est pas prise en charge
* La mise à niveau de {{site.data.keyword.ieam}} 4.1.x à 4.2.x n'est pas prise en charge
* En raison d'un [problème {{site.data.keyword.ocp}} connu](https://access.redhat.com/solutions/5493011), si vous avez des `plans d'installation` dans votre projet configuré pour l'approbation manuelle, tous les autres `plans d'installation` de ce projet sont également pris en compte. Vous devez approuver manuellement la mise à niveau de l'opérateur pour continuer.

### Mise à niveau du {{site.data.keyword.ieam}} Concentrateur de gestion de 4.2.x à 4.3.x

1. Effectuez une sauvegarde avant de procéder à la mise à niveau. Pour plus d'informations, voir [Sauvegarde et reprise](../admin/backup_recovery.md).
2. Accédez à la {{site.data.keyword.ocp}} console Web de votre cluster.
3. Accédez à **Opérateurs** &gt; **Opérateurs installés**.
4. Recherchez **{{site.data.keyword.ieam}}** et cliquez sur le résultat du **{{site.data.keyword.ieam}} Concentrateur de gestion** .
5. Accédez à l'onglet **Abonnement** .
6. Cliquez sur le lien **v4.2** dans la section **Canal** .
7. Cliquez sur le bouton d'option pour basculer le canal actif vers **v4.3** pour lancer la mise à niveau.

Pour vérifier que la mise à niveau est terminée, reportez-vous aux [étapes 1 à 5 de la section de post-installation de la vérification d'installation](post_install.md).

Pour mettre à jour les exemples de services, voir [étapes 1 à 3 de la section Configuration post-installation](post_install.md).

## Mise à niveau des nœuds de périphérie

Les nœuds {{site.data.keyword.ieam}} ne sont pas mis à niveau automatiquement. La version d'agent {{site.data.keyword.ieam}} 4.2.1 (2.28.0-338) est prise en charge avec un concentrateur de gestion {{site.data.keyword.ieam}} {{site.data.keyword.semver}}. Afin de mettre à niveau {{site.data.keyword.edge_notm}}l'agent sur vos périphériques et clusters de périphérie, vous devez d'abord placer les {{site.data.keyword.semver}}fichiers des nœuds de périphérie dans le Cloud Sync Service (CSS).

Exécutez les étapes 1 à 3 sous **Installation de la dernière interface de ligne de commande vers votre environnement** même si vous ne souhaitez pas mettre à niveau vos noeuds de périphérie pour l'instant. Cela garantit que les nouveaux noeuds de périphérie seront installés avec le dernier {{site.data.keyword.ieam}} {{site.data.keyword.semver}} code agent.

### Installation de la dernière interface de ligne de commande dans votre environnement
1. Connectez-vous, tirez et extrayez le paquet d'agents avec votre clé d'habilitation via le [registre d'habilitation](https://myibm.ibm.com/products-services/containerlibrary) :
    ```
    docker login cp.icr.io --username cp &amp;TWBAMP;&amp;TWBAMP; \     docker rm -f ibm-eam-{{site.data.keyword.semver}}-bundle; \     docker create --name ibm-eam-{{site.data.keyword.semver}}-bundle cp.icr.io/cp/ieam/ibm-eam-bundle:{{site.data.keyword.anax_ver}} bash &amp;TWBAMP;&amp;TWBAMP; \     docker cp ibm-eam-{{site.data.keyword.semver}}-bundle:/ibm-eam-{{site.data.keyword.semver}}-bundle.tar.gz ibm-eam-{{site.data.keyword.semver}}-bundle.tar.gz &amp;TWBAMP;&amp;TWBAMP; \     tar -zxvf ibm-eam-{{site.data.keyword.semver}}-bundle.tar.gz
    ```
    {: codeblock}
2. Installez l'interface de ligne de commande **hzn** à l'aide des instructions correspondant à votre plateforme prise en charge :
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
3. Suivez les étapes de la section [Collecte de fichiers de nœuds de périphérie](../hub/gather_files.md) pour insérer les fichiers d'installation de l'agent dans le CSS.

### Mise à jour de l'agent sur les nœuds de périphérie
1. Connectez-vous à votre nœud de périphérie en tant que **superutilisateur** sur une unité, ou en tant qu'**admin** sur votre cluster, et définissez les variables d'environnement d'horizon :
```bash
export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>   export HZN_ORG_ID=<votre-organisation-exchange>   export HZN_FSS_CSSURL=https://<entrée-concentrateur-gestion-ieam>/edge-css/
```
{: codeblock}

2. Définissez les variables d'environnement requises en fonction de votre type de cluster (ignorez cette étape si vous mettez à niveau une unité) :

  * **Sur les clusters de périphérie OCP :**
  
    Définissez la classe de stockage que l'agent doit utiliser :
    
    ```bash
    oc get storageclass exportEDGE_CLUSTER_STORAGE_CLASS=<rook-ceph-cephfs-internal>
    ```
    {: codeblock}

    Définissez le nom d'utilisateur du registre comme étant le nom du compte de service que vous avez créé :
    ```bash    oc get serviceaccount -n openhorizon-agent    export EDGE_CLUSTER_REGISTRY_USERNAME=<service-account-name>
    ```
    {: codeblock}

    Définissez le jeton de registre : 
    ```bash    export EDGE_CLUSTER_REGISTRY_TOKEN=`oc serviceaccounts get-token $EDGE_CLUSTER_REGISTRY_USERNAME`
    ```
    {: codeblock}

  * **Sur k3s :**
  
    Invitez le script **agent-install.sh** à utiliser la classe de stockage par défaut :
    
    ```bash
    export EDGE_CLUSTER_STORAGE_CLASS=local-path
    ```
    {: codeblock}

  * **Sur microk8s :**
  
    Invitez le script **agent-install.sh** à utiliser la classe de stockage par défaut :
    
    ```bash
    export EDGE_CLUSTER_STORAGE_CLASS=microk8s-hostpath
    ```
    {: codeblock}

3. Extrayez **agent-install.sh** à partir de CSS :
```bash
curl -u $HZN_ORG_ID/$HZN_EXCHANGE_USER_AUTH $HZN_FSS_CSSURL/api/v1/objects/IBM/agent_files/agent-install.sh/data -o agent-install.sh --insecure && chmod +x agent-install.sh
```
{: codeblock}

4. Exécutez **agent-install.sh** pour obtenir les fichiers mis à jour de CSS et configurez l'agent Horizon :
  *  **Sur les dispositifs de périphérie :**
    ```bash    sudo -s -E ./agent-install.sh -i 'css:' -s
    ```
    {: codeblock}

  *  **Sur les clusters de périphérie :**
    ```bash    ./agent-install.sh -D cluster -i 'css:' -s
    ```
    {: codeblock}

**Remarque** : incluez l'option -s lors de l'exécution de l'installation de l'agent pour ignorer l'enregistrement, ce qui laisse le nœud de périphérie dans le même état qu'avant la mise à niveau.

## Problèmes connus et FAQ
{: #FAQ}

### {{site.data.keyword.ieam}} 4.2
* Il existe un problème connu avec la base de données {{site.data.keyword.ieam}}mongo cssdb locale 4.2.0, qui entraîne une perte de données lorsque le pod est reprogrammé. Si vous utilisez des bases de données locales (par défaut), il est recommandé d'autoriser l'exécution de la mise à niveau {{site.data.keyword.ieam}} {{site.data.keyword.semver}} avant de mettre à niveau le cluster {{site.data.keyword.ocp}} vers la version 4.6. Pour plus d'informations, voir la page [Problèmes connus](../getting_started/known_issues.md).

* Je n'ai pas mis à jour mon cluster {{site.data.keyword.ocp}} au-delà de la version 4.4, et la mise à jour automatique semble être bloquée.

  * Suivez ces étapes pour résoudre ce problème :
  
    1) Sauvegardez le contenu du concentrateur de gestion {{site.data.keyword.ieam}}.  La documentation sur la sauvegarde est disponible dans [Sauvegarde et récupération des données](../admin/backup_recovery.md).
    
    2) Mise à niveau de votre cluster {{site.data.keyword.ocp}} vers la version 4.6.
    
    3) Du fait d'un problème connu avec la base de données {{site.data.keyword.ieam}} 4.2.0 locale **cssdb** mongo, la mise à niveau dans l'**étape 2** réinitialise la base de données.
    
      * Si vous avez utilisé les fonctionnalités MMS de {{site.data.keyword.ieam}} et craignez une perte de données, utilisez la sauvegarde de l'étape ** 1** et suivez la **procédure de restauration** de la page [Sauvegarde et récupération des données](../admin/backup_recovery.md). (**Remarque :** la procédure de restauration entraîne un temps d'interruption).
      
      * Vous pouvez également effectuer les opérations suivantes pour désinstaller et réinstaller l'opérateur {{site.data.keyword.ieam}} si vous n'avez pas utilisé les fonctionnalités MMS, si vous n'êtes pas concerné par la perte de données MMS ou si vous utilisez des bases de données distantes :
      
        1) Accédez à la page Opérateurs installés de votre cluster {{site.data.keyword.ocp}}.
        
        2) Recherchez l'opérateur Concentrateur de gestion IEAM et ouvrez sa page.
        
        3) Dans le menu d'actions à gauche, choisissez de désinstaller l'opérateur.
        
        4) Accédez à la page OperatorHub et réinstallez l'opérateur Concentrateur de gestion IEAM.

* La version {{site.data.keyword.ocp}} 4.5 est-elle prise en charge ?

  * Le concentrateur de gestion {{site.data.keyword.ieam}} n'a pas été test et n'est pas pris en charge sur {{site.data.keyword.ocp}} version 4.5.  Nous suggérons d'effectuer une mise à niveau vers {{site.data.keyword.ocp}} version 4.6.

* Existe-t-il un moyen de refuser cette version du concentrateur de gestion {{site.data.keyword.ieam}} ?

  * Le concentrateur de gestion {{site.data.keyword.ieam}} 4.2.0 ne sera plus pris en charge à partir de la publication  de la version {{site.data.keyword.semver}}.
