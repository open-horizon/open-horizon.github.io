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

# 升级 {{site.data.keyword.ieam}}
{: #hub_upgrade_overview}

升级到 {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) 管理中心和 [IBM Cloud Platform Common Services ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://www.ibm.com/support/knowledgecenter/SSHKN6/kc_welcome_cs.html) 通过在 {{site.data.keyword.open_shift_cp}} ({{site.data.keyword.ocp}}) 集群上预安装的 Operator Lifecycle Manager 自动发生。

## 升级摘要
{: #sum}

* {{site.data.keyword.ieam}} 4.2.0 本地 **cssdb** Mongo 数据库存在已知问题，在重新调度 pod 时会导致数据丢失。如果使用本地数据库（缺省值），那么建议允许在将 {{site.data.keyword.ocp}} 集群更新到 4.6 前完成 {{site.data.keyword.ieam}} {{site.data.keyword.semver}} 升级。有关更多详细信息，请参阅[已知问题](../getting_started/known_issues.md)页面。
* {{site.data.keyword.ieam}} {{site.data.keyword.semver}} 在 {{site.data.keyword.ocp}} V4.6 上受支持。
* {{site.data.keyword.ieam}} 管理中心的当前版本是 {{site.data.keyword.semver}}。

**注**：不支持从 {{site.data.keyword.ieam}} 4.1 升级。

# 在边缘节点上升级代理程序

现有 {{site.data.keyword.ieam}} 节点不会自动升级。通过 {{site.data.keyword.ieam}} {{site.data.keyword.semver}} 管理中心支持 {{site.data.keyword.ieam}} 4.2.0 代理程序版本 (2.27.0-173)。

要在边缘设备和边缘集群上升级 {{site.data.keyword.edge_notm}} 代理程序，首先需要将 4.2.1 边缘节点文件放入 Cloud Sync Service (CSS)。按照[收集边缘节点文件 ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.2/hub/gather_files.html) 中的步骤来执行此操作。 

1. 以 **root** 用户身份或**管理员**身份登录边缘节点，然后设置 Horizon 环境变量：
```bash
export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
  export HZN_ORG_ID=<your-exchange-organization>
  export HZN_FSS_CSSURL=https://<ieam-management-hub-ingress>/edge-css/
```
{: codeblock}

2. 根据您的边缘集群类型，设置所需环境变量：

  * **在 OCP 边缘集群上：**
  
    设置存储类，代理程序应使用：
    
    ```bash
    oc get storageclass
   export EDGE_CLUSTER_STORAGE_CLASS=<rook-ceph-cephfs-internal>
    ```
    {: codeblock}

    将注册表用户名设置为您创建的服务帐户名称：
    ```bash
    oc get serviceaccount -n openhorizon-agent
    export EDGE_CLUSTER_REGISTRY_USERNAME=<service-account-name>
    ```
    {: codeblock}

    设置注册表令牌：
    ```bash
    export EDGE_CLUSTER_REGISTRY_TOKEN=`oc serviceaccounts get-token $EDGE_CLUSTER_REGISTRY_USERNAME`
    ```
    {: codeblock}

  * **在 k3s 上：**
  
    指示 **agent-install.sh** 使用缺省存储类：
    
    ```bash
    export EDGE_CLUSTER_STORAGE_CLASS=local-path
    ```
    {: codeblock}

  * **在 microk8s 上：**
  
    指示 **agent-install.sh** 使用缺省存储类：
    
    ```bash
    export EDGE_CLUSTER_STORAGE_CLASS=microk8s-hostpath
    ```
    {: codeblock}

3. 从 CSS 中拉取 **agent-install.sh**：
```bash
curl -u $HZN_ORG_ID/$HZN_EXCHANGE_USER_AUTH $HZN_FSS_CSSURL/api/v1/objects/IBM/agent_files/agent-install.sh/data -o agent-install.sh --insecure && chmod +x agent-install.sh
```
{: codeblock}

4. 运行 **agent-install.sh** 以从 CSS 获取更新的文件并配置 Horizon 代理程序：
  *  **在边缘设备上：**
    ```bash
    sudo -s -E ./agent-install.sh -i 'css:' -s
    ```
    {: codeblock}

  *  **在边缘集群上：**
    ```bash
    ./agent-install.sh -D cluster -i 'css:' -s
    ```
    {: codeblock}

**注**：在运行代理程序安装时包含 -s 选项以跳过注册，从而使边缘节点处于与升级前相同的状态。

## 常见问题
{: #FAQ}

* 我没有升级 {{site.data.keyword.ocp}} 集群以往版本 V4.4，自动升级似乎已暂停。

  * 按照以下步骤来解决此问题：
  
    1) 备份当前 {{site.data.keyword.ieam}} 管理中心内容。您可以在此处找到备份文档：[数据备份和恢复](../admin/backup_recovery.md)。
    
    2) 将 {{site.data.keyword.ocp}} 集群升级到 V4.6。
    
    3) 因为 {{site.data.keyword.ieam}} 4.2.0 本地 **cssdb** Mongo 数据库存在已知问题，**步骤 2** 中的升级将重新初始化此数据库。
    
      * 如果您已利用 {{site.data.keyword.ieam}} 的 MMS 功能并担心数据丢失，请使用**步骤 1** 中执行的备份并遵循[数据备份和恢复](../admin/backup_recovery.md)页面上的**复原过程**。（**注：**复原过程将导致停机时间。）
      
      * 或者，如果您尚未利用 MMS 功能，不担心 MMS 数据丢失或正在使用远程数据库，请执行以下步骤来卸载并重新安装 {{site.data.keyword.ieam}} 操作程序：
      
        1) 导航至 {{site.data.keyword.ocp}} 集群的“已安装的操作程序“页面。
        
        2) 找到“IEAM 管理中心”操作程序并打开其页面。
        
        3) 在左侧的操作菜单上，选择卸载操作程序。
        
        4) 导航至 OperatorHub 页面，然后重新安装“IEAM 管理中心”操作程序。

* 支持 {{site.data.keyword.ocp}} V4.5 吗？

  * {{site.data.keyword.ieam}} 管理中心未测试并且在 {{site.data.keyword.ocp}} V4.5 上不受支持。建议升级到 {{site.data.keyword.ocp}} V4.6。

* 是否有办法选择退出此版本的 {{site.data.keyword.ieam}} 管理中心？

  * 在发布 V{{site.data.keyword.semver}} 时，{{site.data.keyword.ieam}} 管理中心 V4.2.0 将不再受支持。
