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

在 {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) 中，{{site.data.keyword.horizon}} agbot 软件自动运行。 每个 agbot 负责与所有用于运行分配给该 agbot 的部署模式（包括该模式的任何服务）的注册代理程序通信。 agbot
与代理程序协商协议。 利用 agbot REST API，您可使用 `http://localhost:8046`
来配置 agbot。 `hzn agbot` 命令与这些 REST API 交互。

有关更多信息，请参阅 [{{site.data.keyword.horizon}} Agreement Bot APIs ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon/anax/blob/master/docs/agreement_bot_api.md)。

{{site.data.keyword.horizon_exchange}} 还会公开 agbot 配置 REST API，这些 API 可供 `hzn exchange agbot` 命令访问。
