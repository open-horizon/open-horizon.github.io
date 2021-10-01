---

copyright:
years: 2020
lastupdated: "2020-4-8"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Dispositivos periféricos
{: #edge_devices}

Un dispositivo periférico proporciona un punto de entrada en las redes principales de
proveedor de servicios o de empresa. Los ejemplos incluyen teléfonos inteligentes, cámaras de seguridad o incluso
un horno de microondas conectado a Internet.

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}})
está disponible para el centro de gestión o los servidores, incluidos los dispositivos distribuidos. Consulte
las secciones siguientes para obtener detalles sobre cómo instalar el agente ligero de
{{site.data.keyword.ieam}} en dispositivos periféricos: 

* [Preparación de un dispositivo periférico](../installing/adding_devices.md)
* [Instalación del agente](../installing/registration.md)
* [Actualización del agente](../installing/updating_the_agent.md)

Todos los dispositivos periféricos (nodos periféricos) requieren que esté instalado el software de {{site.data.keyword.horizon_agent}}. El {{site.data.keyword.horizon_agent}} también depende del software de [Docker ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://www.docker.com/). 

Centrándose en el dispositivo periférico, el diagrama siguiente muestra el flujo de los pasos que se dan para configurar el dispositivo periférico y lo que hace el agente una vez que se inicia.

<img src="../../images/edge/05a_Installing_edge_agent_on_device.svg" width="80%" alt="{{site.data.keyword.horizon_exchange}}, agbots y agentes">
