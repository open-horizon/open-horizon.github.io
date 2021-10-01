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

# エッジ・クラスター
{: #edge_clusters}

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) エッジ・クラスター機能は、管理ハブ・クラスターから OpenShift® Container Platform またはその他の Kubernetes ベースのクラスターのリモート・インスタンスへのワークロードのデプロイと管理に役立ちます。 エッジ・クラスターは、Kubernetes クラスターである {{site.data.keyword.ieam}} エッジ・ノードです。 業務運用とコンピュートを同じ場所に配置する必要があるユース・ケースや、1 つのエッジ・デバイスでサポート可能な範囲を超える拡張容易性、可用性、およびコンピュート機能を必要とするユース・ケースが、エッジでエッジ・クラスターによって可能になります。 さらに、エッジ・クラスターは、エッジ・デバイスの近くにあるために、エッジ・デバイスで実行されるサービスのサポートに必要なアプリケーション・サービスを提供することもよくあります。 {{site.data.keyword.ieam}} は、Kubernetes オペレーターを介してエッジ・サービスをエッジ・クラスターにデプロイし、同じ自律的デプロイメント手段がエッジ・デバイスで使用されるようにします。 コンテナー管理プラットフォームとしての Kubernetes のすべての能力が、{{site.data.keyword.ieam}} でデプロイされたエッジ・サービスに利用できます。

<img src="../OH/docs/images/edge/05b_Installing_edge_agent_on_cluster.svg" style="margin: 3%" alt="{{site.data.keyword.horizon_exchange}}、agbot、およびエージェント">

以下のセクションに、エッジ・クラスターをインストールし、そこに {{site.data.keyword.ieam}} エージェントをインストールする方法が説明されています。

- [エッジ・クラスターの準備](preparing_edge_cluster.md)
- [エージェントのインストール](edge_cluster_agent.md)
{: childlinks}
