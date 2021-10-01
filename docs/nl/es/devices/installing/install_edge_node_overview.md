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

# Visión general de nodo periférico
{: #hub_install_overview}

Un nodo periférico actúa como un portal de usuario final para la comunicación con otros nodos
de la computación de clúster. Esto significa que es un miembro de clúster, pero no una parte del
entorno de cálculo o almacenamiento general. Los nodos periféricos son la interfaz entre los clústeres
y la red externa. Por lo general, los nodos periféricos ejecutan aplicaciones de cliente y
herramientas de administración de clústeres.

Los nodos periféricos facilitan las comunicaciones de los usuarios finales a otros nodos (por ejemplo,
nodos maestro y de trabajador). Los nodos periféricos permiten a los usuarios finales ponerse en contacto con
los nodos de trabajador cuando sea necesario, proporcionando una interfaz de red para el clúster
sin dejar el clúster entero abierto a la comunicación.

IEAM proporciona una gestión de nodos periféricos que minimiza los riesgos de despliegue y
gestiona el ciclo de vida del software de servicio en nodos periféricos de forma totalmente autónoma
utilizando nodos de clúster y de dispositivo.

Añada un gráfico que muestre los pasos de instalación y configuración de alto nivel del
nodo periférico (muestre también los dispositivos y clústeres). 

## Qué hacer a continuación

Consulte [Instalación de nodos periféricos](installing_edge_nodes.md)
para obtener instrucciones de instalación de nodos.

## Información relacionada

* [Instalación de nodos periféricos](installing_edge_nodes.md)
* [Dispositivos periféricos](../developing/edge_devices.md)
* [Clústeres periféricos](../developing/edge_clusters.md)
