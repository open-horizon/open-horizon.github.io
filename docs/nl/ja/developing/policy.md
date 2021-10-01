---

copyright:
  years: 2019, 2020
lastupdated: "2020-2-06"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Hello world
{: #policy}

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) は、ポリシーを使用して、サービスおよびモデルのデプロイメントを確立し、管理します。 これにより、多数のエッジ・ノードを処理する作業を行うのに必要な柔軟性と拡張性が管理者に提供されます。 {{site.data.keyword.ieam}} ポリシーは、デプロイメント・パターンに代わるものです。 このポリシーによって、関心事の分離がより適切になり、エッジ・ノード所有者、サービス・コード開発者、およびビジネス所有者が個別にポリシーを明確に表現できるようになります。

これは、{{site.data.keyword.edge_notm}} デプロイメント・ポリシーを紹介する最小限の "Hello, world" サンプルです。

Horizon ポリシーのタイプ:

* ノード・ポリシー (登録時にノード所有者により提供されます)
* サービス・ポリシー (Exchange に公開されたサービスに適用できます)
* デプロイメント・ポリシー (ビジネス・ポリシーと呼ばれることもあり、ほぼデプロイメント・パターンに相当します)

ポリシーを使用すると、エッジ・ノード上の Horizon Agent と Horizon AgBot との間の合意の定義をより詳細に制御できるようになります。

## ポリシーを使用した Hello World サンプルの実行
{: #helloworld_policy}

[デプロイメント・ポリシーを使用した Hello World サンプル・エッジ・サービスの使用](https://github.com/open-horizon/examples/blob/master/edge/services/helloworld/PolicyRegister.md#using-the-hello-world-example-edge-service-with-deployment-policy) を参照してください。

## 関連情報

* [エッジ・サービスのデプロイ](../using_edge_services/detailed_policy.md)
* [デプロイメント・ポリシーのユース・ケース](../using_edge_services/policy_user_cases.md)
