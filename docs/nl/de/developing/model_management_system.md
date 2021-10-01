---

copyright:
years: 2020
lastupdated: "2020-02-6"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 'Hello World' mit Model Management
{: #model_management_system}

In diesem Beispiel erfahren Sie, wie Sie einen {{site.data.keyword.edge_service}} ({{site.data.keyword.ieam}}-Service) entwickeln, der das Model Management System (MMS) verwendet. Sie können dieses System verwenden, um die lernenden Maschinenmodelle bereitzustellen und zu aktualisieren, die von den auf Ihren Edge-Knoten ausgeführten Edge-Services verwendet werden.
{:shortdesc}

## Vorbereitende Schritte
{: #mms_begin}

Führen Sie die vorausgesetzten Schritte unter [Erstellung eines Edge-Service vorbereiten](service_containers.md) aus. Danach sollten die folgenden Umgebungsvariablen definiert, die folgenden Befehle installiert und die folgenden Dateien vorhanden sein:

```bash
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID" which git jq make ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem cat /etc/default/horizon
```
{: codeblock}

## Vorgehensweise
{: #mms_procedure}

Dieses Beispiel ist Teil des Open-Source-Projekts [{{site.data.keyword.horizon_open}}](https://github.com/open-horizon/). Folgen Sie den Schritten im Abschnitt [Eigenen Hello MMS-Edge-Service erstellen](https://github.com/open-horizon/examples/blob/master/edge/services/helloMMS/CreateService.md)) und kehren Sie dann hierher zurück.

## Nächste Schritte
{: #mms_what_next}

* Unter [Edge-Service für Einheiten entwickeln](../OH/docs/developing/developing.md) finden Sie weitere Beispiele für Edge-Services, mit denen Sie arbeiten können.

## Weiterführende Informationen

* [Model Management System](../OH/docs/developing/model_management_details.md)
