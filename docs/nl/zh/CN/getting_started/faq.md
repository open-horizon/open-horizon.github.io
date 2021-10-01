---

copyright:
years: 2020
lastupdated: "2020-04-21"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 常见问题
{: #faqs}

以下是有关 {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) 的一些常见问题 (FAQ) 的解答。
{:shortdesc}

  * [是否有办法创建自包含环境以用于开发？](#one_click)
  * [{{site.data.keyword.ieam}} 软件是否开源？](#open_sourced)
  * [如何使用 {{site.data.keyword.ieam}} 开发和部署边缘服务？](#dev_dep)
  * [{{site.data.keyword.ieam}} 支持哪些边缘节点硬件平台？](#hw_plat)
  * [我可以使用 {{site.data.keyword.ieam}} 在我的边缘节点上运行任何 {{site.data.keyword.linux_notm}} 分发吗？](#lin_dist)
  * [{{site.data.keyword.ieam}} 支持哪些编程语言和环境？](#pro_env)
  * [{{site.data.keyword.ieam}} 中的组件是否提供 REST API 的详细文档？](#rest_doc)
  * [{{site.data.keyword.ieam}} 是否使用 Kubernetes？](#use_kube)
  * [{{site.data.keyword.ieam}} 是否使用 MQTT？](#use_mqtt)
  * [注册边缘节点之后，通常需要多长时间才能形成协议，并让相应的容器开始运行？](#agree_run)
  * [是否可以从边缘节点主机中移除 {{site.data.keyword.horizon}} 软件以及与 {{site.data.keyword.ieam}} 相关的所有其他软件或数据？](#sw_rem)
  * [是否有仪表板可将边缘节点上活动的协议和服务可视化？](#db_node)
  * [如果容器映像下载因网络中断而中止，怎么办？](#image_download)
  * [{{site.data.keyword.ieam}} 如何实现安全？](#ieam_secure)
  * [如何在带有模型的边缘上管理 AI 以及在云上管理 AI？](#ai_cloud)

## 是否有办法创建自包含环境以用于开发？
{: #one_click}

您可以使用适用于开发人员的“一体化”安装程序来安装开放式源代码管理中心（不使用 {{site.data.keyword.ieam}} 管理控制台）。 此一体化安装程序创建完整但最小的管理中心，不适用于生产用途。 它还配置示例边缘节点。 此工具使开放式源代码组件开发人员能够快速开始，而不需要花费时间来配置完整的生产 {{site.data.keyword.ieam}} 管理中心。 有关一体化安装程序的信息，请参阅 [Open Horizon - Devops ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon/devops/tree/master/mgmt-hub)。

## {{site.data.keyword.ieam}} 软件是否开源？
{: #open_sourced}

{{site.data.keyword.ieam}} 是 IBM 产品。 但是，其核心组件主要使用 [Open Horizon - EdgeX Project Group ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://wiki.edgexfoundry.org/display/FA/Open+Horizon+-+EdgeX+Project+Group) 开放式源代码项目。 {{site.data.keyword.horizon}} 项目中提供的许多程序样本和示例可以用于 {{site.data.keyword.ieam}}。 有关该项目的更多信息，请参阅 [Open Horizon - EdgeX 项目组 ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://wiki.edgexfoundry.org/display/FA/Open+Horizon+-+EdgeX+Project+Group)。

## 如何使用 {{site.data.keyword.ieam}} 开发和部署边缘服务？
{: #dev_dep}

请参阅[使用边缘服务](../using_edge_services/using_edge_services.md)。

## {{site.data.keyword.ieam}} 支持哪些边缘节点硬件平台？
{: #hw_plat}

{{site.data.keyword.ieam}} 通过用于 {{site.data.keyword.horizon}} 的 Debian {{site.data.keyword.linux_notm}} 二进制软件包或通过 Docker 容器，支持不同的硬件体系结构。 有关更多信息，请参阅[安装 {{site.data.keyword.horizon}} 软件](../installing/installing_edge_nodes.md)。

## 我可以使用 {{site.data.keyword.ieam}} 在我的边缘节点上运行任何 {{site.data.keyword.linux_notm}} 分发吗？
{: #lin_dist}

可以，同时也不可以。

如果基本映像在边缘节点的主机 {{site.data.keyword.linux_notm}} 内核上运行，那么您可以开发使用任何 {{site.data.keyword.linux_notm}} 分发作为 Docker 容器的基本映像的边缘软件（如果使用 Dockerfile `FROM` 语句）。 这意味着您可以将任何分发用于 Docker 能够在边缘主机上运行的容器。

但是，边缘节点主机操作系统必须能够运行最新版本的 Docker 并且能够运行 {{site.data.keyword.horizon}} 软件。 当前，{{site.data.keyword.horizon}} 软件仅以针对运行 {{site.data.keyword.linux_notm}} 的边缘节点的 Debian 和 RPM 软件包的形式提供。 对于 Apple Macintosh 机器，提供一个 Docker 容器版本。 {{site.data.keyword.horizon}} 开发团队主要使用 Apple Macintosh、Ubuntu 或 Raspbian {{site.data.keyword.linux_notm}} 分发。

此外，已在使用 Red Hat Enterprise Linux (RHEL) V8.2 配置的边缘节点上测试 RPM 软件包安装。

## {{site.data.keyword.ieam}} 支持哪些编程语言和环境？
{: #pro_env}

{{site.data.keyword.ieam}} 支持几乎任何能够配置为在边缘节点上相应的 Docker 容器中运行的编程语言和软件库。

如果您的软件需要访问特定硬件或操作系统服务，您可能需要提供 `docker run` 等效自变量才能支持该访问。 您可以在 Docker 容器定义文件的 `deployment` 一节中指定受支持的自变量。

## {{site.data.keyword.ieam}} 中的组件是否会提供 REST API 的详细文档？
{: #rest_doc}

是的。 有关更多信息，请参阅 [{{site.data.keyword.ieam}} API](../api/edge_rest_apis.md)。 

## {{site.data.keyword.ieam}} 是否使用 Kubernetes？
{: #use_kube}

是的。 {{site.data.keyword.ieam}} 使用 [{{site.data.keyword.open_shift_cp}} ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://docs.openshift.com/container-platform/4.6/welcome/index.html) Kubernetes 服务。

## {{site.data.keyword.ieam}} 是否使用 MQTT？
{: #use_mqtt}

{{site.data.keyword.ieam}} 不使用消息排队遥测传输 (MQTT) 来支持其自己的内部功能，但是在边缘节点上部署的程序可自由地将 MQTT 用于其自己的目的。 提供使用 MQTT 和其他技术（例如，基于 Apache Kafka 的 {{site.data.keyword.message_hub_notm}}）以与边缘节点相互传输数据的示例程序。

## 注册边缘节点之后，通常需要多长时间才能形成协议，并让相应的容器开始运行？
{: #agree_run}

通常，在注册代理程序和远程 agbot 后仅需几秒钟即可最终完成协议以部署软件。 发生后，{{site.data.keyword.horizon}} 代理程序将容器下载 (`docker pull`) 到边缘节点，使用 {{site.data.keyword.horizon_exchange}} 验证其加密签名，然后运行它们。 根据容器的大小以及启动和正常运行所用的时间，可能只需要多几秒钟到几分钟边缘节点就会完全正常运行。

在注册边缘节点后，您可以运行 `hzn node list` 命令以查看边缘节点上 {{site.data.keyword.horizon}} 的状态。 在 `hzn node list` 命令显示状态为 `configured` 时，{{site.data.keyword.horizon}} agbot 能够发现边缘节点并开始形成协议。

要观察协议协商过程阶段，您可以使用 `hzn agreement list` 命令。

在协议列表最终完成后，您可以使用 `docker ps` 命令来查看正在运行的容器。 您还可以发出 `docker inspect <container>` 以查看有关任何特定 `<container>` 的部署的更多详细信息。

## 是否可以从边缘节点主机中移除 {{site.data.keyword.horizon}} 软件以及与 {{site.data.keyword.ieam}} 相关的所有其他软件或数据？
{: #sw_rem}

是的。 如果注册边缘节点，那么通过运行以下命令注销边缘节点： 
```
hzn unregister -f -r
```
{: codeblock}

在取消注册边缘节点时，您可以除去已安装的 {{site.data.keyword.horizon}} 软件，例如，对于基于 Debian 的系统，运行：
```
sudo apt purge -y bluehorizon horizon horizon-cli
```
{: codeblock}

## 是否有仪表板可将边缘节点上活动的协议和服务可视化？
{: #db_node}

您可以使用 {{site.data.keyword.ieam}} Web UI 以观察边缘节点和服务。

此外，通过使用边缘节点上的本地 {{site.data.keyword.horizon}} 代理程序 REST API，可以使用 `hzn` 命令获取有关活动协议和服务的信息。 运行以下命令即可使用该 API 来检索相关信息：

```
hzn node list
hzn agreement list
docker ps
```
{: codeblock}

## 如果容器映像下载因网络中断而中止，怎么办？
{: #image_download}

使用 Docker API 来下载容器映像。 如果 Docker API 终止下载，它将向代理程序返回错误。 反过来，代理程序将取消当前部署尝试。 当 agbot 检测到取消，它将使用代理程序启动新的部署尝试。 在后续部署尝试期间，Docker API 从中断处恢复下载。 此过程继续，直到完全下载映像且部署可以继续。 Docker 绑定 API 负责映像拉取，在失败时，协议取消。

## {{site.data.keyword.ieam}} 如何实现安全？
{: #ieam_secure}

* {{site.data.keyword.ieam}} 在供应期间与 {{site.data.keyword.ieam}} 管理中心通信时，自动执行并使用边缘设备的以加密方式签名的公用-专用密钥认证。 通信始终由边缘节点启动和控制。
* 系统有节点和服务凭证。
* 使用散列验证来验证软件的真实性。

请参阅 [Security at the Edge ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://www.ibm.com/cloud/blog/security-at-the-edge)。

## 如何在带有模型的边缘上管理 AI 以及在云上管理 AI？
{: #ai_cloud}

通常，边缘上的 AI 支持您执行即时推断，等待时间为亚秒级，从而基于用例和硬件（例如，RaspberryPi、Intel x86 和 Nvidia Jetson nano）实现实时响应。 {{site.data.keyword.ieam}} 模型管理系统支持您部署更新的 AI 模型，而不会产生任何服务停机时间。

请参阅 [Models Deployed at the Edge ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://www.ibm.com/cloud/blog/models-deployed-at-the-edge)。
