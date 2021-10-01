---

copyright:
years: 2020
lastupdated: "2020-10-28"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 安装后的配置

## 先决条件

* [IBM Cloud Pak CLI (**cloudctl**) 和 OpenShift 客户机 CLI (**oc**)](../cli/cloudctl_oc_cli.md)
* [**jq** ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://stedolan.github.io/jq/download/)
* [**git** ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://git-scm.com/downloads)
* [**docker** ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://docs.docker.com/get-docker/) V1.13 或更高版本
* **make**

## 安装验证

1. 完成[安装 {{site.data.keyword.ieam}}](online_installation.md) 中的步骤
2. 确保 {{site.data.keyword.ieam}} 名称空间中的所有 pod 处于**正在运行**或**已完成**状态：

   ```
   oc get pods
   ```
   {: codeblock}

   这是安装本地数据库后应该看到的内容的示例。 期望一些初始化重新启动，但是多次重新启动通常指示问题：
   ```
   $ oc get pods
   NAME                                           READY   STATUS      RESTARTS   AGE
   create-agbotdb-cluster-j4fnb                   0/1     Completed   0          88m
   create-exchangedb-cluster-hzlxm                0/1     Completed   0          88m
   ibm-common-service-operator-68b46458dc-nv2mn   1/1     Running     0          103m
   ibm-eamhub-operator-7bf99c5fc8-7xdts           1/1     Running     0          103m
   ibm-edge-agbot-5546dfd7f4-4prgr                1/1     Running     0          81m
   ibm-edge-agbot-5546dfd7f4-sck6h                1/1     Running     0          81m
   ibm-edge-agbotdb-keeper-0                      1/1     Running     0          88m
   ibm-edge-agbotdb-keeper-1                      1/1     Running     0          87m
   ibm-edge-agbotdb-keeper-2                      1/1     Running     0          86m
   ibm-edge-agbotdb-proxy-7447f6658f-7wvdh        1/1     Running     0          88m
   ibm-edge-agbotdb-proxy-7447f6658f-8r56d        1/1     Running     0          88m
   ibm-edge-agbotdb-proxy-7447f6658f-g4hls        1/1     Running     0          88m
   ibm-edge-agbotdb-sentinel-5766f666f4-5qm9x     1/1     Running     0          88m
   ibm-edge-agbotdb-sentinel-5766f666f4-5whgr     1/1     Running     0          88m
   ibm-edge-agbotdb-sentinel-5766f666f4-9xjpr     1/1     Running     0          88m
   ibm-edge-css-5c59c9d6b6-kqfnn                  1/1     Running     0          81m
   ibm-edge-css-5c59c9d6b6-sp84w                  1/1     Running     0          81m
   ibm-edge-css-5c59c9d6b6-wf84s                  1/1     Running     0          81m
   ibm-edge-cssdb-server-0                        1/1     Running     0          88m
   ibm-edge-exchange-b6647db8d-k97r8              1/1     Running     0          81m
   ibm-edge-exchange-b6647db8d-kkcvs              1/1     Running     0          81m
   ibm-edge-exchange-b6647db8d-q5ttc              1/1     Running     0          81m
   ibm-edge-exchangedb-keeper-0                   1/1     Running     1          88m
   ibm-edge-exchangedb-keeper-1                   1/1     Running     0          85m
   ibm-edge-exchangedb-keeper-2                   1/1     Running     0          84m
   ibm-edge-exchangedb-proxy-6bbd5b485-cx2v8      1/1     Running     0          88m
   ibm-edge-exchangedb-proxy-6bbd5b485-hs27d      1/1     Running     0          88m
   ibm-edge-exchangedb-proxy-6bbd5b485-htldr      1/1     Running     0          88m
   ibm-edge-exchangedb-sentinel-6d685bf96-hz59z   1/1     Running     1          88m
   ibm-edge-exchangedb-sentinel-6d685bf96-m4bdh   1/1     Running     0          88m
   ibm-edge-exchangedb-sentinel-6d685bf96-mxv2b   1/1     Running     1          88m
   ibm-edge-sdo-0                                 1/1     Running     0          81m
   ibm-edge-ui-545d694f6c-4rnrf                   1/1     Running     0          81m
   ibm-edge-ui-545d694f6c-97ptz                   1/1     Running     0          81m
   ibm-edge-ui-545d694f6c-f7bf6                   1/1     Running     0          81m
   ```
   {: codeblock}

   **注**：
   * 有关因资源或调度问题处于**暂挂**状态的任何 pod 的更多信息，请参阅[集群大小调整](cluster_sizing.md)页面。 这包括如何减少组件调度成本的相关信息。
   * 有关任何其他错误的更多信息，请参阅[故障诊断](../admin/troubleshooting.md)。
3. 确保 **ibm-common-services** 名称空间中的所有 pod 处于**正在运行**或**已完成**状态：

   ```
   oc get pods -n ibm-common-services
   ```
   {: codeblock}

4. [从 IBM Passport Advantage 下载代理程序软件包](part_numbers.md)到您的安装环境并解包安装介质：
    ```
    tar -zxvf ibm-eam-{{site.data.keyword.semver}}-bundle.tar.gz && \
    cd ibm-eam-{{site.data.keyword.semver}}-bundle/tools
    ```
    {: codeblock}
5. 验证安装状态：
    ```
    ./service_healthcheck.sh
    ```
    {: codeblock}

    请参阅以下示例输出：
    ```
    $ ./service_healthcheck.sh
    ==Running service verification tests for IBM Edge Application Manager==
    SUCCESS: IBM Edge Application Manager Exchange API is operational
    SUCCESS: IBM Edge Application Manager Cloud Sync Service is operational
    SUCCESS: IBM Edge Application Manager Agbot database heartbeat is current
    SUCCESS: IBM Edge Application Manager SDO API is operational
    SUCCESS: IBM Edge Application Manager UI is properly requiring valid authentication
    ==All expected services are up and running==
    ```

   * 如果 **service_healthcheck.sh** 命令失败、您在运行以下命令时遇到问题或者如果在运行时期间发生问题，请参阅[故障诊断](../admin/troubleshooting.md)。

## 增加缺省证书到期时间长度

正在创建的到期时间长度为 90 天的证书存在已知问题，按照这些指示信息来增加缺省长度并应用新证书：
* 执行[任务 1](../getting_started/cert_refresh.md#task1)（不包括步骤 5，无需导出证书）
* 执行[任务 3](../getting_started/cert_refresh.md#task3)（不包括步骤 7，将在稍后的配置中添加证书）。

**注**：**任务 2** 已跳过，因为现在不存在现有边缘节点。

## 安装后的配置
{: #postconfig}

以下流程必须在支持安装 **hzn** CLI 的主机上运行，该 CLI 当前可以安装在基于 Debian/apt 的 Linux、amd64 Red Hat/rpm Linux 或 macOS 主机上。 这些步骤使用从“安装验证”部分中的 PPA 下载的相同介质。

1. 使用所支持平台的指示信息安装 **hzn** CLI：
  * 浏览至 **agent** 目录并解压缩代理程序文件：
    ```
    cd ibm-eam-{{site.data.keyword.semver}}-agent-x86_64/agent && \
    tar -zxvf edge-packages-{{site.data.keyword.semver}}.tar.gz
    ```
    {: codeblock}

    * Debian {{site.data.keyword.linux_notm}} 示例：
      ```
      sudo apt-get install ./edge-packages-{{site.data.keyword.semver}}/linux/deb/amd64/horizon-cli*.deb
      ```
      {: codeblock}

    * Red Hat {{site.data.keyword.linux_notm}} 示例：
      ```
      sudo dnf install -yq ./edge-packages-{{site.data.keyword.semver}}/linux/rpm/x86_64/horizon-cli-*.x86_64.rpm
      ```
      {: codeblock}

    * macOS 示例：
      ```
      sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain edge-packages-{{site.data.keyword.semver}}/macos/pkg/x86_64/horizon-cli.crt && \
      sudo installer -pkg edge-packages-{{site.data.keyword.semver}}/macos/pkg/x86_64/horizon-cli-*.pkg -target /
      ```
      {: codeblock}

2. 运行安装后脚本。 此脚本执行所有必需的初始化以创建第一个组织。 （组织是 {{site.data.keyword.ieam}} 分隔资源和用户以支持多租户的方式。 初始，第一个组织就足够。 您可以稍后配置更多组织。 有关更多信息，请参阅[多租户 ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](../admin/multi_tenancy.md)）。

   **注**：**ibm** 和 **root** 是内部使用组织，不能选择作为您的初始组织。

   ```
   ./post_install.sh <choose-your-org-name>
   ```
   {: codeblock}

3. 运行以下命令以打印 {{site.data.keyword.ieam}} {{site.data.keyword.ieam}} 管理控制台链接以用于安装：
   ```
   echo https://$(oc get cm management-ingress-ibmcloud-cluster-info -o jsonpath='{.data.cluster_ca_domain}')/edge
   ```
   {: codeblock}

## LDAP 和 API 密钥

如果先前未配置，请使用 {{site.data.keyword.open_shift_cp}} 管理控制台创建 LDAP 连接。 建立 LDAP 连接后，请创建一个团队，授权该团队访问 {{site.data.keyword.edge_notm}} 操作程序已部署到的名称空间，并将用户添加到该团队。 这会将创建 API 密钥的许可权授予各个用户。

**注**：API 密钥用于向 {{site.data.keyword.edge_notm}} CLI 进行认证，并且和 API 密钥关联的许可权与生成这些密钥所使用的用户完全相同。有关 LDAP 的更多信息，请参阅[配置 LDAP 连接 ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://www.ibm.com/support/knowledgecenter/SSHKN6/iam/3.x.x/configure_ldap.html)。

## 下一步是什么

完成[安装后的配置](#postconfig)中的步骤后，遵循[收集边缘节点文件](gather_files.md)页面上的流程，为边缘节点准备安装介质。
