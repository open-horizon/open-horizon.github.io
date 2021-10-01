---

copyright:
years: 2020
lastupdated: "2020-05-11"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# {{site.data.keyword.edge_notm}} の概要
{: #overviewofedge}

このセクションでは、{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) の概要を示します。

## {{site.data.keyword.ieam}} の機能
{: #capabilities}

{{site.data.keyword.ieam}} は、管理ハブ・クラスターから OpenShift Container Platform またはその他の Kubernetes ベースのクラスターのエッジ・デバイスおよびリモート・インスタンスへのワークロードのデプロイと管理に役立つ、エッジコンピューティング機能を提供します。

## アーキテクチャー

エッジコンピューティングの目的は、ハイブリッド・クラウド・コンピューティング用に作成された分野を利用して、エッジコンピューティング設備のリモート・オペレーションをサポートすることです。 {{site.data.keyword.ieam}} はその目的のために設計されています。

{{site.data.keyword.ieam}} のデプロイメントには、データ・センターにインストールされている OpenShift Container Platform のインスタンスで実行される管理ハブが含まれています。 管理ハブは、すべてのリモート・エッジ・ノード (エッジ・デバイスおよびエッジ・クラスター) の管理が行われる場所です。

これらのエッジ・ノードをリモートのオンプレミス・ロケーションにインストールすることで、工場、倉庫、小売店、流通センターなど、重要なビジネス・オペレーションが物理的に実施される場所にアプリケーション・ワークロードをローカルに配置できます。

次の図は、標準的なエッジコンピューティング・セットアップのトポロジーの概要を示しています。

<img src="../OH/docs/images/edge/01_OH_overview.svg" style="margin: 3%" alt="IEAM 概要">

{{site.data.keyword.ieam}} 管理ハブは、デプロイメント・リスクを最小化し、エッジ・ノードのサービス・ソフトウェア・ライフサイクルを完全に自律的に管理するために、エッジ・ノード管理専用に設計されています。 クラウド・インストーラーが、{{site.data.keyword.ieam}} 管理ハブ・コンポーネントをインストールおよび管理します。 ソフトウェア開発者がエッジ・サービスを開発し、管理ハブに公開します。 管理者が、エッジ・サービスがデプロイされる場所を制御するデプロイメント・ポリシーを定義します。 {{site.data.keyword.ieam}} がその他のすべてを処理します。

# コンポーネント
{: #components}

{{site.data.keyword.ieam}} にバンドルされているコンポーネントについて詳しくは、『[コンポーネント](components.md)』を参照してください。

## 次の作業

{{site.data.keyword.ieam}} の使用およびエッジ・サービスの開発について詳しくは、{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) [ウェルカム・ページ](../kc_welcome_containers.html)にリストされているトピックを参照してください。
