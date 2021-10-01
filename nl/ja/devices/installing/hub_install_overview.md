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

# 管理ハブの概要
{: #hub_install_overview}
 
IBM Edge Application Manager (IEAM) ノードのタスクに進む前に、管理ハブをインストールして構成する必要があります。

IEAM が提供するエッジ・コンピューティング機能は、ハブ・クラスターから OpenShift® Container Platform 4.3 またはその他の Kubernetes ベース・クラスターのリモート・インスタンスへのワークロードの管理とデプロイに役立ちます。

IEAM は、IBM Multicloud Management Core 1.2 を使用して、エッジ・サーバー、ゲートウェイ、およびリモート・ロケーションの OpenShift® Container Platform 4.3 クラスターによってホストされるデバイスに対する、コンテナー化されたワークロードのデプロイメントを制御します。

さらに、IEAM には、edge computing manager プロファイルのサポートも含まれています。 このサポートされるプロファイルを使用すると、リモート・エッジ・サーバーのホスティングに使用するために OpenShift® Container Platform 4.3 をインストールした場合、OpenShift® Container Platform 4.3 のリソース使用量を減らすことができます。 このプロファイルは、これらのサーバー環境の堅牢なリモート管理、およびそこでホスティングしている企業の基幹業務アプリケーションをサポートするために必要な最小限のサービスを配置します。 このプロファイルを使用して、ユーザーを認証し、ログとイベント・データを収集し、単一のノードまたは一連のクラスター・ワーカー・ノードにワークロードをデプロイすることができます。

Add a graphic showing hub high-level installation and configuration steps. 

## 次の作業

管理ハブのインストール手順については、[管理ハブのインストール](install.md)を参照してください。

## 関連情報

* [エッジ・ノードのインストール](installing_edge_nodes.md)
* [エッジ・クラスター](../developing/edge_clusters.md)
* [エッジ・デバイス](../developing/edge_devices.md)
