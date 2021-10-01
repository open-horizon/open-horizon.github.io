---

copyright:
years: 2020
lastupdated: "2020-4-24"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# クラスター用エッジ・サービスの概要
{: #edge_clusters_overview}

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) エッジ・クラスター機能は、ハブ・クラスターから OpenShift® Container Platform 4.2 またはその他の Kubernetes ベースのクラスターのリモート・インスタンスへのワークロードのデプロイと管理に役立つ、エッジ・コンピューティング機能を提供します。 エッジ・クラスターとは、Kubernetes クラスターとしてデプロイされた {{site.data.keyword.ieam}} エッジ・ノードです。 エッジで、業務運用とコンピュートを同じ場所に配置する必要があるユース・ケースや、1 つのエッジ・デバイスでサポート可能な範囲を超える拡張容易性およびコンピュート機能を必要とするユース・ケースが、エッジ・クラスターにより可能になります。 さらに、エッジ・クラスターは、エッジ・デバイスの近くにあるために、エッジ・デバイスで実行されるサービスのサポートに必要なアプリケーション・サービスを提供することもよくあります。 IEAM は Kubernetes オペレーターを介してエッジ・クラスターにエッジ・サービスをデプロイし、これにより、エッジ・デバイスで使用されるものと同じ自律型デプロイメント・メカニズムが使用可能になります。 コンテナー管理プラットフォームとしての Kubernetes のすべての能力が、{{site.data.keyword.ieam}} でデプロイされたエッジ・サービスに利用できます。

オプションで、IBM Cloud Pak for Multicloud Management を使用して、IEAM でデプロイされたエッジ・サービスにまでも、エッジ・クラスターのさらに高度な Kubernetes 固有の管理を提供することもできます。

Add a graphic showing edge cluster high-level installation and configuration steps. 

## 次の作業

エッジ・クラスターのインストール情報については、[エッジ・クラスター](../developing/edge_clusters.md)を参照してください。

## 関連情報

* [エッジ・ノードのインストール](installing_edge_nodes.md)
* [エッジ・デバイス](../developing/edge_devices.md)
* [エッジ・クラスター](../developing/edge_clusters.md)
