---

copyright:
years: 2019
lastupdated: "2019-07-04"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# デプロイメント・パターンのサンプル
{: #deploy_pattern_ex}

{{site.data.keyword.edge_devices_notm}} デプロイメント・パターンの使用開始方法の詳細を確認できるように、デプロイメント・パターンとしてロードできるサンプル・プログラムが用意されています。
{:shortdesc}

これらの事前作成された各サンプル・デプロイメント・パターンの登録を試し、デプロイメント・パターンの使用方法の詳細を確認してください。

以下のいずれかのデプロイメント・パターン・サンプル用にエッジ・ノードを登録するには、まず、エッジ・ノードの既存のデプロイメント・パターンの登録を解除する必要があります。 エッジ・ノードで以下のコマンドを実行して、デプロイメント・パターンの登録を解除します。
```
 hzn unregister
 hzn node list | jq .configstate.state
```
{: codeblock}

出力例:
```
"unconfigured"
```
{: codeblock}

コマンド出力で `"unconfigured"` ではなく `"unconfiguring"` と表示された場合、数分待ってからコマンドを再実行します。 通常、このコマンドの完了には数秒しかかかりません。 出力で `"unconfigured"` と表示されるまで、コマンドを再試行してください。

## 例
{: #pattern_examples}

* [Hello, world ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://github.com/open-horizon/examples/blob/master/edge/services/helloworld):
  {{site.data.keyword.edge_devices_notm}} デプロイメント・パターンを紹介する最小限の `"Hello, world."` サンプルです。

* [ホスト CPU 負荷率](cpu_load_example.md):
  CPU 負荷率データを取り込み、{{site.data.keyword.message_hub_notm}} を介して使用可能にするサンプル・デプロイメント・パターンです。

* [ソフトウェア無線](software_defined_radio_ex.md):
  無線局の音声を取り込み、音声を抽出し、抽出された音声をテキストに変換する、完全な機能を備えたサンプルです。 このサンプルは、テキストに対して感情分析を実行し、ユーザー・インターフェースを介してデータおよび結果を使用可能にします。ユーザー・インターフェースでは、各エッジ・ノードのデータの詳細を表示できます。 このサンプルを使用して、エッジ処理の詳細を確認できます。
