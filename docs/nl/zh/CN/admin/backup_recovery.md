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

# 数据备份和恢复
{: #data_backup}

## {{site.data.keyword.open_shift_cp}} 备份和恢复

有关集群范围的数据备份和恢复的更多信息，请参阅：

* [{{site.data.keyword.open_shift_cp}} 4.6 备份 etcd ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://docs.openshift.com/container-platform/4.6/backup_and_restore/backing-up-etcd.html)。

## {{site.data.keyword.edge_notm}} 备份和恢复

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) 备份过程略有不同，具体取决于所使用的数据库类型。 这些数据库被称为本地或远程。

|数据库类型|描述|
|-------------|-----------|
|本地|这些数据库在缺省情况下作为 {{site.data.keyword.open_shift}} 资源安装到 {{site.data.keyword.open_shift}} 集群|
|远程|这些数据库在外部供应给集群。 例如，这些数据库可以是本地或云提供者 SaaS 产品。|

用于管理使用哪些数据库的配置设置在安装时在定制资源 **spec.ieam\_local\_databases** 中进行设置，并且缺省情况下为 true。

要确定已安装的 {{site.data.keyword.ieam}} 实例的有效值，请运行：

```
oc get eamhub ibm-edge -o jsonpath="{.spec.ieam_local_databases}"
```
{: codeblock}

有关在安装时配置远程数据库的更多信息，请参阅[配置](../hub/configuration.md)页面。

**注**：不支持在本地和远程数据库之间进行切换。

{{site.data.keyword.edge_notm}} 产品不会自动备份数据。 您负责按自己选择的节奏备份内容并将这些备份存储在单独的安全位置以确保可恢复性。 机密备份包含用于数据库连接和 {{site.data.keyword.mgmt_hub}}应用程序认证的已编码认证内容，因此应存储在安全位置。

如果使用自己的远程数据库，请确保备份这些数据库。 此文档并未描述如何备份这些远程数据库的数据。

### 备份过程

1. 确保您以集群管理员身份通过 **cloudctl login** 或 **oc login** 连接到集群。 使用以下脚本备份数据和密钥，该脚本位于用于从 Passport Advantage 安装 {{site.data.keyword.mgmt_hub}} 的已解包介质中。 使用 **-h** 运行该脚本以了解用法：

   ```
   ibm-eam-{{site.data.keyword.semver}}-bundle/tools/ieam-backup.sh -h
   ```
   {: codeblock}
   
   **注**：备份脚本自动检测在安装期间使用的数据库类型。

   * 如果不使用任何选项运行以下示例，那么将生成在其中运行脚本的文件夹。 文件夹遵循此命名模式 **ibm-edge-backup/$DATE/**：

     ```
     ibm-eam-{{site.data.keyword.semver}}-bundle/tools/ieam-backup.sh
     ```
     {: codeblock}
     
     如果检测到**本地数据库**安装，那么备份包含 1 个 **customresource** 目录、1 个 **databaseresources** 目录和 2 个 yaml 文件：

     ```
     $ ls -l ibm-edge-backup/20201026_215107/
  	  drwxr-xr-x  3 staff  staff     96 Oct 26 21:51 customresource
	  drwxr-xr-x  5 staff  staff    160 Oct 26 21:51 databaseresources
	  -rw-r--r--  1 staff  staff  13308 Oct 26 21:51 ibm-edge-auth-secret.yaml
	  -rw-r--r--  1 staff  staff   3689 Oct 26 21:51 ibm-edge-config.yaml
     ```
     {: codeblock}
     
	  如果检测到**远程数据库**安装，那么您将看到先前列出的相同目录，但是 3 个 yaml 文件，而非 2 个。
	  
	  ```
     $ ls -l ibm-edge-backup/20201026_215518/
	  drwxr-xr-x  3 staff  staff     96 Oct 26 21:55 customresource
	  drwxr-xr-x  3 staff  staff     96 Oct 26 21:55 databaseresources
	  -rw-r--r--  1 staff  staff  10477 Oct 26 21:55 ibm-edge-auth-overrides.yaml
	  -rw-r--r--  1 staff  staff  11433 Oct 26 21:55 ibm-edge-auth-secret.yaml
	  -rw-r--r--  1 staff  staff   2499 Oct 26 21:55 ibm-edge-config.yaml
     ```
     {: codeblock}

### 复原过程

**注**：如果使用本地数据库或者复原至新的或空的远程数据库，那么在将备份复原到 {{site.data.keyword.mgmt_hub}} 时，{{site.data.keyword.ieam}} 的自主设计会导致已知的挑战。

要复原备份，必须安装相同的 {{site.data.keyword.mgmt_hub}}。 如果在初始安装期间未在进入 **ieam\_maintenance\_mode** 的情况下安装此新中心，那么很有可能所有先前已注册的边缘节点将注销自身。这需要重新注册。

在边缘节点发现因为数据库现在为空其不再存在于 Exchange 中时发生此情况。 通过仅针对 {{site.data.keyword.mgmt_hub}} 启动数据库资源，启用 **ieam\_maintenance\_mode** 以避免此情况。 这允许在启动其余 {{site.data.keyword.mgmt_hub}} 资源（使用这些数据库）前完成复原。

**注**： 

* 在备份**定制资源**文件时，将自动修改为在重新应用于集群时立即进入 **ieam\_maintenance\_mode**。

* 复原脚本通过检查 **\<path/to/backup\>/customresource/eamhub-cr.yaml** 文件自动确定先前使用的数据库类型。

1. 作为集群管理员，确保使用 **cloudctl login** 或 **oc login** 连接到集群，并且已创建有效备份。 在创建备份的集群上，运行以下命令以删除 **eamhub** 定制资源（假定缺省名称 **ibm-edge** 用于定制资源）：
	```
	oc delete eamhub ibm-edge
	```
	{: codeblock}

2. 验证是否正确设置了 **ieam\_maintenance\_mode**：
	```
	yq r ibm-edge-backup/20201026_215738/customresource/eamhub-cr.yaml items[0].spec.ieam_maintenance_mode
	```
	{: codeblock}
	

3. 使用定义为指向您的备份的选项 **-f** 运行 `ieam-restore-k8s-resources.sh` 脚本：
	```
	ibm-eam-{{site.data.keyword.semver}}-bundle/tools/ieam-restore-k8s-resources.sh -f ibm-edge-backup/20201026_215738/
	```
	{: codeblock}
	
4. 编辑 **ibm-edge** 定制资源以暂停操作程序：
	```
	oc patch eamhub ibm-edge --type merge --patch '{"spec":{"pause_control_loop": true}}'
	```
	{: codeblock}

5. 编辑 **ibm-edge-sdo** 有状态集合以将副本数量扩展到 **1**：
	```
	oc patch statefulset ibm-edge-sdo --type merge --patch '{"spec":{"replicas": 1}}'
	```
	{: codeblock}

6. 等待 **ibm-edge-sdo-0** pod 进入正在运行状态：
	```
   	watch oc get pods -n ibm-edge | grep ibm-edge-sdo-0
   	```
	{: codeblock}

7. 使用定义为指向您的备份的选项 **-f** 运行“ieam-restore-data.sh”脚本：
	```
	ibm-eam-{{site.data.keyword.semver}}-bundle/tools/ieam-restore-data.sh -f ibm-edge-backup/20201026_215738/
	```
	{: codeblock}
	
8. 脚本完成且数据已复原后，移除操作程序上的暂停以恢复控制循环：
	```
	oc patch eamhub ibm-edge --type merge --patch '{"spec":{"pause_control_loop": false}}'
	```
	{: codeblock}

