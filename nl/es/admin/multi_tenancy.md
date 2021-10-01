---

copyright:
years: 2020
lastupdated: "2020-10-28"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Multitenencia
{: #multit}

## Arrendatarios en {{site.data.keyword.edge_notm}}
{: #tenants}

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) soporta el concepto de TI general de la multitenencia en las organizaciones, donde cada arrendatario tiene su propia organización. Las organizaciones separan los recursos; por lo tanto, los usuarios de cada organización no pueden crear o modificar recursos en una organización diferente. Además, solo pueden ver los recursos de una organización los usuarios de esa organización, a menos que los recursos estén marcados como públicos.

### Casos de uso frecuentes

Se utilizan dos casos de uso frecuentes para aprovechar la multitenencia en {{site.data.keyword.ieam}}:

* Una empresa tiene varias unidades de negocio, donde cada unidad de negocio es una organización independiente en el mismo centro de gestión de {{site.data.keyword.ieam}}. Tenga en cuenta las razones legales, comerciales o técnicas por las que cada unidad de negocio debe ser una organización una unidad independiente, con su propio conjunto de recursos {{site.data.keyword.ieam}}, a los que, de forma predeterminada, no pueden acceder las otras unidades de negocio. Incluso con organizaciones independientes, la empresa tiene la opción de utilizar un grupo común de administradores de la organización para gestionar todas las organizaciones.
* Una empresa aloja {{site.data.keyword.ieam}} como un servicio para sus clientes, donde cada uno de sus clientes tiene una o varias organizaciones en el centro de gestión. En este caso, los administradores de la organización son exclusivos de cada cliente.

El caso de uso que elija determina cómo se configure {{site.data.keyword.ieam}} y  el servicio Identity and Access Manager ([IAM](https://www.ibm.com/support/knowledgecenter/SSHKN6/iam/landing_iam.html)).

### Tipos de usuarios de {{site.data.keyword.ieam}}
{: #user-types}

{{site.data.keyword.ieam}} da soporte a estos roles de usuario:

| **Rol** | **Acceso** |
|--------------|-----------------|
| **Administrador de hub** | Gestiona la lista de organizaciones {{site.data.keyword.ieam}} mediante la creación, modificación y supresión de organizaciones según sea necesario y mediante la creación de administradores de la organización dentro de cada organización. |
| **Administrador de la organización** | Gestiona los recursos de una o varias organizaciones de {{site.data.keyword.ieam}}. Los administradores de la organización pueden crear, ver o modificar cualquier recurso (usuario, nodo, servicio, política o patrón) de la organización, aunque no sean el propietario del recurso. |
| **Usuario normal** | Crea nodos, servicios, políticas y patrones en la organización y modifica o suprime los recursos que ha creado. Visualiza todos los servicios, políticas y patrones de la organización que otros usuarios han creado. |
{: caption="Tabla 1. Roles de usuario de {{site.data.keyword.ieam}}" caption-side="top"}

Consulte [Control de acceso basado en roles](../user_management/rbac.md) para obtener una descripción de todos los roles de {{site.data.keyword.ieam}}.

## Relación entre IAM y {{site.data.keyword.ieam}}
{: #iam-to-ieam}

El servicio IAM (Identity and Access Manager) gestiona usuarios para todos los productos basados en Cloud Pak, incluido {{site.data.keyword.ieam}}. IAM, a su vez, utiliza LDAP para almacenar los usuarios. Cada usuario de IAM puede ser miembro de uno o varios equipos de IAM. Puesto que cada equipo de IAM está asociado con una cuenta de IAM, un usuario de IAM puede ser indirectamente un miembro de una o varias cuentas de IAM. Consulte [Multitenencia de IAM](https://www.ibm.com/support/knowledgecenter/SSHKN6/iam/3.x.x/multitenancy/multitenancy.html) para obtener detalles.

{{site.data.keyword.ieam}} Exchange proporciona servicios de autenticación y de autorización para los otros componentes de {{site.data.keyword.ieam}}. Exchange delega la autenticación de usuarios a IAM, lo que significa que las credenciales de usuario IAM se pasan a Exchange y éste se basa en IAM para determinar si son válidas. Cada rol de usuario (administrador de hub, administrador de la organización o usuario normal) se define en Exchange y este determina las acciones que pueden realizar los usuarios en {{site.data.keyword.ieam}}.

Cada organización de {{site.data.keyword.ieam}} Exchange está asociada con una cuenta de IAM. Por lo tanto, los usuarios de IAM de una cuenta IAM son automáticamente miembros de la organización {{site.data.keyword.ieam}} correspondiente. La única excepción a esta regla es que se considera que el rol de administrador de hub de {{site.data.keyword.ieam}} está fuera de cualquier organización específica; por lo tanto, no importa la cuenta de IAM en la que se encuentra el usuario de IAM administrador de hub.

Para resumir la correlación entre IAM y {{site.data.keyword.ieam}}:

| **IAM** | **Relación** | **{{site.data.keyword.ieam}}** |
|--------------|----------|-----------------|
| Cuenta de IAM | se correlaciona con | Organización de {{site.data.keyword.ieam}} |
| Usuario de IAM | se correlaciona con | Usuario de {{site.data.keyword.ieam}} |
| No hay ningún homólogo de IAM para el rol | ninguno | Rol de {{site.data.keyword.ieam}} |
{: caption="Tabla 2. Correlación entre IAM - {{site.data.keyword.ieam}}" caption-side="top"}

Las credenciales utilizadas para iniciar la sesión en la consola de {{site.data.keyword.ieam}} son el usuario y la contraseña de IAM. La credencial utilizada para la CLI de {{site.data.keyword.ieam}} (`hzn`) es una clave de API de IAM.

## La organización inicial
{: #initial-org}

De forma predeterminada, se ha creado una organización durante la instalación de {{site.data.keyword.ieam}} con un nombre que ha proporcionado. Si no necesita las prestaciones de multitenencia de {{site.data.keyword.ieam}}, esta organización inicial es suficiente utilizar {{site.data.keyword.ieam}} y puede omitir el resto de esta página.

## Creación de un usuario administrador de hub
{: #create-hub-admin}

El primer paso para utilizar la multitenencia de {{site.data.keyword.ieam}} es crear uno o varios administradores de hub que puedan crear y gestionar las organizaciones. Para poder hacerlo, debe crear o elegir una cuenta de IAM y un usuario que tendrá asignado el rol de administrador de hub.

1. Utilice `cloudctl` para iniciar la sesión en el centro de gestión de {{site.data.keyword.ieam}} como administrador del clúster. (Si todavía no ha instalado `cloudctl`, consulte [Instalación de cloudctl, kubectl y oc](../cli/cloudctl_oc_cli.md) para obtener instrucciones.)

   ```bash
   cloudctl login -a <cluster-url> -u admin -p <password> --skip-ssl-validation
   ```
   {: codeblock}

2. Si todavía no ha conectado una instancia LDAP a IAM, hágalo ahora siguiendo el procedimiento de [Conexión con el directorio de LDAP](https://www.ibm.com/support/knowledgecenter/SSHKN6/iam/3.x.x/configure_ldap.html).

3. El usuario administrador de hub debe estar en una cuenta de IAM. (No importa en qué cuenta.) Si aún no dispone de una cuenta IAM en la que desee que esté el usuario administrador de hub, debe crear una:

   ```bash
   IAM_ACCOUNT_NAME='hub admin account'   # or choose another name    cloudctl iam account-create "$IAM_ACCOUNT_NAME" -d 'account for the hub admin users'    IAM_ACCOUNT_ID=$(cloudctl iam account "$IAM_ACCOUNT_NAME" | grep -E '^ID' | awk '{print $2}')
   IAM_TEAM_ID=$(cloudctl iam teams -s | grep -m 1 "$IAM_ACCOUNT_NAME" | awk '{print $1}')
   ```
   {: codeblock}

4. Cree o elija un usuario LDAP dedicado al rol de administrador de hub de {{site.data.keyword.ieam}}. No utilice el mismo usuario como administrador de hub {{site.data.keyword.ieam}} y como administrador de organización {{site.data.keyword.ieam}} (o usuario de {{site.data.keyword.ieam}} habitual).

5. Importe el usuario en IAM:

   ```bash
   HUB_ADMIN_USER=<the IAM/LDAP user name of the hub admin user>    cloudctl iam user-import -u $HUB_ADMIN_USER    cloudctl iam user-onboard $IAM_ACCOUNT_ID -r PRIMARY_OWNER -u $HUB_ADMIN_USER    IAM_RESOURCE_ID=$(cloudctl iam resources | grep ':n/ibm-edge:')
   cloudctl iam resource-add $IAM_TEAM_ID -r $IAM_RESOURCE_ID
   ```
   {: codeblock}

6. Asigne el rol de administrador de hub al usuario de IAM:

   ```bash
   EXCHANGE_ROOT_PW=<password for the exchange root user>   export HZN_ORG_ID=root   export HZN_EXCHANGE_USER_AUTH=root/root:$EXCHANGE_ROOT_PW   export HZN_EXCHANGE_URL=<the URL of your exchange>   hzn exchange user create -H $HUB_ADMIN_USER ""
   ```
   {: codeblock}

7. Verifique que el usuario tiene el rol de usuario administrador de hub. En la salida del mandato siguiente, debe ver `"hubAdmin": true`.

   ```bash
   hzn exchange user list $HUB_ADMIN_USER
   ```
   {: codeblock}

### Utilización del el usuario administrador de hub con la CLI de {{site.data.keyword.ieam}}
{: #verify-hub-admin}

Cree una clave de API para el usuario administrador de hub y verifique que tiene las prestaciones del administrador de hub:

1. Utilice `cloudctl` para iniciar la sesión en el centro de gestión de {{site.data.keyword.ieam}} como administrador de hub:

   ```bash
   cloudctl login -a <cluster-url> -u $HUB_ADMIN_USER -p <hub-admin-password> -c $IAM_ACCOUNT_ID --skip-ssl-validation
   ```
   {: codeblock}

2. Cree una clave de API para el usuario administrador de hub:

   ```bash
   cloudctl iam api-key-create "${HUB_ADMIN_USER}-api-key" -d "API key for $HUB_ADMIN_USER"
   ```
   {: codeblock}

   Localice el valor de la clave de API en la línea de salida del mandato que empieza por **API Key**. Guarde el valor de la clave en una ubicación segura para utilizarla en el futuro porque más tarde no podrá consultarla desde el sistema. Establezca también esta variable para los mandatos siguientes:

   ```bash
   HUB_ADMIN_API_KEY=<IAM API key you just created>
   ```
   {: codeblock}

3. Visualice todas las organizaciones del centro de gestión. Debería ver la organización inicial que se crea durante la instalación, así como las organizaciones **root** e **IBM**:

   ```bash
   export HZN_ORG_ID=root    export HZN_EXCHANGE_USER_AUTH=root/iamapikey:$HUB_ADMIN_API_KEY    hzn exchange org list -o root
   ```
   {: codeblock}

4. Inicie sesión en la [consola de gestión de {{site.data.keyword.ieam}}](../console/accessing_ui.md) con el usuario y la contraseña de IAM del administrador de hub. La consola de administración de la organización se visualiza porque las credenciales de inicio de sesión tienen el rol de administrador de hub. Utilice esta consola para ver, gestionar y añadir organizaciones. O bien, puede añadir organizaciones utilizando la CLI en la siguiente sección.

## Creación de una organización utilizando la CLI
{: #create-org}

Las organizaciones se pueden crear utilizando la CLI como alternativa al uso de la consola de administración de la organización de {{site.data.keyword.ieam}}. Un requisito previo para crear una organización es crear o elegir una cuenta de IAM que se asociará con la organización. Otro requisito previo es crear o elegir un usuario de IAM al que se le asignará el rol del administrador de la organización.

**Nota**: un nombre de organización no puede contener caracteres de subrayado (_), comas (,), espacios en blanco (), comillas simples (') o signos de interrogación (?).

Siga estos pasos:

1. Si todavía no lo ha hecho, cree un usuario administrador de hub siguiendo los pasos de la sección anterior. Asegúrese de que la clave de API del administrador de hub se haya establecido en la variable siguiente:

   ```bash
   HUB_ADMIN_API_KEY=<IAM API key of the hub admin user>
   ```
   {: codeblock}

2. Utilice `cloudctl` para iniciar la sesión en el centro de gestión de {{site.data.keyword.ieam}} como administrador del clúster y cree una cuenta de IAM con la que se asociará la nueva organización de {{site.data.keyword.ieam}}. (Si todavía no ha instalado `cloudctl`, consulte [Instalación de cloudctl, kubectl y oc](../cli/cloudctl_oc_cli.md).)

   ```bash
   cloudctl login -a <cluster-url> -u admin -p <password> --skip-ssl-validation    NEW_ORG_ID=<new organization name>    IAM_ACCOUNT_NAME="$NEW_ORG_ID"    cloudctl iam account-create "$IAM_ACCOUNT_NAME" -d "$IAM_ACCOUNT_NAME account"    IAM_ACCOUNT_ID=$(cloudctl iam account "$IAM_ACCOUNT_NAME" | grep -E '^ID' | awk '{print $2}')
   IAM_TEAM_ID=$(cloudctl iam teams -s | grep -m 1 "$IAM_ACCOUNT_NAME" | awk '{print $1}')
   ```
   {: codeblock}

3. Cree o elija un usuario de LDAP al que se le asignará el rol del administrador de la organización e impórtelo en IAM. No se puede utilizar un usuario administrador de hub como un usuario administrador de la organización, pero se puede utilizar el mismo usuario administrador de la organización en más de una cuenta IAM. Por lo tanto, esto permite gestionar más de una organización {{site.data.keyword.ieam}}.

   ```bash
   ORG_ADMIN_USER=<the IAM/LDAP user name of the organization admin user>    cloudctl iam user-import -u $ORG_ADMIN_USER    cloudctl iam user-onboard $IAM_ACCOUNT_ID -r PRIMARY_OWNER -u $ORG_ADMIN_USER    IAM_RESOURCE_ID=$(cloudctl iam resources | grep ':n/ibm-edge:')
   cloudctl iam resource-add $IAM_TEAM_ID -r $IAM_RESOURCE_ID
   ```
   {: codeblock}

4. Establezca estas variables de entorno, cree la organización de {{site.data.keyword.ieam}} y verifique que existe:
   ```bash
   export HZN_ORG_ID=root    export HZN_EXCHANGE_USER_AUTH=root/iamapikey:$HUB_ADMIN_API_KEY    export HZN_EXCHANGE_URL=<URL of your exchange>    hzn exchange org create -a IBM/agbot -t "cloud_id=$IAM_ACCOUNT_ID" --description "$NEW_ORG_ID organization" $NEW_ORG_ID    hzn exchange agbot addpattern IBM/agbot IBM '*' $NEW_ORG_ID    hzn exchange org list $NEW_ORG_ID
   ```
   {: codeblock}

5. Asigne el rol de usuario administrador de la organización al usuario de IAM que ha elegido previamente y verifique que el usuario se ha creado en {{site.data.keyword.ieam}} Exchange con el rol de administrador de la organización:

   ```bash
   hzn exchange user create -o $NEW_ORG_ID -A $ORG_ADMIN_USER "" "<email-address>"    hzn exchange user list -o $NEW_ORG_ID $ORG_ADMIN_USER
   ```
   {: codeblock}

   En el listado del usuario, debe ver: `"admin": true`

<div class="note"><span class="notetitle">Nota:</span> Si crea varias organizaciones y quiere que sea un único administrador de la organización quien gestione todas las organizaciones, utilice siempre el mismo valor para `ORG_ADMIN_USER` en esta sección.</div>

Ahora el administrador de la organización puede utilizar la [consola de gestión de {{site.data.keyword.ieam}}](../console/accessing_ui.md) para gestionar los recursos de {{site.data.keyword.ieam}} de esta organización.

### Habilitación del administrador de la organización para utilizar la CLI

Para que un administrador de la organización utilice el mandato `hzn exchange` para gestionar los recursos de {{site.data.keyword.ieam}}utilizando la CLI, deberá:

1. Utilice `cloudctl` para iniciar la sesión en el centro de gestión de {{site.data.keyword.ieam}} y cree una clave de API:

   ```bash
   cloudctl login -a <cluster-url> -u $ORG_ADMIN_USER -p <hub-admin-password> -c $IAM_ACCOUNT_ID --skip-ssl-validation    cloudctl iam api-key-create "${ORG_ADMIN_USER}-api-key" -d "API key for $ORG_ADMIN_USER"
   ```
   {: codeblock}

   Localice el valor de la clave de API en la línea de salida del mandato que empieza por **API Key**. Guarde el valor de la clave en una ubicación segura para utilizarla en el futuro porque más tarde no podrá consultarla desde el sistema. Establezca también esta variable para los mandatos siguientes:

   ```bash
   ORG_ADMIN_API_KEY=<IAM API key you just created>
   ```
   {: codeblock}

   **Sugerencia:** Si añade este usuario a otras cuentas de IAM en el futuro, no es necesario crear una clave de API para cada cuenta. La misma clave de API funcionará en todas las cuentas de IAM de las que este usuario es miembro y, por lo tanto, en todas las organizaciones de {{site.data.keyword.ieam}} de las que este usuario es miembro.

2. Verifique que la clave de API funciona con el mandato `hzn exchange`:

   ```bash
   export HZN_ORG_ID=<organization id>    export HZN_EXCHANGE_USER_AUTH=root/iamapikey:$ORG_ADMIN_API_KEY    hzn exchange user list
   ```
   {: codeblock}


La nueva organización está lista para ser utilizada. Para definir un número máximo de nodos periféricos en esta organización, o para personalizar los valores de pulsación del nodo periférico predeterminado, consulte [Configuración de la organización](#org-config).

## Usuarios no administradores en una organización
{: #org-users}

Se puede añadir un nuevo usuario a una organización importando e incorporado el usuario de IAM (como `MEMBER`) a la cuenta de IAM correspondiente. No es necesario añadir explícitamente el usuario a {{site.data.keyword.ieam}}Exchange porque esto se produce automáticamente cuando es necesario.

A continuación, el usuario puede utilizar la [consola de gestión de {{site.data.keyword.ieam}}](../console/accessing_ui.md). Para que el usuario pueda utilizar la CLI `hzn exchange`, debe seguir estos pasos:

1. Utilice `cloudctl` para iniciar la sesión en el centro de gestión de {{site.data.keyword.ieam}} y cree una clave de API:

   ```bash
   IAM_USER=<iam user>    cloudctl login -a <cluster-url> -u $IAM_USER -p <hub-admin-password> -c $IAM_ACCOUNT_ID --skip-ssl-validation    cloudctl iam api-key-create "${IAM_USER}-api-key" -d "API key for $IAM_USER"
   ```
   {: codeblock}

   Localice el valor de la clave de API en la línea de salida del mandato que empieza por **API Key**. Guarde el valor de la clave en una ubicación segura para utilizarla en el futuro porque más tarde no podrá consultarla desde el sistema. Establezca también esta variable para los mandatos siguientes:

   ```bash
   IAM_USER_API_KEY=<IAM API key you just created>
   ```
   {: codeblock}

3. Establezca estas variables de entorno y verifique el usuario:

```bash
export HZN_ORG_ID=<organization-id> export HZN_EXCHANGE_USER_AUTH=iamapikey:$IAM_USER_API_KEY hzn exchange user list
```
{: codeblock}

## Organización de IBM
{: #ibm-org}

La organización de IBM es una organización exclusiva que proporciona servicios y patrones predefinidos que son ejemplos de tecnología que cualquier usuario puede utilizar en cualquier organización. La organización de IBM se crea automáticamente cuando se instala el centro de gestión de {{site.data.keyword.ieam}}.

**Nota**: Aunque los recursos de la organización de IBM son públicos, esta organización no pretender guardar todo el contenido público del centro de gestión de {{site.data.keyword.ieam}}.

## Configuración de organización
{: #org-config}

Cada organización de {{site.data.keyword.ieam}} tiene los valores siguientes. Los valores predeterminados para estos valores suelen ser suficiente. Si elige personalizar cualquiera de los valores, ejecute el mandato `hzn exchange org update -h` para ver los distintivos del mandato que se pueden utilizar.

| **Valor** | **Descripción** |
|--------------|-----------------|
| `description` | Una descripción de la organización. |
| `label` | El nombre de la organización. Este valor se utiliza para mostrar el nombre de la organización en la consola de gestión de {{site.data.keyword.ieam}}. |
| `heartbeatIntervals` | La frecuencia con la que los agentes de nodo periférico de la organización sondean el centro de gestión para obtener instrucciones. Para obtener información detallada, consulte la sección siguiente. |
| `limits` | Límites para esta organización. Actualmente, el único límite es `maxNodes`, que es el número máximo de nodos periféricos permitido en esta organización. Existe un límite práctico para el número total de nodos periféricos a los que puede dar soporte un solo centro de gestión de {{site.data.keyword.ieam}}. Este valor permite al usuario administrador de hub limitar el número de nodos que puede tener cada organización, lo que evita que una organización utilice toda la capacidad. El valor `0` significa que no hay límite. |
{: caption="Tabla 3. Valores de la organización" caption-side="top"}

### Intervalo de sondeo de pulsaciones de agente
{: #agent-hb}

El agente de {{site.data.keyword.ieam}} que se ha instalado en cada nodo periférico envía periódicamente pulsaciones al centro de gestión para informar al centro de gestión que está conectado y en ejecución y para recibir instrucciones. Solo debe cambiar estos valores para entornos de escala muy alta.

El intervalo de pulsaciones es el tiempo que el agente espera entre pulsaciones en el centro de gestión. El intervalo se ajusta automáticamente a lo largo del tiempo para optimizar la capacidad de respuesta y reducir la carga en el centro de gestión. El ajuste del intervalo se controla mediante tres valores:

| **Valor** | **Descripción**|
|-------------|----------------|
| `minInterval` | El periodo de tiempo más corto (en segundos) que el agente debe esperar entre pulsaciones en el centro de gestión. Cuando un agente se registra, inicia el sondeo con este intervalo. El intervalo nunca será inferior a este valor. El valor `0` significa que se utiliza el valor predeterminado. |
| `maxInterval` | El periodo de tiempo más largo (en segundos) que el agente debe esperar entre pulsaciones en el centro de gestión. El valor `0` significa que se utiliza el valor predeterminado. |
| `intervalAdjustment` | El número de segundos que se deben añadir al intervalo de pulsaciones actual cuando el agente detecta que puede aumentar el intervalo. Después de haber enviado las pulsaciones correctamente al centro de gestión, pero no recibir instrucciones durante un tiempo, el intervalo de pulsaciones aumenta gradualmente hasta que alcanza este intervalo máximo de pulsaciones. Asimismo, cuando se reciben instrucciones, se reduce el intervalo de pulsaciones para garantizar que las instrucciones posteriores se procesan rápidamente. El valor `0` significa que se utiliza el valor predeterminado. |
{: caption="Tabla 4. Valores de heartbeatIntervals" caption-side="top"}

Los valores de intervalo de sondeo de pulsaciones de la organización se aplican a los nodos que no han configurado explícitamente el intervalo de pulsaciones. Para comprobar si un nodo ha establecido explícitamente el valor del intervalo de pulsaciones, utilice `hzn exchange node list <node id>`.

Para obtener más información sobre la configuración de valores en entornos de escala alta, consulte [Configuración del escalado](../hub/configuration.md#scale).
