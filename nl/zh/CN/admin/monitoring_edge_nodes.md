---

copyright:
years: 2020
lastupdated: "2020-2-2"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 监视边缘节点和服务
{: #monitoring_edge_nodes_and_services}

[登录管理控制台](../console/accessing_ui.md)以监视 {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) 边缘节点和服务。

* 监视边缘节点：
  * “节点”仪表板是显示的第一个页面，其中包含显示所有边缘节点的状态的圆环图。
  * 要查看处于特定状态的所有节点，请在圆环图中单击相应的颜色。 例如，要查看含有错误（如果存在）的所有边缘节点，请单击图注指示用于**有错误**的颜色。
  * 将显示含有错误的节点的列表。 要向下钻取到一个节点以查看特定错误，请单击节点名。
  * 在显示的节点详细信息页面中，**边缘代理程序错误**部分显示有错误的服务、具体的错误消息和时间戳记。
* 监视边缘服务：
  * 在**服务**选项卡中，单击想要向下钻取到的服务，此服务显示边缘服务详细信息页面。
  * 在详细信息页面的**部署**部分中，可以查看将此服务部署到边缘节点的策略和模式。
* 监视边缘节点上的边缘服务：
  * 在**节点**选项卡中，切换到列表视图，然后单击要向下钻取到的边缘节点。
  * 在节点详细信息页面中，**服务**部分显示哪些边缘服务当前正在该边缘节点上运行。
