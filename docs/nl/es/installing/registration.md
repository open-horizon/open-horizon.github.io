---

copyright:
years: 2020
lastupdated: "2020-02-03"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Instalación del agente
{: #registration}

Cuando instale el software de agente de {{site.data.keyword.horizon}} en el dispositivo periférico, puede registrar el dispositivo periférico en {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) para añadir el dispositivo al dominio de gestión de computación periférica y ejecutar servicios periféricos. Las instrucciones siguientes registran el nuevo dispositivo periférico en el servicio periférico de ejemplo helloworld mínimo para confirmar que el dispositivo periférico está funcionando correctamente. El servicio periférico helloworld se puede detener fácilmente cuando el usuario está preparado para ejecutar servicios periféricos propios en el dispositivo periférico.
{:shortdesc}

## Antes de empezar
{: #before_begin}

Debe seguir los pasos de la [Preparación de un dispositivo periférico](adding_devices.md).

## Instalación y registro de dispositivos periféricos
{: #installing_registering}

Para instalar y registrar el agente en dispositivos periféricos se proporcionan cuatro métodos diferentes, cada uno de los cuales es útil en circunstancias diferentes:

* [Instalación y registro automatizados de agente](automated_install.md): instale y registre un dispositivo periférico con un mínimo de pasos. **Los usuarios noveles deben utilizar este método.**
* [Instalación y registro manuales avanzados de agente](advanced_man_install.md): realice cada paso usted mismo para instalar y registrar un dispositivo periférico. Utilice este método si necesita hacer algo fuera de lo normal y el script que se utiliza en el método 1 no tiene la flexibilidad necesaria. También puede utilizar este método si desea conocer exactamente qué se necesita para configurar un dispositivo periférico.
* [Instalación y registro masivos de agente](many_install.md#batch-install): instale y registre muchos dispositivos periféricos a la vez.
* [Instalación y registro del agente de SDO](sdo.md): instalación automática con dispositivos SDO.

## Preguntas y resolución de problemas
{: #questions_ts}

Si tiene alguna dificultad con cualquiera de estos pasos, consulte los temas proporcionados sobre resolución de problemas y preguntas más frecuentes. Para obtener más información, consulte:
  * [Resolución de problemas](../troubleshoot/troubleshooting.md)
  * [Preguntas más frecuentes](../getting_started/faq.md)
