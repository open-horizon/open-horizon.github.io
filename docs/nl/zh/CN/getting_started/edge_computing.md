---

copyright:
years: 2020
lastupdated: "2020-05-11"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 边缘计算概述
{: #overviewofedge}

## {{site.data.keyword.edge_notm}} 功能
{: #capabilities}

{{site.data.keyword.edge_notm}} (IEAM) 跨越各个行业，以及使用 Docker 和 Kubernetes 之类的开放式技术和普遍标准优化的多个层。 这包括计算平台（私有云和企业环境）、网络计算空间和本地网关、控制器和服务器以及智能设备。

<img src="../images/edge/01_IEAM_overview.svg" width="100%" alt="IEAM 概述">

超大规模公共云、混合云、并置受管数据中心和传统企业数据中心继续集中充当数据、分析和后端数据处理的聚集点。

公共、专用和内容交付网络正在以边缘网络云的形式从简单管道转换为应用程序的更高价值托管环境。 {{site.data.keyword.ieam}} 的典型用例包括：

* 混合云计算
* 5G 联网 
* 边缘服务器部署
* 边缘服务器计算操作容量
* IoT 设备支持和优化

IBM Multicloud Management Core 1.2 从本地到边缘将来自多个供应商的云平台统一成一致的仪表板。 {{site.data.keyword.ieam}} 是使工作负载的分发和管理能够超出边缘网络扩展到边缘网关和边缘设备的自然扩展。 IBM Multicloud Management Core 1.2 使用边缘组件、私有和混合云环境以及公共云识别企业应用程序中的工作负载；其中 IBM Edge Computing Manager 为分布式 AI 提供新的执行环境以访问关键数据源。

IBM Multicloud Manager-CE 提供 AI 工具来加快深度学习、可视和语音识别以及视频和噪音分析，从而实现对所有解决方法和大多数音频和视频对话服务和发现格式的推理。

## {{site.data.keyword.edge_notm}} 风险与解决方法
{: #risks}

虽然 {{site.data.keyword.ieam}} 会创建特有的机会，但它也会带来挑战。 例如，它超越了云数据中心的物理边界，从而能够暴露安全性、可寻址性、管理、所有权和合规性问题。 更重要的是，它使得基于云的管理技术的缩放问题得以倍增。

边缘网络按数量级增加计算节点数。 边缘网关按另一个数量级增加计算节点数。 边缘设备将该数字增加 3 到 4 个数量级。 如果 DevOps（持续交付和持续部署）对于管理超大规模云基础结构至关重要，那么零操作（没有人为干预的操作）则对于按照 {{site.data.keyword.ieam}} 所表示的大规模进行管理至关重要。

在没有人为干预的情况下部署、更新、监视和恢复边缘计算空间至关重要。 所有这些活动和过程都必须：

* 完全自动化
* 能够独立作出有关工作分配的决策
* 无需干预即可识别不断变化的状况并从中恢复。 

所有这些活动都必须安全、可跟踪并可防御。

<!--{{site.data.keyword.edge_devices_notm}} delivers edge node management that minimizes deployment risks and manages the service software lifecycle on edge nodes fully autonomously. This function creates the capacity to achieve meaningful insights more rapidly from data that is captured closer to its source. {{site.data.keyword.edge_notm}} is available for infrastructure or servers, including distributed devices.
{:shortdesc}

Intelligent devices are being integrated into the tools that are used to conduct business at an ever-increasing rate. Device compute capacity is creating new opportunities for data analysis where data originates and actions are taken. {{site.data.keyword.edge_notm}} innovations fuel improved quality, enhance performance, and drive deeper, more meaningful user interactions. 

{{site.data.keyword.edge_notm}} can:

* Solve new business problems by using Artificial Intelligence (AI)
* Increase capacity and resiliency
* Improve security and privacy protections
* Leverage 5G networks to reduce latency

{{site.data.keyword.edge_notm}} can capture the potential of untapped data that is created by the unprecedented growth of connected devices, which opens new business opportunities, increases operational efficiency, and improves customer experiences. {{site.data.keyword.edge_notm}} brings Enterprise applications closer to where data is created and actions need to be taken, and it allows Enterprises to leverage AI and analyze data in near-real time.

## {{site.data.keyword.edge_notm}} benefits
{: #benefits}

{{site.data.keyword.edge_notm}} helps solve speed and scale challenges by using the computational capacity of edge devices, gateways, and networks. This function retains the principles of dynamic allocation of resources and continuous delivery that are inherent to cloud computing. With {{site.data.keyword.edge_notm}}, businesses have the potential to virtualize the cloud beyond data centers. Workloads that are created in the cloud can be migrated towards the edge, and where appropriate, data that is generated at the edge can be cleansed and optimized and brought back to the cloud.

{{site.data.keyword.edge_devices_notm}} spans industries and multiple tiers that are optimized with open technologies and prevailing standards like Docker and Kubernetes. This includes computing platform, both private cloud and Enterprise environments, network compute spaces and on-premises gateways, controllers and servers, and intelligent devices.

Centrally, the hyper-scale public clouds, hybrid clouds, colocated managed data centers and traditional Enterprise data centers continue to serve as aggregation points for data, analytics, and back-end data processing.

Public, private, and content-delivery networks are transforming from simple pipes to higher-value hosting environments for applications in the form of the edge network cloud.

{{site.data.keyword.edge_devices_notm}} offers: 

* Integrated offerings that provide faster insights and actions, secure and continuous operations.
* The industry's first policy-based, autonomous edge computing platform
that intelligently manages workload life cycles in a secure and flexible way.
* Open technology and ecosystems compatibility to provide robust support and innovation for industry-wide ecosystems and partners.
* Scalable solutions for wide-ranging deployment on edge devices, servers, gateways, and network elements.

## {{site.data.keyword.edge_notm}} capabilities
{: #capabilities}

* Hybrid cloud computing
* 5G networking 
* Edge server deployment
* Edge servers compute operations capacity
* IoT devices support and optimization

## {{site.data.keyword.edge_notm}} risks and resolution
{: #risks}

Although {{site.data.keyword.edge_notm}} creates unique opportunities, it also presents challenges. For example, it transcends cloud data center's physical boundaries, which can expose security, addressability, management, ownership, and compliance issues. More importantly, it multiplies the scaling issues of cloud-based management techniques.

Edge networks increase the number of compute nodes by an order of magnitude. Edge gateways increase that by another order of magnitude. Edge devices increase that number by 3 to 4 orders of magnitude. If DevOps (continuous delivery and continuous deployment) is critical to managing a hyper-scale cloud infrastructure, then zero-ops (operations with no human intervention) is critical to managing at the massive scale that {{site.data.keyword.edge_notm}} represents.

It is critical to deploy, update, monitor, and recover the edge compute space without human intervention. All of these activities and processes must be fully automated, capable of making decisions independently about work allocation, and able to recognize and recover from changing conditions without intervention. All of these activities must be secure, traceable, and defensible.

## Extending multi-cloud deployments to the edge
{: #extend_deploy}

{{site.data.keyword.mcm_core_notm}} unifies cloud platforms from multiple vendors into a consistent dashboard from on-premises to the edge. {{site.data.keyword.edge_devices_notm}} is a natural extension that enables the distribution and management of workloads beyond the edge network to edge gateways and edge devices.

{{site.data.keyword.mcm_core_notm}} recognizes workloads from Enterprise applications with edge components, private and hybrid cloud environments, and public cloud; where {{site.data.keyword.edge_notm}} provides a new execution environment for distributed AI to reach critical data sources.

{{site.data.keyword.mcm_ce_notm}} delivers AI tools for accelerated deep learning, visual and speech recognition, and video and acoustic analytics, which enables inferencing on all resolutions and most formats of video and audio conversation services and discovery.

## {{site.data.keyword.edge_devices_notm}} architecture
{: #iec4d_arch}

Other edge computing solutions typically focus on one of the following architectural strategies:

* A powerful centralized authority for enforcing edge node software compliance.
* Passing the software compliance responsibility down to the edge node owners, who are required to monitor for software updates, and manually bring their own edge nodes into compliance.

The former focuses authority centrally, creating a single point of failure, and a target that attackers can exploit to control the entire fleet of edge nodes. The latter solution can result in large percentages of the edge nodes not having the latest software updates installed. If edge nodes are not all on the latest version or have all of the available fixes, the edge nodes can be vulnerable to attackers. Both approaches also typically rely upon the central authority as a basis for the establishment of trust.

<p align="center">
<img src="../images/edge/overview_illustration.svg" width="70%" alt="Illustration of the global reach of edge computing.">
</p>

In contrast to those solution approaches, {{site.data.keyword.edge_devices_notm}} is decentralized. {{site.data.keyword.edge_devices_notm}} manages service software compliance automatically on edge nodes without any manual intervention. On each edge node, decentralized and fully autonomous agent processes run governed by the policies that are specified during the machine registration with {{site.data.keyword.edge_devices_notm}}. Decentralized and fully autonomous agbot (agreement bot) processes typically run in a central location, but can run anywhere, including on edge nodes. Like the agent processes, the agbots are governed by policies. The agents and agbots handle most of the edge service software lifecycle management for the edge nodes and enforce software compliance on the edge nodes.

For efficiency, {{site.data.keyword.edge_devices_notm}} includes two centralized services, the exchange and the switchboard. These services have no central authority over the autonomous agent and agbot processes. Instead, these services provide simple discovery and metadata sharing services (the exchange) and a private mailbox service to support peer-to-peer communications (the switchboard). These services support the fully autonomous work of the agents and agbots.

Lastly, the {{site.data.keyword.edge_devices_notm}} console helps administrators set policy and monitor the status of the edge nodes.

Each of the five {{site.data.keyword.edge_devices_notm}} component types (agents, agbots, exchange, switchboard, and console) has a constrained area of responsibility. Each component has no authority or credentials to act outside their respective area of responsibility. By dividing responsibility and scoping authority and credentials, {{site.data.keyword.edge_devices_notm}} offers risk management for edge node deployment.

WRITER NOTE: content from https://www-03preprod.ibm.com/support/knowledgecenter/SSFKVV_4.1/hub/offline_installation.html

Merge the content in this section with the above content.

## {{site.data.keyword.edge_devices_notm}}
{: #edge_devices}

{{site.data.keyword.edge_devices_notm}} provides you with a new architecture for edge node management. It is designed specifically to minimize the risks that are inherent in the deployment of either a global or local fleet of edge nodes. You can also use {{site.data.keyword.edge_devices_notm}} to manage the service software lifecycle on edge nodes fully autonomously.
{:shortdesc}

{{site.data.keyword.edge_devices_notm}} is built on the {{site.data.keyword.horizon_open}} project. For more information about the project, see [{{site.data.keyword.horizon_open}} ![Opens in a new tab](../../images/icons/launch-glyph.svg "Opens in a new tab")](https://github.com/open-horizon).-->

有关使用 {{site.data.keyword.edge_notm}} 和开发边缘服务的更多信息，请参阅下列主题和主题组：

* [安装管理中心](../hub/offline_installation.md) 了解如何安装和配置 {{site.data.keyword.edge_devices_notm}} 基础结构并收集添加边缘设备所需的文件。

* [安装边缘节点](../devices/installing/installing_edge_nodes.md) 了解如何安装和配置 {{site.data.keyword.edge_devices_notm}} 基础结构并收集添加边缘设备所需的文件。
  
* [使用边缘服务](../devices/developing/using_edge_services.md) 了解有关使用 {{site.data.keyword.edge_notm}} 边缘服务的更多信息。

* [开发边缘服务](../devices/developing/developing_edge_services.md) 了解有关使用 {{site.data.keyword.edge_notm}} 边缘服务的更多信息。

* [管理 ](../devices/administering_edge_devices/administering.md)
  了解有关管理 {{site.data.keyword.edge_notm}} 边缘服务的更多信息。 
  
* [安全性](../devices/user_management/security.md)
  了解 {{site.data.keyword.edge_notm}} 如何维护安全性来抵御攻击和保护参与者隐私。

* [使用管理控制台](../devices/getting_started/accessing_ui.md)
  查看常见问题，以快速了解有关 {{site.data.keyword.edge_notm}} 的关键信息。

* [使用 CLI](../devices/getting_started/using_cli.md)
  查看常见问题，以快速了解有关 {{site.data.keyword.edge_notm}} 的关键信息。

* [API](../devices/installing/edge_rest_apis.md)
  查看常见问题，以快速了解有关 {{site.data.keyword.edge_notm}} 的关键信息。

* [故障诊断](../devices/troubleshoot/troubleshooting.md)
  如果在设置或使用 {{site.data.keyword.edge_devices_notm}} 时遇到问题，请查看可能出现的常见问题，以及帮助您解决问题的提示。
