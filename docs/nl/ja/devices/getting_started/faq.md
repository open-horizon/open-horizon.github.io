---

copyright:
years: 2020
lastupdated: "2020-04-21"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# よくあるご質問
{: #faqs}

{{site.data.keyword.edge_devices_notm}} に関する最もよくあるご質問 (FAQ) の回答をご覧ください。
{:shortdesc}

  * [{{site.data.keyword.edge_devices_notm}} ソフトウェアはオープン・ソースですか?](#open_sourced)
  * [{{site.data.keyword.edge_devices_notm}} を使用してどのようにエッジ・サービスを開発およびデプロイできますか?](#dev_dep)
  * [{{site.data.keyword.edge_devices_notm}} ではどのようなエッジ・ノード・ハードウェア・プラットフォームがサポートされますか?](#hw_plat)
  * [{{site.data.keyword.edge_devices_notm}} を使用して、エッジ・ノード上で任意の {{site.data.keyword.linux_notm}} ディストリビューションを実行できますか？](#lin_dist)
  * [{{site.data.keyword.edge_devices_notm}} ではどのプログラミング言語および環境がサポートされますか?](#pro_env)
  * [{{site.data.keyword.edge_devices_notm}} のコンポーネントで提供されている REST API の詳細な資料はありますか?](#rest_doc)
  * [{{site.data.keyword.edge_devices_notm}} は Kubernetes を使用しますか?](#use_kube)
  * [{{site.data.keyword.edge_devices_notm}} は MQTT を使用しますか?](#use_mqtt)
  * [合意の前にエッジ・ノードを登録した後、それに対応するコンテナーが実行を開始するまでに通常はどれくらいの時間がかかりますか？](#agree_run)
  * [{{site.data.keyword.horizon}} ソフトウェア、および {{site.data.keyword.edge_devices_notm}} に関連する他のすべてのソフトウェアまたはデータは、エッジ・ノード・ホストから削除できますか?](#sw_rem)
  * [エッジ・ノードでアクティブな合意およびサービスを視覚化するダッシュボードはありますか?](#db_node)
  * [コンテナー・イメージのダウンロードがネットワーク障害で中断された場合、どうなりますか?](#image_download)
  * [IEAM がセキュアである仕組みはどのようなものですか?](#ieam_secure)
  * [クラウド上のモデルと AI でエッジにある AI をどのように管理するのですか?](#ai_cloud)

## {{site.data.keyword.edge_devices_notm}} ソフトウェアはオープン・ソースですか?
{: #open_sourced}

{{site.data.keyword.edge_devices_notm}} は IBM 製品です。 しかし、その中核コンポーネントは、[Open Horizon - EdgeX Project Group ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://wiki.edgexfoundry.org/display/FA/Open+Horizon+-+EdgeX+Project+Group) オープン・ソース・プロジェクトを多用しています。{{site.data.keyword.horizon}} プロジェクトで使用可能な多くのサンプルやサンプル・プログラムが、{{site.data.keyword.edge_devices_notm}} でも動作します。 このプロジェクトについて詳しくは、[Open Horizon - EdgeX Project Group ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://wiki.edgexfoundry.org/display/FA/Open+Horizon+-+EdgeX+Project+Group) を参照してください。

## {{site.data.keyword.edge_devices_notm}} を使用してどのようにエッジ・サービスを開発およびデプロイできますか?
{: #dev_dep}

[エッジ・サービスの使用](../developing/using_edge_services.md)を参照してください。

## {{site.data.keyword.edge_devices_notm}} ではどのようなエッジ・ノード・ハードウェア・プラットフォームがサポートされますか?
{: #hw_plat}

{{site.data.keyword.edge_devices_notm}} では、{{site.data.keyword.horizon}} 用の Debian {{site.data.keyword.linux_notm}} バイナリー・パッケージまたは Docker コンテナーを介して、さまざまなハードウェア・アーキテクチャーがサポートされます。 詳しくは、『[{{site.data.keyword.horizon}} ソフトウェアのインストール](../installing/installing_edge_nodes.md)』を参照してください。

## {{site.data.keyword.edge_devices_notm}} を使用して、エッジ・ノード上で任意の {{site.data.keyword.linux_notm}} ディストリビューションを実行できますか？
{: #lin_dist}

はいとも言えますし、いいえとも言えます。

任意の {{site.data.keyword.linux_notm}} ディストリビューション (Dockerfile `FROM` ステートメントを使用している場合) を Docker コンテナーのベース・イメージとして使用するエッジ・ソフトウェアを開発するには、当該ベースがエッジ・マシン上のホスト {{site.data.keyword.linux_notm}} カーネルで機能する必要があります。 つまり、Docker がエッジ・ホスト上で実行できるディストリビューションであれば、そのディストリビューションをコンテナーに使用することができます。

しかし、ご使用のエッジ・マシンのホスト・オペレーティング・システムは、Docker の最近のバージョンを実行でき、かつ {{site.data.keyword.horizon}} ソフトウェアを実行できる必要があります。 現在、{{site.data.keyword.horizon}} ソフトウェアは、{{site.data.keyword.linux_notm}} を実行するエッジ・マシン用の Debian パッケージとしてのみ提供されています。 Apple Macintosh マシンの場合、Docker コンテナーのバージョンが提供されます。 {{site.data.keyword.horizon}} 開発チームは Apple Macintosh、または {{site.data.keyword.linux_notm}} の Ubuntu または Raspbian ディストリビューションを主に使用しています。

## {{site.data.keyword.edge_devices_notm}} ではどのプログラミング言語および環境がサポートされますか?
{: #pro_env}

{{site.data.keyword.edge_devices_notm}} は、エッジ・ノード上の適切な Docker コンテナーで実行するように構成できる、ほとんどのプログラミング言語およびソフトウェア・ライブラリーをサポートします。

ソフトウェアから特定のハードウェアまたはオペレーティング・システム・サービスにアクセスする必要がある場合、`docker run` 相当の引数を指定してそのアクセスをサポートする必要が生じることがあります。 サポートされている引数は、Docker コンテナー定義ファイルの `deployment` セクション内に指定できます。

## {{site.data.keyword.edge_devices_notm}} のコンポーネントで提供されている REST API の詳細な資料はありますか?
{: #rest_doc}

はい。 詳しくは、『[{{site.data.keyword.edge_devices_notm}} API](../installing/edge_rest_apis.md)』を参照してください。 

## {{site.data.keyword.edge_devices_notm}} は Kubernetes を使用しますか?
{: #use_kube}

はい。 {{site.data.keyword.edge_devices_notm}} は [{{site.data.keyword.open_shift_cp}} ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://docs.openshift.com/container-platform/4.4/welcome/index.html) kubernetes サービスを使用します。

## {{site.data.keyword.edge_devices_notm}} は MQTT を使用しますか?
{: #use_mqtt}

{{site.data.keyword.edge_devices_notm}} は、その内部機能をサポートするために Message Queuing Telemetry Transport (MQTT) を使用しませんが、エッジ・マシンにデプロイするプログラムでは、独自の目的で MQTT を使用することができます。 MQTT および他のテクノロジー (例えば、Apache Kafka に基づく {{site.data.keyword.message_hub_notm}}) を使用してエッジ・マシンとの間でデータをトランスポートするサンプル・プログラムを使用できます。

## 合意の前にエッジ・ノードを登録した後、それに対応するコンテナーが実行を開始するまでに通常はどれくらいの時間がかかりますか？
{: #agree_run}

通常は、登録の後、エージェントとリモート agbot がソフトウェアのデプロイに関する合意を確定するまで数秒間しかかかりません。 その後、{{site.data.keyword.horizon}} エージェントが、コンテナーをエッジ・マシンにダウンロードし (`docker pull`)、{{site.data.keyword.horizon_exchange}} でそれらの暗号署名を検査し、それらを実行します。 コンテナーのサイズ、およびそれらが起動し機能し始めるまでの時間によっては、エッジ・マシンが完全に作動可能になるまで数秒から数分かかる場合があります。

エッジ・マシンの登録が完了したら、`hzn node list` コマンドを実行して、エッジ・マシン上の {{site.data.keyword.horizon}} の状態を表示できます。 `hzn node list` コマンドで状態が `configured` であると示されたら、{{site.data.keyword.horizon}} agbot はエッジ・マシンを検出して合意の形成を開始できます。

合意の交渉プロセス・フェーズを監視するには、`hzn agreement list` コマンドを使用します。

合意リストが確定した後、`docker ps` コマンドを使用して実行中のコンテナーを表示できます。 ある特定の `<container>` のデプロイメントに関する詳細情報を確認するために、`docker inspect<container>` を実行することもできます。

## {{site.data.keyword.horizon}} ソフトウェア、および {{site.data.keyword.edge_devices_notm}} に関連する他のすべてのソフトウェアまたはデータは、エッジ・ノード・ホストから削除できますか?
{: #sw_rem}

はい。 エッジ・マシンが登録されている場合は、以下を実行してエッジ・マシンを登録抹消します。 
```
hzn unregister -f -r
```
{: codeblock}

エッジ・マシンが登録抹消されたら、インストール済みの {{site.data.keyword.horizon}} ソフトウェアを削除します。
```
sudo apt purge -y bluehorizon horizon horizon-cli
```
{: codeblock}

## エッジ・ノードでアクティブな合意およびサービスを視覚化するダッシュボードはありますか?
{: #db_node}

{{site.data.keyword.edge_devices_notm}} Web UI を使用して、エッジ・ノードおよびサービスを監視できます。

また、`hzn` コマンドを使用して、アクティブな合意およびサービスに関する情報を、エッジ・ノードでローカル {{site.data.keyword.horizon}} エージェント REST API を使用することによって取得することもできます。 以下のコマンドを実行し、API を使用して関連情報を取得します。
```
hzn node list
hzn agreement list
docker ps
```
{: codeblock}

## コンテナー・イメージのダウンロードがネットワーク障害で中断された場合、どうなりますか?
{: #image_download}

コンテナー・イメージのダウンロードには、Docker API が使用されます。 Docker API は、ダウンロードを強制終了した場合、エージェントにエラーを戻します。 その後、エージェントが現行のデプロイメント試行を取り消します。 agbot は、取り消しを検出すると、そのエージェントで新規のデプロイメント試行を開始します。 後続のデプロイメント試行で、Docker API は中止されたところからダウンロードを再開します。 イメージが完全にダウンロードされ、デプロイメントが先に進めるようになるまで、このプロセスは続行します。 Docker バインディング API はイメージ・プルの責任を追い、失敗した場合、契約は解除されます。

## IEAM がセキュアである仕組みはどのようなものですか?
{: #ieam_secure}

* {{site.data.keyword.ieam}} は、プロビジョニング時に {{site.data.keyword.ieam}} 管理ハブと通信する際に、エッジ・デバイスの暗号署名された公開鍵/秘密鍵認証を自動化および使用します。通信は、常にエッジ・デバイスによって開始および制御されます。
* システムはノードおよびサービスの資格情報を保有しています。
* ハッシュ検証を使用したソフトウェア検証および真正性。

[Security at the Edge ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://www.ibm.com/cloud/blog/security-at-the-edge) を参照してください。

## クラウド上のモデルと AI でエッジにある AI をどのように管理するのですか?
{: #ai_cloud}

通常、エッジにある AI は、1 秒未満の待ち時間で即座にマシン推論を実行することを可能にし、それによって、ユース・ケースおよびハードウェア (例えば、RaspberryPi、Intel x86、Nvidia Jetson nano) に基づくリアルタイム応答が可能になります。{{site.data.keyword.ieam}} モデル管理システムは、更新された AI モデルをサービス・ダウン時間なしでデプロイすることを可能にします。

[Models Deployed at the Edge ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://www.ibm.com/cloud/blog/models-deployed-at-the-edge) を参照してください。
