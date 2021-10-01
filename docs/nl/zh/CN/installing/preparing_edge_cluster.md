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

执行以下任务，安装边缘集群并使其准备就绪可用于 {{site.data.keyword.edge_notm}} 代理程序：

安装其中一个边缘集群并准备以用于 {{site.data.keyword.edge_notm}} 代理程序：
* [安装 OCP 边缘集群](#install_ocp_edge_cluster)
* [安装并配置 k3s 边缘集群](#install_k3s_edge_cluster)
* [安装并配置 microk8s 边缘集群](#install_microk8s_edge_cluster)（用于开发和测试，建议不要用于生产）

## 安装 OCP 边缘集群
{: #install_ocp_edge_cluster}

1. 遵循 [{{site.data.keyword.open_shift_cp}} 文档 ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://docs.openshift.com/container-platform/4.6/welcome/index.html) 中的安装指示信息，安装 OCP。 （{{site.data.keyword.ieam}} 仅在 x86_64 平台上支持 OCP。）

2. 在您从中管理 OCP 边缘集群的管理主机上安装 Kubernetes CLI (**kubectl**)、Openshift 客户机 CLI (**oc**) 和 Docker。 这也是您运行代理程序安装脚本的主机。 有关更多信息，请参阅[安装 cloudctl、kubectl 和 oc](../cli/cloudctl_oc_cli.md)。

## 安装并配置 k3s 边缘集群
{: #install_k3s_edge_cluster}

此内容总结了如何在 Ubuntu 18.04 上安装 k3s (rancher)，这是一个轻量级的小型 kubernetes 集群。 有关更多信息，请参阅 [k3s 文档 ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://rancher.com/docs/k3s/latest/en/)。

**注**：如果已安装，请先卸载 kubectl，然后再完成这些步骤。

1. 以 **root** 用户身份登录，或使用 `sudo -i` 升级为 **root** 用户

2. 机器的完整主机名必须至少包含两个点。 查看完整主机名：

   ```bash
   hostname
   ```
    {: codeblock}

   如果机器的完整主机名包含的点少于两个，请更改主机名：

   ```bash
   hostnamectl set-hostname <your-new-hostname-with-2-dots>
   ```
   {: codeblock}

   有关更多信息，请参阅 [GitHub 问题![在新的标签页中打开](../images/icons/launch-glyph.svg "在新的标签页中打开")](https://github.com/rancher/k3s/issues/53)。

3. 安装 k3s：

   ```bash
   curl -sfL https://get.k3s.io | sh -
   ```
   {: codeblock}

4. 创建映像注册表服务：
   1. 创建名为 **k3s-persistent-claim.yml** 的文件，并包含以下内容：
      ```yaml
      apiVersion: v1
      kind: PersistentVolumeClaim
      metadata:
        name: docker-registry-pvc
      spec:
        storageClassName: "local-path"
        accessModes:
          - ReadWriteOnce
        resources:
          requests:
            storage: 10Gi
      ```
      {: codeblock}

   2. 创建持久卷声明：

      ```bash
      kubectl apply -f k3s-persistent-claim.yml
      ```
      {: codeblock}

   3. 验证是否已创建持久卷声明，并且持久卷声明是否处于“暂挂”状态

      ```bash
      kubectl get pvc
      ```
      {: codeblock}

   4. 创建包含以下内容且名为 **k3s-registry-deployment.yml** 的文件：

      ```yaml
      apiVersion: apps/v1
      kind: Deployment
      metadata:
        name: docker-registry
        labels:
          app: docker-registry
      spec:
        replicas: 1
        selector:
          matchLabels:
            app: docker-registry
        template:
          metadata:
            labels:
              app: docker-registry
          spec:
            volumes:
            - name: registry-pvc-storage
              persistentVolumeClaim:
                claimName: docker-registry-pvc
            containers:
            - name: docker-registry
              image: registry
              ports:
              - containerPort: 5000
              volumeMounts:
              - name: registry-pvc-storage
                mountPath: /var/lib/registry
      ---
      apiVersion: v1
      kind: Service
      metadata:
        name: docker-registry-service
      spec:
        selector:
          app: docker-registry
        type: NodePort
        ports:
          - protocol: TCP
            port: 5000
      ```
      {: codeblock}

   5. 创建注册表部署和服务：

      ```bash
      kubectl apply -f k3s-registry-deployment.yml
      ```
      {: codeblock}

   6. 验证是否已创建该服务：

      ```bash
      kubectl get deployment
      kubectl get service
      ```
      {: codeblock}

   7. 定义注册表端点：

      ```bash
      export REGISTRY_ENDPOINT=$(kubectl get service docker-registry-service | grep docker-registry-service | awk '{print $3;}'):5000
      cat << EOF >> /etc/rancher/k3s/registries.yaml
      mirrors:
        "$REGISTRY_ENDPOINT":
          endpoint:
            - "http://$REGISTRY_ENDPOINT"
      EOF
      ```
      {: codeblock}

   8. 重新启动 k3s 以应用对 **/etc/rancher/k3s/registries.yaml** 的更改：

      ```bash
      systemctl restart k3s
      ```
      {: codeblock}

5. 将此注册表作为不安全的注册表定义到 Docker：

   1. 创建或添加到 **/etc/docker/daemon.json**（将 `<registry-endpoint>` 替换为在先前步骤中获得的 `$REGISTRY_ENDPOINT` 环境变量值）。

      ```json
      {
        "insecure-registries": [ "<registry-endpoint>" ]
      }
      ```
      {: codeblock}

   2. （可选）需要时，验证相应的 Docker 是否位于计算机上：

      ```bash
      curl -fsSL get.docker.com | sh
      ```
      {: codeblock}     

   3. 重新启动 Docker 以应用更改：

      ```bash
      systemctl restart docker
      ```
      {: codeblock}

## 安装并配置 microk8s 边缘集群
{: #install_microk8s_edge_cluster}

此内容总结了如何在 Ubuntu 18.04 上安装 microk8s，这是一个轻量级的小型 Kubernetes 集群。（有关更详细的指示信息，请参阅 [microk8s 文档 ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://microk8s.io/docs)。）

**注**：此类型的边缘集群用于开发和测试，因为单个工作程序节点 Kubernetes 集群不提供可伸缩性或高可用性。

1. 安装 microk8s：

   ```bash
   sudo snap install microk8s --classic --channel=stable
   ```
   {: codeblock}

2. 如果您未以 **root** 用户身份运行，请将用户添加到 **microk8s** 组：

   ```bash
   sudo usermod -a -G microk8s $USER
   sudo chown -f -R $USER ~/.kube
   su - $USER   # create new session for group update to take place
   ```
   {: codeblock}

3. 在 microk8s 中启用 DNS 和存储模块：

   ```bash
   microk8s.enable dns
   microk8s.enable storage
   ```
   {: codeblock}

   **注**：缺省情况下 Microk8s 使用 `8.8.8.8` 和 `8.8.4.4` 作为上游名称服务器。如果这些名称服务器无法解析管理中心主机名，您必须更改 microk8s 正在使用的名称服务器：
   
   1. 在 `/etc/resolv.conf` 或 `/run/systemd/resolve/resolv.conf` 中检索上游名称服务器的列表。

   2. 在 `kube-system` 名称空间中编辑 `coredns` 配置图。 在 `forward` 部分中设置上游名称服务器。
   
      ```bash
      microk8s.kubectl edit -n kube-system cm/coredns
      ```
      {: codeblock}
   
   3. 有关 Kubernetes DNS 的更多信息，请参阅 [Kubernetes 文档 ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://kubernetes.io/docs/tasks/administer-cluster/dns-custom-nameservers/)。


4. 检查状态：

   ```bash
   microk8s.status --wait-ready
   ```
   {: codeblock}

5. microK8s kubectl 命令名为 **microk8s.kubectl**，以防止与已安装的 **kubectl** 命令发生冲突。 假定未安装 **kubectl**，为 **microk8s.kubectl** 添加此别名：

   ```bash
   echo 'alias kubectl=microk8s.kubectl' >> ~/.bash_aliases
   source ~/.bash_aliases
   ```
   {: codeblock}

6. 启用容器注册表并配置 Docker 以容忍不安全的注册表：

   1. 启用容器注册表：

      ```bash
      microk8s.enable registry
      export REGISTRY_ENDPOINT=localhost:32000
      ```
      {: codeblock}

   2. 安装 Docker（如果尚未安装）：

      ```bash
      curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
      add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
      apt-get install docker-ce docker-ce-cli containerd.io
      ```
      {: codeblock}

   3. 将此注册表定义为对 Docker 不安全。 创建或添加到 **/etc/docker/daemon.json**（将 `<registry-endpoint>` 替换为在先前步骤中获得的 `$REGISTRY_ENDPOINT` 环境变量值）。

      ```json
      {
        "insecure-registries": [ "<registry-endpoint>" ]
      }
      ```
      {: codeblock}

   4. （可选）验证 Docker 是否在您的机器上：

      ```bash
      curl -fsSL get.docker.com | sh
      ```
      {: codeblock}   

   5. 重新启动 Docker 以应用更改：

      ```bash
      sudo systemctl restart docker
      ```
      {: codeblock}

## 下一步是什么

* [安装代理程序](edge_cluster_agent.md)
