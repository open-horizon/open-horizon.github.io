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

# agbot API
{: #agbot_api}

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) では、{{site.data.keyword.horizon}} agbot ソフトウェアは自動的に実行されます。 各 agbot は、エージェントと合意についてネゴシエーションすることで、サービスを実行するように登録されたすべてのエージェントとの通信を行ないます。`hzn agbot` コマンドは、これらの REST API と対話します。これらの API はリモートからアクセスすることはできません。API を使用できるのは、agbot と同じホスト上で稼働しているプロセスのみです。

詳しくは、[{{site.data.keyword.horizon}} 合意ボット API](https://github.com/open-horizon/anax/blob/master/docs/agreement_bot_api.md) を参照してください。

{{site.data.keyword.horizon_exchange}} で agbot 構成 REST API も公開されています。この REST API には、`hzn exchange agbot` コマンドによってアクセスします。
