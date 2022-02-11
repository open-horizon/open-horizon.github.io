---

copyright:
years: 2021
lastupdated: "2021-02-20"

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

**Local** databases require persistent storage, which uses dynamic storage classes that are configured for your {{site.data.keyword.open_shift}} cluster.

For more information, see [supported dynamic {{site.data.keyword.open_shift}} storage options and configuration instructions ](https://docs.openshift.com/container-platform/4.4/storage/understanding-persistent-storage.html){:target="_blank"}{: .externalLink}.

A main consideration for the type of storage class that is chosen, is whether that storage class supports **allowVolumeExpansion**. The following returns **true** if it does:

```
oc get storageclass <desired storage class> -o json | jq .allowVolumeExpansion
```
{: codeblock}

If the storage class allows volume expansion, sizing can be adjusted post installation (given the underlying storage space is available for allocation). If the storage class does not allow volume expansion, you must pre-allocate storage for your use case. 

If more storage is necessary after initial installation with a storage class that does not allow for volume expansion, you will need to run through a re-installation using the steps that are described in the [backup and recovery](../admin/) page.

The allocations can be changed before the {{site.data.keyword.ieam}} Management Hub installation by modifying the **Storage** values as described on the [configuration](configuration.md) page. The allocations are set to the following default values:

* PostgreSQL Exchange (Stores data for the exchange, and fluctuates in size depending on usage, but the default storage setting can support up to 10,000 devices)
  * 20 GB
* PostgreSQL AgBot (Stores data for the agbot, the default storage setting can support up to 10,000 devices)
  * 20 GB
* MongoDB Cloud Sync Service (stores content for the Model Management Service (MMS). Depending on the number and size of your models, you might want to modify this default allocation.
  * 50 GB
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

The services that use [Kubernetes compute resources](https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container) will be scheduled across available worker nodes.

### Minimal requirements for supporting up to 4,000 edge nodes (Supported with the default {{site.data.keyword.ieam}} configuration)
| Number of worker nodes | vCPUs per worker node | Memory per worker node (GB) | Local disk storage per worker node (GB) |
| :---: | :---: | :---: | :---: |
| 3	| 8	| 32	| 100 	|


### Minimal requirements for supporting up to 30,000 edge nodes
| Number of worker nodes | vCPUs per worker node | Memory per worker node (GB) | Local disk storage per worker node (GB) |
| :---: | :---: | :---: | :---: |
| 3	| 16	| 32	| 100 	|


&nbsp;
&nbsp;

After you determine the appropriate sizing for your cluster, you can begin the [installation](online_installation.md).
