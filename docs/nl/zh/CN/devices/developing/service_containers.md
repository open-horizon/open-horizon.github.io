---

copyright:
years: 2019,2020
lastupdated: "2020-01-28"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 准备创建边缘服务
{: #service_containers}

使用 {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) 以在 {{site.data.keyword.docker}} 容器中为边缘设备开发服务。您可以使用任何适当的 {{site.data.keyword.linux_notm}} Base、编程语言、库或实用程序来创建边缘服务。
{:shortdesc}

推送、签署和发布服务后，{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) 在边缘设备上使用完全自主的代理程序来下载、验证、配置、安装和监视服务。 

边缘服务通常使用云采集服务来存储和进一步处理边缘分析结果。 此过程包括边缘和云代码开发工作流程。

{{site.data.keyword.ieam}} 基于开放式源代码 [{{site.data.keyword.horizon_open}} ![在新选项卡中打开](../../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon/) 项目，并且使用 `hzn` {{site.data.keyword.horizon}} {{site.data.keyword.linux_notm}} 命令来运行某些进程。

## 准备工作
{: #service_containers_begin}

1. 通过在您的开发主机上安装 {{site.data.keyword.horizon}} 代理程序并向 {{site.data.keyword.horizon_exchange}} 注册主机，配置该主机以用于 {{site.data.keyword.ieam}}。请参阅[在边缘设备上安装 {{site.data.keyword.horizon}} 代理程序并使用 hello world 示例注册](../installing/registration.md)。

2. 创建 [Docker Hub ![在新选项卡中打开](../../images/icons/launch-glyph.svg "在新选项卡中打开")](https://hub.docker.com/) 标识。 这是必需的，因为此部分中的指示信息包括将服务容器映像发布到 Docker Hub。

## 过程
{: #service_containers_procedure}

注：请参阅[此文档中使用的约定](../../getting_started/document_conventions.md)以获取有关命令语法的更多信息。

1. 执行[在边缘设备上安装 {{site.data.keyword.horizon}} 代理程序并使用 hello world 示例注册](../installing/registration.md)中的步骤时，您将设置 Exchange 凭证。 通过验证此命令不显示错误，确认凭证设置仍正确：

  ```
  hzn exchange user list
  ```
  {: codeblock}

2. 如果使用 {{site.data.keyword.macOS_notm}} 作为开发主机，配置 Docker 以在 `~/.docker` 中存储凭证：

   1. 打开 Docker **首选项**对话框。
   2. 取消选中**在 macOS 密钥链中安全地存储 Docker 登录**。
  
     * 如果无法取消选中此框，请执行以下步骤：
     
       1. 选中**在时间机器备份中包含 VM**. 
       2. 取消选中**在 macOS 密钥链中安全地存储 Docker 登录**。
       3. （可选）取消选中**在时间机器备份中包含 VM**.
       4. 单击**应用 & 重新启动**。
   3. 如果存在名为 `~/.docker/plaintext-passwords.json` 的文件，请将其移除。   

3. 使用先前创建的 Docker Hub 标识登录到 Docker Hub：

  ```
  export DOCKER_HUB_ID="<dockerhubid>"
  echo "<dockerhubpassword>" | docker login -u $DOCKER_HUB_ID --password-stdin
  ```
  {: codeblock}

  输出示例：
  ```
  WARNING! Your password will be stored unencrypted in ~userName/.docker/config.json.
  Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

  Login Succeeded
  ```

4. 创建加密签名密钥对。 这使您可以在将服务发布到 Exchange 时对服务进行签名。 

   注：您只需要执行一次此步骤。

  ```
  hzn key create "<companyname>" "<youremailaddress>"
  ```
  {: codeblock}
  
  其中，`companyname` 用作 x509 组织，而 `youremailaddress` 用作 x509 CN。

5. 安装一些开发工具：

  在 **{{site.data.keyword.linux_notm}}** 上：

  ```
  sudo apt install -y git jq make
  ```
  {: codeblock}

  在 **{{site.data.keyword.macOS_notm}}** 上：

  ```
  brew install git jq make
  ```
  {: codeblock}
  
  注：请参阅 [homebrew ![在新选项卡中打开](../../images/icons/launch-glyph.svg "在新选项卡中打开")](https://brew.sh/) 以获取有关根据需要安装 brew 的详细信息。

## 后续操作
{: #service_containers_what_next}

使用凭证和签名密钥来完成开发示例。 这些示例显示如何构建简单边缘服务并了解针对 {{site.data.keyword.edge_devices_notm}} 进行开发的基础知识。
