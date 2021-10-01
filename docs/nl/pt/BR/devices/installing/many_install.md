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

# Instalação e registro em massa do agente
{: #batch-install}

Use o processo de instalação em massa para configurar vários dispositivos de borda de tipos semelhantes (em outras palavras, que tenham a mesma arquitetura, o mesmo sistema operacional, o mesmo padrão ou a mesma política).

Nota: para este processo, os dispositivos de borda de destino que são computadores macOs não são suportados. No entanto, se desejado, é possível conduzir esse processo a partir de um computador macOs. (Em outras palavras, o host pode ser um computador macOs).

### Pré-requisitos

* Os dispositivos a serem instalados e registrados devem ter acesso à rede para o hub de gerenciamento.
* Os dispositivos já devem ter um sistema operacional instalado.
* Se você estiver usando DHCP para dispositivos de borda, cada dispositivo deverá manter o mesmo endereço IP até que a tarefa seja concluída (ou o mesmo `hostname`, caso esteja usando DDNS).
* Todas as entradas do usuário do serviço de borda devem ser especificadas como padrões na definição de serviço ou no padrão ou na política de implementação. Não é possível usar entradas de usuário específicas do nó.

### Procedimento
{: #proc-multiple}

1. Caso ainda não tenha feito isso, obtenha ou crie o arquivo **agentInstallFiles-&lt;edge-device-type&gt;.tar.gz** e a chave de API, seguindo [Reúna as informações e os arquivos necessários para dispositivos de borda](../../hub/gather_files.md#prereq_horizon). Configure o nome do arquivo e o valor da chave de API nestas variáveis de ambiente:

   ```bash
   export AGENT_TAR_FILE=agentInstallFiles-<edge-device-type>.tar.gz
   export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
   ```
  {: codeblock}

2. O pacote **pssh** inclui os comandos **pssh** e **pscp**, que permitem executar comandos para vários dispositivos de borda em paralelo e copiar arquivos para vários dispositivos de borda em paralelo. Caso ainda não possua esses comandos no host, instale o pacote agora:

  * No {{site.data.keyword.linux_notm}}:

   ```bash
   sudo apt install pssh
   alias pssh=parallel-ssh
   alias pscp=parallel-scp
   ```
   {: codeblock}

  * No {{site.data.keyword.macOS_notm}}:

   ```bash
   brew install pssh
   ```
   {: codeblock}

   (Se o **brew** ainda não estiver instalado, consulte: [Instalar o pssh no computador macOs com Brew ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://brewinstall.org/Install-pssh-on-Mac-with-Brew/)).

3. Há várias maneiras de fornecer os acessos **pscp** e **pssh** aos dispositivos de borda. Esta seção descreve o uso de uma chave pública ssh. O primeiro requisito é que este host deve ter um par de chaves ssh (geralmente em **~/.ssh/id_rsa** e **~/.ssh/id_rsa.pub**). Se ainda não houver um, gere-o:

   ```bash
   ssh-keygen -t rsa
   ```
   {: codeblock}

4. Coloque o conteúdo da chave pública privada (**~/.ssh/id_rsa.pub**) de cada dispositivo de borda em **/root/.ssh/authorized_keys** .

5. Crie um arquivo de mapeamento de duas colunas chamado **node-id-mapping.csv**, mapeando o endereço IP ou nome de host de cada dispositivo de borda para o nome de nó do {{site.data.keyword.ieam}} que ele deve receber durante o registro. Quando **agent-install.sh** for executado em cada dispositivo de borda, esse arquivo informará o nome de nó de borda a ser fornecido a esse dispositivo. Use o formato CSV:

   ```bash
   Hostname/IP, Node Name
   1.1.1.1, factory2-1
   1.1.1.2, factory2-2
   ```
   {: codeblock}

6. Inclua **node-id-mapping.csv** no arquivo tar do agente:

   ```bash
   gunzip $AGENT_TAR_FILE
   tar -uf ${AGENT_TAR_FILE%.gz} node-id-mapping.csv
   gzip ${AGENT_TAR_FILE%.gz}
   ```
   {: codeblock}

7. Em um arquivo chamado **nodes.hosts** coloque a lista de dispositivos de borda a serem instalados e registrados em massa. Isso será usado com os comandos **pscp** e **pssh**. Cada linha deve estar no formato ssh padrão `<user>@<IP-or-hostname>` :

   ```bash
   root@1.1.1.1
   root@1.1.1.2
   ```
   {: codeblock}

   Nota: se você usar um usuário não raiz para qualquer um dos hosts, o sudo deverá ser configurado para permitir o sudo desse usuário sem inserir uma senha.

8. Copie o arquivo tar do agente para os dispositivos de borda. Esta etapa pode demorar um pouco:

   ```bash
   pscp -h nodes.hosts -e /tmp/pscp-errors $AGENT_TAR_FILE /tmp
   ```
   {: codeblock}

   Nota: se você receber **[FAILURE]** na saída **pscp** para qualquer um dos dispositivos de borda, será possível ver os erros em **/tmp/pscp-errors**.

9. Execute **agent-install.sh** em cada dispositivo de borda para instalar o agente do Horizon e registrar os dispositivos de borda. É possível registrar os dispositivos de borda usando um padrão ou uma política:

   1. Registre os dispositivos de borda com um padrão:

      ```bash
      pssh -h nodes.hosts -t 0 "bash -c \"tar -zxf /tmp/$AGENT_TAR_FILE agent-install.sh && sudo -s ./agent-install.sh -i . -u $HZN_EXCHANGE_USER_AUTH -p IBM/pattern-ibm.helloworld -w ibm.helloworld -o IBM -z /tmp/$AGENT_TAR_FILE 2>&1 >/tmp/agent-install.log \" "
      ```
      {: codeblock}

      Em vez de registrar os dispositivos de borda com o padrão de implementação **IBM/pattern-ibm.helloworld**, é possível usar um padrão de implementação diferente modificando as sinalizações **-p**, **-w** e **-o**. Para ver todas as descrições de sinalizações disponíveis de **agent-install.sh**:

      ```bash
      tar -zxf $AGENT_TAR_FILE agent-install.sh &&./agent-install.sh -h
      ```
      {: codeblock}

   2. Ou, registre os dispositivos de borda com a política. Crie uma política de nó, copie-a para os dispositivos de borda e registre os dispositivos com essa política:

      ```bash
      echo '{ "properties": [ { "name": "nodetype", "value": "special-node" } ] }' > node-policy.json
      pscp -h nodes.hosts -e /tmp/pscp-errors node-policy.json /tmp
      pssh -h nodes.hosts -t 0 "bash -c \"tar -zxf /tmp/$AGENT_TAR_FILE agent-install.sh && sudo -s ./agent-install.sh -i . -u $HZN_EXCHANGE_USER_AUTH -n /tmp/node-policy.json  -z /tmp/$AGENT_TAR_FILE 2>&1 >/tmp/agent-install.log \" "
      ```
      {: codeblock}

      Neste ponto, os dispositivos de borda estão prontos, mas não começarão a executar os serviços de borda até que você crie uma política de implementação (política de negócios) que especifique que um serviço deve ser implementado neste tipo de dispositivo de borda (neste exemplo, dispositivos com **nodetype** de **special-node**). Consulte [Usando a política de implementação](../using_edge_devices/detailed_policy.md) para obter detalhes.

10. Se você receber **[FAILURE]** na saída do **pssh** para qualquer um dos dispositivos de borda, será possível investigar o problema acessando o dispositivo de borda e visualizando **/tmp/agent-install.log**.

11. Durante a execução do comando **pssh**, é possível visualizar o status dos nós de borda no console do {{site.data.keyword.edge_notm}}. Consulte [Usando o console de gerenciamento](../getting_started/accessing_ui.md).
