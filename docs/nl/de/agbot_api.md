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

# Agbot-API
{: #agbot_api}

In {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) wird die Software des {{site.data.keyword.horizon}}-Agbots (Agreement Bot; Vereinbarungsbot) automatisch ausgeführt. Jeder agbot ist für die Kommunikation mit allen Agenten zuständig, die für die Ausführung von Services durch Aushandlung von Vereinbarungen mit den Agenten registriert sind. Die `hzn agbot`-Befehle dienen zur Interaktion mit diesen REST-APIs. Diese APIs sind nicht über Fernzugriff zugänglich; sie können nur von Prozessen verwendet werden, die auf demselben Host wie der agbot ausgeführt werden.

Weitere Informationen finden Sie unter [{{site.data.keyword.horizon}} Agreement-Bot-APIs](https://github.com/open-horizon/anax/blob/master/docs/agreement_bot_api.md).

{{site.data.keyword.horizon_exchange}} stellt auch REST-APIs für die Agbot-Konfiguration bereit, auf die mit dem Befehl `hzn exchange agbot` zugegriffen werden kann.
