---

copyright:
years: 2019
lastupdated: "2019-06-28"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 故障诊断提示
{: #troubleshooting_devices}

当您遇到 {{site.data.keyword.edge_devices_notm}} 相关问题时，请复查下列提问。 每个提问的提示和指南都可以帮助您解决常见问题，以及获取信息来确定根本原因。
{:shortdesc}

  * [是否已安装 {{site.data.keyword.horizon}} 软件包的当前发行版？](#install_horizon)
  * [{{site.data.keyword.horizon}} 代理程序当前是否在正常运行？](#setup_horizon)
  * [边缘节点是否已配置为可以与 {{site.data.keyword.horizon_exchange}} 交互？](#node_configured)
  * [是否已为运行中的边缘节点启动所需的 Docker 容器？](#node_running)
  * [期望的服务容器版本是否在运行中？](#run_user_containers)
  * [期望的容器是否稳定？](#containers_stable)
  * [您的容器是否已与 Docker 正确联网？](#container_networked)
  * [依赖关系容器在容器上下文中是否可达？](#setup_correct)
  * [用户定义的容器是否正在将错误消息写入日志？](#log_user_container_errors)
  * [您能否使用贵组织的 {{site.data.keyword.message_hub_notm}} Kafka 代理实例？](#kafka_subscription)
  * [您的容器是否已发布到 {{site.data.keyword.horizon_exchange}}？](#publish_containers)
  * [发布的部署模式是否包括所有必需的服务和版本？](#services_included)
  * [特定于 {{site.data.keyword.open_shift_cp}} 环境的故障诊断提示](#troubleshooting_icp)
  * [对节点错误进行故障诊断](#troubleshooting_node_errors)

## 是否已安装 {{site.data.keyword.horizon}} 软件包的当前发行版？
{: #install_horizon}

请确保边缘节点上安装的 {{site.data.keyword.horizon}} 软件始终为最新发行版。

在 {{site.data.keyword.linux_notm}} 系统上，可以通过运行以下命令来检查已安装的 {{site.data.keyword.horizon}} 软件包的版本：  
```
dpkg -l | grep horizon
```
{: codeblock}

可以更新在系统上使用软件包管理器的 {{site.data.keyword.horizon}} 软件包。 例如，在基于 Ubuntu 的 {{site.data.keyword.linux_notm}} 系统上，使用以下命令将 {{site.data.keyword.horizon}} 更新为当前版本：
```
sudo apt update
sudo apt install -y blue horizon
```

## {{site.data.keyword.horizon}} 代理程序是否在正常运行？
{: #setup_horizon}

可以通过使用以下 {{site.data.keyword.horizon}} CLI 命令来验证代理程序是否正在运行：
```
hzn node list | jq .
```
{: codeblock}

您还可以使用主机的系统管理软件来检查 {{site.data.keyword.horizon}} 代理程序的状态： 例如，在基于 Ubuntu 的 {{site.data.keyword.linux_notm}} 系统上，可以使用 `systemctl` 实用程序：
```
sudo systemctl status horizon
```
{: codeblock}

如果代理程序处于活动状态，那么会显示类似于以下的行：
```
Active: active (running) since Fri 2018-09-02 15:00:04 UTC; 2h 29min ago
```
{: codeblock}

## 边缘节点是否已配置为可以与 {{site.data.keyword.horizon_exchange}} 交互？ 
{: #node_configured}

要验证是否可与 {{site.data.keyword.horizon_exchange}} 进行通信，请运行以下命令：
```
hzn exchange version
```
{: codeblock}

要验证是否已接受 {{site.data.keyword.horizon_exchange}}，请运行以下命令：
```
hzn exchange user list
```
{: codeblock}

在边缘节点向 {{site.data.keyword.horizon}} 注册之后，您可通过查看本地 {{site.data.keyword.horizon}} 代理程序配置，验证该节点是否正在与 {{site.data.keyword.horizon_exchange}} 交互。 运行以下命令以查看代理程序配置：
```
hzn node list | jq .configuration.exchange_api
```
{: codeblock}

## 边缘节点所需的 Docker 容器是否正在运行？
{: #node_running}

当边缘节点向 {{site.data.keyword.horizon}} 注册时，{{site.data.keyword.horizon}} agbot 会与该边缘节点创建协议，以运行网关类型（部署模式）中引用的服务。 如果未创建该协议，请完成这些检查来对问题进行故障诊断。

确认边缘节点是否处于 `configured` 状态并具有正确的 `id` 和 `organization` 值。 此外，确认 {{site.data.keyword.horizon}} 报告的体系结构是否是在服务的元数据中使用的同一体系结构。 运行以下命令以列出这些设置：
```
hzn node list | jq .
```
{: codeblock}

如果这些值符合预期，那么可以通过运行以下命令来检查边缘节点的协议状态： 
```
hzn agreement list -r | jq .
```
{: codeblock}

如果此命令未显示任何协议，那么表明这些协议可能已形成，但是可能发现了问题。 如果发生此情况，那么可以取消协议，然后该协议才能显示在先前命令的输出中。 如果发生协议取消，那么取消的协议会在已归档协议的列表中显示状态 `terminated_description`。 可以通过运行以下命令来查看已归档列表： 
```
hzn agreement list -r | jq .
```
{: codeblock}

在创建协议前也可能会出现问题。 如果发生此问题，请查看 {{site.data.keyword.horizon}} 代理程序的事件日志，以确定可能的错误。 运行以下命令以查看日志： 
```
hzn eventlog list
``` 
{: codeblock}

事件日志可能包含： 

* 无法验证服务元数据的签名，具体而言，无法验证 `deployment`
字段。 此错误通常表示签名公用密钥未导入到边缘节点中。 您可使用
`hzn key import -k <pubkey>` 命令导入该密钥。 您可使用
`hzn key list` 命令查看已导入到本地边缘节点的密钥。 可以通过使用以下命令来验证 {{site.data.keyword.horizon_exchange}} 中的服务元数据是否使用密钥进行了签名：
  ```
  hzn exchange service verify -k $PUBLIC_KEY_FILE <service-id>
  ```
  {: codeblock} 

将 `<service-id>` 替换为服务标识。 此标识可能类似于以下格式样本：`workload-cpu2wiotp_${CPU2WIOTP_VERSION}_${ARCH2}`。

* 服务 `deployment` 字段中的 Docker 映像路径不正确。 确认边缘节点是否可对映像路径执行 `docker pull` 命令。
* 边缘节点上的 {{site.data.keyword.horizon}} 代理程序无法访问保存 Docker 映像的 Docker 注册表。 如果远程 Docker 注册表中的 Docker 映像并非可供全局读取，您必须使用 `docker login` 命令，将凭证添加到边缘节点。 此步骤只需完成一次，因为边缘节点会记住这些凭证。
* 如果某个容器不断重新启动，请查看容器日志以获取详细信息。 您运行 `docker ps` 命令时，如果某个容器仅列示几秒钟，或者一直列为“正在重新启动”，那么表明该容器可能是在不断重新启动。 可以通过运行以下命令来查看容器日志以获取详细信息：
  ```
  grep --text -E ' <service>\[[0-9]+\]' /var/log/syslog
  ```
  {: codeblock}

## 期望的服务容器版本是否在运行中？
{: #run_user_containers}

容器版本由一个协议监管，该协议是您将服务添加到部署模式之后以及针对该模式注册边缘节点之后创建的。 通过运行以下命令，验证边缘节点是否具有模式的当前协议：

```
hzn agreement list | jq .
```
{: codeblock}

如果您已确认模式的协议正确，请使用以下命令查看正在运行的容器。 请确保用户定义的容器列出并且正在运行：
```
docker ps
```
{: codeblock}

接受协议后，{{site.data.keyword.horizon}} 代理程序可能要花费数分钟时间，然后才能下载、验证并开始运行相应的容器。 此协议主要取决于必须从远程存储库提取的容器本身的大小。

## 期望的容器是否稳定？
{: #containers_stable}

通过运行以下命令来检查容器是否稳定：
```
docker ps
```
{: codeblock}

从命令输出中，可以看到每个容器运行的持续时间。 如果随着时间推移，您发现容器意外重新启动，请在容器日志中检查是否有错误。

作为开发的最佳做法，请考虑通过运行以下命令来配置个别服务日志记录（仅限 {{site.data.keyword.linux_notm}} 系统）：
```bash
cat <<'EOF' > /etc/rsyslog.d/10-horizon-docker.conf
$template DynamicWorkloadFile,"/var/log/workload/%syslogtag:R,ERE,1,DFLT:.*workload-([^\[]+)--end%.log"

:syslogtag, startswith, "workload-" -?DynamicWorkloadFile
& stop
:syslogtag, startswith, "docker/" -/var/log/docker_containers.log
& stop
:syslogtag, startswith, "docker" -/var/log/docker.log
& stop
EOF
service rsyslog restart
```
{: codeblock}

如果完成上一步，那么容器的日志会记录在 `/var/log/workload/` 目录内的单独文件中。 使用 `docker ps`
命令可找出容器的全名。 您可以在此目录中找到该名称的日志文件，其后缀为 `.log`。

如果未配置个别服务日志记录，那么服务将与所有其他日志消息一起记录到系统日志。 要复审容器的数据，需要在 `/var/log/syslog` 文件内的系统日志输出中搜索容器名称。 例如，可以通过运行类似以下命令的命令来搜索日志：
```
grep --text -E 'YOURSERVICENAME\[[0-9]+\]' /var/log/syslog
```
{: codeblock}

## 您的容器是否已与 Docker 联网？
{: #container_networked}

确保容器与 Docker 正确联网，以便其能够访问必需服务。 运行以下命令以确保可以查看在边缘节点上处于活动状态的 Docker 虚拟网络：
```
docker network list
```
{: codeblock}

要查看有关网络的更多信息，请使用 `docker inspect X` 命令，其中 `X` 是网络的名称。 命令输出会列出所有在虚拟网络上运行的容器。

另外，还可以在每个容器上运行 `docker inspect Y` 命令（其中 `Y` 是容器名称），以获取更多信息。 例如，复审 `NetworkSettings` 容器信息并搜索 `Networks` 容器。 在此容器中，可以查看相关网络标识字符串，以及有关该容器在网络上的表示方式的信息。 这些表示信息包括容器 `IPAddress`，以及此网络上的网络别名列表。 

别名可供此虚拟网络上的所有容器使用，这些名称通常由代码部署模式中的容器用于发现虚拟网络上的其他容器。 例如，可以将服务命名为 `myservice`，这样一来，其他容器就可以直接使用该名称在网络中访问该服务，例如通过 `ping myservice` 命令进行访问。 容器的别名在传递到 `hzn exchange service publish` 命令的该容器的服务定义文件的 `deployment` 字段中进行指定。

有关 Docker 命令行界面所支持的命令的更多信息，请参阅 [Docker 命令参考 ![在新选项卡中打开](../../images/icons/launch-glyph.svg "在新选项卡中打开")](https://docs.docker.com/engine/reference/commandline/docker/#child-commands)。

## 依赖关系容器在容器上下文中是否可达？
{: #setup_correct}

进入运行容器的上下文以通过使用 `docker exec` 命令在运行时对问题进行故障诊断。 使用 `docker ps` 命令找到运行中的容器的标识，然后使用类似于以下命令的命令来进入上下文。 请将 `CONTAINERID` 替换为您的容器标识：
```
docker exec -it CONTAINERID /bin/sh
```
{: codeblock}

如果容器包含 Bash，那么可能要在上述命令的末尾而不是 `/bin/sh` 指定 `/bin/bash`。

一旦位于容器上下文内，即可使用 `ping` 或 `curl` 之类的命令与其所需的容器进行交互并验证连接。

有关 Docker 命令行界面所支持的命令的更多信息，请参阅 [Docker 命令参考 ![在新选项卡中打开](../../images/icons/launch-glyph.svg "在新选项卡中打开")](https://docs.docker.com/engine/reference/commandline/docker/#child-commands)。

## 用户定义的容器是否正在将错误消息写入日志？
{: #log_user_container_errors}

如果已配置个别服务日志记录，那么每个容器都会记录到 `/var/log/workload/` 目录内的单独文件中。 使用 `docker ps`
命令可找出容器的全名。 然后，在该目录中查找该名称的文件，其后缀为 `.log`。

如果未配置单个服务日志记录，那么服务日志将与所有其他详细信息一起记录在系统日志中。 要复审数据，请在 `/var/log/syslog` 目录内的系统日志输出中搜索容器日志。 例如，通过运行类似以下命令的命令来搜索日志：
```
grep --text -E 'YOURSERVICENAME\[[0-9]+\]' /var/log/syslog
```
{: codeblock}

## 您能否使用贵组织的 {{site.data.keyword.message_hub_notm}} Kafka 代理实例？
{: #kafka_subscription}

从 {{site.data.keyword.message_hub_notm}} 预订组织的 Kafka 实例有助于确认您的 Kafka
用户凭证正确无误。 此预订还可以帮助您确认 Kafka 服务实例正在云端运行，以及边缘节点会在数据发布时发送数据。

要预订 Kafka 代理，请安装 `kafkacat` 程序。 例如，在 Ubuntu {{site.data.keyword.linux_notm}} 系统上，使用以下命令：

```bash
sudo apt install kafkacat
```
{: codeblock}

安装后，可以使用类似于以下示例的命令进行预订，该命令会使用您通常放在环境变量引用中的凭证：

```bash
kafkacat -C -q -o end -f "%t/%p/%o/%k: %s\n" -b $EVTSTREAMS_BROKER_URL -X api.version.request=true -X security.protocol=sasl_ssl -X sasl.mechanisms=PLAIN -X sasl.username=token -X sasl.password=$EVTSTREAMS_API_KEY -t $EVTSTREAMS_TOPIC
```
{: codeblock}

其中，`EVTSTREAMS_BROKER_URL` 是 Kafka 代理的 URL，`EVTSTREAMS_TOPIC` 是 Kafka 主题，而 `EVTSTREAMS_API_KEY` 是用于向 {{site.data.keyword.message_hub_notm}} API 认证的 API 密钥。

如果预订命令成功，那么该命令会无限期地阻止。 该命令会等待面向 Kafka 代理的任何发布，并检索和显示生成的任何消息。 如果在几分钟后仍未看到任何来自边缘节点的消息，请在服务日志中查找错误消息。

例如，要复审 `cpu2evtstreams` 服务的日志，请运行以下命令：

* 对于 {{site.data.keyword.linux_notm}} 和 {{site.data.keyword.windows_notm}} 

```bash
tail -n 500 -f /var/log/syslog | grep -E 'cpu2evtstreams\[[0-9]+\]:'
```
{: codeblock}

* 对于 macOS

```bash
docker logs -f $(docker ps --filter 'name=-cpu2evtstreams' | tail -n +2 | awk '{print $1}')
```
{: codeblock}

## 您的容器是否已发布到 {{site.data.keyword.horizon_exchange}}？
{: #publish_containers}

{{site.data.keyword.horizon_exchange}} 是中央仓库，用于保存您为边缘节点发布的代码的相关元数据。 如果您尚未对代码进行签名并发布到 {{site.data.keyword.horizon_exchange}}，那么无法将该代码提取到已验证的边缘节点并运行。

请搭配下列参数来运行 `hzn` 命令，以查看已发布的代码列表，确认所有服务容器都已成功发布：

```
hzn exchange service list | jq .
hzn exchange service list $ORG_ID/$SERVICE | jq .
```
{: codeblock}

参数 `$ORG_ID` 是您的组织标识，`$SERVICE` 是您获取有关信息的服务的名称。

## 发布的部署模式是否包括所有必需的服务和版本？
{: #services_included}

在安装 `hzn` 命令所在的任何机器上，您可使用该命令获取有关任何部署模式的详细信息。 请搭配下列参数来运行该命令，以从 {{site.data.keyword.horizon_exchange}} 提取部署模式列表： 

```
hzn exchange pattern list | jq .
hzn exchange pattern list $ORG_ID/$PATTERN | jq .
```
{: codeblock}

参数 `$ORG_ID` 是您的组织标识，`$PATTERN` 是您获取有关信息的部署模式的名称。

## 特定于 {{site.data.keyword.open_shift_cp}} 环境的故障诊断提示
{: #troubleshooting_icp}

复查此内容以帮助对与 {{site.data.keyword.edge_devices_notm}} 相关的 {{site.data.keyword.open_shift_cp}} 环境的常见问题进行故障诊断。 这些提示可帮助您解决常见问题以及获取信息来确定根本原因。
{:shortdesc}

### 您的 {{site.data.keyword.edge_devices_notm}} 凭证是否正确配置用于 {{site.data.keyword.open_shift_cp}} 环境中？
{: #setup_correct}

您需要 {{site.data.keyword.open_shift_cp}} 用户帐户来完成此环境中的 {{site.data.keyword.edge_devices_notm}} 内的任何操作。 您还需要从该帐户创建的 API 密钥。

要在此环境中验证您的 {{site.data.keyword.edge_devices_notm}} 凭证，请运行以下命令：

   ```
   hzn exchange user list
   ```
   {: codeblock}

如果从显示一个或多个用户的 Exchange 返回 JSON 格式化条目，那么表明正确配置了 {{site.data.keyword.edge_devices_notm}} 凭证。

如果返回了错误响应，那么可以采取步骤对凭证设置进行故障诊断。

如果错误消息指示 API 密钥不正确，那么可以使用以下命令创建新 API 密钥。

请参阅[收集必需的信息和文件](../developing/software_defined_radio_ex_full.md#prereq-horizon)。

## 对节点错误进行故障诊断
{: #troubleshooting_node_errors}

{{site.data.keyword.edge_devices_notm}} 将事件日志的子集发布到在 {{site.data.keyword.gui}} 中可查看的 Exchange。 这些错误链接到故障诊断指南。
{:shortdesc}

  - [映像装入错误](#eil)
  - [部署配置错误](#eidc)
  - [容器启动错误](#esc)

### 映像装入错误
{: #eil}

当服务定义中引用的服务映像在映像存储库中不存在时，会发生此错误。 要解决此错误，请执行以下操作：

1. 在没有 **-I** 标志的情况下重新发布服务。
    ```
    hzn exchange service publish -f <service-definition-file>
    ```
    {: codeblock}

2. 将服务映像直接推送到映像存储库。 
    ```
    docker push <image name>
    ```
    {: codeblock} 
    
### 部署配置错误
{: #eidc}

当服务定义部署配置指定与根受保护的文件的绑定时，会发生此错误。 要解决此错误，请执行以下操作：

1. 将容器绑定到根不受保护的文件。
2. 将文件许可权更改为允许用户对文件进行读取和写入。

### 容器启动错误
{: #esc}

如果 Docker 在启动服务容器时遇到错误，那么会发生此错误。 错误消息可能包含指示容器启动失败原因的详细信息。 错误解决步骤取决于错误。 可能会发生以下错误：

1. 设备已在使用部署配置所指定的已发布端口。 要解决错误，请执行以下操作： 

    - 将其他端口映射到服务容器端口。 显示的端口号不必与服务端口号匹配。
    - 停止正在使用同一端口的程序。

2. 部署配置所指定的已发布端口不是有效的端口号。 端口号必须是范围在 1 - 65535 内的数字。
3. 部署配置中的卷名不是有效的文件路径。 卷路径必须由其绝对（而非相对）路径指定。 

### 其他信息

有关更多信息，请参阅：
  * [故障诊断](../troubleshoot/troubleshooting.md)
