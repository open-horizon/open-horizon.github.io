---

copyright:
years: 2019
lastupdated: "2019-09-04"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# セキュリティー 
{: #security}

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) は、[Open Horizon](https://github.com/open-horizon) に基づいており、複数のセキュリティー・テクノロジーを使用して、攻撃から保護された状態を保ち、プライバシーを保護しています。 {{site.data.keyword.ieam}} のセキュリティーおよび役割について詳しくは、以下を参照してください。

* [セキュリティーおよびプライバシー](../OH/docs/user_management/security_privacy.md)
* [役割ベースのアクセス制御](rbac.md)
* [{{site.data.keyword.edge_notm}}GDPR 対応に向けた考慮事項](gdpr.md)
{: childlinks}

まだ独自の RSA 鍵がない場合にワークロード署名鍵を作成する方法について詳しくは、『[エッジ・サービス作成の準備](../developing/service_containers.md)』を参照してください。 サービスを Exchange に公開する際にこれらの鍵を使用してサービスに署名し、{{site.data.keyword.ieam}} エージェントで有効なワークロードが開始されていることを確認できるようにします。
