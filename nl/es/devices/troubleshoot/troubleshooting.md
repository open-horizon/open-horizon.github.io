---

copyright:
years: 2019
lastupdated: "2019-06-25"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Resolución de problemas
{: #troubleshooting}

Revise las sugerencias de resolución de problemas y los problemas comunes que se pueden producir con
{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) para ayudarle a resolver
cualquier problema que encuentre. {:shortdesc}

Las guías de resolución de problemas siguientes describen los componentes principales de un sistema {{site.data.keyword.ieam}} y cómo investigar las interfaces incluidas para determinar el estado del sistema.

## Herramientas de resolución de problemas
{: #ts_tools}

Muchas interfaces que se incluyen con {{site.data.keyword.ieam}} proporcionan información que puede utilizarse para diagnosticar problemas. Esta información está disponible a través de la {{site.data.keyword.gui}}, las API REST HTTP y una herramienta de shell de {{site.data.keyword.linux_notm}}, `hzn`.

En una máquina periférica, es posible que tenga que resolver problemas de host, del software de Horizon, de Docker o de la configuración o el código de los contenedores de servicios. Los problemas de host de la máquina periférica están más allá del ámbito de este documento. Si tiene que resolver problemas de Docker, hay muchos mandatos e interfaces de Docker que puede utilizar. Para obtener más información, consulte la documentación de Docker.

Si los contenedores de servicios que está ejecutando utilizan {{site.data.keyword.message_hub_notm}} (que se basa en Kafka) para la mensajería, puede conectarse manualmente a las corrientes de Kafka para {{site.data.keyword.ieam}} para diagnosticar problemas. Puede suscribirse a un tema de mensaje para observar lo que ha recibido {{site.data.keyword.message_hub_notm}}, o bien puede publicar en un tema de mensaje para simular mensajes de otro dispositivo. El mandato `kafkacat`{{site.data.keyword.linux_notm}} es una manera fácil de publicar o suscribirse a {{site.data.keyword.message_hub_notm}}. Utilice la versión más reciente de esta herramienta. {{site.data.keyword.message_hub_notm}} también proporciona páginas web gráficas que puede utilizar para acceder a alguna información.

En cualquier máquina en la que se haya instalado {{site.data.keyword.horizon}}, utilice el mandato `hzn` para depurar problemas del agente {{site.data.keyword.horizon}} local y el {{site.data.keyword.horizon_exchange}} remoto. Internamente, el mandato `hzn` interactúa con las API REST de HTTP suministradas. El mandato `hzn` simplifica el acceso y proporciona una mejor experiencia de usuario que las propias API REST. El mandato `hzn` a menudo proporciona un texto más descriptivo en su salida, e incluye un sistema de ayuda en línea incorporado. Utilice el sistema de ayuda para obtener información y detalles acerca de los mandatos que se deben utilizar y detalles sobre la sintaxis y los argumentos del mandato. Para ver esta información de ayuda, ejecute los mandatos `hzn --help` o `hzn \<submandato\> --help`.

En los nodos en los que los paquetes de {{site.data.keyword.horizon}} no están soportados o instalados, puede interactuar directamente con las API REST HTTP subyacentes. Por ejemplo, puede utilizar el programa de utilidad `curl` u otros programas de utilidad de CLI de API REST. También puede escribir un programa en un lenguaje que dé soporte a consultas REST. 

## Sugerencias para la resolución de problemas
{: #ts_tips}

Para ayudarle a resolver problemas específicos, consulte las preguntas sobre el estado del sistema y cualesquiera sugerencias asociadas acerca de los temas siguientes. Para cada pregunta se proporciona una descripción de la relevancia de la pregunta para la resolución de problemas del sistema. Para algunas preguntas se proporcionan sugerencias o una guía detallada para aprender a obtener la información relacionada del sistema.

Estas preguntas se basan en la naturaleza de la depuración de problemas y están relacionadas con distintos entornos. Por ejemplo, cuando se resuelven problemas en un nodo periférico, es posible que necesite acceso y control completos sobre el nodo, lo que puede aumentar su más capacidad para recopilar y ver información.

* [Sugerencias para la resolución de problemas](troubleshooting_devices.md)

  Revise los problemas comunes que puede encontrar al utilizar {{site.data.keyword.ieam}}.
