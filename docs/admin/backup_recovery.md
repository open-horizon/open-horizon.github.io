---

copyright:
years: 2020 - 2022
lastupdated: "2022-03-17"
title: Backup
description: Data Backup and recovery
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Data backup and recovery
{: #data_backup}

## {{site.data.keyword.open_shift_cp}} backup and recovery

For more information about cluster-wide data backup and recovery, see:

* [{{site.data.keyword.open_shift_cp}} 4.6 backup etcd](https://docs.openshift.com/container-platform/4.6/backup_and_restore/backing-up-etcd.html).

If you have not downloaded the {{site.data.keyword.semver}} bundle, use the following commands with your [Entitled Registry Key](https://myibm.ibm.com/products-services/containerlibrary):

```
docker login cp.icr.io --username cp && \
docker rm -f ibm-eam-{{site.data.keyword.semver}}-bundle; \
docker create --name ibm-eam-{{site.data.keyword.semver}}-bundle cp.icr.io/cp/ieam/ibm-eam-bundle:{{site.data.keyword.anax_ver}} bash && \
docker cp ibm-eam-{{site.data.keyword.semver}}-bundle:/ibm-eam-{{site.data.keyword.semver}}-bundle.tar.gz ibm-eam-{{site.data.keyword.semver}}-bundle.tar.gz && \
tar -zxvf ibm-eam-{{site.data.keyword.semver}}-bundle.tar.gz
```
{: codeblock}

## Prerequisites

* `yq` (must be v3)

## {{site.data.keyword.edge_notm}} backup and recovery


{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) backup procedures differ slightly depending on the type of databases you are using. These databases are referred as local or remote.

|Database type|Description|
|-------------|-----------|
|Local|These databases are installed (by default) as {{site.data.keyword.open_shift}} resources onto your {{site.data.keyword.open_shift}} cluster|
|Remote|These databases are provisioned external to the cluster. For example, these databases can be on-premises or a cloud provider SaaS offering.|

The configuration setting that governs which databases are used is set during installation time in your custom resource as **spec.ieam\_local\_databases**, and is true by default.

To determine the active value for an installed {{site.data.keyword.ieam}} instance, run:

```
oc get eamhub ibm-edge -o jsonpath="{.spec.ieam_local_databases}"
```
{: codeblock}

For more information about configuring remote databases at installation time, see the [Configuration](../hub/configuration.md) page.

**Note**: Switching between local and remote databases is not supported.

The {{site.data.keyword.edge_notm}} product does not automatically back up your data. You are responsible for backing up content at your chosen cadence and storing those backups in a separate secure location to ensure recoverability. Because secret backups contain encoded authentication content for database connections and {{site.data.keyword.mgmt_hub}} application authentication, store them in a secure location.

If you are using your own remote databases, ensure that those databases are backed up. This documentation does not describe how to back up the data of those remote databases.

### Backup procedure

1. Ensure you are connected to your cluster with either **cloudctl login** or **oc login** as a cluster administrator. Validate you have enough space to contain the backup by running the following commands to check database usage:
   ```
   oc exec -ti ibm-edge-agbotdb-keeper-0 -- sh -c 'du -sh /stolon-data' && \
   oc exec -ti ibm-edge-exchangedb-keeper-0 -- sh -c 'du -sh /stolon-data' && \
   oc exec -ti ibm-edge-cssdb-server-0 -c mongod -- sh -c 'du -sh /data/db'
   ```
   {: codeblock}
2. Back up your data and secrets with the following script (Run the script with **-h** for usage):

   ```
   ibm-eam-{{site.data.keyword.semver}}-bundle/tools/ieam-backup.sh -h
   ```
   {: codeblock}
   
   **Note**: The backup script automatically detects the type of databases that are used during installation.

   * If you run the following example with no options, it generates a folder where the script ran. The folder follows this naming pattern **ibm-edge-backup/$DATE/**:

     ```
     ibm-eam-{{site.data.keyword.semver}}-bundle/tools/ieam-backup.sh
     ```
     {: codeblock}
     
     If a **local database** installation was detected, your backup contains a **customresource** directory, a **databaseresources** directory, and two yaml files:

     ```
     $ ls -l ibm-edge-backup/20201026_215107/
  	  drwxr-xr-x  3 staff  staff     96 Oct 26 21:51 customresource
	  drwxr-xr-x  5 staff  staff    160 Oct 26 21:51 databaseresources
	  -rw-r--r--  1 staff  staff  13308 Oct 26 21:51 ibm-edge-auth-secret.yaml
	  -rw-r--r--  1 staff  staff   3689 Oct 26 21:51 ibm-edge-config.yaml
     ```
     {: codeblock}
     
	  If a **remote database** installation was detected, you see the same directories that are listed previously, but three yaml files instead of 2.
	  
	  ```
     $ ls -l ibm-edge-backup/20201026_215518/
	  drwxr-xr-x  3 staff  staff     96 Oct 26 21:55 customresource
	  drwxr-xr-x  3 staff  staff     96 Oct 26 21:55 databaseresources
	  -rw-r--r--  1 staff  staff  10477 Oct 26 21:55 ibm-edge-auth-overrides.yaml
	  -rw-r--r--  1 staff  staff  11433 Oct 26 21:55 ibm-edge-auth-secret.yaml
	  -rw-r--r--  1 staff  staff   2499 Oct 26 21:55 ibm-edge-config.yaml
     ```
     {: codeblock}

### Restore Procedure

**Note**: When local databases are used or are restored to new or empty remote databases, {{site.data.keyword.ieam}}'s autonomous design results in a known challenge when it restores backups to the {{site.data.keyword.mgmt_hub}}.

To restore backups, an identical {{site.data.keyword.mgmt_hub}} must be installed. If this new hub is installed without entering **ieam\_maintenance\_mode** during the initial installation, it is likely that all edge nodes, which were previously registered, unregister themselves. This requires them to be reregistered.

This situation occurs when the edge node recognizes that it no longer exists in the exchange because the database is now empty. Enable **ieam\_maintenance\_mode** to avoid this by starting the database resources only for the {{site.data.keyword.mgmt_hub}}. This allows restoration to complete before the remaining {{site.data.keyword.mgmt_hub}} resources (which use those databases) are started.

**Notes**: 

* Restore backups to the same {{site.data.keyword.ieam}} version where the backup was taken; for example, a 4.2 {{site.data.keyword.ieam}} backup can only be restored to a 4.2 {{site.data.keyword.ieam}} installation.

* When your **Custom Resource** file was backed up, it was automatically modified to enter **ieam\_maintenance\_mode** immediately upon reapplication to the cluster.

* The restore scripts examine the **\[path/to/backup\]/customresource/eamhub-cr.yaml** file to determine what type of database was used previously.
	

1. As a cluster administrator, ensure that you are connected to your cluster with **cloudctl login** or **oc login** and that a valid backup was created. On the cluster where the backup was made, run the following command to delete the **eamhub** custom resource (this assumes the default name of **ibm-edge** was used for the custom resource):
	```
	oc delete eamhub ibm-edge
	```
	{: codeblock}

2. Delete the persistent volume claims provisioned by {{site.data.keyword.mgmt_hub}} components. Ensure only claims that include **ibm-edge** in their names are deleted because this step removes data (assuming the default name of **ibm-edge** for the custom resource). Modify the following loop as needed:
	```
    for CLAIM in $(oc get pvc | grep -E 'agbot|exchange|css|sdo|vault' | awk '{print $1}')
	do
		oc delete pvc $CLAIM
	done
	```
	{: codeblock}

3. Delete any remaining config maps created by the **eamhub** operator. Modify the following loop as needed:
	```
    for CONFIGMAP in $(oc get cm | grep -E 'stolon-cluster' | awk '{print $1}')
	do
		oc delete cm $CONFIGMAP
	done
	```
	{: codeblock}

4. Verify that **ieam\_maintenance\_mode** is correct:
	```
	yq r ibm-edge-backup/20201026_215738/customresource/eamhub-cr.yaml 'items[0].spec.ieam_maintenance_mode'
	```
	{: codeblock}

5. Run the `ieam-restore-k8s-resources.sh` script with option **-f** defined to point at your backup:
	```
	ibm-eam-{{site.data.keyword.semver}}-bundle/tools/ieam-restore-k8s-resources.sh -f ibm-edge-backup/20201026_215738/
	```
	{: codeblock}

   Wait until all the database, SDO, and vault pods are running before proceeding. It is possible that vault may continually restart, the vault bootstrap may reach an `Error` state, and/or SDO will likely be in a `0/1 Running` state and may reach a `CrashLoopBackOff` state. These are expected, and it is ok to proceed with those pods in those states.
	
6. Scale down the **eamhub** operator deployment to pause the operator and end the current control loop:
	```
    oc scale deploy ibm-eamhub-controller-manager --replicas=0
	```
	{: codeblock}

7. Run the `ieam-restore-data.sh` script with option **-f** defined to point at your backup:
	```
	ibm-eam-{{site.data.keyword.semver}}-bundle/tools/ieam-restore-data.sh -f ibm-edge-backup/20201026_215738/
	```
	{: codeblock}
	
8. After the script completes and your data has been restored, scale the operator back up to restart the control loop:
	```
    oc scale deploy ibm-eamhub-controller-manager --replicas=1
	```
	{: codeblock}

