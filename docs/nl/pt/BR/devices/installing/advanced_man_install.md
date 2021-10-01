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

# Instalação e registro manuais avançados do agente
{: #advanced_man_install}

Esta etapa descreve cada etapa manual para instalar o agente {{site.data.keyword.edge_devices_notm}} em um dispositivo de borda e registrá-lo. Para obter um método mais automatizado, consulte [Instalação e registro automatizados do agente](automated_install.md).
{:shortdesc}

## Instalando o Agente
{: #agent_install}

Nota: consulte [Convenções usadas neste documento](../../getting_started/document_conventions.md) para obter informações sobre a sintaxe de comando.

1. Antes de continuar, obtenha o arquivo `agentInstallFiles-<edge-device-type>.tar.gz` e a Chave de API que é criada juntamente com esse arquivo.

    Como uma etapa de pós-instalação para [Instalando o hub de gerenciamento](../../hub/offline_installation.md), foi criado um arquivo compactado que contém os arquivos necessários para instalar o agente {{site.data.keyword.horizon}} no dispositivo de borda e registrá-lo com o exemplo helloworld.

2. Copie este arquivo para o dispositivo de borda com um dispositivo USB, o comando de cópia segura ou outro método.

3. Expanda o arquivo tar:

   ```bash
   tar -zxvf agentInstallFiles-<edge-device-type>.tar.gz
   ```
   {: codeblock}

4. Use qualquer uma das seções a seguir, que seja aplicável ao seu tipo de dispositivo de borda.

### Instalando o agente em dispositivos de borda ou máquinas virtuais Linux (ARM 32-bit, ARM 64-bit ou x86_64)
{: #agent_install_linux}

Siga
estas etapas:

1. Efetue login e, caso esteja conectado como um usuário não raiz, alterne para um usuário com privilégios de administrador:

   ```bash
   sudo -s
   ```
   {: codeblock}

2. Consulte a versão do Docker para verificar se ela é recente o suficiente:

   ```bash
   docker -- version
   ```
   {: codeblock}

      Se o Docker não estiver instalado ou se a versão for mais antiga que `18.06.01`, instale a versão mais recente do Docker:

   ```bash
   curl -fsSL get.docker.com | sh
      docker --version
   ```
   {: codeblock}

3. Instale os pacotes do Horizon Debian que você copiou para este dispositivo de borda:

   ```bash
   apt update && apt install ./*horizon*.deb
   ```
   {: codeblock}
   
4. Configure suas informações específicas como variáveis de ambiente:

   ```bash
   eval export $(cat agent-install.cfg)
   ```
   {: codeblock}

5. Aponte seu agente de horizonte de dispositivo de borda para o cluster do {{site.data.keyword.edge_notm}} preenchendo o `/etc/default/horizon` com as informações corretas:

   ```bash
   sed -i.bak -e "s|^HZN_EXCHANGE_URL=[^ ]*|HZN_EXCHANGE_URL=${HZN_EXCHANGE_URL}|g" -e "s|^HZN_FSS_CSSURL=[^ ]*|HZN_FSS_CSSURL=${HZN_FSS_CSSURL}|g" /etc/default/horizon
   ```
   {: codeblock}

6. Faça com que o agente do Horizon confie em `agent-install.crt`:

   ```bash
   if grep -qE '^HZN_MGMT_HUB_CERT_PATH=' /etc/default/horizon; then sed -i.bak -e "s|^HZN_MGMT_HUB_CERT_PATH=[^ ]*|HZN_MGMT_HUB_CERT_PATH=${PWD}/agent-install.crt|" /etc/default/horizon; else echo "HZN_MGMT_HUB_CERT_PATH=${PWD}/agent-install.crt" >> /etc/default/horizon; fi
   ```
   {: codeblock}
   
7. Reinicie o agente para obter as mudanças no `/etc/default/horizon`:

   ```bash
   systemctl restart horizon.service
   ```
   {: codeblock}

8. Verifique se o agente está em execução e configurado corretamente:

   ```bash
   hzn version
       hzn exchange version
       hzn node list
   ```
   {: codeblock}  

      A saída deve ser semelhante a esta (os números de versão e as URLs podem ser diferentes):

   ```bash
   $ hzn version
   Horizon CLI version: 2.23.29
   Horizon Agent version: 2.23.29
   $ hzn exchange version
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

9. Caso tenha alternado para o shell privilegiado anteriormente, saia agora. Não é necessário ter acesso raiz para a próxima etapa do registro do dispositivo.

   ```bash
   sair
   ```
   {: codeblock}

10. Continue em [Registrando o agente](#agent_reg).

### Instalando o agente em um dispositivo de borda macOS
{: #mac-os-x}

1. Importe o certificado de pacote `horizon-cli` em seu keychain {{site.data.keyword.macOS_notm}}:

   ```bash
   sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain horizon-cli.crt
   ```
   {: codeblock}

      Nota: é necessário concluir esta etapa apenas uma vez em cada máquina {{site.data.keyword.macOS_notm}}. Com esse certificado confiável importado, será possível instalar qualquer versão futura do software {{site.data.keyword.horizon}}.

2. Instale o pacote da CLI do {{site.data.keyword.horizon}}:

   ```bash
   sudo installer -pkg horizon-cli-*.pkg -target /
   ```
   {: codeblock}

3. O comando anterior inclui comandos para `/usr/local/bin`. Inclua esse diretório no caminho do shell incluindo isto em `~/.bashrc`:

   ```bash
   export PATH="/usr/local/bin:$PATH"
   ```
   {: codeblock}

4. Inclua `/usr/local/share/man` no caminho da página do manual, incluindo esse diretório no caminho do shell, incluindo isto em `~/.bashrc`:

  ```bash
  export MANPATH="/usr/local/share/man:$MANPATH"
  ```
  {: codeblock}

5. Ative a conclusão do nome do subcomando para o comando `hzn`, incluindo isto em `~/.bashrc`:

  ```bash
  source /usr/local/share/horizon/hzn_bash_autocomplete.sh
  ```
  {: codeblock}

6. Quando você instala um **novo dispositivo**, esta etapa **não** é necessária. No entanto, se você instalou e iniciou o contêiner do Horizon nesta máquina anteriormente, pare-o agora executando:

  ```bash
  horizon-container stop
  ```
  {: codeblock}
7. Configure suas informações específicas como variáveis de ambiente:

  ```bash
  eval export $(cat agent-install.cfg)
  ```
  {: codeblock}

8. Aponte seu agente de horizonte de dispositivo de borda para o cluster do {{site.data.keyword.edge_notm}} preenchendo o `/etc/default/horizon` com as informações corretas:

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

9. Inicie o agente {{site.data.keyword.horizon}}:

  ```bash
  horizon-container start
  ```
  {: codeblock}

10. Verifique se o agente está em execução e configurado corretamente:

  ```bash
  hzn version
       hzn exchange version
       hzn node list
  ```
  {: codeblock}

      A saída deve ser semelhante a esta (os números de versão e as URLs podem ser diferentes):

  ```bash
  $ hzn version
  Horizon CLI version: 2.23.29
  Horizon Agent version: 2.23.29
  $ hzn exchange version
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

11. Continue em [Registrando o agente](#agent_reg).

## Registrando o agente
{: #agent_reg}

1. Configure suas informações específicas como **variáveis de ambiente**:

  ```bash
  eval export $(cat agent-install.cfg)
  export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
  ```
  {: codeblock}

2. Visualize a lista de padrões de implementação do serviço de borda de amostra:

  ```bash
  hzn exchange pattern list IBM/
  ```
  {: codeblock}

3. O serviço de borda do helloworld é o exemplo mais básico, o que o torna um bom local para começar. **Registre** seu dispositivo de borda com o {{site.data.keyword.horizon}} para executar o **padrão de implementação helloworld**:

  ```bash
  hzn register -p IBM/pattern-ibm.helloworld
  ```
  {: codeblock}

  Nota: o ID do nó mostrado na saída na linha que começa com **Usando o ID do nó**.

4. O dispositivo de borda fará um acordo com um dos robôs de contrato do {{site.data.keyword.horizon}} (em geral, isso leva cerca de 15 segundos). **Consulte repetidamente os contratos** desse dispositivo até que os campos `agreement_finalized_time` e `agreement_execution_start_time` sejam preenchidos:

  ```bash
  hzn agreement list
  ```
  {: codeblock}

5. **Depois que o contrato for feito**, liste o serviço de borda do contêiner do docker que foi iniciado como resultado:

  ```bash
  sudo docker ps
  ```
  {: codeblock}

6. Visualize o serviço de borda helloworld **saída**:

  ```bash
  sudo hzn service log -f ibm.helloworld
  ```
  {: codeblock}

## O que fazer a seguir
{: #what_next}

Navegue [Uso da CPU para o IBM Event Streams](cpu_load_example.md) para obter outros exemplos de serviço de borda.
