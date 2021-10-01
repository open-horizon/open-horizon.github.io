---

copyright:
years: 2019
lastupdated: "2020-2-25"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Watson speech to text
{: #watson-speech}

このサービスは、Watson という単語を listen します。 それが検出されると、サービスはオーディオ・クリップを取り込み、Speech to Text のインスタンスに送信します。  ストップワードが (オプションで) 削除され、書き起こされたテキストが {{site.data.keyword.event_streams}} に送信されます。

## 始める前に

ご使用のシステムが、以下の要件を満たしていることを確認してください。

* 『[エッジ・デバイスの準備](adding_devices.md)』のステップを実行して、登録および登録抹消を行う必要がある。
* Raspberry Pi に USB サウンド・カードおよびマイクが取り付けられている。 

このサービスを使用するには、{{site.data.keyword.event_streams}} のインスタンスおよび IBM Speech to Text の両方が正しく実行されている必要があります。 Event Streams のインスタンスをデプロイする方法については、『[ホスト CPU 負荷率のサンプル (cpu2evtstreams)](../using_edge_services/cpu_load_example.md)』を参照してください。  

必要な {{site.data.keyword.event_streams}} の環境変数が設定されていることを確認します。

```
echo "$EVTSTREAMS_API_KEY, $EVTSTREAMS_BROKER_URL"
```
{: codeblock}

このサンプルで使用される Event Streams のトピックは、デフォルトで `myeventstreams` ですが、以下の環境変数を設定することで任意のトピックを使用できます。

```
export EVTSTREAMS_TOPIC=<your-topic-name>
```
{: codeblock}

## IBM Speech to Text のインスタンスのデプロイ
{: #deploy_watson}

現時点でインスタンスがデプロイされている場合は、アクセス情報を取得して環境変数を設定するか、以下のステップに従います。

1. IBM Cloud にナビゲートします。
2. 「**リソースの作成**」をクリックします。
3. 検索ボックスに「`Speech to Text`」と入力します。
4. `「Speech to Text」`タイルを選択します。
5. リージョンと料金プランを選択して、サービス名を入力し、**「作成」**をクリックしてインスタンスをプロビジョンします。
6. プロビジョニングが完了したら、インスタンスをクリックして資格情報の API 鍵と URL をメモし、それらを以下の環境変数としてエクスポートします。

    ```
    export STT_IAM_APIKEY=<speech-to-text-api-key>
    export STT_URL=<speech-to-text-url>
    ```
    {: codeblock}

7. Speech to Text サービスをテストする方法については、入門セクションを参照してください。

## エッジ・デバイスの登録
{: #watson_reg}

この watsons2text サービスのサンプルをエッジ・ノードで実行するには、エッジ・ノードを `IBM/pattern-ibm.watsons2text-arm` デプロイメント・パターンに登録する必要があります。 README ファイルの「[ Using Watson Speech to Text to IBM Event Streams Service with Deployment Pattern](https://github.com/open-horizon/examples/tree/master/edge/evtstreams/watson_speech2text#-using-the-ibm-watson-speech-to-text-to-ibm-event-streams-service-with-deployment-pattern)」セクションのステップを実行します。

## 追加情報

`processtect` サンプルのソース・コードは、{{site.data.keyword.edge_notm}} 開発のサンプルとして Horizon GitHub リポジトリーからも入手できます。 このソースには、このサンプルのためにエッジ・ノードで実行される 4 つすべてのサービスのコードが含まれています。 

これらのサービスは、以下のとおりです。

* [hotworddetect](https://github.com/open-horizon/examples/tree/master/edge/services/hotword_detection) サービスは、対象の単語 Watson を listens して検出し、オーディオ・クリップを録音して、それを mqtt ブローカーにパブリッシュします。
* [watsons2text](https://github.com/open-horizon/examples/tree/master/edge/evtstreams/watson_speech2text) サービスは、オーディオ・クリップを受信し、それを IBM Speech to Text に送信して、復号したテキストを mqtt ブローカーにパブリッシュします。
* [stopwordremoval](https://github.com/open-horizon/examples/tree/master/edge/services/stopword_removal) サービスは、WSGI サーバーとして実行され、{"text": "how are you today"} のような JSON オブジェクトを取得し、共通のストップワードを削除してから {"result": "how you today"} を返します。
* [mqtt2kafka](https://github.com/open-horizon/examples/tree/master/edge/services/mqtt2kafka) サービスは、サブスクライブしている mqtt トピックで何かを受信すると、データを {{site.data.keyword.event_streams}} にパブリッシュします。
* [mqtt_broker](https://github.com/open-horizon/examples/tree/master/edge/services/mqtt_broker) は、すべてのコンテナー間通信を担当します。

## 次の作業

* 独自のバージョンのオフライン音声アシスタント・エッジ・サービスの作成および公開の手順については、[オフライン音声アシスタント・エッジ・サービス](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/watson_speech2text/CreateService.md#-building-and-publishing-your-own-version-of-the-watson-speech-to-text-to-ibm-event-streams-service) を参照してください。 Open Horizon サンプル・リポジトリーの `watson_speech2text` ディレクトリーにあるステップに従います。

* [Open Horizon examples リポジトリー](https://github.com/open-horizon/examples)を参照してください。
