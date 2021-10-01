---

copyright:
  years: 2020
lastupdated: "2020-5-11"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 安装 hzn CLI
{: #using_hzn_cli}

`hzn` 命令是 {{site.data.keyword.ieam}} 命令行界面。在边缘节点上安装 {{site.data.keyword.ieam}} 代理程序软件时，会自动安装 `hzn` CLI。 也可以安装 `hzn` CLI，但不安装代理程序。 例如，在没有完整代理程序的情况下，边缘管理员可能希望查询 {{site.data.keyword.ieam}} Exchange，或边缘开发者可能希望使用 `hzn` 命令进行测试。

1. 获取 `horizon-cli` 软件包。根据您的组织在[收集边缘节点文件](../hub/gather_files.md)步骤中所做的操作，您可以从 CSS 或从 `agentInstallFiles-<edge-node-type>.tar.gz` tar 文件获取 `horizon-cli` 软件包：

   * 从 CSS 获取 `horizon-cli` 软件包：

      * 如果尚未执行[准备设置边缘节点](../hub/prepare_for_edge_nodes.md)中的步骤，请立即执行。 从该步骤设置环境变量：

         ```bash
         export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
  export HZN_ORG_ID=<your-exchange-organization>
  export HZN_FSS_CSSURL=https://<ieam-management-hub-ingress>/edge-css/
         ```
         {: codeblock}

      * 将 `HOST_TYPE` 设置为与您将在其中安装 `horizon-cli` 软件包的主机类型相匹配的以下某个值：

         * linux-deb-amd64
         * linux-deb-arm64
         * linux-deb-armhf
         * linux-rpm-x86_64
         * linux-rpm-ppc64le
         * macos-pkg-x86_64

         ```bash
         HOST_TYPE=<host-type>
         ```
         {: codeblock}

      * 下载证书、配置文件以及包含来自 CSS 的 `horizon-cli` 软件包的 tar 文件：

         ```bash
         curl -sSL -w "%{http_code}" -u "$HZN_ORG_ID/$HZN_EXCHANGE_USER_AUTH" -k -o agent-install.crt $HZN_FSS_CSSURL/api/v1/objects/IBM/agent_files/agent-install.crt/data
         curl -sSL -w "%{http_code}" -u "$HZN_ORG_ID/$HZN_EXCHANGE_USER_AUTH" --cacert agent-install.crt -o agent-install.cfg $HZN_FSS_CSSURL/api/v1/objects/IBM/agent_files/agent-install.cfg/data
         curl -sSL -w "%{http_code}" -u "$HZN_ORG_ID/$HZN_EXCHANGE_USER_AUTH" --cacert agent-install.crt -o horizon-agent-$HOST_TYPE.tar.gz $HZN_FSS_CSSURL/api/v1/objects/IBM/agent_files/horizon-agent-$HOST_TYPE.tar.gz/data
         ```
         {: codeblock}

      * 从其 tar 文件中解压缩 `horizon-cli` 软件包：

         ```bash
         rm -f horizon-cli*   # remove any previous versions
         tar -zxvf horizon-agent-$HOST_TYPE.tar.gz
         ```
         {: codeblock}

   * 或者，从 `agentInstallFiles-<edge-node-type>.tar.gz` tar 文件获取 `horizon-cli` 软件包：

      * 从管理中心管理员处获取 `agentInstallFiles-<edge-node-type>.tar.gz` 文件，其中 `<edge-node-type>` 与您将在其中安装 `horizon-cli` 的主机相匹配。将此文件复制到此主机。

      * 将 tar 文件解包：

         ```bash
         tar -zxvf agentInstallFiles-<edge-device-type>.tar.gz
         ```
         {: codeblock}

2. 创建或更新 `/etc/default/horizon`：

   ```bash
   sudo cp agent-install.cfg /etc/default/horizon
   sudo cp agent-install.crt /etc/horizon
   sudo sh -c "echo 'HZN_MGMT_HUB_CERT_PATH=/etc/horizon/agent-install.crt' >> /etc/default/horizon"
   ```
   {: codeblock}

3. 安装 `horizon-cli` 软件包：

   * 确认软件包版本与[组件](../getting_started/components.md)中列出的设备代理程序相同。

   * 在基于 debian 的分发版上：

     ```bash
     sudo apt update && sudo apt install ./horizon-cli*.deb
     ```
     {: codeblock}

   * 在基于 RPM 的分发版上：

     ```bash
     sudo yum install ./horizon-cli*.rpm
     ```
     {: codeblock}

   * 在 {{site.data.keyword.macOS_notm}} 上：

     ```bash
     sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain horizon-cli.crt
     sudo installer -pkg horizon-cli-*.pkg -target /
     pkgutil --pkg-info com.github.open-horizon.pkg.horizon-cli   # confirm version installed
     ```
     {: codeblock}

## 卸载 hzn CLI

如果要从主机移除 `horizon-cli` 软件包：

* 从基于 debian 的分发版卸载 `horizon-cli`：

  ```bash
  sudo apt-get remove horizon-cli
  ```
  {: codeblock}

* 从基于 RPM 的分发版卸载 `horizon-cli`：

  ```bash
  sudo yum remove horizon-cli
  ```
  {: codeblock}

* 或者从 {{site.data.keyword.macOS_notm}} 卸载 `horizon-cli`：

  ```bash
  sudo horizon-cli-uninstall.sh
  ```
  {: codeblock}
