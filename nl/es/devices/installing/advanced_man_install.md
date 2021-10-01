---

copyright:
years: 2019
lastupdated: "2019-011-14"

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

En esta sección se describe cada paso manual para instalar el agente de {{site.data.keyword.edge_devices_notm}} en un dispositivo periférico y registrarlo. Para
obtener un método más automatizado, consulte [Instalación y registro
automatizados de agente](automated_install.md).{:shortdesc}

## Instalación del agente
{: #agent_install}

Nota: consulte [Convenciones utilizadas en este documento](../../getting_started/document_conventions.md)
para obtener información sobre la sintaxis de mandatos.

1. Antes de continuar obtenga el archivo `agentInstallFiles-<edge-device-type>.tar.gz`
y la clave de API que se crea junto con este archivo. 

    Como paso posterior a la configuración para la [Instalación del centro de gestión](../../hub/offline_installation.md),
se ha creado un archivo comprimido que contiene los archivos necesarios para instalar el agente
{{site.data.keyword.horizon}} en el dispositivo periférico y registrarlo con el ejemplo helloworld.

2. Copie estar archivo en el dispositivo periférico con un lápiz USB, el mandato de copia segura u otro método.

3. Expanda el archivo tar:

   ```bash
   tar -zxvf agentInstallFiles-<tipo-de-dispositivo-periférico>.tar.gz
   ```
   {: codeblock}

4. Utilice cualquiera de las secciones siguientes que se aplican a su tipo de dispositivo periférico.

### Instalación del agente en dispositivos periféricos de Linux (ARM 32 bits, ARM 64 bits o x86_64) o máquinas virtuales
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

      Si Docker no está instalado, o la versión es anterior a la `18.06.01`, instale
la versión más reciente de Docker:

   ```bash
   curl -fsSL get.docker.com | sh
      docker --version
   ```
   {: codeblock}

3. Instale los paquetes de Horizon Debian que ha copiado en este dispositivo periférico:

   ```bash
   apt update && apt install ./*horizon*.deb
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
   hzn version
       hzn exchange version
       hzn node list
   ```
   {: codeblock}  

      La salida debería tener un aspecto similar a esto (los números de versión y los URL podrían ser diferentes):

   ```bash
   $ hzn version
   Horizon CLI versión: 2.23.29
   Horizon Agent versión: 2.23.29
   $ hzn exchange versión
   1.116.0
   $ hzn node list
   {
         "id": "",
         "organization": null,
         "pattern": null,
         "name": null,
         "token_last_valid_time": "",
         "token_valid": null,
         "ha": null,
         "configstate": {
            "state": "unconfigured",
            "last_update_time": ""
         },
         "configuration": {
            "exchange_api": "https://9.30.210.34:8443/ec-exchange/v1/",
            "exchange_version": "1.116.0",
            "required_minimum_exchange_version": "1.116.0",
            "preferred_exchange_version": "1.116.0",
            "mms_api": "https://9.30.210.34:8443/ec-css",
            "architecture": "amd64",
            "horizon_version": "2.23.29"
         },
         "connectivity": {
            "firmware.bluehorizon.network": true,
            "images.bluehorizon.network": true
         }
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

      Nota: Debe completar este paso solo una vez en cada máquina de
{{site.data.keyword.macOS_notm}}. Con este certificado de confianza importado, puede instalar cualquier versión futura del software de {{site.data.keyword.horizon}}.

2. Instale el paquete de CLI de {{site.data.keyword.horizon}}:

   ```bash
   sudo installer -pkg horizon-cli-*.pkg -target /
   ```
   {: codeblock}

3. El mandato anterior añade mandatos a `/usr/local/bin`. Añada dicho directorio a la vía de acceso de shell añadiendo esto a `~/.bashrc`:

   ```bash
   export PATH="/usr/local/bin:$PATH"
   ```
   {: codeblock}

4. Añada `/usr/local/share/man` a la vía de acceso de la página man añadiendo dicho directorio a la vía de acceso de shell añadiendo esto a `~/.bashrc`:

  ```bash
  export MANPATH="/usr/local/share/man:$MANPATH"
  ```
  {: codeblock}

5. Habilite la finalización de nombre de submandato para el mandato `hzn`, añadiendo esto a
`~/.bashrc`:

  ```bash
  source /usr/local/share/horizon/hzn_bash_autocomplete.sh
  ```
  {: codeblock}

6. Cuando se instala un **dispositivo nuevo**, este paso **no**
es necesario. Sin embargo, si ha instalado e iniciado el contenedor de horizon en esta máquina anteriormente, deténgalo ahora ejecutando:

  ```bash
  horizon-container stop
  ```
  {: codeblock}
7. Establezca la información específica como variables de entorno:

  ```bash
  eval export $(cat agent-install.cfg)
  ```
  {: codeblock}

8. Apunte el agente Horizon del dispositivo periférico al clúster de {{site.data.keyword.edge_notm}} llenando `/etc/default/horizon` con la información correcta:

  ```bash
  sudo mkdir -p /etc/default

  sudo sh -c "cat << EndOfContent > /etc/default/horizon
  HZN_EXCHANGE_URL=$HZN_EXCHANGE_URL
  HZN_FSS_CSSURL=$HZN_FSS_CSSURL
  HZN_MGMT_HUB_CERT_PATH=${PWD}/agent-install.crt
  HZN_DEVICE_ID=$(hostname)
  EndOfContent"
  ```
  {: codeblock}

9. Inicie el agente {{site.data.keyword.horizon}}:

  ```bash
  horizon-container start
  ```
  {: codeblock}

10. Verifique que el agente se está ejecutando y está correctamente configurado:

  ```bash
  hzn version
       hzn exchange version
       hzn node list
  ```
  {: codeblock}

      La salida debería tener un aspecto similar a esto (los números de versión y los URL podrían ser diferentes):

  ```bash
  $ hzn version
   Horizon CLI versión: 2.23.29
   Horizon Agent versión: 2.23.29
   $ hzn exchange versión
   1.116.0
   $ hzn node list
   {
         "id": "",
         "organization": null,
         "pattern": null,
         "name": null,
         "token_last_valid_time": "",
         "token_valid": null,
         "ha": null,
         "configstate": {
            "state": "unconfigured",
            "last_update_time": ""
         },
         "configuration": {
            "exchange_api": "https://9.30.210.34:8443/ec-exchange/v1/",
            "exchange_version": "1.116.0",
            "required_minimum_exchange_version": "1.116.0",
            "preferred_exchange_version": "1.116.0",
            "mms_api": "https://9.30.210.34:8443/ec-css",
            "architecture": "amd64",
            "horizon_version": "2.23.29"
         },
         "connectivity": {
            "firmware.bluehorizon.network": true,
            "images.bluehorizon.network": true
         }
      }
  ```
  {: codeblock}

11. Continúe con el [Registro del agente](#agent_reg).

## Registro del agente
{: #agent_reg}

1. Establezca la información específica como **variables de entorno**:

  ```bash
  eval export $(cat agent-install.cfg)
  export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
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

  Nota: el ID de nodo que se muestra en la salida de la línea que empieza por
**Utilización del ID de nodo**.

4. El dispositivo periférico hará un acuerdo con uno de los bots de acuerdo {{site.data.keyword.horizon}} (normalmente se tardan unos 15 segundos). **Consulte repetidamente los acuerdos** de este dispositivo hasta que se rellenen los campos `agreement_finalized_time` y `agreement_execution_start_time`:

  ```bash
  hzn agreement list
  ```
  {: codeblock}

5. **Después de que se haya realizado el acuerdo**, liste el servicio periférico del contenedor Docker que se ha iniciado como resultado:

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

Vaya a [Uso de CPU en IBM Event Streams](cpu_load_example.md) para continuar con
otros ejemplos de servicio periférico.
