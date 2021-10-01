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

边缘设备提供了企业或服务提供者核心网络的入口点。 示例包括智能手机、监控摄像头，甚至已连接因特网的微波炉。

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) 可用于管理中心或服务器，包括分布式设备。 请参阅以下部分，以获取有关如何在边缘设备上安装 {{site.data.keyword.ieam}} 轻量级代理程序的详细信息：

* [准备边缘设备](../installing/adding_devices.md)
* [安装代理程序](../installing/registration.md)
* [更新代理程序](../installing/updating_the_agent.md)

所有边缘设备（边缘节点）都需要安装 {{site.data.keyword.horizon_agent}} 软件。 {{site.data.keyword.horizon_agent}} 还取决于 [Docker ![在新选项卡中打开](../../images/icons/launch-glyph.svg "在新选项卡中打开")](https://www.docker.com/) 软件。 

聚焦于边缘设备，下图显示为设置边缘设备将执行的步骤的流程以及代理程序在启动后将执行的操作。

<img src="../../images/edge/05a_Installing_edge_agent_on_device.svg" width="80%" alt="{{site.data.keyword.horizon_exchange}}、agbots 和代理程序">
