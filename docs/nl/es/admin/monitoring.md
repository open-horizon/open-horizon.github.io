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


# Supervisión

## Acceso al Panel de Grafana de {{site.data.keyword.ieam}} 
{: #monitoring_dashboard}

1. Siga los pasos de [Utilización de la consola de gestión](../console/accessing_ui.md) para asegurarse de que puede acceder a la consola de gestión de {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}).
2. Vaya a `https://<cluster-url>/grafana` para ver el panel de grafana. 
3. En la esquina inferior izquierda, hay un icono de perfil. Pase el cursor por encima y seleccione la opción de la organización del conmutador. 
4. Seleccione la organización `ibm-edge`. Si ha instalado {{site.data.keyword.ieam}} en un espacio de nombres diferente, seleccione esta organización en su lugar.
5. Busque "{{site.data.keyword.ieam}}" para que pueda supervisar la CPU global, la memoria y la presión de red de {{site.data.keyword.ieam}} .

   <img src="../images/edge/ieam_monitoring_dashboard.png" style="margin: 3%" alt="IEAM Monitoring Dashboard" width="85%" height="85%" align="center">


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
