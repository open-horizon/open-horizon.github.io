---

copyright:
years: 2019
lastupdated: "2019-10-28"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 高级手动代理程序安装和注册
{: #advanced_man_install}

此内容描述在边缘设备上安装 {{site.data.keyword.edge_notm}} 代理程序并将其注册的每个手动步骤。 有关更为自动化的方法，请参阅[自动代理程序安装和注册](automated_install.md)。
{:shortdesc}

## 安装代理程序
{: #agent_install}

**注**：有关命令语法的更多信息，请参阅[此文档中使用的约定](../getting_started/document_conventions.md)。

1. 先获取 `agentInstallFiles-<edge-device-type>.tar.gz` 文件以及随此文件创建的 API 密钥，再继续此过程。

    作为[安装管理中心](../hub/online_installation.md)的配置后步骤，为您创建了一个压缩文件。此文件包含在边缘设备上安装 {{site.data.keyword.horizon}} 代理程序并使用 helloworld 示例进行注册所必需的文件。

2. 使用 USB 记忆棒、安全复制命令或其他方法，将该文件复制到边缘设备。

3. 展开 tar 文件：

   ```bash
   tar -zxvf agentInstallFiles-<edge-device-type>.tar.gz
   ```
   {: codeblock}

4. 使用适用于您的边缘设备类型的以下任一部分。

### 在 Linux（ARM 32 位、ARM 64 位、ppc64le（仅 {{site.data.keyword.ieam}} {{site.data.keyword.semver}}）或 x86_64）边缘设备或虚拟机上安装代理程序
{: #agent_install_linux}

执行以下步骤：

1. 如果已经以非 root 用户身份登录，请切换到具有 root 特权的用户：

   ```bash
   sudo -s
   ```
   {: codeblock}

2. 查看 Docker 版本以检查其是否足够新：

   ```bash
   docker --version
   ```
   {: codeblock}

      如果未安装 Docker，或者版本低于 `18.06.01`，请安装最新版本的 Docker：

   ```bash
   curl -fsSL get.docker.com | sh
      docker --version
   ```
   {: codeblock}

3. 安装复制到此边缘设备的 Horizon 软件包：

   * 对于 Debian/Ubuntu 分发：
      ```bash
      apt update && apt install ./*horizon*.deb
      ```
      {: codeblock}

   * 对于 Red Hat Enterprise Linux&reg; 分发：
      ```bash
      yum install ./*horizon*.rpm
      ```
      {: codeblock}
   
4. 将特定信息设置为环境变量：

   ```bash
   eval export $(cat agent-install.cfg)
   ```
   {: codeblock}

5. 通过使用正确的信息填充 `/etc/default/horizon`，将边缘设备 Horizon 代理程序指向 {{site.data.keyword.edge_notm}} 集群：

   ```bash
   sed -i.bak -e "s|^HZN_EXCHANGE_URL=[^ ]*|HZN_EXCHANGE_URL=${HZN_EXCHANGE_URL}|g" -e "s|^HZN_FSS_CSSURL=[^ ]*|HZN_FSS_CSSURL=${HZN_FSS_CSSURL}|g" /etc/default/horizon
   ```
   {: codeblock}

6. 使 Horizon 代理程序信任 `agent-install.crt`：

   ```bash
   if grep -qE '^HZN_MGMT_HUB_CERT_PATH=' /etc/default/horizon; then sed -i.bak -e "s|^HZN_MGMT_HUB_CERT_PATH=[^ ]*|HZN_MGMT_HUB_CERT_PATH=${PWD}/agent-install.crt|" /etc/default/horizon; else echo "HZN_MGMT_HUB_CERT_PATH=${PWD}/agent-install.crt" >> /etc/default/horizon; fi
   ```
   {: codeblock}
   
7. 重新启动代理程序以将更改选取到 `/etc/default/horizon`：

   ```bash
   systemctl restart horizon.service
   ```
   {: codeblock}

8. 验证代理程序正在运行且配置正确：

   ```bash
   hzn version
       hzn exchange version
       hzn node list
   ```
   {: codeblock}  

      输出应该类似于此示例（版本号和 URL 可能不同）：

   ```bash
   $ hzn version
   Horizon CLI version: 2.23.29
   Horizon Agent version: 2.23.29
   $ hzn exchange version
   1.116.0
   $ hzn node list
   {
         "id": "",
         "organization": null,
         "pattern": null,
         "name": null,
         "token_last_valid_time": "",
         "token_valid": null,
         "ha": null,
         "configstate": {
            "state": "unconfigured",
            "last_update_time": ""
         },
         "configuration": {
            "exchange_api": "https://9.30.210.34:8443/ec-exchange/v1/",
            "exchange_version": "1.116.0",
            "required_minimum_exchange_version": "1.116.0",
            "preferred_exchange_version": "1.116.0",
            "mms_api": "https://9.30.210.34:8443/ec-css",
            "architecture": "amd64",
            "horizon_version": "2.23.29"
         },
         "connectivity": {
            "firmware.bluehorizon.network": true,
            "images.bluehorizon.network": true
         }
      }
      ```
   {: codeblock}

9. 如果先前切换到特权 shell，请立即退出。 您无需 root 用户访问权即可注册设备。

   ```bash
   exit
   ```
   {: codeblock}

10. 继续[注册代理程序](#agent_reg)。

### 在 macOS 边缘设备上安装代理程序
{: #mac-os-x}

1. 将 `horizon-cli` 软件包证书导入到 {{site.data.keyword.macOS_notm}} 密钥链：

   ```bash
   sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain horizon-cli.crt
   ```
   {: codeblock}

      **注**：您只需要在每个 {{site.data.keyword.macOS_notm}} 机器上完成一次此步骤。导入这个可信证书后，就可以安装任何未来版本的 {{site.data.keyword.horizon}} 软件。

2. 安装 {{site.data.keyword.horizon}} CLI 软件包：

   ```bash
   sudo installer -pkg horizon-cli-*.pkg -target /
   ```
   {: codeblock}

3. 通过将以下内容添加到 `~/.bashrc`，为 `hzn` 命令启用子命令名称补全：

  ```bash
  source /usr/local/share/horizon/hzn_bash_autocomplete.sh
  ```
  {: codeblock}

4. 在安装**新设备**时，此步骤不是必需的。 但是，如果先前已在此机器上安装和启动 horizon 容器，那么现在通过运行以下命令停止：

  ```bash
  horizon-container stop
  ```
  {: codeblock}
5. 将特定信息设置为环境变量：

  ```bash
  eval export $(cat agent-install.cfg)
  ```
  {: codeblock}

6. 通过使用正确的信息填充 `/etc/default/horizon`，将边缘设备 Horizon 代理程序指向 {{site.data.keyword.edge_notm}} 集群：

  ```bash
  sudo mkdir -p /etc/default

  sudo sh -c "cat << EndOfContent > /etc/default/horizon
  HZN_EXCHANGE_URL=$HZN_EXCHANGE_URL
  HZN_FSS_CSSURL=$HZN_FSS_CSSURL
  HZN_MGMT_HUB_CERT_PATH=${PWD}/agent-install.crt
  HZN_DEVICE_ID=$(hostname)
  EndOfContent"
  ```
  {: codeblock}

7. 启动 {{site.data.keyword.horizon}} 代理程序：

  ```bash
  horizon-container start
  ```
  {: codeblock}

8. 验证代理程序正在运行且配置正确：

  ```bash
  hzn version
       hzn exchange version
       hzn node list
  ```
  {: codeblock}

      输出应该类似于以下内容（版本号和 URL 可能不同）：

  ```bash
  $ hzn version
  Horizon CLI version: 2.23.29
  Horizon Agent version: 2.23.29
  $ hzn exchange version
  1.116.0
  $ hzn node list
      {
         "id": "",
         "organization": null,
         "pattern": null,
         "name": null,
         "token_last_valid_time": "",
         "token_valid": null,
         "ha": null,
         "configstate": {
            "state": "unconfigured",
            "last_update_time": ""
         },
         "configuration": {
            "exchange_api": "https://9.30.210.34:8443/ec-exchange/v1/",
            "exchange_version": "1.116.0",
            "required_minimum_exchange_version": "1.116.0",
            "preferred_exchange_version": "1.116.0",
            "mms_api": "https://9.30.210.34:8443/ec-css",
            "architecture": "amd64",
            "horizon_version": "2.23.29"
         },
         "connectivity": {
            "firmware.bluehorizon.network": true,
            "images.bluehorizon.network": true
         }
      }
  ```
  {: codeblock}

9. 继续[注册代理程序](#agent_reg)。

## 注册代理程序
{: #agent_reg}

1. 将特定信息设置为**环境变量**：

  ```bash
  eval export $(cat agent-install.cfg)
  export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
  ```
  {: codeblock}

2. 查看样本边缘服务部署模式的列表：

  ```bash
  hzn exchange pattern list IBM/
  ```
  {: codeblock}

3. helloworld 边缘服务是最基本的示例，这是非常好的起点。 向 {{site.data.keyword.horizon}} **注册**边缘设备以运行 **helloworld 部署模式**：

  ```bash
  hzn register -p IBM/pattern-ibm.helloworld
  ```
  {: codeblock}

  **注**：以**使用节点标识**开头的行中的输出显示节点标识。

4. 边缘设备将与其中一个 {{site.data.keyword.horizon}} 协议自动程序达成协议（此过程通常需要约 15 秒）。 **重复查询此设备的协议**，直至填写 `agreement_finalized_time` 和 `agreement_execution_start_time` 字段：

  ```bash
  hzn agreement list
  ```
  {: codeblock}

5. **在达成协议后**，列出已作为结果启动的 Docker 容器边缘服务：

  ```bash
  sudo docker ps
  ```
  {: codeblock}

6. 查看 helloworld 边缘服务**输出**：

  ```bash
  sudo hzn service log -f ibm.helloworld
  ```
  {: codeblock}

## 后续操作
{: #what_next}

浏览到 [CPU 使用量到 IBM Event Streams](../using_edge_services/cpu_load_example.md) 以继续执行其他边缘服务示例。
