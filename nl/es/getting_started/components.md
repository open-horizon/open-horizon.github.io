---

copyright:
years: 2019, 2020
lastupdated: "2020-02-10"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Componentes

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) incluye varios componentes que están empaquetados con el producto.
{:shortdesc}

Consulte la tabla siguiente para obtener una descripción de los componentes de {{site.data.keyword.ieam}}:

|Componente|Versión|Descripción|
|---------|-------|----|
|[IBM Cloud Platform Common Services](https://www.ibm.com/docs/en/cpfs)|3.6.x|Se trata de un conjunto de componentes fundamentales que se instalan automáticamente como parte de la instalación del operador {{site.data.keyword.ieam}}.|
|Agbot|{{site.data.keyword.anax_ver}}|Las instancias de bot de acuerdo (agbot) se crean de forma centralizada y son responsables de desplegar cargas de trabajo y modelos de aprendizaje automático en {{site.data.keyword.ieam}}.|
|MMS |1.5.3-338|El sistema de gestión del modelo (MMS) facilita el almacenamiento, la entrega y la seguridad de los modelos, datos y otros paquetes de metadatos necesarios para los servicios periféricos. Esto permite a los nodos periféricos enviar y recibir fácilmente modelos y metadatos a la nube y desde la nube.|
|API Exchange|2.87.0-531|Exchange proporciona la API REST que contiene todas las definiciones (patrones, políticas, servicios, etc.) utilizadas por todos los demás componentes de {{site.data.keyword.ieam}}.|
|Consola de gestión|1.5.0-578|La IU web utilizada por los administradores de {{site.data.keyword.ieam}} para ver y gestionar los demás componentes de {{site.data.keyword.ieam}}.|
|Secure Device Onboard (Incorporación segura de dispositivo)|1.11.11-441|El componente SDO habilita la tecnología creada por Intel para configurar de una forma simple y segura los dispositivos periféricos y asociarlos a un centro de gestión periférico.|
|Cluster Agent|{{site.data.keyword.anax_ver}}|Se trata de una imagen de contenedor que se instala como un agente en clústeres periféricos para habilitar la gestión de carga de trabajo de nodo mediante {{site.data.keyword.ieam}}.|
|Device Agent|{{site.data.keyword.anax_ver}}|Este componente se instala en dispositivos periféricos para habilitar la gestión de carga de trabajo de nodo mediante {{site.data.keyword.ieam}}.|
|Secrets Manager|1.0.0-168|El gestor de secretos es el repositorio de los secretos desplegados en los dispositivos periférico, lo que permite que los servicios reciban de forma segura las credenciales utilizadas para la autenticación en sus dependencias en sentido ascendente.|
