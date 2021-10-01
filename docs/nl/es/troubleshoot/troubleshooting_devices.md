---

copyright:
years: 2019, 2020, 2021
lastupdated: "2021-09-01"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Sugerencias para la resolución de problemas
{: #troubleshooting_devices}

Consulte las preguntas siguientes cuando tenga un problema con {{site.data.keyword.edge_notm}}. Las sugerencias y guías de cada pregunta pueden ayudarle a resolver problemas comunes y obtener información para identificar las causas raíz.
{:shortdesc}

  * [¿Está instaladas las versiones publicadas actualmente de los paquetes de {{site.data.keyword.horizon}}?](#install_horizon)
  * [¿Está actualmente el agente de {{site.data.keyword.horizon}} activo y en ejecución?](#setup_horizon)
  * [¿Está configurado el nodo periférico para interactuar con {{site.data.keyword.horizon_exchange}}?](#node_configured)
  * [¿Se han iniciado los contenedores de Docker necesarios para el nodo periférico en ejecución?](#node_running)
  * [¿Están ejecutándose las versiones de contenedores de servicio esperadas?](#run_user_containers)
  * [¿Son los contenedores esperados estables?](#containers_stable)
  * [¿Están los contenedores Docker conectados en red correctamente?](#container_networked)
  * [¿Se puede acceder a los contenedores de dependencia dentro del contexto del contenedor?](#setup_correct)
  * [¿Los contenedores definidos por usuario están emitiendo mensajes de error en el registro?](#log_user_container_errors)
  * [¿Puede utilizar la instancia de la organización del intermediario Kafka de {{site.data.keyword.message_hub_notm}}?](#kafka_subscription)
  * [¿Se publican los contenedores en {{site.data.keyword.horizon_exchange}}?](#publish_containers)
  * [¿Incluye el patrón de despliegue publicado todos los servicios y las versiones necesarios?](#services_included)
  * [Sugerencias para la resolución de problemas específicos del entorno de {{site.data.keyword.open_shift_cp}}](#troubleshooting_icp)
  * [Resolución de errores de nodo](#troubleshooting_node_errors)
  * [¿Cómo se desinstala Podman de RHEL?](#uninstall_podman)

## ¿Está instaladas las versiones disponibles actualmente de los paquetes de {{site.data.keyword.horizon}}?
{: #install_horizon}

Asegúrese de que el software de {{site.data.keyword.horizon}} que está instalado en los nodos periféricos tenga siempre la última versión publicada.

En un sistema {{site.data.keyword.linux_notm}}, normalmente puede comprobar la versión de los paquetes de {{site.data.keyword.horizon}} instalados ejecutando este mandato:  
```
dpkg -l | grep horizon
```
{: codeblock}

Puede actualizar los paquetes de {{site.data.keyword.horizon}} que utilizan el gestor de paquetes en el sistema. Por ejemplo, en un sistema {{site.data.keyword.linux_notm}} basado en Ubuntu, utilice los mandatos siguientes para actualizar {{site.data.keyword.horizon}} a la versión actual:
```
sudo apt update sudo apt install -y blue horizon
```

## ¿Está actualmente el agente de {{site.data.keyword.horizon}} activo y en ejecución?
{: #setup_horizon}

Puede verificar que el agente se está ejecutando mediante este mandato de la CLI de {{site.data.keyword.horizon}}:
```
hzn node list | jq .
```
{: codeblock}

También puede utilizar el software de gestión del sistema del host para comprobar el estado del agente de {{site.data.keyword.horizon}}. Por ejemplo, en un sistema {{site.data.keyword.linux_notm}} basado en Ubuntu, puede utilizar el programa de utilidad `systemctl`:
```
sudo systemctl status horizon
```
{: codeblock}

Si el agente está activo, se mostrará una línea similar a la siguiente:
```
Active: active (running) since Thu 2020-10-01 17:56:12 UTC; 2 weeks 0 days ago
```
{: codeblock}

## ¿Está configurado el nodo periférico para interactuar con {{site.data.keyword.horizon_exchange}}? 
{: #node_configured}

Para verificar que puede comunicarse con {{site.data.keyword.horizon_exchange}}, ejecute este mandato:
```
hzn exchange version
```
{: codeblock}

Para verificar que {{site.data.keyword.horizon_exchange}} es accesible, ejecute este mandato:
```
hzn exchange user list
```
{: codeblock}

Una vez registrado el nodo periférico con {{site.data.keyword.horizon}}, puede verificar si el nodo está interactuando con {{site.data.keyword.horizon_exchange}} viendo la configuración de agente de {{site.data.keyword.horizon}} local. Ejecute este mandato para ver la configuración del agente:
```
hzn node list | jq .configuration.exchange_api
```
{: codeblock}

## ¿Se están ejecutando los contenedores de Docker necesarios para el nodo periférico?
{: #node_running}

Cuando el nodo periférico se registra con {{site.data.keyword.horizon}}, un agbot de {{site.data.keyword.horizon}} crea un acuerdo con el nodo periférico para ejecutar los servicios a los que se hace referencia en el tipo de pasarela (patrón de despliegue). Si no se crea dicho acuerdo, realice estas comprobaciones para resolver el problema.

Confirme que el nodo periférico está en el estado `configured` y tiene los valores `id` y `organization` correctos. Confirme además que la arquitectura que {{site.data.keyword.horizon}} notifica es la misma arquitectura que ha utilizado en los metadatos de los servicios. Ejecute este mandato para listar estos valores:
```
hzn node list | jq .
```
{: codeblock}

Si esos valores son los esperados, puede comprobar el estado de acuerdo del nodo periférico ejecutando: 
```
hzn agreement list | jq .
```
{: codeblock}

Si este mandato no muestra ningún acuerdo, es posible que estos acuerdos se hayan formado, pero es posible que se haya descubierto un problema. En ese caso, el acuerdo se puede cancelar antes de que pueda visualizarse en la salida del mandato anterior. Si se produce una cancelación de acuerdo, el acuerdo cancelado muestra un estado `terminated_description` en la lista de acuerdos archivados. Puede ver la lista archivada ejecutando este mandato: 
```
hzn agreement list -r | jq .
```
{: codeblock}

También se puede producir un problema antes de que se cree un acuerdo. Si se produce este problema, revise el registro de sucesos para que el agente {{site.data.keyword.horizon}} identifique posibles errores. Ejecute este mandato para ver el registro: 
```
hzn eventlog list
``` 
{: codeblock}

El registro de sucesos puede incluir: 

* La firma de los metadatos de servicio, específicamente el campo `deployment`, no se puede verificar. Normalmente este error significa que la clave pública de firma no se importa en el nodo periférico. Puede importar la clave mediante el mandato `hzn key import -k <pubkey>`. Puede ver las claves importadas en el nodo periférico local mediante el mandato `hzn key list`. Puede verificar que los metadatos de servicio de {{site.data.keyword.horizon_exchange}} se hayan firmado con la clave mediante este mandato:
  ```
  hzn exchange service verify -k $PUBLIC_KEY_FILE <id-servicio>
  ```
  {: codeblock} 

Sustituya `<ID-de-servicio>` por el ID del servicio. Este ID puede ser parecido al formato de ejemplo siguiente: `workload-cpu2wiotp_${CPU2WIOTP_VERSION}_${ARCH2}`.

* La vía de acceso de la imagen de Docker del campo `deployment` no es correcta. Confirme que en el nodo periférico puede realizar `docker pull` para esa vía de acceso de imagen.
* El agente de {{site.data.keyword.horizon}} del nodo periférico no tiene acceso al registro de Docker que aloja las imágenes de Docker. Si las imágenes de Docker en el registro de Docker remoto no se pueden leer universalmente, debe añadir las credenciales al nodo periférico mediante el mandato `docker login`. Debe completar este paso una vez, ya que las credenciales se recuerdan en el nodo periférico.
* Si un contenedor se está reiniciando continuamente, revise el registro de contenedor para obtener más detalles. Un contenedor puede reiniciarse continuamente cuando se lista durante sólo unos segundos o permanece en la lista como reiniciándose cuando se ejecuta el mandato `docker ps`. Puede ver el registro del contenedor para obtener detalles ejecutando este mandato:
  ```
  grep --text -E ' <id-servicio>\[[0-9]+\]' /var/log/syslog
  ```
  {: codeblock}

## ¿Se están ejecutando las versiones previstas del contenedor de servicios?
{: #run_user_containers}

Las versiones de contenedor se rigen por un acuerdo que se crea después de añadir el servicio al patrón de despliegue y después de registrar el nodo periférico para dicho patrón. Verifique que el nodo periférico tenga un acuerdo actual para el patrón ejecutando este mandato:

```
hzn agreement list | jq .
```
{: codeblock}

Si ha confirmado el acuerdo correcto para el patrón, utilice este mandato para ver los contenedores en ejecución. Asegúrese de que los contenedores definidos por el usuario aparecen en la lista y se están ejecutando:
```
docker ps
```
{: codeblock}

El agente de {{site.data.keyword.horizon}} puede tardar varios minutos una vez aceptado el acuerdo antes de que los contenedores correspondientes se descarguen, verifiquen y empiecen a ejecutarse. Este acuerdo depende principalmente de los tamaños de los propios contenedores, que deben extraerse de los repositorios remotos.

## ¿Son los contenedores esperados estables?
{: #containers_stable}

Compruebe si los contenedores son estables ejecutando este mandato:
```
docker ps
```
{: codeblock}

En la salida del mandato puede ver la duración de la ejecución de cada mandato. Si a lo largo del tiempo, observa que los contenedores se están reiniciando de forma inesperada, consulte los registros del contenedor para ver si hay errores.

Como práctica de desarrollo recomendada, considere la posibilidad de configurar el registro de servicios individuales ejecutando los mandatos siguientes (sólo sistemas {{site.data.keyword.linux_notm}}):
```bash
cat <<'EOF' > /etc/rsyslog.d/10-horizon-docker.conf $template DynamicWorkloadFile,"/var/log/workload/%syslogtag:R,ERE,1,DFLT:.*workload-([^\[]+)--end%.log"  :syslogtag, startswith, "workload-" -?DynamicWorkloadFile & stop :syslogtag, startswith, "docker/" -/var/log/docker_containers.log & stop :syslogtag, startswith, "docker" -/var/log/docker.log & stop EOF service rsyslog restart
```
{: codeblock}

Si ha completado el paso anterior, los registros de los contenedores se registran en archivos separados dentro del directorio `/var/log/workload/`. Utilice el mandato `docker ps` para buscar los nombres completos de los contenedores. Puede encontrar el archivo de registro de ese nombre, con un sufijo `.log`, en este directorio.

Si el registro de servicio individual no está configurado, los registros de servicio se añaden al registro de sistema con todos los demás mensajes de registro. Para consultar los datos de los contenedores, debe buscar el nombre del contenedor en la salida del registro del sistema dentro del archivo `/var/log/syslog`. Por ejemplo, puede buscar el registro ejecutando un mandato similar:
```
grep --text -E 'YOURSERVICENAME\[[0-9]+\]' /var/log/syslog
```
{: codeblock}

## ¿Están los contenedores correctamente conectados en red de Docker?
{: #container_networked}

Asegúrese de que los contenedores estén adecuadamente conectados en red de Docker, para que puedan acceder a los servicios necesarios. Ejecute este mandato para asegurarse de que puede ver las redes virtuales Docker activas en el nodo periférico:
```
docker network list
```
{: codeblock}

Para ver más información sobre las redes, utilice el mandato `docker inspect X`, donde `X` es el nombre de la red. La salida del mandato lista todos los contenedores que se ejecutan en la red virtual.

También puede ejecutar el mandato `docker inspect Y` en cada contenedor, donde `Y` es el nombre del contenedor, para obtener más información. Por ejemplo, consulte la información del contenedor `NetworkSettings` y busque en el contenedor `Networks`. Dentro de este contenedor, puede ver la serie de ID de red relevante y la información sobre cómo está representado el contenedor en la red. Esta información de representación incluye el contenedor `IPAddress` y la lista de alias de red que están en esta red. 

Los nombres de alias están disponibles para todos los contenedores de esta red virtual y estos nombres suelen ser utilizados por los contenedores en el patrón de despliegue de código para descubrir otros contenedores en la red virtual. Por ejemplo, puede denominar el servicio `myservice`. A continuación, otros contenedores pueden utilizar ese nombre directamente para acceder a él en la red, por ejemplo con el mandato `ping myservice`. El nombre de alias del contenedor se especifica en el campo `deployment` del archivo de definición de servicio correspondiente que ha pasado al mandato `hzn exchange service publish`.

Para obtener más información sobre los mandatos soportados por la interfaz de línea de mandatos de Docker, consulte [Docker command reference](https://docs.docker.com/engine/reference/commandline/docker/#child-commands).

## ¿Se puede acceder a los contenedores de dependencia dentro del contexto del contenedor?
{: #setup_correct}

Especifique el contexto de un contenedor en ejecución para resolver problemas en tiempo de ejecución mediante el mandato `docker exec`. Utilice el mandato `docker ps` para buscar el identificador del contenedor en ejecución y, a continuación, utilice un mandato que se parezca a lo siguiente para especificar el contexto. Sustituya `ID_CONTENEDOR` por el identificador del contenedor.
```
docker exec -it ID_CONTENEDOR /bin/sh
```
{: codeblock}

Si el contenedor incluye bash, puede que desee especificar `/bin/bash` en la parte final del mandato anterior en lugar de `/bin/sh`.

Cuando esté dentro del contexto de contenedor, puede utilizar mandatos como `ping` o `curl` para interactuar con los contenedores que necesita y verificar la conectividad.

Para obtener más información sobre los mandatos soportados por la interfaz de línea de mandatos de Docker, consulte [Docker command reference](https://docs.docker.com/engine/reference/commandline/docker/#child-commands).

## ¿Los contenedores definidos por usuario están emitiendo mensajes de error en el registro?
{: #log_user_container_errors}

Si ha configurado el registro de servicio individual, cada uno de los contenedores inicia la sesión en un archivo independiente en el directorio `/var/log/workload/`. Utilice el mandato `docker ps` para buscar los nombres completos de los contenedores. A continuación, busque un archivo con ese nombre con el sufijo `.log` dentro de este directorio.

Si el registro de servicio individual no está configurado, los registros de servicio se anotan en el registro del sistema con todos los demás detalles. Para consultar los datos, busque el registro de contenedor en la salida del registro del sistema dentro del directorio `/var/log/syslog`. Por ejemplo, busque el registro ejecutando un mandato similar a:
```
grep --text -E 'YOURSERVICENAME\[[0-9]+\]' /var/log/syslog
```
{: codeblock}

## ¿Puede utilizar la instancia de la organización del intermediario Kafka de {{site.data.keyword.message_hub_notm}}?
{: #kafka_subscription}

La suscripción a la instancia de Kafka para su organización desde {{site.data.keyword.message_hub_notm}} puede ayudarle a verificar que las credenciales de usuario de Kafka son correctas. Esta suscripción también puede ayudarle a verificar que la instancia de servicio de Kafka se está ejecutando en la nube y que el nodo periférico envía datos cuando se publica.

Para suscribirse al intermediario Kafka, instale el programa `kafkacat`. Por ejemplo, en un sistema {{site.data.keyword.linux_notm}} Ubuntu, utilice este mandato:

```bash
sudo apt install kafkacat
```
{: codeblock}

Después de la instalación, puede suscribirse mediante un mandato similar al ejemplo siguiente que utiliza las credenciales que suele colocar en las referencias de variables de entorno:

```bash
kafkacat -C -q -o end -f "%t/%p/%o/%k: %s\n" -b $EVTSTREAMS_BROKER_URL -X api.version.request=true -X security.protocol=sasl_ssl -X sasl.mechanisms=PLAIN -X sasl.username=token -X sasl.password=$EVTSTREAMS_API_KEY -t $EVTSTREAMS_TOPIC
```
{: codeblock}

Donde `EVTSTREAMS_BROKER_URL` es el URL al intermediario Kafka, `EVTSTREAMS_TOPIC` es el tema de Kafka y `EVTSTREAMS_API_KEY` es la clave de API para la autenticación con la API de {{site.data.keyword.message_hub_notm}}.

Si el mandato de suscripción es satisfactorio, el mandato se bloquea indefinidamente. El mandato espera a que se produzca una publicación en el intermediario Kafka y recupera y visualiza los mensajes resultantes. Si no ve mensajes del nodo periférico después de unos minutos, consulte el registro de servicio para ver los mensajes de error.

Por ejemplo, para consultar el registro del servicio `cpu2evtstreams`, ejecute este mandato:

* Para {{site.data.keyword.linux_notm}} y {{site.data.keyword.windows_notm}} 

```bash
tail -n 500 -f /var/log/syslog | grep -E 'cpu2evtstreams\[[0-9]+\]:'
```
{: codeblock}

* Para macOS

```bash
docker logs -f $(docker ps --filter 'name=-cpu2evtstreams' | tail -n +2 | awk '{print $1}')
```
{: codeblock}

## ¿Se publican los contenedores en {{site.data.keyword.horizon_exchange}}?
{: #publish_containers}

{{site.data.keyword.horizon_exchange}} es el almacén central para los metadatos sobre el código que se publica para los nodos periféricos. Si no ha firmado ni publicado el código en {{site.data.keyword.horizon_exchange}}, el código no se puede extraer en los nodos periféricos, que se verifican, y ejecutarse.

Ejecute el mandato `hzn` con los argumentos siguientes para ver la lista de código publicado para verificar que todos los contenedores de servicios se han publicado correctamente:

```
hzn exchange service list | jq .
hzn exchange service list $ORG_ID/$SERVICE | jq .
```
{: codeblock}

El parámetro `$ORG_ID` es el ID de la organización, y `$SERVICE` es el nombre del servicio sobre el que está obteniendo información.

## ¿Incluye el patrón de despliegue publicado todos los servicios y las versiones necesarios?
{: #services_included}

En cualquier nodo periférico donde esté instalado el mandato `hzn`, puede utilizar este mandato para obtener detalles sobre cualquier patrón de despliegue. Ejecute el mandato `hzn` con los argumentos siguientes para extraer la lista de patrones de despliegue de {{site.data.keyword.horizon_exchange}}: 

```
hzn exchange pattern list | jq .
hzn exchange pattern list $ORG_ID/$PATTERN | jq .
```
{: codeblock}

El parámetro `$ORG_ID` es el ID de la organización, y `$PATTERN` es el nombre del patrón de despliegue sobre el que está obteniendo información.

## Sugerencias para la resolución de problemas específicas para el entorno de {{site.data.keyword.open_shift_cp}}
{: #troubleshooting_icp}

Consulte este contenido para ayudarle a resolver problemas comunes en los entornos {{site.data.keyword.open_shift_cp}} relacionados con {{site.data.keyword.edge_notm}}. Estas sugerencias pueden ayudarle a resolver problemas comunes y a obtener información para identificar las causas raíz.
{:shortdesc}

### ¿Se han configurado correctamente las credenciales de {{site.data.keyword.edge_notm}} para su uso en el entorno {{site.data.keyword.open_shift_cp}}?
{: #setup_correct}

Necesita una cuenta de usuario de {{site.data.keyword.open_shift_cp}} para completar cualquier acción dentro de {{site.data.keyword.edge_notm}} en este entorno. También necesita una clave de API creada desde esa cuenta.

Para verificar las credenciales de {{site.data.keyword.edge_notm}} en este entorno, ejecute este mandato:

   ```
   hzn exchange user list
   ```
   {: codeblock}

Si se devuelve desde Exchange una entrada con formato JSON que muestra uno o más usuarios, las credenciales de {{site.data.keyword.edge_notm}} se han configurado correctamente.

Si se devuelve una respuesta de error, puede realizar pasos para solucionar los problemas de configuración de las credenciales.

Si el mensaje de error indica una clave de API incorrecta, puede crear una nueva clave de API que utilice los mandatos siguientes.

Consulte [Creación de la clave de API](../hub/prepare_for_edge_nodes.md).

## Resolución de errores de nodo
{: #troubleshooting_node_errors}

{{site.data.keyword.edge_notm}} publica un subconjunto de registros de sucesos en Exchange que se puede visualizar en la {{site.data.keyword.gui}}. Estos errores se enlazan a la orientación para la resolución de
{:shortdesc}

  - [Error de carga de imagen](#eil)
  - [Error de configuración de despliegue](#eidc)
  - [Error de inicio de contenedor](#esc)
  - [Error interno de TLS de clúster periférico de OCP](#tls_internal)

### Error de carga de imagen
{: #eil}

Este error se produce cuando la imagen de servicio a la que se hace referencia en la definición de servicio no existe en el repositorio de imágenes. Para solucionar este error:

1. Vuelva a publicar el servicio sin el distintivo **-I**.
    ```
    hzn exchange service publish -f <archivo-definición-servicio>
    ```
    {: codeblock}

2. Envíe la imagen de servicio directamente al repositorio de imágenes. 
    ```
    docker push <nombre de imagen>
    ```
    {: codeblock} 
    
### Error de configuración de despliegue
{: #eidc}

Este error se produce cuando las configuraciones de despliegue de definiciones de servicio especifican un enlace a un archivo protegido por root. Para solucionar este error:

1. Enlace el contenedor con un archivo que no esté protegido por root.
2. Cambie los permisos de archivo para que los usuarios puedan leer y escribir en el archivo.

### Error de inicio de contenedor
{: #esc}

Este error se produce cuando docker encuentra un error al iniciar el contenedor de servicio. Es posible que el mensaje de error contenga detalles que indiquen por qué el inicio del contenedor ha fallado. Los pasos de resolución dependen del error. Se pueden producir los errores siguientes:

1. El dispositivo ya está utilizando un puerto publicado que se especifica en las configuraciones de despliegue. Para resolver el error: 

    - Correlacione un puerto diferente con el puerto de contenedor de servicio. El número de puerto visualizado no tiene que coincidir con el número de puerto de servicio.
    - Detenga el programa que está utilizando el mismo puerto.

2. Un puerto publicado que se especifica en las configuraciones de despliegue no es un número de puerto válido. Los números de puerto deben ser un número en el rango 1-65535.
3. Un nombre de volumen de las configuraciones de despliegue no es una vía de acceso de archivo válida. Las vías de acceso de volumen deben especificarse por sus vías de acceso absolutas (no relativas). 

### Error interno de TLS de clúster periférico de OCP

  ```
  Error from server: error dialing backend: remote error: tls: internal error
  ```
  {: codeblock} 

Si ve este error al final del proceso de instalación del agente del clúster o al intentar interactuar con el pod del agente, es posible que haya un problema con las solicitudes de firma de certificados (CSR) del clúster de OCP. 

1. Compruebe si tiene algún CSR en estado pendiente:

    ```
    oc get csr
    ```
    {: codeblock} 

2. Apruebe los CSR pendientes:

  ```
  oc adm certificate approve <csr-name>
  ```
  {: codeblock}
    
**Nota**: Puede aprobar todos los CSR con un mandato:

  ```
  for i in `oc get csr |grep Pending |awk '{print $1}'`; do oc adm certificate approve $i; done
  ```
  {: codeblock}

### Información adicional

Para obtener más información, consulte:
  * [Resolución de problemas](../troubleshoot/troubleshooting.md)
