---

copyright:
years: 2019, 2020
lastupdated: "2020-02-10"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# コンポーネント

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) には、製品にバンドルされている複数のコンポーネントが含まれています。
{:shortdesc}

{{site.data.keyword.ieam}} コンポーネントの説明については、以下の表を参照してください。

|コンポーネント|バージョン|説明|
|---------|-------|----|
|[IBM Cloud プラットフォーム共通サービス](https://www.ibm.com/docs/en/cpfs)|3.6.x|これは、{{site.data.keyword.ieam}} オペレーターのインストールの一部として自動的にインストールされる一連の基本コンポーネントです。|
|Agbot|{{site.data.keyword.anax_ver}}|合意ボット (agbot) インスタンスは集中的に作成され、ワークロードおよび機械学習モデルを {{site.data.keyword.ieam}} にデプロイする責任を負います。|
|MMS |1.5.3-338|モデル管理システム (MMS) は、エッジ・サービスが必要とする、モデル、データ、およびその他のメタデータ・パッケージの保管、送信、および保護を容易にします。 これにより、エッジ・ノードはクラウドとの間でモデルおよびメタデータの送受信を簡単に行えるようになります。|
|Exchange API|2.87.0-531|Exchange は、{{site.data.keyword.ieam}} の他のすべてのコンポーネントによって使用されるすべての定義 (パターン、ポリシー、サービスなど) を保持する REST API を提供します。|
|管理コンソール|1.5.0-578|{{site.data.keyword.ieam}} の管理者が {{site.data.keyword.ieam}} の他のコンポーネントを表示および管理するために使用する Web UI。|
|セキュア・デバイス・オンボード|1.11.11-441|SDO コンポーネントにより、Intel によって作成されたテクノロジーを使用して、エッジ・デバイスの構成およびエッジ管理ハブとの関連付けを簡単かつセキュアに行うことができます。|
|クラスター・エージェント|{{site.data.keyword.anax_ver}}|これは、{{site.data.keyword.ieam}} によるノード・ワークロード管理を可能にするためにエッジ・クラスターにエージェントとしてインストールされるコンテナー・イメージです。|
|デバイス・エージェント|{{site.data.keyword.anax_ver}}|このコンポーネントは、{{site.data.keyword.ieam}} によるノード・ワークロード管理を可能にするためにエッジ・デバイスにインストールされます。|
|シークレット・マネージャー|1.0.0-168|シークレット・マネージャーは、エッジ・デバイスにデプロイされるシークレットのリポジトリーであり、これにより、サービスはアップストリーム依存関係への認証に使用される資格情報を安全に受け取ることができます。|
