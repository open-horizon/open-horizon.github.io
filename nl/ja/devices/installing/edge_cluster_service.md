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

一般に、エッジ・クラスター内で実行されるサービスの開発は、エッジ・デバイス上で実行されるエッジ・サービスの開発に似ていますが、エッジ・デバイスがどのようにデプロイされるのかに違いがあります。コンテナー化されたエッジ・サービスをエッジ・クラスターにデプロイするために、開発者はまず、コンテナー化されたエッジ・サービスを Kubernetes クラスターにデプロイする Kubernetes オペレーターを作成する必要があります。 オペレーターが記述されてテストされた後、開発者はそのオペレーターを IBM Edge Application Manager (IEAM) サービスとして作成して公開します。 このプロセスによって、IEAM 管理者は、あらゆる IEAM サービスに行われるのと同様に、ポリシーやパターンとともに、このオペレーター・サービスをデプロイできるようになります。

コンテナー化されたサービス `helloworld` をクラスター上で実行するために、デプロイメント・ポリシーを使用して既に IEAM Exchange 内に公開されている `ibm.operator` を使用するには、[Horizon Operator Example Edge Service ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://github.com/open-horizon/examples/tree/master/edge/services/operator#horizon-operator-example-edge-service) を参照してください。
