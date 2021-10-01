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

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) に関するよくあるご質問 (FAQ) の回答を以下に示します。
{:shortdesc}

  * [開発のために自己完結型環境を作成する方法はありますか?](#one_click)
  * [{{site.data.keyword.ieam}} ソフトウェアはオープン・ソースですか?](#open_sourced)
  * [どのように {{site.data.keyword.ieam}} を使用してエッジ・サービスを開発およびデプロイできますか?](#dev_dep)
  * [{{site.data.keyword.ieam}} ではどのようなエッジ・ノード・ハードウェア・プラットフォームがサポートされますか?](#hw_plat)
  * [{{site.data.keyword.ieam}} を使用して、エッジ・ノード上で任意の {{site.data.keyword.linux_notm}} ディストリビューションを実行できますか?](#lin_dist)
  * [{{site.data.keyword.ieam}} ではどのプログラミング言語および環境がサポートされますか?](#pro_env)
  * [{{site.data.keyword.ieam}} のコンポーネントで提供されている REST API の詳細な資料はありますか?](#rest_doc)
  * [{{site.data.keyword.ieam}} は Kubernetes を使用しますか?](#use_kube)
  * [{{site.data.keyword.ieam}} は MQTT を使用しますか?](#use_mqtt)
  * [エッジ・ノードを登録してから合意が形成されるまで、また、それに対応するコンテナーが実行を開始するまでに通常はどれくらいの時間がかかりますか？](#agree_run)
  * [{{site.data.keyword.horizon}} ソフトウェア、および {{site.data.keyword.ieam}} に関連する他のすべてのソフトウェアまたはデータは、エッジ・ノード・ホストから削除できますか?](#sw_rem)
  * [エッジ・ノードでアクティブな合意およびサービスを視覚化するダッシュボードはありますか?](#db_node)
  * [コンテナー・イメージのダウンロードがネットワーク障害で中断された場合、どうなりますか?](#image_download)
  * [{{site.data.keyword.ieam}} がセキュアである仕組みはどのようなものですか?](#ieam_secure)
  * [クラウド上のモデルと AI でエッジにある AI をどのように管理するのですか?](#ai_cloud)

## 開発のために自己完結型環境を作成する方法はありますか?
{: #one_click}

開発者用に「オールインワン」インストーラーを使用して、オープンソースの管理ハブ ({{site.data.keyword.ieam}} 管理コンソールなし) をインストールできます。 このオールインワン・インストーラーにより、完全ですが最小限の管理ハブが作成されます。この管理ハブは実動用途には適していません。 また、サンプル・エッジ・ノードも構成されます。 このツールにより、オープンソース・コンポーネントの開発者は、完全な実動用 {{site.data.keyword.ieam}} 管理ハブを構成するために時間をかけず、迅速に開始することができます。 オールインワン・インストーラーについては、『[Open Horizon - Devops](https://github.com/open-horizon/devops/tree/master/mgmt-hub)』を参照してください。

## {{site.data.keyword.ieam}} ソフトウェアはオープン・ソースですか?
{: #open_sourced}

{{site.data.keyword.ieam}} は IBM 製品です。 しかし、その中核コンポーネントは、[Open Horizon - EdgeX Project Group](https://wiki.edgexfoundry.org/display/FA/Open+Horizon+-+EdgeX+Project+Group) オープン・ソース・プロジェクトを多用しています。 {{site.data.keyword.horizon}} プロジェクトで使用可能な多くのサンプルやサンプル・プログラムが、{{site.data.keyword.ieam}} でも動作します。 このプロジェクトについて詳しくは、[Open Horizon - EdgeX Project Group](https://wiki.edgexfoundry.org/display/FA/Open+Horizon+-+EdgeX+Project+Group) を参照してください。

## {{site.data.keyword.ieam}} を使用してどのようにエッジ・サービスを開発およびデプロイできますか?
{: #dev_dep}

[エッジ・サービスの使用](../using_edge_services/using_edge_services.md)を参照してください。

## {{site.data.keyword.ieam}} ではどのようなエッジ・ノード・ハードウェア・プラットフォームがサポートされますか?
{: #hw_plat}

{{site.data.keyword.ieam}} では、{{site.data.keyword.horizon}} 用の Debian {{site.data.keyword.linux_notm}} バイナリー・パッケージまたは Docker コンテナーを介して、さまざまなハードウェア・アーキテクチャーがサポートされます。 詳しくは、『[{{site.data.keyword.horizon}} ソフトウェアのインストール](../installing/installing_edge_nodes.md)』を参照してください。

## {{site.data.keyword.ieam}} を使用して、エッジ・ノード上で任意の {{site.data.keyword.linux_notm}} ディストリビューションを実行できますか?
{: #lin_dist}

はいとも言えますし、いいえとも言えます。

任意の {{site.data.keyword.linux_notm}} ディストリビューション (Dockerfile `FROM` ステートメントを使用している場合) を Docker コンテナーのベース・イメージとして使用するエッジ・ソフトウェアを開発するには、当該ベースがエッジ・ノード上のホスト {{site.data.keyword.linux_notm}} カーネルで機能する必要があります。 つまり、Docker がエッジ・ホスト上で実行できるディストリビューションであれば、そのディストリビューションをコンテナーに使用することができます。

しかし、ご使用のエッジ・ノードのホスト・オペレーティング・システムは、Docker の最近のバージョンを実行でき、かつ {{site.data.keyword.horizon}} ソフトウェアを実行できる必要があります。 現在、{{site.data.keyword.horizon}} ソフトウェアは、{{site.data.keyword.linux_notm}} で実行されるエッジ・ノード用に Debian および RPM パッケージとしてのみ提供されています。 Apple Macintosh マシンの場合、Docker コンテナーのバージョンが提供されます。 {{site.data.keyword.horizon}} 開発チームは Apple Macintosh、または {{site.data.keyword.linux_notm}} の Ubuntu または Raspbian ディストリビューションを主に使用しています。

また、RPM パッケージのインストールは、Red Hat Enterprise Linux (RHEL) バージョン 8.2 を使用して構成されたエッジ・ノードでテストされています。

## {{site.data.keyword.ieam}} ではどのプログラミング言語および環境がサポートされますか?
{: #pro_env}

{{site.data.keyword.ieam}} は、エッジ・ノード上の適切な Docker コンテナーで実行するように構成できる、ほとんどのプログラミング言語およびソフトウェア・ライブラリーをサポートします。

ソフトウェアから特定のハードウェアまたはオペレーティング・システム・サービスにアクセスする必要がある場合、`docker run` 相当の引数を指定してそのアクセスをサポートする必要が生じることがあります。 サポートされている引数は、Docker コンテナー定義ファイルの `deployment` セクション内に指定できます。

## {{site.data.keyword.ieam}} のコンポーネントで提供されている REST API の詳細な資料はありますか?
{: #rest_doc}

はい。 詳しくは、『[{{site.data.keyword.ieam}} API](../api/edge_rest_apis.md)』を参照してください。 

## {{site.data.keyword.ieam}} は Kubernetes を使用しますか?
{: #use_kube}

はい。 {{site.data.keyword.ieam}} は、[{{site.data.keyword.open_shift_cp}})](https://docs.openshift.com/container-platform/4.6/welcome/index.md) Kubernetes サービスを使用します。

## {{site.data.keyword.ieam}} は MQTT を使用しますか?
{: #use_mqtt}

{{site.data.keyword.ieam}} は、その内部機能をサポートするために Message Queuing Telemetry Transport (MQTT) を使用しませんが、エッジ・ノードにデプロイするプログラムでは、独自の目的で MQTT を使用することができます。 MQTT および他のテクノロジー (例えば、Apache Kafka に基づく {{site.data.keyword.message_hub_notm}}) を使用してエッジ・ノードとの間でデータをトランスポートするサンプル・プログラムを使用できます。

## 合意の前にエッジ・ノードを登録した後、それに対応するコンテナーが実行を開始するまでに通常はどれくらいの時間がかかりますか？
{: #agree_run}

通常は、登録の後、エージェントとリモート agbot がソフトウェアのデプロイに関する合意を確定するまで数秒間しかかかりません。 その後、{{site.data.keyword.horizon}} エージェントが、コンテナーをエッジ・ノードにダウンロードし (`docker pull`)、{{site.data.keyword.horizon_exchange}} でそれらの暗号署名を検査し、それらを実行します。 コンテナーのサイズ、およびそれらが開始して機能し始めるまでの時間によって、エッジ・ノードが完全に作動可能になるまで数秒から数分かかる場合があります。

エッジ・ノードの登録が完了したら、`hzn node list` コマンドを実行して、エッジ・ノード上の {{site.data.keyword.horizon}} の状態を表示できます。 `hzn node list` コマンドで状態が `configured` であると示されたら、{{site.data.keyword.horizon}} agbot はエッジ・ノードを検出して合意の形成を開始できます。

合意の交渉プロセス・フェーズを監視するには、`hzn agreement list` コマンドを使用します。

合意リストが確定した後、`docker ps` コマンドを使用して実行中のコンテナーを表示できます。 ある特定の `<container>` のデプロイメントに関する詳細情報を確認するために、`docker inspect<container>` を実行することもできます。

## {{site.data.keyword.horizon}} ソフトウェア、および {{site.data.keyword.ieam}} に関連する他のすべてのソフトウェアまたはデータは、エッジ・ノード・ホストから削除できますか?
{: #sw_rem}

はい。 エッジ・ノードが登録されている場合は、以下を実行してエッジ・ノードを登録抹消します。 
```
hzn unregister -f -r
```
{: codeblock}

エッジ・ノードを登録抹消した場合、インストールされている {{site.data.keyword.horizon}} ソフトウェアを削除できます。例えば、Debian ベースのシステムでは、以下を実行します。
```
sudo apt purge -y bluehorizon horizon horizon-cli
```
{: codeblock}

## エッジ・ノードでアクティブな合意およびサービスを視覚化するダッシュボードはありますか?
{: #db_node}

{{site.data.keyword.ieam}} Web UI を使用して、エッジ・ノードおよびサービスを監視できます。

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

## {{site.data.keyword.ieam}} がセキュアである仕組みはどのようなものですか?
{: #ieam_secure}

* {{site.data.keyword.ieam}} は、プロビジョニング時に {{site.data.keyword.ieam}} 管理ハブと通信する際に、エッジ・デバイスの暗号署名された公開鍵/秘密鍵認証を自動化および使用します。 通信は、常にエッジ・ノードによって開始および制御されます。
* システムはノードおよびサービスの資格情報を保有しています。
* ハッシュ検証を使用したソフトウェア検証および真正性。

[Security at the Edge](https://www.ibm.com/cloud/blog/security-at-the-edge) を参照してください。

## クラウド上のモデルと AI でエッジにある AI をどのように管理するのですか?
{: #ai_cloud}

通常、エッジにある AI は、1 秒未満の待ち時間で即座にマシン推論を実行することを可能にし、それによって、ユース・ケースおよびハードウェア (例えば、RaspberryPi、Intel x86、Nvidia Jetson nano) に基づくリアルタイム応答が可能になります。 {{site.data.keyword.ieam}} モデル管理システムは、更新された AI モデルをサービス・ダウン時間なしでデプロイすることを可能にします。

[Models Deployed at the Edge](https://www.ibm.com/cloud/blog/models-deployed-at-the-edge) を参照してください。
