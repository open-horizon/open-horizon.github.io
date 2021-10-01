---

copyright:
years: 2021
lastupdated: "2021-03-23"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# アップグレード
{: #hub_upgrade_overview}

## アップグレードの要約
{: #sum}
* {{site.data.keyword.ieam}} Management Hub の現行バージョンは {{site.data.keyword.semver}} です。
* {{site.data.keyword.ieam}} {{site.data.keyword.semver}} は {{site.data.keyword.ocp}} バージョン 4.6 でサポートされています。

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) Management Hub および [IBM Cloud Platform Common Services](https://www.ibm.com/docs/en/cpfs) の同じ Operator Lifecycle Manager (OLM) チャネルへのアップグレードは、{{site.data.keyword.open_shift_cp}} ({{site.data.keyword.ocp}}) クラスターに事前にインストールされた OLM を介して自動的に行われます。

{{site.data.keyword.ieam}} チャネルは、**マイナー・バージョン** (例えば、v4.2 および v4.3) によって定義され、**パッチ・バージョン** (例えば 4.2.x) のみ自動的に更新します。**マイナー・バージョン**のアップグレードの場合、アップグレードを開始するには手動でチャネルを変更する必要があります。**マイナー・バージョン**のアップグレードを開始するには、前の**マイナー・バージョン**の使用可能な最新の**パッチ・バージョン**になっている必要があり、そうであればチャネルの切り替えによってアップグレードが開始されます。

**注:**
* ダウングレードはサポートされていません。
* {{site.data.keyword.ieam}} 4.1.x から 4.2.x へのアップグレードはサポートされていません。
* [既知の {{site.data.keyword.ocp}} 問題](https://access.redhat.com/solutions/5493011)のため、プロジェクト内に手動承認として構成されている `InstallPlan` があると、そのプロジェクト内の他のすべての `InstallPlan` も同様になります。続行するには、オペレーターのアップグレードを手動で承認する必要があります。

### 4.2.x から 4.3.x への {{site.data.keyword.ieam}} Management Hub のアップグレード

1. アップグレードの前にバックアップを取ります。詳しくは、『[バックアップとリカバリー](../admin/backup_recovery.md)』を参照してください。
2. クラスターの {{site.data.keyword.ocp}} Web コンソールにナビゲートします。
3. **「Operators」**->**「Installed Operators」**に移動します。
4. **{{site.data.keyword.ieam}}** を検索し、**{{site.data.keyword.ieam}} Management Hub** 結果をクリックします。
5. **「Subscription」**タブにナビゲートします。
6. **「Channel」**セクションの **v4.2** リンクをクリックします。
7. アップグレードを開始するため、ラジオ・ボタンをクリックして、アクティブなチャネルを **v4.3** に切り替えます。

アップグレードが完了したことを確認するには、[インストール後の『インストールの検査』セクションのステップ 1 から 5](post_install.md) を参照してください。

サンプル・サービスを更新するには、[『インストール後の構成』セクションのステップ 1 から 3](post_install.md) を参照してください。

## エッジ・ノードのアップグレード

既存の {{site.data.keyword.ieam}} ノードは自動的にはアップグレードされません。 {{site.data.keyword.ieam}} 4.2.1 エージェントのバージョン (2.28.0-338) は {{site.data.keyword.ieam}} {{site.data.keyword.semver}} Management Hub でサポートされています。 エッジ・デバイスおよびエッジ・クラスターで {{site.data.keyword.edge_notm}} エージェントをアップグレードするには、まず、{{site.data.keyword.semver}} エッジ・ノード・ファイルをクラウド同期サービス (CSS) に配置する必要があります。

この時点でエッジ・ノードをアップグレードしたくない場合でも、『**環境への最新 CLI のインストール**』のステップ 1 から 3 を実行してください。これにより、新しいエッジ・ノードが最新の {{site.data.keyword.ieam}} {{site.data.keyword.semver}} エージェント・コードでインストールされることが確実になります。

### 環境への最新 CLI のインストール
1. [Entitled Registry](https://myibm.ibm.com/products-services/containerlibrary) を介してライセンス・キーを使用して、ログインし、エージェント・バンドルをプルし、解凍します。
    ```
    docker login cp.icr.io --username cp && \
    docker rm -f ibm-eam-{{site.data.keyword.semver}}-bundle; \
    docker create --name ibm-eam-{{site.data.keyword.semver}}-bundle cp.icr.io/cp/ieam/ibm-eam-bundle:{{site.data.keyword.anax_ver}} bash && \
    docker cp ibm-eam-{{site.data.keyword.semver}}-bundle:/ibm-eam-{{site.data.keyword.semver}}-bundle.tar.gz ibm-eam-{{site.data.keyword.semver}}-bundle.tar.gz && \
    tar -zxvf ibm-eam-{{site.data.keyword.semver}}-bundle.tar.gz
    ```
    {: codeblock}
2. サポートされるプラットフォームの手順を使用して、**hzn** CLI をインストールします。
  * **agent** ディレクトリーに移動し、エージェント・ファイルを解凍します。
    ```
    cd ibm-eam-{{site.data.keyword.semver}}-bundle/agent && \
    tar -zxvf edge-packages-{{site.data.keyword.semver}}.tar.gz
    ```
    {: codeblock}

    * Debian {{site.data.keyword.linux_notm}} の例:
      ```
      sudo apt-get install ./edge-packages-{{site.data.keyword.semver}}/linux/deb/amd64/horizon-cli*.deb
      ```
      {: codeblock}

    * Red Hat {{site.data.keyword.linux_notm}} の例:
      ```
      sudo dnf install -yq ./edge-packages-{{site.data.keyword.semver}}/linux/rpm/x86_64/horizon-cli-*.x86_64.rpm
      ```
      {: codeblock}

    * macOS の例:
      ```
      sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain edge-packages-{{site.data.keyword.semver}}/macos/pkg/x86_64/horizon-cli.crt && \
      sudo installer -pkg edge-packages-{{site.data.keyword.semver}}/macos/pkg/x86_64/horizon-cli-*.pkg -target /
      ```
      {: codeblock}
3. [エッジ・ノード・ファイルの収集](../hub/gather_files.md)の手順に従って、エージェント・インストール・ファイルを CSS にプッシュします。

### エッジ・ノード上のエージェントのアップグレード
1. デバイス上の **root** またはクラスター上の **admin** としてエッジ・ノードにログインし、Horizon 環境変数を設定します。
```bash
export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
  export HZN_ORG_ID=<your-exchange-organization>
  export HZN_FSS_CSSURL=https://<ieam-management-hub-ingress>/edge-css/
```
{: codeblock}

2. クラスターのタイプに応じて、必要な環境変数を設定します (デバイスをアップグレードしている場合はこのステップをスキップしてください)。

  * **OCP エッジ・クラスター上:**
  
    エージェントが使用するストレージ・クラスを設定します。
    
    ```bash
    oc get storageclass
   export EDGE_CLUSTER_STORAGE_CLASS=<rook-ceph-cephfs-internal>
    ```
    {: codeblock}

    作成したサービス・アカウント名にレジストリー・ユーザー名を設定します。
    ```bash
    oc get serviceaccount -n openhorizon-agent
    export EDGE_CLUSTER_REGISTRY_USERNAME=<service-account-name>
    ```
    {: codeblock}

    レジストリー・トークンを設定します。 
    ```bash
    export EDGE_CLUSTER_REGISTRY_TOKEN=`oc serviceaccounts get-token $EDGE_CLUSTER_REGISTRY_USERNAME`
    ```
    {: codeblock}

  * **k3s の場合:**
  
    デフォルトのストレージ・クラスを使用するように **agent-install.sh** に指示します。
    
    ```bash
    export EDGE_CLUSTER_STORAGE_CLASS=local-path
    ```
    {: codeblock}

  * **microk8s の場合:**
  
    デフォルトのストレージ・クラスを使用するように **agent-install.sh** に指示します。
    
    ```bash
    export EDGE_CLUSTER_STORAGE_CLASS=microk8s-hostpath
    ```
    {: codeblock}

3. CSS から **agent-install.sh** をプルします。
```bash
curl -u $HZN_ORG_ID/$HZN_EXCHANGE_USER_AUTH $HZN_FSS_CSSURL/api/v1/objects/IBM/agent_files/agent-install.sh/data -o agent-install.sh --insecure && chmod +x agent-install.sh
```
{: codeblock}

4. **agent-install.sh** を実行して、更新されたファイルを CSS から取得し、Horizon エージェントを構成します。
  *  **エッジ・デバイス上:**
    ```bash
    sudo -s -E ./agent-install.sh -i 'css:' -s
    ```
    {: codeblock}

  *  **エッジ・クラスター上:**
    ```bash
    ./agent-install.sh -D cluster -i 'css:' -s
    ```
    {: codeblock}

**注:** エージェントのインストールの実行中に -s オプションを含め、登録をスキップします。これにより、エッジ・ノードはアップグレード前と同じ状態のままになります。

## 既知の問題および FAQ
{: #FAQ}

### {{site.data.keyword.ieam}} 4.2
* {{site.data.keyword.ieam}} 4.2.0 ローカルの cssdb Mongo データベースには既知の問題があり、ポッドの再スケジュール時にデータが失われます。 ローカル・データベースを使用している場合 (デフォルト)、{{site.data.keyword.ocp}} クラスターを 4.6 に更新する前に {{site.data.keyword.ieam}} {{site.data.keyword.semver}} アップグレードが完了することが可能になります。詳しくは、「[既知の問題](../getting_started/known_issues.md)」ページを参照してください。

* {{site.data.keyword.ocp}} クラスターはバージョン 4.4 以降ですがアップグレードしませんでした。自動アップグレードが停止しているようです。

  * この問題を解決するには、以下の手順を実行します。
  
    1) 現在の {{site.data.keyword.ieam}} Management Hub の内容をバックアップします。  バックアップについては、[データのバックアップとリカバリー](../admin/backup_recovery.md)の資料を参照してください。
    
    2) {{site.data.keyword.ocp}} クラスターをバージョン 4.6 にアップグレードします。
    
    3) {{site.data.keyword.ieam}} 4.2.0 ローカルの **cssdb** Mongo データベースに関する既知の問題のため、**ステップ 2** でのアップグレードによってデータベースが再初期化されます。
    
      * {{site.data.keyword.ieam}} の MMS 機能を活用しており、データ損失の懸念がある場合は、**ステップ 1** で取ったバックアップを使用して、[「データのバックアップとリカバリー」](../admin/backup_recovery.md)ページの**『リストア手順』**に従います。 (**注:** リストア手順を実行すると、ダウン時間が発生します。)
      
      * あるいは、MMS 機能を利用していない場合、MMS データ損失の懸念がない場合、またはリモート・データベースを使用している場合は、以下の手順を実行して {{site.data.keyword.ieam}} オペレーターをアンインストールして再インストールします。
      
        1) {{site.data.keyword.ocp}} クラスターの「Installed Operators」ページに移動します。
        
        2) IEAM Management Hub オペレーターを見つけて、そのページを開きます。
        
        3) 左側のアクション・メニューで、オペレーターをアンインストールすることを選択します。
        
        4) 「OperatorHub」ページに移動し、IEAM Management Hub オペレーターを再インストールします。

* {{site.data.keyword.ocp}} バージョン 4.5 はサポートされていますか?

  * {{site.data.keyword.ieam}} Management Hub は、{{site.data.keyword.ocp}} バージョン 4.5 ではテストされず、サポートされていません。  {{site.data.keyword.ocp}} バージョン 4.6 にアップグレードすることをお勧めします。

* {{site.data.keyword.ieam}} Management Hub のこのバージョンをオプトアウトする方法はありますか?

  * {{site.data.keyword.ieam}} Management Hub バージョン 4.2.0 は、バージョン {{site.data.keyword.semver}} がリリースされた時点でサポートされなくなりました。
