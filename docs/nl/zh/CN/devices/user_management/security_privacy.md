---

copyright:
years: 2019
lastupdated: "2019-06-24"
 
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 安全与保密
{: #security_privacy}

{{site.data.keyword.edge_devices_notm}} 以 {{site.data.keyword.horizon}} 为基础，实现最大限度的安全来抵御攻击，以及保护参与者的隐私。 {{site.data.keyword.edge_devices_notm}} 依赖于地理上的分布式自主代理程序进程和协议自动程序 (agbot) 进程来进行边缘软件管理以及保持匿名性。
{:shortdesc}

为保持匿名性，代理程序进程和 agbot 进程在 {{site.data.keyword.edge_devices_notm}}
的整个发现和协商过程中只共享其公用密钥。 缺省情况下，{{site.data.keyword.edge_devices_notm}}
内的所有参与方都将对方视为不可信实体。 只有在建立信任、双方协商完成并达成正式协议的情况下，双方才会共享信息并进行协作。

## 分布式控制平面
{: #dc_pane}

相较于典型的集中式物联网 (IoT) 平台以及基于云的控制系统，{{site.data.keyword.edge_devices_notm}} 的控制平面基本上是分散式平面。 系统中每个角色的权限范围都受限制，仅具有完成关联的任务所需的最低权限级别。 没有任何单一权限可以断言对整个系统的控制权。 用户或角色无法通过损害任何单一主机或软件组件来获取系统中所有节点的访问权。

控制平面由三个不同的软件实体实现：
* {{site.data.keyword.horizon}} 代理程序
* {{site.data.keyword.horizon}} agbot
* {{site.data.keyword.horizon_exchange}}

{{site.data.keyword.horizon}} 代理程序和 agbot 是主要实体，它们自主地管理边缘节点。 {{site.data.keyword.horizon_exchange}} 促进代理程序与 agbot 之间的发现、协商和安全通信。

### 代理程序
{: #agents}

{{site.data.keyword.horizon}} 代理程序的数量超过 {{site.data.keyword.edge_devices_notm}} 中的所有其他参与者。 代理程序在每个受管边缘节点上运行。 每个代理程序仅有权管理该单一边缘节点。 代理程序在 {{site.data.keyword.horizon_exchange}} 中通告其公用密钥，并与远程 agbot 进程协商管理本地节点的软件。 该代理程序只期望接收在该代理程序的组织之内，对部署模式负责的 agbot 的通信。

受损的代理程序不具有影响任何其他边缘节点或系统中任何其他组件的任何权限。 主机操作系统或者某边缘节点上的代理程序进程遭黑客攻击或遭受其他损害时，只有该边缘节点受损。 {{site.data.keyword.edge_devices_notm}} 系统的所有其他部分不受影响。

边缘节点代理程序可以是边缘节点上功能最强大的组件，但是它危害总体 {{site.data.keyword.edge_devices_notm}} 系统安全性的能力却是最低。 代理程序负责将软件下载到边缘节点，验证该软件，然后运行该软件，并将其与边缘节点上的其他软硬件关联。 但是，在 {{site.data.keyword.edge_devices_notm}} 的总体系统范围安全性中，代理程序的权限不会超越运行该代理程序所在的边缘节点。

### agbot
{: #agbots}

{{site.data.keyword.horizon}} agbot 进程可以在任何位置运行。 缺省情况下，这些进程自动运行。 agbot
实例是 {{site.data.keyword.horizon}} 中第二常见的参与者。 每个 agbot 仅对分配给它的部署模式负责。 部署模式主要由策略和软件服务清单组成。 单个 agbot 实例可以管理组织内的多个部署模式。

部署模式由开发者在 {{site.data.keyword.edge_devices_notm}} 用户组织的上下文中发布。 部署模式由 agbot
提供给 {{site.data.keyword.horizon}} 代理程序。 当边缘节点向
{{site.data.keyword.horizon_exchange}} 注册时，该组织的一个部署模式就会分配给该边缘节点。 该边缘节点上的代理程序只接受从该特定组织提供该特定部署模式的 agbot 所提供的部署模式。 agbot 是交付部署模式的媒介，但部署模式本身必须可以被边缘节点所有者在边缘节点上设置的策略所接受。 部署模式必须通过签名验证，否则代理程序不会接受该模式。

受损的 agbot 可以尝试提出与边缘节点的恶意协议，并尝试在边缘节点上部署恶意的部署模式。 但是，边缘节点代理程序只接受代理程序通过注册来请求的部署模式的协议，而且这些部署模式必须可以被该边缘节点上设置的策略接受。 此外，代理程序先使用其公用密钥来验证该模式的加密签名，然后才接受该模式。

即使 agbot 进程编排软件安装并维护更新，agbot 也无权强制任何边缘节点或代理程序接受该 agbot 所提供的软件。 每个边缘节点上的代理程序决定接受或拒绝哪些软件。 该代理程序根据其安装的公用密钥以及边缘节点所有者向 {{site.data.keyword.horizon_exchange}} 注册边缘节点时设置的策略做出此决定。

## {{site.data.keyword.horizon_exchange}}
{: #exchange}

{{site.data.keyword.horizon_exchange}} 是集中式服务，但在地理上进行复制和负载均衡，它使分布式代理程序和 agbot 能够加入和协商协议。 有关更多信息，请参阅 [{{site.data.keyword.edge}} 概述](../../getting_started/overview_ieam.md)。

{{site.data.keyword.horizon_exchange}} 还用作用户、组织、边缘节点以及所有已发布的服务、策略和部署模式的元数据共享数据库。

开发者将他们所创建的软件服务实现、策略和部署模式的相关 JSON 元数据发布到 {{site.data.keyword.horizon_exchange}} 中。 这些信息由开发者建立散列，并进行加密签名。 边缘节点所有者在注册边缘节点期间需要为软件安装公用密钥，以便本地代理程序可以使用这些密钥来验证签名。

受损的 {{site.data.keyword.horizon_exchange}} 可以恶意提供虚假信息给代理程序进程和 agbot 进程，但因为系统内置有验证机制，影响已降至最低水平。 {{site.data.keyword.horizon_exchange}}
没有恶意签署元数据所需的凭证。 受损的 {{site.data.keyword.horizon_exchange}}
无法恶意欺骗任何用户或组织。 {{site.data.keyword.horizon_exchange}} 充当开发者及边缘节点所有者所发布的工件的仓库，可以在发现和协商过程中用来启用 agbot。

{{site.data.keyword.horizon_exchange}} 还调解并保护代理程序与 agbot 之间的所有通信。 它实现了邮箱机制，允许参与者向其他参与者发送消息。 要接收消息，参与者必须轮询 Horizon Switchboard 以确定其邮箱是否包含任何消息。

此外，代理程序和 agbot 都与 {{site.data.keyword.horizon_exchange}} 共享公用密钥，以进行安全的私密通信。 当任何参与者需要与另一参与者通信时，发件人可使用预期收件人的公用密钥来识别收件人。 发件人使用该公用密钥将发给收件人的消息加密。 然后，收件人可以使用发件人的公用密钥将他们的回应加密。

此方法可确保 Horizon Exchange 无法窃听消息，因为它缺少解密消息所必需的共享密钥。 只有预期收件人才能将消息解密。 损坏的 Horizon Exchange 无法查看任何参与者的通信，并且无法在参与者之间的任何对话中插入恶意通信。

## 拒绝服务攻击
{: #denial}

{{site.data.keyword.horizon}} 依赖集中式服务。 在典型的物联网系统中，集中式服务通常容易受到拒绝服务攻击。 对于 {{site.data.keyword.edge_devices_notm}}，这些集中式服务仅用于发现、协商和更新任务。 仅当进程必须完成发现、协商和更新任务时，分布式自主代理程序进程和
agbot 进程才会使用集中式服务。 否则，形成协议后，系统可以继续正常工作，即使这些集中式服务脱机也是如此。 这种行为可确保 {{site.data.keyword.edge_devices_notm}} 保持活动状态，即使集中式服务遭受攻击也是如此。

## 非对称密码术
{: #asym_crypt}

{{site.data.keyword.edge_devices_notm}} 中的大部分密码术基于非对称密钥加密。 使用这种形式的密码术，您和开发者必须使用 `hzn key` 命令生成密钥对，并使用您的专用密钥对所要发布的任何软件或服务进行加密签名。 您必须将自己的公用密钥安装在需要运行软件或服务的边缘节点上，以便验证该软件或服务的加密签名。

代理程序和 agbot 都使用自己的专用密钥对发给对方的消息进行加密签名，并使用对方的公用密钥来验证它们所收到的消息。 代理程序和 agbot 还使用另一方的公用密钥将自己的消息加密，以确保只有预期收件人才能将该消息解密。

代理程序、agbot 或用户的专用密钥和凭证受损时，只有该实体控制之下的工件才会暴露。 

## 摘要
{: #summary}

通过使用散列、加密签名和加密，{{site.data.keyword.edge_devices_notm}} 可以保护平台的大多数部分免遭有害访问。 通过在根本上实现分散化，{{site.data.keyword.edge_devices_notm}} 可以避免您遭受较传统物联网平台中常见的大部分攻击。 通过限制参与者角色的权限及影响范围，{{site.data.keyword.edge_devices_notm}} 可将受损主机或受损软件组件的潜在损害限制在系统的相应部分。 即使 {{site.data.keyword.edge_devices_notm}} 中使用的 {{site.data.keyword.horizon}} 服务的集中式服务遭受大规模外部攻击，对已达成协议的参与者也只有最轻微的影响。 在有效协议管控下的参与者可以继续正常工作，不受干扰。
