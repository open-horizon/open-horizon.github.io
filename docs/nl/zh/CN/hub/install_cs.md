---

copyright:
years: 2020
lastupdated: "2020-06-03"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 安装公共服务

## 先决条件
{: #prereq}

### {{site.data.keyword.ocp_tm}}
确保您拥有[设置了适当大小](cluster_sizing.md)并且受支持的 {{site.data.keyword.open_shift_cp}} 安装。 包含集群中已安装并在正常运作的注册表和存储服务。 有关安装 {{site.data.keyword.open_shift_cp}} 的更多信息，请参阅下面的 {{site.data.keyword.open_shift}} 文档以了解受支持的版本：

* [{{site.data.keyword.open_shift_cp}} 4.3 文档 ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://www.ibm.com/links?url=https%3A%2F%2Fdocs.openshift.com%2Fcontainer-platform%2F4.3%2Fwelcome%2Findex.html)
* [{{site.data.keyword.open_shift_cp}} 4.4 文档 ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://www.ibm.com/links?url=https%3A%2F%2Fdocs.openshift.com%2Fcontainer-platform%2F4.4%2Fwelcome%2Findex.html)

### 其他先决条件

* Docker 1.13+
* [{{site.data.keyword.open_shift}} 客户机 CLI (oc) 4.4 ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest-4.4/)

## 安装过程

1. [从 IBM Passport Advantage 下载所需的软件包](part_numbers.md)到您的安装环境并解包安装介质：
    ```
    tar -zxvf ibm-eam-{{site.data.keyword.semver}}-x86_64.tar.gz
    cd ibm-eam-{{site.data.keyword.semver}}-x86_64
    ```
    {: codeblock}

2. 准备安装要使用的目录，并复制将作为安装一部分接受的许可证 zip 文件：

    ```
    mkdir -p /opt/common-services-3.2.7/ibm-eam-{{site.data.keyword.semver}}-licenses && \
    cp ibm-eam-{{site.data.keyword.semver}}-licenses.zip /opt/common-services-3.2.7/ibm-eam-{{site.data.keyword.semver}}-licenses
    ```
    {: codeblock}

3. 确保 Docker 服务正在运行并从安装 tarball 解压缩/装入 Docker 映像：

    ```
    systemctl enable docker
    systemctl start docker
    tar -zvxf common-services-boeblingen-2004-x86_64.tar.gz -O | sudo docker load
    ```
    {: codeblock}

    **注：**这可能需要几分钟时间，然后才会显示输出，因为要解包几个映像

4. 准备并抽取安装配置：

    ```
    cd /opt/common-services-3.2.7 && \
    sudo docker run --rm -v $(pwd):/data:z -e LICENSE=accept -v $(pwd)/ibm-eam-{{site.data.keyword.semver}}-licenses:/installer/cfc-files/license:z --security-opt label:disable ibmcom/icp-inception-amd64:3.2.7 cp -r cluster /data
    ```
    {: codeblock}

5. 设置新的 KUBECONFIG 位置，并在以下 **oc login** 命令（从 {{site.data.keyword.open_shift}} 集群安装获取）中**填写相应集群信息**，然后将 **$KUBECONFIG** 文件复制到安装配置目录：

    ```
    export KUBECONFIG=$(pwd)/myclusterconfig
    ```
    {: codeblock}

    ```
    oc login https://<API_ENDPOINT_HOST>:<PORT> -u <ADMIN_USER> -p <ADMIN_PASSWORD> --insecure-skip-tls-verify=true && \
    cp $KUBECONFIG $(pwd)/cluster/kubeconfig && \
    cd cluster
    ```
    {: codeblock}

6. 更新 config.yaml 文件：

   * 确定要将 {{site.data.keyword.common_services}} 配置为在其上调度的节点，避免使用**主**节点：

     ```
     # oc get nodes
     NAME               STATUS   ROLES    AGE  VERSION
     master0.test.com   Ready    master   8h   v1.17.1
     master1.test.com   Ready    master   8h   v1.17.1
     master2.test.com   Ready    master   8h   v1.17.1
     worker0.test.com   Ready    worker   8h   v1.17.1
     worker1.test.com   Ready    worker   8h   v1.17.1
     worker2.test.com   Ready    worker   8h   v1.17.1
    ```

     在 cluster/config.yaml 中（此处 **master** 指属于 {{site.data.keyword.common_services}} 的一组特定服务，**不**指 **master** 节点角色）：

     ```
     # A list of OpenShift nodes that used to run services components
     cluster_nodes:
       master:
         - worker0.test.com
       proxy:
         - worker0.test.com
       management:
         - worker0.test.com
     ```
     注：主参数、代理参数和管理参数的值是一个数组，可以具有多个节点，并且可以将同一个节点用于每个参数。 以上配置用于**最小****生产**安装，针对每个参数包含三个工作程序节点。

   * 针对持久数据选择首选 **storage_class** 以利用动态存储器：

     ```
     # oc get storageclass
     NAME                               PROVISIONER                     AGE
     rook-ceph-block-internal           rook-ceph.rbd.csi.ceph.com      8h
     rook-ceph-cephfs-internal          rook-ceph.cephfs.csi.ceph.com   8h
     rook-ceph-delete-bucket-internal   ceph.rook.io/bucket             8h
     ```

     在 cluster/config.yaml 中：

     ```
     # Storage Class
storage_class: rook-ceph-cephfs-internal
     ```

     请参阅以下内容以了解[受支持的动态 {{site.data.keyword.open_shift}} 存储选项和配置指示信息 ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开 ")](https://docs.openshift.com/container-platform/4.4/storage/understanding-persistent-storage.html)

   * 定义超过 32 个字符的字母数字 **default_admin_password**：

     ```
     # default_admin_password:
     # password_rules:
     #   - '^([a-zA-Z0-9\-]{32,})$'
     default_admin_password: <YOUR-32-CHARACTER-OR-LONGER-ADMIN-PASSWORD>
     ```

   * 添加一行以定义 **cluster_name** 来唯一标识集群：

     ```
     cluster_name: <INSERT_YOUR_UNIQUE_CLUSTER_NAME>
     ```

     注：如果没有此定义，那么将选择缺省值 **mycluster**。 这是对集群正确命名的重要步骤，因为 **cluster_name** 将用于为 {{site.data.keyword.edge_notm}} 定义几个组件

7. 打开到内部 {{site.data.keyword.open_shift}} 映像注册表的缺省路由：

    ```
    oc patch configs.imageregistry.operator.openshift.io/cluster --type merge -p '{"spec":{"defaultRoute":true}}'
    ```
    {: codeblock}

8. 安装 {{site.data.keyword.common_services}}

    ```
    sudo docker run -t --net=host -e LICENSE=accept -v $(pwd)/../ibm-eam-{{site.data.keyword.semver}}-licenses:/installer/cfc-files/license:z -v $(pwd):/installer/cluster:z -v /var/run:/var/run:z -v /etc/docker:/etc/docker:z --security-opt label:disable ibmcom/icp-inception-amd64:3.2.7 install-with-openshift
    ```
    {: codeblock}
    **注：**安装时间将根据网络速度而变化，预计在“装入映像”任务期间需要过一段时间才会显示输出。

请记录安装输出中的 URL，在[安装 {{site.data.keyword.ieam}}](offline_installation.md) 的下一步中需要使用此 URL。
