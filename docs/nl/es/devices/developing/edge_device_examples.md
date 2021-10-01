---

copyright:
years: 2019
lastupdated: "2019-07-04"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Ejemplos de desarrollo de servicios periféricos
{: #edge_devices_ex}

Para ayudarle a obtener más información sobre cómo desarrollar servicios periféricos para {{site.data.keyword.edge_devices_notm}}, se proporcionan los ejemplos de desarrollo siguientes.
{:shortdesc}

## Ejemplos
{: #edge_devices_ex_examples}

Cada uno de estos ejemplos de desarrollo demuestra algunos aspectos adicionales del desarrollo de servicio de periféricos. Para obtener una experiencia de aprendizaje óptima, complete los ejemplos en el orden en el que se enumeran aquí.

* [Empaquetar un contenedor Docker existente como un servicio periférico](quickstart_example.md) - Demuestra el despliegue de una imagen Docker existente como un servicio periférico.

* [Creación de su propio servicio periférico hello world](developingstart_example.md) - Demuestra los conceptos básicos de desarrollo, pruebas, publicación y despliegue de un servicio periférico.

* [CPU en servicio {{site.data.keyword.message_hub_notm}}](cpu_msg_example.md) - Demuestra cómo definir parámetros de configuración del servicio periférico, especificar que el servicio periférico requiere otros servicios periféricos y enviar datos a un servicio de ingestión de datos de nube.

* [Código completo de la radio definida por software](software_defined_radio_ex_full.md) - Un ejemplo completo de una aplicación periférica que accede a los datos del sensor de hardware, realiza una inferencia de IA en
el borde, centraliza los resultados en un servicio de ingestión de nube, realiza más análisis de IA y proporciona una interfaz de usuario para visualizar los resultados.

* [Servicio periférico que utiliza el sistema de gestión de modelos](mms.md) - Demuestra cómo desarrollar un servicio periférico que utiliza el servicio de gestión de modelos. El servicio de gestión de modelos proporciona de forma asíncrona actualizaciones de archivo a los servicios periféricos en nodos periféricos, por ejemplo, para actualizar de forma dinámica un modelo de aprendizaje automático cada que vez que evoluciona.
