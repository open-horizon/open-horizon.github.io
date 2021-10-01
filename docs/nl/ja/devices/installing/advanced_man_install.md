---

copyright:
years: 2019
lastupdated: "2019-011-14"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# エージェントの拡張手動インストールおよび登録
{: #advanced_man_install}

このセクションでは、{{site.data.keyword.edge_devices_notm}} エージェントをエッジ・デバイスにインストールして登録するための各手動ステップについて説明します。 より自動化された方法については、[エージェントの自動インストールおよび登録](automated_install.md)を参照してください。
{:shortdesc}

## エージェントのインストール
{: #agent_install}

注: コマンド構文については、[本書の規則](../../getting_started/document_conventions.md)を参照してください。

1. 続行する前に、`agentInstallFiles-<edge-device-type>.tar.gz` ファイルを入手し、このファイルと一緒に作成された API 鍵を取得してください。

    [管理ハブのインストール](../../hub/offline_installation.md)の構成後ステップとして、HelloWorld サンプルを使用したエッジ・デバイスでの {{site.data.keyword.horizon}} エージェントのインストールと登録に必要なファイルが含まれている圧縮ファイルが作成済みです。

2. USB スティック、セキュア・コピー・コマンド、または他の方法を使用して、このファイルをエッジ・デバイスにコピーします。

3. この tar ファイルを解凍します。

   ```bash
   tar -zxvf agentInstallFiles-<edge-device-type>.tar.gz
   ```
   {: codeblock}

4. エッジ・デバイスのタイプに応じて、以下のいずれかのセクションを使用してください。

### Linux (ARM 32 ビット、ARM 64 ビット、または x86_64) エッジ・デバイスまたは仮想マシンへのエージェントのインストール
{: #agent_install_linux}

以下のステップに従います。

1. ログインします。非 root ユーザーとしてログインしている場合は、root 特権を持つユーザーに切り替えます。

   ```bash
   sudo -s
   ```
   {: codeblock}

2. Docker バージョンを照会して、それが十分新しいものであるかどうかを確認します。

   ```bash
   docker --version
   ```
   {: codeblock}

      Docker がインストールされていないか、バージョンが `18.06.01` よりも古い場合は、最新バージョンの Docker をインストールします。

   ```bash
   curl -fsSL get.docker.com | sh
      docker --version
   ```
   {: codeblock}

3. このエッジ・デバイスにコピーした Horizon Debian パッケージをインストールします。

   ```bash
   apt update && apt install ./*horizon*.deb
   ```
   {: codeblock}
   
4. ユーザー固有の情報を環境変数として設定します。

   ```bash
   eval export $(cat agent-install.cfg)
   ```
   {: codeblock}

5. `/etc/default/horizon` に正しい情報を取り込むことで、ご使用のエッジ・デバイスの Horizon エージェントを {{site.data.keyword.edge_notm}} クラスターに指定します。

   ```bash
   sed -i.bak -e "s|^HZN_EXCHANGE_URL=[^ ]*|HZN_EXCHANGE_URL=${HZN_EXCHANGE_URL}|g" -e "s|^HZN_FSS_CSSURL=[^ ]*|HZN_FSS_CSSURL=${HZN_FSS_CSSURL}|g" /etc/default/horizon
   ```
   {: codeblock}

6. Horizon エージェントが `agent-install.crt` を信頼するようにします。

   ```bash
   if grep -qE '^HZN_MGMT_HUB_CERT_PATH=' /etc/default/horizon; then sed -i.bak -e "s|^HZN_MGMT_HUB_CERT_PATH=[^ ]*|HZN_MGMT_HUB_CERT_PATH=${PWD}/agent-install.crt|" /etc/default/horizon; else echo "HZN_MGMT_HUB_CERT_PATH=${PWD}/agent-install.crt" >> /etc/default/horizon; fi
   ```
   {: codeblock}
   
7. エージェントを再始動して、`/etc/default/horizon` への変更を取り込みます。

   ```bash
   systemctl restart horizon.service
   ```
   {: codeblock}

8. エージェントが稼働しており、正しく構成されていることを確認します。

   ```bash
   hzn version
       hzn exchange version
       hzn node list
   ```
   {: codeblock}  

      出力は次のようになります (バージョン番号と URL は異なる場合があります)。

   ```bash
   $ hzn version
   Horizon CLI version: 2.23.29
   Horizon Agent version: 2.23.29
   $ hzn exchange version
   1.116.0
   $ hzn node list
   {
         "id": "",
         "organization": null,
         "pattern": null,
         "name": null,
         "token_last_valid_time": "",
         "token_valid": null,
         "ha": null,
         "configstate": {
            "state": "unconfigured",
            "last_update_time": ""
         },
         "configuration": {
            "exchange_api": "https://9.30.210.34:8443/ec-exchange/v1/",
            "exchange_version": "1.116.0",
            "required_minimum_exchange_version": "1.116.0",
            "preferred_exchange_version": "1.116.0",
            "mms_api": "https://9.30.210.34:8443/ec-css",
            "architecture": "amd64",
            "horizon_version": "2.23.29"
         },
         "connectivity": {
            "firmware.bluehorizon.network": true,
            "images.bluehorizon.network": true
         }
      }
      ```
   {: codeblock}

9. 以前に特権シェルに切り替えた場合は、ここで終了します。 デバイスを登録する次のステップには root アクセス権限は必要ありません。

   ```bash
   exit
   ```
   {: codeblock}

10. 続けて[エージェントの登録](#agent_reg)を行います。

### macOS エッジ・デバイスへのエージェントのインストール
{: #mac-os-x}

1. `horizon-cli` パッケージ証明書を {{site.data.keyword.macOS_notm}} キーチェーンにインポートします。

   ```bash
   sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain horizon-cli.crt
   ```
   {: codeblock}

      注: このステップは、{{site.data.keyword.macOS_notm}} マシンごとに 1 回のみ実行する必要があります。 この信頼された証明書がインポートされていると、任意の将来のバージョンの {{site.data.keyword.horizon}} ソフトウェアをインストールできます。

2. {{site.data.keyword.horizon}} CLI パッケージをインストールします。

   ```bash
   sudo installer -pkg horizon-cli-*.pkg -target /
   ```
   {: codeblock}

3. 前のコマンドは、`/usr/local/bin` にコマンドを追加します。 以下を `~/.bashrc` に追加することで、そのディレクトリーをシェル・パスに追加します。

   ```bash
   export PATH="/usr/local/bin:$PATH"
   ```
   {: codeblock}

4. 以下を `~/.bashrc` に追加して `/usr/local/share/man` ディレクトリーをシェル・パスに追加することで、man ページのパスに `/usr/local/share/man` を追加します。

  ```bash
  export MANPATH="/usr/local/share/man:$MANPATH"
  ```
  {: codeblock}

5. 以下を `~/.bashrc` に追加することで、`hzn` コマンドのサブコマンド名コンプリートを有効にします。

  ```bash
  source /usr/local/share/horizon/hzn_bash_autocomplete.sh
  ```
  {: codeblock}

6. **新規デバイス**をインストールする場合、この手順は**不要**です。 しかし、以前にこのマシン上に Horizon コンテナーをインストールして開始した場合は、以下を実行してコンテナーを停止します。

  ```bash
  horizon-container stop
  ```
  {: codeblock}
7. ユーザー固有の情報を環境変数として設定します。

  ```bash
  eval export $(cat agent-install.cfg)
  ```
  {: codeblock}

8. `/etc/default/horizon` に正しい情報を取り込むことで、ご使用のエッジ・デバイスの Horizon エージェントを {{site.data.keyword.edge_notm}} クラスターに指定します。

  ```bash
  sudo mkdir -p /etc/default

  sudo sh -c "cat << EndOfContent > /etc/default/horizon
  HZN_EXCHANGE_URL=$HZN_EXCHANGE_URL
  HZN_FSS_CSSURL=$HZN_FSS_CSSURL
  HZN_MGMT_HUB_CERT_PATH=${PWD}/agent-install.crt
  HZN_DEVICE_ID=$(hostname)
  EndOfContent"
  ```
  {: codeblock}

9. {{site.data.keyword.horizon}} エージェントを開始します。

  ```bash
  horizon-container start
  ```
  {: codeblock}

10. エージェントが稼働しており、正しく構成されていることを確認します。

  ```bash
  hzn version
       hzn exchange version
       hzn node list
  ```
  {: codeblock}

      出力は次のようになります (バージョン番号と URL は異なる場合があります)。

  ```bash
  $ hzn version
   Horizon CLI version: 2.23.29
   Horizon Agent version: 2.23.29
   $ hzn exchange version
   1.116.0
   $ hzn node list
   {
         "id": "",
         "organization": null,
         "pattern": null,
         "name": null,
         "token_last_valid_time": "",
         "token_valid": null,
         "ha": null,
         "configstate": {
            "state": "unconfigured",
            "last_update_time": ""
         },
         "configuration": {
            "exchange_api": "https://9.30.210.34:8443/ec-exchange/v1/",
            "exchange_version": "1.116.0",
            "required_minimum_exchange_version": "1.116.0",
            "preferred_exchange_version": "1.116.0",
            "mms_api": "https://9.30.210.34:8443/ec-css",
            "architecture": "amd64",
            "horizon_version": "2.23.29"
         },
         "connectivity": {
            "firmware.bluehorizon.network": true,
            "images.bluehorizon.network": true
         }
      }
  ```
  {: codeblock}

11. 続けて[エージェントの登録](#agent_reg)を行います。

## エージェントの登録
{: #agent_reg}

1. ユーザー固有の情報を **環境変数**として設定します。

  ```bash
  eval export $(cat agent-install.cfg)
  export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
  ```
  {: codeblock}

2. サンプル・エッジ・サービス・デプロイメントのパターンのリストを表示します。

  ```bash
  hzn exchange pattern list IBM/
  ```
  {: codeblock}

3. helloworld エッジ・サービスは最も基本的なサンプルであり、サービスを始める際に最適です。 エッジ・デバイスを {{site.data.keyword.horizon}} に**登録**して、**helloworld デプロイメント・パターン**を実行します。

  ```bash
  hzn register -p IBM/pattern-ibm.helloworld
  ```
  {: codeblock}

  注: 出力の **Using node ID** で始まる行に、ノード ID が表示されます。

4. エッジ・デバイスは、いずれかの {{site.data.keyword.horizon}} 合意ボットと合意します (通常、これには約 15 秒かかります)。 `agreement_finalized_time` フィールドおよび `agreement_execution_start_time` フィールドが埋まるまで、このデバイスの**合意を繰り返し照会します**。

  ```bash
  hzn agreement list
  ```
  {: codeblock}

5. **合意が成立したら**、結果として開始された Docker コンテナー・エッジ・サービスをリストします。

  ```bash
  sudo docker ps
  ```
  {: codeblock}

6. helloworld エッジ・サービス**出力**を表示します。

  ```bash
  sudo hzn service log -f ibm.helloworld
  ```
  {: codeblock}

## 次の作業
{: #what_next}

[IBM Event Streams に対する CPU 使用率](cpu_load_example.md)にナビゲートして、他のエッジ・サービスのサンプルを引き続き試してください。
