---

copyright:
  years: 2016, 2019
lastupdated: "2019-03-14"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Funciones de accesibilidad

Las funciones de accesibilidad ayudan a los usuarios con discapacidades como, por ejemplo, movilidad restringida o visión limitada, de manera que puedan usar el contenido de las tecnologías de la información satisfactoriamente.
{:shortdesc}

## Visión general

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) incluye las principales funciones de accesibilidad siguientes:

* Operaciones de sólo teclado
* Operaciones de lector de pantalla
* Interfaz de línea de mandatos (CLI) para gestionar el clúster de {{site.data.keyword.ieam}}

{{site.data.keyword.ieam}} utiliza el último estándar de la W3C, [WAI-ARIA 1.0 ![Icono de enlace externo](../images/icons/launch-glyph.svg "Icono de enlace externo")](http://www.w3.org/TR/wai-aria/){: new_window}, para asegurar el cumplimiento con [Section 508 Standards for Electronic and Information Technology ![Icono de enlace externo](../images/icons/launch-glyph.svg "Icono de enlace externo")](http://www.access-board.gov/guidelines-and-standards/communications-and-it/about-the-section-508-standards/section-508-standards){: new_window} y [Web Content Accessibility Guidelines (WCAG) 2.0 ![Icono de enlace externo](../images/icons/launch-glyph.svg "Icono de enlace externo")](http://www.w3.org/TR/WCAG20/){: new_window}. Para beneficiarse de las funciones de accesibilidad, utilice la última versión de nuestro lector de pantalla y el último navegador admitido por {{site.data.keyword.ieam}}.

La documentación del producto en línea de {{site.data.keyword.ieam}}, que forma parte de la documentación de IBM, está habilitada para una correcta accesibilidad. Para obtener información general sobre accesibilidad, consulte [Accesibilidad en IBM ![Icono de enlace externo](../images/icons/launch-glyph.svg "Icono de enlace externo")](http://www.ibm.com/accessibility/us/en/){: new_window}.

## Hiperenlaces

Todos los enlaces externos, que son enlaces al contenido alojado fuera de la documentación de IBM, se abren en una ventana nueva. Estos enlaces externos también se marcan con un icono de enlace externo (![Icono de enlace externo](../images/icons/launch-glyph.svg "Icono de enlace externo")).

## Navegación con el teclado

{{site.data.keyword.ieam}} utiliza las teclas de navegación estándares.

{{site.data.keyword.ieam}} utiliza los siguientes atajos de teclado.

|Acción|Atajo para Internet Explorer|Atajo para Firefox|
|------|------------------------------|--------------------|
|Desplazarse al marco Vista de contenido|Alt+C y luego pulse Intro y Mayús+F6|Mayús+Alt+C y Mayús+F6|
{: caption="Tabla 1. Atajos de teclado en {{site.data.keyword.ieam}}" caption-side="top"}

## Información sobre las interfaces

Utilice la versión más reciente de un lector de pantalla con {{site.data.keyword.ieam}}.

Las interfaces de usuario de {{site.data.keyword.ieam}} no tienen contenido que parpadee de 2 a 55 veces por segundo.

La interfaz de usuario web de {{site.data.keyword.ieam}} se basa en hojas de estilos en cascada para representar contenido correctamente y ofrecer una correcta experiencia de uso. La aplicación proporciona un método equivalente para usuarios con problemas de poca visión para utilizar los parámetros de visualización del sistema, incluido el modo de alto contraste. Puede controlar el tamaño de fuente utilizando los valores de dispositivo o de navegador web.

Para acceder a {{site.data.keyword.gui}}, abra un navegador web y vaya al URL siguiente:

`https://<Cluster Master Host>:<Cluster Master API Port>/edge`

El nombre de usuario y la contraseña se definen en el archivo config.yaml.

La {{site.data.keyword.gui}} no se basa en hojas de estilo en cascada para representar el contenido correctamente y para proporcionar una correcta experiencia de uso. Sin embargo, la documentación del producto, que está disponible en la documentación en IBM Knowledge Center, se basa en hojas de estilo en cascada. {{site.data.keyword.ieam}} proporciona una forma equivalente para los usuarios con discapacidad visual para utilizar los parámetros de visualización del sistema, incluido el modo de alto contraste. Puede controlar el tamaño de font utilizando los valores de dispositivo o navegador. Tenga en cuenta que la documentación del producto contiene vías de acceso de archivos, variables de entorno, mandatos y otro contenido que puede que los lectores de pantalla estándares no pronuncien bien. Para obtener descripciones más precisas, configure los valores del lector de pantalla para que lea toda la puntuación.


## Software de distribuidor

{{site.data.keyword.ieam}} incluye algunos productos de software de otros proveedores que no están incluidos en el acuerdo de licencia de IBM. IBM no es responsable de las características de accesibilidad de estos productos. Póngase en contacto con el proveedor para obtener información sobre accesibilidad relacionada con sus productos.

## Información relacionada sobre la accesibilidad

Además del centro de atención al cliente y de los sitios web de soporte estándar de IBM, IBM dispone de un servicio telefónico TTY que permite a clientes sordos o con dificultades auditivas acceder a los servicios de ventas y asistencia técnica:

Servicio TTY  
 800-IBM-3383 (800-426-3383)  
 (en América del Norte)

Si desea más información sobre el compromiso que tiene IBM con la accesibilidad, consulte [IBM Accessibility ![Icono de enlace externo](../images/icons/launch-glyph.svg "Icono de enlace externo")](http://www.ibm.com/able){: new_window}.
