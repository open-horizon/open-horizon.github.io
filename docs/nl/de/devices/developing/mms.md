---

copyright:
  years: 2019
lastupdated: "2019-06-24"

---

{:shortdesc: .shortdesc}
{:new_window: target="_blank"}
{:codeblock: .codeblock}
{:pre: .pre}
{:screen: .screen}
{:tip: .tip}
{:download: .download}

# Edge-Service, der den Model Management System-Service (MMS) verwendet
{: #mms}

In diesem Beispiel erfahren Sie, wie Sie einen {{site.data.keyword.edge_service}} entwickeln, der das Model Management System (MMS) verwendet. Sie können dieses System verwenden, um die lernenden Maschinenmodelle bereitzustellen und zu aktualisieren, die von den auf Ihren Edge-Knoten ausgeführten Edge-Services verwendet werden.
{:shortdesc}

## Vorbereitende Schritte
{: #mms_begin}

Führen Sie die vorausgesetzten Schritte wie im Abschnitt [Erstellung eines Edge-Service vorbereiten](service_containers.md) beschrieben aus. Danach sollten die folgenden Umgebungsvariablen definiert, die folgenden Befehle installiert und die folgenden Dateien vorhanden sein: 

```bash
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID"
which git jq make
ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem
cat /etc/default/horizon
```

## Vorgehensweise
{: #mms_procedure}

Dieses Beispiel ist Teil des Open-Source-Projekts [{{site.data.keyword.horizon_open}} ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://github.com/open-horizon/). Führen Sie die Schritte unter [Eigenen 'Hello' MMS-Edge-Service erstellen![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://github.com/open-horizon/examples/blob/master/edge/services/helloMMS/CreateService.md)) aus und kehren Sie hierher zurück.

## Nächste Schritte
{: #mms_what_next}

* Unter [Edge-Services mit {{site.data.keyword.edge_devices_notm}} entwickeln](developing.md) finden Sie weitere Beispiele für Edge-Services, mit denen Sie arbeiten können. 

## Weiterführende Informationen

* [Model Management System](model_management_system.md)
