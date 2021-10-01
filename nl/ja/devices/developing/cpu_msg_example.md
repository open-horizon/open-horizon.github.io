---

copyright:
years: 2019, 2020
lastupdated: "2019-06-28"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# CPU to {{site.data.keyword.message_hub_notm}} サービス
{: #cpu_msg_ex}

このサンプルは、CPU 負荷パーセンテージ情報を収集して {{site.data.keyword.message_hub_notm}} に送信します。 このサンプルは、クラウド・サービスにデータを送信する独自のエッジ・アプリケーションを開発するのに役立ちます。
{:shortdesc}

## 始める前に
{: #cpu_msg_begin}

[エッジ・サービス作成の準備](service_containers.md)の前提条件ステップを実行してください。 その結果、以下の環境変数が設定され、以下のコマンドがインストールされ、以下のファイルが存在していなければなりません。

```bash
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID"
which git jq make
ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem
cat /etc/default/horizon
```

## 手順
{: #cpu_msg_procedure}

このサンプルは、[{{site.data.keyword.horizon_open}} ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://github.com/open-horizon/) オープン・ソース・プロジェクトの一部です。 [独自のバージョンの CPU To IBM Event Streams Edge Service のビルドと公開 ![新しいタブで開く](../../images/icons/launch-glyph.svg " 新しいタブで開く")](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/cpu2evtstreams/CreateService.md#-building-and-publishing-your-own-version-of-the-cpu-to-ibm-event-streams-edge-service) のステップに従ってから、ここに戻ってください。

## この例で学んだこと

### 必要なサービス

cpu2evtstreams エッジ・サービスは、タスクを実行するために、他の 2 つのエッジ・サービス (**cpu** および **gps**) に依存しているサービスの例です。 これらの依存関係の詳細は、以下のような **horizon/service.definition.json** ファイルの **requiredServices** セクションで確認できます。

```json
    "requiredServices": [
        {
            "url": "ibm.cpu",
            "org": "IBM",
            "versionRange": "[0.0.0,INFINITY)",
            "arch": "$ARCH"
        },
        {
            "url": "ibm.gps",
            "org": "IBM",
            "versionRange": "[0.0.0,INFINITY)",
            "arch": "$ARCH"
        }
    ],
```

### 構成変数
{: #cpu_msg_config_var}

**cpu2evtstreams** サービスを実行するには、その前にいくつかの構成が必要です。 エッジ・サービスは、タイプとデフォルト値を指定して構成変数を宣言できます。 これらの構成変数は、以下のような **horizon/service.definition.json** ファイルの **userInput** セクションで確認できます。

```json  
    "userInput": [
        {
            "name": "EVTSTREAMS_API_KEY",
            "label": "The API key to use when sending messages to your instance of IBM Event Streams",
            "type": "string",
            "defaultValue": ""
        },
        {
            "name": "EVTSTREAMS_BROKER_URL",
            "label": "The comma-separated list of URLs to use when sending messages to your instance of IBM Event Streams",
            "type": "string",
            "defaultValue": ""
        },
        {
            "name": "EVTSTREAMS_CERT_ENCODED",
            "label": "The base64-encoded self-signed certificate to use when sending messages to your ICP instance of IBM Event Streams. Not needed for IBM Cloud Event Streams.",
            "type": "string",
            "defaultValue": "-"
        },
        {
            "name": "EVTSTREAMS_TOPIC",
            "label": "The topic to use when sending messages to your instance of IBM Event Streams",
            "type": "string",
            "defaultValue": "cpu2evtstreams"
        },
        {
            "name": "SAMPLE_SIZE",
            "label": "the number of samples to read before calculating the average",
            "type": "int",
            "defaultValue": "5"
        },
        {
            "name": "SAMPLE_INTERVAL",
            "label": "the number of seconds between samples",
            "type": "int",
            "defaultValue": "2"
        },
        {
            "name": "MOCK",
            "label": "mock the CPU sampling",
            "type": "boolean",
            "defaultValue": "false"
        },
        {
            "name": "PUBLISH",
            "label": "publish the CPU samples to IBM Event Streams",
            "type": "boolean",
            "defaultValue": "true"
        },
        {
            "name": "VERBOSE",
            "label": "log everything that happens",
            "type": "string",
            "defaultValue": "1"
        }
    ],
```

これらのようなユーザー入力構成変数は、エッジ・ノードでエッジ・サービスが開始されるときに、値が設定されている必要があります。 値は、以下のソースのいずれかから (以下の優先順位で) 取得されます。

1. **hzn register -f** フラグで指定されたユーザー入力ファイル
2. Exchange のエッジ・ノード・リソースの **userInput** セクション
3. Exchange のパターン・リソースまたはデプロイメント・ポリシー・リソースの **userInput** セクション
4. Exchange のサービス定義リソース内に指定されたデフォルト値

このサービス用のエッジ・デバイスを登録したときに、デフォルト値を持たない構成変数をいくつか指定した **userinput.json** ファイルを作成しました。

### 開発のヒント
{: #cpu_msg_dev_tips}

構成変数をサービスに組み込むと、サービスのテストおよびデバッグに役立つことがあります。 例えば、このサービスのメタデータ (**service.definition.json**) およびコード (**service.sh**) は、以下の構成変数を使用します。

* **VERBOSE** は、実行中にログに記録される情報量を増やします。
* **PUBLISH** は、コードがメッセージを {{site.data.keyword.message_hub_notm}} に送信しようとするかどうかを制御します。
* **MOCK** は、**service.sh** が、従属サービス (**cpu** および **gps**) の REST API を呼び出そうとするのか、代わりに模擬データを自身で作成しようとするのかを制御します。

依存しているサービスのモック機能はオプションですが、必要なサービスから分離された状態でコンポーネントを開発およびテストするのに役立ちます。 また、この手法により、ハードウェア・センサーもアクチュエーターも存在しないデバイス・タイプでのサービスの開発が可能になります。

クラウド・サービスとの対話をオフにする機能は、開発およびテスト中に便利であり、不要な課金が発生しないようにしたり、合成 DevOps 環境でのテストを促進したりできます。

## 次の作業
{: #cpu_msg_what_next}

* [{{site.data.keyword.edge_devices_notm}} を使用したエッジ・サービスの開発](developing.md)にある他のエッジ・サービスのサンプルを試してください。
