---

copyright:
  years: 2019
lastupdated: "2019-06-12"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 准备安装 {{site.data.keyword.edge_servers_notm}}
{: #edge_planning}

在安装 {{site.data.keyword.icp_server}} 之前，启用 {{site.data.keyword.mgmt_hub}} 并配置 {{site.data.keyword.edge_servers_notm}}，确保系统满足以下需求。 这些需求确定了计划的边缘服务器所需的最低组件和配置。
{:shortdesc}

这些需求还确定了计划用于管理边缘服务器的 {{site.data.keyword.mgmt_hub}} 集群的最低配置设置。

使用此信息可帮助您规划边缘计算拓扑和总体
{{site.data.keyword.icp_server}} 和 {{site.data.keyword.mgmt_hub}} 设置的资源需求。

   * [硬件需求](#prereq_hard)
   * [受支持的 IaaS](#prereq_iaas)
   * [受支持的环境](#prereq_env)
   * [必需端口](#prereq_ports)
   * [集群大小调整注意事项](#cluster)

## 硬件需求
{: #prereq_hard}

在为边缘计算拓扑调整管理节点的大小时，请使用单节点或多节点部署的
{{site.data.keyword.icp_server}} 大小调整准则来帮助调整集群的大小。 有关更多信息，请参阅 [Sizing your {{site.data.keyword.icp_server}} cluster ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.2.0/installing/plan_capacity.html)。

以下边缘服务器需求仅适用于使用 {{site.data.keyword.edge_profile}} 部署到远程操作中心的 {{site.data.keyword.icp_server}}。

| 要求 | 节点（boot 节点、主节点和管理节点） | 工作程序节点 |
|-----------------|-----------------------------|--------------|
| 主机数量 | 1 | 1 |
| 核心数 | 4 或以上 | 4 或以上 |
| CPU | >= 2.4 GHz | >= 2.4 GHz |
| RAM | 8 GB 或更多 | 8 GB 或更多 |
| 可用于安装的磁盘空间 | 150 GB 或更多 | |
{: caption="表 1 最小边缘服务器集群硬件需求。" caption-side="top"}

注：如果网络与中央数据中心断开连接，150 GB 的存储空间最多可保留三天的日志和事件数据。

## 受支持的 IaaS
{: #prereq_iaas}

下表标识可用于边缘服务的受支持的基础结构即服务 (IaaS)。

| IaaS | 版本 |
|------|---------|
|在边缘服务器位置中使用的 Nutanix NX-3000 Series | NX-3155G-G6 |
|由 Nutanix 支持的用于边缘服务器的 IBM 超连接系统 | CS821 和 CS822|
{: caption="表 2. {{site.data.keyword.edge_servers_notm}} 的受支持 IaaS" caption-side="top"}

有关更多信息，请参阅 [IBM Hyperconverged Systems powered by Nutanix PDF ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://www.ibm.com/downloads/cas/BZP46MAV)。

## 受支持的环境
{: #prereq_env}

下表标识了可与边缘服务器搭配使用的其他 Nutanix 配置系统。

| LOE 站点类型 | 节点类型 | 集群大小 | 每个节点的内核数（总计） | 每个节点的逻辑处理器（总计）	| 每个节点的内存 (GB)（总计） | 每个磁盘组的高速缓存磁盘 (GB) |	每个节点的高缓存磁盘数量	| 每个节点的高速缓存磁盘大小 (GB)	| 存储器总集群池大小（所有闪存）(TB) |
|---|---|---|---|---|---|---|---|---|---|
| 小	| NX-3155G-G6	| 3 节点	| 24 (72)	| 48 (144)	| 256 (768)	| 不适用	| 不适用	| 不适用	| 8 TB |
| 中 | NX-3155G-G6 | 3 节点 | 24 (72)	| 48 (144)	| 512 (1,536)	| 不适用	| 不适用	| 不适用	| 45 TB |
| 大	| NX-3155G-G6	| 4 节点	| 24 (96)	| 48 (192)	| 512 (2,048)	| 不适用	| 不适用	| 不适用	| 60 TB |
{: caption="表 3. Nutanix NX-3000 系列支持的配置" caption-side="top"}

| LOE 站点类型	| 节点类型	| 集群大小 |	每个节点的内核数（总计） | 每个节点的逻辑处理器（总计）	| 每个节点的内存 (GB)（总计）	| 每个磁盘组的高速缓存磁盘 (GB) | 每个节点的高缓存磁盘数量	| 每个节点的高速缓存磁盘大小 (GB)	| 存储器总集群池大小（所有闪存）(TB) |
|---|---|---|---|---|---|---|---|---|---|
| 小	| CS821（2 套接字，1U） | 3 节点 | 20 (60)	| 80 (240) | 256 (768) | 不适用	| 不适用	| 不适用	| 8 TB |
| 中 | CS822（2 套接字，1U） | 3 节点	| 22 (66)	| 88 (264) | 512 (1,536) | 不适用 | 不适用 | 不适用 | 45 TB |
| 大	| CS822（2 套接字，1U） | 4 节点 | 22 (88) | 88 (352) | 512 (2,048) | 不适用 | 不适用 | 不适用 | 60 TB |
{: caption="表 4. Nutanix 支持的 IBM 超连接系统" caption-side="top"}

有关更多信息，请参阅 [Nutanix 支持的 IBM 超连接系统
![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://www.ibm.com/downloads/cas/BZP46MAV)。

## 必需端口
{: #prereq_ports}

如果计划使用标准集群配置部署远程边缘服务器，那么节点的端口需求与部署
{{site.data.keyword.icp_server}} 的端口需求相同。 有关这些需求的更多信息，请参阅 [Required ports ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.2.0/supported_system_config/required_ports.html)。 有关中央集群所需的端口，请参阅 _{{site.data.keyword.mcm_core_notm}} 所需的端口_一节。

如果计划配置 {{site.data.keyword.edge_profile}} 所使用的边缘服务器，请启用以下端口：

| 端口 | 协议 | 要求 |
|------|----------|-------------|
| NA | IPv4 | 使用 IP-in-IP 的（calico_ipip_mode：Always） |
| 179 | TCP	| 针对 Calico 设置为 Always (network_type:calico) |
| 500 | TCP 和 UDP	| IPSec（ipsec.enabled：true，calico_ipip_mode：Always） |
| 2380 | TCP | 如果已启用 etcd，那么设置为 Always |
| 4001 | TCP | 如果已启用 etcd，那么设置为 Always |
| 4500 | UDP | IPSec（ipsec.enabled：true） |
| 9091 | TCP | Calico（network_type：calico） |
| 9099 | TCP | Calico（network_type：calico） |
| 10248:10252 | TCP	| 针对 Kubernetes 设置为 Always |
| 30000:32767 | TCP 和 UDP | 针对 Kubernetes 设置为 Always |
{: caption="表 5. {{site.data.keyword.edge_servers_notm}} 需要的端口" caption-side="top"}

注：端口 30000:32767 具有外部访问权限。 仅当 Kubernetes 服务类型设置为 NodePort 时，才必须打开这些端口。

## 集群大小调整注意事项
{: #cluster}

对于 {{site.data.keyword.edge_servers_notm}} 服务器，中央集群通常是标准的 {{site.data.keyword.icp_server}} 托管环境。 您还可以使用此环境托管您需要或希望从中心位置提供服务的其他计算工作负载。 中央集群环境的大小必须使其具有足够的资源来托管 {{site.data.keyword.mcm_core_notm}} 集群和您计划在环境中托管的任何其他工作负载。 有关调整标准 {{site.data.keyword.icp_server}} 托管环境大小的更多信息，请参阅 [Sizing your {{site.data.keyword.icp_server}} cluster ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.2.0/installing/plan_capacity.html)。

如果需要，可以在资源受限的环境中操作远程边缘服务器。 如果需要在资源受限的环境中操作边缘服务器，请考虑使用 {{site.data.keyword.edge_profile}}。 此概要文件仅配置边缘服务器环境所需的最小组件。 如果使用此概要文件，那么仍必须为 {{site.data.keyword.edge_servers_notm}} 体系结构所需的一组组件分配足够的资源，并为托管在边缘服务器环境上的任何其他应用程序工作负载提供所需的资源。 有关 {{site.data.keyword.edge_servers_notm}} 体系结构的更多信息，请参阅 [{{site.data.keyword.edge_servers_notm}}](overview.md#edge_arch)。

虽然 {{site.data.keyword.edge_profile}} 配置可以节省内存和存储资源，但这些配置会导致低级别的弹性。 基于此概要文件的边缘服务器可以从中央集群所在的中央数据中心断开连接进行操作。 这种断开连接的操作通常可以持续三天。 如果边缘服务器出现故障，服务器将停止为远程操作中心提供操作支持。

{{site.data.keyword.edge_profile}} 配置也仅限于支持以下技术和进程：
  * {{site.data.keyword.linux_notm}} 64 位平台
  * 非高可用性 (HA) 部署拓扑
  * 添加和移除作为 day-2 操作的工作程序节点
  * CLI 对集群的访问权和控制
  * Calico 网络

如果您需要更高的恢复能力，或者如果前面的任何限制太过约束，那么可以选择为
{{site.data.keyword.icp_server}} 使用其他标准部署配置概要文件之一，以提供更好的故障转移支持。

### 部署样本

* 基于 {{site.data.keyword.edge_profile}} 的边缘服务器环境（弹性低）

| 节点类型 | 节点数 | CPU | 内存 (GB) | 磁盘 (GB) |
|------------|:-----------:|:---:|:-----------:|:---:|
| 引导节点       | 1           | 1   | 2           | 8   |
| 主要     | 1           | 2   | 4           | 16  |
| 管理节点 | 1           | 1   | 2           | 8   |
| 工作程序节点     | 1           | 4   | 8           | 32  |
{: caption="表 6. 低弹性边缘服务器环境的边缘概要文件值" caption-side="top"}

* 基于其他 {{site.data.keyword.icp_server}} 概要文件的边缘服务环境（弹性中到高）

  当需要为边缘服务器环境使用 {{site.data.keyword.edge_profile}} 以外的配置时，请使用小型、中型和大型示例部署要求。 有关更多信息，请参阅 [Sizing your {{site.data.keyword.icp_server}} cluster sample deployments ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.2.0/installing/plan_capacity.html#samples)。
