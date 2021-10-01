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

# 边缘软件管理
{: #edge_software_mgmt}

{{site.data.keyword.edge_devices_notm}} 依赖于地理上的分布式自主进程来管理所有边缘节点的软件生命周期。{:shortdesc}

处理边缘节点软件管理的自主进程使用 {{site.data.keyword.horizon_exchange}} 和 {{site.data.keyword.horizon_switch}} 服务在因特网上找到彼此，但不透露它们的地址。找到彼此之后，该进程使用 {{site.data.keyword.horizon_exchange}} 和 {{site.data.keyword.horizon_switch}} 来协商关系，然后协作管理边缘节点软件。有关更多信息，请参阅[发现与协商](discovery_negotiation.md)。

任何主机上的 {{site.data.keyword.horizon}} 软件都可以充当边缘节点代理程序和/或 agbot。

## agbot（协议自动程序）

agbot 实例集中创建，用于管理发布到 {{site.data.keyword.horizon_exchange}} 的各个 {{site.data.keyword.edge_devices_notm}} 软件部署模式。此外，您或其中一位开发者也可以在任何可以访问 {{site.data.keyword.horizon_exchange}} 和 {{site.data.keyword.horizon_switch}} 的机器上运行 agbot 进程。

当 agbot 启动并配置为管理特定的软件部署模式时，该 agbot 就会向 {{site.data.keyword.horizon_exchange}} 注册，并开始轮询注册为运行同一部署模式的边缘节点。发现边缘节点时，该 agbot 就会向该边缘节点上的本地代理程序发送请求，以协作管理软件。

议定协议时，该 agbot 会向该代理程序发送以下信息：

* 包含在部署模式中的策略详细信息。
* 包括在部署模式中的 {{site.data.keyword.horizon}} 服务和版本的列表。
* 这些服务之间的任何依赖关系。
* 这些服务的可共享性。服务可以设置为 `exclusive`、`singleton` 或 `multiple`。
* 每个服务的每个容器的相关详细信息。这些详细信息包括下列信息： 
  * 注册容器所在的 Docker 注册表，例如公用 DockerHub 注册表或私有注册表。
  * 私有注册表的注册表凭证。
  * 有关配置和定制的 Shell 环境详细信息。
  * 该容器及其配置的散列（进行加密签名）。

该 agbot 会继续监视 {{site.data.keyword.horizon_exchange}} 中的软件部署模式是否有任何更改，例如是否为该模式发布了新版 {{site.data.keyword.horizon}} 服务。如果检测到更改，那么该 agbot 将再次向每个针对该模式注册的边缘节点发送请求，以协作进行管理，从而过渡到新软件版本。

该 agbot 还会定期检查每个针对该部署模式注册的边缘节点，以确保强制实施该模式的任何策略。当有策略未得到强制实施时，该 agbot 可以将议定的协议停止。例如，如果该边缘节点停止发送数据或提供脉动信号的时间已较长，那么该 agbot 可以取消该协议。  

### 边缘节点代理程序

在边缘机器上安装 {{site.data.keyword.horizon}} 软件包时，边缘节点代理程序随即创建。有关安装该软件的更多信息，请参阅[安装 {{site.data.keyword.horizon}} 软件](../installing/adding_devices.md)。

稍后，在向 {{site.data.keyword.horizon_exchange}} 注册边缘节点时，必须提供以下信息：

* {{site.data.keyword.horizon_exchange}} URL。
* 边缘节点名称，以及该边缘节点的访问令牌。
* 在该边缘节点上运行的软件部署模式。您必须同时提供组织和模式名称才能识别该模式。

有关注册的更多信息，请参阅[注册边缘机器](../installing/registration.md)。

注册边缘节点之后，本地代理程序会轮询 {{site.data.keyword.horizon_switch}}，以获取来自远程 agbot 进程的协作请求。当该代理程序由一个对应于其部署模式的 agbot 发现时，该 agbot 就会向边缘节点代理程序发送一个请求，以协商就该边缘节点的软件生命周期管理进行协作。达成协议时，该 agbot 会向该边缘节点发送信息。

该代理程序会从相应的注册表中提取指定的 Docker 容器。然后，该代理程序会验证容器散列和加密签名。接着，该代理程序将按所指定环境配置的相反依赖顺序启动容器。在这些容器运行时，本地代理程序会监视它们。如果有任何容器意外停止运行，该代理程序会重新启动该容器，以尝试使边缘节点上的部署模式保持不变。

### {{site.data.keyword.horizon}} 服务依赖关系

尽管 {{site.data.keyword.horizon}} 代理程序按指定的部署模式来启动和管理容器，但在服务容器代码中，必须对服务之间的依赖关系进行管理。尽管容器以相反依赖顺序启动，{{site.data.keyword.horizon}} 无法确保在服务使用者启动之前，服务提供者已完全启动并准备好提供服务。使用者必须战略性地处理它们所依赖的服务有可能启动迟缓的问题。因为提供容器的服务可能会失败并变为禁用，服务使用者还必须处理它们所要使用的服务不存在的情况。 

本地代理程序会检测到服务崩溃的情况，并且会在同一个 Docker 专用网络上，以相同的网络名称启动该服务。在重新启动过程中，有短暂的停机时间。使用者服务还必须处理这个短暂的停机时间，否则使用者服务也可能失败。

代理程序承受失败的能力有限。如果某个容器反复地快速崩溃，代理程序可能会放弃重新启动不断失败的服务，并可以取消协议。

### {{site.data.keyword.horizon}} Docker 联网

{{site.data.keyword.horizon}} 使用 Docker 联网功能来隔离提供服务的 Docker 容器。这种隔离可确保只有获得授权的使用者才能访问容器。每个容器都以相反依赖顺序（生产者居先，使用者居后），在单独的专用
Docker 虚拟网络上启动。每当使用服务的容器启动时，该容器会连接到其生产者容器的专用网络。生产者容器只能由那些与生成者的依赖关系可以被 {{site.data.keyword.horizon}}
识别的使用者访问。基于实现 Docker 网络的方式，所有容器都可以从主机 Shell 访问。 

如果您需要获取任何容器的 IP 地址，您可使用 `docker inspect <containerID>` 命令来获取分配的 `IPAddress`。您可以从主机 Shell 访问任何容器。

## 安全性与隐私

虽然边缘节点代理程序和部署模式 agbot 可以彼此发现，但在正式议定协作协议之前，这些组件会保持完全保密。代理程序和
agbot 身份以及所有通信都会进行加密。软件管理协作也会进行加密。所有受管软件都会进行加密签名。有关 {{site.data.keyword.edge_devices_notm}}
的保密和安全方面的更多信息，请参阅[安全与保密](../user_management/security_privacy.md)。
