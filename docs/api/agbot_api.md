---

copyright:
years: 2020 - 2022
lastupdated: "2022-03-17"
title: Agent API
description: An Agreement Bot API is a REST API which uses agreements with edge nodes to run edge services to fulfill the patterns and deployment policies specified.
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# {{site.data.keyword.agbot}} API
{: #agbot_api}

In {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}), the {{site.data.keyword.horizon}} {{site.data.keyword.agbot}} software runs automatically. Each {{site.data.keyword.agbot}} is responsible for communicating with all of the agents that are registered to run services by negotiating agreements with the agents. The `hzn agbot` commands interact with these REST APIs. These APIs are not remotely accessible; they can only be used by processes running on the same host as the {{site.data.keyword.agbot}}.

For more information, see [{{site.data.keyword.horizon}} Agreement Bot APIs](https://github.com/open-horizon/anax/blob/master/docs/agreement_bot_api.md).

{{site.data.keyword.horizon_exchange}} also exposes {{site.data.keyword.agbot}} configuration REST APIs, which are accessed by the `hzn exchange agbot` command.
