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

# Configurar {{site.data.keyword.ieam}}

## Configuración de recursos personalizados de EamHub
{: #cr}

La configuración principal para {{site.data.keyword.ieam}} se realiza a través del recurso personalizado EamHub, en particular el campo **spec** de dicho recurso personalizado.

En este documento se da por supuesto que:
* El espacio de nombres para el que ejecuta estos mandatos es donde se ha desplegado el operador del centro de gestión de  {{site.data.keyword.ieam}}.
* El nombre del recurso personalizado EamHub es el **ibm-edge** predeterminado. Si es diferente, modifique los mandatos para sustituir **ibm-edge**.
* Se instala el **jq** binario, lo que garantiza que la salida se visualiza en un formato legible.


La **spec** predeterminada definida es mínima, solo contiene la aceptación de licencia, que puede ver con:
```
$ oc get eamhub ibm-edge -o yaml ... spec:   license:     accept: true ...
```

### Bucle de control de operador
{: #loop}

El operador de centro de gestión de {{site.data.keyword.ieam}} se ejecuta en un bucle idempotent continuo para sincronizar el estado actual de los recursos con el estado esperado de los recursos.

Debido a ese bucle continuo, debe comprender dos cosas cuando intente configurar los recursos gestionados por el operador:
* Cualquier cambio en el recurso personalizado se leerá de forma asíncrona mediante el bucle de control. Después de realizar el cambio, este cambio puede tardar unos minutos en entrar en vigor a través del operador.
* Cualquier cambio manual que se realice en un recurso que el operador controle puede sobrescribirlo (deshacerlo) el operador imponiendo un estado específico. 

Examine los registros de pod del operador para observar este bucle:
```
oc logs $(oc get pods | grep ibm-eamhub-operator | awk '{print $1}') --tail 20 -f
```
{: codeblock}

Cuando un bucle finaliza, genera un resumen **PLAY RECAP**. Para ver el resumen más reciente, ejecute:
```
oc logs $(oc get pods | grep ibm-eamhub-operator | awk '{print $1}') --tail 5000 | grep -A 1 '^PLAY RECAP' | tail -n 1
```
{: codeblock}

Lo siguiente indica un bucle que se ha completado sin que tengan lugar operaciones (en su estado actual, **PLAY RECAP** mostrará siempre **changed=1**):
```
$ oc logs $(oc get pods | grep ibm-eamhub-operator | awk '{print $1}') --tail 5000 | grep -A 1 '^PLAY RECAP' | tail -n 1 localhost                  : ok=51   changed=1    unreachable=0    failed=0    skipped=11   rescued=0    ignored=0
```
{: codeblock}

Revise estos campos al realizar cambios de configuración:
* **changed**: Cuando es mayor que **1** indica que el operador ha realizado una tarea que ha modificado el estado de uno o más recursos (puede ser a petición del usuario modificando el recurso personalizado o porque el operador ha revertido un cambio manual que se ha realizado).
* **rescued**: Una tarea ha fallado, sin embargo era una anomalía conocida posible y la tarea se volverá a intentar en el siguiente bucle.
* **failed**: en la instalación inicial hay algunas anomalías esperadas, si se está viendo repetidamente la misma anomalía y el mensaje no se borra (u oculta), probablemente indica un problema.

### Opciones de configuración comunes de EamHub

Se pueden realizar varios cambios de configuración, pero es más probable que algunos se realicen más que otros. Esta sección describe algunos de los valores más comunes.

| Valor de configuración | Valor predeterminado | Descripción |
| :---: | :---: | :---: |
| Valores globales | -- | -- |
| pause_control_loop | false | Pone en pausa el bucle de control mencionado anteriormente, para habilitar los cambios manuales temporales para la depuración. No se debe utilizar para el estado estable. |
| ieam_maintenance_mode | false | Establece todos los recuentos de réplicas de pod sin almacenamiento persistente a 0. Utilizado para la restauración de copia de seguridad. |
| ieam_local_databases | true | Habilita o inhabilita bases de datos locales. No se soporta la conmutación entre estados. Consulte [configuración de base de datos remota](./configuration.md#remote). |
| ieam_database_HA | true | Habilita o inhabilita la modalidad HA para bases de datos locales. Esto establece el recuento de réplicas para todos los pods de base de datos en **3** cuando es **true** y en **1** cuando es **false**. |
| hide_sensitive_logs | true | Oculta los registros de operador que tratan con el establecimiento de **Secretos de Kubernetes**, si se establece en **false** los errores de tarea pueden hacer que el operador registre valores de autenticación codificados. |
| storage_class_name | "" | Utiliza la clase de almacenamiento predeterminada si no se ha establecido. |
| ieam_enable_tls | false | Habilita o inhabilita el TLS interno para el tráfico entre componentes de {{site.data.keyword.ieam}}. **Precaución:** si se altera temporalmente la configuración predeterminada para Exchange, CSS o Vault, la configuración TLS se debe modificar manualmente en la alteración temporal de la configuración. |
| ieam_local_secrets_manager | true | Habilita o inhabilita el componente de gestor de secretos local (vault). |


### Opciones de configuración de escalado de componentes de EamHub

| Valor de escalado de componentes | Número predeterminado de réplicas | Descripción |
| :---: | :---: | :---: |
| exchange_replicas | 3 | El número predeterminado de réplicas para Exchange. Si se altera temporalmente la configuración de Exchange predeterminada (exchange_config), **maxPoolSize** se debe ajustar manualmente utilizando esta fórmula `((exchangedb_max_connections-8)/exchange_replicas)` |
| css_replicas | 3 | El número predeterminado de réplicas para el CSS. |
| ui_replicas | 3 | El número predeterminado de réplicas para la interfaz de usuario. |
| agbot_replicas | 2 | El número predeterminado de réplicas para el bot de acuerdo. Si se altera temporalmente la configuración predeterminada del bot de acuerdo (agbot_config), **MaxOpenConnections** se debe ajustar manualmente utilizando esta fórmula `((agbotdb_max_connections-8)/agbot_replicas)` |


### Opciones de configuración del recurso del componente EamHub

**Nota**: debido a que los operadores de Ansible requieren que se añada un diccionario anidado en su totalidad, debe añadir los valores de configuración anidados en su totalidad. Consulte [Configuración de escalado](./configuration.md#scale) para ver un ejemplo.

<table>
<tr>
<td> Valor de recurso de componente </td> <td> Valor predeterminado </td> <td> Descripción </td>
</tr>
<tr>
<td> exchange_resources </td> 
<td>

```
  exchange_resources:     requests:       memory: 512Mi       cpu: 10m     limits:       memory: 2Gi       cpu: 2
```

</td>
<td>
Las solicitudes y los límites predeterminados para Exchange. 
</td>
</tr>
<tr>
<td> agbot_resources </td> 
<td>

```
  agbot_resources:     requests:       memory: 64Mi       cpu: 10m     limits:       memory: 2Gi       cpu: 2
```

</td>
<td>
Las solicitudes y los límites predeterminados para el bot de acuerdo. 
</td>
</tr>
<tr>
<td> css_resources </td> 
<td>

```
  css_resources:     requests:       memory: 64Mi       cpu: 10m     limits:       memory: 2Gi       cpu: 2
```

</td>
<td>
Las solicitudes y los límites predeterminados para el CSS. 
</td>
</tr>
<tr>
<td> sdo_resources </td> 
<td>

```
  sdo_resources:     requests:       memory: 1024Mi       cpu: 10m     limits:       memory: 2Gi       cpu: 2
```

</td>
<td>
Las solicitudes y los límites predeterminados para SDO. 
</td>
</tr>
<tr>
<td> ui_resources </td> 
<td>

```
  ui_resources:     requests:       memory: 64Mi       cpu: 10m     limits:       memory: 2Gi       cpu: 2
```

</td>
<td>
Las solicitudes y los límites predeterminados para la interfaz de usuario. 
</td>
</tr>
<tr>
<td> vault_resources </td> 
<td>

```
  vault_resources:     requests:       memory: 1024Mi       cpu: 10m     limits:       memory: 2Gi       cpu: 2
```

</td>
<td>
Las solicitudes y los límites predeterminados para el gestor de secretos. 
</td>
</tr>
<tr>
<td> mongo_resources </td> 
<td>

```
  mongo_resources:     limits:       cpu: 2       memory: 2Gi     requests:       cpu: 100m       memory: 256Mi
```

</td>
<td>
Las solicitudes y los límites predeterminados para la base de datos de CSS de mongo. 
</td>
</tr>
<tr>
<td> postgres_exchangedb_sentinel </td> 
<td>

```
  postgres_exchangedb_sentinel:     resources:       requests:         cpu: "100m"         memory: "256Mi"       limits:         cpu: 1         memory: 1Gi
```

</td>
<td>
Las solicitudes y los límites predeterminados para el centinela de Exchange Postgres. 
</td>
</tr>
<tr>
<td> postgres_exchangedb_proxy </td> 
<td>

```
  postgres_exchangedb_proxy:     resources:       requests:         cpu: "100m"         memory: "256Mi"       limits:         cpu: 1         memory: 1Gi
```

</td>
<td>
Las solicitudes y los límites predeterminados para el proxy de Exchange Postgres. 
</td>
</tr>
<tr>
<td> postgres_exchangedb_keeper </td> 
<td>

```
  postgres_exchangedb_keeper:     resources:       requests:         cpu: "100m"         memory: "256Mi"       limits:         cpu: 2         memory: 2Gi
```

</td>
<td>
Las solicitudes y los límites predeterminados para el guardián de Exchange Postgres. 
</td>
</tr>
<tr>
<td> postgres_agbotdb_sentinel </td> 
<td>

```
  postgres_agbotdb_sentinel:     resources:       requests:         cpu: "100m"         memory: "256Mi"       limits:         cpu: 1         memory: 1Gi
```

</td>
<td>
Las solicitudes y los límites predeterminados para el centinela de Postgres del bot de acuerdo. 
</td>
</tr>
<tr>
<td> postgres_agbotdb_proxy </td> 
<td>

```
  postgres_agbotdb_proxy:     resources:       requests:         cpu: "100m"         memory: "256Mi"       limits:         cpu: 1         memory: 1Gi
```

</td>
<td>
Las solicitudes y los límites predeterminados para el proxy de postgres del bot de acuerdo. 
</td>
</tr>
<tr>
<td> postgres_agbotdb_keeper </td> 
<td>

```
  postgres_agbotdb_keeper:     resources:       requests:         cpu: "100m"         memory: "256Mi"       limits:         cpu: 2         memory: 2Gi
```

</td>
<td>
Las solicitudes y los límites predeterminados para el poseedor de postgres del bot de acuerdo. 
</td>
</tr>
</table>

### Opciones de configuración del tamaño de la base de datos local de EamHub

| Valor de configuración de componentes | Tamaño de volumen persistente predeterminado | Descripción |
| :---: | :---: | :---: |
| postgres_exchangedb_storage_size | 20Gi | Tamaño de la base de datos de Exchange Postgres. |
| postgres_agbotdb_storage_size | 20Gi | Size of the postgres agbot database. |
| mongo_cssdb_storage_size | 20Gi | Tamaño de la base de datos de CSS de mongo. |

## Configuración de la traducción de API Exchange

Puede configurar la API exchange de {{site.data.keyword.ieam}} para devolver respuestas en un idioma específico. Para ello, defina una variable de entorno con un **LANG** soportado de su elección (el valor predeterminado es **en**):

```
oc set env deployment <CUSTOM_RESOURCE_NAME>-exchange HZN_EXCHANGE_LANG=<LANG>
```
{: codeblock}

**Nota:** Para obtener una lista de los códigos de idioma soportados, consulte la primera tabla en la página [Idiomas soportados](../getting_started/languages.md).

## Configuración de base de datos remota
{: #remote}

**Nota**: No se da soporte a la conmutación entre bases de datos remotas y locales.

Para instalar con bases de datos remotas, cree el recurso personalizado EamHub durante la instalación con el valor adicional en el campo **spec**:
```
spec:   ieam_local_databases: false   license:     accept: true
```
{: codeblock}

Rellene la siguiente plantilla para crear un secreto de autenticación, asegúrese de leer cada comentario para cerciorarse de que se ha rellenado correctamente y guárdelo en **edge-auth-overrides.yaml**:
```
apiVersion: v1 kind: Secret metadata:   # NOTA: al nombre se le -debe- añadir como prefijo el nombre que se ha dado al recurso personalizado, toma 'ibm-edge' como valor predeterminado   #name: <NOMBRE_RP>-auth-overrides   name: ibm-edge-auth-overrides type: Opaque stringData:   # valores de conexión de agbot postgresql eliminar comentario y sustituir por los valores a utilizar   agbot-db-host: "<Nombre de host único de la base de datos remota>"   agbot-db-port: "<Puerto único en el que se ejecuta la base de datos>"   agbot-db-name: "<Nombre de la base de datos a utilizar en la instancia de postgresql>"   agbot-db-user: "<Nombre de usuario utilizado para conectarse>"   agbot-db-pass: "<Contraseña utilizada para conectarse>"   agbot-db-ssl: "<disable|require|verify-full>"   # Asegurar sangría correcta (cuatro espacios)   agbot-db-cert: |-     -----BEGIN CERTIFICATE-----
    ....
    -----END CERTIFICATE-----

  # valores de conexión de exchange postgresql   exchange-db-host: "<Nombre de host único de la base de datos remota>"   exchange-db-port: "<Puerto único en el que se ejecuta la base de datos>"   exchange-db-name: "<Nombre de la base de datos a utilizar en la instancia de postgresql>"   exchange-db-user: "<Nombre de usuario utilizado para conectarse>"   exchange-db-pass: "<Contraseña utilizada para conectarse>"   exchange-db-ssl: "<disable|require|verify-full>"   #  Asegurar sangría correcta (cuatro espacios)   exchange-db-cert: |-     -----BEGIN CERTIFICATE-----
    ....
    -----END CERTIFICATE-----

  # valores de conexión de css mongodb   css-db-host: "<Lista separada por comas incluyendo puertos: nombrehost.dominio:puerto,nombrehost2.dominio:puerto2 >"   css-db-name: "<Nombre de la base de datos a utilizar en la instancia de mongodb>"   css-db-user: "<Nombre de usuario utilizado para conectarse>"   css-db-pass: "<Contraseña utilizada para conectarse>"   css-db-auth: "<Nombre de la base de datos utilizada para almacenar credenciales de usuario>"   css-db-ssl: "<true|false>"   # Asegurar sangría correcta (cuatro espacios)   css-db-cert: |-     -----BEGIN CERTIFICATE-----
    ....
    -----END CERTIFICATE-----
```
{: codeblock}

Cree el secreto:
```
oc apply -f edge-auth-overrides.yaml
```
{: codeblock}

Observe los registros de operador como documentados en la sección [Bucle de control de operador](./configuration.md#remote).


## Configuración de escalado
{: #scale}

La configuración de recursos personalizados de EamHub expone los parámetros de configuración que podrían ser necesarios para aumentar los recursos a los pods en el centro de gestión de {{site.data.keyword.ieam}}  para dar soporte a un gran número de nodos periféricos.
Los clientes deben supervisar el consumo de recursos de los  pods de {{site.data.keyword.ieam}}, especialmente de los bots de intercambios y acuerdos (agbots) y añadir recursos cuando sea necesario. Consulte [Acceso al {{site.data.keyword.ieam}} Panel de Grafana](../admin/monitoring.md) La plataforma OpenShift reconoce estas actualizaciones y las aplica automáticamente a los PODS de {{site.data.keyword.ieam}} que se ejecutan bajo {{site.data.keyword.ocp}}.

Restricciones

Con las asignaciones de recursos predeterminadas y TLS interno entre los pods de {{site.data.keyword.ieam}} inhabilitados, IBM ha probado hasta 40.000 nodos periféricos registrados obteniendo 40.000 instancias de servicio desplegadas con actualizaciones de la política de despliegue que afectan al 25% (o 10.000) de los servicios desplegados.

Para dar soporte a 40.000 nodos periféricos registrados, cuando se habilita el TLS interno entre los pods de {{site.data.keyword.ieam}}, los pods de Exchange requieren recursos de CPU adicionales. 
Realice el cambio siguiente en la configuración de recursos personalizados de EamHub

Añada la siguiente sección bajo **spec**:

```
spec:   exchange_resources:     requests:       memory: 512Mi       cpu: 10m     limits:       memory: 2Gi       cpu: 5
```
{: codeblock}

Para dar soporte a más de 90.000 despliegues de servicio, realice el cambio siguiente en la configuración de recursos personalizados de EamHub.

Añada la siguiente sección bajo **spec**:

```
spec:   agbot_resources:     requests:       memory: 1Gi       cpu: 10m     limits:       memory: 4Gi       cpu: 2
```
{: codeblock}

