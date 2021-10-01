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

# Sauvegarde et récupération des données
{: #data_backup}

## Sauvegarde et récupération d'{{site.data.keyword.open_shift_cp}}

Pour plus d'informations sur la sauvegarde et la récupération des données à l'échelle du cluster, voir :

* [{{site.data.keyword.open_shift_cp}} 4.6 backup etcd](https://docs.openshift.com/container-platform/4.6/backup_and_restore/backing-up-etcd.html).

## Sauvegarde et récupération d'{{site.data.keyword.edge_notm}}

Les procédures de sauvegarde {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) varient légèrement selon le type de base de données que vous utilisez. Ces bases de données sont désignées comme locales ou distantes.

|Type de base de données|Description|
|-------------|-----------|
|Locale|Ces bases de données sont installées (par défaut) comme ressources {{site.data.keyword.open_shift}} sur votre cluster {{site.data.keyword.open_shift}}.|
|Distante|Ces bases de données sont mises à disposition en accès externe au cluster. Par exemple, il peut s'agir de bases de données sur site ou d'une offre SaaS d'un fournisseur cloud.|

Le paramètre qui permet de définir les bases de données à utiliser doit être configuré lors de l'installation dans votre ressource personnalisée en tant que **spec.ieam\_local\_databases**, et a la valeur true par défaut.

Pour déterminer la valeur active d'une instance {{site.data.keyword.ieam}} installée, exécutez la commande suivante :

```
oc get eamhub ibm-edge -o jsonpath="{.spec.ieam_local_databases}"
```
{: codeblock}

Pour plus d'informations sur la configuration des bases de données distantes pendant l'installation, voir la page [Configuration](../hub/configuration.md).

**Remarque** : le basculement entre les bases de données locales et distantes n'est pas pris en charge.

Le produit {{site.data.keyword.edge_notm}} ne sauvegarde pas automatiquement vos données. Il vous incombe de sauvegarder ce contenu à la fréquence de votre choix, et de stocker ces sauvegardes dans un emplacement sécurisé distinct afin de garantir la reprise. Les sauvegardes confidentielles contiennent du contenu d'authentification codé pour les connexions à la base de données et pour l'authentification des applications du {{site.data.keyword.mgmt_hub}}. Elles doivent par conséquent être stockées dans un emplacement sécurisé.

Si vous utilisez vos propres bases de données distantes, veillez à ce qu'elles soient également sauvegardées. La présente documentation n'explique pas comment sauvegarder les données contenues dans ces bases de données distantes.

{{site.data.keyword.ieam}}La procédure de sauvegarde nécessite également l'utilisation de `yq` v3.

### Procédure de sauvegarde

1. Vérifiez que vous êtes connecté à votre cluster avec les droits d'administrateur du cluster **cloudctl login** ou **oc login**. Sauvegardez vos données et vos valeurs confidentielles à l'aide du script suivant, qui se trouve sur le support décompressé utilisé lors de l'installation du {{site.data.keyword.mgmt_hub}} à partir de Passport Advantage. Exécutez le script avec **-h** en respectant la syntaxe suivante :

   ```
   ibm-eam-{{site.data.keyword.semver}}-bundle/tools/ieam-backup.sh -h
   ```
   {: codeblock}
   
   **Remarque ** : le script de sauvegarde détecte automatiquement le type des bases de données utilisées lors de l'installation.

   * Si vous exécutez l'exemple suivant sans options, il génère un dossier dans lequel le script a été exécuté. Le dossier applique le schéma de nommage **ibm-edge-backup/$DATE/** :

     ```
     ibm-eam-{{site.data.keyword.semver}}-bundle/tools/ieam-backup.sh
     ```
     {: codeblock}
     
     Si une installation de **base de données locale** a été détectée, votre sauvegarde contient un répertoire **customresource**, un répertoire **databaseresources** et deux fichiers yaml :

     ```
     $ ls -l ibm-edge-backup/20201026_215107/   	  drwxr-xr-x  3 staff  staff     96 Oct 26 21:51 customresource 	  drwxr-xr-x  5 staff  staff    160 Oct 26 21:51 databaseresources 	  -rw-r--r--  1 staff  staff  13308 Oct 26 21:51 ibm-edge-auth-secret.yaml 	  -rw-r--r--  1 staff  staff   3689 Oct 26 21:51 ibm-edge-config.yaml
     ```
     {: codeblock}
     
	  Si une installation de **base de données distante** a été détectée, vous voyez les mêmes répertoires que ceux répertoriés précédemment, mais par contre 3 fichiers yaml au lieu de 2.
	  
	  ```
     $ ls -l ibm-edge-backup/20201026_215518/ 	  drwxr-xr-x  3 staff  staff     96 Oct 26 21:55 customresource 	  drwxr-xr-x  3 staff  staff     96 Oct 26 21:55 databaseresources 	  -rw-r--r--  1 staff  staff  10477 Oct 26 21:55 ibm-edge-auth-overrides.yaml 	  -rw-r--r--  1 staff  staff  11433 Oct 26 21:55 ibm-edge-auth-secret.yaml 	  -rw-r--r--  1 staff  staff   2499 Oct 26 21:55 ibm-edge-config.yaml
     ```
     {: codeblock}

### Procédure de restauration

**Remarque** : lorsque des bases de données locales sont utilisées ou sont restaurées dans des bases de données distantes nouvelles ou vides, la conception autonome de {{site.data.keyword.ieam}}entraîne un problème connu lorsqu'elle restaure les sauvegardes sur le {{site.data.keyword.mgmt_hub}}.

Pour restaurer des sauvegardes, vous devez installer un {{site.data.keyword.mgmt_hub}}. Si vous installez ce nouveau concentrateur sans indiquer **ieam\_maintenance\_mode** lors de l'installation initiale, tous les nœuds de périphérie déjà enregistrés risquent d'être désenregistrés. Vous devrez les enregistrer à nouveau.

Cela est dû au fait que le noeud de périphérie reconnaît qu'il n'existe plus dans Exchange, car la base de données est maintenant vide. Activez **ieam\_maintenance\_mode** pour éviter ce problème en démarrant les ressources de la base de données uniquement pour le {{site.data.keyword.mgmt_hub}}. Cela permet de terminer la restauration avant le démarrage des ressources restantes du {{site.data.keyword.mgmt_hub}}, qui utilisent ces bases de données.

**Remarques** : 

* Lorsque votre fichier **Custom Resource** a été sauvegardé, il a été automatiquement modifié de façon à entrer en mode **ieam\_maintenance\_mode** immédiatement après une nouvelle application au cluster.

* Les scripts de restauration déterminent automatiquement le type de base de données précédemment utilisé en examinant le fichier **\<path/to/backup\>/customresource/eamhub-cr.yaml**.

1. En tant qu'administrateur de cluster, vérifiez que vous êtes connecté à votre cluster avec **cloudctl login** ou **oc login**, et qu'une copie de sauvegarde valide a été créée. Sur le cluster où la sauvegarde a été effectuée, exécutez la commande suivante pour supprimer la ressource personnalisée **eamhub** (en supposant que le nom par défaut de **ibm-edge** a été utilisé pour la ressource personnalisée) :
	```
	oc delete eamhub ibm-edge
	```
	{: codeblock}

2. Vérifiez que **ieam\_maintenance\_mode** est défini correctement :
	```
	yq r ibm-edge-backup/20201026_215738/customresource/eamhub-cr.yaml 'items[0].spec.ieam_maintenance_mode'
	```
	{: codeblock}
	

3. Exécutez le script `ieam-restore-k8s-resources.sh` avec l'option **-f** définie de façon à pointer vers votre sauvegarde :
	```
	ibm-eam-{{site.data.keyword.semver}}-bundle/tools/ieam-restore-k8s-resources.sh -f ibm-edge-backup/20201026_215738/
	```
	{: codeblock}

   Attendez que toutes les bases de données et les pods SDO fonctionnent avant de poursuivre.
	
4. Modifiez la ressource personnalisée **ibm-edge** pour mettre l'opérateur en pause :
	```
	oc patch eamhub ibm-edge --type merge --patch '{"spec":{"pause_control_loop": true}}'
	```
	{: codeblock}

5. Modifiez l'objet StatefulSet **ibm-edge-sdo** pour augmenter le nombre de répliques à **1** :
	```
	oc patch statefulset ibm-edge-sdo --type merge --patch '{"spec":{"replicas": 1}}'
	```
	{: codeblock}

6. Attendez que le pod **ibm-edge-sdo-0** soit en cours d'exécution :
	```
   	watch oc get pods -n ibm-edge | grep ibm-edge-sdo-0
   	```
	{: codeblock}

7. Exécutez le script `ieam-restore-data.sh` avec l'option **-f** définie pour pointer sur votre sauvegarde :
	```
	ibm-eam-{{site.data.keyword.semver}}-bundle/tools/ieam-restore-data.sh -f ibm-edge-backup/20201026_215738/
	```
	{: codeblock}
	
8. Une fois que l'exécution du script terminée et vos données restaurées, retirez la pause sur l'opérateur pour reprendre la boucle de contrôle :
	```
	oc patch eamhub ibm-edge --type merge --patch '{"spec":{"pause_control_loop": false}}'
	```
	{: codeblock}

