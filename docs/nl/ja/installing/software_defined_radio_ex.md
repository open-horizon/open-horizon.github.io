---

copyright:
years: 2020
lastupdated: "2020-02-5" 

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

このサンプルでは、エッジ処理の例としてソフトウェア無線 (SDR) を使用しています。 SDR により、無線スペクトル全体で生データをクラウド・サーバーに処理のために送信できます。 エッジ・ノードはデータをローカルで処理し、容量を削減し、価値を高めたデータを追加の処理のためにクラウド処理サービスに送信します。
{:shortdesc}

以下の図は、この SDR のサンプルの体系を示しています。

<img src="../OH/docs/images/edge/08_sdrarch.svg" style="margin: 3%" alt="例の体系">

SDR のエッジ処理は、無線局の音声を取り込み、音声を抽出し、抽出された音声をテキストに変換する、完全な機能を備えたサンプルです。 このサンプルは、テキストに対して感情分析を実行し、ユーザー・インターフェースを介してデータおよび結果を使用可能にします。ユーザー・インターフェースでは、各エッジ・ノードのデータの詳細を表示できます。 このサンプルを使用して、エッジ処理の詳細を確認できます。

SDR は、専門のアナログ回路のセットを必要とする作業を扱うためのコンピューター CPU 内のデジタル回路を使用して、無線信号を受信します。 通常、アナログ回路が受信できる無線スペクトル幅は限定されています。 例えば、FM 無線局を受信するために作成されたアナログ無線レシーバーでは、無線スペクトルの他の範囲の無線信号を受信できません。 SDR では、スペクトルの大部分にアクセスできます。 SDR ハードウェアがない場合は、模擬データを使用できます。 模擬データを使用している場合、インターネット・ストリームからの音声は、FM を介してブロードキャストされ、エッジ・ノードで受信されたものとして扱われます。

このタスクを実行する前に、[エージェントのインストール](registration.md)のステップを実行して、エッジ・デバイスの登録および登録抹消を行ってください。

このコードには、以下の主要コンポーネントが含まれています。

