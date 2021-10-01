---

copyright:
years: 2020
lastupdated: "2020-04-9"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# agbot API
{: #agbot_api}

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) では、{{site.data.keyword.horizon}} agbot ソフトウェアは自動的に実行されます。 各 agbot は、各 agbot に割り当てられたデプロイメント・パターン (パターンのサービスを含む) を実行するように登録されたすべてのエージェントとの通信を担当します。 agbot は、エージェントとの合意をネゴシエーションします。 agbot REST API により、`http://localhost:8046` を使用して agbot を構成できます。 `hzn agbot` コマンドは、これらの REST API と対話します。

詳しくは、[{{site.data.keyword.horizon}} 合意ボット API](https://github.com/open-horizon/anax/blob/master/docs/agreement_bot_api.md) を参照してください。

{{site.data.keyword.horizon_exchange}} で agbot 構成 REST API も公開されています。この REST API には、`hzn exchange agbot` コマンドによってアクセスします。
