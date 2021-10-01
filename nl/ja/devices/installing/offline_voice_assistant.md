---

copyright:
years: 2019
lastupdated: "2019-11-12"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# オフライン音声アシスタント
{: #offline-voice-assistant}

1 分ごとに、オフライン音声アシスタントは 5 秒のオーディオ・クリップを録音し、そのオーディオ・クリップをエッジ・デバイスでローカルにテキストに変換し、ホスト・マシンにコマンドを実行して出力を読み上げるように指示します。 

## 始める前に
{: #before_beginning}

ご使用のシステムが、以下の要件を満たしていることを確認してください。

* 『[エッジ・デバイスの準備](adding_devices.md)』のステップを実行して、登録および登録抹消を行う必要がある。
* Raspberry Pi に USB サウンド・カードおよびマイクが取り付けられている。 

## エッジ・デバイスの登録
{: #reg_edge_device}

この `processtext` サービスのサンプルをエッジ・ノードで実行するには、エッジ・ノードを `IBM/pattern-ibm.processtext` デプロイメント・パターンに登録する必要があります。 

readme ファイルの [Using the Offline Voice Assistant Example Edge Service with Deployment Pattern![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://github.com/open-horizon/examples/tree/master/edge/services/processtext#-using-the-offline-voice-assistant-example-edge-service-with-deployment-pattern) セクションのステップを実行します。

## 追加情報
{: #additional_info}

`processtext` サンプルのソース・コードは、{{site.data.keyword.edge_devices_notm}} 開発のサンプルとして Horizon GitHub リポジトリーからも入手できます。 このソースには、このサンプルのためにエッジ・ノードで実行されるすべてのサービスのコードが含まれています。 

これらの [Open Horizon サンプル ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://github.com/open-horizon/examples/tree/master/edge/services/voice2audio) のサービスには、以下が含まれています。

* [voice2audio ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://github.com/open-horizon/examples/tree/master/edge/services/voice2audio) サービスは、5 秒のオーディオ・クリップを録音し、それを mqtt ブローカーにパブリッシュします。
* [audio2text ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://github.com/open-horizon/examples/tree/master/edge/services/audio2text) サービスは、オーディオ・クリップを使用し、それを pocket sphinx を使用してオフラインでテキストに変換します。
* [processtext ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://github.com/open-horizon/examples/tree/master/edge/services/processtext) サービスは、テキストを使用し、記録されたコマンドの実行を試みます。
* [text2speech ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://github.com/open-horizon/examples/tree/master/edge/services/text2speech) サービスは、スピーカーを介してコマンドの出力を再生します。
* [mqtt_broker ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://github.com/open-horizon/examples/tree/master/edge/services/mqtt_broker) は、すべてのコンテナー間通信を管理します。

## 次の作業
{: #what_next}

独自版の Watson speech to text の作成および公開の手順については、[Open Horizon サンプル ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://github.com/open-horizon/examples/blob/master/edge/services/processtext/CreateService.md#-building-and-publishing-your-own-version-of-the-offline-voice-assistant-edge-service) リポジトリーの `processtext` ディレクトリーのステップを参照してください。 
