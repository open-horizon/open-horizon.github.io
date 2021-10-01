---

copyright:
  years: 2020
lastupdated: "2020-04-9"

---

{:shortdesc: .shortdesc}
{:new_window: target="_blank"}
{:codeblock: .codeblock}
{:pre: .pre}
{:screen: .screen}
{:tip: .tip}
{:download: .download}

# クラスター用エッジ・サービスの開発
{: #developing_clusters}

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) エッジ・クラスター機能は、管理ハブ・クラスターから OpenShift® Container Platform またはその他の Kubernetes ベースのクラスターのリモート・インスタンスへのワークロードのデプロイと管理に役立つ、エッジコンピューティング機能を提供します。 エッジ・クラスターは、Kubernetes クラスターである {{site.data.keyword.ieam}} エッジ・ノードです。 業務運用とコンピュートを同じ場所に配置する必要があるユース・ケースや、1 つのエッジ・デバイスでサポート可能な範囲を超える拡張容易性、可用性、およびコンピュート機能を必要とするユース・ケースが、エッジでエッジ・クラスターによって可能になります。 さらに、エッジ・クラスターは、エッジ・デバイスの近くにあるため、エッジ・デバイスで実行されるサービスをサポートするために必要なアプリケーション・サービスを提供することもよくあり、その場合は結果的に複数層アプリケーションになります。 {{site.data.keyword.ieam}} は、Kubernetes オペレーターを介してエッジ・サービスをエッジ・クラスターにデプロイし、同じ自律的デプロイメント手段がエッジ・デバイスで使用されるようにします。 コンテナー管理プラットフォームとしての Kubernetes のすべての能力が、{{site.data.keyword.ieam}} でデプロイされたエッジ・サービスに利用できます。

<img src="../OH/docs/images/edge/03b_Developing_edge_service_for_cluster.svg" style="margin: 3%" alt="クラスター用エッジ・サービスの開発">

* [Kubernetes オペレーターの開発](service_operators.md)
* [クラスター用の独自の Hello World の作成](creating_hello_world.md)
