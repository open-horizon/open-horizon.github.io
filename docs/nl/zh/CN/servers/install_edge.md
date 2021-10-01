---

copyright:
  years: 2019, 2020
lastupdated: "2020-02-13"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 将 CP4MCM 与 IEAM 配合使用
{: #using_cp4mcm}

遵循以下安装步骤以配置并启用 {{site.data.keyword.edge_shared_notm}}。 此安装支持 {{site.data.keyword.edge_servers_notm}} 和 {{site.data.keyword.edge_devices_notm}}。
{:shortdesc}

## 先决条件
{: #prereq}

确保您已[适当调整](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/servers/cluster_sizing.html) {{site.data.keyword.icp_server_notm}} 的集群。

* Docker 1.13+
* [OpenShift 客户机 CLI (oc) 4.2 ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest-4.2/)

## 安装过程

1. 根据购买的产品，将适用于 {{site.data.keyword.edge_servers_notm}} 或 {{site.data.keyword.edge_devices_notm}} 的 **ibm-cp4mcm-core** 和 **ibm-ecm** 捆绑软件从 IBM Passport Advantage 下载到安装环境。

2. 准备安装要使用的目录，并解压缩将作为安装一部分接受的许可证 zip 文件：

    ```
    mkdir -p /opt/ibm-multicloud-manager-1.2 && \
    tar -C /opt/ibm-multicloud-manager-1.2 -zxvf ibm-ecm-4.0.0-x86_64.tar.gz ibm-ecm-4.0.0-x86_64/ibm-ecm-licenses-4.0.zip
    ```
    {: codeblock}

3. 确保 Docker 服务正在运行并从安装 tarball 解压缩/装入 Docker 映像：

    ```
    tar -zvxf ibm-cp4mcm-core-1.2-x86_64.tar.gz -O | sudo docker load
    ```
    {: codeblock}

4. 准备并抽取安装配置：

    ```
    cd /opt/ibm-multicloud-manager-1.2 && \
    sudo docker run --rm -v $(pwd):/data:z -e LICENSE=accept -v $(pwd)/ibm-ecm-4.0.0-x86_64:/installer/cfc-files/license:z --security-opt label:disable ibmcom/mcm-inception-amd64:3.2.3 cp -r cluster /data
    ```
    {: codeblock}

5. 指定新的 KUBECONFIG 位置，并在以下 **oc login** 命令（从 OpenShift 集群安装获取）中**填写相应集群信息**，然后将**$KUBECONFIG** 文件复制到安装配置目录：

    ```
    export KUBECONFIG=$(pwd)/myclusterconfig
    ```
    {: codeblock}

    ```
    oc login https://<API_ENDPOINT_HOST>:<PORT> -u <ADMIN_USER> -p <ADMIN_PASSWORD> --insecure-skip-tls-verify=true && \
    cp $KUBECONFIG /opt/ibm-multicloud-manager-1.2/cluster/kubeconfig && \
    cd cluster
    ```
    {: codeblock}

6. 更新 config.yaml 文件：

  * 确定要将 {{site.data.keyword.edge_shared_notm}} 服务配置为要在其上调度的节点。 强烈建议您避免使用 **master** 节点：

     ```
     # oc get nodes
     NAME               STATUS   ROLES    AGE  VERSION
     master0.test.com   Ready    master   8h   v1.14.6+c07e432da
     master1.test.com   Ready    master   8h   v1.14.6+c07e432da
     master2.test.com   Ready    master   8h   v1.14.6+c07e432da
     worker0.test.com   Ready    worker   8h   v1.14.6+c07e432da
     worker1.test.com   Ready    worker   8h   v1.14.6+c07e432da
     worker2.test.com   Ready    worker   8h   v1.14.6+c07e432da
     ```

     在 cluster/config.yaml 中（此处 **master** 指属于 {{site.data.keyword.edge_servers_notm}} 的一组特定服务，**不**指 **master** 节点角色）：

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

   * 针对持久数据选择首选 **storage_class**：

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

     注：如果没有此定义，那么将选择缺省值 **mycluster**。 如果您还将安装 {{site.data.keyword.edge_devices_notm}}，那么这是正确命名集群的重要步骤。 **cluster_name** 将用于定义该产品的多个组件。

7. 打开到内部 OpenShift 映像注册表的缺省路由：

    ```
    oc patch configs.imageregistry.operator.openshift.io/cluster --type merge -p '{"spec":{"defaultRoute":true}}'
    ```
    {: codeblock}

8. 安装 {{site.data.keyword.edge_shared_notm}}：

    ```
    sudo docker run -t --net=host -e LICENSE=accept -v $(pwd)/../ibm-ecm-4.0.0-x86_64:/installer/cfc-files/license:z -v $(pwd):/installer/cluster:z -v /var/run:/var/run:z -v /etc/docker:/etc/docker:z --security-opt label:disable ibmcom/mcm-inception-amd64:3.2.3 install-with-openshift
    ```
    {: codeblock}

<!--## Importing a cluster to be managed
There is a known issue with importing clusters, we are working on providing functional documentation steps for this process.

## Next steps
If this installation was done as part of a prerequisite for {{site.data.keyword.edge_devices_notm}}, [return to continue that installation](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/devices/installing/install.html).-->
