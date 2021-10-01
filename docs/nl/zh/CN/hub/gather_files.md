---

copyright:
years: 2020
lastupdated: "2020-05-18"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 收集边缘节点文件
{: #prereq_horizon}

在边缘设备和边缘集群上安装 {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) 代理程序并将其向 {{site.data.keyword.ieam}} 注册，将需要几个文件。 此内容指导您绑定边缘节点所需的文件。 请在连接到 {{site.data.keyword.ieam}} 管理中心的管理主机上执行这些步骤。

以下步骤假定您已安装 [IBM Cloud Pak CLI (**cloudctl**) 和 OpenShift 客户机 CLI (**oc**)](../cli/cloudctl_oc_cli.md) 命令，并且将从解压缩的安装介质目录 **ibm-eam-{{site.data.keyword.semver}}-agent-x86_64** 中运行这些步骤。此脚本搜索 **agent/edge-packages-{{site.data.keyword.semver}}.tar.gz** 文件中必需的 {{site.data.keyword.horizon}} 软件包，并创建所需的边缘节点配置和证书文件。

1. 设置以下环境变量。 假定您作为管理中心安装步骤的结果仍登录到 **oc**。

   ```bash
   export CLUSTER_URL=https://$(oc get cm management-ingress-ibmcloud-cluster-info -o jsonpath='{.data.cluster_ca_domain}')
   export CLUSTER_USER=$(oc -n ibm-common-services get secret platform-auth-idp-credentials -o jsonpath='{.data.admin_username}' | base64 --decode)
   export CLUSTER_PW=$(oc -n ibm-common-services get secret platform-auth-idp-credentials -o jsonpath='{.data.admin_password}' | base64 --decode)
   oc --insecure-skip-tls-verify=true -n kube-public get secret ibmcloud-cluster-ca-cert -o jsonpath="{.data.ca\.crt}" | base64 --decode > ieam.crt
   export HZN_MGMT_HUB_CERT_PATH="$PWD/ieam.crt"
   export HZN_FSS_CSSURL=${CLUSTER_URL}/edge-css
   ```
   {: codeblock}

   定义以下 Docker 认证环境变量，以提供您自己的 **ENTITLEMENT_KEY**：
   ```
   export REGISTRY_USERNAME=cp
   export REGISTRY_PASSWORD=<ENTITLEMENT_KEY>
   ```
   {: codeblock}

   **注：**通过[我的 IBM 密钥](https://myibm.ibm.com/products-services/containerlibrary)获取权利密钥。

2. 移至 **edge-packages-{{site.data.keyword.semver}}.tar.gz** 所在的 **agent** 目录：

   ```bash
   cd agent
   ```
   {: codeblock}

3. 有两种首选方法可以使用 **edgeNodeFiles.sh** 脚本收集用于边缘节点安装的文件。 根据您的需要选择以下某种方法：

   * 运行 ***edgeNodeFiles.sh** 脚本以收集必需的文件并将它们放入模型管理系统 (MMS) 的 Cloud Sync Service (CSS) 组件中。

     **注**：**edgeNodeFiles.sh 脚本**已作为 horizon-cli 软件包的一部分进行安装且应位于您的路径中。

     ```bash
     HZN_EXCHANGE_USER_AUTH='' edgeNodeFiles.sh ALL -c -p edge-packages-{{site.data.keyword.semver}} -r cp.icr.io/cp/ieam
     ```
     {: codeblock}

     在每个边缘节点上，使用 **agent-install.sh** 的 **-i 'css:'** 标志以从 CSS 获取所需文件。

     **注**：如果您计划使用[启用 SDO 的边缘设备](../installing/sdo.md)，您必须运行此格式的 `edgeNodeFiles.sh` 命令。

   * 或者，使用 **edgeNodeFiles.sh** 以在 tar 文件中捆绑文件：

     ```bash
     edgeNodeFiles.sh ALL -t -p edge-packages-{{site.data.keyword.semver}} -r cp.icr.io/cp/ieam
     ```
     {: codeblock}

     将 tar 文件复制到每个边缘节点并使用 **agent-install.sh** 的 **-z** 标志以从 tar 文件获取所需文件。

**注**：**edgeNodeFiles.sh** 具有更多标志以控制收集的文件以及应放置的位置。要查看所有可用标志，请运行：**edgeNodeFiles.sh -h**

## 下一步是什么

在设置边缘节点之前，您或者您的节点技术人员必须创建 API 密钥并收集其他环境变量值。 遵循[准备设置边缘节点](prepare_for_edge_nodes.md)中的步骤。
