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

# 批量代理程序安装和注册
{: #batch-install}

使用批量安装过程来设置类型类似的多个边缘设备（即相同的体系结构、操作系统以及模式或策略）。

**注**：对于此过程，不支持作为 macOs 计算机的目标边缘设备。但是，您可以根据需要从 macOs 计算机驱动此过程。 （换句话说，此主机可以是 macOs 计算机。）

### 先决条件

* 要安装和注册的设备必须具有到管理中心的网络访问权。
* 设备必须具有已安装的操作系统。
* 如果要将 DHCP 用于边缘设备，每个设备必须保留相同的 IP 地址，直到任务完成（若使用 DDNS，则为相同的 `hostname`）。
* 所有边缘服务用户输入必须在服务定义或者模式或部署策略中指定为缺省值。 不能使用特定于节点的用户输入。

### 过程
{: #proc-multiple}

1. 如果您尚未遵循[为边缘设备收集必要的信息和文件](../hub/gather_files.md#prereq_horizon)来获取或创建 **agentInstallFiles-&lt;edge-device-type&gt;.tar.gz** 文件和 API 密钥，请立即执行此操作。 在以下环境变量中设置文件的名称和 API 密钥值：

   ```bash
   export AGENT_TAR_FILE=agentInstallFiles-<edge-device-type>.tar.gz
   export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
   ```
  {: codeblock}

2. **pssh** 软件包包含 **pssh** 和 **pscp** 命令，这些命令使您能够以并行方式向很多边缘设备运行命令，以及以并行方式将文件复制到多个边缘设备。 如果您在此主机上尚未具有这些命令，请立即安装软件包：

  * 在 {{site.data.keyword.linux_notm}} 上：

   ```bash
   sudo apt install pssh
   alias pssh=parallel-ssh
   alias pscp=parallel-scp
   ```
   {: codeblock}

  * 在 {{site.data.keyword.macOS_notm}} 上：

   ```bash
   brew install pssh
   ```
   {: codeblock}

   （如果尚未安装 **brew**，请参阅[使用 Brew 在 macOs 计算机上安装 pssh ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://brewinstall.org/Install-pssh-on-Mac-with-Brew/)。）

3. 您可以通过多种方法为边缘设备提供 **pscp** 和 **pssh** 访问权。 此内容描述如何使用 SSH 公用密钥。 首先，该主机必须具有 SSH 密钥对（通常位于 **~/.ssh/id_rsa** 和 **~/.ssh/id_rsa.pub** 中）。 如果没有 SSH 密钥对，请生成：

   ```bash
   ssh-keygen -t rsa
   ```
   {: codeblock}

4. 将公用密钥 (**~/.ssh/id_rsa.pub**) 的内容置于每个边缘设备上的 **/root/.ssh/authorized_keys** 中。

5. 创建名为 **node-id-mapping.csv** 的具有 2 列的映射文件，该文件将每个边缘设备的 IP 地址或主机名映射到注册期间应提供的 {{site.data.keyword.ieam}} 节点名。 在每个边缘设备上运行 **agent-install.sh** 时，此文件会告诉程序要提供给该设备的边缘节点名称。 使用 CSV 格式：

   ```bash
   Hostname/IP, Node Name
   1.1.1.1, factory2-1
   1.1.1.2, factory2-2
   ```
   {: codeblock}

6. 将 **node.id-mapping.csv** 添加到代理程序 tar 文件：

   ```bash
   gunzip $AGENT_TAR_FILE
   tar -uf ${AGENT_TAR_FILE%.gz} node-id-mapping.csv
   gzip ${AGENT_TAR_FILE%.gz}
   ```
   {: codeblock}

7. 在名为 **nodes.hosts** 的文件中放置要批量安装和注册的边缘设备列表。 这将与 **pscp** 和 **pssh** 命令一起使用。 每行应采用标准 SSH 格式 `<user>@<IP-or-hostname>`：

   ```bash
   root@1.1.1.1
   root@1.1.1.2
   ```
   {: codeblock}

   **注**：如果将非 root 用户用于任何主机，那么 sudo 必须配置为允许该用户执行 sudo 而无需输入密码。

8. 将代理程序 tar 文件复制到边缘设备。 执行此步骤可能需要一些时间：

   ```bash
   pscp -h nodes.hosts -e /tmp/pscp-errors $AGENT_TAR_FILE /tmp
   ```
   {: codeblock}

   **注**：如果您在任何边缘设备的 **pscp** 输出中获取 **[FAILURE]**，那么可以在 **/tmp/pscp-errors** 中看到错误。

9. 在每个边缘设备上运行 **agent-install.sh**，以安装 Horizon 代理程序并注册边缘设备。 您可以使用模式或策略来注册边缘设备：

   1. 向模式注册边缘设备：

      ```bash
      pssh -h nodes.hosts -t 0 "bash -c \"tar -zxf /tmp/$AGENT_TAR_FILE agent-install.sh && sudo -s ./agent-install.sh -i . -u $HZN_EXCHANGE_USER_AUTH -p IBM/pattern-ibm.helloworld -w ibm.helloworld -o IBM -z /tmp/$AGENT_TAR_FILE 2>&1 >/tmp/agent-install.log \" "
      ```
      {: codeblock}

      您可以通过修改 **-p**、**-w** 和 **-o** 标志，使用不同的部署模式，而不是向 **IBM/pattern-ibm.helloworld** 部署模式注册边缘设备。 要查看所有可用的 **agent-install.sh** 标志描述：

      ```bash
      tar -zxf $AGENT_TAR_FILE agent-install.sh &&./agent-install.sh -h
      ```
      {: codeblock}

   2. 或者，向策略注册边缘设备。 创建节点策略，将其复制到边缘设备，并使用该策略注册设备：

      ```bash
      echo '{ "properties": [ { "name": "nodetype", "value": "special-node" } ] }' > node-policy.json
      pscp -h nodes.hosts -e /tmp/pscp-errors node-policy.json /tmp
      pssh -h nodes.hosts -t 0 "bash -c \"tar -zxf /tmp/$AGENT_TAR_FILE agent-install.sh && sudo -s ./agent-install.sh -i . -u $HZN_EXCHANGE_USER_AUTH -n /tmp/node-policy.json  -z /tmp/$AGENT_TAR_FILE 2>&1 >/tmp/agent-install.log \" "
      ```
      {: codeblock}

      现在，边缘设备已就绪，但是将不会开始运行边缘服务，直至创建部署策略（业务策略），指定应该将服务部署到此类型的边缘设备（在此示例中，**nodetype** 为 **special-node** 的设备）。 请参阅[使用部署策略](../using_edge_services/detailed_policy.md)以获取详细信息。

10. 如果您在任何边缘设备的 **pssh** 输出中获取 **[FAILURE]**，那么可以通过转至边缘设备并查看 **/tmp/agent-install.log** 来调查问题。

11. 运行 **pssh** 命令时，您可以在 {{site.data.keyword.edge_notm}} 控制台中查看边缘节点的状态。 请参阅[使用管理控制台](../console/accessing_ui.md)。
