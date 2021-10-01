---

copyright:
  years: 2019
lastupdated: "2019-06-28"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# {{site.data.keyword.edge_devices_notm}} 工作方式概述
{: #overview}

{{site.data.keyword.edge_devices_notm}} 专为边缘节点管理而设计，旨在最大限度减少部署风险，以及完全自主地管理边缘节点上的服务软件生命周期。
{:shortdesc}

## {{site.data.keyword.edge_devices_notm}} 体系结构

{: #iec4d_arch}

其他边缘计算解决方案通常侧重于下列其中一个体系结构策略：

* 强大的集中权限，用于强制实施边缘节点软件合规性。
* 将软件合规性责任传递给边缘节点所有者，他们需要监视软件更新，并手动使自己的边缘节点合规。

前一种解决方案侧重于集中权限，这会产生单一故障点，攻击者可以利用该目标来控制整个边缘节点群。 后一种解决方案可能会导致很大比例的边缘节点没有安装最新的软件更新。 如果边缘节点并非全为最新版本或安装全部可用修订，那么可能很容易遭受攻击者攻击。 这两种方法通常还依赖于集中权限作为建立信任的基础。

<p align="center">
<img src="../../images/edge/overview_illustration.svg" width="70%" alt="此图说明边缘计算的全局可达性。">
</p>

相较于这些解决方案的方法，{{site.data.keyword.edge_devices_notm}} 具有分散式特征。 {{site.data.keyword.edge_devices_notm}} 自动管理边缘节点上的服务软件合规性，无需任何手动干预。 在每个边缘节点上，完全自主的分散式代理程序进程在策略的监管下运行，这些策略是在机器向 {{site.data.keyword.edge_devices_notm}} 注册期间指定。 完全自主的分散式 agbot（协议自动程序）进程通常在中心位置运行，但也可以在任意位置运行，包括在边缘节点上运行。 与代理程序进程一样，agbot 由策略监管。 代理程序和 agbot 处理边缘节点的大部分边缘服务软件生命周期管理，并在边缘节点上强制实施软件合规性。

为提高效率，{{site.data.keyword.edge_devices_notm}} 随附两个集中式服务，即 Exchange 和 Switchboard。 这些服务对于自主代理程序进程和 agbot 进程不具有中央权限。 相反，这些服务提供简单的发现和元数据共享服务 (Exchange)，以及支持点对点通信的私有邮箱服务 (Switchboard)。 这些服务支持代理程序和 agbot 的完全自主工作。

最后，{{site.data.keyword.edge_devices_notm}} 控制台帮助管理员设置策略和监视边缘节点的状态。

五种 {{site.data.keyword.edge_devices_notm}} 组件类型（代理程序、agbot、Exchange、Switchboard 和控制台）各有受约束的责任范围。 每个组件都没有在各自的责任范围之外采取行动的权限或凭证。 通过划分责任，以及限定权限和凭证的范围，{{site.data.keyword.edge_devices_notm}} 可以为边缘节点部署提供风险管理。

## 发现与协商
{: #discovery_negotiation}

基于 [1{{site.data.keyword.horizon_open}} ![在新的选项卡中打开](../../images/icons/launch-glyph.svg "在新的选项卡中打开")](https://github.com/open-horizon/) 项目的 {{site.data.keyword.edge_devices_notm}} 主要具有分散式和分布式特征。 自主代理程序进程与协议自动程序 (agbot) 进程相互协作，完成所有已注册的边缘节点的软件管理工作。

在每个 Horizon 边缘节点上都会运行自主代理程序进程，用于强制实施边缘设备所有者所设置的策略。

自主 agbot 监视 Exchange 中的部署模式和策略并搜寻尚未合规的边缘节点代理程序。 Agbot 向边缘节点建议协议，以使其合规。 当 agbot 和代理程序达成协议时，它们合作管理边缘节点上边缘服务的软件生命周期。

agbot 和代理程序使用下列集中式服务来彼此找到对方，建立信任，然后在 {{site.data.keyword.edge_devices_notm}} 上安全地进行通信：

* {{site.data.keyword.horizon_exchange}}：用于促进发现。
* {{site.data.keyword.horizon_switch}}：在 agbot 与代理程序之间启用安全且私密的对等通信。

<img src="../../images/edge/distributed.svg" width="90%" alt="集中式服务和分散式服务">

### {{site.data.keyword.horizon_exchange}}
{: #iec4d_exchange}

{{site.data.keyword.horizon_exchange}} 使边缘设备所有者能够注册边缘节点，以便进行软件生命周期管理。 向 {{site.data.keyword.horizon_exchange}} for {{site.data.keyword.edge_devices_notm}} 注册边缘节点时，请为该边缘节点指定部署模式或策略。 （在其核心处，部署模式是用于管理边缘节点的简单预先定义且指定的策略集。） 模式和策略必须在 {{site.data.keyword.horizon_exchange}} 中进行设计、开发、测试、签署和发布。

每个边缘节点都使用一个唯一标识和安全令牌进行注册。 节点可以注册为使用其自己的组织提供的模式或策略，或者其他组织提供的模式。

在将模式或策略发布到 {{site.data.keyword.horizon_exchange}} 时，agbot 寻求发现受新的或更新的模式或策略影响的任何边缘节点。 在找到已注册的边缘节点时，agbot 与边缘节点代理程序进行协商。

虽然 {{site.data.keyword.horizon_exchange}} 使 agbot 能够找到注册为使用模式或策略的边缘节点，但
{{site.data.keyword.horizon_exchange}} 并不直接参与边缘节点软件管理过程。 软件管理过程由 agbot
和代理程序处理。 {{site.data.keyword.horizon_exchange}} 在边缘节点上不具有权限，不会向边缘节点代理程序发起任何联系。

### {{site.data.keyword.horizon_switch}}
{: #horizon_switch}

当 agbot 发现受新的或更新的模式或策略影响的边缘节点时，agbot 会使用 {{site.data.keyword.horizon}} Switchboard 向该节点上的代理程序发送一条私有消息。 该消息是在边缘节点的软件生命周期管理上协作的协议建议。 代理程序 {{site.data.keyword.horizon_switch}} 上的其私有邮箱中收到来自 agbot 的消息，其解密并评估建议。 如果符合其自己的节点策略，那么节点会向 agbot 发送接受消息。 否则，节点将拒绝该建议。 在 agbot 在 {{site.data.keyword.horizon_switch}} 中其自己的私有邮箱中收到协议接受时，协商完成。

代理程序和 agbot 在 {{site.data.keyword.horizon_switch}} 中发布公用密钥，以其有用使用完美前向保密的安全私密通信。 在这种加密中，{{site.data.keyword.horizon_switch}}
仅充当邮箱管理器。 其无法解密消息。

注：因为所有通信都通过 {{site.data.keyword.horizon_switch}} 进行代理，直到每个边缘节点上的代理程序选择公开边缘节点的 IP 地址之后，才会将该信息透露给任何 agbot。 当代理程序与 agbot 成功议定协议时，代理程序就会公开这些信息。

## 边缘软件生命周期管理
{: #edge_lifecycle}

当 agbot 和代理程序就特定模式或策略集达成协议时，它们合作管理边缘节点上模式或策略的软件生命周期。 Agbot 监视模式或策略随时间的演进，并监视边缘节点以实现合规性。 代理程序将软件下载到边缘节点本地，验证该软件的签名，如果已验证，则运行并监视该软件。 如有必要，代理程序会更新该软件，以及在适当时停止该软件。

代理程序从相应的注册表轮询指定的边缘服务 Docker 容器映像，并验证容器映像签名。 接着，该代理程序将按模式或策略中指定的配置的相反依赖顺序启动容器。 在这些容器运行时，本地代理程序会监视它们。 如果有任何容器意外停止运行，该代理程序会重新启动该容器，以尝试使边缘节点上的模式或策略保持合规性。

代理程序承受失败的能力有限。 如果某个容器反复地快速崩溃，代理程序停止尝试重新启动不断失败的服务，并且将取消协议。

### {{site.data.keyword.horizon}} 服务依赖关系
{: #service_dependencies}

边缘服务可以在其元数据依赖性中指定其使用的其他边缘服务。 在将边缘服务部署到边缘节点作为模式或策略的结果时，代理程序还会部署其需要的所有边缘服务（以逆向依赖顺序）。 支持任意数量的服务依赖性级别。

### {{site.data.keyword.horizon}} Docker 联网
{: #docker_networking}

{{site.data.keyword.horizon}} 使用 Docker 联网功能来隔离 Docker 容器，因此只有需要容器的服务才能连接到容器。 在启动依赖于另一服务的服务容器时，服务容器将连接到相依服务容器的专用网络。 这有助于运行不同组织编写的边缘服务，因为每个边缘服务只能访问其元数据中列出的其他服务。
