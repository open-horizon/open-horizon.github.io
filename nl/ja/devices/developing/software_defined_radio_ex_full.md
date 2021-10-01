---

copyright:
years: 2019
lastupdated: "2019-06-26"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# ソフトウェア無線のエッジ処理
{: #defined_radio_ex}

***WRITER NOTE: this will be merged with software_defined_radio_ex.md when Troy combines.***

このサンプルでは、エッジ処理の例としてソフトウェア無線 (SDR) を使用しています。 SDR により、無線スペクトル全体で生データをクラウド・サーバーに処理のために送信できます。 エッジ・ノードはデータをローカルで処理し、容量を削減し、価値を高めたデータを追加の処理のためにクラウド処理サービスに送信します。
{:shortdesc}

以下の図は、この SDR のサンプルの体系を示しています。

<img src="../../images/edge/08_sdrarch.svg" width="70%" alt="サンプル体系">

SDR のエッジ処理は、無線局の音声を取り込み、音声を抽出し、抽出された音声をテキストに変換する、完全な機能を備えたサンプルです。 このサンプルは、テキストに対して感情分析を実行し、ユーザー・インターフェースを介してデータおよび結果を使用可能にします。ユーザー・インターフェースでは、各エッジ・ノードのデータの詳細を表示できます。 このサンプルを使用して、エッジ処理の詳細を確認できます。

SDR は、専門のアナログ回路のセットを必要とする作業を扱うためのコンピューター CPU 内のデジタル回路を使用して、無線信号を受信します。 通常、アナログ回路が受信できる無線スペクトル幅は限定されています。 例えば、FM 無線局を受信するために作成されたアナログ無線レシーバーでは、無線スペクトルの他の範囲の無線信号を受信できません。 SDR では、スペクトルの大部分にアクセスできます。 SDR ハードウェアがない場合は、模擬データを使用できます。 模擬データを使用している場合、インターネット・ストリームからの音声は、FM を介してブロードキャストされ、エッジ・ノードで受信されたものとして扱われます。

このタスクを実行する前に、[Hello World サンプルを使用したエッジ・デバイスでの Horizon エージェントのインストールと登録](registration.md)のステップを実行して、エッジ・デバイスの登録および登録抹消を行ってください。

このコードには、以下の主要コンポーネントが含まれています。

|コンポーネント|説明|
|---------|-----------|
|[sdr サービス ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://github.com/open-horizon/examples/tree/master/edge/services/sdr)|下位サービスは、エッジ・ノード上のハードウェアにアクセスします。|
|[ssdr2evtstreams サービス ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://github.com/open-horizon/examples/tree/master/edge/evtstreams/sdr2evtstreams)|高位サービスは、それより下位の sdr サービスからデータを受信し、エッジ・ノード上でそのデータのローカル分析を実行します。 sdr2evtstreams サービスは、その後、処理されたデータをクラウド・バックエンド・ソフトウェアに送信します。|
|[クラウド・バックエンド・ソフトウェア ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://github.com/open-horizon/examples/tree/master/cloud/sdr)|クラウド・バックエンド・ソフトウェアは、さらに分析を進めるためにエッジ・ノードからデータを受信します。 バックエンド実装は、その後、Web ベースの UI で、エッジ・ノードのマップの提示などを行うことができます。|
{: caption="表 1. {{site.data.keyword.message_hub_notm}} 主要コンポーネントへのソフトウェア無線" caption-side="top"}

## デバイスの登録

このサービスはどのエッジ・デバイスでも模擬データを使用して実行可能ですが、SDR ハードウェアを使った Raspberry Pi のようなエッジ・デバイスを使用する場合は、まず、ご使用の SDR ハードウェアをサポートするようにカーネル・モジュールを構成してください。 このモジュールは手動で構成する必要があります。 Docker コンテナーは、Linux の各種ディストリビューションをそのコンテキストで設定できますが、コンテナーでカーネル・モジュールをインストールすることはできません。 

以下のステップを実行してこのモジュールを構成します。

1. root ユーザーとして、`/etc/modprobe.d/rtlsdr.conf` という名前のファイルを作成します。

   ```
   sudo nano /etc/modprobe.d/rtlsdr.conf
   ```
   {: codeblock}

2. 以下の行をファイルに追加します。

   ```
   blacklist rtl2830
     blacklist rtl2832
     blacklist dvb_usb_rtl28xxu
   ```
   {: codeblock}

3. ファイルを保存し、続行する前に以下のように再始動します。
   ```
   sudo reboot
   ```
   {: codeblock}   

4. 環境で以下の {{site.data.keyword.message_hub_notm}} API 鍵を設定します。 この鍵は、このサンプルで使用するために作成されたものであり、エッジ・ノードによって収集され、処理されたデータを IBM ソフトウェア無線 UI をフィードするために使用されます。

   ```
   export EVTSTREAMS_API_KEY=X2e8cSjbDAMk-ztJLaoi3uffy8qsQTnZttUjcHCfm7cp
    export EVTSTREAMS_BROKER_URL=broker-3-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-5-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-4-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-1-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-0-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-2-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093
   ```
   {: codeblock}

5. この sdr2evtstreams サービスのサンプルをエッジ・ノードで実行するには、エッジ・ノードを IBM/pattern-ibm.sdr2evtstreams デプロイメント・パターンに登録する必要があります。 [SDR から IBM Event Streams のサンプル・エッジ・サービスを使用するための前提条件 ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://www.ibm.com/links?url=https%3A%2F%2Fgithub.com%2Fopen-horizon%2Fexamples%2Ftree%2Fmaster%2Fedge%2Fevtstreams%2Fsdr2evtstreams) のステップを実行してください。

6. サンプル Web UI を調べて、エッジ・ノードが結果を送信しているかどうかを確認します。 詳しくは、[ソフトウェア無線のサンプル Web UI ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://sdr-poc-sdr-poc-app-delightful-leopard.mybluemix.net) を参照してください。 以下の資格情報を使用してログインします。

   * ユーザー名: guest@ibm.com
   * パスワード: guest123

## クラウドでのデプロイ

オプションで、独自のソフトウェア無線サンプル Web UI を作成したい場合には、IBM Functions、IBM Databases、および Web UI コードを IBM Cloud にデプロイできます。 これは、[有料アカウントを作成 ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://cloud.ibm.com/login) した後、単一のコマンドで行えます。

デプロイメント・コードは examples/cloud/sdr/deploy/ibm リポジトリーに入っています。 For more information, see [デプロイメント・リポジトリーのコンテンツ ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://www.ibm.com/links?url=https%3A%2F%2Fgithub.com%2Fopen-horizon%2Fexamples%2Ftree%2Fmaster%2Fcloud%2Fsdr%2Fdeploy%2Fibm) を参照してください。 

このコードは、詳しい指示が記載された README.md ファイルと、ワークロードを処理する deploy.sh スクリプトからなります。 このリポジトリーには、deploy.sh スクリプトへの別のインターフェースとして、Makefile も含まれています。 サンプルの SDR 用に独自のクラウド・バックエンドをデプロイすることについて詳しくは、リポジトリーの説明を検討してください。

注: このデプロイメント・プロセスには、{{site.data.keyword.cloud_notm}} アカウントに課金される有料サービスが必要です。

## 次の作業

独自のソフトウェアをエッジ・ノードにデプロイする場合は、独自のエッジ・サービスと、関連するデプロイメント・パターンまたはデプロイメント・ポリシーを作成する必要があります。 詳しくは、『[IBM Edge Application Manager for Devices を使用したエッジ・サービスの開発](../developing/developing.md)』を参照してください。
