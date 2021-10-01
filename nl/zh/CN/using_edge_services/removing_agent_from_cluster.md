---

copyright:
years: 2020
lastupdated: "2020-8-25"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 从边缘集群中移除代理程序
{: #remove_agent}

要注销边缘集群并从该集群中移除 {{site.data.keyword.ieam}} 代理程序，请执行以下步骤：

1. 从 tar 文件解压缩 **agent-uninstall.sh** 脚本：

   ```bash
   tar -zxvf agentInstallFiles-x86_64-Cluster.tar.gz agent-uninstall.sh
   ```
   {: codeblock}

2. 导出 Horizon Exchange 用户凭证：

   ```bash
   export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
   ```
   {: codeblock}

3. 移除代理程序：

   ```bash
   ./agent-uninstall.sh -u $HZN_EXCHANGE_USER_AUTH -d
   ```
   {: codeblock}

注：删除名称空间有时会停留在“正在终止”状态。 在这种情况下，请参阅[名称空间陷入“正在终止”状态 ![在新的选项卡中打开](../images/icons/launch-glyph.svg "在新的选项卡中打开")](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.1.1/troubleshoot/ns_terminating.html) 以手动删除名称空间。
