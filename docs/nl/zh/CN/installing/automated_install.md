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

注：对于所有边缘设备类型（体系结构），这些步骤都是相同的。

1. 如果尚未执行[准备设置边缘节点](../hub/prepare_for_edge_nodes.md)中的步骤，请立即执行。 此过程创建 API 密钥，查找某些文件，并收集设置边缘节点时所需的环境变量值。

2. 登录到边缘设备并设置在步骤 1 中获取的相同环境变量：

   ```bash
   export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
  export HZN_ORG_ID=<your-exchange-organization>
  export HZN_FSS_CSSURL=https://<ieam-management-hub-ingress>/edge-css/
   ```
   {: codeblock}

3. 如果您没有使用管理员准备的安装捆绑软件，请将 **agent-install.sh** 脚本从 Cloud Sync Service (CSS) 下载到您的设备并使其可执行：

   ```bash
   curl -u "$HZN_ORG_ID/$HZN_EXCHANGE_USER_AUTH" -k -o agent-install.sh $HZN_FSS_CSSURL/api/v1/objects/IBM/agent_files/agent-install.sh/data
   chmod +x agent-install.sh
   ```
   {: codeblock}

4. 运行 **agent-install.sh** 以从 CSS 获取必要文件，安装并配置 {{site.data.keyword.horizon}} 代理程序，然后注册边缘设备以运行 helloworld 样本边缘服务：

   ```bash
   sudo -s -E ./agent-install.sh -i 'css:' -p IBM/pattern-ibm.helloworld -w '*' -T 120
   ```
   {: codeblock}

   要查看所有可用的 **agent-install.sh** 标志描述，请运行：**./agent-install.sh -h**

   注：在 {{site.data.keyword.macOS_notm}} 上，代理程序将在作为根运行的 Docker 容器中运行。

5. 查看 helloworld 输出：

   ```bash
   hzn service log -f ibm.helloworld
  # Press Ctrl-c to stop the output display
   ```
   {: codeblock}

6. 如果 helloworld 边缘服务未启动，请运行此命令以查看错误消息：

   ```bash
   hzn eventlog list -f
  # Press Ctrl-c to stop the output display
   ```
   {: codeblock}

7. （可选）在此边缘节点上使用 **hzn** 命令以查看 {{site.data.keyword.horizon}} Exchange 中的服务、模式和部署策略。 在 shell 中，将特定信息设置为环境变量，然后运行这些命令：

   ```bash
   eval export $(cat agent-install.cfg)
  hzn exchange service list IBM/
  hzn exchange pattern list IBM/
  hzn exchange deployment listpolicy
   ```
   {: codeblock}

8. 浏览所有 **hzn** 命令标志和子命令：

   ```bash
   hzn --help
   ```
   {: codeblock}

## 下一步是什么

* 使用 {{site.data.keyword.ieam}} 控制台查看边缘节点（设备）、服务、模式和策略。 有关更多信息，请参阅[使用管理控制台](../console/accessing_ui.md)。
* 探索并运行另一个边缘服务示例。 有关更多信息，请参阅 [CPU 使用量到 IBM Event Streams](../using_edge_services/cpu_load_example.md)。
