---

copyright:
years: 2021 - 2022
lastupdated: "2022-06-03"
title: APIs
description: ""
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# APIs
{: #edge_rest_apis}

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) provides RESTful APIs for enabling components to collaborate, and to enable your organization's developers and users to control the components.
{:shortdesc}

The {{site.data.keyword.ieam}} REST APIs are documented within the {{site.data.keyword.horizon}} project documentation. For more information, see [{{site.data.keyword.horizon}}](https://github.com/open-horizon).

For most users, the `hzn` command line interface (CLI) tool, which calls these APIs, is sufficient for completing most tasks. If you do use this tool, direct use of the API is unnecessary.

* [Agent API](agent_api.md)
* [Agbot API](agbot_api.md)
{% if site.data.keyword.edge_notm == "Open Horizon" %}
* [Agbot User API](../api/agbot_secure_api.html)
* [Exchange API](../api/exchange_swagger.html)
{% else %}
* [Agbot User API](agbot_secure_api.json)
* [Exchange API](exchange_swagger.json)
{% endif %}
* [MMS API](mms_swagger.html)
* [SDO API](sdo_swagger.html)
