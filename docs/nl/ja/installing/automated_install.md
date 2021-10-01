---

copyright:
years: 2020
lastupdated: "2020-5-10"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# エージェントの自動インストールおよび登録
{: #method_one}

注: 以下のステップは、すべてのエッジ・デバイス・タイプ (アーキテクチャー) で同じです。

1. まだ API 鍵を持っていない場合は、[API 鍵の作成](../hub/prepare_for_edge_nodes.md)の手順に従って作成します。 このプロセスでは、API 鍵を作成し、エッジ・ノードのセットアップ時に必要ないくつかのファイルを見つけて環境変数値を収集します。

2. 以下のように、エッジ・デバイスにログインし、ステップ 1 で取得したのと同じ環境変数を設定します。

   ```bash
   export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
  export HZN_ORG_ID=<your-exchange-organization>
  export HZN_FSS_CSSURL=https://<ieam-management-hub-ingress>/edge-css/
   ```
   {: codeblock}

3. 管理者用の準備済みインストール・バンドルを使用していない場合は、クラウド同期サービス (CSS) から **agent-install.sh** スクリプトをデバイスにダウンロードして実行可能にします。

   ```bash
   curl -u "$HZN_ORG_ID/$HZN_EXCHANGE_USER_AUTH" -k -o agent-install.sh $HZN_FSS_CSSURL/api/v1/objects/IBM/agent_files/agent-install.sh/data
   chmod +x agent-install.sh
   ```
   {: codeblock}

4. 以下のように、**agent-install.sh** を実行して CSS から必要なファイルを取得し、{{site.data.keyword.horizon}} エージェントをインストールおよび構成し、helloworld サンプル・エッジ・サービスを実行するためのエッジ・デバイスを登録します。

   ```bash
   sudo -s -E ./agent-install.sh -i 'css:' -p IBM/pattern-ibm.helloworld -w '*' -T 120
   ```
   {: codeblock}

   使用可能なすべての **agent-install.sh** フラグの説明を表示するには、**./agent-install.sh -h** を実行します。

   注: {{site.data.keyword.macOS_notm}} では、エージェントはルートとして実行されている Docker コンテナーで実行されます。

5. 以下のようにして、helloworld の出力を表示します。

   ```bash
   hzn service log -f ibm.helloworld
  # Press Ctrl-c to stop the output display
   ```
   {: codeblock}

6. helloworld エッジ・サービスが開始しない場合は、以下のコマンドを実行してエラー・メッセージを確認します。

   ```bash
   hzn eventlog list -f
  # Press Ctrl-c to stop the output display
   ```
   {: codeblock}

7. (オプション) このエッジ・ノードで **hzn** コマンドを使用して、{{site.data.keyword.horizon}} Exchange 内のサービス、パターン、およびデプロイメント・ポリシーを表示します。 シェルで環境変数として固有の情報を設定し、以下のコマンドを実行します。

   ```bash
   eval export $(cat agent-install.cfg)
  hzn exchange service list IBM/
  hzn exchange pattern list IBM/
  hzn exchange deployment listpolicy
   ```
   {: codeblock}

8. 以下のようにして、すべての **hzn** コマンドのフラグおよびサブコマンドを探索します。

   ```bash
   hzn --help
   ```
   {: codeblock}

## 次の作業

* {{site.data.keyword.ieam}} コンソールを使用して、エッジ・ノード (デバイス)、サービス、パターン、およびポリシーを表示します。 詳しくは、[管理コンソールの使用](../console/accessing_ui.md)を参照してください。
* 別のエッジ・サービスの例を探索および実行します。 詳しくは、[IBM Event Streams に対する CPU 使用率](../using_edge_services/cpu_load_example.md)を参照してください。
