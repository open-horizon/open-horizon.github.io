---

copyright:
years: 2020
lastupdated: "2020-10-13"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 准备设置边缘节点
{: #prepare_for_edge_nodes}

此内容阐述如何创建 API 密钥并收集设置边缘节点所需的一些文件和环境变量值。 在可连接到 {{site.data.keyword.ieam}} 管理中心集群的管理主机上执行这些步骤。

## 准备工作

* 如果尚未安装 **cloudctl**，请参阅[安装 cloudctl、oc 和 kubectl](../cli/cloudctl_oc_cli.md) 以执行此操作。
* 请联系 {{site.data.keyword.ieam}} 管理员以获取通过 **cloudctl** 登录到管理中心所需的信息。

## 过程

1. 使用 `cloudctl` 登录 {{site.data.keyword.ieam}} 管理中心。 指定要为其创建 API 密钥的用户：

   ```bash
   cloudctl login -a <cluster-url> -u <user> -p <password> --skip-ssl-validation
   ```
   {: codeblock}

2. 设置边缘节点的每个用户必须具有一个 API 密钥。 您可以使用相同 API 密钥来设置所有边缘节点（不在边缘节点上进行保存）。 创建 API 密钥：

   ```bash
   cloudctl iam api-key-create "<choose-an-api-key-name>" -d "<choose-an-api-key-description>"
   ```
   {: codeblock}

   在命令输出中查找密钥值；这是以 **API Key** 开头的行。 保存密钥值以供将来使用，因为以后无法从系统进行查询。

3. 如果尚未在此主机上安装 **horizon-cli** 软件包，请立即执行此操作。 请参阅[安装后配置](post_install.md#postconfig)以获取此流程的示例。

4. 找到作为 **horizon-cli** 软件包的一部分安装的 **agent-install.sh** 和 **agent-uninstall.sh** 脚本。 设置期间在每个边缘节点上都需要这些脚本（当前，**agent-uninstall.sh** 仅支持边缘集群）：
  * Linux {{site.data.keyword.linux_notm}} 示例：

    ```
    ls /usr/horizon/bin/agent-{install,uninstall}.sh
    ```
    {: codeblock}

  * macOS 示例：

    ```
    ls /usr/local/bin/agent-{install,uninstall}.sh
    ```
    {: codeblock}

5. 请联系 {{site.data.keyword.ieam}} 管理员以获取设置这些环境变量的帮助：

  ```bash
  export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
  export HZN_ORG_ID=<your-exchange-organization>
  mgmtHubIngress=$(oc get cm management-ingress-ibmcloud-cluster-info -o jsonpath='{.data.cluster_ca_domain}')
  export HZN_FSS_CSSURL=https://$mgmtHubIngress/edge-css/
  echo "export HZN_FSS_CSSURL=$HZN_FSS_CSSURL"
  ```
  {: codeblock}

## 下一步是什么

在准备好设置边缘节点时，遵循[安装边缘节点](../installing/installing_edge_nodes.md)中的步骤。

