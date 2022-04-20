---

copyright:
years: 2020 - 2022
lastupdated: "2022-03-17"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}


# Sizing and system requirements
{: #size}

## Sizing considerations

Sizing your cluster involves many considerations. This content describes some of these considerations and provides a best-effort guide to help you size your cluster.

The primary consideration is what services need to run on your cluster. This content provides sizing guidance for the following services only:

* {{site.data.keyword.common_services}}
* {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) Management Hub

Optionally, you can install [{{site.data.keyword.open_shift_cp}} cluster logging](../admin/accessing_logs.md#ocp_logging).

## {{site.data.keyword.ieam}} database considerations

Two supported database configurations impact sizing considerations for the {{site.data.keyword.ieam}} management hub:

* **Local** databases are installed (by default) as {{site.data.keyword.open_shift}} resources onto your {{site.data.keyword.open_shift}} cluster.
* **Remote** databases are databases that you provisioned, which can be on-premises, cloud provider SaaS offerings, and so on.

### {{site.data.keyword.ieam}} local database storage requirements

In addition to the always installed Secure Device Onboarding (SDO) component, **local** databases and secrets manager require persistent storage. This storage uses dynamic storage classes that are configured for your {{site.data.keyword.open_shift}} cluster.

For more information, see [supported dynamic {{site.data.keyword.open_shift}} storage options and configuration instructions ](https://docs.openshift.com/container-platform/4.6/storage/understanding-persistent-storage.html){:target="_blank"}{: .externalLink}.

You are responsibile for enabling encryption at rest at the time of cluster creation. It can often be included as part of cluster creation on cloud platforms. For more information, see the [following documentation ](https://docs.openshift.com/container-platform/4.6/installing/installing-fips.html){:target="_blank"}{: .externalLink}.

A main consideration for the type of storage class that is chosen, is whether that storage class supports **allowVolumeExpansion**. The following returns **true** if it does:

```
oc get storageclass <desired storage class> -o json | jq .allowVolumeExpansion
```
{: codeblock}

If the storage class allows volume expansion, sizing can be adjusted post installation (given the underlying storage space is available for allocation). If the storage class does not allow volume expansion, you must pre-allocate storage for your use case.

If more storage is necessary after initial installation with a storage class that does not allow for volume expansion, you will need to run through a re-installation by using the steps that are described in the [backup and recovery](../admin/backup_recovery.md) page.

The allocations can be changed before the {{site.data.keyword.ieam}} Management Hub installation by modifying the **Storage** values as described on the [configuration](configuration.md) page. The allocations are set to the following default values:

* PostgreSQL Exchange (Stores data for the Exchange, and fluctuates in size depending on usage, but the default storage setting can support up to the advertised limit of edge nodes)
  * 20 GB
* PostgreSQL {{site.data.keyword.agbot}} (Stores data for the {{site.data.keyword.agbot}}, the default storage setting can support up to the advertised limit of edge nodes)

  * 20 GB
* MongoDB Cloud Sync Service (stores content for the Model Management Service (MMS). Depending on the number and size of your models, you might want to modify this default allocation.
  * 50 GB
* Hashicorp Vault persistent volume (Stores secrets used by edge device services)
  * 10 GB (This volume size is not configurable)
* Secure Device Onboarding persistent volume (Stores device ownership vouchers, device configuration options, and the deployment status of each device)
  * 1 GB (This volume size is not configurable)

* **Notes:**
  * {{site.data.keyword.ieam}} volumes are created with the **ReadWriteOnce** access mode.

### {{site.data.keyword.ieam}} remote database considerations

Leveraging your own **remote** databases reduces the storage class and compute requirements for this installation, unless they are provisioned on the same cluster.

At a minimum, provision **Remote** databases with the following resources and settings:

* 2vCPU's
* 2 GB of RAM
* The default storage sizes mentioned in the previous section
* For the PostgreSQL databases, 100 **max_connections** (which is typically the default)

## Worker node sizing

The services that use [Kubernetes compute resources ](https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container){:target="_blank"}{: .externalLink} will be scheduled across available worker nodes.

### Minimal requirements for the default {{site.data.keyword.ieam}} configuration
| Number of worker nodes | vCPUs per worker node | Memory per worker node (GB) | Local disk storage per worker node (GB) |
| :---: | :---: | :---: | :---: |
| 3	| 8	| 32	| 100 	|

**Note:** Some customer environments might require additional vCPUs per worker node or additional worker nodes, so more CPU capacity can be
allocated to the Exchange component.


&nbsp;
&nbsp;

After you determine the appropriate sizing for your cluster, you can begin the [installation](online_installation.md).
