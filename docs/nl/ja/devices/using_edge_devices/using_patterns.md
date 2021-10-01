---

copyright:
  years: 2020
lastupdated: "2020-05-10"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# パターンの使用
{: #using_patterns}

通常、開発者が Horizon Exchange 内でエッジ・サービスを公開した後、サービス・デプロイメント・パターンを {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) ハブに公開できます。

hzn CLI は、{{site.data.keyword.horizon_exchange}} 内のパターンをリストおよび管理する機能を提供します。これには、サービス・デプロイメント・パターンをリスト、公開、検証、更新、および削除するためのコマンドが含まれます。 また、特定のデプロイメント・パターンに関連付けられている暗号鍵をリストおよび削除するための方法も提供します。

CLI コマンドの完全なリストおよび詳細については、以下を実行します。

```
hzn exchange pattern -h
```
{: codeblock}

## 例

{{site.data.keyword.horizon_exchange}} 内のパターン・リソースに署名して作成 (または更新) します。

```
hzn exchange pattern publish --json-file=JSON-FILE [<flags>]
```
{: codeblock}

## デプロイメント・パターンの使用

デプロイメント・パターンの使用は、エッジ・ノードにサービスをデプロイするための単純で簡単な方法です。 エッジ・ノードにデプロイされる最上位サービス (複数可) を指定すると、{{site.data.keyword.ieam}} が残りを処理します (最上位サービスの従属サービスのデプロイメントなど)。

サービスを作成して {{site.data.keyword.ieam}} Exchange に追加した後、次のような `pattern.json` ファイルを作成する必要があります。

```
{
  "name": "pattern-ibm.cpu2evtstreams-arm",
  "label": "Edge ibm.cpu2evtstreams Service Pattern for arm",
  "description": "Pattern for ibm.cpu2evtstreams for arm",
  "public": true,
  "services": [
    {
      "serviceUrl": "ibm.cpu2evtstreams",
      "serviceOrgid": "IBM",
      "serviceArch": "arm",
      "serviceVersions": [
        {
          "version": "1.4.3",
          "priority": {
            "priority_value": 1,
            "retries": 1,
            "retry_durations": 1800,
            "verified_durations": 45
          }
        },
        {
          "version": "1.4.2",
          "priority": {
            "priority_value": 2,
            "retries": 1,
            "retry_durations": 3600
          }
        }
      ]
    }
  ],
  "userInput": [
    {
      "serviceOrgid": "IBM",
      "serviceUrl": "ibm.cpu2evtstreams",
      "serviceVersionRange": "[0.0.0,INFINITY)",
      "inputs": [
        {
          "name": "EVTSTREAMS_API_KEY",
          "value": "$EVTSTREAMS_API_KEY"
        },
        {
          "name": "EVTSTREAMS_BROKER_URL",
          "value": "$EVTSTREAMS_BROKER_URL"
        },
        {
          "name": "EVTSTREAMS_CERT_ENCODED",
          "value": "$EVTSTREAMS_CERT_ENCODED"
        }
      ]
    }
  ]
}
```
{: codeblock}

このコードは、`arm` デバイス用の `ibm.cpu2evtstreams` サービスの `pattern.json` ファイルの例です。 ここで示されているように、`cpu_percent` および `gps` (`cpu2evtstreams` の従属サービス) を指定する必要はありません。 その作業は `service_definition.json` ファイルによって処理されるため、正常に登録されたエッジ・ノードはそれらのワークロードを自動的に実行します。

`pattern.json` ファイルを使用すると、`serviceVersions` セクションでロールバック設定をカスタマイズすることができます。 サービスの古いバージョンを複数指定して、新バージョンでエラーがあった場合にエッジ・ノードがロールバックする際の優先順位を各バージョンに付与できます。 各ロールバック・バージョンに優先順位を割り当てることに加えて、指定されたサービスの優先順位の低いバージョンにフォールバックするまでの再試行の回数と期間などといったことを指定できます。

また、デプロイメント・パターンを公開したときにサービスが中央で正しく機能するために必要な構成変数を、最下部の近くにある `userInput` セクションに組み込むことによって設定できます。 `ibm.cpu2evtstreams` サービスは、公開されるときに、IBM Event Streams にデータを公開するために必要な資格情報を一緒に渡します。これは以下によって行うことができます。

```
hzn exchange pattern publish -f pattern.json
```
{: codeblock}

パターンが公開されると、そこに arm デバイスを登録できます。

```
hzn register -p pattern-ibm.cpu2evtstreams-arm
```
{: codeblock}

このコマンドにより、`ibm.cpu2evtstreams` およびすべての従属サービスがノードにデプロイされます。

注: [Using the CPU To IBM Event Streams Edge Service with Deployment Pattern ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://github.com/open-horizon/examples/tree/master/edge/evtstreams/cpu2evtstreams#-using-the-cpu-to-ibm-event-streams-edge-service-with-deployment-pattern) リポジトリー例のステップに従った場合のように `userInput.json` ファイルが上記の `hzn register` コマンドに渡されることはありません。 なぜなら、ユーザー入力はパターン自体と共に渡されており、自動的に登録するエッジ・ノードがそれらの環境変数にアクセスできるためです。

登録抹消することによって、すべての `ibm.cpu2evtstreams` ワークロードを停止できます。

```
hzn unregister -fD
```
{: codeblock}
