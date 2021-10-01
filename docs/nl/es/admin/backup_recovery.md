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

# Copia de seguridad y recuperación de datos
{: #data_backup}

## Copia de seguridad y recuperación de {{site.data.keyword.open_shift_cp}}

Para obtener más información sobre la copia de seguridad y recuperación de datos en todo el clúster, consulte:

* [Copia de seguridad de {{site.data.keyword.open_shift_cp}} 4.6 etcd](https://docs.openshift.com/container-platform/4.6/backup_and_restore/backing-up-etcd.html).

## Copia de seguridad y recuperación de {{site.data.keyword.edge_notm}}

Los procedimientos de copia de seguridad de {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) difieren ligeramente en función del tipo de bases de datos que utilice. Estas bases de datos se conocen como locales o remotas.

|Tipo de base de datos|Descripción|
|-------------|-----------|
|Local|Estas bases de datos se instalan (de forma predeterminada) como recursos de {{site.data.keyword.open_shift}} en el clúster {{site.data.keyword.open_shift}}|
|Remota|Estas bases de datos se suministran de forma externa al clúster. Por ejemplo, estas bases de datos pueden ser locales o una oferta SaaS de proveedor de nube.|

El valor de configuración que controla qué bases de datos se utilizan se establece durante la instalación en el recurso personalizado como **spec.ieam\_local\_databases** y es true de forma predeterminada.

Para determinar el valor activo para una instancia de {{site.data.keyword.ieam}} instalada, ejecute:

```
oc get eamhub ibm-edge -o jsonpath="{.spec.ieam_local_databases}"
```
{: codeblock}

Para obtener más detalles sobre la configuración de bases de datos remotas durante la instalación, consulte la página [Configuración](../hub/configuration.md).

**Nota**: No se da soporte a la conmutación entre bases de datos locales y remotas.

El producto {{site.data.keyword.edge_notm}} no realiza una copia de seguridad automática de los datos. Es responsable de realizar una copia de seguridad del contenido en la cadencia elegida y de almacenar esas copias de seguridad en una ubicación segura independiente para garantizar la recuperabilidad. Puesto que las copias de seguridad secretas tienen contenido de autenticación codificado para las conexiones de base de datos y la autenticación de aplicación de {{site.data.keyword.mgmt_hub}}, almacénelas en una ubicación segura.

Si utiliza sus propias bases de datos remotas, asegúrese de que se realice una copia de seguridad de dichas bases de datos. Esta documentación no describe cómo realizar la copia de seguridad de los datos de esas bases de datos remotas.

El procedimiento de copia de seguridad de {{site.data.keyword.ieam}}también requiere `yq` v3.

### Procedimiento de copia de seguridad

1. Asegúrese de que está conectado al clúster con **cloudctl login** u **oc login** como administrador de clúster. Realice una copia de seguridad de los datos y los secretos con el siguiente script, que se encuentra en el soporte no empaquetado que se ha utilizado para la instalación de {{site.data.keyword.mgmt_hub}} desde Passport Advantage. Ejecute el script con **-h** para su uso:

   ```
   ibm-eam-{{site.data.keyword.semver}}-bundle/tools/ieam-backup.sh -h
   ```
   {: codeblock}
   
   **Nota**: El script de copia de seguridad detecta automáticamente el tipo de bases de datos que se utilizan durante la instalación.

   * Si ejecuta el siguiente ejemplo sin opciones, genera una carpeta allí donde se ha ejecutado el script. La carpeta sigue este esquema de denominación, **ibm-edge-backup/$DATE/**:

     ```
     ibm-eam-{{site.data.keyword.semver}}-bundle/tools/ieam-backup.sh
     ```
     {: codeblock}
     
     Si se ha detectado una instalación de **base de datos local**, la copia de seguridad contiene un directorio **customresource**, un directorio **databaseresources** y dos archivos yaml:

     ```
     $ ls -l ibm-edge-backup/20201026_215107/   	  drwxr-xr-x  3 staff  staff     96 Oct 26 21:51 customresource 	  drwxr-xr-x  5 staff  staff    160 Oct 26 21:51 databaseresources 	  -rw-r--r--  1 staff  staff  13308 Oct 26 21:51 ibm-edge-auth-secret.yaml 	  -rw-r--r--  1 staff  staff   3689 Oct 26 21:51 ibm-edge-config.yaml
     ```
     {: codeblock}
     
	  Si se ha detectado una instalación de **base de datos remota**, se muestran los mismos directorios indicados anteriormente, pero tres archivos yaml en lugar de dos.
	  
	  ```
     $ ls -l ibm-edge-backup/20201026_215518/ 	  drwxr-xr-x  3 staff  staff     96 Oct 26 21:55 customresource 	  drwxr-xr-x  3 staff  staff     96 Oct 26 21:55 databaseresources 	  -rw-r--r--  1 staff  staff  10477 Oct 26 21:55 ibm-edge-auth-overrides.yaml 	  -rw-r--r--  1 staff  staff  11433 Oct 26 21:55 ibm-edge-auth-secret.yaml 	  -rw-r--r--  1 staff  staff   2499 Oct 26 21:55 ibm-edge-config.yaml
     ```
     {: codeblock}

### Procedimiento de restauración

**Nota**: Cuando se utilizan bases de datos locales o se restauran en bases de datos remotas nuevas o vacías, el diseño autónomo de {{site.data.keyword.ieam}} genera un desafío conocido al restaurar copias de seguridad en {{site.data.keyword.mgmt_hub}}.

Para restaurar copias de seguridad, se debe instalar un {{site.data.keyword.mgmt_hub}} idéntico. Si se instala este nuevo hub sin entrar **ieam\_maintenance\_mode** durante la instalación inicial, es probable que se anule el registro de todos los nodos periféricos, que se habían registrado previamente. Esto hace que sea necesario que se vuelvan a registrar.

Esta situación se produce cuando el nodo periférico reconoce que ya no existe en Exchange porque ahora la base de datos está vacía. Habilite **ieam\_maintenance\_mode** para evitarlo iniciando los recursos de base de datos sólo para el {{site.data.keyword.mgmt_hub}}. Esto permite que se complete la restauración antes de que se inicien los recursos de {{site.data.keyword.mgmt_hub}} restantes (que utilizan dichas bases de datos).

**Notas**: 

* Cuando se ha realizado una copia de seguridad del archivo de **Recurso personalizado**, se ha modificado automáticamente para especificar **ieam\_maintenance\_mode** inmediatamente después de volverlo a aplicar en el clúster.

* Los scripts de restauración determinan automáticamente qué tipo de base de datos se ha utilizado previamente examinando el archivo **\<path/to/backup\>/customresource/eamhub-cr.yaml**.

1. Como administrador de clúster, asegúrese de que está conectado al clúster con **cloudctl login** o **oc login** y que se ha creado una copia de seguridad válida. En el clúster donde se ha realizado la copia de seguridad, ejecute el mandato siguiente para suprimir el recurso personalizado **eamhub** (lo que presupone que el nombre predeterminado de **ibm-edge** se ha utilizado para el recurso personalizado):
	```
	oc delete eamhub ibm-edge
	```
	{: codeblock}

2. Verifique que **ieam\_maintenance\_mode** se ha establecido correctamente:
	```
	yq r ibm-edge-backup/20201026_215738/customresource/eamhub-cr.yaml 'items[0].spec.ieam_maintenance_mode'
	```
	{: codeblock}
	

3. Ejecute el script `ieam-restore-k8s-resources.sh` con la opción **-f** definida para apuntar a la copia de seguridad:
	```
	ibm-eam-{{site.data.keyword.semver}}-bundle/tools/ieam-restore-k8s-resources.sh -f ibm-edge-backup/20201026_215738/
	```
	{: codeblock}

   Espere a que se ejecuten todos los pods de base de datos y SDO antes de continuar.
	
4. Edite el recurso personalizado **ibm-edge** para detener el operador:
	```
	oc patch eamhub ibm-edge --type merge --patch '{"spec":{"pause_control_loop": true}}'
	```
	{: codeblock}

5. Edite el conjunto con estado **ibm-edge-sdo** para aumentar el número de réplicas en **1**:
	```
	oc patch statefulset ibm-edge-sdo --type merge --patch '{"spec":{"replicas": 1}}'
	```
	{: codeblock}

6. Espere a que el pod **ibm-edge-sdo-0** esté en estado en ejecución:
	```
   	watch oc get pods -n ibm-edge | grep ibm-edge-sdo-0
   	```
	{: codeblock}

7. Ejecute el script `ieam-restore-data.sh` con la opción **-f** definida para que apunte a la copia de seguridad:
	```
	ibm-eam-{{site.data.keyword.semver}}-bundle/tools/ieam-restore-data.sh -f ibm-edge-backup/20201026_215738/
	```
	{: codeblock}
	
8. Cuando el script se haya completado y los datos se hayan restaurado, elimine la pausa en el operador para reanudar el bucle de control:
	```
	oc patch eamhub ibm-edge --type merge --patch '{"spec":{"pause_control_loop": false}}'
	```
	{: codeblock}

