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

# IEAM での CP4MCM の使用
{: #using_cp4mcm}

以下のインストール手順に従って、{{site.data.keyword.edge_shared_notm}} を構成して使用できるようにします。 このインストールは、{{site.data.keyword.edge_servers_notm}} および {{site.data.keyword.edge_devices_notm}} の両方をサポートします。
{:shortdesc}

## 前提条件
{: #prereq}

{{site.data.keyword.icp_server_notm}} 用のクラスターを[適切にサイジング](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/servers/cluster_sizing.html)したことを確認します。

* Docker 1.13+
* [OpenShift Client CLI (oc) 4.2 ![新しいタブで開く](../images/icons/launch-glyph.svg "新しいタブで開く")](https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest-4.2/)

## インストール・プロセス

1. どちらの製品が購入されたのかに応じて、{{site.data.keyword.edge_servers_notm}} または {{site.data.keyword.edge_devices_notm}} の **ibm-cp4mcm-core** および **ibm-ecm** バンドルを、IBM パスポート・アドバンテージからインストール環境にダウンロードします。

2. インストールで使用するディレクトリーを作成し、インストールの一部として受け入れるライセンス zip ファイルを解凍します。

    ```
    mkdir -p /opt/ibm-multicloud-manager-1.2 && \
    tar -C /opt/ibm-multicloud-manager-1.2 -zxvf ibm-ecm-4.0.0-x86_64.tar.gz ibm-ecm-4.0.0-x86_64/ibm-ecm-licenses-4.0.zip
    ```
    {: codeblock}

3. Docker サービスが実行中であることを確認し、インストール tarball から Docker イメージをアンパック/ロードします。

    ```
    tar -zvxf ibm-cp4mcm-core-1.2-x86_64.tar.gz -O | sudo docker load
    ```
    {: codeblock}

4. インストール構成のための準備を行い、解凍します。

    ```
    cd /opt/ibm-multicloud-manager-1.2 && \
    sudo docker run --rm -v $(pwd):/data:z -e LICENSE=accept -v $(pwd)/ibm-ecm-4.0.0-x86_64:/installer/cfc-files/license:z --security-opt label:disable ibmcom/mcm-inception-amd64:3.2.3 cp -r cluster /data
    ```
    {: codeblock}

5. 新規の KUBECONFIG ロケーションを指定し、以下の **oc login** コマンドに**適切なクラスター情報を入力**し (OpenShift クラスター・インストールから取得)、**$KUBECONFIG** ファイルをインストール構成ディレクトリーにコピーします。

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

6. config.yaml ファイルを更新します。

  * {{site.data.keyword.edge_shared_notm}} サービスをどのノードでスケジュールされるように構成するのかを判別します。 **マスター**・ノードの使用を避けることを強くお勧めします。

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

     cluster/config.yaml 内部 (ここでは、**master** は {{site.data.keyword.edge_servers_notm}} の一部である特定のサービス・セットを指し、**master** ノード役割を指すものでは**ありません**):

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
     注: master パラメーター、proxy パラメーター、および management パラメーターの値は配列であり、複数のノードを指定できます。同じノードを各パラメーターに使用できます。 上記の構成は**最小**インストール用のものであり、**実動**インストールの場合は各パラメーターに 3 つのワーカー・ノードを含めます。

   * 永続データの **storage_class** を選択します。

     ```
     # oc get storageclass
     NAME                               PROVISIONER                     AGE
     rook-ceph-block-internal           rook-ceph.rbd.csi.ceph.com      8h
     rook-ceph-cephfs-internal          rook-ceph.cephfs.csi.ceph.com   8h
     rook-ceph-delete-bucket-internal   ceph.rook.io/bucket             8h
     ```

     cluster/config.yaml の内部:

     ```
     # Storage Class
storage_class: rook-ceph-cephfs-internal
     ```

   * **default_admin_password** 32 文字以上の英数字を定義します。

     ```
     # default_admin_password:
     # password_rules:
     #   - '^([a-zA-Z0-9\-]{32,})$'
     default_admin_password: <YOUR-32-CHARACTER-OR-LONGER-ADMIN-PASSWORD>
     ```

   * クラスターを一意的に識別する **cluster_name** を定義する行を追加します。

     ```
     cluster_name: <INSERT_YOUR_UNIQUE_CLUSTER_NAME>
     ```

     注: この定義がない場合、デフォルトの **mycluster** 名が選択されます。 {{site.data.keyword.edge_devices_notm}} もインストールする場合、これはクラスターに適切な名前を付けるための重要なステップです。 その製品の複数のコンポーネントを定義するために **cluster_name** が使用されます。

7. 内部 OpenShift イメージ・レジストリーへのデフォルト・ルートを開きます。

    ```
    oc patch configs.imageregistry.operator.openshift.io/cluster --type merge -p '{"spec":{"defaultRoute":true}}'
    ```
    {: codeblock}

8. {{site.data.keyword.edge_shared_notm}} をインストールします。

    ```
    sudo docker run -t --net=host -e LICENSE=accept -v $(pwd)/../ibm-ecm-4.0.0-x86_64:/installer/cfc-files/license:z -v $(pwd):/installer/cluster:z -v /var/run:/var/run:z -v /etc/docker:/etc/docker:z --security-opt label:disable ibmcom/mcm-inception-amd64:3.2.3 install-with-openshift
    ```
    {: codeblock}

<!--## Importing a cluster to be managed
There is a known issue with importing clusters, we are working on providing functional documentation steps for this process.

## Next steps
If this installation was done as part of a prerequisite for {{site.data.keyword.edge_devices_notm}}, [return to continue that installation](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/devices/installing/install.html).-->
