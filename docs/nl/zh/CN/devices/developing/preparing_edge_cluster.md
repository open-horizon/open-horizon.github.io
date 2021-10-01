---

copyright:
years: 2020
lastupdated: "2020-4-24"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 准备边缘集群
{: #preparing_edge_cluster}

## 准备工作

请在开始使用边缘集群前考虑以下事项：

* [先决条件](#preparing_clusters)
* [为边缘集群收集必要的信息和文件](#gather_info)

## 先决条件
{: #preparing_clusters}

在边缘集群上安装代理程序前：

1. 在代理程序安装脚本运行的环境中安装 Kubectl。
2. 在代理程序安装脚本运行的环境中安装 {{site.data.keyword.open_shift}} 客户机 (oc) CLI。
3. 获取创建相关集群资源必需的集群管理员访问权。
4. 拥有边缘集群注册表以托管代理程序 Docker 映像。
5. 安装 **cloudctl** 和 **kubectl** 命令，并抽取 **ibm-edge-computing-4.1-x86_64.tar.gz**。 请参阅[安装流程](../installing/install.md#process)。

## 为边缘集群收集必要的信息和文件
{: #gather_info}

您需要多个文件以使用 {{site.data.keyword.edge_notm}} 安装和注册边缘集群。 此部分引导您将这些文件收集到 tar 文件中，然后可以在每个边缘集群上使用这些文件。

1. 设置 **CLUSTER_URL** 环境变量：

    ```
    export CLUSTER_URL=<cluster-url>
   export USER=<your-icp-admin-user>
   export PW=<your-icp-admin-password>
    ```
    {: codeblock}

    或者，在使用 **oc login** 连接到集群后，您可以运行：

    ```
    export CLUSTER_URL=https://$(oc get routes icp-console -o jsonpath='{.spec.host}')
    ```
    {: codeblock}
    
2. 使用集群管理员权限连接到集群，然后选择 **kube-system** 作为名称空间，填写在 {{site.data.keyword.mgmt_hub}} [安装过程](../installing/install.md#process)中在 config.yaml 中定义的密码：

    ```
    cloudctl login -a $CLUSTER_URL -u admin -p <your-icp-admin-password> -n kube-system --skip-ssl-validation
    ```
    {: codeblock}    

3. 在环境变量中的边缘集群注册表上设置边缘集群注册表用户名、密码和完整映像名称。 使用以下格式指定 IMAGE_ON_EDGE_CLUSTER_REGISTRY 的值：

    ```
    <registry-name>/<repo-name>/<image-name>.
    ```
    {: codeblock} 

    如果使用 Docker Hub 作为注册表，请使用以下格式指定值：
    
    ```
    <docker-repo-name>/<image-name>
    ```
    {: codeblock}
    
    例如：
    
    ```
    export EDGE_CLUSTER_REGISTRY_USER=<your-edge-cluster-registry-username>
    export EDGE_CLUSTER_REGISTRY_PW=<your-edge-cluster-registry-password>
    export IMAGE_ON_EDGE_CLUSTER_REGISTRY=<full-image-name-on-your-edge-cluster registry>
    ```
    {: codeblock}
    
4. 下载最新版本的 **edgeDeviceFiles.sh**：

   ```
   curl -O https://raw.githubusercontent.com/open-horizon/examples/master/tools/edgeDeviceFiles.sh chmod +x edgeDeviceFiles.sh
   ```
   {: codeblock}

5. 运行 **edgeDeviceFiles.sh** 脚本以收集必要的文件：

   ```
   ./edgeDeviceFiles.sh x86_64-Cluster -t -r -o <hzn-org-id> -n <node-id> <other flags>
   ```
   {: codeblock}
    
   这将创建名为 agentInstallFiles-x86_64-Cluster..tar.gz 的文件。 
    
**命令自变量**
   
注：请指定 x86_64-Cluster 以在边缘集群上安装代理程序。
   
|命令自变量|结果|
|-----------------|------|
|t                |创建包含所有收集的文件的 **agentInstallFiles-&lt;edge-device-type&gt;.tar.gz** 文件。 如果未设置此标志，那么收集的文件将放置在当前目录中。|
|f                |指定要将收集的文件移至的目录。 如果该目录不存在，那么将创建该目录。 当前目录为缺省目录|
|r                |如果使用此标志，需要在环境变量中设置 **EDGE_CLUSTER_REGISTRY_USER**、**EDGE_CLUSTER_REGISTRY_PW** 和 **IMAGE_ON_EDGE_CLUSTER_REGISTRY**（步骤 1）。 在 4.1 中，它是必需标志。|
|o                |指定 **HZN_ORG_ID**。 此值用于边缘集群注册。|
|n                |指定 **NODE_ID**，它应该是边缘集群名称的值。 此值用于边缘集群注册。|
|s                |指定持久卷声明要使用的集群存储类。 缺省存储类为“gp2”。|
|i                |要在边缘集群上部署的代理程序映像版本。|


当准备就绪可在边缘集群上安装代理程序时，请参阅[安装代理程序和注册边缘集群](importing_clusters.md)。

<!--DELETE DOWN TO    
   The following flags are only supported for x86_64-Cluster:

    * **-r**: specify edge cluster registry if edge cluster is not using Openshift image registry. "EDGE_CLUSTER_REGISTRY_USER", "EDGE_CLUSTER_REGISTRY_PW" and "EDGE_CLUSTER_REGISTRY_REPONAME" need to be set in environment variable (step 1) if using this flag.
    * **-s**: specify cluster storage class to be used by persistent volume claim. Default storage class is "gp2".
    * **-i**: agent image version to be deployed on edge cluster
    * **-o**: specify HZN_ORG_ID. This value is used for edge cluster registration.
    * **-n**: specify NODE_ID. NODE_ID should be the value of your edge cluster name. This value is used for edge cluster registration. 

4. The command in the previous step creates a file that is called **agentInstallFiles-&lt;edge-device-type&gt;.tar.gz**. If you have other types of edge devices (different architectures), repeat the previous step for each type.

5. Take note of the API key that was created and displayed by the **edgeDeviceFiles.sh** command.

6. Now that you are logged in via **cloudctl**, if you need to create additional API keys for users to use with the {{site.data.keyword.horizon}} **hzn** command:

   ```
   cloudctl iam api-key-create "<choose-an-api-key-name>" -d "<choose-an-api-key-description>"
   ```
   {: codeblock}

   In the output of the command look for the key value in the line that starts with **API Key** and save the key value for future use.

7. When you are ready to set up edge devices, follow [Getting started using {{site.data.keyword.edge_devices_notm}}](../getting_started/getting_started.md).

Lily - is the pointer in step 7 above still correct?-->

## 下一步是什么

* [安装代理程序和注册边缘集群](importing_clusters.md)

## 相关信息

* [边缘集群](edge_clusters.md)
* [开始使用 {{site.data.keyword.edge_notm}}](../getting_started/getting_started.md)
* [安装过程](../installing/install.md#process)
