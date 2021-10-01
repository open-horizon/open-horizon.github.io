---

copyright:
years: 2021
lastupdated: "2021-03-23"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Actualizaciones
{: #hub_upgrade_overview}

## Resumen de las actualizaciones
{: #sum}
* La versión actual del Centro de gestión de {{site.data.keyword.ieam}} es {{site.data.keyword.semver}}.
* {{site.data.keyword.ieam}} {{site.data.keyword.semver}} está soportado en {{site.data.keyword.ocp}} versión 4.6.

Las actualizaciones del mismo canal de Operator Lifecycle Manager (OLM) para el Centro de gestión de {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) e [IBM Cloud Platform Common Services](https://www.ibm.com/docs/en/cpfs) se producen automáticamente a través de OLM que viene preinstalado en el clúster de {{site.data.keyword.open_shift_cp}} ({{site.data.keyword.ocp}}).

Los canales de {{site.data.keyword.ieam}} se definen mediante la **versión menor** (por ejemplo v4.2 y v4.3) y automáticamente actualizarán las **versiones de parche** (por ejemplo, 4.2.x). Para las actualizaciones de **versión menor**, debe cambiar manualmente los canales para iniciar la actualización. Para poder iniciar una actualización de **versión menor**, debe estar en la última **versión de parche** disponible de la **versión menor** anterior, a continuación, los canales de conmutación iniciarán la actualización.

**Notas:**
* La degradación no está soportada
* La actualización de {{site.data.keyword.ieam}} 4.1.x a 4.2.x no está soportada
* Debido a un [problema conocido de {{site.data.keyword.ocp}}](https://access.redhat.com/solutions/5493011), si tiene algún `InstallPlans` en el proyecto configurado para la aprobación manual, todos los demás `InstallPlans` de ese proyecto también lo hacen. Debe aprobar manualmente la actualización del operador para poder continuar.

### Actualización del centro de gestión de {{site.data.keyword.ieam}} de 4.2.x a 4.3.x

1. Realice una copia de seguridad antes de la actualización. Para obtener más información, consulte [Copia de seguridad y recuperación](../admin/backup_recovery.md).
2. Vaya a la consola web de {{site.data.keyword.ocp}} para el clúster.
3. Vaya a **Operadores** &gt; **Operadores instalados**.
4. Busque **{{site.data.keyword.ieam}}** y pulse el resultado de **centro de gestión de {{site.data.keyword.ieam}}** .
5. Vaya al separador **Suscripción**.
6. Pulse el enlace **v4.2** en la sección **Canal**.
7. Pulse el botón de selección para cambiar el canal activo a **v4.3** para iniciar la actualización.

Para verificar que la actualización se ha completado, consulte los [pasos 1 a 5 en la sección posterior a la instalación de la verificación de la instalación](post_install.md).

Para actualizar los servicios de ejemplo, consulte [pasos 1 a 3 en la sección Configuración posterior a la instalación](post_install.md).

## Actualización de nodos periféricos

Los nodos {{site.data.keyword.ieam}} existentes no se actualizan automáticamente. La versión del agente de {{site.data.keyword.ieam}} 4.2.0 (2.27.0-173) está soportada con un centro de gestión de {{site.data.keyword.ieam}} {{site.data.keyword.semver}}. Para actualizar el agente de {{site.data.keyword.edge_notm}} en los dispositivos periféricos y los clústeres periféricos, primero debe colocar los archivos de nodos periféricos de {{site.data.keyword.semver}} en el servicio de sincronización de nube (Cloud Sync Service, CSS).

Realice los pasos 1 a 3 bajo **Instalación de la última CLI en el entorno** incluso si no desea actualizar los nodos periféricos en este momento. Esto garantiza que los nuevos nodos periféricos se instalarán con el último código de agente de {{site.data.keyword.ieam}} {{site.data.keyword.semver}}.

### Instalación de la CLI más reciente en el entorno
1. Inicie sesión, saque y extraiga el paquete de agentes con la clave de titularidad a través del [Registro autorizado](https://myibm.ibm.com/products-services/containerlibrary):
    ```
    docker login cp.icr.io --username cp &amp;TWBAMP;&amp;TWBAMP; \     docker rm -f ibm-eam-{{site.data.keyword.semver}}-bundle; \     docker create --name ibm-eam-{{site.data.keyword.semver}}-bundle cp.icr.io/cp/ieam/ibm-eam-bundle:{{site.data.keyword.anax_ver}} bash &amp;TWBAMP;&amp;TWBAMP; \     docker cp ibm-eam-{{site.data.keyword.semver}}-bundle:/ibm-eam-{{site.data.keyword.semver}}-bundle.tar.gz ibm-eam-{{site.data.keyword.semver}}-bundle.tar.gz &amp;TWBAMP;&amp;TWBAMP; \     tar -zxvf ibm-eam-{{site.data.keyword.semver}}-bundle.tar.gz
    ```
    {: codeblock}
2. Instale la CLI **hzn** utilizando las instrucciones para la plataforma soportada:
  * Vaya al directorio **agent** y desempaquete los archivos de agente:
    ```
    cd ibm-eam-{{site.data.keyword.semver}}-bundle/agent &amp;TWBAMP;&amp;TWBAMP; \ tar -zxvf edge-packages-{{site.data.keyword.semver}}.tar.gz
    ```
    {: codeblock}

    * Ejemplo de Debian {{site.data.keyword.linux_notm}}:
      ```
      sudo apt-get install ./edge-packages-{{site.data.keyword.semver}}/linux/deb/amd64/horizon-cli*.deb
      ```
      {: codeblock}

    * Ejemplo de Red Hat {{site.data.keyword.linux_notm}}:
      ```
      sudo dnf install -yq ./edge-packages-{{site.data.keyword.semver}}/linux/rpm/x86_64/horizon-cli-*.x86_64.rpm
      ```
      {: codeblock}

    * Ejemplo de macOS:
      ```
      sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain edge-packages-{{site.data.keyword.semver}}/macos/pkg/x86_64/horizon-cli.crt && \       sudo installer -pkg edge-packages-{{site.data.keyword.semver}}/macos/pkg/x86_64/horizon-cli-*.pkg -target /
      ```
      {: codeblock}
3. Siga los pasos recogidos en [Recopilar archivos de nodo periférico](../hub/gather_files.md) para enviar los archivos de instalación del agente a CSS.

### Actualización del agente en nodos periféricos
1. Inicie la sesión en el nodo periférico como usuario **root** en un dispositivo o como usuario **admin** en el clúster y, a continuación, establezca las variables de entorno de Horizon:
```bash
export HZN_EXCHANGE_USER_AUTH=iamapikey:<clave-api>   export HZN_ORG_ID=<su-organización-exchange>   export HZN_FSS_CSSURL=https://<ingreso-centro-gestión-ieam>/edge-css/
```
{: codeblock}

2. Establezca las variables de entorno necesarias en función del tipo de clúster (omita este paso si está actualizando un dispositivo):

  * **En los clústeres periféricos OCP:**
  
    Establezca la clase de almacenamiento que el agente debe utilizar:
    
    ```bash
    oc get storageclass    export EDGE_CLUSTER_STORAGE_CLASS=<rook-ceph-cephfs-internal>
    ```
    {: codeblock}

    Establezca el nombre de usuario de registro en el nombre de cuenta de servicio que ha creado:
    ```bash  oc get serviceaccount -n openhorizon-agent export EDGE_CLUSTER_REGISTRY_USERNAME=<service-account-name>
    ```
    {: codeblock}

    Establezca la señal de registro: 
    ```bash export EDGE_CLUSTER_REGISTRY_TOKEN=`oc serviceaccounts get-token $EDGE_CLUSTER_REGISTRY_USERNAME`
    ```
    {: codeblock}

  * **En k3s:**
  
    Indique a **agent-install.sh** que utilice la clase de almacenamiento predeterminada:
    
    ```bash
    export EDGE_CLUSTER_STORAGE_CLASS=local-path
    ```
    {: codeblock}

  * **En microk8s:**
  
    Indique a **agent-install.sh** que utilice la clase de almacenamiento predeterminada:
    
    ```bash
    export EDGE_CLUSTER_STORAGE_CLASS=microk8s-hostpath
    ```
    {: codeblock}

3. Extraiga **agent-install-sh** desde CSS:
```bash
curl -u $HZN_ORG_ID/$HZN_EXCHANGE_USER_AUTH $HZN_FSS_CSSURL/api/v1/objects/IBM/agent_files/agent-install.sh/data -o agent-install.sh --insecure && chmod +x agent-install.sh
```
{: codeblock}

4. Ejecute **agent-install.sh** para obtener los archivos actualizados de CSS y configure el agente de Horizon:
  *  **En dispositivos periféricos:**
    ```bash  sudo -s -E ./agent-install.sh -i 'css:' -s
    ```
    {: codeblock}

  *  **En clústeres periféricos:**
    ```bash ./agent-install.sh -D cluster -i 'css:' -s
    ```
    {: codeblock}

**Nota**: Si incluye la opción -s mientras ejecuta la instalación del agente para omitir el registro, el nodo periférico se quedará en el mismo estado en el que estaba antes de la actualización.

## Problemas conocidos y preguntas frecuentes
{: #FAQ}

### {{site.data.keyword.ieam}} 4.2
* Existe un problema conocido con la base de datos mongo cssdb local de {{site.data.keyword.ieam}} 4.2.0, que produce la pérdida de datos cuando se vuelve a planificar el pod. Si utiliza bases de datos locales (valor predeterminado), se recomienda permitir que la actualización de {{site.data.keyword.ieam}} {{site.data.keyword.semver}} se complete antes de actualizar el clúster {{site.data.keyword.ocp}} a la versión 4.6. Para obtener más detalles, consulte la página de [problemas conocidos](../getting_started/known_issues.md).

* No he actualizado mi anterior versión de clúster {{site.data.keyword.ocp}} 4.4 y la actualización automática parece estar detenida.

  * Para resolver este problema, siga estos pasos:
  
    1) Realice una copia de seguridad del contenido del Centro de gestión de {{site.data.keyword.ieam}} actual.  Aquí encontrará la documentación sobre la copia de seguridad: [Copia de seguridad y recuperación de datos](../admin/backup_recovery.md).
    
    2) Actualice el clúster {{site.data.keyword.ocp}} a la versión 4.6.
    
    3) Debido a un problema conocido con la base de datos mongo {{site.data.keyword.ieam}} 4.2.0 local **cssdb**, la actualización del **paso 2** reinicializará la base de datos.
    
      * Si ha aprovechado las prestaciones MMS de {{site.data.keyword.ieam}} y está preocupado por la pérdida de datos, utilice la copia de seguridad realizada en el **paso 1** y siga el **Procedimiento de restauración** en la página [Copia de seguridad y restauración de datos](../admin/backup_recovery.md). (**Nota:** El procedimiento de restauración producirá un tiempo de inactividad.)
      
      * Como alternativa, realice lo siguiente para desinstalar y volver a instalar el operador {{site.data.keyword.ieam}}, si no ha aprovechado las prestaciones de MMS, no está preocupado por la pérdida de datos de MMS o está utilizando bases de datos remotas:
      
        1) Vaya a la página Operadores instalados del clúster {{site.data.keyword.ocp}}
        
        2) Localice el operador del Centro de gestión de IEAM y abra la página.
        
        3) En el menú de acciones situado a la izquierda, elija desinstalar el operador.
        
        4) Vaya a la página OperatorHub y vuelva a instalar el operador del Centro de gestión de IEAM.

* ¿{{site.data.keyword.ocp}} versión 4.5 está soportado?

  * El Centro de gestión de {{site.data.keyword.ieam}} no se ha probado y no está soportado en {{site.data.keyword.ocp}} versión 4.5.  Le sugerimos actualizar a {{site.data.keyword.ocp}} versión 4.6.

* ¿Hay alguna forma de renunciar a esta versión del Centro de gestión de {{site.data.keyword.ieam}}?

  * El Centro de gestión de {{site.data.keyword.ieam}} versión 4.2.0 ya no estará soportado tras el release de la versión {{site.data.keyword.semver}}.
