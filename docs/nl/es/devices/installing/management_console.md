---

copyright:
years: 2020
lastupdated: "2020-1-31"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Utilización de la consola de {{site.data.keyword.edge_notm}}
{: #accessing_ui}

Utilice la consola para realizar funciones de gestión de computación periférica. 
 
## Navegación a la consola de {{site.data.keyword.edge_notm}}

1. Navegue a la consola de {{site.data.keyword.edge_notm}} a través de `https://<cluster-url>/edge`, donde `<cluster-url>` es el ingreso externo del clúster.
2. Escriba sus credenciales de usuario. Aparece la página de inicio de sesión de {{site.data.keyword.mcm}}.
3. En la barra de direcciones del navegador, elimine `/multicloud/welcome` del final del URL, añada `/edge` y pulse **Intro**. Aparece la página de {{site.data.keyword.edge_notm}}.

## Navegadores soportados

{{site.data.keyword.edge_notm}} se ha probado satisfactoriamente con estos navegadores.

|Plataforma|Navegadores soportados|
|--------|------------------|
|Microsoft Windows™|<ul><li>Mozilla Firefox - última versión para Windows</li><li>Google Chrome - última versión para Windows</li></ul>|
|{{site.data.keyword.macOS_notm}}|<ul><li>Mozilla Firefox - última versión para Mac</li><li>Google Chrome - última versión para Mac</li></ul>|
{: caption="Tabla 1. Navegadores soportados en {{site.data.keyword.edge_notm}}" caption-side="top"}


## Exploración de la {{site.data.keyword.edge_notm}} consola
{: #exploring-management-console}

Las características de la consola de {{site.data.keyword.edge_notm}} incluyen:

* Incorporación fácil con enlaces de sitios periféricos para un soporte robusto
* Amplias funciones de visibilidad y gestión:
  * Vistas de gráficas exhaustivas, incluido el estado de nodo, la arquitectura e información de error.
  * Detalles de error con enlaces para soporte de resolución
  * Ubicación y filtrado de contenido que incluye información sobre: 
    * Propietarios
    * Arquitectura 
    * Pulsaciones (por ejemplo, los últimos 10 minutos, hoy, etc.)
    * Estado de nodo (Activo, Inactivo, Tiene error, etc.)
    * Tipo de despliegue (política o patrón)
  * Detalles útiles acerca de los nodos periféricos de Exchange, incluidos:
    * Propiedades
    * Restricciones 
    * Despliegues
    * Servicios activos

* Prestaciones de vista robustas

  * La capacidad de ubicar y filtrar rápidamente por: 
    * Propietario
    * Arquitectura
    * Versión
    * Público (true o false)
  * Vistas de servicio de lista o tarjeta
  * Servicios agrupados que comparten un nombre
  * Detalles para cada servicio en Exchange que incluyen: 
    * Propiedades
    * Restricciones
    * Despliegues
    * Variables de servicio
    * Dependencias de servicio
  
* Gestión de política de despliegue

  * La capacidad de ubicar y filtrar rápidamente por:
    * ID de política
    * Propietario
    * Etiqueta
  * Desplegar cualquier servicio desde Exchange
  * Añadir propiedades a políticas de despliegue
  * Un constructor de restricciones para la creación de expresiones 
  * Una modalidad avanzado para escribir restricciones directamente en JSON
  * La capacidad de ajustar las versiones de despliegue de retrotracción y los valores de estado del nodo
  * Ver y editar detalles de política que incluyen:
    * Propiedades de servicio y despliegue
    * Restricciones
    * Retrotracciones
    * Valores de estado de nodo
  
