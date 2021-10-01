---

copyright:
years: 2019
lastupdated: "2019-09-18"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# {{site.data.keyword.icp_notm}} 环境中的故障诊断提示
{: #troubleshooting_icp}

复审此内容以帮助对与 {{site.data.keyword.edge_devices_notm}} 相关的 {{site.data.keyword.icp_notm}} 环境的常见问题进行故障诊断。每个提问的提示和指南都可以帮助您解决常见问题，以及获取信息来确定根本原因。{:shortdesc}

   * [您的 {{site.data.keyword.edge_devices_notm}} 凭证是否正确配置用于 {{site.data.keyword.icp_notm}} 环境中？](#setup_correct)

### 您的 {{site.data.keyword.edge_devices_notm}} 凭证是否正确配置用于 {{site.data.keyword.icp_notm}} 环境中？
{: #setup_correct}

您需要 {{site.data.keyword.icp_notm}} 用户帐户来完成此环境中的 {{site.data.keyword.edge_devices_notm}} 内的任何操作。您还需要从该帐户创建的 API 密钥。

要在此环境中验证您的 {{site.data.keyword.edge_devices_notm}} 凭证，请运行以下命令：

   ```
   hzn exchange user list
    ```
   {: codeblock}

如果从显示一个或多个用户的 Exchange 返回 JSON 格式化条目，那么表明正确配置了 {{site.data.keyword.edge_devices_notm}} 凭证。

如果返回了错误响应，那么可以采取步骤对凭证设置进行故障诊断。

如果错误消息指示 API 密钥不正确，那么可以使用以下命令创建新 API 密钥。

**注：**首先，为这些命令中以 `$` 为前缀的所有环境变量设置相应的值：

   ```
   cloudctl login -a $ICP_URL -u $USER -p $PW -n kube-public --skip-ssl-validation
   cloudctl iam api-key-create "$KEY_NAME" -d "$KEY_DESC"
   ```
   {: codeblock}

如果错误消息指示证书无效，请使用以下命令创建新的自签名证书：

   ```
   kubectl -n kube-public get secret ibmcloud-cluster-ca-cert -o jsonpath="{.data['ca\.crt']}" | base64 --decode > icp.crt
     ```
   {: codeblock}

然后，指示操作系统信任此证书。在 Linux 机器上，运行以下命令：

   ```
   sudo cp icp.crt /usr/local/share/ca-certificates &&  sudo update-ca-certificates
       ````
   {: codeblock}

在 MacOS 机器上，运行以下命令：

   ```
   sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain icp.crt
       ```
   {: codeblock}
