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

**注**：{{site.data.keyword.ieam}} 代理程序安装需要边缘集群上的集群管理员访问权。

首先在以下某种类型的 Kubernetes 边缘集群上安装 {{site.data.keyword.edge_notm}} 代理程序：

* [在 {{site.data.keyword.ocp}} Kubernetes 边缘集群上安装代理程序](#install_kube)
* [在 k3s 和 microk8s 边缘集群上安装代理程序](#install_lite)

然后，将边缘服务部署到边缘集群：

* [将服务部署到边缘集群](#deploying_services)

如果需要移除代理程序：

* [从边缘集群移除代理程序](../using_edge_services/removing_agent_from_cluster.md)

## 在 {{site.data.keyword.ocp}} Kubernetes 边缘集群上安装代理程序
{: #install_kube}

此内容描述如何在 {{site.data.keyword.ocp}} 边缘集群上安装 {{site.data.keyword.ieam}} 代理程序。 在对边缘集群具有管理员访问权的主机上执行以下步骤：

1. 以 **admin** 身份登录到边缘集群：

   ```bash
   oc login https://<api_endpoint_host>:<port> -u <admin_user> -p <admin_password> --insecure-skip-tls-verify=true
   ```
   {: codeblock}

2. 如果尚未完成[准备设置边缘节点](../hub/prepare_for_edge_nodes.md)中的步骤，请立即执行。 此过程创建 API 密钥，查找某些文件，并收集设置边缘节点时所需的环境变量值。 在此边缘集群上设置相同环境变量：

  ```bash
  export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
  export HZN_ORG_ID=<your-exchange-organization>
  export HZN_FSS_CSSURL=https://<ieam-management-hub-ingress>/edge-css/
  ```
  {: codeblock}

3. 将代理程序名称空间变量设置为其缺省值（或您要将代理程序显式安装到的任何名称空间）：

   ```bash
   export AGENT_NAMESPACE=openhorizon-agent
   ```
   {: codeblock}

4. 设置您希望代理程序使用的存储类 - 内置存储类或您创建的存储类。 您可以使用以下两个命令中的第一个来查看可用存储类，然后将要使用的存储类的名称替换为第二个命令。 一个存储类应该标记为 `(default)`：

   ```bash
   oc get storageclass
   export EDGE_CLUSTER_STORAGE_CLASS=<rook-ceph-cephfs-internal>
   ```
   {: codeblock}

5. 确定是否已创建 {{site.data.keyword.open_shift}} 映像注册表的缺省路由，以使其可从集群外部访问：

   ```bash
   oc get route default-route -n openshift-image-registry --template='{{ .spec.host }}'
   ```
   {: codeblock}

   如果命令响应指示找不到 **default-route**，您需要进行公开（请参阅 [Exposing the registry ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://docs.openshift.com/container-platform/4.6/registry/securing-exposing-registry.html) 以获取详细信息）：

   ```bash
   oc patch configs.imageregistry.operator.openshift.io/cluster --patch '{"spec":{"defaultRoute":true}}' --type=merge
   ```
   {: codeblock}

6. 检索您需要使用的存储库路由名称：

   ```bash
   export OCP_IMAGE_REGISTRY=`oc get route default-route -n openshift-image-registry --template='{{ .spec.host }}'`
   ```
   {: codeblock}

7. 创建新项目以存储映像：

   ```bash
   export OCP_PROJECT=$AGENT_NAMESPACE
   oc new-project $OCP_PROJECT
   ```
   {: codeblock}

8. 使用您选择的名称创建服务帐户：

   ```bash
   export OCP_USER=<service-account-name>
   oc create serviceaccount $OCP_USER
   ```
   {: codeblock}

9. 将角色添加到当前项目的服务帐户：

   ```bash
   oc policy add-role-to-user edit system:serviceaccount:$OCP_PROJECT:$OCP_USER
   ```
   {: codeblock}

10. 将服务帐户令牌设置为以下环境变量：

   ```bash
   export OCP_TOKEN=`oc serviceaccounts get-token $OCP_USER`
   ```
   {: codeblock}

11. 获取 {{site.data.keyword.open_shift}} 证书并允许 Docker 信任此证书：

   ```bash
   echo | openssl s_client -connect $OCP_IMAGE_REGISTRY:443 -showcerts | sed -n "/-----BEGIN CERTIFICATE-----/,/-----END CERTIFICATE-----/p" > ca.crt
   ```
   {: codeblock}

   在 {{site.data.keyword.linux_notm}} 上：

   ```bash
   mkdir -p /etc/docker/certs.d/$OCP_IMAGE_REGISTRY
   cp ca.crt /etc/docker/certs.d/$OCP_IMAGE_REGISTRY
   systemctl restart docker.service
   ```
   {: codeblock}

   在 {{site.data.keyword.macOS_notm}} 上：

   ```bash
   mkdir -p ~/.docker/certs.d/$OCP_IMAGE_REGISTRY
   cp ca.crt ~/.docker/certs.d/$OCP_IMAGE_REGISTRY
   ```
   {: codeblock}

   在 {{site.data.keyword.macOS_notm}} 上，使用桌面菜单栏右侧的 Docker 桌面图标并通过单击下拉菜单中的**重新启动**来重新启动 Docker。

12. 登录 {{site.data.keyword.ocp}} Docker 主机：

   ```bash
   echo "$OCP_TOKEN" | docker login -u $OCP_USER --password-stdin $OCP_IMAGE_REGISTRY
   ```
   {: codeblock}

13. 为映像注册表访问配置其他信任库：   

    ```bash
    oc create configmap registry-config --from-file=$OCP_IMAGE_REGISTRY=ca.crt -n openshift-config
    ```
    {: codeblock}

14. 编辑新的 `registry-config`：

    ```bash
    oc edit image.config.openshift.io cluster
    ```
    {: codeblock}

15. 更新 `spec:` 部分：

    ```bash
    spec:
      additionalTrustedCA:
      name: registry-config
    ```
    {: codeblock}

16. **agent-install.sh** 脚本将 {{site.data.keyword.ieam}} 代理程序存储在边缘集群容器注册表中。 设置注册表用户、密码和完整映像路径（去掉标记）：

   ```bash
   export EDGE_CLUSTER_REGISTRY_USERNAME=$OCP_USER
   export EDGE_CLUSTER_REGISTRY_TOKEN="$OCP_TOKEN"
   export IMAGE_ON_EDGE_CLUSTER_REGISTRY=$OCP_IMAGE_REGISTRY/$OCP_PROJECT/amd64_anax_k8s
   ```
   {: codeblock}

   **注**：{{site.data.keyword.ieam}} 代理程序映像存储在本地边缘集群注册表中，因为边缘集群 Kubernetes 需要持续访问该映像，以备需要将其重新启动或移至另一个 pod。

17. 将 **agent-install.sh** 脚本复制到新的边缘集群。

18. 运行 **agent-install.sh** 以从 CSS (Cloud Sync Service) 获取必要文件，安装并配置 {{site.data.keyword.horizon}}代理程序，然后使用策略注册边缘集群：

   ```bash
   ./agent-install.sh -D cluster -i 'css:'
   ```
   {: codeblock}

   **注**：
   * 要查看所有可用标志，请运行 **./agent-install.sh -h**
   * 如果错误导致 **agent-install.sh** 失败，请纠正错误，然后重新运行 **agent-install.sh**。 如果无效，请运行 **agent-uninstall.sh**（请参阅[从边缘集群移除代理程序](../using_edge_services/removing_agent_from_cluster.md)），然后再重新运行 **agent-install.sh**。

19. 切换到代理程序名称空间（也称为项目）并验证代理程序 pod 正在运行：

   ```bash
   oc project $AGENT_NAMESPACE
   oc get pods
   ```
   {: codeblock}

20. 由于已在边缘集群上安装代理程序，如果您希望熟悉与代理程序相关联的 Kubernetes 资源，您可以运行以下命令：

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

21. 通常，如果某个边缘集群针对策略进行了注册，但没有用户指定的节点策略，那么任何部署策略都不会将边缘服务部署到该集群。 Horizon 示例就是这种情况。 继续[将服务部署到边缘集群](#deploying_services)，以设置节点策略，以便边缘服务将部署到此边缘集群。

## 在 k3s 和 microk8s 边缘集群上安装代理程序
{: #install_lite}

此内容描述如何在 [k3s ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://k3s.io/) 或 [microk8s ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://microk8s.io/)、轻量级和小型 Kubernetes 集群上安装 {{site.data.keyword.ieam}} 代理程序：

1. 以 **root** 身份登录到边缘集群。

2. 如果尚未完成[准备设置边缘节点](../hub/prepare_for_edge_nodes.md)中的步骤，请立即执行。 此过程创建 API 密钥，查找某些文件，并收集设置边缘节点时所需的环境变量值。 在此边缘集群上设置相同环境变量：

  ```bash
  export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
  export HZN_ORG_ID=<your-exchange-organization>
  export HZN_FSS_CSSURL=https://<ieam-management-hub-ingress>/edge-css/
  ```
  {: codeblock}

3. 将 **agent-install.sh** 脚本复制到新的边缘集群。

4. **agent-install.sh** 脚本将 {{site.data.keyword.ieam}} 代理程序存储在边缘集群映像注册表中。 设置应该使用的完整映像路径（去掉标记）。 例如：

   * 在 k3s 上：

      ```bash
      REGISTRY_ENDPOINT=$(kubectl get service docker-registry-service | grep docker-registry-service | awk '{print $3;}'):5000
      export IMAGE_ON_EDGE_CLUSTER_REGISTRY=$REGISTRY_ENDPOINT/openhorizon-agent/amd64_anax_k8s
      ```
      {: codeblock}

   * 在 microk8s 上：

      ```bash
      export IMAGE_ON_EDGE_CLUSTER_REGISTRY=localhost:32000/openhorizon-agent/amd64_anax_k8s
      ```
      {: codeblock}

   **注**：{{site.data.keyword.ieam}} 代理程序映像存储在本地边缘集群注册表中，因为边缘集群 Kubernetes 需要持续访问该映像，以备需要将其重新启动或移至另一个 pod。

5. 指示 **agent-install.sh** 使用缺省存储类：

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

6. 运行 **agent-install.sh** 以从 CSS (Cloud Sync Service) 获取必要文件，安装并配置 {{site.data.keyword.horizon}}代理程序，然后使用策略注册边缘集群：

   ```bash
   ./agent-install.sh -D cluster -i 'css:'
   ```
   {: codeblock}

   **注**：
   * 要查看所有可用标志，请运行 **./agent-install.sh -h**
   * 如果发生错误，导致 **agent-install.sh** 未成功完成，请纠正显示的错误，然后重新运行 **agent-install.sh**。 如果无效，请运行 **agent-uninstall.sh**（请参阅[从边缘集群移除代理程序](../using_edge_services/removing_agent_from_cluster.md)），然后再重新运行 **agent-install.sh**。

7. 验证代理程序 pod 是否正在运行：

   ```bash
   kubectl get namespaces
   kubectl -n openhorizon-agent get pods
   ```
   {: codeblock}

8. 通常，如果某个边缘集群针对策略进行了注册，但没有任何用户指定的节点策略，那么任何部署策略都不会将边缘服务部署到该集群。 这是期望的行为。 继续[将服务部署到边缘集群](#deploying_services)，以设置节点策略，以便边缘服务将部署到此边缘集群。

## 将服务部署到边缘集群
{: #deploying_services}

在此边缘集群上设置节点策略可能导致部署策略在此处部署边缘服务。 此内容显示了执行该操作的一个示例。

1. 设置一些别名，便于运行 `hzn` 命令。 （`hzn` 命令位于代理程序容器中，但使用这些别名，就可以从此主机运行 `hzn`。）

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

3. 要测试边缘集群代理程序，请使用将示例 helloworld 操作程序和服务部署到此边缘节点的属性来设置节点策略：

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

   **注**：
   * 由于实际 **hzn** 命令正在代理程序容器内部运行，因此对于需要输入文件的任何 `hzn` 命令，需要将该文件管道化到命令中，以便将其内容传输到容器中。

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

* **注**：在某些使用 microk8s 的 VM 上，被停止（替换）的服务 pod 可能会卡在**正在终止**状态。 如果发生此情况，请运行：

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
