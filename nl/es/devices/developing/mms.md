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

# Servicio periférico que utiliza el servicio del sistema de gestión de modelos (MMS)
{: #mms}

Este ejemplo le ayuda a aprender a desarrollar un {{site.data.keyword.edge_service}} que utiliza el sistema de gestión de modelos (MMS). Puede utilizar este sistema para desplegar y actualizar los modelos de aprendizaje automático utilizados por los servicios periféricos que se ejecutan en los nodos periféricos.
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

## Procedimiento
{: #mms_procedure}

Este ejemplo forma parte del proyecto de código abierto de [{{site.data.keyword.horizon_open}} ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://github.com/open-horizon/). Siga los pasos de [Creating Your Own Hello MMS Edge Service ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://github.com/open-horizon/examples/blob/master/edge/services/helloMMS/CreateService.md)) y, a continuación, vuelva aquí.

## Qué hacer a continuación
{: #mms_what_next}

* Pruebe los otros ejemplos de servicio periférico en [Desarrollo de servicios periféricos con {{site.data.keyword.edge_devices_notm}}](developing.md).

## Lectura adicional

* [Sistema de gestión de modelos](model_management_system.md)
