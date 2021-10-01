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

# Agbot-API
{: #agbot_api}

In {{site.data.keyword.edge_notm}} ({{site.data.keyword.edge_ieam}}) wird die Software des {{site.data.keyword.horizon}}-Agbots (Agreement Bot; Vereinbarungsbot) automatisch ausgeführt. Jeder Agbot ist für die Kommunikation mit allen Agenten verantwortlich, die zur Ausführung des zugewiesenen Bereitstellungsmusters für den Agbot registriert wurden (einschließlich aller Services für das Muster). Die Agbots verhandeln mit den Agenten über Vereinbarungen. Mit den REST-APIs des Agbots können Sie den Agbot über die Adresse `http://localhost:8046` konfigurieren. Die `hzn agbot`-Befehle dienen zur Interaktion mit diesen REST-APIs.

Weitere Einzelheiten hierzu finden Sie in den Informationen zur [REST-API des {{site.data.keyword.horizon}}-Agbots ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://github.com/open-horizon/anax/blob/master/doc/agreement_bot_api.md).

{{site.data.keyword.horizon_exchange}} stellt auch REST-APIs für die Agbot-Konfiguration bereit, auf die mit dem Befehl `hzn exchange agbot` zugegriffen werden kann.
