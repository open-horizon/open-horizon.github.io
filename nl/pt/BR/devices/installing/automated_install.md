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

# Instalação e registro automatizados do agente
{: #method_one}

Nota: essas etapas são as mesmas para todos os tipos de dispositivos (arquiteturas).

1. Obtenha junto ao administrador o arquivo **agentInstallFiles-&lt;edge-device-type&gt;.tar.gz** e uma chave de API. Ele já deve ter criado esses itens na seção [Reúna as informações e os arquivos necessários para dispositivos de borda](../../hub/gather_files.md#prereq_horizon). Copie esse arquivo para o dispositivo de borda, usando o comando de cópia segura, uma unidade flash USB ou outro método. Além disso, anote o valor da chave API. Ele será necessário em uma etapa posterior. Em seguida, configure o nome do arquivo em uma variável de ambiente para as etapas subsequentes:

   ```bash
   export AGENT_TAR_FILE=agentInstallFiles-<edge-device-type>.tar.gz
   ```
   {: codeblock}

2. Extraia o comando **agent-install.sh** a partir do arquivo tar:

   ```bash
   tar -zxvf $AGENT_TAR_FILE agent-install.sh
   ```
   {: codeblock}

3. Exporte suas credenciais de usuário do {{site.data.keyword.horizon}} Exchange (a chave de API):

  ```bash
  export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
  ```
  {: codeblock}

4. Execute o comando **agent-install.sh** para instalar e configurar o agente {{site.data.keyword.horizon}} e para registrar o dispositivo de borda para executar o serviço de borda de amostra helloworld:

  ```bash
  sudo -s ./agent-install.sh -i . -u $HZN_EXCHANGE_USER_AUTH -p IBM/pattern-ibm.helloworld -w ibm.helloworld -o IBM -z $AGENT_TAR_FILE
  ```
  {: codeblock}

  Nota: durante a instalação dos pacotes do agente, poderá ser perguntado o seguinte: "Deseja sobrescrever a configuração do nó atual?`[y/N]`:" é possível responder "y" e pressionar Enter, porque **agent-install.sh** fará a configuração corretamente.

  Para ver todas as descrições de sinalizações disponíveis de **agent-install.sh**:

  ```bash
  ./agent-install.sh -h
  ```
  {: codeblock}

5. Agora que o dispositivo de borda está instalado e registrado, configure as informações específicas, como variáveis de ambiente, no shell. Isso permite a execução do comando **hzn** para visualizar a saída de helloworld:

  ```bash
  eval export $(cat agent-install.cfg)
  hzn service log -f ibm.helloworld
  ```
  {: codeblock}
  
  Nota: pressione **Ctrl** **C** para parar a exibição de saída.

6. Explore as sinalizações e os subcomandos do comando **hzn**:

  ```bash
  hzn --help
  ```
  {: codeblock}

7. Também é possível visualizar seus nós de borda (nós), seus serviços, seus padrões e suas políticas usando o console do {{site.data.keyword.ieam}}. Consulte [Usando o console de gerenciamento](../getting_started/accessing_ui.md).

8. Navegue [Uso da CPU para o IBM Event Streams](cpu_load_example.md) para obter outros exemplos de serviço de borda.
