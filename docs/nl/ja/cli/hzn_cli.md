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

`hzn` コマンドは {{site.data.keyword.ieam}} コマンド・ライン・インターフェースです。 {{site.data.keyword.ieam}} エージェント・ソフトウェアをエッジ・ノードにインストールすると、`hzn` CLI が自動的にインストールされます。 ただし、このエージェントがなくても `hzn` CLI をインストールできます。 例えば、完全なエージェントなしで、エッジ管理者が {{site.data.keyword.ieam}} exchange を照会したい場合や、エッジ開発者が `hzn` コマンドを使用してテストしたい場合などがあります。

1. `horizon-cli` パッケージを取得します。 組織が[エッジ・ノード・ファイルの収集](../hub/gather_files.md)のステップで行ったことに応じて、CSS または `agentInstallFiles-<edge-node-type>.tar.gz` tar ファイルから、`horizon-cli` パッケージを取得できます。

   * CSS から `horizon-cli` パッケージを取得します。

      * まだ API 鍵を持っていない場合は、[API 鍵の作成](../hub/prepare_for_edge_nodes.md)の手順に従って作成します。 そのステップから環境変数を設定します。

         ```bash
         export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
  export HZN_ORG_ID=<your-exchange-organization>
  export HZN_FSS_CSSURL=https://<ieam-management-hub-ingress>/edge-css/
         ```
         {: codeblock}

      * `HOST_TYPE` を、`horizon-cli` パッケージをインストールするホストのタイプに一致する以下のいずれかの値に設定します。

         * linux-deb-amd64
         * linux-deb-arm64
         * linux-deb-armhf
         * linux-rpm-x86_64
         * linux-rpm-ppc64le
         * macos-pkg-x86_64

         ```bash
         HOST_TYPE=<host-type>
         ```
         {: codeblock}

      * CSS から、証明書、構成ファイル、および `horizon-cli` パッケージを含む tar ファイルをダウンロードします。

         ```bash
         curl -sSL -w "%{http_code}" -u "$HZN_ORG_ID/$HZN_EXCHANGE_USER_AUTH" -k -o agent-install.crt $HZN_FSS_CSSURL/api/v1/objects/IBM/agent_files/agent-install.crt/data
         curl -sSL -w "%{http_code}" -u "$HZN_ORG_ID/$HZN_EXCHANGE_USER_AUTH" --cacert agent-install.crt -o agent-install.cfg $HZN_FSS_CSSURL/api/v1/objects/IBM/agent_files/agent-install.cfg/data
         curl -sSL -w "%{http_code}" -u "$HZN_ORG_ID/$HZN_EXCHANGE_USER_AUTH" --cacert agent-install.crt -o horizon-agent-$HOST_TYPE.tar.gz $HZN_FSS_CSSURL/api/v1/objects/IBM/agent_files/horizon-agent-$HOST_TYPE.tar.gz/data
         ```
         {: codeblock}

      * tar ファイルから `horizon-cli` パッケージを解凍します。

         ```bash
         rm -f horizon-cli*   # remove any previous versions
         tar -zxvf horizon-agent-$HOST_TYPE.tar.gz
         ```
         {: codeblock}

   * または、`agentInstallFiles-<edge-node-type>.tar.gz` tar ファイルから、`horizon-cli` パッケージを取得します。

      * 管理ハブ管理者から `agentInstallFiles-<edge-node-type>.tar.gz` ファイルを取得します。ここで、`<edge-node-type>` は、`horizon-cli` をインストールするホストに一致します。 このファイルをこのホストにコピーします。

      * tar ファイルを解凍します。

         ```bash
         tar -zxvf agentInstallFiles-<edge-device-type>.tar.gz
         ```
         {: codeblock}

2. `/etc/default/horizon` を作成または更新します。

   ```bash
   sudo cp agent-install.cfg /etc/default/horizon
   sudo cp agent-install.crt /etc/horizon
   sudo sh -c "echo 'HZN_MGMT_HUB_CERT_PATH=/etc/horizon/agent-install.crt' >> /etc/default/horizon"
   ```
   {: codeblock}

3. 以下のように、`horizon-cli` パッケージをインストールします。

   * パッケージ・バージョンが、[コンポーネント](../getting_started/components.md)にリストされているデバイス・エージェントと同じであることを確認します。

   * debian ベースのディストリビューションの場合:

     ```bash
     sudo apt update && sudo apt install ./horizon-cli*.deb
     ```
     {: codeblock}

   * RPM ベースのディストリビューションの場合:

     ```bash
     sudo yum install ./horizon-cli*.rpm
     ```
     {: codeblock}

   * {{site.data.keyword.macOS_notm}} の場合:

     ```bash
     sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain horizon-cli.crt
     sudo installer -pkg horizon-cli-*.pkg -target /
     pkgutil --pkg-info com.github.open-horizon.pkg.horizon-cli   # confirm version installed
     ```
     {: codeblock}

## hzn CLI のアンインストール

ホストから `horizon-cli` パッケージを削除する必要がある場合、次のようにします。

* debian ベースのディストリビューションから `horizon-cli` をアンインストールする場合:

  ```bash
  sudo apt-get remove horizon-cli
  ```
  {: codeblock}

* RPM ベースのディストリビューションから `horizon-cli` をアンインストールする場合:

  ```bash
  sudo yum remove horizon-cli
  ```
  {: codeblock}

* {{site.data.keyword.macOS_notm}} から `horizon-cli` をアンインストールする場合:

  ```bash
  sudo horizon-cli-uninstall.sh
  ```
  {: codeblock}
