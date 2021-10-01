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

Nota: Estos pasos son los mismos para todos los tipos de dispositivo (arquitecturas).

1. Obtenga el archivo **agentInstallFiles-&lt;tipo-de-dispositivo-periférico&gt;.tar.gz** y una clave de API del administrador. Ya se deberían haber creado en la sección [Recopilar la información y los archivos necesarios para dispositivos periféricos](../../hub/gather_files.md#prereq_horizon). Copie este archivo en el dispositivo periférico mediante el mandato de copia segura, un lápiz USB u otro método. Además, anote el valor de la clave de API. Lo
necesita en un paso posterior. A continuación, establezca el nombre de archivo en una variable de entorno
para los pasos siguientes:

   ```bash
   export AGENT_TAR_FILE=agentInstallFiles-<tipo-de-dispositivo-periférico>.tar.gz
   ```
   {: codeblock}

2. Extraiga el mandato **agent-install.sh** en el archivo tar:

   ```bash
   tar -zxvf $AGENT_TAR_FILE agent-install.sh
   ```
   {: codeblock}

3. Exporte las credenciales de usuario de {{site.data.keyword.horizon}} Exchange (la clave de API):

  ```bash
  export HZN_EXCHANGE_USER_AUTH=iamapikey:<clave-de-API>
  ```
  {: codeblock}

4. Ejecute el mandato **agent-install.sh** para instalar y configurar el agente de {{site.data.keyword.horizon}}, y para registrar el dispositivo periférico para ejecutar el servicio periférico de ejemplo helloworld:

  ```bash
  sudo -s ./agent-install.sh -i . -u $HZN_EXCHANGE_USER_AUTH -p IBM/pattern-ibm.helloworld -w ibm.helloworld -o IBM -z $AGENT_TAR_FILE
  ```
  {: codeblock}

  Nota: durante la instalación de los paquetes de agente, puede que reciba esta pregunta: "Desea
sobrescribir la configuración de nodo actual?`[y/N]`:" Puede responder "y" y pulsar Intro
porque **agent-install.sh** establecerá la configuración correctamente.

  Para ver todas las descripciones de distintivo de **agent-install.sh** disponibles:

  ```bash
  ./agent-install.sh -h
  ```
  {: codeblock}

5. Ahora que el dispositivo periférico está instalado y registrado, establezca la información específica como variables de entorno en el shell. Esto
le permite ejecutar el mandato **hzn** para ver la salida de helloworld:

  ```bash
  eval export $(cat agent-install.cfg)
  hzn service log -f ibm.helloworld
  ```
  {: codeblock}
  
  Nota: pulse **Ctrl** **C** para detener la visualización de salida.

6. Explore los distintivos y submandatos del mandato **hzn**:

  ```bash
  hzn --help
  ```
  {: codeblock}

7. También puede ver los nodos periféricos (dispositivos), los servicios, los patrones y las políticas
utilizando la consola de {{site.data.keyword.ieam}}. Consulte
[Utilización de la consola de gestión](../getting_started/accessing_ui.md).

8. Vaya a [Uso de CPU en IBM Event Streams](cpu_load_example.md) para continuar con
otros ejemplos de servicio periférico.
