---

copyright:
years: 2020
lastupdated: "2020-4-8"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 边缘设备
{: #edge_devices}

# 准备工作

了解使用边缘设备的先决条件：

* [准备边缘设备](#adding-devices)
* [受支持的体系结构和操作系统](#suparch-horizon)
* [大小调整](#size)

注：边缘设备又被称为代理程序。 请参阅“编写者备份”以获取边缘设备和集群的描述。

## 准备边缘设备
{: #adding-devices}

{{site.data.keyword.edge_devices_notm}} 使用 [{{site.data.keyword.horizon_open}} ![在新选项卡中打开](../../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon/) 项目软件。 边缘设备上的 {{site.data.keyword.horizon_agents}} 与其他 {{site.data.keyword.horizon}} 组件通信，以在其设备上安全地编排软件生命周期管理。
{:shortdesc}

下图显示 {{site.data.keyword.horizon}} 中各个组件之间的典型交互。

<img src="../../images/edge/installers.svg" width="90%" alt="{{site.data.keyword.horizon}} 中的组件交互">

所有边缘设备（边缘节点）都需要安装 {{site.data.keyword.horizon_agent}} 软件。 {{site.data.keyword.horizon_agent}} 还取决于 [Docker ![在新选项卡中打开](../../images/icons/launch-glyph.svg "在新选项卡中打开")](https://www.docker.com/) 软件。 

聚焦于边缘设备，下图显示为设置边缘设备将执行的步骤的流程以及代理程序在启动后将执行的操作。

<img src="../../images/edge/registration.svg" width="80%" alt="{{site.data.keyword.horizon_exchange}}、agbot 和代理程序">

下列指示信息指导您完成在边缘设备上安装必需软件并使用 {{site.data.keyword.edge_devices_notm}} 进行注册的过程。

## 受支持的体系结构和操作系统
{: #suparch-horizon}

{{site.data.keyword.edge_devices_notm}} 支持采用以下硬件体系结构的系统：

* {{site.data.keyword.linux_bit_notm}} 设备或虚拟机，运行 Ubuntu 18.x (bionic)、Ubuntu 16.x (xenial)、Debian 10 (buster) 或 Debian 9 (stretch)
* {{site.data.keyword.linux_notm}} on ARM（32 位），例如，运行 Raspbian buster 或 stretch 的 Raspberry Pi
* {{site.data.keyword.linux_notm}} on ARM（64 位），例如，运行 Ubuntu 18.x (bionic) 的 NVIDIA Jetson Nano、TX1 或 TX2
* {{site.data.keyword.macOS_notm}}

## 调整大小
{: #size}

代理程序需要：

1. 100 MB RAM（包括 Docker）。 高于此容量的 RAM 增长为每个协议约 100 K，加上在节点上运行的工作负载所需的任何额外内存。
2. 400 MB 磁盘（包括 Docker）。 高于此容量的磁盘增长基于工作负载使用的容器映像大小以及部署到节点的模型对象的大小（乘以 2）。

## 下一步是什么

[安装代理程序](installing_the_agent.md)
