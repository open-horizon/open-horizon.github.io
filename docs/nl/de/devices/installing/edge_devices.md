---

copyright:
years: 2020
lastupdated: "2020-4-8"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Edge-Einheiten
{: #edge_devices}

Eine Edge-Einheit bietet einen Einstiegspunkt in zentrale Netze von Unternehmen oder Service-Providern. Beispiele für solche Einheiten sind unter anderem Smartphones, Überwachungskameras oder sogar mit dem Internet verbundene Mikrowellengeräte.

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) steht für Management-Hubs oder Server einschließlich verteilter Einheiten zur Verfügung. Nähere Informationen zur Installation des schlanken {{site.data.keyword.ieam}}-Agenten auf Edge-Einheiten finden Sie in den folgenden Abschnitten:

* [Edge-Einheit vorbereiten](../installing/adding_devices.md)
* [Agent installieren](../installing/registration.md)
* [Agent aktualisieren](../installing/updating_the_agent.md)

Daher muss die {{site.data.keyword.horizon_agent}}-Software  für alle Edge-Einheiten (Edge-Knoten) installiert sein. Der {{site.data.keyword.horizon_agent}} ist darüber hinaus von der [Docker-Software ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://www.docker.com/) abhängig.  

Das folgende Diagramm konzentriert sich auf die Edge-Einheit und zeigt den Ablauf der Schritte zum Einrichten der Edge-Einheit sowie die Funktionen des Agenten nach seinem Start an. 

<img src="../../images/edge/05a_Installing_edge_agent_on_device.svg" width="80%" alt="{{site.data.keyword.horizon_exchange}}, Agbots und Agenten">
