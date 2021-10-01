---

copyright:
years: 2019
lastupdated: "2019-06-25"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# トラブルシューティング
{: #troubleshooting}

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) で発生する問題をトラブルシューティングする際に役立つ、トラブルシューティングのヒントと一般的な問題を確認します。
{:shortdesc}

以下のトラブルシューティング・ガイドでは、{{site.data.keyword.ieam}} システムの主なコンポーネントについて、またシステムの状態を判別するために組み込みインターフェースを調査する方法を説明しています。

## トラブルシューティング・ツール
{: #ts_tools}

{{site.data.keyword.ieam}} に含まれる多くのインターフェースは、問題の診断に使用できる情報を提供します。 この情報は、{{site.data.keyword.gui}}、HTTP REST API、および {{site.data.keyword.linux_notm}} シェル・ツール `hzn` を介して入手できます。

エッジ・マシンでは、ホストの問題、Horizon ソフトウェアの問題、Docker の問題、構成の問題、またはサービス・コンテナーのコードの問題のトラブルシューティングを行うことが必要になる場合があります。 エッジ・マシンのホストの問題はこの文書の対象外です。 Docker の問題をトラブルシューティングする必要がある場合、使用できる Docker コマンドやインターフェースは多数あります。 詳細については、Docker の資料を参照してください。

実行しているサービス・コンテナーがメッセージングに (Kafka に基づく) {{site.data.keyword.message_hub_notm}} を使用している場合は、{{site.data.keyword.ieam}} の Kafka ストリームに手動で接続して問題を診断することができます。 メッセージ・トピックをサブスクライブして、{{site.data.keyword.message_hub_notm}} によって受信された内容を監視することも、別の装置からのメッセージをシミュレートするためにメッセージ・トピックにパブリッシュすることもできます。 `kafkacat` {{site.data.keyword.linux_notm}} コマンドは、簡単に {{site.data.keyword.message_hub_notm}} にパブリッシュまたはサブスクライブする方法です。 このツールの最新バージョンを使用してください。 {{site.data.keyword.message_hub_notm}} は、情報へのアクセスに使用できるグラフィカル Web ページも提供しています。

{{site.data.keyword.horizon}} がインストールされているマシンでは、`hzn` コマンドを使用して、ローカル {{site.data.keyword.horizon}} エージェントとリモート {{site.data.keyword.horizon_exchange}} の問題をデバッグします。 内部では、`hzn` コマンドが、提供された HTTP REST API と対話します。 `hzn` コマンドは、アクセスを簡略化し、REST API 自体よりも優れたユーザー・エクスペリエンスを提供します。 `hzn` コマンドは、多くの場合、出力でより詳細な説明テキストを提供し、組み込まれたオンライン・ヘルプ・システムを含んでいます。 使用すべきコマンド、コマンドの構文および引数に関する詳細情報を入手するには、ヘルプ・システムを使用します。 このヘルプ情報を表示するには、`hzn --help` コマンドまたは `hzn \<subcommand\> --help` コマンドを実行します。

{{site.data.keyword.horizon}} パッケージがサポートまたはインストールされていないノードでは、基礎となる HTTP REST API と直接対話することができます。 例えば、`curl` ユーティリティーまたはその他の REST API CLI ユーティリティーを使用できます。 REST 照会をサポートする言語でプログラムを作成することもできます。 

## トラブルシューティングのヒント
{: #ts_tips}

特定の問題のトラブルシューティングを行う場合、以下のトピックについて、ご使用のシステムの状態に関する質問および関連するヒントを確認してください。 質問ごとに、その質問がシステムのトラブルシューティングにどのように関係があるかについて説明されています。 質問によっては、ご使用のシステムに関連する情報の入手方法のヒントや詳細ガイドが記載されています。

これらの質問は、問題のデバッグの性質に基づいており、さまざまな環境に関連しています。 例えば、エッジ・ノードで問題のトラブルシューティングを行う場合、ノードに対する完全なアクセス権限と制御が必要になる場合があります。これにより、情報をさらに収集して表示できるようになります。

* [トラブルシューティングのヒント](troubleshooting_devices.md)

  {{site.data.keyword.ieam}} を使用したときに発生する可能性がある一般的な問題を確認します。
