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

# 安全与隐私
{: #security_privacy}

基于 [Open Horizon ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon) 的 {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) 使用多种不同的安全技术以确保可抵御攻击并保护隐私。 {{site.data.keyword.ieam}} 依赖于地理上的分布式自助代理程序进程来进行边缘软件管理。 因此，{{site.data.keyword.ieam}} 管理中心和代理程序均表示安全违规的潜在目标。 本文档阐述 {{site.data.keyword.ieam}} 如何缓解或消除威胁。
{:shortdesc}

## 管理中心
{{site.data.keyword.ieam}} 管理中心部署到 OpenShift Container Platform；因此，其继承所有已继承的安全机制收益。 所有 {{site.data.keyword.ieam}} 管理中心网络流量穿过受 TLS保护的入口点。 无需 TLS，即可执行 {{site.data.keyword.ieam}} 管理中心组件之间的管理中心网络通信。

## 保护控制平面
{: #dc_pane}

{{site.data.keyword.ieam}} 管理中心和分发的代理程序通过控制平面进行通信以向边缘节点部署工作负载和模型。 相较于典型的集中式物联网 (IoT) 平台以及基于云的控制系统，{{site.data.keyword.ieam}} 控制平面尽最大可能去中心化。 系统中每个参与者的权限范围都受限制，仅每个参与者具有完成其任务所需的最低权限级别。 没有任何单一参与者可以断言对整个系统的控制权。 此外，单个参与者无法通过损害任何单个边缘节点、主机或软件组件来获取系统中所有边缘节点的访问权。

控制平面由三个不同的软件实体实现：
* Open {{site.data.keyword.horizon}} 代理程序
* Open {{site.data.keyword.horizon}} agbot
* Open {{site.data.keyword.horizon_exchange}}

Open {{site.data.keyword.horizon}} 代理程序和 agbot 是控制平面中的主要参与者。 {{site.data.keyword.horizon_exchange}} 促进代理程序与 agbot 之间的发现和安全通信。 而且，他们通过使用被称为“完美前向保密”的算法提供消息级别保护。

缺省情况下，代理程序和 agbot 通过 TLS 1.3 与 Exchange 通信。 但是，TLS 自身不提供足够的安全性。 {{site.data.keyword.ieam}} 先加密在代理程序和 agbot 之间流动的每条控制消息，然后再通过网络就进行发送。 每个代理程序和 agbot 生成一个 2048 位 RSA 密钥对并在 Exchange 中发布其公用密钥。 专用密钥存储在每个参与者的根受保护的存储器中。 系统中的其他参与者使用消息接收器的公用密钥来加密用于加密控制平面消息的对称密钥。 这确保仅目标接收方可解密对称密钥；也就是，消息自身。 控制平面中使用的“完美前向保密”提供额外安全性，例如，阻止中间人攻击，而 TLS 无法阻止。

### 代理程序
{: #agents}

{{site.data.keyword.horizon_open}} 代理程序的数量超过 {{site.data.keyword.ieam}} 中的所有其他参与者。 代理程序在每个受管边缘节点上运行。 每个代理程序仅有权管理此边缘节点。 受损的代理程序不具有影响任何其他边缘节点或系统中任何其他组件的任何权限。 每个节点具有存储在其自己的根受保护存储器中的唯一凭证。 {{site.data.keyword.horizon_exchange}} 确保节点只能访问其自己的资源。 在通过使用 `hzn register` 命令注册节点时，可以提供认证令牌。 但是，最佳实践是允许代理程序生成其自己的令牌，从而使任何人都不知道节点凭证，这可以降低损害边缘节点的可能性。

代理程序不受网络攻击影响，因为其不侦听主机网络上的任何端口。 代理程序与管理中心之间的所有通信都由轮询管理中心的代理程序完成。 此外，强烈鼓励用户利用网络防火墙保护边缘节点，这可阻止侵入节点的主机。 通过这些保护，如果代理程序的主机操作系统或代理程序进程自身遭黑客攻击或受其他损害，那么只有该边缘节点受损。 {{site.data.keyword.ieam}} 系统的所有其他部分不受影响。

代理程序负责下载和启动容器化工作负载。 要确保下载的容器映像及其配置未受损，代理程序验证容器映像数字签名和部署配置数字签名。 当容器存储在容器注册表中时，注册表提供映像的数字签名（例如，SHA256 散列）。 容器注册表管理用于创建签名的密钥。 在使用 `hzn exchange service publish` 命令发布 {{site.data.keyword.ieam}} 服务时，其获取映像签名并与已发布的服务一起存储在 {{site.data.keyword.horizon_exchange}} 中。 通过安全控制平面将映像的数字签名传递到代理程序，这允许代理程序针对下载的映像验证容器映像签名。 如果映像签名不匹配映像，那么代理程序不启动容器。 容器配置的过程类似，但是有一个例外。 `hzn exchange service publish` 命令对容器配置进行签名，并将签名存储在 {{site.data.keyword.horizon_exchange}} 中。 在此情况下，用户（发布服务）必须提供用于创建签名的 RSA 密钥对。 如果用户尚无任何密钥，那么 `hzn key create` 命令可用于针对此目的生成密钥。 公用密钥与容器配置的签名一起存储在 Exchange 中，并通过安全控制平面传递到代理程序。 然后，代理程序可以使用公用密钥来验证容器配置。 如果您更愿意对每个容器配置使用不同密钥对，那么现在可以丢弃用于签署此容器配置的专用密钥，因为不再需要。 请参阅[开发边缘服务](../developing/developing_edge_services.md)以获取有关发布工作负载的更多详细信息。

在将模型部署到边缘节点时，代理程序下载模型并将其存储在主机上根受保护的存储器中。 当代理程序启动服务时，向每个服务提供一个凭证。 服务使用此凭证以标识自身并支持访问允许服务访问的模型。 {{site.data.keyword.ieam}} 中的每个模型对象指示可访问模型的服务列表。 在 {{site.data.keyword.ieam}} 每次重新启动服务时，每个服务获取一个新凭证。 {{site.data.keyword.ieam}} 不加密模型对象。 因为 {{site.data.keyword.ieam}} 将模型对象视为一个比特包，服务实施可自由地加密模型（如果需要）。 有关如何使用 MMS 的更多信息，请参阅[模型管理详细信息](../developing/model_management_details.md)。

### agbot
{: #agbots}

{{site.data.keyword.ieam}} 管理中心包含 agbot 的多个实例，其负责启动到使用管理中心注册的所有边缘节点的工作负载的部署。 Agbot 定期查找已发布到到 Exchange 的所有部署策略和模式，确保在所有正确的边缘节点上部署这些模式和策略中的服务。 在 agbot 启动部署请求时，其通过安全控制平面发送请求。 部署请求包含代理程序验证工作负载及其配置（代理程序决定是否接受请求）所需的一切。 请参阅[代理程序](security_privacy.md#agents)以获取有关代理程序执行的事项的安全性详细信息。 Agbot 还会将 MMS 定向到部署模型的位置和时间。 请参阅[代理程序](security_privacy.md#agents)以获取有关如何管理模型的安全性详细信息。

受损的 agbot 可能尝试恶意工作负载部署，但是提议的部署必须满足代理程序部分中规定的安全需求。 即使 agbot 启动工作负载部署，但是其无权创建工作负载和容器配置，因此无法提出其自己的恶意工作负载。

## {{site.data.keyword.horizon_exchange}}
{: #exchange}

{{site.data.keyword.horizon_exchange}} 是集中式、已复制且已负载均衡的 REST API 服务器。 其用作用户、组织、边缘节点、已发布的服务、策略和模式的共享元数据数据库。 其还通过针对安全控制平面提供存储器，支持分布式代理程序和 agbot 以部署容器化工作负载，直至消息可检索。 {{site.data.keyword.horizon_exchange}} 无法读取控制消息，因为其不控制专用 RSA 密钥来解密消息。 因此，受损的 {{site.data.keyword.horizon_exchange}} 无法监视控制平面流量。 有关 Exchange 角色的更多信息，请参阅 [{{site.data.keyword.edge}} 概述](../getting_started/overview_ieam.md)。

## 拒绝服务攻击
{: #denial}

{{site.data.keyword.ieam}} 管理中心是集中式服务。 基于典型云的环境的集中式服务通常容易受到拒绝服务攻击。 仅在代理程序首次注册到中心时或者在协商工作负载部署时，才需要连接。 在所有其他时间，代理程序持续正常运行，即使与 {{site.data.keyword.ieam}} 管理中心断开连接。  这确保即使管理中心遭到攻击，{{site.data.keyword.ieam}} 代理程序仍在边缘节点上保持活动。

### 模型管理系统

{{site.data.keyword.ieam}} 对上载到 MMS 的数据不执行恶意软件或病毒扫描。请确保已扫描任何上载数据，然后再将其上载到 MMS。

## 静态数据
{: #drest}

{{site.data.keyword.ieam}} 不加密静态数据。 应该使用适合 {{site.data.keyword.ieam}} 管理中心或代理程序运行所在的主机操作系统的实用程序来实施静态数据加密。

## 安全性标准
{: #standards}

在 {{site.data.keyword.ieam}} 中使用以下安全性标准：
* TLS 1.2 (HTTPS) 用于进出管理中心的动态数据加密。
* AES 256 位加密用于动态数据，尤其是流经安全控制平面的消息。
* 2048 位 RSA 密钥对用于动态数据，尤其是流经安全控制平面的 AES 256 对称密钥。
* 用户提供的 RSA 密钥提用于在使用 **hzn exchange service publish** 命令时对容器部署配置进行签名。
* RSA 密钥对由 **hzn key create** 命令（如果用户选择使用此命令）生成。 缺省情况下，此密钥的位大小为 4096，但是用户可进行更改。

## 摘要
{: #summary}

{{site.data.keyword.edge_notm}} 使用散列、加密签名和加密来确保安全性，避免不必要的访问。 通过在根本上实现分散化，{{site.data.keyword.ieam}} 可以避免您遭受边缘计算环境中常见的大部分攻击。 通过限制参与者角色的权限范围，{{site.data.keyword.ieam}} 可将受损主机或受损软件组件的潜在损害限制在系统的相应部分。 即使 {{site.data.keyword.ieam}} 中使用的 {{site.data.keyword.horizon}} 服务的集中式服务遭到大规模外部攻击，对边缘上的工作负载执行也只有最轻微的影响。
