---

copyright:
  years: 2020
lastupdated: "2020-5-11"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# hzn CLI のインストール
{: #using_hzn_cli}

{{site.data.keyword.ieam}} エージェント・ソフトウェアをエッジ・ノードにインストールすると、**hzn** CLI が自動的にインストールされます。ただし、このエージェントがなくても **hzn** CLI をインストールできます。例えば、エッジ管理者が {{site.data.keyword.ieam}} exchange を照会したい場合や、エッジ開発者が **hzn dev** コマンドを使用してテストしたい場合などがあります。

1. 管理ハブ管理者から **agentInstallFiles-&lt;edge-device-type&gt;.tar.gz** ファイルを取得します。ここで、**&lt;edge-device-type&gt;** は、**hzn** をインストールするホストに一致します。『[エッジ・デバイス用の必要な情報とファイルの収集](../../hub/gather_files.md#prereq_horizon)』で既に作成されているはずです。 **hzn** をインストールするホストにこのファイルをコピーします。

2. 以降のステップのために環境変数にファイル名を設定します。

   ```bash
   export AGENT_TAR_FILE=agentInstallFiles-<edge-device-type>.tar.gz
   ```
   {: codeblock}

3. tar ファイルから horizon CLI パッケージを解凍します。

   ```bash
   tar -zxvf $AGENT_TAR_FILE 'horizon-cli*'
   ```
   {: codeblock}

   * パッケージ・バージョンが、[コンポーネント](../getting_started/components.md)にリストされているデバイス・エージェントと同じであることを確認します。

4. 以下のように、**horizon-cli** パッケージをインストールします。

   * debian ベースのディストリビューションの場合:

     ```bash
     sudo apt update && sudo apt install horizon-cli*.deb
     ```
     {: codeblock}

   * {{site.data.keyword.macOS_notm}} の場合:

     ```bash
     sudo installer -pkg horizon-cli-*.pkg -target /
     ```
     {: codeblock}

     注: {{site.data.keyword.macOS_notm}} では、horizon-cli pkg ファイルを Finder からインストールすることもできます。ファイルをダブルクリックするとインストーラーが開きます。プログラムを「cannot be opened because it is from an unidentified developer」というエラー・メッセージが表示される場合、ファイルを右クリックし、**「開く」**を選択します。 「Are you sure you want to open it?」というプロンプトが出されたら、もう一度**「開く」**をクリックします。 その後、プロンプトに従って CLI horizon パッケージをインストールします。その際、ご使用の ID に管理者特権があることを確認してください。

## hzn CLI のアンインストール

ホストから **horizon-cli** パッケージを削除する必要がある場合、次のようにします。

* debian ベースのディストリビューションから **horizon-cli** をアンインストールする場合:

  ```bash
  sudo apt-get remove horizon-cli
  ```
  {: codeblock}

* {{site.data.keyword.macOS_notm}} から **horizon-cli** をアンインストールする場合:

  * hzn クライアント・フォルダー (/usr/local/bin) を開き、`hzn` アプリを「ごみ箱」(Dock の最後にある) にドラッグします。
