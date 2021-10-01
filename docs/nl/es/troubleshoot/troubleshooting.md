---

copyright:
years: 2020
lastupdated: "2020-10-15"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Sugerencias para la resolución de problemas y preguntas más frecuentes
{: #troubleshooting}

Revise las sugerencias para la resolución de problemas y las preguntas más frecuentes como ayuda para resolver los problemas que pueda encontrar.
{:shortdesc}

* [Sugerencias para la resolución de problemas](troubleshooting_devices.md)
* [Preguntas más frecuentes](../getting_started/faq.md)

El siguiente contenido de resolución de problemas describe los principales componentes de {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) y cómo investigar las interfaces incluidas para determinar el estado del sistema.

## Herramientas de resolución de problemas
{: #ts_tools}

Muchas interfaces que se incluyen con {{site.data.keyword.ieam}} proporcionan información que puede utilizarse para diagnosticar problemas. Esta información está disponible a través de la {{site.data.keyword.gui}}, las API REST HTTP y una herramienta de shell de {{site.data.keyword.linux_notm}}, `hzn`.

En un nodo periférico, es posible que tenga que resolver problemas de host, problemas de software de Horizon, problemas de Docker o problemas en la configuración o el código en los contenedores de servicio. Los problemas de host de nodo periférico están fuera del ámbito de este documento. Si necesita resolver problemas de Docker, puede utilizar muchos mandatos e interfaces de Docker. Para obtener más información, consulte la documentación de Docker.

Si los contenedores de servicios que está ejecutando utilizan {{site.data.keyword.message_hub_notm}} (que se basa en Kafka) para la mensajería, puede conectarse manualmente a las corrientes de Kafka para {{site.data.keyword.ieam}} para diagnosticar problemas. Puede suscribirse a un tema de mensaje para observar lo que ha recibido {{site.data.keyword.message_hub_notm}}, o bien puede publicar en un tema de mensaje para simular mensajes de otro dispositivo. El mandato `kafkacat` de {{site.data.keyword.linux_notm}} es una forma de publicar o suscribirse a {{site.data.keyword.message_hub_notm}}. Utilice la versión más reciente de esta herramienta. {{site.data.keyword.message_hub_notm}} también proporciona páginas web gráficas que puede utilizar para acceder a alguna información.

En cualquier nodo periférico donde {{site.data.keyword.horizon}} esté instalado, utilice el mandato `hzn` para depurar problemas con el agente de {{site.data.keyword.horizon}} local y el {{site.data.keyword.horizon_exchange}} remoto. Internamente, el mandato `hzn` interactúa con las API REST de HTTP suministradas. El mandato `hzn` simplifica el acceso y proporciona una mejor experiencia de usuario que las propias API REST. El mandato `hzn` a menudo proporciona un texto más descriptivo en su salida, e incluye un sistema de ayuda en línea incorporado. Utilice el sistema de ayuda para obtener información y detalles acerca de los mandatos que se deben utilizar y detalles sobre la sintaxis y los argumentos del mandato. Para ver esta información de ayuda, ejecute los mandatos `hzn --help` o `hzn <subcommand> --help`.

En los nodos periféricos donde no se soportan o no se han instalado paquetes de {{site.data.keyword.horizon}}, en su lugar puede interactuar directamente con las API REST HTTP subyacentes. Por ejemplo, puede utilizar el programa de utilidad `curl` u otros programas de utilidad de CLI de API REST. También puede escribir un programa en un lenguaje que dé soporte a consultas REST.

Por ejemplo, ejecute el programa de utilidad `curl` para comprobar el estado del nodo periférico:
```
curl localhost:8510/status
```
{: codeblock}

## Sugerencias para la resolución de problemas
{: #ts_tips}

Para ayudarle a resolver problemas específicos, consulte las preguntas sobre el estado del sistema y cualesquiera sugerencias asociadas acerca de los temas siguientes. Para cada pregunta, se proporciona una descripción de por qué la pregunta es relevante para la resolución de problemas del sistema. Para algunas preguntas se proporcionan sugerencias o una guía detallada para aprender a obtener la información relacionada del sistema.

Estas preguntas se basan en la naturaleza de la depuración de problemas y están relacionadas con distintos entornos. Por ejemplo, cuando se solucionan problemas en un nodo periférico, es posible que necesite acceso y control completos del nodo, lo que puede aumentar la capacidad para recopilar y ver información.

* [Sugerencias para la resolución de problemas](troubleshooting_devices.md)

  Revise los problemas comunes que puede encontrar al utilizar {{site.data.keyword.ieam}}.
  
## Riesgos de {{site.data.keyword.ieam}} y resolución
{: #risks}

A pesar de que {{site.data.keyword.ieam}} crea oportunidades únicas, también presenta desafíos. Por ejemplo, supera los límites físicos de centro de datos de nube, lo que puede exponerle a problemas de seguridad, direccionabilidad, gestión, propiedad y conformidad. Y, más importante, multiplica los problemas de escalado de las técnicas de gestión basadas en la nube.

Las redes periféricas aumentan el número de nodos de cálculo en un orden de magnitud. Las pasarelas periféricas lo aumentan en otro orden de magnitud. Los dispositivos periféricos aumentan ese número en 3 a 4 órdenes de magnitud. Si DevOps (entrega continua y despliegue continuo) son fundamentales para gestionar una infraestructura de nube de hiperescala, entonces zero-ops (operaciones sin intervención humana) es fundamental para gestionar a la escala masiva que {{site.data.keyword.ieam}} representa.

Es fundamental desplegar, actualizar, supervisar y recuperar el espacio de cálculo periférico sin intervención humana. Todas estas actividades y procesos deben:

* Estar totalmente automatizados
* Capaz de tomar decisiones independientes sobre la asignación de trabajo
* Poder reconocer las condiciones cambiantes y recuperarse de las mismas sin intervención.

Todas estas actividades deben ser seguras, rastreables y defendibles.
