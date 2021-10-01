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

# Creación de su propio servicio periférico hello world
{: #dev_start_ex}

El ejemplo siguiente utiliza un servicio `Hello World` simple para ayudarle a obtener más información sobre el desarrollo de {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}). Con este ejemplo, se desarrolla un servicio periférico único que da soporte a tres arquitecturas de hardware y utiliza las herramientas de desarrollo de {{site.data.keyword.horizon}}.
{:shortdesc}

## Antes de empezar
{: #dev_start_ex_begin}

Complete los pasos de requisito previo en [Preparación para crear un servicio periférico](service_containers.md). Como resultado, estas variables de entorno se deben establecer, estos mandatos deben estar instalados y estos archivos deben existir.
```
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID" which git jq make ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem cat /etc/default/horizon
```
{: codeblock}

## Procedimiento
{: #dev_start_ex_procedure}

Este ejemplo forma parte del proyecto de código abierto de [{{site.data.keyword.horizon_open}}](https://github.com/open-horizon/). Siga los pasos de [Creación y publicación de su propio servicio periférico de ejemplo Hello World](https://github.com/open-horizon/examples/blob/master/edge/services/helloworld/CreateService.md#build-publish-your-hw) y, a continuación, vuelva aquí.

## Qué hacer a continuación
{: #dev_start_ex_what_next}

* Pruebe los otros ejemplos de servicio periférico en [Desarrollo de un servicio periférico para dispositivos}](../OH/docs/developing/developing.md).
