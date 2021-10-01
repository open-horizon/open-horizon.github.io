---

copyright:
  years: 2019, 2020
lastupdated: "2020-2-06"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Hello world
{: #policy}

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) utiliza políticas para establecer y gestionar despliegues de servicio y modelo, lo que ofrece a los administradores la flexibilidad y la escalabilidad necesarias para trabajar con grandes cantidades de nodos periféricos. La política de {{site.data.keyword.ieam}} es una alternativa a los patrones de despliegue. Proporciona una mayor separación de las preocupaciones, lo que permite a los propietarios de nodos periféricos, desarrolladores de código de servicio y propietarios de negocio articular políticas de forma independiente.

Este es un ejemplo "Hello, world" mínimo para presentarle las políticas de despliegue de {{site.data.keyword.edge_notm}}.

Tipos de políticas Horizon:

* Política de nodo (proporcionado en el registro por el propietario del nodo)
* Política de servicio (se puede aplicar a un servicio publicado en Exchange)
* Política de despliegue (también a veces denominada política de negocio, que corresponde aproximadamente a un patrón de despliegue)

Las políticas proporcionan más control sobre la definición de acuerdos entre los agentes Horizon en nodos periféricos y los agbots Horizon.

## Utilización de una política para ejecutar el ejemplo hello world
{: #helloworld_policy}

Consulte [Utilización del servicio periférico del ejemplo Hello World con la política de despliegue](https://github.com/open-horizon/examples/blob/master/edge/services/helloworld/PolicyRegister.md#using-the-hello-world-example-edge-service-with-deployment-policy).

## Información relacionada

* [Despliegue de servicios periféricos](../using_edge_services/detailed_policy.md)
* [Casos de uso de política de despliegue](../using_edge_services/policy_user_cases.md)
