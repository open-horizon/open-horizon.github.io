---

copyright:
years: 2021
lastupdated: "2021-02-20"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# デバイス用のエッジ・サービスの開発
{: #developing}

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) でのエッジ・サービスの開発を開始するには、最初に、コンテンツを公開するための資格情報をセットアップする必要があります。 すべてのサービスは署名済みでなければならないため、暗号署名鍵ペアも作成する必要があります。 [エッジ・サービス作成の準備](service_containers.md)の前提条件ステップを実行してください。

次の図は、{{site.data.keyword.horizon}} 内のコンポーネント間の典型的な相互作用を示しています。

<img src="../images/edge/03a_Developing_edge_service_for_device.svg" style="margin: 3%" alt="エッジ・デバイス"> 

## 例
{: #edge_devices_ex_examples}

資格情報および署名鍵を使用して、開発サンプルを実行します。 これらのサンプルには、単純なサービスの作成方法が示されており、{{site.data.keyword.ieam}} 開発の基本についての理解を深めるのに役立ちます。

これらの各開発サンプルには、エッジ・サービス開発のさらなる側面がいくつか示されています。 最適な学習体験を得るには、ここにリストされている順番でサンプルを実行してください。

* [エッジ・サービスへのイメージの変換](transform_image.md) - 既存の Docker イメージをエッジ・サービスとしてデプロイする方法を示します。

* [独自の Hello World エッジ・サービスの作成](developingstart_example.md) - エッジ・サービスの開発、テスト、公開、およびデプロイの基本を示します。

* [CPU to {{site.data.keyword.message_hub_notm}} サービス](cpu_msg_example.md) - エッジ・サービス構成パラメーターを定義する方法、エッジ・サービスが他のエッジ・サービスを必要とすることを指定する方法、データをクラウド・データ取り込みサービスに送信する方法を示します。

* [モデル管理を使用する Hello World](model_management_system.md) - モデル管理サービスを使用するエッジ・サービスを開発する方法を示します。 モデル管理サービスは、例えば、機械学習モデルが進化するたびに機械学習モデルを動的に更新するため、エッジ・ノード上のエッジ・サービスにファイル更新を非同期的に提供します。

* [シークレットを使用する Hello World](developing_secrets.md) - シークレットを使用するエッジ・サービスを開発する方法を示します。 シークレットは、ログイン資格情報や秘密鍵などの機密データを保護するために使用されます。シークレットは、エッジで稼働中のサービスに安全にデプロイされます。

* [ロールバックによるエッジ・サービスの更新](../using_edge_services/service_rollbacks.md) - デプロイメントが成功したかをモニターして、いずれかのエッジ・ノードで失敗した場合には前のエッジ・サービス・バージョンにノードを戻す方法を示します。

これらのサンプル・サービスの作成を完了した後、以下の資料で、{{site.data.keyword.ieam}} 用のサービスの開発に関する詳しい説明を参照してください。

## 参考文献
{: #developing_more_info}

{{site.data.keyword.ieam}} ソフトウェア開発の重要な原則およびベスト・プラクティスを検討してください。

* [エッジ・ネイティブ開発のベスト・プラクティス](best_practices.md)

{{site.data.keyword.ieam}} では、オプションで、パブリック Docker ハブではなく、IBM のセキュアなプライベート・コンテナー・レジストリーに、サービス・コンテナー・イメージを入れることができます。 例えば、パブリック・レジストリーに入れるのが適切でないアセットが含まれているソフトウェア・イメージがある場合などに使用します。

* [プライベート・コンテナー・レジストリーの使用](container_registry.md)

{{site.data.keyword.ieam}} を使用して、パブリック Docker Hub ではなく、IBM のセキュアなプライベート・コンテナー・レジストリーにサービス・コンテナーを入れることができます。

* [開発の詳細](developing_details.md)

{{site.data.keyword.ieam}} を使用して、エッジ・マシン用の任意のサービス・コンテナーを開発できます。

* [API](../api/edge_rest_apis.md)

{{site.data.keyword.ieam}} は、コンポーネントが連携できるようにするため、および、組織の開発者とユーザーがコンポーネントを制御できるようにするための  RESTful API を提供します。
