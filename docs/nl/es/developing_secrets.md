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

# Hello world con un secreto
{: #secrets}

En este ejemplo, se muestra cómo desarrollar un {{site.data.keyword.edge_service}} que utilice secretos. Los secretos garantizan que se mantengan seguras las credenciales de inicio de sesión y otra información confidencial.
{:shortdesc}

## Antes de empezar
{: #secrets_begin}

Complete los pasos de requisito previo en [Preparación para crear un servicio periférico](service_containers.md). Como resultado, estas variables de entorno se deben establecer, estos mandatos deben estar instalados y estos archivos deben existir.

```bash
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID" which git jq make ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem cat /etc/default/horizon
```

## Procedimiento
{: #secrets_procedure}

Este ejemplo forma parte del proyecto de código abierto de [{{site.data.keyword.horizon_open}}](https://github.com/open-horizon/). Siga los pasos de [Creating Your Own Hello MMS Edge Service](https://github.com/open-horizon/examples/blob/master/edge/services/helloSecretWorld/CreateService.md) y, a continuación, vuelva aquí.

## Qué hacer a continuación
{: #secrets_what_next}

* Pruebe los otros ejemplos de servicio periférico en [Desarrollo de un servicio periférico para dispositivos](developing.md).

## Lectura adicional

* [Utilización de secretos](../developing/secrets_details.md)
