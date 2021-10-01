---

copyright:
years: 2020
lastupdated: "2020-2-2"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Supervisión de nodos y servicios periféricos
{: #monitoring_edge_nodes_and_services}

[Inicie la sesión en la consola de gestión](../console/accessing_ui.md) para supervisar los nodos y servicios periférico de {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}).

* Supervisar los nodos periféricos:
  * El panel de control Nodos es la primera página que se visualiza e incluye un diagrama de anillo que muestra el estado de todos los nodos periféricos.
  * Para ver todos los nodos en un estado determinado, pulse ese color en el diagrama de anillo. Por ejemplo, para ver todos los nodos periféricos con errores (si existe alguno), pulse el color que la descripción indica que se utiliza para **Tiene error**.
  * Se visualiza una lista de los nodos con errores. Para profundizar en un nodo para ver el error específico, pulse el nombre de nodo.
  * En la página de detalles de nodo que se visualiza, la sección **Errores de agente periférico** muestra los servicios que tienen errores, el mensaje de error específico y la indicación de fecha y hora.
* Supervisar servicios periféricos:
  * En el separador **Servicios**, pulse el servicio en el que desea profundizar, lo que mostrará la página de detalles del servicio periférico.
  * En la sección **Despliegue** de la página de detalles, puede ver las políticas y los patrones que están desplegando este servicio en los nodos periféricos.
* Supervisar servicios periféricos en un nodo periférico:
  * En la pestaña **Nodos**, cambie a la vista de lista y pulse el nodo periférico en el que desea acceder a los detalles.
  * En la página de detalles de nodo, la sección **Servicios** muestra qué servicios periféricos se están ejecutando actualmente en ese nodo periférico.
