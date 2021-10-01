---

copyright:
years: 2019
lastupdated: "2019-06-24"  

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Eigenen Edge-Service ('Hello World') erstellen
{: #dev_start_ex}

Das folgende Beispiel veranschaulicht die Entwicklung für {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) anhand eines einfachen `Hello World`-Service. In diesem Beispiel entwickeln Sie einen einzelnen Edge-Service, der drei Hardwarearchitekturen unterstützt und die Entwicklungstools von {{site.data.keyword.horizon}} verwendet.
{:shortdesc}

## Vorbereitende Schritte
{: #dev_start_ex_begin}

Führen Sie die vorausgesetzten Schritte unter [Erstellung eines Edge-Service vorbereiten](service_containers.md) aus. Danach sollten die folgenden Umgebungsvariablen definiert, die folgenden Befehle installiert und die folgenden Dateien vorhanden sein:
```
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID" which git jq make ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem cat /etc/default/horizon
```
{: codeblock}

## Vorgehensweise
{: #dev_start_ex_procedure}

Dieses Beispiel ist Teil des Open-Source-Projekts [{{site.data.keyword.horizon_open}}](https://github.com/open-horizon/). Führen Sie die Schritte im Abschnitt [Erstellen und Veröffentlichen Ihres eigenen Beispiel-Edge-Services "Hello World"](https://github.com/open-horizon/examples/blob/master/edge/services/helloworld/CreateService.md#build-publish-your-hw) aus und kehren Sie dann hierher zurück.

## Nächste Schritte
{: #dev_start_ex_what_next}

* Versuchen Sie die anderen Edge-Service-Beispiele unter [Edge-Service für Geräte entwickeln}](../OH/docs/developing/developing.md).
