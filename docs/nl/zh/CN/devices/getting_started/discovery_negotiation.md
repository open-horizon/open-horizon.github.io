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

# 发现与协商
{: #discovery_negotiation}

{{site.data.keyword.edge_devices_notm}} 是以 {{site.data.keyword.horizon_open}} 项目为基础，它在根本上具备分散式和分布式特征。自主代理程序进程与协议自动程序 (agbot) 进程相互协作，完成所有已注册的边缘节点的软件管理工作。{:shortdesc}

有关 {{site.data.keyword.horizon_open}} 项目的更多信息，请参阅 [{{site.data.keyword.horizon_open}}](https://github.com/open-horizon/)。

在每个 Horizon 边缘节点上都会运行自主代理程序进程，用于强制实施边缘机器所有者所设置的策略。

同时，自主 agbot 进程（分配给每一种软件部署模式）使用针对所分配模式定义的策略，找出针对该模式注册的边缘节点代理程序。这些自主 agbot 和代理程序均独立遵循边缘机器所有者策略，以议定正式的协议来进行协作。每当 agbot 与代理程序达成协议时，它们就会进行协作，以管理相应边缘节点的软件生命周期。

agbot 和代理程序使用下列集中式服务来彼此找到对方，建立信任，然后在 {{site.data.keyword.edge_devices_notm}} 上安全地进行通信：

* {{site.data.keyword.horizon_switch}}：在 agbot 与代理程序之间启用安全且私密的对等通信。
* {{site.data.keyword.horizon_exchange}}：用于促进发现。

<img src="../../images/edge/distributed.svg" width="90%" alt="集中式服务和分散式服务">

## {{site.data.keyword.horizon_exchange}}

{{site.data.keyword.horizon_exchange}} 使边缘机器所有者能够注册边缘节点，以便进行软件生命周期管理。向 {{site.data.keyword.horizon_exchange}} for {{site.data.keyword.edge_devices_notm}} 注册边缘节点时，请为该边缘节点指定部署模式。部署模式是一组策略，用于管理边缘节点、进行加密签名的软件清单以及任何相关配置。部署模式必须在 {{site.data.keyword.horizon_exchange}} 上进行设计、开发、测试、签署和发布。

每个边缘节点必须在边缘机器所有者的组织之下向 {{site.data.keyword.horizon_exchange}} 注册。每个边缘节点都使用仅适用于该节点的标识和安全令牌进行注册。节点可以注册为运行它们自己的组织所提供的软件部署模式，或者运行由另一组织提供的模式（如果该部署模式可公开获得）。

当部署模式发布到 {{site.data.keyword.horizon_exchange}} 时，将分配一个或多个 agbot 来管理该部署模式以及任何相关策略。这些 agbot 会尝试发现任何针对该部署模式注册的边缘节点。找到已注册的边缘节点时，agbot 将与该边缘节点的本地代理程序进程进行协商。

虽然 {{site.data.keyword.horizon_exchange}} 使 agbot 能够找到与注册的部署模式对应的边缘节点，但
{{site.data.keyword.horizon_exchange}} 并不直接参与边缘节点软件管理过程。软件管理过程由 agbot
和代理程序处理。{{site.data.keyword.horizon_exchange}} 在边缘节点上不具有权限，不会向边缘节点代理程序发起任何联系。

## {{site.data.keyword.horizon_switch}}

agbot 定期轮询 {{site.data.keyword.horizon_exchange}}，以查找所有针对其部署模式注册的边缘节点。当 agbot 发现针对其部署模式注册的边缘节点时，agbot 会使用 {{site.data.keyword.horizon}} Switchboard 向该节点上的代理程序发送一条私有消息。该消息是向该代理程序发出的协作请求，即，请求就该边缘节点的软件生命周期管理进行协作。同时，该代理程序会轮询其在 {{site.data.keyword.horizon_switch}} 上的私有邮箱，以获取 agbot 消息。收到消息时，该代理程序会进行解密、验证和响应，以接受该请求。

除轮询 {{site.data.keyword.horizon_exchange}} 之外，每个 agbot 还会轮询其在 {{site.data.keyword.horizon_switch}}
中的私有邮箱。当 agbot 收到代理程序接受请求的响应时，协商随即完成。

代理程序和 agbot 都与 {{site.data.keyword.horizon_switch}} 共享公用密钥，以进行安全的私密通信。在这种加密中，{{site.data.keyword.horizon_switch}}
仅充当邮箱管理器。所有消息先由发送方加密，再发送到
{{site.data.keyword.horizon_switch}}。{{site.data.keyword.horizon_switch}} 无法对消息进行解密。但是，接收方可以将任何使用其公用密钥进行加密的消息解密。此外，接收方还使用发送方的公用密钥，对接收方发送给发送方的应答进行加密。

**注：**因为所有通信都通过 {{site.data.keyword.horizon_switch}} 进行代理，直到每个边缘节点上的代理程序选择公开边缘节点的 IP 地址之后，才会将该信息透露给任何 agbot。当代理程序与 agbot 成功议定协议时，代理程序就会公开这些信息。

## 软件生命周期管理

当边缘节点针对特定部署模式向 {{site.data.keyword.horizon_exchange}} 注册后，该部署模式的 agbot 就可以找到该边缘节点上的代理程序。部署模式的 agbot 使用 {{site.data.keyword.horizon_exchange}} 来查找代理程序，并使用 {{site.data.keyword.horizon_switch}} 与该代理程序协商，以便协作进行软件管理。

边缘节点代理程序接收来自 agbot 的协作请求，并评估建议，以确保其符合边缘节点所有者所定义的策略。该代理程序使用安装在本地的密钥文件来验证加密签名。如果根据本地策略可接受该建议，而且签名通过验证，该代理程序就会接受该建议，然后与 agbot 达成协议。 

达成协议后，agbot 与代理程序协作管理该边缘节点上部署模式的软件生命周期。agbot
提供部署模式随时间演变的详细信息，并监视该边缘节点的合规性。代理程序将软件下载到边缘节点本地，验证该软件的签名，如果已获核准，则运行并监视该软件。如有必要，代理程序会更新该软件，以及在适当时停止该软件。

有关软件管理过程的更多信息，请参阅[边缘软件管理](edge_software_management.md)。