|コンポーネント|説明|
|---------|-----------|
|[sdr サービス](https://github.com/open-horizon/examples/tree/master/edge/services/sdr)|下位サービスは、エッジ・ノード上のハードウェアにアクセスします。|
|[ssdr2evtstreams サービス](https://github.com/open-horizon/examples/tree/master/edge/evtstreams/sdr2evtstreams)|高位サービスは、それより下位の sdr サービスからデータを受信し、エッジ・ノード上でそのデータのローカル分析を実行します。 sdr2evtstreams サービスは、その後、処理されたデータをクラウド・バックエンド・ソフトウェアに送信します。|
|[クラウド・バックエンド・ソフトウェア](https://github.com/open-horizon/examples/tree/master/cloud/sdr)|クラウド・バックエンド・ソフトウェアは、さらに分析を進めるためにエッジ・ノードからデータを受信します。 バックエンド実装は、その後、Web ベースの UI で、エッジ・ノードのマップの提示などを行うことができます。|
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

5. この sdr2evtstreams サービスのサンプルをエッジ・ノードで実行するには、エッジ・ノードを IBM/pattern-ibm.sdr2evtstreams デプロイメント・パターンに登録する必要があります。 [SDR から IBM Event Streams のサンプル・エッジ・サービスを使用するための前提条件](https://www.ibm.com/links?url=https%3A%2F%2Fgithub.com%2Fopen-horizon%2Fexamples%2Ftree%2Fmaster%2Fedge%2Fevtstreams%2Fsdr2evtstreams) のステップを実行してください。

6. サンプル Web UI を調べて、エッジ・ノードが結果を送信しているかどうかを確認します。 

## SDR 実装の詳細

### sdr 下位サービス
{: #sdr}

このサービスのソフトウェア・スタックの最下位には `sdr` サービス実装が含まれています。 このサービスは、一般的な `librtlsdr` ライブラリーおよび派生する `rtl_fm` および `rtl_power` ユーティリティーを `rtl_rpcd` デーモンと一緒に使用することによって、ローカルのソフトウェア定義ラジオ・ハードウェアにアクセスします。 `librtlsdr` ライブラリーについて詳しくは、[librtlsdr](https://github.com/librtlsdr/librtlsdr) を参照してください。

`sdr` サービスは、ソフトウェア定義ラジオ・ハードウェアを直接制御して、特定の周波数にチューニングして送信データを受信したり、指定されたスペクトル範囲内の信号の強さを測定したりします。 このサービスの典型的なワークフローは、特定の周波数にチューニングして、その周波数の局からデータを受信することです。 その後、このサービスは、収集したデータを処理できます。

### sdr2evtstreams 高位サービス
{: #sdr2evtstreams}

`sdr2evtstreams` 高位サービス実装は、ローカルのプライベート仮想 Docker ネットワークを介して、`sdr` サービス REST API と `gps` サービス REST API の両方を使用します。 `sdr2evtstreams` サービスは、`sdr` サービスからデータを受信し、そのデータに対してローカル推論を実行し、音声のための最適な局を選択します。 次に、`sdr2evtstreams` サービスは、{{site.data.keyword.message_hub_notm}} を使用することにより、Kafka を使用してオーディオ・クリップをクラウドに公開します。

### IBM Functions
{: #ibm_functions}

IBM Functions は、このソフトウェア定義ラジオのサンプル・アプリケーションのクラウド側を調整します。 IBM Functions は、OpenWhisk に基づいていて、サーバーレス・コンピューティングを可能にします。 サーバーレス・コンピューティングとは、コード・コンポーネントを、サポートするインフラストラクチャー (オペレーティング・システムやプログラミング言語システムなど) なしでデプロイできることを意味します。 IBM Functions を使用すると、ユーザーは自身のコードに集中でき、その他すべてのことについて、スケーリング、セキュリティー、および継続的な保守を IBM に任せることができます。 ハードウェアをプロビジョンする必要はなく、VM もコンテナーも不要です。

サーバーレス・コード・コンポーネントは、イベントに応えてトリガー (実行) するように構成されます。 このサンプルでは、トリガーするイベントは、エッジ・ノードによってオーディオ・クリップが {{site.data.keyword.message_hub_notm}} に公開されるたびの、{{site.data.keyword.message_hub_notm}} におけるエッジ・ノードからのメッセージの受信です。 データの取り込みとその処理のためにサンプルのアクションがトリガーされます。 そこでは、IBM Watson Speech-To-Text (STT) サービスを使用して、着信音声データがテキストに変換されます。 その後、そのテキストが IBM Watson Natural Language Understanding (NLU) サービスに送信されて、含まれている各名詞に表されている感情が分析されます。 詳しくは、[IBM Functions action code](https://github.com/open-horizon/examples/blob/master/cloud/sdr/data-processing/ibm-functions/actions/msgreceive.js) を参照してください。

### IBM データベース
{: #ibm_database}

IBM Functions アクション・コードは、最後に、計算した感情結果を IBM Databases に保管します。 その後、Web サーバーおよびクライアント・ソフトウェアは、このデータをデータベースからユーザーの Web ブラウザーに提示する処理を実行します。

### Web インターフェース
{: #web_interface}

ソフトウェア定義ラジオ・アプリケーションの Web ユーザー・インターフェースは、IBM Databases から提示される感情データをユーザーが表示することを可能にします。 このユーザー・インターフェースは、データを提供したエッジ・ノードを示すマップも表示します。 このマップは、`sdr2evtstreams` サービスのエッジ・ノード・コードによって使用される IBM 提供の `gps` サービスからのデータを使用して作成されます。 `gps` サービスは、GPS ハードウェアとのインターフェースを持つか、または、デバイス所有者から位置情報を受信することができます。 GPS ハードウェアとデバイス所有者位置の両方がない場合、`gps` サービスは、エッジ・ノードの IP アドレスを使用して地理的ロケーションを判別することによって、エッジ・ノード位置を推測できます。 `sdr2evtstreams` は、このサービスを使用することによって、オーディオ・クリップを送信するときにクラウドに位置データを提供できます。 詳しくは、[software-defined radio application web UI code](https://github.com/open-horizon/examples/tree/master/cloud/sdr/ui/sdr-app) を参照してください。

オプションで、独自のソフトウェア無線サンプル Web UI を作成したい場合には、IBM Functions、IBM Databases、および Web UI コードを IBM Cloud にデプロイできます。 これは、[有料アカウントを作成](https://cloud.ibm.com/login) した後、単一のコマンドで行えます。 詳しくは、[deployment repository content](https://www.ibm.com/links?url=https%3A%2F%2Fgithub.com%2Fopen-horizon%2Fexamples%2Ftree%2Fmaster%2Fcloud%2Fsdr%2Fdeploy%2Fibm) を参照してください。 

**注**: このデプロイメント・プロセスには、{{site.data.keyword.cloud_notm}} アカウントに課金される有料サービスが必要です。

## 次の作業

独自のソフトウェアをエッジ・ノードにデプロイする場合は、独自のエッジ・サービスと、関連するデプロイメント・パターンまたはデプロイメント・ポリシーを作成する必要があります。 詳しくは、[デバイス用のエッジ・サービスの開発](../OH/docs/developing/developing.md)を参照してください。
