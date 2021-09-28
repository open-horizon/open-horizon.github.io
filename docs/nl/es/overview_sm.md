---

copyright:
years: 2021
lastupdated: "2021-07-20"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Visión general del gestor de secretos
{: #overviewofsm}

Los servicios desplegados de forma periférica a menudo requieren acceso a servicios en la nube, lo que significa que el servicio necesita credenciales para autenticarse en el servicio de nube. El gestor de secretos proporciona un mecanismo seguro que permite almacenar, desplegar y gestionar credenciales sin exponer los detalles en los metadatos de {{site.data.keyword.ieam}} (por ejemplo, las definiciones de servicio y las políticas), o a otros usuarios del sistema que no deban tener acceso al secreto. El gestor de secretos es un componente conectable de {{site.data.keyword.ieam}}. Actualmente, HashiCorp Vault es el único gestor de secretos soportado.

Un secreto es un ID de usuario/contraseña, un certificado, una clave RSA o cualquier otra credencial que otorgue acceso a un recurso protegido que necesite una aplicación periférica para poder realizar su función. Los secretos se almacenan en el gestor de secretos. Un secreto tiene un nombre que se utiliza para su identificación, pero que no proporciona información sobre los detalles del secreto. Los secretos están administrados por la CLI de {{site.data.keyword.ieam}} o por un administrador, utilizando la IU o CLI del gestor de secretos.

Un desarrollador de servicios declara la necesidad de un secreto en una definición de servicio de {{site.data.keyword.ieam}}. El desplegador de servicio adjunta (o enlaza) un secreto del gestor de secretos al despliegue del servicio, asociando el servicio con un secreto del gestor de secretos. Por ejemplo, supongamos que un desarrollador necesita acceder al servicio de nube XYZ a través de la autenticación básica. El desarrollador actualiza la definición de servicio de {{site.data.keyword.ieam}} para incluir un secreto denominado myCloudServiceCred. El desplegador de servicios ve que el servicio requiere un secreto para poder desplegarse y detecta un secreto en el gestor de secretos denominado cloudServiceXYZSecret que contiene credenciales de autenticación básica. El desplegador de servicio actualiza la política de despliegue (o el patrón) para indicar que el secreto del servicio denominado myCloudServiceCreds debe contener las credenciales del secreto del gestor de secretos denominado cloudServiceXYZSecret. Cuando el desplegador de servicios publica la política de despliegue (o patrón), {{site.data.keyword.ieam}} desplegará de forma segura los detalles de cloudServiceXYZSecret en todos los nodos periféricos que sean compatibles con la política de despliegue (o el patrón).
