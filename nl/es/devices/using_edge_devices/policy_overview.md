---

copyright:
years: 2020
lastupdated: "2020-4-24"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Visión general de política
{: #policy_overview}

Añada un gráfico que muestre las partes implicadas en la política (por ej. política de nodo, servicio y negocio,
restricciones, propiedades). 

En esta sección se describen los conceptos de política. 

Para obtener una visión general más completa de varios componentes del sistema, consulte
[Visión general del funcionamiento de IBM Edge Application Manager for
Devices](../getting_started/overview.md). Para obtener un ejemplo práctico de política, consulte
[Hello world](../getting_started/policy.md).

Debido a que un administrador no puede gestionar simultáneamente miles de nodos periféricos, al llegar a decenas de miles o más se crea una situación imposible. Para llegar a este nivel, {{site.data.keyword.edge_devices_notm}} utiliza políticas para determinar dónde y cuándo se deben desplegar servicios y modelos de aprendizaje automático de forma autónoma. Las políticas son una alternativa a los patrones de despliegue.

Una política se expresa a través de un lenguaje de política flexible que se aplica a los modelos, nodos, servicios y políticas de despliegue. El lenguaje de políticas define los atributos (denominados `propiedades`) y certifica requisitos específicos (denominados `restricciones`). Esto permite a cada componente del sistema proporcionar una entrada al motor de despliegue de {{site.data.keyword.edge_devices_notm}}. Para poder desplegar los servicios, se comprueban las restricciones de las políticas de modelos, nodos, servicios y despliegue para asegurarse de que se cumplen todos los requisitos.

Debido al hecho de que los nodos (donde se despliegan los servicios) pueden expresar requisitos, la política de {{site.data.keyword.edge_devices_notm}} se describe como un sistema de política bidireccional. Los nodos no son esclavos en el sistema de despliegue de políticas de {{site.data.keyword.edge_devices_notm}}. Como resultado, las políticas proporcionan un control más preciso sobre el despliegue de servicios y modelos que los patrones. Cuando la política está en uso, {{site.data.keyword.edge_devices_notm}} busca nodos en los que puede desplegar un servicio determinado y analiza los nodos existentes para asegurarse de que siguen siendo conformes (están dentro de la política). Un nodo está dentro de la política cuando las políticas de nodo, servicio y despliegue que originalmente desplegaron el servicio siguen en vigor o cuando los cambios en una de esas políticas no afectan a la compatibilidad de política. El uso de una política proporciona una mayor separación de las preocupaciones, lo que permite a los propietarios de nodos periféricos, desarrolladores de servicio y propietarios de negocio articular su propias políticas de forma independiente.

Hay cuatro tipos de política:

* Nodo
* Servicio
* Despliegue
* Modelo
