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

# 共通サービスのインストール

## 前提条件
{: #prereq}

### {{site.data.keyword.ocp_tm}}
[適切なサイズ](cluster_sizing.md)のサポートされている {{site.data.keyword.open_shift_cp}} インストール済み環境があることを確認します。 クラスターにインストールされ、作動しているレジストリーおよびストレージ・サービスも必要です。 {{site.data.keyword.open_shift_cp}} のインストールについて詳しくは、以下のサポートされるバージョンの {{site.data.keyword.open_shift}} 資料を参照してください。

* [{{site.data.keyword.open_shift_cp}} 4.3 の資料 ![新しいタブで開く](../images/icons/launch-glyph.svg "新しいタブで開く")](https://www.ibm.com/links?url=https%3A%2F%2Fdocs.openshift.com%2Fcontainer-platform%2F4.3%2Fwelcome%2Findex.html)
* [{{site.data.keyword.open_shift_cp}} 4.4 の資料 ![新しいタブで開く](../images/icons/launch-glyph.svg "新しいタブで開く")](https://www.ibm.com/links?url=https%3A%2F%2Fdocs.openshift.com%2Fcontainer-platform%2F4.4%2Fwelcome%2Findex.html)

### その他の前提条件

* Docker 1.13+
* [{{site.data.keyword.open_shift}} client CLI (oc) 4.4 ![新しいタブで開く](../images/icons/launch-glyph.svg "新しいタブで開く")](https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest-4.4/)

## インストール・プロセス

1. インストール環境に[必要なパッケージを IBM パスポート・アドバンテージからダウンロード](part_numbers.md)し、インストール・メディアを解凍します。
    ```
    tar -zxvf ibm-eam-{{site.data.keyword.semver}}-x86_64.tar.gz
    cd ibm-eam-{{site.data.keyword.semver}}-x86_64
    ```
    {: codeblock}

2. インストールで使用するディレクトリーを準備し、インストールの一部として受け入れるライセンス zip ファイルをコピーします。

    ```
    mkdir -p /opt/common-services-3.2.7/ibm-eam-{{site.data.keyword.semver}}-licenses && \
    cp ibm-eam-{{site.data.keyword.semver}}-licenses.zip /opt/common-services-3.2.7/ibm-eam-{{site.data.keyword.semver}}-licenses
    ```
    {: codeblock}

3. Docker サービスが実行中であることを確認し、インストール tarball から Docker イメージをアンパック/ロードします。

    ```
    systemctl enable docker
    systemctl start docker
    tar -zvxf common-services-boeblingen-2004-x86_64.tar.gz -O | sudo docker load
    ```
    {: codeblock}

    **注:** いくつかのイメージを解凍するため、出力が表示されるまでに数分かかることがあります。

4. インストール構成のための準備を行い、解凍します。

    ```
    cd /opt/common-services-3.2.7 && \
    sudo docker run --rm -v $(pwd):/data:z -e LICENSE=accept -v $(pwd)/ibm-eam-{{site.data.keyword.semver}}-licenses:/installer/cfc-files/license:z --security-opt label:disable ibmcom/icp-inception-amd64:3.2.7 cp -r cluster /data
    ```
    {: codeblock}

5. 新規の KUBECONFIG ロケーションを設定し、以下の **oc login** コマンドに**適切なクラスター情報を入力**し ({{site.data.keyword.open_shift}} クラスター・インストールから取得)、**$KUBECONFIG** ファイルをインストール構成ディレクトリーにコピーします。

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

6. config.yaml ファイルを更新します。

   * {{site.data.keyword.common_services}}をどのノードでスケジュールされるように構成するのかを判別します。**マスター**・ノードの使用は避けてください。

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

     cluster/config.yaml 内部 (ここでは、**master** は {{site.data.keyword.common_services}} の一部である特定のサービス・セットを指し、**master** ノード役割を指すものでは**ありません**):

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

   * 動的ストレージを利用するための永続データの **storage_class** を選択します。

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

     [サポートされる動的 {{site.data.keyword.open_shift}} ストレージのオプションおよび構成手順 ![新しいタブで開く](../images/icons/launch-glyph.svg "新しいタブで開く")](https://docs.openshift.com/container-platform/4.4/storage/understanding-persistent-storage.html) を参照してください。

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

     注: この定義がない場合、デフォルトの **mycluster** 名が選択されます。 これはクラスターに適切な名前を付けるための重要なステップです。**cluster_name** は {{site.data.keyword.edge_notm}} のいくつかのコンポーネントを定義するために使用されるためです。

7. 内部 {{site.data.keyword.open_shift}} イメージ・レジストリーへのデフォルト・ルートを開きます。

    ```
    oc patch configs.imageregistry.operator.openshift.io/cluster --type merge -p '{"spec":{"defaultRoute":true}}'
    ```
    {: codeblock}

8. {{site.data.keyword.common_services}} をインストールします。

    ```
    sudo docker run -t --net=host -e LICENSE=accept -v $(pwd)/../ibm-eam-{{site.data.keyword.semver}}-licenses:/installer/cfc-files/license:z -v $(pwd):/installer/cluster:z -v /var/run:/var/run:z -v /etc/docker:/etc/docker:z --security-opt label:disable ibmcom/icp-inception-amd64:3.2.7 install-with-openshift
    ```
    {: codeblock}
    **注:** インストール時間はネットワーク速度によって異なり、「イメージのロード」タスク中にしばらくの間は出力が表示されないことが予期されます。

インストール出力から URL をメモします。これは、[{{site.data.keyword.ieam}} のインストール](offline_installation.md)の次のステップで必要になります。
