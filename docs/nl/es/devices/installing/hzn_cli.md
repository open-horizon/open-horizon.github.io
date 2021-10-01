---

copyright:
  years: 2020
lastupdated: "2020-5-11"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Instalación de la CLI de hzn
{: #using_hzn_cli}

Cuando se instala el software de agente de {{site.data.keyword.ieam}} en un nodo periférico,
la CLI **hzn** se instala automáticamente. Pero también puede instalar la CLI
**hzn** sin el agente. Por
ejemplo, un administrador periférico puede desear consultar
{{site.data.keyword.ieam}} Exchange o puede que un desarrollador de periferia desee
probar con mandatos **hzn dev**.

1. Solicite el archivo **agentInstallFiles-&lt;tipo-dispositivo-periférico&gt;.tar.gz** al
administrador de centro de gestión, donde **&lt;tipo-dispositivo-periférico&gt;** coincide
con el host en el que instalará **hzn**. Ya debe haberlo creado en
[Recopilar la información y los archivos necesarios para dispositivos periféricos](../../hub/gather_files.md#prereq_horizon). Copie
este archivo en el host en el que desea instalar **hzn**.

2. Establezca el nombre de archivo en una variable de entorno para los pasos siguientes:

   ```bash
   export AGENT_TAR_FILE=agentInstallFiles-<tipo-de-dispositivo-periférico>.tar.gz
   ```
   {: codeblock}

3. Extraiga el paquete de CLI de Horizon del archivo tar:

   ```bash
   tar -zxvf $AGENT_TAR_FILE 'horizon-cli*'
   ```
   {: codeblock}

   * Confirme que la versión de paquete es la misma que la del agente de dispositivo listado en
[Componentes](../getting_started/components.md).

4. Instale el paquete **horizon-cli**:

   * En un distro basado en debian: 

     ```bash
     sudo apt update && sudo apt install horizon-cli*.deb
     ```
     {: codeblock}

   * En {{site.data.keyword.macOS_notm}}:

     ```bash
     sudo installer -pkg horizon-cli-*.pkg -target /
     ```
     {: codeblock}

     Nota: En {{site.data.keyword.macOS_notm}}, también puede instalar el archivo pkg de
horizon-cli desde Finder: efectúe una doble pulsación en el archivo para abrir el instalador. Si obtiene
un mensaje de error que indica que el programa "no se puede abrir porque es de un desarrollador no identificado",
pulse el botón derecho del ratón en el archivo y seleccione **Abrir**. Pulse
**Abrir** de nuevo cuando se le solicite "¿Está seguro de que desea abrirlo?". A continuación,
siga las solicitudes para instalar el paquete de Horizon de CLI, asegurándose de que el ID tiene
privilegios de administrador.

## Desinstalación de la CLI hzn

Si desea eliminar el paquete **horizon-cli** de un host:

* Desinstale **horizon-cli** de un distro basado en Debian:

  ```bash
  sudo apt-get remove horizon-cli
  ```
  {: codeblock}

* O desinstale **horizon-cli** de {{site.data.keyword.macOS_notm}}:

  * Abra la carpeta de cliente hzn (/usr/local/bin) y arrastre la aplicación
`hzn` a la papelera (al final de Dock).
