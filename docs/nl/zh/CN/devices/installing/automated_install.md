---

copyright:
years: 2020
lastupdated: "2020-5-10"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 自动代理程序安装和注册
{: #method_one}

注：对于所有设备类型（体系结构），这些步骤都是相同的。

1. 从管理员处获取 **agentInstallFiles-&lt;edge-device-type&gt;.tar.gz** 文件和 API 密钥。 管理员应该已在[为边缘设备收集必要的信息和文件](../../hub/gather_files.md#prereq_horizon)部分中进行了创建。 使用安全复制命令、USB 记忆棒或其他方法将此文件复制到边缘设备。 另外，请记录 API 密钥值。 在后续步骤中需要该密钥值。然后，在环境变量中为后续步骤设置文件名：

   ```bash
   export AGENT_TAR_FILE=agentInstallFiles-<edge-device-type>.tar.gz
   ```
   {: codeblock}

2. 从 tar 文件抽取 **agent-install.sh** 命令：

   ```bash
   tar -zxvf $AGENT_TAR_FILE agent-install.sh
   ```
   {: codeblock}

3. 导出 {{site.data.keyword.horizon}} Exchange 用户凭证（API 密钥）：

  ```bash
  export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
  ```
  {: codeblock}

4. 运行 **agent-install.sh** 命令以安装和配置 {{site.data.keyword.horizon}} 代理程序，并注册边缘设备以运行 helloworld 样本边缘服务：

  ```bash
  sudo -s ./agent-install.sh -i . -u $HZN_EXCHANGE_USER_AUTH -p IBM/pattern-ibm.helloworld -w ibm.helloworld -o IBM -z $AGENT_TAR_FILE
  ```
  {: codeblock}

  注：在安装代理程序软件包期间，可能会提示您回答以下问题：“要覆盖当前节点配置吗？`[y/N]`：”您可以回答“y”并按 Enter 键，因为 **agent-install.sh** 将正确设置配置。

  要查看所有可用的 **agent-install.sh** 标志描述：

  ```bash
  ./agent-install.sh -h
  ```
  {: codeblock}

5. 安装和注册边缘设备后，在 Shell 中，将特定信息设置为环境变量。 这将使您能够运行 **hzn** 命令以查看 helloworld 输出：

  ```bash
  eval export $(cat agent-install.cfg)
  hzn service log -f ibm.helloworld
  ```
  {: codeblock}
  
  注：按 **Ctrl** **C** 以停止输出显示。

6. 浏览 **hzn** 命令的标志和子命令：

  ```bash
  hzn --help
  ```
  {: codeblock}

7. 您还可以使用 {{site.data.keyword.ieam}} 控制台查看边缘节点（设备）、服务、模式和策略。请参阅[使用管理控制台](../getting_started/accessing_ui.md)。

8. 浏览到 [CPU 使用量到 IBM Event Streams](cpu_load_example.md) 以继续执行其他边缘服务示例。
