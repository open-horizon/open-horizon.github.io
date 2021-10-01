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

# エージェントの一括インストールおよび登録
{: #batch-install}

一括インストール・プロセスは、似たタイプの (言い換えると、アーキテクチャー、オペレーティング・システム、および、パターンまたはポリシーが同じ) 複数のエッジ・デバイスをセットアップするために使用します。

注: このプロセスでは、ターゲットのエッジ・デバイスとして macOs コンピューターはサポートされません。ただし、必要な場合は、このプロセスを macOs コンピューターから駆動できます (言い換えると、このホストは macOs コンピューターであることが可能です)。

### 前提条件

* インストールおよび登録されるデバイスには、管理ハブへのネットワーク・アクセスが必要です。
* デバイスには既にオペレーティング・システムがインストールされている必要があります。
* エッジ・デバイス用に DHCP を使用している場合、タスクが完了するまで同じ IP アドレスを維持しなければなりません (または、DDNS を使用している場合は、同じ `hostname` を維持しなければなりません)。
* サービス定義に、または、パターンまたはデプロイメント・ポリシー内に、すべてのエッジ・サービス・ユーザー入力がデフォルトとして指定されている必要があります。 ノード固有のユーザー入力を使用することはできません。

### 手順
{: #proc-multiple}

1. **agentInstallFiles-&lt;edge-device-type&gt;.tar.gz** ファイルおよび API 鍵を取得または作成していない場合は、『[エッジ・デバイス用の必要な情報とファイルの収集](../../hub/gather_files.md#prereq_horizon)』に従ってこれを行います。 ファイルの名前と API 鍵の値を以下の環境変数に設定します。

   ```bash
   export AGENT_TAR_FILE=agentInstallFiles-<edge-device-type>.tar.gz
   export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
   ```
  {: codeblock}

2. **pssh** パッケージには、**pssh** コマンドおよび **pscp** コマンドが含まれています。これにより、多数のエッジ・デバイスに対してコマンドを並行して実行したり、多数のエッジ・デバイスにファイルを並行してコピーしたりできます。 これらのコマンドがホストにまだない場合、この時点でパッケージをインストールしてください。

  * {{site.data.keyword.linux_notm}} の場合:

   ```bash
   sudo apt install pssh
   alias pssh=parallel-ssh
   alias pscp=parallel-scp
   ```
   {: codeblock}

  * {{site.data.keyword.macOS_notm}} の場合:

   ```bash
   brew install pssh
   ```
   {: codeblock}

   (まだ **brew** がインストールされていない場合、[Install pssh on Mac with Brew ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://brewinstall.org/Install-pssh-on-Mac-with-Brew/) を参照してください。)

3. エッジ・デバイスに **pscp** および **pssh** アクセス権限を付与するには、いくつかの方法があります。 このセクションでは、SSH 公開鍵の使用について説明します。第一の要件は、このホストに SSH 鍵ペアがなければならないということです (通常、**~/.ssh/id_rsa** および **~/.ssh/id_rsa.pub** 内)。 まだない場合は、生成してください。

   ```bash
   ssh-keygen -t rsa
   ```
   {: codeblock}

4. 公開鍵 (**~/.ssh/id_rsa.pub**) の内容を各エッジ・デバイスの **/root/.ssh/authorized_keys** に入れます。

5. **node-id-mapping.csv** という名前の 2 列のマッピング・ファイルを作成します。これは、各エッジ・デバイスの IP アドレスまたはホスト名を、登録時に付けられる必要のある {{site.data.keyword.ieam}} ノード名にマップします。 **agent-install.sh** が各エッジ・デバイスで実行されるときに、そのデバイスに付けられるエッジ・ノード名をこのファイルが知らせます。 以下のような CSV フォーマットを使用します。

   ```bash
   Hostname/IP, Node Name
   1.1.1.1, factory2-1
   1.1.1.2, factory2-2
   ```
   {: codeblock}

6. **node-id-mapping.csv** をエージェント tar ファイルに追加します。

   ```bash
   gunzip $AGENT_TAR_FILE
   tar -uf ${AGENT_TAR_FILE%.gz} node-id-mapping.csv
   gzip ${AGENT_TAR_FILE%.gz}
   ```
   {: codeblock}

7. 一括でインストールおよび登録するエッジ・デバイスのリストを、**nodes.hosts** という名前のファイルに入れます。 これは、**pscp** コマンドおよび **pssh** コマンドで使用されます。 各行は標準 ssh フォーマット `<user>@<IP-or-hostname>` でなければなりません。

   ```bash
   root@1.1.1.1
   root@1.1.1.2
   ```
   {: codeblock}

   注: いずれかのホストに非 root ユーザーを使用する場合は、そのユーザーがパスワードを入力しなくても sudo を使用できるように sudo が構成されている必要があります。

8. エージェント tar ファイルをエッジ・デバイスにコピーします。 このステップには少し時間がかかることがあります。

   ```bash
   pscp -h nodes.hosts -e /tmp/pscp-errors $AGENT_TAR_FILE /tmp
   ```
   {: codeblock}

   注: いずれかのエッジ・デバイスの **pscp** 出力で **[FAILURE]** が示される場合、**/tmp/pscp-errors** のエラーが表示されます。

9. 各エッジ・デバイスで **agent-install.sh** を実行して、Horizon エージェントをインストールし、エッジ・デバイスを登録します。 パターンまたはポリシーのどちらかを使用してエッジ・デバイスを登録できます。

   1. パターンを使用してエッジ・デバイスを登録する場合は、次のようにします。

      ```bash
      pssh -h nodes.hosts -t 0 "bash -c \"tar -zxf /tmp/$AGENT_TAR_FILE agent-install.sh && sudo -s ./agent-install.sh -i . -u $HZN_EXCHANGE_USER_AUTH -p IBM/pattern-ibm.helloworld -w ibm.helloworld -o IBM -z /tmp/$AGENT_TAR_FILE 2>&1 >/tmp/agent-install.log \" "
      ```
      {: codeblock}

      **IBM/pattern-ibm.helloworld** デプロイメント・パターンを使用してエッジ・デバイスを登録する代わりに、**-p**、**-w**、および **-o** フラグを変更して、異なるデプロイメント・パターンを使用できます。 使用可能なすべての **agent-install.sh** フラグ説明を表示するには、以下のようにします。

      ```bash
      tar -zxf $AGENT_TAR_FILE agent-install.sh &&./agent-install.sh -h
      ```
      {: codeblock}

   2. あるいは、ポリシーを使用してエッジ・デバイスを登録する場合は、次のようにします。 ノード・ポリシーを作成し、それをエッジ・デバイスにコピーし、そのポリシーを使用してデバイスを登録します。

      ```bash
      echo '{ "properties": [ { "name": "nodetype", "value": "special-node" } ] }' > node-policy.json
      pscp -h nodes.hosts -e /tmp/pscp-errors node-policy.json /tmp
      pssh -h nodes.hosts -t 0 "bash -c \"tar -zxf /tmp/$AGENT_TAR_FILE agent-install.sh && sudo -s ./agent-install.sh -i . -u $HZN_EXCHANGE_USER_AUTH -n /tmp/node-policy.json  -z /tmp/$AGENT_TAR_FILE 2>&1 >/tmp/agent-install.log \" "
      ```
      {: codeblock}

      この時点で、エッジ・デバイスは作動可能ですが、サービスをこのタイプのエッジ・デバイス (この例では **nodetype** が **special-node** のデバイス) にデプロイすることを指定するデプロイメント・ポリシー (ビジネス・ポリシー) を作成するまで、エッジ・サービスの実行を開始しません。 詳しくは、『[デプロイメント・ポリシーの使用](../using_edge_devices/detailed_policy.md)』を参照してください。

10. いずれかのエッジ・デバイスの **pssh** 出力で **[FAILURE]** が示される場合、そのエッジ・デバイスに移動してから **/tmp/agent-install.log** を表示することによって問題を調査できます。

11. **pssh** コマンドの実行中に、{{site.data.keyword.edge_notm}} コンソールでエッジ・ノードの状況を確認できます。 [管理コンソールの使用](../getting_started/accessing_ui.md)を参照してください。
