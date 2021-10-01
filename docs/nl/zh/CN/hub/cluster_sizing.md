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


# 大小调整和系统需求
{: #size}

## 大小调整注意事项

调整集群大小涉及多个注意事项。 此内容描述其中部分注意事项并提供了尽力而为的指南以帮助调整集群大小。

主要注意事项是需要在集群上运行的服务。 此内容仅提供以下服务的大小调整指南：

* {{site.data.keyword.common_services}}
* {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) 管理中心

（可选）可以安装 [{{site.data.keyword.open_shift_cp}} 集群日志记录](../admin/accessing_logs.md#ocp_logging)。

## {{site.data.keyword.ieam}} 数据库注意事项

两个受支持的数据库配置影响 {{site.data.keyword.ieam}} 管理中心的大小调整注意事项：

* **本地**数据库在缺省情况下作为 {{site.data.keyword.open_shift}} 资源安装到 {{site.data.keyword.open_shift}} 集群。
* **远程**数据库是您供应的数据库，其可以是本地或云提供者 SaaS 产品等。

### {{site.data.keyword.ieam}} 本地数据库存储需求

**本地**数据库需要持久存储器，后者使用为 {{site.data.keyword.open_shift}} 集群配置的动态存储类。

有关更多信息，请参阅[受支持的动态 {{site.data.keyword.open_shift}} 存储选项和配置指示信息 ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开 ")](https://docs.openshift.com/container-platform/4.6/storage/understanding-persistent-storage.html)。

所选存储类的类型的主要注意事项是该存储类是否支持 **allowVolumeExpansion**。 如果是，那么以下命令返回 **true**：

```
oc get storageclass <desired storage class> -o json | jq .allowVolumeExpansion
```
{: codeblock}

如果存储类支持卷扩展，那么可以在安装后调整大小设置（假设底层存储空间可供分配）。 如果存储类不允许卷扩展，您必须为用例预分配存储器。 

如果在初始安装后需要更多存储器以用于不允许卷扩展的存储类，您将需要使用[备份和恢复](../admin/backup_recovery.md)页面中所述的步骤来运行重新安装。

可以在 {{site.data.keyword.ieam}} 管理中心安装之前，通过修改**存储**值来更改分配，如[配置](configuration.md)页面上所述。 分配设置为以下缺省值：

* PostgreSQL Exchange（存储 Exchange 的数据，并且其大小根据使用情况而波动，但缺省存储设置最多可支持已公布限制数量的边缘节点）
  * 20 GB
* PostgreSQL AgBot（存储 AgBot 的数据，缺省存储设置最多可支持已公布限制数量的边缘节点）
  * 20 GB
* MongoDB Cloud Sync Service（存储模型管理服务 (MMS) 的内容）。根据您的模型的数量及大小，可能需要修改此缺省分配。
  * 50 GB
* Secure Device Onboarding 持久卷（存储设备所有权凭单、设备配置点和每个设备的部署状态）
  * 1 GB（此卷大小不可配置）

* **注：**
  * 使用 **ReadWriteOnce** 访问方式创建 {{site.data.keyword.ieam}} 卷。
  * IBM Cloud Platform Common Services 对于其服务具有更多存储需求。 使用 {{site.data.keyword.ieam}} 缺省值进行安装时，在 **ibm-common-services** 名称空间中创建以下卷：
    ```
    NAME                                                                                     STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
    alertmanager-ibm-monitoring-alertmanager-db-alertmanager-ibm-monitoring-alertmanager-0   Bound    pvc-3979805f-8e3b-44d6-a039-cd438a3dbb25   10Gi       RWO            csi-cephfs     20h
    mongodbdir-icp-mongodb-0                                                                 Bound    pvc-e21604a7-14e4-4049-824e-a5a9feb472c8   20Gi       RWO            csi-cephfs     20h
    mongodbdir-icp-mongodb-1                                                                 Bound    pvc-eaecfa29-5c6a-45c2-9d26-58a393103791   20Gi       RWO            csi-cephfs     20h
    mongodbdir-icp-mongodb-2                                                                 Bound    pvc-42282c2b-bde8-4adf-86ad-006d2f07df91   20Gi       RWO            csi-cephfs     19h
    prometheus-ibm-monitoring-prometheus-db-prometheus-ibm-monitoring-prometheus-0           Bound    pvc-90237949-6f13-481b-8afa-7d86883b8a4f   10Gi       RWO            csi-cephfs     20h
    ```

    您可以在[此处](https://www.ibm.com/support/knowledgecenter/SSHKN6/installer/3.x.x/custom_resource.html)了解有关 IBM Cloud Platform Common Services 存储需求和配置选项的更多信息。

### {{site.data.keyword.ieam}} 远程数据库注意事项

利用自己的**远程**数据库可减少适用于此安装的存储类和计算需求（在同一集群上供应这些数据库的情况除外）。

至少向**远程**数据库供应以下资源和设置：

* 2 个 vCPU
* 2 GB RAM
* 先前部分中提到的缺省存储大小
* 对于 PostgreSQL 数据库，**最大连接数** 为 100（这通常为缺省值）

## 工作程序节点大小设置

使用 [Kubernetes 计算资源](https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container)的服务在可用工作程序节点间进行调度。

### 支持最多 6,000 个边缘节点的最低需求（通过缺省 {{site.data.keyword.ieam}} 配置支持）
| 工作程序节点数 | 每个工作程序节点的 vCPU 数 | 每个工作程序节点的内存 (GB) | 每个工作程序节点的本地磁盘存储量 (GB) |
| :---: | :---: | :---: | :---: |
| 3	| 8	| 32	| 100 	|


### 支持最多 40,000 个边缘节点的最低需求
| 工作程序节点数 | 每个工作程序节点的 vCPU 数 | 每个工作程序节点的内存 (GB) | 每个工作程序节点的本地磁盘存储量 (GB) |
| :---: | :---: | :---: | :---: |
| 3	| 16	| 32	| 100 	|


&nbsp;
&nbsp;

确定集群的合适大小设置后，即可开始使用[安装](online_installation.md)。
