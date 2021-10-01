---

copyright:
years: 2019
lastupdated: "2019-06-25"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 故障诊断
{: #troubleshooting}

查看故障诊断提示和 {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) 可能出现的常见问题，以帮助您对遇到的任何问题进行故障诊断。
{:shortdesc}

以下故障诊断指南描述 {{site.data.keyword.ieam}} 系统的主要组件，以及如何调查随附的界面以确定系统状态。

## 故障诊断工具
{: #ts_tools}

{{site.data.keyword.ieam}} 随附的许多界面会提供可用于诊断问题的信息。 这些信息可通过 {{site.data.keyword.gui}}、HTTP REST API 和 {{site.data.keyword.linux_notm}} Shell 工具 `hzn` 获得。

在边缘机器上，可能需要对主机问题、Horizon 软件问题、Docker 问题、配置中的问题或者服务容器中的代码进行故障诊断。 边缘机器主机问题超出本文档的范围。 如果需要对 Docker 问题进行故障诊断，有许多 Docker 命令和界面可供使用。 有关更多信息，请参阅 Docker 文档。

如果您所运行的服务容器使用 {{site.data.keyword.message_hub_notm}}（基于 Kafka）进行消息传递，您可手动连接到 {{site.data.keyword.ieam}} 的 Kafka 流，以便诊断问题。 您可以预订消息主题以观察 {{site.data.keyword.message_hub_notm}} 所接收到的内容，也可以发布到消息主题以模拟来自其他设备的消息。 `kafkacat` {{site.data.keyword.linux_notm}} 命令是发布到 {{site.data.keyword.message_hub_notm}} 或对其进行预订的简单方法。 请使用此工具的最新版本。 {{site.data.keyword.message_hub_notm}} 还提供有可用于访问某些信息的图形 Web 页面。

在任何安装有 {{site.data.keyword.horizon}} 的机器上，使用 `hzn` 命令可调试本地 {{site.data.keyword.horizon}} 代理程序和远程 {{site.data.keyword.horizon_exchange}} 的问题。 `hzn` 命令以内部方式与提供的 HTTP REST API 进行交互。 `hzn` 命令可简化访问，并提供优于 REST API 本身的用户体验。 `hzn` 命令往往会在其输出中提供更具描述性的文本，而且随附内置的联机帮助系统。 使用该帮助系统可获取有关所需使用的命令的信息和详细资料，以及有关命令语法和自变量的详细信息。 要查看这些帮助信息，请运行 `hzn --help` 或 `hzn \<subcommand\> --help` 命令。

在不支持或未安装 {{site.data.keyword.horizon}} 软件包的节点上，可以改为直接与底层 HTTP REST API 进行交互。 例如，可以使用 `curl` 实用程序或其他 REST API CLI 实用程序。 您还可以使用支持 REST 查询的语言来编写程序。 

## 故障诊断提示
{: #ts_tips}

为帮助您诊断特定问题，请查看有关系统状态的提问，以及有关以下主题的任何关联提示。 对于每个提问，将会描述该提问与系统故障诊断相关的原因。 对于某些提问，提供了提示或详细指南，以帮助您了解如何获取系统的相关信息。

这些提问基于调试问题的性质，并与不同环境相关。 例如，在边缘节点上诊断问题时，您可能需要该节点的完全访问权和控制权，这可提升您收集和查看信息的能力。

* [故障诊断提示](troubleshooting_devices.md)

  查看您使用 {{site.data.keyword.ieam}} 时可能遇到的常见问题。
