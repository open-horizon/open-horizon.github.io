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

# Instalación y registro automatizados de agente
{: #method_one}

Nota: estos pasos son los mismos para todos los tipos de dispositivo periférico (arquitecturas).

1. Si todavía no tiene una clave de API, cree una siguiendo los pasos recogidos en [Creación de la clave de API](../hub/prepare_for_edge_nodes.md). Este proceso crea una clave de API, localiza algunos archivos y recopila los valores de variables de entorno que se necesitan para configurar los nodos periféricos.

2. Inicie la sesión en el dispositivo periférico y establezca las mismas variables de entorno que ha obtenido en el paso 1:

   ```bash
   export HZN_EXCHANGE_USER_AUTH=iamapikey:<clave-api>
  export HZN_ORG_ID=<su-organización-exchange>
  export HZN_FSS_CSSURL=https://<ingreso-centro-gestión-ieam>/edge-css/
   ```
   {: codeblock}

3. Si no utiliza un paquete de instalación preparado del administrador, descargue el script **agent-install.sh** desde Cloud Sync Service (CSS) en su dispositivo y conviértalo en ejecutable:

   ```bash
   curl -u "$HZN_ORG_ID/$HZN_EXCHANGE_USER_AUTH" -k -o agent-install.sh $HZN_FSS_CSSURL/api/v1/objects/IBM/agent_files/agent-install.sh/data   chmod +x agent-install.sh
   ```
   {: codeblock}

4. Ejecute **agent-install.sh** para obtener los archivos necesarios de CSS, instale y configure el agente de {{site.data.keyword.horizon}} y registre el dispositivo periférico para ejecutar el servicio periférico de ejemplo helloworld:

   ```bash
   sudo -s -E ./agent-install.sh -i 'css:' -p IBM/pattern-ibm.helloworld -w '*' -T 120
   ```
   {: codeblock}

   Para ver todas las descripciones de distintivo de **agent-install.sh** disponibles, ejecute: **./agent-install.sh -h**

   Nota: En {{site.data.keyword.macOS_notm}}, el agente se ejecutará en un contenedor Docker que se ejecuta como root.

5. Vea la salida de helloworld:

   ```bash
   hzn service log -f ibm.helloworld   # Pulse Ctrl-c para detener la visualización de la salida
   ```
   {: codeblock}

6. Si el servicio periférico helloworld no se inicia, ejecute este mandato para ver los mensajes de error:

   ```bash
   hzn eventlog list -f   # Pulse Ctrl-c para detener la visualización de la salida
   ```
   {: codeblock}

7. (opcional) Utilice el mandato **hzn** en este nodo periférico para ver los servicios, los patrones y las políticas de despliegue en {{site.data.keyword.horizon}} Exchange. Establezca la información específica como variables de entorno en el shell y ejecute estos mandatos:

   ```bash
   eval export $(cat agent-install.cfg)   hzn exchange service list IBM/   hzn exchange pattern list IBM/   hzn exchange deployment listpolicy
   ```
   {: codeblock}

8. Explore todos los submandatos y distintivos de mandato **hzn**:

   ```bash
   hzn --help
   ```
   {: codeblock}

## Qué hacer a continuación

* Utilice la consola de {{site.data.keyword.ieam}} para ver los nodos periféricos (dispositivos), servicios, patrones y políticas. Para obtener más información, consulte [Utilización de la consola de gestión](../console/accessing_ui.md).
* Explore y ejecute otro ejemplo de servicio periférico. Para obtener más información, consulte [Uso de CPU en IBM Event Streams](../using_edge_services/cpu_load_example.md).
