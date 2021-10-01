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

El mandato `hzn` es la interfaz de línea de mandatos de {{site.data.keyword.ieam}}. Cuando se instala el software de agente de {{site.data.keyword.ieam}}en un nodo periférico, la CLI `hzn` se instala automáticamente. Pero también puede instalar la CLI `hzn` sin el agente. Por ejemplo, puede que un administrador periférico desee consultar {{site.data.keyword.ieam}} Exchange o puede que un desarrollador de periferia desee probarlo con mandatos `hzn`, sin el agente completo.

1. Obtenga el paquete `horizon-cli`. En función de lo que la organización realizó en el paso [Recopilar archivos de nodo periférico](../hub/gather_files.md), puede obtener el paquete `horizon-cli` desde CSS o desde el archivo tar `agentInstallFiles-<edge-node-type>.tar.gz`:

   * Obtenga el paquete `horizon-cli` desde CSS:

      * Si todavía no tiene una clave de API, cree una siguiendo los pasos recogidos en [Creación de la clave de API](../hub/prepare_for_edge_nodes.md). Establezca las variables de entorno de ese paso:

         ```bash
         export HZN_EXCHANGE_USER_AUTH=iamapikey:<clave-api>   export HZN_ORG_ID=<su-organización-exchange>   export HZN_FSS_CSSURL=https://<ingreso-centro-gestión-ieam>/edge-css/
         ```
         {: codeblock}

      * Establezca `HOST_TYPE` en uno de estos valores que coincide con el tipo de host  en el que está instalando en el paquete `horizon-cli`:

         * linux-deb-amd64
         * linux-deb-arm64
         * linux-deb-armhf
         * linux-rpm-x86_64
         * linux-rpm-ppc64le
         * macos-pkg-x86_64

         ```bash
         HOST_TYPE=<host-type>
         ```
         {: codeblock}

      * Descargue el archivo certificate, config y el archivo tar  que contiene el paquete `horizon-cli` desde CSS:

         ```bash
         curl -sSL -w "%{http_code}" -u "$HZN_ORG_ID/$HZN_EXCHANGE_USER_AUTH" -k -o agent-install.crt $HZN_FSS_CSSURL/api/v1/objects/IBM/agent_files/agent-install.crt/data curl -sSL -w "%{http_code}" -u "$HZN_ORG_ID/$HZN_EXCHANGE_USER_AUTH" --cacert agent-install.crt -o agent-install.cfg $HZN_FSS_CSSURL/api/v1/objects/IBM/agent_files/agent-install.cfg/data  curl -sSL -w "%{http_code}" -u "$HZN_ORG_ID/$HZN_EXCHANGE_USER_AUTH" --cacert agent-install.crt -o horizon-agent-$HOST_TYPE.tar.gz $HZN_FSS_CSSURL/api/v1/objects/IBM/agent_files/horizon-agent-$HOST_TYPE.tar.gz/data
         ```
         {: codeblock}

      * Extraiga el paquete `horizon-cli`del archivo tar:

         ```bash
         rm -f horizon-cli*   # remove any previous versions tar -zxvf horizon-agent-$HOST_TYPE.tar.gz
         ```
         {: codeblock}

   * O bien, obtenga el paquete `horizon-cli` del archivo tar `agentInstallFiles-<edge-node-type>.tar.gz`:

      * Obtenga el archivo `agentInstallFiles-<edge-node-type>.tar.gz` del administrador del centro de gestión, donde `<edge-node-type>` coincide con el host en el que está instalando `horizon-cli`. Copie este archivo en este host.

      * Desempaquete el archivo tar:

         ```bash
         tar -zxvf agentInstallFiles-<tipo-de-dispositivo-periférico>.tar.gz
         ```
         {: codeblock}

2. Cree o actualice `/etc/default/horizon`:

   ```bash
   sudo cp agent-install.cfg /etc/default/horizon sudo cp agent-install.crt /etc/horizon sudo sh -c "echo 'HZN_MGMT_HUB_CERT_PATH=/etc/horizon/agent-install.crt' >> /etc/default/horizon"
   ```
   {: codeblock}

3. Instale el paquete `horizon-cli`:

   * Confirme que la versión de paquete es la misma que el agente de dispositivo listado en [Componentes](../getting_started/components.md).

   * En un distro basado en debian:

     ```bash
     sudo apt update && sudo apt install ./horizon-cli*.deb
     ```
     {: codeblock}

   * En un distro basado en RPM:

     ```bash
     sudo yum install ./horizon-cli*.rpm
     ```
     {: codeblock}

   * En {{site.data.keyword.macOS_notm}}:

     ```bash
     sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain horizon-cli.crt sudo installer -pkg horizon-cli-*.pkg -target / pkgutil --pkg-info com.github.open-horizon.pkg.horizon-cli   # confirm version installed
     ```
     {: codeblock}

## Desinstalación de la CLI hzn

Si desea eliminar el paquete `horizon-cli` de un host:

* Desinstale `horizon-cli` de un distro basado en debian:

  ```bash
  sudo apt-get remove horizon-cli
  ```
  {: codeblock}

* Desinstale `horizon-cli` desde un distro basado en Debian:

  ```bash
  sudo yum remove horizon-cli
  ```
  {: codeblock}

* O desinstale `horizon-cli` de {{site.data.keyword.macOS_notm}}:

  ```bash
  sudo horizon-cli-uninstall.sh
  ```
  {: codeblock}
