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

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) da soporte a varios roles. Su rol determina las acciones que puede realizar.
{:shortdesc}

## Organizaciones
{: #orgs}

{{site.data.keyword.ieam}} soporta el concepto general de la multitenencia a través de las organizaciones, donde cada arrendatario tiene su propia organización. Las organizaciones separan los recursos;
por lo tanto, los usuarios de cada organización no pueden crear o modificar recursos en una organización diferente. Además, los recursos de una organización sólo pueden verlos los usuarios de esa organización (a menos que los recursos estén marcados como públicos). Los recursos que se marcan como públicos son los únicos recursos que se pueden ver en las organizaciones.

La organización de IBM proporciona servicios y patrones predefinidos. Aunque los recursos de esa organización son públicos, no está destinado a contener todo el contenido público del centro de gestión de {{site.data.keyword.ieam}}.

De forma predeterminada, se crea una organización durante la instalación de {{site.data.keyword.ieam}} con un nombre que elija. Puede crear organizaciones adicionales según sea necesario. Para obtener más información sobre cómo añadir organizaciones al centro de gestión, consulte [Multitenencia](../admin/multi_tenancy.md).

## Identidades
{: #ids}

Hay cuatro tipos de identidades en {{site.data.keyword.ieam}}:

* Usuarios de gestión de identidad y acceso (IAM). Todos los componentes de {{site.data.keyword.ieam}} reconocen los usuarios de IAM: UI, Exchange, CLI **hzn**, CLI **cloudctl**, CLI **oc**, CLI **kubectl**.
  * IAM proporciona un plugin de LDAP, por lo que los usuarios de LDAP conectados a IAM se comportan como usuarios de IAM
  * Las claves de API de IAM (utilizadas con el mandato **hzn**) se comportan como usuarios de IAM
* Usuarios sólo de Exchange: el usuario root de Exchange es un ejemplo de esto. Normalmente no es necesario crear otros usuarios locales sólo de Exchange. Como procedimiento recomendado, gestione los usuarios en IAM y utilice esas credenciales de usuario (o las claves de API asociadas con esos usuarios) para autenticarse en {{site.data.keyword.ieam}}.
* Nodos de Exchange (dispositivos periféricos o clústeres periféricos)
* Agbots de Exchange

### Control de accesos basado en roles (RBAC)
{: #rbac_roles}

{{site.data.keyword.ieam}} incluye los siguientes roles:

| **Rol**    | **Acceso**    |  
|---------------|--------------------|
| Usuario de IAM | Mediante IAM, se pueden proporcionar estos roles de centro de gestión: Administrador de clústeres, Administrador, Operador, Editor y Visor. Un rol de IAM se asigna a los usuarios o grupos de usuarios cuando éstos se añaden a un equipo de IAM. El acceso de equipo a los recursos puede controlarse mediante el espacio de nombres de Kubernetes. A los usuarios de IAM también se les puede proporcionar cualquiera de los roles de Exchange siguientes utilizando la CLI **hzn exchange**. |
| Usuario root de Exchange | Tiene privilegio ilimitado en Exchange. Este usuario se define en el archivo de configuración de Exchange. Se puede inhabilitar, si se desea. |
| Usuario administrador del hub de Exchange | Puede ver la lista de organizaciones, ver los usuarios de una organización y crear o suprimir organizaciones. |
| Usuario administrador de organización de Exchange | Tiene privilegio de Exchange ilimitado en la organización. |
| Usuario de Exchange | Puede crear recursos de Exchange (nodos, servicios, patrones, políticas) en la organización. Puede actualizar o suprimir recursos propiedad de este usuario. Puede leer todos los servicios, patrones y políticas en la organización y los servicios y patrones públicos en otras organizaciones. Puede leer los nodos que son propiedad de este usuario. |
| Nodos de Exchange | Puede leer su propio nodo en Exchange y leer todos los servicios, patrones y políticas en la organización y el servicio público y los patrones en otras organizaciones. Estas son las únicas credenciales que se deben guardar en el nodo periférico, porque tienen el privilegio mínimo necesario para operar en el nodo periférico.|
| Agbots de Exchange | Los agbots de la organización de IBM pueden leer todos los nodos, servicios, patrones y políticas en todas las organizaciones. |
{: caption="Tabla 1. Roles de RBAC" caption-side="top"}
