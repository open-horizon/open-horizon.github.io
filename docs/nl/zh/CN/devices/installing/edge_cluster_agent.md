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

# 安装代理程序
{: #importing_clusters}

首先在以下某种类型的 Kubernetes 边缘集群上安装 {{site.data.keyword.edge_notm}} 代理程序：

* [在 {{site.data.keyword.ocp}} Kubernetes 边缘集群上安装代理程序](#install_kube)
* [在 k3s 和 microk8s 边缘集群上安装代理程序](#install_lite)

然后将边缘服务部署到边缘集群：

* [将服务部署到边缘集群](#deploying_services)

如果需要移除代理程序：

* [从边缘集群移除代理程序](#remove_agent)

## 在 {{site.data.keyword.ocp}} Kubernetes 边缘集群上安装代理程序
{: #install_kube}

此部分描述如何在 {{site.data.keyword.ocp}} 边缘集群上安装 {{site.data.keyword.ieam}} 代理程序。在对边缘集群具有管理员访问权的主机上执行以下步骤：

1. 以 **admin** 身份登录到边缘集群：

   ```bash
	oc login https://<API_ENDPOINT_HOST>:<PORT> -u <ADMIN_USER> -p <ADMIN_PASSWORD> --insecure-skip-tls-verify=true
   ```
   {: codeblock}

2. 将代理程序名称空间变量设置为其缺省值（或您要将代理程序显式安装到的任何名称空间）：

   ```bash
   export AGENT_NAMESPACE=openhorizon-agent
   ```
   {: codeblock}

3. 将您希望代理程序使用的存储类设置为内置存储类或您创建的存储类。例如：

   ```bash
   export EDGE_CLUSTER_STORAGE_CLASS=rook-ceph-cephfs-internal
   ```
   {: codeblock}

4. 要在边缘集群上设置映像注册表，请执行[使用 OpenShift 映像注册表](../developing/container_registry.md##ocp_image_registry)的步骤 2-8，但进行下面这项更改：在步骤 4 中，将 **OCP_PROJECT** 设置为：**$AGENT_NAMESPACE**。

5. **agent-install.sh** 脚本将 {{site.data.keyword.ieam}} 代理程序存储在边缘集群容器注册表中。设置应该使用的注册表用户、密码和完整映像路径（去掉标记）：

   ```bash
   export EDGE_CLUSTER_REGISTRY_USERNAME=$OCP_USER
   export EDGE_CLUSTER_REGISTRY_TOKEN="$OCP_TOKEN"
   export IMAGE_ON_EDGE_CLUSTER_REGISTRY=$OCP_DOCKER_HOST/$OCP_PROJECT/amd64_anax_k8s
   ```
   {: codeblock}

   **注：**{{site.data.keyword.ieam}} 代理程序映像存储在本地边缘集群注册表中，因为边缘集群 Kubernetes 需要持续访问该映像，以备需要将其重新启动或移至另一个 pod。

6. 导出 Horizon Exchange 用户凭证：

   ```bash
   export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
   ```
   {: codeblock}

7. 从管理员处获取 **agentInstallFiles-x86_64-Cluster.tar.gz** 文件和 API 密钥。 这些应该已在[为边缘集群收集必要的信息和文件](preparing_edge_cluster.md)中创建。

8. 从 tar 文件抽取 **agent-install.sh** 脚本：

   ```bash
   tar -zxvf agentInstallFiles-x86_64-Cluster.tar.gz agent-install.sh
   ```
   {: codeblock}

9. 运行 **agent-install.sh** 命令以安装和配置 Horizon 代理程序，并使用策略注册边缘集群：

   ```bash
   ./agent-install.sh -D cluster -z agentInstallFiles-x86_64-Cluster.tar.gz -d <node-id>
   ```
   {: codeblock}

   **注：**
   * 要查看所有可用标志，请运行 **./agent-install.sh -h**
   * 如果发生错误，导致 **agent-install.sh** 未完成，请运行 **agent-uninstall.sh**（请参阅[从边缘集群移除代理程序](#remove_agent)），然后重复此部分中的步骤。

10. 切换到代理程序的名称空间/项目，并验证代理程序 pod 是否正在运行：

   ```bash
   oc project $AGENT_NAMESPACE
   oc get pods
   ```
   {: codeblock}

11. 由于已在边缘集群上安装代理程序，如果您希望熟悉与代理程序相关联的 Kubernetes 资源，您可以运行以下命令：

   ```bash
   oc get namespace $AGENT_NAMESPACE
   oc project $AGENT_NAMESPACE   # ensure this is the current namespace/project
   oc get deployment -o wide
   oc get deployment agent -o yaml   # get details of the deployment
   oc get configmap openhorizon-agent-config -o yaml
   oc get secret openhorizon-agent-secrets -o yaml
   oc get pvc openhorizon-agent-pvc -o yaml   # persistent volume
   ```
   {: codeblock}

12. 通常，如果某个边缘集群针对策略进行了注册，但没有任何用户指定的节点策略，那么任何部署策略都不会将边缘服务部署到该集群。Horizon 示例就是这种情况。继续[将服务部署到边缘集群](#deploying_services)，以设置节点策略，以便边缘服务将部署到此边缘集群。

## 在 k3s 和 microk8s 边缘集群上安装代理程序
{: #install_lite}

此部分描述如何在 k3s 或 microk8s（轻量级和小型 kubernetes 集群）上安装 {{site.data.keyword.ieam}} 代理程序：

1. 以 **root** 身份登录到边缘集群。

2. 从管理员处获取 **agentInstallFiles-x86_64-Cluster.tar.gz** 文件和 API 密钥。 这些应该已在[为边缘集群收集必要的信息和文件](preparing_edge_cluster.md)中创建。

3. 从 tar 文件抽取 **agent-install.sh** 脚本：

   ```bash
   tar -zxvf agentInstallFiles-x86_64-Cluster.tar.gz agent-install.sh
   ```
   {: codeblock}

4. 导出 Horizon Exchange 用户凭证：

   ```bash
   export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
   ```
   {: codeblock}

5. **agent-install.sh** 脚本将 {{site.data.keyword.ieam}} 代理程序存储在边缘集群映像注册表中。设置应该使用的完整映像路径（去掉标记）。例如：

   ```bash
   export IMAGE_ON_EDGE_CLUSTER_REGISTRY=$REGISTRY_ENDPOINT/openhorizon-agent/amd64_anax_k8s
   ```
   {: codeblock}

   **注：**{{site.data.keyword.ieam}} 代理程序映像存储在本地边缘集群注册表中，因为边缘集群 Kubernetes 需要持续访问该映像，以备需要将其重新启动或移至另一个 pod。

6. 指示 **agent-install.sh** 使用缺省存储类：

   * 在 k3s 上：

      ```bash
      export EDGE_CLUSTER_STORAGE_CLASS=local-path
      ```
      {: codeblock}

   * 在 microk8s 上：

      ```bash
      export EDGE_CLUSTER_STORAGE_CLASS=microk8s-hostpath
      ```
      {: codeblock}

7. 运行 **agent-install.sh** 命令以安装和配置 Horizon 代理程序，并使用策略注册边缘集群：

   ```bash
   ./agent-install.sh -D cluster -z agentInstallFiles-x86_64-Cluster.tar.gz -d <node-id>
   ```
   {: codeblock}

   **注：**
   * 要查看所有可用标志，请运行 **./agent-install.sh -h**
   * 如果发生错误，导致 **agent-install.sh** 未完成，请运行 **agent-uninstall.sh**（请参阅[从边缘集群移除代理程序](#remove_agent)），然后再次运行 **agent-install.sh**。

8. 验证代理程序 pod 是否处于运行状态：

   ```bash
   kubectl get namespaces
   kubectl -n openhorizon-agent get pods
   ```
   {: codeblock}

9. 通常，如果某个边缘集群针对策略进行了注册，但没有任何用户指定的节点策略，那么任何部署策略都不会将边缘服务部署到该集群。Horizon 示例就是这种情况。继续[将服务部署到边缘集群](#deploying_services)，以设置节点策略，以便边缘服务将部署到此边缘集群。

## 将服务部署到边缘集群
{: #deploying_services}

在此边缘集群上设置节点策略可能导致部署策略在此处部署边缘服务。本部分显示了执行该操作的一个示例。

1. 设置一些别名，便于运行 `hzn` 命令。（`hzn` 命令位于代理程序容器中，但使用这些别名，就可以从此主机运行 `hzn`。）

   ```bash
   cat << 'END_ALIASES' >> ~/.bash_aliases
   alias getagentpod='kubectl -n openhorizon-agent get pods --selector=app=agent -o jsonpath={.items[*].metadata.name}'
   alias hzn='kubectl -n openhorizon-agent exec -i $(getagentpod) -- hzn'
   END_ALIASES
   source ~/.bash_aliases
   ```
   {: codeblock}

2. 验证边缘节点是否已配置（向 {{site.data.keyword.ieam}} 管理中心注册）：

   ```bash
   hzn node list
   ```
   {: codeblock}

3. 要测试边缘集群代理程序，请使用将导致示例 helloworld 操作程序和服务部署到此边缘节点的属性来设置节点策略：

   ```bash
   cat << 'EOF' > operator-example-node.policy.json
   {
     "properties": [
       { "name": "openhorizon.example", "value": "operator" }
     ]
   }
   EOF

   cat operator-example-node.policy.json | hzn policy update -f-
   hzn policy list
   ```
   {: codeblock}

   **注：**
   * 由于实际 **hzn** 命令正在代理程序容器内部运行，因此对于需要输入文件的任何 `hzn` 子命令，需要将该文件管道化到命令中，以便将其内容传输到容器中。

4. 1 分钟后，请检查是否存在协议以及正在运行的边缘操作程序和服务容器：

   ```bash
   hzn agreement list
   kubectl -n openhorizon-agent get pods
   ```
   {: codeblock}

5. 使用先前命令中的 pod 标识，查看边缘操作程序和服务的日志：

   ```bash
   kubectl -n openhorizon-agent logs -f <operator-pod-id>
   # control-c to get out
   kubectl -n openhorizon-agent logs -f <service-pod-id>
   # control-c to get out
   ```
   {: codeblock}

6. 您还可以查看代理程序传递到边缘服务的环境变量：

   ```bash
   kubectl -n openhorizon-agent exec -i <service-pod-id> -- env | grep HZN_
   ```
   {: codeblock}

### 更改将哪些服务部署到边缘集群
{: #changing_services}

* 要更改将哪些服务部署到边缘集群，请更改节点策略：

  ```bash
  cat <new-node-policy>.json | hzn policy update -f-
  hzn policy list
  ```
  {: codeblock}

   在一两分钟后，新服务将部署到此边缘集群。

* 注：在某些类型的 VM 上使用 microk8s 时，被停止（替换）的服务 pod 可能会卡在**正在终止**状态。如果发生此情况，可以通过运行以下命令来将其清除：

  ```bash
  kubectl delete pod <pod-id> -n openhorizon-agent --force --grace-period=0
  pkill -fe <service-process>
  ```
  {: codeblock}

* 如果要使用模式（而不是策略）以在边缘集群上运行服务：

  ```bash
  hzn unregister -f
  hzn register -n $HZN_EXCHANGE_NODE_AUTH -p <pattern-name>
  ```
  {: codeblock}

## 从边缘集群中移除代理程序
{: #remove_agent}

要注销边缘集群并从该集群中移除 {{site.data.keyword.ieam}} 代理程序，请执行以下步骤：

1. 从 tar 文件解压缩 **agent-uninstall.sh** 脚本：

   ```bash
   tar -zxvf agentInstallFiles-x86_64-Cluster.tar.gz agent-uninstall.sh
   ```
   {: codeblock}

2. 导出 Horizon Exchange 用户凭证：

   ```bash
   export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
   ```
   {: codeblock}

3. 移除代理程序：

   ```bash
   ./agent-uninstall.sh -u $HZN_EXCHANGE_USER_AUTH -d
   ```
   {: codeblock}

注：删除名称空间有时会停留在“正在终止”状态。 在这种情况下，请参阅[名称空间陷入“正在终止”状态 ![在新的选项卡中打开](../../images/icons/launch-glyph.svg "在新的选项卡中打开")](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.1.1/troubleshoot/ns_terminating.html) 以手动删除名称空间。
