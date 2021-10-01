---

copyright:
years: 2020
lastupdated: "2020-5-10"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Instalación y registro masivos de agente
{: #batch-install}

Utilice el proceso de instalación masiva para configurar varios dispositivos periféricos de tipo similar (en otras palabras, arquitectura, sistema operativo y patrón o política iguales).

**Nota**: En este proceso, no están soportados los dispositivos periféricos de destino que son sistemas macOs. Sin embargo, si lo desea puede controlar este proceso desde un sistema macOs. (En otras palabras, este host puede ser un sistema macOs.)

### Requisitos previos

* Los dispositivos que se van a instalar y registrar deben tener acceso de red a este centro de gestión.
* Los dispositivos deben tener un sistema operativo instalado.
* Si está utilizando DHCP para dispositivos periféricos, cada dispositivo debe mantener la misma dirección IP hasta que se complete la tarea (o el mismo `nombre de host` si utiliza DDNS).
* Todas las entradas de usuario de servicio periférico deben especificarse como valores predeterminados en la definición de servicio o en la política de despliegue o patrón. No se pueden utilizar entradas de usuario específicas de nodo.

### Procedimiento
{: #proc-multiple}

1. Si todavía no ha obtenido o creado el archivo **agentInstallFiles-&lt;tipo-de-dispositivo-periférico&gt;.tar.gz** y la clave de API siguiendo lo indicado en [Recopilar la información y los archivos necesarios para dispositivos periféricos](../hub/gather_files.md#prereq_horizon), hágalo ahora. Establezca el nombre del archivo y el valor de clave de API en estas variables de entorno:

   ```bash
   export AGENT_TAR_FILE=agentInstallFiles-<tipo-de-dispositivo-periférico>.tar.gz    export HZN_EXCHANGE_USER_AUTH=iamapikey:<clave-de-API>
   ```
  {: codeblock}

2. El paquete **pssh** incluye los mandatos **pssh** y **pscp** que le permiten ejecutar mandatos en muchos dispositivos periféricos en paralelo y copiar archivos en muchos dispositivos periféricos en paralelo. Si no tiene estos mandatos en este host, instale el paquete ahora:

  * En {{site.data.keyword.linux_notm}}:

   ```bash
   sudo apt install pssh    alias pssh=parallel-ssh    alias pscp=parallel-scp
   ```
   {: codeblock}

  * En {{site.data.keyword.macOS_notm}}:

   ```bash
   brew install pssh
   ```
   {: codeblock}

   (Si **brew** aún no se ha instalado, consulte [Instalar pssh en el sistema macOs con Brew](https://brewinstall.org/Install-pssh-on-Mac-with-Brew/).)

3. Puede asignar acceso **pscp** y **pssh** a los dispositivos periféricos de varias formas. En este contenido se describe cómo utilizar una clave pública ssh. En primer lugar, este host debe tener un par de claves ssh (normalmente en **~/.ssh/id_rsa** y **~/.ssh/id_rsa.pub**). Si no tiene un par de claves ssh, genérelo:

   ```bash
   ssh-keygen -t rsa
   ```
   {: codeblock}

4. Coloque el contenido de la clave pública (**~/.ssh/id_rsa.pub**) en cada dispositivo periférico en **/root/.ssh/authorized_keys** .

5. Cree un archivo de correlación de 2 columnas llamado **node-id-mapping.csv** que correlacione cada dirección IP o nombre de host de dispositivo con el nombre de nodo de {{site.data.keyword.ieam}} que debe adoptar durante el registro. Cuando **agent-install.sh** se ejecuta en cada dispositivo periférico, este archivo le indica qué nombre de nodo periférico se le debe dar a ese dispositivo. Utilice el formato CSV:

   ```bash
   Nombre de host/IP, Nombre de nodo    1.1.1.1, factory2-1    1.1.1.2, factory2-2
   ```
   {: codeblock}

6. Añada **node-id-mapping.csv** al archivo tar de agente:

   ```bash
   gunzip $AGENT_TAR_FILE    tar -uf ${AGENT_TAR_FILE%.gz} node-id-mapping.csv    gzip ${AGENT_TAR_FILE%.gz}
   ```
   {: codeblock}

7. Coloque la lista de dispositivos periféricos que desea instalar y registrar de forma masiva en un archivo llamado **nodes.hosts**. Esto se utilizará con los mandatos **pscp** y **pssh**. Cada línea debe estar en el formato de ssh estándar `<user>@<IP-or-hostname>` :

   ```bash
   root@1.1.1.1    root@1.1.1.2
   ```
   {: codeblock}

   **Nota**: Si utiliza un usuario no root para cualquiera de los hosts, se debe configurar sudo para permitir utilizar sudo desde ese usuario sin entrar una contraseña.

8. Copie el archivo tar de agente en los dispositivos periféricos. Este paso puede tardar un poco:

   ```bash
   pscp -h nodes.hosts -e /tmp/pscp-errors $AGENT_TAR_FILE /tmp
   ```
   {: codeblock}

   **Nota**: Si obtiene **[FAILURE]** en la salida **pscp** para cualquiera de los dispositivos periféricos, puede ver los errores en **/tmp/pscp-errors**.

9. Ejecute **agent-install.sh** en cada dispositivo periférico para instalar el agente de Horizon y registrar los dispositivos periféricos. Puede utilizar un patrón o una política para registrar los dispositivos periférico:

   1. Registre los dispositivos periféricos con un patrón:

      ```bash
      pssh -h nodes.hosts -t 0 "bash -c \"tar -zxf /tmp/$AGENT_TAR_FILE agent-install.sh && sudo -s ./agent-install.sh -i . -u $HZN_EXCHANGE_USER_AUTH -p IBM/pattern-ibm.helloworld -w ibm.helloworld -o IBM -z /tmp/$AGENT_TAR_FILE 2>&1 >/tmp/agent-install.log \" "
      ```
      {: codeblock}

      En lugar de registrar los dispositivos periféricos con el patrón de despliegue **IBM/pattern-ibm.helloworld**, puede utilizar un patrón de despliegue diferente modificando los distintivos **-p**, **-w** y **-o**. Para ver todas las descripciones de distintivo de **agent-install.sh** disponibles:

      ```bash
      tar -zxf $AGENT_TAR_FILE agent-install.sh &&./agent-install.sh -h
      ```
      {: codeblock}

   2. O registre los dispositivos periféricos con la política. Cree una política de nodo, cópielo en los dispositivos periféricos y registre los dispositivos con esa política:

      ```bash
      echo '{ "properties": [ { "name": "nodetype", "value": "special-node" } ] }' > node-policy.json       pscp -h nodes.hosts -e /tmp/pscp-errors node-policy.json /tmp       pssh -h nodes.hosts -t 0 "bash -c \"tar -zxf /tmp/$AGENT_TAR_FILE agent-install.sh && sudo -s ./agent-install.sh -i . -u $HZN_EXCHANGE_USER_AUTH -n /tmp/node-policy.json  -z /tmp/$AGENT_TAR_FILE 2>&1 >/tmp/agent-install.log \" "
      ```
      {: codeblock}

      Ahora los dispositivos periféricos están listos, pero no empezarán a ejecutar servicios periféricos hasta que cree una política de despliegue (política de negocio) que especifique que un servicio debe desplegarse en este tipo de dispositivo periférico (en este ejemplo, dispositivos con **nodetype** de **especial-node**). Consulte [Utilización de política de despliegue](../using_edge_services/detailed_policy.md) para conocer los detalles.

10. Si obtiene **[FAILURE]** en la salida de **pssh** para cualquiera de los dispositivos periféricos, puede investigar el problema accediendo al dispositivo periférico y viendo **/tmp/agent-install.log** .

11. Mientras se está ejecutando el mandato **pssh**, puede ver el estado de los nodos periféricos en la consola de {{site.data.keyword.edge_notm}}. Consulte
[Utilización de la consola de gestión](../console/accessing_ui.md).
