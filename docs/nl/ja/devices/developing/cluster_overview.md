---

copyright:
  years: 2020
lastupdated: "2020-04-27"

---

{:shortdesc: .shortdesc}
{:new_window: target="_blank"}
{:codeblock: .codeblock}
{:pre: .pre}
{:screen: .screen}
{:tip: .tip}
{:download: .download}

# クラスター用のエッジ・サービスの概要
{: #cluster_deployment}

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) エッジ・クラスター機能は、ハブ・クラスターから OpenShift® Container Platform 4.2 またはその他の Kubernetes ベースのクラスターのリモート・インスタンスへのワークロードのデプロイと管理に役立つ、エッジ・コンピューティング機能を提供します。 エッジ・クラスターとは、Kubernetes クラスターとしてデプロイされた {{site.data.keyword.ieam}} エッジ・ノードです。 エッジで、業務運用とコンピュートを同じ場所に配置する必要があるユース・ケースや、1 つのエッジ・デバイスでサポート可能な範囲を超える拡張容易性およびコンピュート機能を必要とするユース・ケースが、エッジ・クラスターにより可能になります。 さらに、エッジ・クラスターは、エッジ・デバイスの近くにあるために、エッジ・デバイスで実行されるサービスのサポートに必要なアプリケーション・サービスを提供することもよくあります。 {{site.data.keyword.ieam}} は、Kubernetes オペレーターを介してエッジ・サービスをエッジ・クラスターにデプロイし、同じ自律的デプロイメント手段がエッジ・デバイスで使用されるようにします。 コンテナー管理プラットフォームとしての Kubernetes のすべての能力が、{{site.data.keyword.ieam}} でデプロイされたエッジ・サービスに利用できます。

オプションで IBM Cloud Pak for Multicloud Management を使用して、{{site.data.keyword.ieam}} によってデプロイされたエッジ・サービスに対しても、より深いレベルでのエッジ・クラスターの Kubernetes 固有の管理を提供できます。

ハイレベルのインストールおよび構成ステップにおけるエッジ・ノード (デバイスとクラスターも) を示すグラフィックを追加します。
