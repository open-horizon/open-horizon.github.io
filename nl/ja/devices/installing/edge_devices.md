---

copyright:
years: 2020
lastupdated: "2020-4-8"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# エッジ・デバイス
{: #edge_devices}

エッジ・デバイスは、エンタープライズまたはサービス・プロバイダーのコア・ネットワークへのエントリー・ポイントを提供します。 例として、スマートフォンやセキュリティー・カメラのほか、インターネット接続した電子レンジなども挙げられます。

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) は、分散デバイスを含む管理ハブまたはサーバーで使用できます。 軽量 {{site.data.keyword.ieam}} エージェントをエッジ・デバイスにインストールする方法について詳しくは、以下のセクションを参照してください。

* [エッジ・デバイスの準備](../installing/adding_devices.md)
* [エージェントのインストール](../installing/registration.md)
* [エージェントの更新](../installing/updating_the_agent.md)

すべてのエッジ・デバイス (エッジ・ノード) で {{site.data.keyword.horizon_agent}} ・ソフトウェアがインストールされている必要があります。 さらに、{{site.data.keyword.horizon_agent}} は、[Docker ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://www.docker.com/) ソフトウェアに依存しています。 

以下の図は、エッジ・デバイスに焦点が合わせてあり、エッジ・デバイスをセットアップする際に実行するステップのフローと、開始後にエージェントが実行する処理を示しています。

<img src="../../images/edge/05a_Installing_edge_agent_on_device.svg" width="80%" alt="{{site.data.keyword.horizon_exchange}}、agbot、およびエージェント">
