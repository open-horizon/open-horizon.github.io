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

# Agbot API
{: #agbot_api}

In {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}), the {{site.data.keyword.horizon}} agbot software runs automatically. Each agbot is responsible for communicating with all of the agents that are registered to run services by negotiating agreements with the agents. The `hzn agbot` commands interact with these REST APIs. These APIs are not remotely accessible; they can only be used by processes running on the same host as the agbot.

For more information, see [{{site.data.keyword.horizon}} Agreement Bot APIs](https://github.com/open-horizon/anax/blob/master/docs/agreement_bot_api.md).

{{site.data.keyword.horizon_exchange}} also exposes agbot configuration REST APIs, which are accessed by the `hzn exchange agbot` command.
