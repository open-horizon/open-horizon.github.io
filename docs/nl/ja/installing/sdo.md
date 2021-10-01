---

copyright:
years: 2020
lastupdated: "2020-4-24"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# SDO エージェントのインストールおよび登録
{: #sdo}

Intel によって作成された [SDO](https://software.intel.com/en-us/secure-device-onboard) (Secure Device Onboard) により、エッジ・デバイスの構成およびエッジ管理ハブとの関連付けを簡単かつセキュアに行うことができます。 {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) では SDO 対応デバイスがサポートされるため、ゼロタッチで (単にデバイスの電源オンのみで) エージェントがデバイスにインストールされ、{{site.data.keyword.ieam}} 管理ハブに登録されるようになります。

## SDO の概要
{: #sdo-overview}

SDO は、以下のコンポーネントで構成されています。

* エッジ・デバイス上の SDO モジュール (通常、デバイス製造元によってインストールされます)
* 所有権証明書 (デバイスの購入者に物理デバイスと一緒に提供されるファイル)
* SDO ランデブー・サーバー (SDO 対応デバイスが初回始動時に最初に接続する既知のサーバー)
* SDO 所有者サービス (この特定の {{site.data.keyword.ieam}} のインスタンスを使用するようにデバイスを構成する、{{site.data.keyword.ieam}} 管理ハブで実行されるサービス)

**注**: SDO では、エッジ・デバイスのみがサポートされ、エッジ・クラスターはサポートされません。

### SDO のフロー

<img src="../OH/docs/images/edge/09_SDO_device_provisioning.svg" style="margin: 3%" alt="SDO インストールの概要">

## 始める前に
{: #before_begin}

SDO では、エージェント・ファイルが {{site.data.keyword.ieam}} Cloud Sync Service (CSS) に保管されている必要があります。 そのようになっていない場合は、管理者に、『[エッジ・ノード・ファイルの収集](../hub/gather_files.md)』で説明されているように以下のいずれかのコマンドを実行するように依頼してください。

  `edgeNodeFiles.sh ALL -c ...`

## SDO の試用
{: #trying-sdo}

SDO 対応エッジ・デバイスを購入する前に、SDO 対応デバイスをシミュレートする VM を使用して、{{site.data.keyword.ieam}} の SDO サポートをテストできます。

1. API 鍵が必要です。 API 鍵がまだない場合は、API 鍵を作成する手順について、[API 鍵の作成](../hub/prepare_for_edge_nodes.md)を参照してください。

2. {{site.data.keyword.ieam}} 管理者に連絡して、以下の環境変数の値を入手します。 (次のステップで必要になります)。

   ```bash
   export HZN_ORG_ID=<exchange-org>
   export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
   export HZN_SDO_SVC_URL=https://<ieam-mgmt-hub-ingress>/edge-sdo-ocs/api
   export HZN_MGMT_HUB_CERT_PATH=<path-to-mgmt-hub-self-signed-cert>
   export CURL_CA_BUNDLE=$HZN_MGMT_HUB_CERT_PATH
   ```

3. [open-horizon/SDO-support リポジトリー](https://github.com/open-horizon/SDO-support/blob/master/README-1.10.md)の手順に従って、SDO が自動的に {{site.data.keyword.ieam}} エージェントをデバイスにインストールし、それを {{site.data.keyword.ieam}} 管理ハブに登録することを監視します。

## {{site.data.keyword.ieam}} ドメインへの SDO 対応デバイスの追加
{: #using-sdo}

SDO 対応デバイスが購入済みであり、それを {{site.data.keyword.ieam}} ドメインに取り込む場合は、以下のようにします。

1. [{{site.data.keyword.ieam}} 管理コンソールにログインします](../console/accessing_ui.md)。

2. **「ノード」**タブで、**「ノードの追加」**をクリックします。 

   SDO サービスにプライベート所有権キーを作成するために必要な情報を入力し、対応する公開鍵をダウンロードします。
   
3. デバイスの購入時に受け取った所有権証明書をインポートするために必要な情報を入力します。

4. デバイスをネットワークに接続し、電源をオンにします。

5. 管理コンソールに戻り、**「ノード」**概要ページを表示し、インストール名でフィルターに掛けることで、デバイスがオンラインになるまでの進行状況を確認します。
