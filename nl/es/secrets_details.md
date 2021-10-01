---

copyright:
years: 2021
lastupdated: "2021-08-16"

---

{:shortdesc: .shortdesc}
{:new_window: target="_blank"}
{:codeblock: .codeblock}
{:pre: .pre}
{:screen: .screen}
{:tip: .tip}
{:download: .download}

# Desarrollo de un servicio utilizando secretos
{: #using secrets}

<img src="../images/edge/10_Secrets.svg" style="margin: 3%" alt="Developing a service using secrets"> 

# Detalles del gestor de secretos
{: #secrets_details}

El gestor de secretos proporciona almacenamiento seguro para información confidencial como, por ejemplo, las credenciales de autenticación o las claves de cifrado. {{site.data.keyword.ieam}} despliega de forma segura estos secretos para que solo los servicios configurados para recibir un secreto tengan acceso a él. El [Ejemplo Hello Secret World](https://github.com/open-horizon/examples/blob/master/edge/services/helloSecretWorld/CreateService.md) proporciona una visión general de cómo explotar los secretos en un servicio periférico.

{{site.data.keyword.ieam}} da soporte al uso de [Hashicorp Vault](https://www.vaultproject.io/) como gestor de secretos. Los secretos creados mediante la CLI de hzn se correlacionan con los secretos de caja fuerte utilizando el [gestor de secretos KV V2](https://www.vaultproject.io/docs/secrets/kv/kv-v2). Esto significa que los detalles de cada secreto de {{site.data.keyword.ieam}} están compuestos de una clave y un valor. Ambos se almacenan como parte de los detalles del secreto y se pueden establecer en cualquier valor de serie. Un uso común de esta característica es proporcionar el tipo de secreto en la clave e información confidencial como el valor. Por ejemplo, establezca la clave en "basicauth" y establezca el valor en "user:password". Al hacerlo, el desarrollador de servicios puede consultar el tipo de secreto, lo que permite al código de servicio manejar el valor correctamente.

Los nombres de los secretos en el gestor de secretos nunca son conocidos para una implementación de servicio. No es posible transmitir información de la caja fuerte a una implementación de servicio utilizando el nombre de un secreto.

Los secretos se almacenan en el gestor de secretos KV V2 añadiendo openhorizon y la organización del usuario como prefijos al nombre de secreto. Esto garantiza que los secretos creados por los usuarios de {{site.data.keyword.ieam}} se aíslen de otros usos de la caja fuerte de otras integraciones, y que se mantenga el aislamiento de varios arrendatarios.

Los nombres de secreto los gestionan los administradores de organización de {{site.data.keyword.ieam}} (o los usuarios cuando utilizan secretos privados de usuario). Las listas de control de acceso (ACL) de caja fuerte controlan los secretos que un usuario de {{site.data.keyword.ieam}} puede gestionar. Esto se consigue a través de un plugin de autenticación de caja fuerte que delega la autenticación de usuarios a {{site.data.keyword.ieam}} Exchange. Al autenticar correctamente un usuario, el plugin de autenticación en la caja fuerte creará un conjunto de políticas de ACL específicas de este usuario. Un usuario con privilegios de administrador en Exchange puede:
- Añadir, eliminar, leer y listar todos los secretos de una organización.
- Añadir, eliminar, leer y listar todos los secretos privados de ese usuario.
- Eliminar y listar los secretos privados de otros usuarios en la organización (pero no puede añadirlos ni leerlos).

Un usuario sin privilegios de administrador puede:
- Listar todos los secretos de una organización (pero no puede añadirlos, eliminarlos ni leerlos).
- Añadir, eliminar, leer y listar todos los secretos privados de ese usuario.

El agbot de {{site.data.keyword.ieam}} también tiene acceso a los secretos para poder desplegarlos en nodos periféricos. El agbot mantiene un inicio de sesión renovable en la caja fuerte y se le proporcionan políticas de ACL específicas. Un agbot puede:
- Leer secretos de toda la organización y secretos privados de usuario de cualquier organización, pero no puede añadir, eliminar o listar secretos.

El usuario root de Exchange y los administradores de concentrador de Exchange no tienen permisos en la caja fuerte. Consulte [Control de acceso basado en roles](../user_management/rbac.html) para obtener más información sobre estos roles.
