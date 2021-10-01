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

# Hello world utilizando la gestión de modelos
{: #model_management_system}

Este ejemplo le ayuda a aprender a desarrollar un {{site.data.keyword.edge_service}} ({{site.data.keyword.ieam}}) que utiliza el sistema de gestión de modelos (MMS). Puede utilizar este sistema para desplegar y actualizar los modelos de aprendizaje automático utilizados por los servicios periféricos que se ejecutan en los nodos periféricos.
{:shortdesc}

## Antes de empezar
{: #mms_begin}

Complete los pasos de requisito previo en [Preparación para crear un servicio periférico](service_containers.md). Como resultado, estas variables de entorno se deben establecer, estos mandatos deben estar instalados y estos archivos deben existir.

```bash
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID"
which git jq make
ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem
cat /etc/default/horizon
```
{: codeblock}

## Procedimiento
{: #mms_procedure}

Este ejemplo forma parte del proyecto de código abierto de [{{site.data.keyword.horizon_open}}](https://github.com/open-horizon/). Siga los pasos de [Creating Your Own Hello MMS Edge Service](https://github.com/open-horizon/examples/blob/master/edge/services/helloMMS/CreateService.md) y, a continuación, vuelva aquí.

## Qué hacer a continuación
{: #mms_what_next}

* Pruebe los otros ejemplos de servicio periférico en [Desarrollo de un servicio periférico para dispositivos](../OH/docs/developing/developing.md).

## Lectura adicional

* [Sistema de gestión de modelos](../OH/docs/developing/model_management_details.md)
