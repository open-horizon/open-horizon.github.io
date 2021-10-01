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

# 更新代理程序
{: #updating_the_agent}

如果您已收到更新的 {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) 代理程序软件包，那么可以轻松更新边缘设备：

1. 执行[为边缘设备收集必要的信息和文件](../hub/gather_files.md#prereq_horizon)中的步骤，以使用较新的代理程序软件包来创建更新的 **agentInstallFiles-&lt;edge-device-type&gt;.tar.gz** 文件。
  
2. 对于每个边缘设备，执行[自动代理程序安装和注册](automated_install.md#method_one)中的步骤，但在运行 **agent-install.sh** 命令时，指定要在边缘设备上运行的服务和模式或策略。
