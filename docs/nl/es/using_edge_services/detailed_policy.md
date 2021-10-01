---

copyright:
years: 2019, 2020
lastupdated: "2020-01-22"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Despliegue de servicios periféricos
{: #detailed_deployment_policy}

Puede desplegar políticas de {{site.data.keyword.edge_notm}} {{site.data.keyword.ieam}} utilizando políticas o patrones. Para obtener una visión general más completa de diversos componentes de sistema, consulte [Visión general de {{site.data.keyword.edge}}](../getting_started/overview_ieam.md) y [Casos de uso de política de despliegue](policy_user_cases.md). Para obtener un ejemplo práctico de política, consulte [Proceso CI-CD para servicios periféricos](../developing/cicd_process.md).

Nota: también puede crear y gestionar políticas de despliegue o patrones desde la consola de gestión. Consulte
[Utilización de la consola de gestión](../console/accessing_ui.md).

En esta sección se describen conceptos de política y patrones e incluye un escenario de caso de uso.

Debido a que un administrador no puede gestionar simultáneamente miles de nodos periféricos, al llegar a decenas de miles o más se crea una situación imposible. Para llegar a este nivel, {{site.data.keyword.edge_notm}} utiliza políticas para determinar dónde y cuándo se deben desplegar servicios y modelos de aprendizaje automático de forma autónoma. 

Una política se expresa a través de un lenguaje de política flexible que se aplica a los modelos, nodos, servicios y políticas de despliegue. El lenguaje de políticas define los atributos (denominados `propiedades`) y certifica requisitos específicos (denominados `restricciones`). Esto permite a cada componente del sistema proporcionar una entrada al motor de despliegue de {{site.data.keyword.edge_notm}}. Para poder desplegar los servicios, se comprueban las restricciones de las políticas de modelos, nodos, servicios y despliegue para asegurarse de que se cumplen todos los requisitos.

Debido al hecho de que los nodos (donde se despliegan los servicios) pueden expresar requisitos, la política de {{site.data.keyword.edge_notm}} se describe como un sistema de política bidireccional. Los nodos no son esclavos en el sistema de despliegue de políticas de {{site.data.keyword.edge_notm}}. Como resultado, las políticas proporcionan un control más preciso sobre el despliegue de servicios y modelos que los patrones. Cuando la política está en uso, {{site.data.keyword.edge_notm}} busca nodos en los que puede desplegar un servicio determinado y analiza los nodos existentes para asegurarse de que siguen siendo conformes (están dentro de la política). Un nodo está dentro de la política cuando las políticas de nodo, servicio y despliegue que originalmente desplegaron el servicio siguen en vigor o cuando los cambios en una de esas políticas no afectan a la compatibilidad de política. El uso de una política proporciona una mayor separación de las preocupaciones, lo que permite a los propietarios de nodos periféricos, desarrolladores de servicio y propietarios de negocio articular su propias políticas de forma independiente.

Las políticas son una alternativa a los patrones de despliegue. Puede publicar patrones en el hub {{site.data.keyword.ieam}} después de que un desarrollador haya publicado un servicio periférico en Horizon Exchange. La CLI de hzn proporciona funciones para listar y gestionar patrones en Horizon Exchange, incluidos los mandatos para listar, publicar, verificar, actualizar y eliminar patrones de despliegue de servicio. También proporciona una forma de listar y eliminar claves criptográficas asociadas con un patrón de despliegue específico.

* [Casos de uso de política de despliegue](policy_user_cases.md)
* [Utilización de patrones](using_patterns.md)
