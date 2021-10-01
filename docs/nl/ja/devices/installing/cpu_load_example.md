---

copyright:
years: 2020
lastupdated: "2020-02-06"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# {{site.data.keyword.message_hub_notm}} に対する CPU 使用率
{: #cpu_load_ex}

このホスト CPU 負荷率は、CPU 負荷率データを取り込み、IBM Event Streams を介してそのデータを使用可能にするサンプルのデプロイメント・パターンです。

このエッジ・サービスは、エッジ・デバイスの CPU 負荷を繰り返し照会し、結果のデータを [IBM Event Streams ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://www.ibm.com/cloud/event-streams) に送信します。 このエッジ・サービスは、特殊なセンサー・ハードウェアを必要としないため、どのエッジ・ノードでも実行できます。

このタスクを実行する前に、『[Hello World サンプルを使用したエッジ・デバイスでの Horizon エージェントのインストールと登録](registration.md)』のステップを実行して、登録および登録抹消を行ってください。

より現実的なシナリオでの経験を積めるように、この cpu2evtstreams サンプルでは以下のような一般的なエッジ・サービスのさらなる側面を示しています。

* 動的エッジ・デバイス・データの照会
* エッジ・デバイス・データの分析 (例えば、`cpu2evtstreams` は CPU 負荷の期間平均を計算します)
* 処理されたデータの中央データ取り込みサービスへの送信
* データ転送を安全に認証するための Event Stream 資格情報の取得の自動化

## 始める前に
{: #deploy_instance}

cpu2evtstreams エッジ・サービスをデプロイする前に、そのデータを受信するための、クラウドで実行されている {{site.data.keyword.message_hub_notm}} のインスタンスが必要です。 組織のすべてのメンバーが、1 つの {{site.data.keyword.message_hub_notm}} インスタンスを共有できます。 インスタンスがデプロイされている場合、アクセス情報を取得して環境変数を設定します。

### {{site.data.keyword.cloud_notm}} への {{site.data.keyword.message_hub_notm}} のデプロイ
{: #deploy_in_cloud}

1. {{site.data.keyword.cloud_notm}} にナビゲートします。

2. 「**リソースの作成**」をクリックします。

3. 検索ボックスに「`Event Streams`」と入力します。

4. **「Event Streams」**タイルを選択します。

5. **「Event Streams」**で、サービス名を入力し、ロケーションと料金プランを選択したら、**「作成」**をクリックしてインスタンスをプロビジョンします。

6. プロビジョニングが完了したら、インスタンスをクリックします。

7. トピックを作成するには、+ アイコンをクリックし、インスタンスに「`cpu2evtstreams`」と名前を付けます。

8. ご使用の端末で資格情報を作成するか、資格情報が作成済みの場合にはそれを取得できます。 資格情報を作成するには、**「サービス資格情報」 > 「新規資格情報」**をクリックしてください。 以下のコード・ブロックのようにフォーマットされた新規資格情報を使用して、`event-streams.cfg` という名前のファイルを作成します。 これらの資格情報の作成が必要なのは一度のみですが、自分自身や {{site.data.keyword.event_streams}} アクセスを必要とする他のチーム・メンバーが今後も使用できるように、このファイルは保存します。

   ```
   EVTSTREAMS_API_KEY="<the value of api_key>"
   EVTSTREAMS_BROKER_URL="<all kafka_brokers_sasl values in a single string, separated by commas>"
   ```
   {: codeblock}
        
   例えば「資格情報の表示」ペインでは以下のように表示されます。

   ```
   EVTSTREAMS_BROKER_URL=broker-4-x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-3-  x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-2-x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-0-x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-1-x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-5-x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093
   ```
   {: codeblock}

9. `event-streams.cfg` の作成後、これらの環境変数をシェルに設定します。

   ```
   eval export $(cat event-streams.cfg)
   ```
   {: codeblock}

### {{site.data.keyword.cloud_notm}} での {{site.data.keyword.message_hub_notm}} のテスト
{: #testing}

1. `kafkacat` (https://linuxhostsupport.com/blog/how-to-install-apache-kafka-on-ubuntu-16-04/) をインストールします。

2. 最初の端末では、`cpu2evtstreams` トピックをサブスクライブするために以下を入力します。

    ```
    kafkacat -C -q -o end -f "%t/%p/%o/%k: %s\n" -b $EVTSTREAMS_BROKER_URL -X api.version.request=true -X security.protocol=sasl_ssl -X sasl.mechanisms=PLAIN -X sasl.username=token -X sasl.password=$EVTSTREAMS_API_KEY -t cpu2evtstreams
    ```
    {: codeblock}

3. 2 番目の端末では、元のコンソールに表示するために、テスト・コンテンツを `cpu2evtstreams` トピックにパブリッシュします。 以下に例を示します。

    ```
    echo 'hi there' | kafkacat -P -b $EVTSTREAMS_BROKER_URL -X api.version.request=true -X security.protocol=sasl_ssl -X sasl.mechanisms=PLAIN -X sasl.username=token -X sasl.password=$EVTSTREAMS_API_KEY -t cpu2evtstreams
    ```
    {: codeblock}

## エッジ・デバイスの登録
{: #reg_device}

この cpu2evtstreams サービスのサンプルをエッジ・ノードで実行するには、エッジ・ノードを `IBM/pattern-ibm.cpu2evtstreams` デプロイメント・パターンに登録する必要があります。 [{{site.data.keyword.message_hub_notm}} に対する Horizon CPU (Horizon CPU To {{site.data.keyword.message_hub_notm}})![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/cpu2evtstreams/README.md)の**最初の**セクションのステップを実行します。

## 追加情報
{: #add_info}

CPU サンプル・ソース・コードは、{{site.data.keyword.edge_devices_notm}} エッジ・サービス開発のサンプルとして [{{site.data.keyword.horizon_open}} サンプル・リポジトリー ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://github.com/open-horizon/examples) にあります。 このソースには、このサンプルのためにエッジ・ノードで実行される 3 つすべてのサービスのコードが含まれています。

  * cpu サービス。ローカル・プライベート Docker ネットワーク上の REST サービスとして CPU 負荷率データを提供します。 詳しくは、『[Horizon CPU Percent Service ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://github.com/open-horizon/examples/tree/master/edge/services/cpu_percent)』を参照してください。
  * gps サービス。GPS ハードウェア (使用可能な場合) からのロケーション情報、またはエッジ・ノードの IP アドレスから推定されるロケーション情報を提供します。 ロケーション・データは、ローカル・プライベート Docker ネットワーク上の REST サービスとして提供されます。 詳しくは、『[Horizon GPS Service ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://github.com/open-horizon/examples/tree/master/edge/services/gps)』を参照してください。
  * cpu2evtstreams サービス。他の 2 つのサービスで提供されている REST API を使用します。 このサービスは、結合したデータをクラウドの {{site.data.keyword.message_hub_notm}} kafka ブローカーに送信します。 このサービスについて詳しくは、『[{{site.data.keyword.horizon}} CPU To {{site.data.keyword.message_hub_notm}} Service ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/cpu2evtstreams/cpu2evtstreams.md)』を参照してください。
  * {{site.data.keyword.message_hub_notm}} について詳しくは、[イベント・ストリーム - 概要![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://www.ibm.com/cloud/event-streams?mhsrc=ibmsearch_a&mhq=event%20streams)を参照してください。

## 次の作業
{: #cpu_next}

独自のソフトウェアをエッジ・ノードにデプロイする場合は、独自のエッジ・サービスと、関連するデプロイメント・パターンまたはデプロイメント・ポリシーを作成する必要があります。 詳しくは、『[{{site.data.keyword.edge_devices_notm}} を使用したエッジ・サービスの開発](../developing/developing.md)』を参照してください。
