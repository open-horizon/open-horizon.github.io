# IBM&reg; Edge Application Manager

## Introducción

IBM Edge Application Manager proporciona una **Plataforma de gestión de aplicaciones**
de principio a fin para aplicaciones desplegadas en dispositivos periféricos en despliegues
de IoT. Esta plataforma automatiza completamente la tarea de desplegar de forma segura las revisiones de las cargas de trabajo periféricas en miles de dispositivos periféricos desplegados en campo y libera a los desarrolladores de aplicaciones de realizarla. En lugar de esto, el desarrollador de aplicaciones puede centrarse en la tarea de escribir el código de la aplicación en cualquier lenguaje de programación como un contenedor de Docker de despliegue independiente. Esta plataforma asume la carga de desplegar la solución de negocio completa como una orquestación de varios niveles de contenedores de Docker en todos los dispositivos de forma segura y sin problemas.

https://www.ibm.com/cloud/edge-application-manager

## Requisitos previos

Consulte lo siguiente para conocer los
[Requisitos
previos](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/hub/offline_installation.html#prereq).

## Requisitos de SecurityContextConstraints de Red Hat OpenShift

El nombre de `SecurityContextConstraints` predeterminado: [`restricted`](https://ibm.biz/cpkspec-scc) se ha verificado para esta gráfica. Este
release está limitado al despliegue en el espacio de nombres `kube-system` y crea cuentas
de servicio para la gráfica principal y cuentas de servicio adicionales para las subgráficas de base de datos
locales predeterminados.

## Detalles de gráfica

Esta gráfica de Helm instala y configura los contenedores certificados de IBM Edge Application Manager en
un entorno de OpenShift. Se instalarán los componentes siguientes:

* IBM Edge Application Manager - Exchange
* IBM Edge Application Manager - AgBots
* IBM Edge Application Manager - Servicio de sincronización de nube (parte del Sistema de gestión de modelos)
* IBM Edge Application Manager - Interfaz de usuario (consola de gestión)

## Recursos necesarios

Consulte lo siguiente para conocer el
[Dimensionamiento](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/hub/cluster_sizing.html).

## Requisitos de almacenamiento y base de datos

Se necesitan tres instancias de base de datos para almacenar los datos de componente de
IBM Edge Application Manager.

De forma predeterminada, la gráfica instalará tres bases de datos persistentes con los
dimensionamientos de volumen siguientes, utilizando una clase de almacenamiento dinámico de
kubernetes predeterminada definida (o configurada por el usuario). Si se utiliza una clase de almacenamiento
que no permite la expansión de volumen, asegúrese de permitir la expansión adecuadamente.

**Nota:** estas bases de datos predeterminadas no están pensadas para su uso en producción. Para utilizar sus propias bases de datos gestionadas, consulte los requisitos que figuran a continuación y siga los pasos de la sección **Configurar bases de datos remotas**.

* PostgreSQL: datos de Stores Exchange y AgBot
  * Se necesitan 2 instancias independientes, cada una con 20 GB de almacenamiento como mínimo
  * La instancia debe admitir 100 conexiones como mínimo
  * Para el uso en producción, estas instancias deben ser de alta disponibilidad
* MongoDB: datos de Stores Cloud Sync Service
  * Se necesita 1 instancia con 50 GB de almacenamiento como mínimo. **Nota:** el tamaño necesario es altamente dependiente del tamaño y el número de modelos de servicios periféricos que almacene y utilice.
  * Para el uso en producción, esta instancia debe ser de alta disponibilidad

**Nota:** el usuario es responsable de los procedimientos/la cadencia de copia de seguridad
para estas bases de datos predeterminadas, así como de sus propias bases de datos gestionadas.
Consulte la sección **Copia de seguridad y recuperación** para conocer los procedimientos de base de datos predeterminados.

## Supervisión de recursos

Cuando IBM Edge Application Manager se instala, configura automáticamente una supervisión básica de
los recursos de producto que se ejecutan en kubernetes. Los datos de supervisión se pueden ver en el panel de
control de Grafana de la consola de gestión en la ubicación siguiente:

* `https://<MANAGEMENT_URL:PORT>/grafana/d/kube-system-ibm-edge-overview/ibm-edge-overview`

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
  name: ibm-edge-remote-dbs
  labels:
    release: ibm-edge
type: Opaque
stringData:
  # valores de conexión de postgresql de agbot
  agbot-db-host: "Nombre de host único de la base de datos remota"
  agbot-db-port: "Puerto único en el que se ejecuta la base de datos"
  agbot-db-name: "El nombre de la base de datos a utilizar en la instancia postgresql"
  agbot-db-user: "Nombre de usuario utilizado para conectarse"
  agbot-db-pass: "Contraseña utilizada para conectarse"
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

Para cambiar cualquiera de los parámetros de configuración de Helm predeterminados, revise los parámetros y
sus descripciones utilizando el mandato `grep` siguiente y, a continuación, visualice/edite los
valores correspondientes en `values.yaml`:

```bash
grep -v -E '(^ *#|__metadata)' ibm_cloud_pak/values-metadata.yaml
vi values.yaml   # o utilice cualquier editor
```

## Instalación de la gráfica

**Notas:**

* Se trata de una instalación solo de CLI, la instalación desde GUI no está soportada

* Asegúrese de que se han completado los pasos en
[Instalación
de la infraestructura de IBM Edge Application Manager - Proceso de instalación](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/hub/offline_installation.html#process).
* Sólo puede haber una instancia de IBM Edge Application Manager instalada por clúster y sólo se puede
instalar en el espacio de nombres `kube-system`.
* No se soporta la actualización de IBM Edge Application Manager 4.0

Ejecute el script de instalación proporcionado para instalar IBM Edge Application Manager. Los pasos principales que el script lleva a cabo son: instalar la gráfica de helm y configurar el entorno después de la instalación (crear agbot, org y servicios de patrón/política).

```bash
ibm_cloud_pak/pak_extensions/support/ieam-install.sh
```

**Nota:** en función de las velocidades de red, se tardará unos minutos en descargar las
imágenes y en desplegar todos los recursos de gráfica.

### Verificación de la gráfica

* El script anterior verifica que las pods se están ejecutando y que el agbot y Exchange están respondiendo. Busque un mensaje "RUNNING" y "PASSED" hacia el final de la instalación.
* Si es "FAILED", la salida le pedirá que busque más información en los registros específicos.
* Si es "PASSED", la salida mostrará detalles de las pruebas que se han ejecutado y el URL para la IU de gestión
  * Vaya a la consola de la interfaz de usuario de IBM Edge Application Manager en el URL proporcionado
al final del registro.
    * `https://<MANAGEMENT_URL:PORT>/edge`

## Acciones posteriores a la instalación

Siga los pasos que se indican en [Configuración posterior a la instalación](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/hub/post_install.html).

## Desinstalación de la gráfica

Siga los pasos para [Desinstalar el
centro de gestión](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/hub/uninstall.html).

## Acceso basado en roles

* La autoridad del administrador de clúster en el espacio de nombres de `kube-system` es necesaria para instalar gestionar este producto.
* Las cuentas de servicio, los roles y los enlaces de rol se crean para esta gráfica y las subgráficas
basándose en el nombre de release.
* Autenticación de Exchange y roles:
  * IAM proporciona la autenticación de todos los administradores y los usuarios de Exchange a través de las claves de API generadas con el mandato `cloudctl`
  * Los administradores de Exchange deben tener el privilegio `admin` dentro de Exchange. Con ese privilegio, pueden gestionar todos los usuarios, nodos, servicios, patrones y políticas dentro de su organización de Exchange
  * Los usuarios que no sean administradores de Exchange solo podrán gestionar usuarios, nodos, servicios, patrones y políticas que hayan creado.

## Seguridad

* TLS se utiliza para todos los datos que entran/salen del clúster de OpenShift a través de ingress. En este release, no se utiliza TLS **dentro** del clúster de OpenShift para la comunicación de nodo a nodo. Si
lo desea, configure la malla de servicio de Red Hat OpenShift para la comunicación entre microservicios. Consulte [Understanding Red Hat OpenShift Service Mesh](https://docs.openshift.com/container-platform/4.4/service_mesh/service_mesh_arch/understanding-ossm.html#understanding-ossm).
* Esta gráfica no proporciona ningún cifrado de los datos en reposo.  Corresponde al administrador
configurar el almacenamiento en el cifrado en reposo.

## Copia de seguridad y recuperación

Siga los pasos de
[Copia de seguridad y
recuperación](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/admin/backup_recovery.html).

## Limitaciones

* Límites de instalación: este producto sólo se puede instalar una vez, y sólo en el espacio de nombres de `kube-system`

## Documentación

* Consulte la documentación del Knowledge Center de
[Instalación](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/hub/hub.html)
para obtener información adicional.

## Copyright

© Copyright IBM Corporation 2020. Reservados todos los derechos.
