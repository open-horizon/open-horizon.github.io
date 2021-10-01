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

注: 以下のステップは、すべてのデバイス・タイプ (アーキテクチャー) で同じです。

1. 管理者から **agentInstallFiles-&lt;edge-device-type&gt;.tar.gz** ファイルおよび API 鍵を取得します。 『[エッジ・デバイス用の必要な情報とファイルの収集](../../hub/gather_files.md#prereq_horizon)』セクションで、既にそれらが作成されているはずです。 セキュア・コピー・コマンド、USB スティック、または他の方法を使用して、このファイルをエッジ・デバイスにコピーします。 API 鍵の値をメモします。 これは以降のステップで必要になります。 次に、以降のステップのために環境変数にファイル名を設定します。

   ```bash
   export AGENT_TAR_FILE=agentInstallFiles-<edge-device-type>.tar.gz
   ```
   {: codeblock}

2. tar ファイルから **agent-install.sh** コマンドを解凍します。

   ```bash
   tar -zxvf $AGENT_TAR_FILE agent-install.sh
   ```
   {: codeblock}

3. {{site.data.keyword.horizon}} Exchange ユーザー資格情報をエクスポートします (API 鍵)。

  ```bash
  export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
  ```
  {: codeblock}

4. **agent-install.sh** コマンドを実行して {{site.data.keyword.horizon}} エージェントをインストールおよび構成し、helloworld サンプル・エッジ・サービスを実行するためにエッジ・デバイスを登録します。

  ```bash
  sudo -s ./agent-install.sh -i . -u $HZN_EXCHANGE_USER_AUTH -p IBM/pattern-ibm.helloworld -w ibm.helloworld -o IBM -z $AGENT_TAR_FILE
  ```
  {: codeblock}

  注: エージェント・パッケージのインストール中にプロンプトが出され、「現行のノード構成を上書きしますか? (Do you want to overwrite the current node configuration?) `[y/N]`:」という質問が表示されます。**agent-install.sh** が構成を正しく設定するので、「y」と答えて Enter を押してかまいません。

  使用可能なすべての **agent-install.sh** フラグ説明を表示するには、以下のようにします。

  ```bash
  ./agent-install.sh -h
  ```
  {: codeblock}

5. これで、エッジ・デバイスはインストールおよび登録されたので、ユーザー固有の情報を環境変数としてシェルに設定します。 これで、helloworld 出力を表示するために **hzn** コマンドを実行できます。

  ```bash
  eval export $(cat agent-install.cfg)
  hzn service log -f ibm.helloworld
  ```
  {: codeblock}
  
  注: 出力表示を停止するには、**Ctrl** **C** を押します。

6. **hzn** コマンドのフラグおよびサブコマンドを検討します。

  ```bash
  hzn --help
  ```
  {: codeblock}

7. {{site.data.keyword.ieam}} コンソールを使用して、エッジ・ノード (デバイス)、サービス、パターン、およびポリシーを表示することもできます。[管理コンソールの使用](../getting_started/accessing_ui.md)を参照してください。

8. [IBM Event Streams に対する CPU 使用率](cpu_load_example.md)にナビゲートして、他のエッジ・サービスのサンプルを引き続き試してください。
