---

copyright:
years: 2019
lastupdated: "2019-10-28"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Instalación y registro manuales avanzados del agente
{: #advanced_man_install}

Este contenido describe cada paso manual para instalar el agente de {{site.data.keyword.edge_notm}} en un dispositivo periférico y registrarlo. Para obtener un método más automatizado, consulte [Instalación y registro automatizados de agente](automated_install.md).
{:shortdesc}

## Instalación del agente
{: #agent_install}

**Nota**: para obtener más información sobre la sintaxis de mandato, consulte [Convenciones utilizadas en este documento](../getting_started/document_conventions.md).

1. Obtenga el archivo `agentInstallFiles-<edge-device-type>.tar.gz` antes de continuar y la clave de API que se crea junto con este archivo antes de continuar este proceso.

    Como paso posterior a la configuración para la [Instalación del centro de gestión](../hub/online_installation.md), se ha creado automáticamente un archivo comprimido. Este archivo contiene los archivos necesarios para instalar el agente de {{site.data.keyword.horizon}} en el dispositivo periférico y registrarlo en el ejemplo helloworld.

2. Copie estar archivo en el dispositivo periférico con un lápiz USB, el mandato de copia segura u otro método.

3. Expanda el archivo tar:

   ```bash
   tar -zxvf agentInstallFiles-<tipo-de-dispositivo-periférico>.tar.gz
   ```
   {: codeblock}

4. Utilice cualquiera de las secciones siguientes que se aplican a su tipo de dispositivo periférico.

**Nota**: si Linux no es una de las distribuciones soportadas y admite contenedores, consulte el tema sobre [Instalación del agente de contenedor](https://github.com/open-horizon/anax/blob/master/docs/agent_container_manual_deploy.md) para obtener instrucciones sobre cómo utilizar el agente contenerizado.

### Instalación del agente en dispositivos periféricos Linux (ARM de 32 bits, ARM de 64 bits, ppc64le o x86_64) o en máquinas virtuales
{: #agent_install_linux}

Siga estos pasos:

1. Inicie la sesión y como usuario no root, cambie a un usuario con privilegios de root:

   ```bash
   sudo -s
   ```
   {: codeblock}

2. Consulte la versión de Docker para comprobar si es lo suficientemente reciente:

   ```bash
   docker --version
   ```
   {: codeblock}

      Si Docker no está instalado, o la versión es anterior a la `18.06.01`, instale la versión más reciente de Docker:

   ```bash
   curl -fsSL get.docker.com | sh       docker --version
   ```
   {: codeblock}

3. Instale los paquetes de Horizon que ha copiado en este dispositivo periférico:

   * Para las distribuciones Debian/Ubuntu:
      ```bash apt update && apt install ./*horizon*.deb
      ```
      {: codeblock}

   * Para las distribuciones Red Hat Enterprise Linux&reg;:
      ```bash      yum install ./*horizon*.rpm
      ```
      {: codeblock}
   
4. Establezca la información específica como variables de entorno:

   ```bash
   eval export $(cat agent-install.cfg)
   ```
   {: codeblock}

5. Apunte el agente Horizon del dispositivo periférico al clúster de {{site.data.keyword.edge_notm}} llenando `/etc/default/horizon` con la información correcta:

   ```bash
   sed -i.bak -e "s|^HZN_EXCHANGE_URL=[^ ]*|HZN_EXCHANGE_URL=${HZN_EXCHANGE_URL}|g" -e "s|^HZN_FSS_CSSURL=[^ ]*|HZN_FSS_CSSURL=${HZN_FSS_CSSURL}|g" /etc/default/horizon
   ```
   {: codeblock}

6. Haga que el agente de horizonte confíe en `agent-install.crt`:

   ```bash
   if grep -qE '^HZN_MGMT_HUB_CERT_PATH=' /etc/default/horizon; then sed -i.bak -e "s|^HZN_MGMT_HUB_CERT_PATH=[^ ]*|HZN_MGMT_HUB_CERT_PATH=${PWD}/agent-install.crt|" /etc/default/horizon; else echo "HZN_MGMT_HUB_CERT_PATH=${PWD}/agent-install.crt" >> /etc/default/horizon; fi
   ```
   {: codeblock}
   
7. Reinicie el agente para seleccionar los cambios en `/etc/default/horizon`:

   ```bash
   systemctl restart horizon.service
   ```
   {: codeblock}

8. Verifique que el agente se está ejecutando y está correctamente configurado:

   ```bash
   hzn version        hzn exchange version        hzn node list
   ```
   {: codeblock}  

      La salida debe tener un aspecto similar a este ejemplo (los números de versión y los URL pueden ser diferentes):

   ```bash
   $ hzn version    Horizon CLI versión: 2.23.29    Horizon Agent versión: 2.23.29    $ hzn exchange versión    1.116.0    $ hzn node list    {
         "id": "",          "organization": null,          "pattern": null,          "name": null,          "token_last_valid_time": "",          "token_valid": null,          "ha": null,          "configstate": {
            "state": "unconfigured",             "last_update_time": ""
         },          "configuration": {
            "exchange_api": "https://9.30.210.34:8443/ec-exchange/v1/",             "exchange_version": "1.116.0",             "required_minimum_exchange_version": "1.116.0",             "preferred_exchange_version": "1.116.0",             "mms_api": "https://9.30.210.34:8443/ec-css",             "architecture": "amd64",             "horizon_version": "2.23.29"
         },          "connectivity": {
            "firmware.bluehorizon.network": true,             "images.bluehorizon.network": true          }
      }
      ```
   {: codeblock}

9. Si ha cambiado previamente al shell privilegiado, salga de él ahora. No necesita acceso de usuario root para el siguiente paso del registro del dispositivo.

   ```bash
   exit
   ```
   {: codeblock}

10. Continúe con el [Registro del agente](#agent_reg).

### Instalación del agente en un dispositivo periférico Mac OS
{: #mac-os-x}

1. Importe el certificado del paquete `horizon-cli` en la cadena de claves {{site.data.keyword.macOS_notm}}:

   ```bash
   sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain horizon-cli.crt
   ```
   {: codeblock}

      **Nota**:  Es necesario completar este paso únicamente una vez en cada máquina {{site.data.keyword.macOS_notm}}. Con este certificado de confianza importado, puede instalar cualquier versión futura del software de {{site.data.keyword.horizon}}.

2. Instale el paquete de CLI de {{site.data.keyword.horizon}}:

   ```bash
   sudo installer -pkg horizon-cli-*.pkg -target /
   ```
   {: codeblock}

3. Habilite la finalización de nombre de submandato para el mandato `hzn`, añadiendo lo siguiente a `~/.bashrc`:

  ```bash
  source /usr/local/share/horizon/hzn_bash_autocomplete.sh
  ```
  {: codeblock}

4. Cuando instale un **dispositivo nuevo**, este paso no será necesario. Pero si ha instalado e iniciado el contenedor de Horizon en esta máquina anteriormente, deténgalo ahora ejecutando:

  ```bash
  horizon-container stop
  ```
  {: codeblock}
5. Establezca la información específica como variables de entorno:

  ```bash
  eval export $(cat agent-install.cfg)
  ```
  {: codeblock}

6. Apunte el agente Horizon del dispositivo periférico al clúster de {{site.data.keyword.edge_notm}} llenando `/etc/default/horizon` con la información correcta:

  ```bash
  sudo mkdir -p /etc/default

  sudo sh -c "cat << EndOfContent > /etc/default/horizon   HZN_EXCHANGE_URL=$HZN_EXCHANGE_URL   HZN_FSS_CSSURL=$HZN_FSS_CSSURL   HZN_MGMT_HUB_CERT_PATH=${PWD}/agent-install.crt   HZN_DEVICE_ID=$(hostname)   EndOfContent"
  ```
  {: codeblock}

7. Inicie el agente {{site.data.keyword.horizon}}:

  ```bash
  horizon-container start
  ```
  {: codeblock}

8. Verifique que el agente se está ejecutando y está correctamente configurado:

  ```bash
  hzn version        hzn exchange version        hzn node list
  ```
  {: codeblock}

      La salida debería tener un aspecto similar a esto (los números de versión y los URL podrían ser diferentes):

  ```bash
  $ hzn version    Horizon CLI versión: 2.23.29    Horizon Agent versión: 2.23.29    $ hzn exchange versión    1.116.0    $ hzn node list    {
         "id": "",          "organization": null,          "pattern": null,          "name": null,          "token_last_valid_time": "",          "token_valid": null,          "ha": null,          "configstate": {
            "state": "unconfigured",             "last_update_time": ""
         },          "configuration": {
            "exchange_api": "https://9.30.210.34:8443/ec-exchange/v1/",             "exchange_version": "1.116.0",             "required_minimum_exchange_version": "1.116.0",             "preferred_exchange_version": "1.116.0",             "mms_api": "https://9.30.210.34:8443/ec-css",             "architecture": "amd64",             "horizon_version": "2.23.29"
         },          "connectivity": {
            "firmware.bluehorizon.network": true,             "images.bluehorizon.network": true          }
      }
  ```
  {: codeblock}

9. Continúe con el [Registro del agente](#agent_reg).

## Registro del agente
{: #agent_reg}

1. Establezca la información específica como **variables de entorno**:

  ```bash
  eval export $(cat agent-install.cfg)   export HZN_EXCHANGE_USER_AUTH=iamapikey:<clave-api>
  ```
  {: codeblock}

2. Vea la lista de patrones de despliegue de servicio periférico de ejemplo:

  ```bash
  hzn exchange pattern list IBM/
  ```
  {: codeblock}

3. El servicio periférico helloworld es el ejemplo más básico, lo que lo convierte en un buen lugar para empezar. **Registre** el dispositivo periférico con {{site.data.keyword.horizon}} para ejecutar el **patrón de despliegue helloworld**:

  ```bash
  hzn register -p IBM/pattern-ibm.helloworld
  ```
  {: codeblock}

  **Nota**: el ID de nodo mostrado en la salida en la línea que empieza por **Utilización de ID de nodo**.

4. El dispositivo periférico hará un acuerdo con uno de los bots de acuerdo de {{site.data.keyword.horizon}} (este proceso suele durar unos 15 segundos). **Consulte repetidamente los acuerdos** de este dispositivo hasta que los campos `agreement_finalized_time` y `agreement_execution_start_time` estén completos:

  ```bash
  hzn agreement list
  ```
  {: codeblock}

5. **Después de que se haya realizado el acuerdo**, liste el servicio periférico de contenedor Docker que se ha iniciado como resultado:

  ```bash
  sudo docker ps
  ```
  {: codeblock}

6. Vea la **salida** del servicio periférico helloworld:

  ```bash
  sudo hzn service log -f ibm.helloworld
  ```
  {: codeblock}

## Qué hacer a continuación
{: #what_next}

Vaya a [Uso de CPU en IBM Event Streams](../using_edge_services/cpu_load_example.md) para continuar con otros ejemplos de servicio periférico.
