---

copyright:
years: 2019
lastupdated: "2019-09-27"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Control de acceso basado en roles
{: #rbac}

{{site.data.keyword.edge_notm}} {{site.data.keyword.ieam}} da soporte a varios roles. Su rol determina las acciones que puede realizar.
{:shortdesc}

## Organizaciones
{: #orgs}

Las organizaciones de {{site.data.keyword.ieam}} se utilizan para separar el acceso a los recursos. Los
recursos para una organización sólo los puede ver esa organización, a menos que los recursos se hayan marcado
explícitamente como públicos. Los recursos que se marcan como públicos son los únicos recursos que se pueden ver entre las organizaciones.

La organización de IBM se utiliza para proporcionarle servicios y patrones predefinidos.

En {{site.data.keyword.ieam}}, el nombre de la organización es el nombre del clúster.

## Identidades
{: #ids}

Hay tres tipos de identidades en {{site.data.keyword.ieam}}:

* Hay dos tipos de usuarios. Los usuarios pueden acceder a la consola de {{site.data.keyword.ieam}}
y a Exchange.
  * Usuarios de gestión de identidad y acceso (IAM). {{site.data.keyword.ieam}} Exchange
reconoce los usuarios de IAM.
    * IAM proporciona un plugin de LDAP, por lo que los usuarios de LDAP conectados a IAM se comportan
como usuarios de IAM
    * Las claves de API de IAM (utilizadas con el mandato **hzn**)
se comportan como usuarios de IAM
  * Usuarios de Exchange locales: el usuario root de Exchange es un ejemplo de esto. Normalmente
no es necesario crear otros usuarios de Exchange locales.
* Nodos (dispositivos periféricos o clústeres periféricos)
* AgBots

### Control de accesos basado en roles (RBAC)
{: #rbac_roles}

{{site.data.keyword.ieam}} incluye los siguientes roles:

| **Rol**    | **Acceso**    |  
|---------------|--------------------|
| Usuario root de Exchange | Tiene privilegio ilimitado en Exchange. Este usuario se define en el archivo de configuración de Exchange. Se puede inhabilitar, si se desea.|
| Usuario administrador o clave de API | Tiene privilegio ilimitado en la organización. |
| Usuario no administrador o clave de API | Puede crear recursos de Exchange (nodos, servicios, patrones, políticas) en la organización. Puede actualizar o suprimir recursos propiedad de este usuario. Puede leer todos los servicios, patrones y políticas en la organización y los servicios y patrones públicos en otras organizaciones.|
| Nodos | Puede leer su propio nodo en Exchange y leer todos los servicios, patrones y políticas en la organización y el servicio público y los patrones en otras organizaciones.|
| Agbots | Los agbots de la organización de IBM pueden leer todos los nodos, servicios, patrones y políticas en todas las organizaciones. |
{: caption="Tabla 1. Roles de RBAC" caption-side="top"}
