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

# 管理ハブのインストール
{: #hub_install_overview}
 
{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) ノードのタスクに進む前に、管理ハブをインストールして構成する必要があります。

{{site.data.keyword.ieam}} が提供するエッジ・コンピューティング機能は、ハブ・クラスターから OpenShift® Container Platform 4.2 またはその他の Kubernetes ベース・クラスターのリモート・インスタンスへのワークロードの管理とデプロイに役立ちます。

{{site.data.keyword.ieam}} は、IBM Multicloud Management Core 1.2 を使用して、エッジ・サーバー、ゲートウェイ、およびリモート・ロケーションの OpenShift® Container Platform 4.2 クラスターによってホストされるデバイスに対する、コンテナー化されたワークロードのデプロイメントを制御します。

さらに、{{site.data.keyword.ieam}} には、edge computing manager プロファイルのサポートも含まれています。 このサポートされるプロファイルを使用すると、リモート・エッジ・サーバーのホスティングに使用するために OpenShift® Container Platform 4.2 をインストールした場合、OpenShift® Container Platform 4.2 のリソース使用量を減らすことができます。 このプロファイルは、これらのサーバー環境の堅牢なリモート管理、およびそこでホスティングしている企業の基幹業務アプリケーションをサポートするために必要な最小限のサービスを配置します。 このプロファイルを使用して、ユーザーを認証し、ログとイベント・データを収集し、単一のノードまたは一連のクラスター・ワーカー・ノードにワークロードをデプロイすることができます。

# 管理ハブのインストール

{{site.data.keyword.edge_notm}} のインストール・プロセスでは、以下の大まかなインストールと構成のステップを行います。
{:shortdesc}

  - [インストールの要約](#sum)
  - [サイジング](#size)
  - [前提条件](#prereq)
  - [インストール・プロセス](#process)
  - [インストール後の構成](#postconfig)
  - [必要な情報とファイルの収集](#prereq_horizon)
  - [アンインストール](#uninstall)

## インストールの要約
{: #sum}

* 以下の管理ハブ・コンポーネントをデプロイします。
  * {{site.data.keyword.edge_devices_notm}} Exchange API。
  * {{site.data.keyword.edge_devices_notm}} agbot。
  * {{site.data.keyword.edge_devices_notm}} Cloud Sync Service (CSS)。
  * {{site.data.keyword.edge_devices_notm}} ユーザー・インターフェース。
* インストールが正常に行われたことを確認します。
* サンプル・エッジ・サービスを取り込みます。

## サイジング
{: #size}

このサイジング情報は {{site.data.keyword.edge_notm}} サービスのみが対象であり、{{site.data.keyword.edge_shared_notm}}のサイジング推奨事項 ([この資料](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/servers/cluster_sizing.html)を参照) 以上のものです。

### データベース・ストレージ要件

* PostgreSQL Exchange
  * 10 GB デフォルト
* PostgreSQL AgBot
  * 10 GB デフォルト  
* MongoDB Cloud Sync Service
  * 50 GB デフォルト

### コンピュート要件

[Kubernetes コンピュート・リソース](https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container)を利用するサービスは、使用可能なワーカー・ノードすべてにわたってスケジュールされます。 少なくとも 3 つのワーカー・ノードが推奨されます。

* 以下の構成変更は、最大 10,000 個のエッジ・デバイスをサポートします。

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

  注: これらの変更を行う手順は、[README.md](README.md) の『**拡張構成**』セクションに記述されています。

* デフォルト構成は、最大 4,000 個のエッジ・デバイスをサポートします。デフォルトのコンピュート・リソースのチャート合計は次のとおりです。

  * 要求
     * 5 GB 未満の RAM
     * 1 CPU 未満
  * 限度
     * 18 GB の RAM
     * 18 CPU


## 前提条件
{: #prereq}

* [{{site.data.keyword.edge_shared_notm}}](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/servers/install_edge.html) のインストール
* **macOS または Ubuntu {{site.data.keyword.linux_notm}} ホスト**
* [OpenShift client CLI (oc) 4.2 ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest-4.2/)
* **jq** [ダウンロード ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://stedolan.github.io/jq/download/)
* **git**
* **docker** 1.13+
* **make**
* 以下の CLI (`https://<CLUSTER_URL_HOST>/common-nav/cli` で {{site.data.keyword.mgmt_hub}} クラスター・インストールから取得可能)

    注: 非認証アクセスによってナビゲーションがウェルカム・ページにリダイレクトされるために、上記の URL に 2 回ナビゲートすることが必要な場合があります。

  * Kubernetes CLI (**kubectl**)
  * Helm CLI (**helm**)
  * IBM Cloud Pak CLI (**cloudctl**)

注: デフォルトでは、チャートのインストールの一部としてローカル開発データベースがプロビジョンされます。 独自のデータベースのプロビジョンに関するガイドについては、[README.md](README.md) を参照してください。 データベースのバックアップまたはリストアは、お客様の責任で行ってください。

## インストール・プロセス
{: #process}

1. **CLUSTER_URL** 環境変数を設定します。この値は、{{site.data.keyword.mgmt_hub}} のインストール出力から取得できます。

    ```
    export CLUSTER_URL=<CLUSTER_URL>
    ```
    {: codeblock}

    あるいは、**oc login** を使用してクラスターに接続した後、以下を実行することもできます。

    ```
    export CLUSTER_URL=https://$(oc get routes icp-console -o jsonpath='{.spec.host}' -n kube-system)
    ```
    {: codeblock}

2. クラスター管理者特権でクラスターに接続します。その際、名前空間として **kube-system** を選択し、{{site.data.keyword.mgmt_hub}} のインストール時に config.yaml 内に定義した**パスワードを入力**します。

    ```
    cloudctl login -a $CLUSTER_URL -u admin -p <your-icp-admin-password> -n kube-system --skip-ssl-validation
    ```
    {: codeblock}

3. イメージ・レジストリー・ホストを定義して、自己署名証明書を信頼するように Docker CLI を構成します。

    ```
    export REGISTRY_HOST=$(oc get routes -n openshift-image-registry default-route -o jsonpath='{.spec.host}')

    ```
    {: codeblock}

   macOS の場合:

      1. 証明書を信頼します

      ```
      mkdir -p ~/.docker/certs.d/$REGISTRY_HOST && \
      echo | openssl s_client -showcerts -connect $REGISTRY_HOST:443 2>/dev/null | openssl x509 -outform PEM > ~/.docker/certs.d/$REGISTRY_HOST/ca.crt && \
      sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain ~/.docker/certs.d/$REGISTRY_HOST/ca.crt

      ```
      {: codeblock}
      
      2. メニュー・バーでの Docker サービスの再始動

   Ubuntu の場合:

      1. 証明書を信頼します

      ```
      mkdir /etc/docker/certs.d/$REGISTRY_HOST && \
      echo | openssl s_client -showcerts -connect $REGISTRY_HOST:443 2>/dev/null | openssl x509 -outform PEM > /etc/docker/certs.d/$REGISTRY_HOST/ca.crt && \
      service docker restart

      ```
      {: codeblock}

4. {{site.data.keyword.open_shift_cp}} イメージ・レジストリーにログインします。

      ```
      docker login $REGISTRY_HOST -u $(oc whoami) -p $(oc whoami -t)
      ```
      {: codeblock}

5. IBM パスポート・アドバンテージからダウンロードした {{site.data.keyword.edge_devices_notm}} インストールの圧縮ファイルを解凍します。

    ```
    tar -zxvf ibm-ecm-4.1.0-x86_64.tar.gz && \
    cd ibm-ecm-4.1.0-x86_64
    ```
    {: codeblock}

6. アーカイブ・コンテンツをカタログにロードし、イメージをレジストリーの ibmcom 名前空間にロードします。

    ```
    cloudctl catalog load-archive --archive ibm-ecm-prod-catalog-archive-4.1.0.tgz --registry $REGISTRY_HOST/ibmcom
    ```
    {: codeblock}

  注: {{site.data.keyword.edge_devices_notm}} は、CLI 駆動型のインストールのみをサポートしています。カタログからのインストールはこのリリースではサポートされていません。

7. チャートの圧縮ファイルの内容を現行ディレクトリーに抽出し、作成したディレクトリーに移動します。

    ```
    tar -O -zxvf ibm-ecm-prod-catalog-archive-4.1.0.tgz charts/ibm-ecm-prod-4.1.0.tgz | tar -zxvf - && \
    cd ibm-ecm-prod
    ```
    {: codeblock}

8. 設定されていない場合、デフォルトのストレージ・クラスを定義します。

   ```
   # oc get storageclass
   NAME                                 PROVISIONER                     AGE
   rook-ceph-block-internal             rook-ceph.rbd.csi.ceph.com      8h
   rook-ceph-cephfs-internal (default)  rook-ceph.cephfs.csi.ceph.com   8h
   rook-ceph-delete-bucket-internal     ceph.rook.io/bucket             8h
   ```
   
   上記の **(default)** ストリングのある行が表示されない場合、以下を使用して、優先するデフォルト・ストレージをタグ付けします。

   ```
   oc patch storageclass <PREFERRED_DEFAULT_STORAGE_CLASS_NAME> -p '{"metadata": {"annotations": {"storageclass.kubernetes.io/is-default-class": "true"}}}'
   ```
   {: codeblock}

9. 構成オプションを読み、検討してから、[README.md](README.md) の『**チャートのインストール**』セクションに従います。

  スクリプトは、上記の『**インストールの要約**』セクションに記述されている管理ハブ・コンポーネントをインストールし、インストール検証を実行し、その後、下の『**インストール後の構成**』セクションに戻ります。

## インストール後の構成
{: #postconfig}

初期インストールを実行したホストと同じホストで、以下のコマンドを実行します。

1. 上記の『**インストール・プロセス**』セクションのステップ 1 および 2 を参照して、クラスターにログインします。
2. **hzn** CLI を Ubuntu {{site.data.keyword.linux_notm}} または macOS パッケージ・インストーラーのいずれかを使用してインストールします。このインストーラーは、上記の [ インストール・プロセス](#process) のステップ 5 で解凍した圧縮コンテンツの該当する OS/ARCH ディレクトリー内の **horizon-edge-packages** にあります。
  * Ubuntu {{site.data.keyword.linux_notm}} の例:

    ```
    sudo dpkg -i horizon-edge-packages/linux/ubuntu/bionic/amd64/horizon-cli*.deb
    ```
    {: codeblock}

  * macOS の例:

    ```
    sudo installer -pkg horizon-edge-packages/macos/horizon-cli-*.pkg -target /
    ```
    {: codeblock}

3. 次のステップに必要な以下の変数をエクスポートします。

    ```
    export EXCHANGE_ROOT_PASS=$(oc -n kube-system get secret edge-computing -o jsonpath="{.data.exchange-config}" | base64 --decode | jq -r .api.root.password)
    export HZN_EXCHANGE_URL=https://$(oc get routes icp-console -o jsonpath='{.spec.host}' -n kube-system)/ec-exchange/v1
    export HZN_EXCHANGE_USER_AUTH="root/root:$EXCHANGE_ROOT_PASS"
    export HZN_ORG_ID=IBM
    ```
    {: codeblock}

4. {{site.data.keyword.open_shift_cp}} 認証局を信頼します。
    ```
    oc --namespace kube-system get secret cluster-ca-cert -o jsonpath="{.data['tls\.crt']}" | base64 --decode > /tmp/icp-ca.crt
    ```
    {: codeblock}

  * Ubuntu {{site.data.keyword.linux_notm}} の例:
     ```
     sudo cp /tmp/icp-ca.crt /usr/local/share/ca-certificates &&sudo update-ca-certificates
     ```
    {: codeblock}

  * macOS の例:

    ```
    sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain /tmp/icp-ca.crt
    ```
    {: codeblock}

5. 署名鍵ペアを作成します。 詳しくは、『[エッジ・サービス作成の準備](../developing/service_containers.md)』のステップ 5 を参照してください。
    ```
    hzn key create <company-name> <owner@email>
    ```
    {: codeblock}

6. セットアップしたものが {{site.data.keyword.edge_devices_notm}} Exchange API と通信できることを確認します。
    ```
    hzn exchange status
    ```
    {: codeblock}

7. サンプル・エッジ・サービスを取り込みます。

    ```
    curl https://raw.githubusercontent.com/open-horizon/examples/v4.1/tools/exchangePublishScript.sh | bash -s -- -c $(oc get -n kube-public configmap -o jsonpath="{.items[]..data.cluster_name}")
    ```
    {: codeblock}

8. 以下のコマンドを実行して、{{site.data.keyword.edge_devices_notm}} Exchange 内に作成されたサービスおよびポリシーの一部を表示します。

    ```
    hzn exchange service list IBM/
    hzn exchange pattern list IBM/
    hzn exchange service listpolicy
    ```
    {: codeblock}

9. LDAP 接続がまだセットアップされていない場合は、{{site.data.keyword.open_shift_cp}} 管理コンソールを使用して LDAP 接続を作成します。 LDAP 接続が確立されたら、チームを作成し、そのチームに任意の名前空間へのアクセス権限を付与し、ユーザーをそのチームに追加します。 これにより、個々のユーザーに API 鍵を作成するための許可が付与されます。

  注: API 鍵は、{{site.data.keyword.edge_devices_notm}} CLI での認証に使用されます。 LDAP について詳しくは、[ LDAP 接続の構成 ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://www.ibm.com/support/knowledgecenter/SSFC4F_1.2.0/iam/3.4.0/configure_ldap.html) を参照してください。


## エッジ・デバイス用の必要な情報とファイルの収集
{: #prereq_horizon}

エッジ・デバイスでの {{site.data.keyword.edge_devices_notm}} エージェントのインストールと {{site.data.keyword.edge_devices_notm}} への登録には、いくつかのファイルが必要になります。 このセクションでは、それらのファイルを収集して、各エッジ・デバイスで使用できる 1 つの tar ファイルにする方法をガイドします。

このページで前述されているように、**cloudctl** および **kubectl** コマンドが既にインストールされていて、インストール・コンテンツから **ibm-edge-computing-4.1.0-x86_64.tar.gz** が解凍されていると想定します。

1. 上記の『**インストール・プロセス**』セクションのステップ 1 および 2 を参照して、以下の環境変数を設定します。

   ```
   export CLUSTER_URL=<cluster-url>
   export CLUSTER_USER=<your-icp-admin-user>
   export CLUSTER_PW=<your-icp-admin-password>
   ```
   {: codeblock}

2. 最新バージョンの **edgeDeviceFiles.sh** をダウンロードします。

   ```
   curl -O https://raw.githubusercontent.com/open-horizon/examples/v4.0/tools/edgeDeviceFiles.sh
   chmod +x edgeDeviceFiles.sh
   ```
   {: codeblock}

3. **edgeDeviceFiles.sh** スクリプトを実行して、必要なファイルを収集します。

   ```
   ./edgeDeviceFiles.sh <edge-device-type> -t
   ```
   {: codeblock}

   コマンド引数は次のとおりです。
   * サポートされる **<edge-device-type>** 値: **32-bit-ARM**、**64-bit-ARM**、**x86_64-{{site.data.keyword.linux_notm}}**、および **{{site.data.keyword.macOS_notm}}**
   * **-t**: 収集されたすべてのファイルを含んでいる 1 つの **agentInstallFiles-&lt;edge-device-type&gt;.tar.gz** ファイルを作成します。 このフラグが設定されていない場合、収集されたファイルは現行ディレクトリーに入れられます。
   * **-k**: **$USER-Edge-Device-API-Key** という名前の新規 API 鍵を作成します。 このフラグが設定されていない場合、既存の API 鍵に **$USER-Edge-Device-API-Key** という名前のものがないか検査され、既にある場合は作成がスキップされます。
   * **-d** **<distribution>**: **64-bit-ARM** または **x86_64-Linux** にインストールする場合、デフォルトの bionic の代わりに古いバージョンの Ubuntu を示す **-d xenial** を指定できます。 **32-bit-ARM** にインストールする場合は、デフォルトの buster の代わりに **-d stretch** を指定できます。 macOS では -d フラグは無視されます。
   * **-f** **<directory>**: 収集されたファイルを移動する先のディレクトリーを指定します。 ディレクトリーが存在しない場合は作成されます。 デフォルトは現行ディレクトリーです。

4. 前のステップのコマンドによって、**agentInstallFiles-&lt;edge-device-type&gt;.tar.gz** という名前のファイルが作成されます。 追加のエッジ・デバイスのタイプ (異なるアーキテクチャー) がある場合、タイプごとに前のステップを繰り返します。

5. **edgeDeviceFiles.sh** コマンドによって作成および表示された API 鍵をメモします。

6. 現在、**cloudctl** を介してログインしている状態です。ユーザーが {{site.data.keyword.horizon}} **hzn** コマンドで使用するための追加の API 鍵を作成する必要がある場合、以下のようにします。

   ```
   cloudctl iam api-key-create "<choose-an-api-key-name>" -d "<choose-an-api-key-description>"
   ```
   {: codeblock}

   コマンドの出力で、**API Key** で始まる行の鍵の値を探し、今後の使用に備えてその値を保存します。

7. エッジ・デバイスをセットアップする準備ができたら、[{{site.data.keyword.edge_devices_notm}} 入門](../getting_started/getting_started.md)に従います。

## アンインストール
{: #uninstall}

注: デフォルトでは、**ローカル・データベース**が構成されますが、この場合はアンインストールによってすべての永続データが削除されます。 アンインストール・スクリプトを実行する前に、必要なすべての永続データのバックアップを作成したことを確認してください (バックアップ手順は README に記載されています)。 **リモート・データベース**を構成した場合、そのデータはアンインストール中には削除されず、必要な場合は手動で削除する必要があります。

インストールの一部として解凍されたチャートの場所に戻り、提供されたアンインストール・スクリプトを実行します。 このスクリプトは、helm リリースおよび関連するすべてのリソースをアンインストールします。 最初に、**cloudctl** を使用してクラスター管理者としてクラスターにログインし、次に、以下を実行します。

```
ibm_cloud_pak/pak_extensions/uninstall/uninstall-edge-computing.sh <cluster-name>
```
{: codeblock}
