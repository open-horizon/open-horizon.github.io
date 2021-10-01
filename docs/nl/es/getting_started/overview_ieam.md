---

copyright:
years: 2020
lastupdated: "2020-05-11"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Visión general de {{site.data.keyword.edge_notm}}
{: #overviewofedge}

Esta sección proporciona una visión general de {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}).

## Prestaciones de {{site.data.keyword.ieam}}
{: #capabilities}

{{site.data.keyword.ieam}} proporciona características de cálculo periférico para ayudarle a gestionar y desplegar cargas de trabajo de un clúster de centro de gestión a dispositivos periféricos e instancias remotas de OpenShift Container Platform u otros clústeres basados en Kubernetes.

## Arquitectura

El objetivo de Edge Computing es aprovechar las disciplinas que se han creado para Cloud Computing híbrido para dar soporte a operaciones remotas de instalaciones de Edge Computing. {{site.data.keyword.ieam}} está diseñado para ese fin.

El despliegue de {{site.data.keyword.ieam}} incluye el centro de gestión que se ejecuta en una instancia de OpenShift Container Platform instalada en el centro de datos. El centro de gestión es el lugar donde se produce la gestión de todos los nodos periféricos remotos (dispositivos periféricos y clústeres periféricos).

Estos nodos periféricos se pueden instalar en ubicaciones locales remotas para que las cargas de trabajo de aplicación sean locales en el lugar donde se producen físicamente las operaciones de negocio críticas, como por ejemplo en las fábricas, los almacenes, los puntos de venta al por menor, los centros de distribución y más.

El diagrama siguiente muestra la topología de alto nivel de una configuración de computación periférica típica:

<img src="../OH/docs/images/edge/01_OH_overview.svg" style="margin: 3%" alt="IEAM overview">

El centro de gestión de {{site.data.keyword.ieam}} está específicamente diseñado para que la gestión de nodos periféricos minimice los riesgos de despliegue y gestione el ciclo de vida del software de servicio en los nodos periféricos de forma totalmente autónoma. Un instalador de Cloud instala y gestiona los componentes de centro de gestión de {{site.data.keyword.ieam}}. Los desarrolladores de software desarrollan y publican servicios periféricos en el centro de gestión. Los administradores definen las políticas de despliegue que controlan dónde se despliegan los servicios periféricos. {{site.data.keyword.ieam}} maneja todo lo demás.

# Componentes
{: #components}

Para obtener más información sobre los componentes que vienen empaquetados con {{site.data.keyword.ieam}}, consulte [Componentes](components.md).

## Qué hacer a continuación

Para obtener más información sobre la utilización de {{site.data.keyword.ieam}} y el desarrollo de servicios periféricos, revise los temas que se listan en la [Página de bienvenida](../kc_welcome_containers.html) de {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}).
