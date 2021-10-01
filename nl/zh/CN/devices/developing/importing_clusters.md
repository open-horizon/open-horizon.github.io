---

copyright:
  years: 2020
lastupdated: "2020-04-9"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 安装代理程序和注册边缘集群
{: #importing_clusters}

您可以在以下边缘集群上安装代理程序：

* Kubernetes
* 轻量级小型 Kuberetes（建议用于测试）

## 在 Kubernetes 边缘集群上安装代理程序
{: #install_kube}

自动代理程序安装可通过运行 `agent-install.sh` 脚本实现。 

在代理程序安装脚本将运行的环境中按照以下步骤操作：

1. 从管理员处获取 `agentInstallFiles-x86_64-Cluster.tar.gz` 文件和 API 密钥。 这些应该已在[为边缘集群收集必要的信息和文件](preparing_edge_cluster.md)中创建。

2. 在环境变量中为后续步骤设置文件名：

   ```
   export AGENT_TAR_FILE=agentInstallFiles-x86_64-Cluster.tar.gz
   ```
   {: codeblock}

3. 从 tar 文件中抽取这些文件：

   ```
   tar -zxvf agentInstallFiles-x86_64-Cluster.tar.gz
   ```
   {: codeblock}

4. 导出 Horizon Exchange 用户凭证，可能使用以下某个格式：

   ```
   export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
   ```
   {: codeblock}

   或者

   ```
   export HZN_EXCHANGE_USER_AUTH=<username>/<username>:<password>
   ```
   {: codeblock}

5. 运行 `agent-install.sh` 命令以安装和配置 Horizon 代理程序，并注册边缘集群以运行 helloworld 样本边缘服务：

   ```
   ./agent-install.sh -u $HZN_EXCHANGE_USER_AUTH -k agent-install.cfg  -D cluster -p
   ```
   {: codeblock}

   注：在代理程序安装期间，您可能会看到此提示：**要覆盖 Horizon 吗？[y/N]:**. 请选择 **y** 并按 **Enter**; `agent-install.sh` 正确设置配置。

6. （可选）查看可用的 `agent-install.sh` 标志描述： 

   ```
   ./agent-install.sh -h
   ```
   {: codeblock}

7. 列出 Kubernetes 上正在运行的代理程序资源。 由于已在边缘集群上安装代理程序，并且已注册边缘集群，您可以列出以下边缘集群资源：

   * 名称空间：

   ```
   kubectl get namespace openhorizon-agent
   ```
   {: codeblock}

   * 部署：

   ```
   kubectl get deployment -n openhorizon-agent
   ```
   {: codeblock}

   列出代理程序部署的详细信息：

   ```
   kubectl get deployment -n openhorizon-agent -o yaml
   ```
   {: codeblock}

   * 配置图：

   ```
   kubectl get configmap openhorizon-agent-config -n openhorizon-agent -o yaml
   ```
   {: codeblock}

   * 密钥：
   
   ```
   kubectl get secret openhorizon-agent-secrets -n openhorizon-agent -o yaml
   ```
   {: codeblock}

   * PersistentVolumeClaim：
   
   ```
   kubectl get pvc openhorizon-agent-pvc -n openhorizon-agent -o yaml
   ```
   {: codeblock}

   * pod：

   ```
   kubectl get pod -n openhorizon-agent
   ```
   {: codeblock}

8. 查看日志，获取 pod 标识： 

   ```
   kubectl logs <pod-id> -n openhorizon-agent
   ```
   {: codeblock}

9. 在代理程序容器内执行 `hzn` 命令：

   ```
   kubectl exec -it <pod-id> -n openhorizon-agent /bin/bash
   hzn --help
   ```
   {: codeblock}

10. 浏览 `hzn` 命令标志和子命令：

   ```
   hzn --help
   ```
   {: codeblock}

## 在轻量级小型 Kubernetes 边缘集群上安装代理程序

此内容描述如何在 microk8s（可在本地安装和配置的轻量级小型 Kubernetes 集群）中安装代理程序，包括：

* 安装和配置 microk8s
* 在 microk8s 上安装代理程序

### 安装和配置 microk8s

1. 安装 microk8s：

   ```
   sudo snap install microk8s --classic --channel=1.14/stable
   ```
   {: codeblock}

2. 为 microk8s.kubectl 设置别名：

   注：如果要在 microk8s 上进行测试，请确保没有 `kubectl` 命令。 

  * microK8s 使用 namespaced kubectl 命令来防止与 kubectl 的任何现有安装发生冲突。 如果没有现有安装，添加别名更容易（`append to ~/.bash_aliases`）： 
   
   ```
   alias kubectl='microk8s.kubectl' 
   ```
   {: codeblock}
  
   * 然后：

   ```
   source ~/.bash_aliases
   ```
   {: codeblock}

3. 在 microk8s 中启用 DNS 和存储模块：

   ```
   microk8s.enable dns storage
   ```
   {: codeblock}

4. 在 microk8s 中创建存储类。 代理程序安装脚本使用 `gp2` 作为持久卷声明的缺省存储类。 此存储类需要在安装代理程序前在 microk8s 环境中创建。 如果边缘集群代理程序将使用其他存储类，那么它还必须事先创建好。 

   以下是创建 `gp2` 作为存储类的示例：  

   1. 创建 storageClass.yml 文件： 

      ```
      apiVersion: storage.k8s.io/v1
      kind: StorageClass
      metadata:
       name: gp2
      provisioner: microk8s.io/hostpath
      reclaimPolicy: Delete
      volumeBindingMode: Immediate
      ```
      {: codeblock}

   2. 使用 `kubectl` 命令在 microk8s 中创建 storageClass 对象：

      ```
      kubectl apply -f storageClass.yml
      ```
      {: codeblock}

### 在 microk8s 上安装代理程序

执行以下步骤，在 microk8s 上安装代理程序。

1. 完成[步骤 1-3](#install_kube)。

2. 运行 `agent-install.sh` 命令以安装和配置 Horizon 代理程序，并注册边缘集群以运行 helloworld 样本边缘服务：

   ```
   source agent-install.sh -u $HZN_EXCHANGE_USER_AUTH -k agent-install.cfg  -D cluster -p "IBM/pattern-ibm.helloworld"
   ```
   {: codeblock}

   注：在代理程序安装期间，您可能会看到此提示：**要覆盖 Horizon 吗？[y/N]:**. 请选择 **y** 并按 **Enter**; `agent-install.sh` 正确设置配置。

## 从 Kubernetes 轻量级集群中移除代理程序 

注：因为代理程序卸载脚本在此发行版中不完整，所以通过删除 openhorizon-agent 名称空间来完成代理程序移除。

1. 删除名称空间：

   ```
   kubectl delete namespace openhorizon-agent
   ```
   {: codeblock}

      注：删除名称空间有时会停留在“正在终止”状态。 在这种情况下，请参阅[名称空间陷入“正在终止”状态 ![在新的选项卡中打开](../../images/icons/launch-glyph.svg "在新的选项卡中打开")](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.1.1/troubleshoot/ns_terminating.html) 以手动删除名称空间。

2. 删除 clusterrolebinding： 

   ```
   kubectl delete clusterrolebinding openhorizon-agent-cluster-rule
   ```
   {: codeblock}

<!--If this installation was done as part of a prerequisite for {{site.data.keyword.edge_devices_notm}}, [return to continue that installation](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/devices/installing/install.html).-->
