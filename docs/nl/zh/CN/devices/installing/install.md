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

# 安装管理中心
{: #hub_install_overview}
 
您必须先安装并配置管理中心，然后才能继续执行 {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) 节点任务。

{{site.data.keyword.ieam}} 提供边缘计算功能，以帮助您管理工作负载并将其从中心集群部署到 OpenShift® Container Platform 4.2 或其他基于 Kubernetes 的集群的远程实例。

{{site.data.keyword.ieam}} 使用 IBM Multicloud Management Core 1.2 控制将容器化工作负载部署到远程位置上的 OpenShift® Container Platform 4.2 集群托管的边缘服务器、网关和设备。

此外，{{site.data.keyword.ieam}} 包含对 Edge Computing Manager 概要文件的支持。 此受支持的概要文件可以帮助您在安装用于托管远程边缘服务器的 OpenShift® Container Platform 4.2 时，减少 OpenShift® Container Platform 4.2 的资源使用。 此概要文件提供了对这些服务器环境和托管在其中的企业关键型应用程序进行可靠远程管理所需的最低服务。 使用此概要文件，您仍然能够对用户进行身份验证，收集日志和事件数据，并在单个或一组聚集的工作程序节点中部署工作负载。

# 安装管理中心

{{site.data.keyword.edge_notm}} 安装过程指导您完成以下高级别的安装和配置步骤：
{:shortdesc}

  - [安装摘要](#sum)
  - [大小调整](#size)
  - [先决条件](#prereq)
  - [安装过程](#process)
  - [安装后的配置](#postconfig)
  - [收集必需的信息和文件](#prereq_horizon)
  - [卸载](#uninstall)

## 安装摘要
{: #sum}

* 部署下列管理中心组件：
  * {{site.data.keyword.edge_devices_notm}} Exchange API。
  * {{site.data.keyword.edge_devices_notm}} agbot。
  * {{site.data.keyword.edge_devices_notm}} Cloud Sync Service (CSS)。
  * {{site.data.keyword.edge_devices_notm}} 用户界面。
* 确认安装成功。
* 填充样本边缘服务。

## 调整大小
{: #size}

此大小调整信息仅用于 {{site.data.keyword.edge_notm}} 服务，不在 {{site.data.keyword.edge_shared_notm}} 的大小调整建议（可在[此处记录内容](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/servers/cluster_sizing.html)中找到）中。

### 数据库存储需求

* PostgreSQL Exchange
  * 10 GB 缺省值
* PostgreSQL AgBot
  * 10 GB 缺省值  
* MongoDB Cloud Sync Service
  * 50 GB 缺省值

### 计算需求

利用 [Kubernetes 计算资源](https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container)的服务将在可用工作程序节点间进行调度。 建议至少使用三个工作程序节点。

* 这些配置更改将最多支持 10,000 个边缘设备：

  ```
  exchange:
    replicaCount: 5
    dbPool: 18
    cache:
      idsMaxSize: 11000
    resources:
      limits:
        cpu: 5
  ```

  注：在 [README.md](README.md) 的**高级配置**部分中描述了进行这些更改的指示信息。

* 缺省配置最多支持 4,000 个边缘设备，缺省计算资源的 Chart 总计为：

  * 请求
     * 小于 5 GB 的 RAM
     * 小于 1 个 CPU
  * 限制
     * 18 GB RAM
     * 18 个 CPU


## 先决条件
{: #prereq}

* 安装 [{{site.data.keyword.edge_shared_notm}}](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/servers/install_edge.html)
* **macOS 或 Ubuntu {{site.data.keyword.linux_notm}} 主机**
* [OpenShift 客户机 CLI (oc) 4.2 ![在新选项卡中打开](../../images/icons/launch-glyph.svg "在新选项卡中打开")](https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest-4.2/)
* **jq** [下载 ![在新选项卡中打开](../../images/icons/launch-glyph.svg "在新选项卡中打开")](https://stedolan.github.io/jq/download/)
* **git**
* **docker** 1.13+
* **make**
* 以下 CLI，可以从 `https://<CLUSTER_URL_HOST>/common-nav/cli` 处的 {{site.data.keyword.mgmt_hub}} 集群安装获取

    注：您可能必须导航至以上 URL 两次，因为未经授权的访问将导航重定向到欢迎页面

  * Kubernetes CLI (**kubectl**)
  * Helm CLI (**helm**)
  * IBM Cloud Pak CLI (**cloudctl**)

注：缺省情况下，本地开发数据库将在 Chart 安装过程期间进行供应。 请参阅 [README.md](README.md) 以获取有关供应您自己的数据库的指导。 您负责备份或复原数据库。

## 安装过程
{: #process}

1. 设置 **CLUSTER_URL** 环境变量，此值可从 {{site.data.keyword.mgmt_hub}} 安装的输出获取：

    ```
    export CLUSTER_URL=<CLUSTER_URL>
    ```
    {: codeblock}

    或者，在使用 **oc login** 连接到集群后，您可以运行：

    ```
    export CLUSTER_URL=https://$(oc get routes icp-console -o jsonpath='{.spec.host}' -n kube-system)
    ```
    {: codeblock}

2. 使用集群管理员特权连接到集群，选择 **kubbe-system** 作为名称空间，填写 {{site.data.keyword.mgmt_hub}} 安装期间在 config.yaml 中定义的**密码**：

    ```
    cloudctl login -a $CLUSTER_URL -u admin -p <your-icp-admin-password> -n kube-system --skip-ssl-validation
    ```
    {: codeblock}

3. 定义映像注册表主机，配置 Docker CLI 以信任自签名证书：

    ```
    export REGISTRY_HOST=$(oc get routes -n openshift-image-registry default-route -o jsonpath='{.spec.host}')

    ```
    {: codeblock}

   对于 macOS：

      1. 信任证书

      ```
      mkdir -p ~/.docker/certs.d/$REGISTRY_HOST && \
      echo | openssl s_client -showcerts -connect $REGISTRY_HOST:443 2>/dev/null | openssl x509 -outform PEM > ~/.docker/certs.d/$REGISTRY_HOST/ca.crt && \
      sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain ~/.docker/certs.d/$REGISTRY_HOST/ca.crt

      ```
      {: codeblock}
      
      2. 从菜单栏重新启动 Docker 服务

   对于 Ubuntu：

      1. 信任证书

      ```
      mkdir /etc/docker/certs.d/$REGISTRY_HOST && \
      echo | openssl s_client -showcerts -connect $REGISTRY_HOST:443 2>/dev/null | openssl x509 -outform PEM > /etc/docker/certs.d/$REGISTRY_HOST/ca.crt && \
      service docker restart

      ```
      {: codeblock}

4. 登录到 {{site.data.keyword.open_shift_cp}} 映像注册表：

      ```
      docker login $REGISTRY_HOST -u $(oc whoami) -p $(oc whoami -t)
      ```
      {: codeblock}

5. 解压缩从 IBM Passport Advantage 下载的 {{site.data.keyword.edge_devices_notm}} 安装压缩文件：

    ```
    tar -zxvf ibm-ecm-4.1.0-x86_64.tar.gz && \
    cd ibm-ecm-4.1.0-x86_64
    ```
    {: codeblock}

6. 将归档内容装入到目录中，将映像装入到注册表的 ibmcom 名称空间中：

    ```
    cloudctl catalog load-archive --archive ibm-ecm-prod-catalog-archive-4.1.0.tgz --registry $REGISTRY_HOST/ibmcom
    ```
    {: codeblock}

  注：{{site.data.keyword.edge_devices_notm}} 仅支持 CLI 驱动的安装；此发行版不支持从目录进行安装。

7. 将 Chart 压缩文件内容解压缩到当前目录，并移至创建的目录中：

    ```
    tar -O -zxvf ibm-ecm-prod-catalog-archive-4.1.0.tgz charts/ibm-ecm-prod-4.1.0.tgz | tar -zxvf - && \
    cd ibm-ecm-prod
    ```
    {: codeblock}

8. 如果未设置缺省存储类，请进行定义：

   ```
   # oc get storageclass
   NAME                                 PROVISIONER                     AGE
   rook-ceph-block-internal             rook-ceph.rbd.csi.ceph.com      8h
   rook-ceph-cephfs-internal (default)  rook-ceph.cephfs.csi.ceph.com   8h
   rook-ceph-delete-bucket-internal     ceph.rook.io/bucket             8h
   ```
   
   如果未显示带以上 **(default)** 字符串的行，请使用以下内容标记首选缺省存储器：

   ```
   oc patch storageclass <PREFERRED_DEFAULT_STORAGE_CLASS_NAME> -p '{"metadata": {"annotations": {"storageclass.kubernetes.io/is-default-class": "true"}}}'
   ```
   {: codeblock}

9. 阅读并考虑配置选项，然后遵循 [README.md](README.md) 中的**安装 Chart**部分执行操作。

  此脚本安装以上**安装摘要**部分中提到的管理中心组件，运行安装验证，然后将您带回以下**安装后配置**部分。

## 安装后的配置
{: #postconfig}

在运行初始安装的主机上，运行以下命令：

1. 请参阅以上**安装过程**部分中的步骤 1 和 2 以登录到集群
2. 使用 Ubuntu {{site.data.keyword.linux_notm}} 或 macOS 软件包安装程序安装 **hzn** CLI，可以在以上[安装过程](#process)的步骤 5 中抽取的压缩内容的相应 OS/ARCH 目录中的 **horizon-edge-packages** 下找到这些安装程序：
  * Ubuntu {{site.data.keyword.linux_notm}} 示例：

    ```
    sudo dpkg -i horizon-edge-packages/linux/ubuntu/bionic/amd64/horizon-cli*.deb
    ```
    {: codeblock}

  * macOS 示例：

    ```
    sudo installer -pkg horizon-edge-packages/macos/horizon-cli-*.pkg -target /
    ```
    {: codeblock}

3. 导出后续步骤所需的下列变量：

    ```
    export EXCHANGE_ROOT_PASS=$(oc -n kube-system get secret edge-computing -o jsonpath="{.data.exchange-config}" | base64 --decode | jq -r .api.root.password)
    export HZN_EXCHANGE_URL=https://$(oc get routes icp-console -o jsonpath='{.spec.host}' -n kube-system)/ec-exchange/v1
    export HZN_EXCHANGE_USER_AUTH="root/root:$EXCHANGE_ROOT_PASS"
    export HZN_ORG_ID=IBM
    ```
    {: codeblock}

4. 信任 {{site.data.keyword.open_shift_cp}} 认证中心：
    ```
    oc --namespace kube-system get secret cluster-ca-cert -o jsonpath="{.data['tls\.crt']}" | base64 --decode > /tmp/icp-ca.crt
    ```
    {: codeblock}

  * Ubuntu {{site.data.keyword.linux_notm}} 示例：
     ```
     sudo cp /tmp/icp-ca.crt /usr/local/share/ca-certificates &&sudo update-ca-certificates
     ```
    {: codeblock}

  * macOS 示例：

    ```
    sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain /tmp/icp-ca.crt
    ```
    {: codeblock}

5. 要创建签名密钥对。 有关更多信息，请参阅[准备创建边缘服务](../developing/service_containers.md)中的步骤 5。
    ```
    hzn key create <company-name> <owner@email>
    ```
    {: codeblock}

6. 要确认安装程序可以与 {{site.data.keyword.edge_devices_notm}} Exchange API 通信：
    ```
    hzn exchange status
    ```
    {: codeblock}

7. 填充样本边缘服务：

    ```
    curl https://raw.githubusercontent.com/open-horizon/examples/v4.1/tools/exchangePublishScript.sh | bash -s -- -c $(oc get -n kube-public configmap -o jsonpath="{.items[]..data.cluster_name}")
    ```
    {: codeblock}

8. 运行以下命令，以查看在 {{site.data.keyword.edge_devices_notm}} Exchange 中创建的部分服务和策略：

    ```
    hzn exchange service list IBM/
    hzn exchange pattern list IBM/
    hzn exchange service listpolicy
    ```
    {: codeblock}

9. 如果尚未设置，请使用 {{site.data.keyword.open_shift_cp}} 管理控制台创建 LDAP 连接。 建立 LDAP 连接后，请创建一个团队，授权该团队访问任何名称空间，并将用户添加到该团队。 这会将创建 API 密钥的许可权授予各个用户。

  注：API 密钥用于向 {{site.data.keyword.edge_devices_notm}} CLI 进行认证。 有关 LDAP 的更多信息，请参阅[配置 LDAP 连接 ![在新选项卡中打开](../../images/icons/launch-glyph.svg "在新选项卡中打开")](https://www.ibm.com/support/knowledgecenter/SSFC4F_1.2.0/iam/3.4.0/configure_ldap.html)。


## 为边缘设备收集必要的信息和文件
{: #prereq_horizon}

在边缘设备上安装 {{site.data.keyword.edge_devices_notm}} 代理程序并将其向 {{site.data.keyword.edge_devices_notm}} 注册，将需要几个文件。 此部分将引导您将这些文件收集到 tar 文件中，然后可以在每个边缘设备上使用这些文件。

假定您已安装 **cloudctl** 和 **kubectl** 命令，并从安装内容中抽取了 **ibm-edge-computing-4.1.0-x86_64.tar.gz**，如本页面中先前部分所述。

1. 请参阅上面的**安装过程**部分中的步骤 1 和 2 ，以设置以下环境变量：

   ```
   export CLUSTER_URL=<cluster-url>
   export CLUSTER_USER=<your-icp-admin-user>
   export CLUSTER_PW=<your-icp-admin-password>
   ```
   {: codeblock}

2. 下载最新版本的 **edgeDeviceFiles.sh**：

   ```
   curl -O https://raw.githubusercontent.com/open-horizon/examples/v4.0/tools/edgeDeviceFiles.sh
   chmod +x edgeDeviceFiles.sh
   ```
   {: codeblock}

3. 运行 **edgeDeviceFiles.sh** 脚本以收集必要的文件：

   ```
   ./edgeDeviceFiles.sh <edge-device-type> -t
   ```
   {: codeblock}

   命令自变量：
   * 支持的 **<edge-device-type>** 值：**32-bit-ARM**、**64-bit-ARM**、**x86_64-{{site.data.keyword.linux_notm}}** 或 **{{site.data.keyword.macOS_notm}}**
   * **-t**：创建包含所有收集的文件的 **agentInstallFiles-&lt;edge-device-type&gt;.tar.gz** 文件。 如果未设置此标志，那么收集的文件将放置在当前目录中。
   * **-k**：创建名为 **$USER-Edge-Device-API-Key** 的新 API 密钥。 如果未设置此标志，那么将检查现有 API 密钥是否存在名为 **$USER-Edge-Device-API-Key** 的密钥，如果已存在此密钥，那么会跳过创建。
   * **-d** **<distribution>**：在 **64-bit-ARM** 或 **x86_64-Linux** 上安装时，您可以为较旧版本的 Ubuntu 指定 **-d xenial** 而不是使用缺省值 bionic。 在 **32-bit-ARM** 上安装时，可以指定 **-d stretch** 代替缺省值 buster。 使用 macOS 时，将忽略 -d 标志。
   * **-f** **<directory>**：指定要将收集文件移动到的目录。 如果该目录不存在，那么将创建该目录。 缺省值是当前目录

4. 先前步骤中的命令将创建名为 **agentInstallFiles-&lt;edge-device-type&gt;.tar.gz** 的文件。 如果您具有其他类型的边缘设备（不同体系结构），请针对每种类型重复先前步骤。

5. 记录通过 **edgeDeviceFiles.sh** 命令创建并显示的 API 密钥。

6. 现在您已通过 **cloudctl** 登录，如果需要为用户创建要与 {{site.data.keyword.horizon}} **hzn** 命令一起使用的其他 API 密钥，请执行以下命令：

   ```
   cloudctl iam api-key-create "<choose-an-api-key-name>" -d "<choose-an-api-key-description>"
   ```
   {: codeblock}

   在命令输出中，请在以 **API Key** 开头的行中查找密钥值，并保存密钥值以供将来使用。

7. 准备好设置边缘设备时，请遵循[开始使用 {{site.data.keyword.edge_devices_notm}}](../getting_started/getting_started.md)。

## 卸载
{: #uninstall}

注：缺省情况下，已配置**本地数据库**，在此情况下，卸载将删除所有持久数据。 在运行卸载脚本之前，请确保您已备份所有必需的持久数据（在 README 中记录了备份指示信息）。 如果已配置**远程数据库**，那么不会在卸载时删除该数据，必须在需要时手动移除。

返回到安装过程中解压缩的 Chart 的位置，并运行提供的卸载脚本。 此脚本将卸载 helm 发行版和所有关联的资源。 首先，以集群管理员身份，使用 **cloudctl** 登录集群，然后运行：

```
ibm_cloud_pak/pak_extensions/uninstall/uninstall-edge-computing.sh <cluster-name>
```
{: codeblock}
