---

copyright:
years: 2020
lastupdated: "2020-10-15"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 故障诊断提示和常见问题
{: #troubleshooting}

查看故障诊断提示和常见问题以帮助对可能遇到的问题进行故障诊断。
{:shortdesc}

* [故障诊断提示](troubleshooting_devices.md)
* [常见问题](../getting_started/faq.md)

以下故障诊断内容描述 {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) 的主要组件，以及如何调查随附的界面以确定系统状态。

## 故障诊断工具
{: #ts_tools}

{{site.data.keyword.ieam}} 随附的许多界面会提供可用于诊断问题的信息。 这些信息可通过 {{site.data.keyword.gui}}、HTTP REST API 和 {{site.data.keyword.linux_notm}} Shell 工具 `hzn` 获得。

在边缘节点上，可能需要对主机问题、Horizon 软件问题、Docker 问题、配置中的问题或者服务容器中的代码进行故障诊断。 边缘节点主机问题超出本文档的范围。 如果需要对 Docker 问题进行故障诊断，可以使用多个 Docker 命令和界面。 有关更多信息，请参阅 Docker 文档。

如果您所运行的服务容器使用 {{site.data.keyword.message_hub_notm}}（基于 Kafka）进行消息传递，您可手动连接到 {{site.data.keyword.ieam}} 的 Kafka 流，以便诊断问题。 您可以预订消息主题以观察 {{site.data.keyword.message_hub_notm}} 所接收到的内容，也可以发布到消息主题以模拟来自其他设备的消息。 `kafkacat` {{site.data.keyword.linux_notm}} 命令是发布到 {{site.data.keyword.message_hub_notm}} 或对其进行预订的一种方法。 请使用此工具的最新版本。 {{site.data.keyword.message_hub_notm}} 还提供有可用于访问某些信息的图形 Web 页面。

在任何安装有 {{site.data.keyword.horizon}} 的边缘节点上，使用 `hzn` 命令可调试本地 {{site.data.keyword.horizon}} 代理程序和远程 {{site.data.keyword.horizon_exchange}} 的问题。 `hzn` 命令以内部方式与提供的 HTTP REST API 进行交互。 `hzn` 命令可简化访问，并提供优于 REST API 本身的用户体验。 `hzn` 命令往往会在其输出中提供更具描述性的文本，而且随附内置的联机帮助系统。 使用该帮助系统可获取有关所需使用的命令的信息和详细资料，以及有关命令语法和自变量的详细信息。 要查看这些帮助信息，请运行 `hzn --help` 或 `hzn <subcommand> --help` 命令。

在不支持或未安装 {{site.data.keyword.horizon}} 软件包的边缘节点上，可以改为直接与底层 HTTP REST API 进行交互。 例如，可以使用 `curl` 实用程序或其他 REST API CLI 实用程序。 您还可以使用支持 REST 查询的语言来编写程序。

例如，运行 `curl` 实用程序以检查边缘节点的状态：
```
curl localhost:8510/status
```
{: codeblock}

## 故障诊断提示
{: #ts_tips}

为帮助您诊断特定问题，请查看有关系统状态的提问，以及有关以下主题的任何关联提示。 对于每个提问，将会描述该提问与系统故障诊断相关的原因。 对于某些提问，提供了提示或详细指南，以帮助您了解如何获取系统的相关信息。

这些提问基于调试问题的性质，并与不同环境相关。 例如，在边缘节点上诊断问题时，您可能需要该节点的完全访问权和控制权，这可提升您收集和查看信息的能力。

* [故障诊断提示](troubleshooting_devices.md)

  查看您使用 {{site.data.keyword.ieam}} 时可能遇到的常见问题。
  
## {{site.data.keyword.ieam}} 风险与解决方法
{: #risks}

虽然 {{site.data.keyword.ieam}} 会创建特有的机会，但它也会带来挑战。 例如，它超越了云数据中心的物理边界，从而能够暴露安全性、可寻址性、管理、所有权和合规性问题。 更重要的是，它使得基于云的管理技术的缩放问题得以倍增。

边缘网络按数量级增加计算节点数。 边缘网关按另一个数量级增加计算节点数。 边缘设备将该数字增加 3 到 4 个数量级。 如果 DevOps（持续交付和持续部署）对于管理超大规模云基础结构至关重要，那么零操作（没有人为干预的操作）则对于按照 {{site.data.keyword.ieam}} 所表示的大规模进行管理至关重要。

在没有人为干预的情况下部署、更新、监视和恢复边缘计算空间至关重要。 所有这些活动和过程都必须：

* 完全自动执行
* 能够独立制定有关工作分配的决策
* 无需干预即可识别不断变化的状况并从中恢复。

所有这些活动都必须安全、可跟踪并可防御。
