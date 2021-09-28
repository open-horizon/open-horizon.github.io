---

copyright:
years: 2021
lastupdated: "2021-08-16"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Hallo Welt mit einem geheimen Schlüssel
{: #secrets}

In diesem Beispiel wird beschrieben, wie ein {{site.data.keyword.edge_service}} entwickelt wird, der geheime Schlüssel verwendet. Geheime Schlüssel stellen sicher, dass Anmeldeinformationen und andere sensible Informationen sicher aufbewahrt werden.
{:shortdesc}

## Vorbereitende Schritte
{: #secrets_begin}

Führen Sie die vorausgesetzten Schritte unter [Erstellung eines Edge-Service vorbereiten](service_containers.md) aus. Danach sollten die folgenden Umgebungsvariablen definiert, die folgenden Befehle installiert und die folgenden Dateien vorhanden sein:

```bash
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID" which git jq make ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem cat /etc/default/horizon
```

## Vorgehensweise
{: #secrets_procedure}

Dieses Beispiel ist Teil des Open-Source-Projekts [{{site.data.keyword.horizon_open}}](https://github.com/open-horizon/). Folgen Sie den Schritten im Abschnitt [Eigenen Hallo Secret Service erstellen](https://github.com/open-horizon/examples/blob/master/edge/services/helloSecretWorld/CreateService.md)) und kehren Sie dann hierher zurück.

## Nächste Schritte
{: #secrets_what_next}

* Unter [Edge-Service für Einheiten entwickeln](developing.md) finden Sie weitere Beispiele für Edge-Services, mit denen Sie arbeiten können.

## Weiterführende Informationen

* [Geheime Schlüssel verwenden](../developing/secrets_details.md)
