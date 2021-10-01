---

copyright:
  years: 2020
lastupdated: "2020-05-9"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# エッジ・クラスター・サービス
{: #Edge_cluster_service}

一般に、エッジ・クラスター内で実行されるサービスの開発は、エッジ・デバイス上で実行されるエッジ・サービスの開発に似ていますが、エッジ・デバイスがどのようにデプロイされるのかに違いがあります。 コンテナー化されたエッジ・サービスをエッジ・クラスターにデプロイするために、開発者はまず、コンテナー化されたエッジ・サービスを Kubernetes クラスターにデプロイする Kubernetes オペレーターを作成する必要があります。 オペレーターが記述されてテストされた後、開発者はそのオペレーターを {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) サービスとして作成して公開します。 オペレーター・サービスは、どの {{site.data.keyword.edge_notm}} サービスでもそうであるように、ポリシーまたはパターンを使用してエッジ・クラスターにデプロイできます。

{{site.data.keyword.ieam}} Exchange には、`hello-operator` というサービスが含まれています。このサービスは、`curl` コマンドを使用して外部からアクセス可能なポートをエッジ・クラスターで公開できるようにします。 このサンプル・サービスをエッジ・クラスターにデプロイするには、[Horizon Operator Example Edge Service](https://github.com/open-horizon/examples/tree/v2.27/edge/services/hello-operator#-using-the-operator-example-edge-service-with-deployment-policy) を参照してください。
