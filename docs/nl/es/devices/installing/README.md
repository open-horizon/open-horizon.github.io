# IBM Edge Computing Manager

## Introducción

IBM Edge Computing Manager for Devices proporciona una **Plataforma de gestión de aplicaciones** de extremo a extremo para aplicaciones desplegadas en dispositivos periféricos típicas en despliegues de IoT. Esta plataforma automatiza completamente la tarea de desplegar de forma segura las revisiones de las cargas de trabajo periféricas en miles de dispositivos periféricos desplegados en campo y libera a los desarrolladores de aplicaciones de realizarla. En lugar de esto, el desarrollador de aplicaciones puede centrarse en la tarea de escribir el código de la aplicación en cualquier lenguaje de programación como un contenedor de Docker de despliegue independiente. Esta plataforma asume la carga de desplegar la solución de negocio completa como una orquestación de varios niveles de contenedores de Docker en todos los dispositivos de forma segura y sin problemas.

## Requisitos previos

* Red Hat OpenShift Container Platform 4.2
* IBM Multicloud Management Core 1.2
* Si está alojando sus propias bases de datos, suministre dos instancias de PostgreSQL y una instancia de MongoDB para almacenar datos para los componentes de IBM Edge Computing Manager for Devices. Consulte la sección **Almacenamiento** que figura a continuación para conocer los detalles.
* Un host de Ubuntu Linux o macOS desde el que controlar la instalación. Debe tener el software siguiente instalado:
  * [CLI de Kubernetes (kubectl)](https://kubernetes.io/docs/tasks/tools/install-kubectl/) versión 1.14.0 o más reciente
  * [CLI de IBM Cloud Pak (cloudctl)](https://www.ibm.com/support/knowledgecenter/SSFC4F_1.2.0/cloudctl/icp_cli.html)
  * [CLI de OpenShift (oc)](https://docs.openshift.com/container-platform/4.2/cli_reference/openshift_cli/getting-started-cli.html)
  * [CLI de Helm](https://helm.sh/docs/using_helm/#installing-the-helm-client) versión 2.9.1 o más reciente
  * Otros paquetes de software:
    * jq
    * git
    * docker (versión 18.06.01 o posterior)
    * make

## Requisitos de SecurityContextConstraints de Red Hat OpenShift

El nombre de `SecurityContextConstraints` predeterminado: [`restricted`](https://ibm.biz/cpkspec-scc) se ha verificado para esta gráfica. Este release está limitado al despliegue en el espacio de nombres `kube-system` y utiliza la cuenta de servicio `default` además de crear sus propias cuentas de servicio para las subgráficas de base de datos opcionales.

## Detalles de gráfica

Esta gráfica de helm instala y configura los contenedores certificados de IBM Edge Computing Manager for Devices en un entorno OpenShift. Se instalarán los componentes siguientes:

* IBM Edge Computing Manager for Devices - Exchange
* IBM Edge Computing Manager for Devices - AgBots
* IBM Edge Computing Manager for Devices - Cloud Sync Service (parte del Sistema de gestión de modelos)
* IBM Edge Computing Manager for Devices - User Interface (consola de gestión)

## Recursos necesarios

Para obtener información sobre los recursos necesarios, consulte [Instalación - Dimensionamiento](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/devices/installing/install.html#size).

## Requisitos de almacenamiento y base de datos

Se necesitan tres instancias de base de datos para almacenar los datos de componente de IBM Edge Computing Manager for Devices.

De forma predeterminada, el gráfico instalará tres bases de datos persistentes con los dimensionamientos de volúmenes que se indican a continuación, mediante una clase de almacenamiento dinámico de Kubernetes definida de forma predeterminada (o configurada por el usuario).

**Nota:** estas bases de datos predeterminadas no están pensadas para su uso en producción. Para utilizar sus propias bases de datos gestionadas, consulte los requisitos que figuran a continuación y siga los pasos de la sección **Configurar bases de datos remotas**.

* PostgreSQL: datos de Stores Exchange y AgBot
  * Se necesitan 2 instancias distintas, cada una con 10 GB de almacenamiento como mínimo
  * La instancia debe admitir 100 conexiones como mínimo
  * Para el uso en producción, estas instancias deben ser de alta disponibilidad
* MongoDB: datos de Stores Cloud Sync Service
  * Se necesita 1 instancia con 50 GB de almacenamiento como mínimo. **Nota:** el tamaño necesario es altamente dependiente del tamaño y el número de modelos de servicios periféricos que almacene y utilice.
  * Para el uso en producción, esta instancia debe ser de alta disponibilidad

**Nota:** el usuario es responsable de los procedimientos de copia de seguridad/restauración si utiliza propias bases de datos gestionadas propias.
Consulte la sección **Copia de seguridad y recuperación** para conocer los procedimientos de base de datos predeterminados.

## Supervisión de recursos

Cuando IBM Edge Computing Manager for Devices está instalado, configura automáticamente la supervisión del producto y de los pods en los que se ejecuta. Los datos de supervisión se pueden ver en el panel de instrumentos de Grafana de la consola de gestión en las ubicaciones siguientes:

* `https://<MANAGEMENT_URL:PORT>/grafana/d/kube-system-edge-computing-overview/edge-computing-overview`
* `https://<MANAGEMENT_URL:PORT>/grafana/d/kube-system-edge-computing-pod-overview/edge-computing-pod-overview`

## Configuración

#### Configurar bases de datos remotas

1. Para utilizar sus propias bases de datos gestionadas, busque el siguiente parámetro de configuración de helm en `values.yaml` y cambie el valor a `false`:

```yaml
localDBs:
  enabled: true
```

2. Cree un archivo (llamado, por ejemplo, `dbinfo.yaml`) que empiece con este contenido de plantilla:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: edge-computing-remote-dbs
  labels:
    release: edge-computing
type: Opaque
stringData:
  # valores de conexión de postgresql de agbot
  agbot-db-host: "Nombre de host único de la base de datos remota"
  agbot-db-port: "Puerto único en el que se ejecuta la base de datos"
  agbot-db-name: "El nombre de la base de datos que se va a utilizar en la instancia postgresql"
  agbot-db-user: "Nombre de usuario utilizado para conectar"
  agbot-db-pass: "Contraseña utilizada para conectar"
  agbot-db-ssl: "Opciones de SSL: <disable|require|verify-full>"

  # exchange postgresql connection settings
  exchange-db-host: "Nombre de host único de la base de datos remota"
  exchange-db-port: "Puerto único en el que se ejecuta la base de datos"
  exchange-db-name: "El nombre de la base de datos que se va a utilizar en la instancia postgresql"
  exchange-db-user: "Nombre de usuario utilizado para conectar"
  exchange-db-pass: "Contraseña utilizada para conectar"
  exchange-db-ssl: "Opciones de SSL: <disable|require|verify-full>"

  # css mongodb connection settings
  css-db-host: "<nombre_de_host>:<puerto>,<nombre_de_host2>:<puerto2> separados por comas"
  css-db-name: "El nombre de la base de datos que se va a utilizar en la instancia de mongodb"
  css-db-user: "Nombre de usuario utilizado para conectar"
  css-db-pass: "Contraseña utilizada para conectar"
  css-db-auth: "El nombre de la base de datos utilizada para almacenar credenciales de usuario"
  css-db-ssl: "Opciones de SSL: <true|false>"

  trusted-certs: |-
    -----BEGIN CERTIFICATE-----
    ....
    -----END CERTIFICATE-----
    -----BEGIN CERTIFICATE-----
    ....
    -----END CERTIFICATE-----
```

3. Edite `dbinfo.yaml` para proporcionar la información de acceso para las bases de datos que ha suministrado. Cumplimente toda la información entre las comillas (manteniendo los valores entrecomillados). Al añadir los certificados de confianza, asegúrese de que cada línea está sangrada 4 espacios para garantizar la lectura correcta del archivo yaml. Si 2 o más de las bases de datos utilizan el mismo certificado, el certificado **no** se debe repetir en `dbinfo.yaml`. Guarde el archivo y a continuación, ejecute:

```bash
oc --namespace kube-system apply -f dbinfo.yaml
```


#### Configuración avanzada

Para cambiar cualquiera de los parámetros de configuración de helm predeterminados, puede revisar los parámetros y las descripciones mediante el mandato `grep` y a continuación ver/editar los valores correspondientes en `values.yaml`:

```bash
grep -v -E '(^ *#|__metadata)' ibm_cloud_pak/values-metadata.yaml
vi values.yaml   # o utillice su editor preferido
```

## Instalación de la gráfica

**Notas:**

* Se trata de una instalación solo de CLI, la instalación desde GUI no está soportada

* Ya debe haber completado los pasos de [Instalación de la infraestructura de IBM Edge Computing Manager for Devices - Proceso de instalación](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/devices/installing/install.html#process)
* Solo puede haber una instancia de IBM Edge Computing Manager for Devices instalada por clúster y solo puede estar instalada en el espacio de nombres de `kube-system`.
* La actualización desde IBM Edge Computing Manager for Devices 3.2 no está soportada

Ejecute el script de instalación proporcionado para instalar IBM Edge Computing Manager for Devices. Los pasos principales que el script lleva a cabo son: instalar la gráfica de helm y configurar el entorno después de la instalación (crear agbot, org y servicios de patrón/política).

```bash
ibm_cloud_pak/pak_extensions/full-install/install-edge-computing.sh
```

**Nota:** según la velocidad de la red, transcurrirán algunos minutos hasta que las imágenes se descarguen, los pods pasen a estado RUNNING y se activen todos los servicios.

### Verificación de la gráfica

* El script anterior verifica que las pods se están ejecutando y que el agbot y Exchange están respondiendo. Busque un mensaje "RUNNING" y "PASSED" hacia el final de la instalación.
* Si es "FAILED", la salida le pedirá que busque más información en los registros específicos.
* Si es "PASSED", la salida mostrará los detalles de las pruebas que se han ejecutado y dos elementos más para verificar
  * Vaya a la consola de interfaz de usuario de IBM Edge Computing Manager en el URL indicado al final del registro.
    * `https://<MANAGEMENT_URL:PORT>/edge`

## Acciones posteriores a la instalación

Siga los pasos que se indican en [Configuración posterior a la instalación](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/devices/installing/install.html#postconfig).

## Desinstalación de la gráfica

**Nota:** si está desinstalando con bases de datos locales configuradas, **se suprimirán todos los datos**. Si desea conservar estos datos antes de la desinstalación, consulte la sección **Procedimiento de copia de seguridad** que figura a continuación.

Vuelva a la ubicación de este archivo README.md y ejecute el script de desinstalación proporcionado para automatizar las tareas de desinstalación. Los pasos principales cubiertos por el script son: desinstalación de gráficas de helm, eliminación de secretos. En primer lugar, inicie la sesión en el clúster como administrador de clúster utilizando `cloudctl`. A continuación:

```bash
ibm_cloud_pak/pak_extensions/uninstall/uninstall-edge-computing.sh <nombre-clúster>
```

**Nota:** si ha suministrado bases de datos remotas, el secreto de autenticación se suprimirá pero no se ejecutarán tareas para desmantelar/suprimir datos de esas bases de datos remotas. Si desea suprimir esos datos, hágalo ahora.

## Acceso basado en roles

* La autoridad del administrador de clúster en el espacio de nombres de `kube-system` es necesaria para instalar gestionar este producto.
* Autenticación de Exchange y roles:
  * IAM proporciona la autenticación de todos los administradores y los usuarios de Exchange a través de las claves de API generadas con el mandato `cloudctl`
  * Los administradores de Exchange deben tener el privilegio `admin` dentro de Exchange. Con ese privilegio, pueden gestionar todos los usuarios, nodos, servicios, patrones y políticas dentro de su organización de Exchange
  * Los usuarios que no sean administradores de Exchange solo podrán gestionar usuarios, nodos, servicios, patrones y políticas que hayan creado.

## Seguridad

* TLS se utiliza para todos los datos que entran/salen del clúster de OpenShift a través de ingress. En este release, no se utiliza TLS **dentro** del clúster de OpenShift para la comunicación de nodo a nodo. Si lo desea, puede configurar la malla de servicios de Red Hat OpenShift para la comunicación entre los microservicios. Consulte [Understanding Red Hat OpenShift Service Mesh](https://docs.openshift.com/container-platform/4.2/service_mesh/service_mesh_arch/understanding-ossm.html#understanding-ossm).
* Esta gráfica no proporciona ningún cifrado de los datos en reposo.  Es el administrador el que debe configurar el cifrado de almacenamiento.

## Copia de seguridad y recuperación

### Procedimiento de copia de seguridad

Ejecute estos mandatos después de conectar con el clúster en una ubicación que tenga espacio adecuado para almacenar estas copias de seguridad.


1. Cree un directorio que se utilice para almacenar las copias de seguridad que se indican a continuación, ajústelo tal como desee

```bash
export BACKUP_DIR=/tmp/edge-computing-backup/$(date +%Y%m%d_%H%M%S)
mkdir -p $BACKUP_DIR
```

2. Ejecute lo siguiente para realizar copias de seguridad de la autenticación/los secretos

```bash
oc -n kube-system get secret edge-computing -o yaml > $BACKUP_DIR/edge-computing-secret.yaml && \
oc -n kube-system get secret edge-computing-agbotdb-postgresql-auth-secret -o yaml > $BACKUP_DIR/edge-computing-agbotdb-postgresql-auth-secret-backup.yaml && \
oc -n kube-system get secret edge-computing-exchangedb-postgresql-auth-secret -o yaml > $BACKUP_DIR/edge-computing-exchangedb-postgresql-auth-secret-backup.yaml && \
oc -n kube-system get secret edge-computing-css-db-ibm-mongodb-auth-secret -o yaml > $BACKUP_DIR/edge-computing-css-db-ibm-mongodb-auth-secret-backup.yaml
```

3. Ejecute lo siguiente para hacer una copia de seguridad del contenido de la base de datos

```bash
oc -n kube-system exec edge-computing-exchangedb-keeper-0 -- bash -c "export PGPASSWORD=$(oc -n kube-system get secret edge-computing -o jsonpath="{.data.exchange-db-pass}" | base64 --decode) && pg_dump -U admin -h edge-computing-exchangedb-proxy-svc -F t postgres > /stolon-data/exchange-backup.tar" && \
oc -n kube-system cp edge-computing-exchangedb-keeper-0:/stolon-data/exchange-backup.tar $BACKUP_DIR/exchange-backup.tar
```

```bash
oc -n kube-system exec edge-computing-agbotdb-keeper-0 -- bash -c "export PGPASSWORD=$(oc -n kube-system get secret edge-computing -o jsonpath="{.data.agbot-db-pass}" | base64 --decode) && pg_dump -U admin -h edge-computing-agbotdb-proxy-svc -F t postgres > /stolon-data/agbot-backup.tar" && \
oc -n kube-system cp edge-computing-agbotdb-keeper-0:/stolon-data/agbot-backup.tar $BACKUP_DIR/agbot-backup.tar
```

```bash
oc -n kube-system exec edge-computing-cssdb-server-0 -- bash -c "mkdir -p /data/db/backup; mongodump -u admin -p $(oc -n kube-system get secret edge-computing -o jsonpath="{.data.css-db-pass}" | base64 --decode) --out /data/db/css-backup" && \
oc -n kube-system cp edge-computing-cssdb-server-0:/data/db/css-backup $BACKUP_DIR/css-backup
```

4. Una vez verificadas las copias de seguridad, elimine las copias de seguridad de los contenedores sin estado

```bash
oc -n kube-system exec edge-computing-exchangedb-keeper-0 -- bash -c "rm -f /stolon-data/exchange-backup.tar"
```

```bash
oc -n kube-system exec edge-computing-agbotdb-keeper-0 -- bash -c "rm -f /stolon-data/agbot-backup.tar"
```

```bash
oc -n kube-system exec edge-computing-cssdb-server-0 -- bash -c "rm -rf /data/db/css-backup"
```

### Procedimiento de restauración

**Nota:** si se restaura en un nuevo clúster, ese 'nombre de clúster' debe coincidir con el nombre del clúster del que se han sacado las copias de seguridad.

1. Suprima los secretos preexistentes del clúster
```bash
oc -n kube-system delete secret edge-computing edge-computing-agbotdb-postgresql-auth-secret edge-computing-exchangedb-postgresql-auth-secret edge-computing-css-db-ibm-mongodb-auth-secret;
```

2. Exporte estos valores a la máquina local

```bash
export BACKUP_DIR=/tmp/edge-computing-backup/<Insertar indicación de fecha y hora de copia de seguridad deseada AAAAMMDD_HHMMSS>
```

3. Ejecute lo siguiente para restaurar la autenticación/los secretos

```bash
oc apply -f $BACKUP_DIR
```

4. Vuelva a instalar IBM Edge Computing Manager antes de continuar, siga las instrucciones de la sección **Instalación de la gráfica**

5. Ejecute lo siguiente para copiar copias de seguridad en los contenedores y restaurarlas

```bash
oc -n kube-system cp $BACKUP_DIR/exchange-backup.tar edge-computing-exchangedb-keeper-0:/stolon-data/exchange-backup.tar && \
oc exec -n kube-system edge-computing-exchangedb-keeper-0 -- bash -c "export PGPASSWORD=$(oc get secret edge-computing -o jsonpath="{.data.exchange-db-pass}" | base64 --decode) && pg_restore -U admin -h edge-computing-exchangedb-proxy-svc -d postgres -c /stolon-data/exchange-backup.tar"
```

```bash
oc -n kube-system cp $BACKUP_DIR/agbot-backup.tar edge-computing-agbotdb-keeper-0:/stolon-data/agbot-backup.tar && \
oc exec -n kube-system edge-computing-agbotdb-keeper-0 -- bash -c "export PGPASSWORD=$(oc get secret edge-computing -o jsonpath="{.data.agbot-db-pass}" | base64 --decode) && pg_restore -U admin -h edge-computing-agbotdb-proxy-svc -d postgres -c /stolon-data/agbot-backup.tar"
```

```bash
oc -n kube-system cp $BACKUP_DIR/css-backup edge-computing-cssdb-server-0:/data/db/css-backup && \
oc exec -n kube-system edge-computing-cssdb-server-0 -- bash -c "mongorestore -u admin -p $(oc get secret edge-computing -o jsonpath="{.data.css-db-pass}" | base64 --decode) /data/db/css-backup";
```

6. Ejecute lo siguiente para renovar las conexiones de base de datos de pod de Kubernetes
```bash
for POD in $(oc get pods -n kube-system | grep -E '\-agbot\-|\-css\-|\-exchange\-' | awk '{print $1}'); do oc delete pod $POD -n kube-system; done
```

## Limitaciones

* Límites de instalación: este producto sólo se puede instalar una vez, y sólo en el espacio de nombres de `kube-system`
* En este release, no hay privilegios de autorización distintos para la administración del producto y para la operación del producto.

## Documentación

* Consulte el documento [Instalación](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/devices/installing/install.html) del Knowledge Center para obtener directrices adicionales y actualizaciones.

## Copyright

© Copyright IBM Corporation 2020. Reservados todos los derechos.
