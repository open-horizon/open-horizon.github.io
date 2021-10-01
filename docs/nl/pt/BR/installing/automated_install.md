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

Nota: essas etapas são iguais para todos os tipos de dispositivos de borda (arquiteturas).

1. Se você ainda não tem uma chave API, crie uma seguindo as etapas em [Criando sua chave de API](../hub/prepare_for_edge_nodes.md). Esse processo cria uma chave de API, localiza alguns arquivos e reúne valores da variável de ambiente que serão necessários quando você estiver configurando nós de borda.

2. Efetue login em seu dispositivo de borda e configure as mesmas variáveis de ambiente que você obteve na etapa 1:

   ```bash
   export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>   export HZN_ORG_ID=<your-exchange-organization>   export HZN_FSS_CSSURL=https://<ieam-management-hub-ingress>/edge-css/
   ```
   {: codeblock}

3. Se não estiver usando um pacote configurável de instalação preparado pelo administrador, faça download do script **agent-install.sh** por meio do Cloud Sync Service (CSS) para seu dispositivo e torne-o executável:

   ```bash
   curl -u "$HZN_ORG_ID/$HZN_EXCHANGE_USER_AUTH" -k -o agent-install.sh $HZN_FSS_CSSURL/api/v1/objects/IBM/agent_files/agent-install.sh/data    chmod +x agent-install.sh
   ```
   {: codeblock}

4. Execute **agent-install.sh** para obter os arquivos necessários do CSS, instale e configure o agente {{site.data.keyword.horizon}} e registre seu dispositivo de borda para executar o serviço de borda de amostra Hello World:

   ```bash
   sudo -s -E ./agent-install.sh -i 'css:' -p IBM/pattern-ibm.helloworld -w '*' -T 120
   ```
   {: codeblock}

   Para ver todas as descrições de sinalizadores **agent-install.sh** disponíveis, execute: **./agent-install.sh -h**

   Nota: no {{site.data.keyword.macOS_notm}}, o agente será executado em um contêiner do Docker em execução como raiz.

5. Veja a saída do Hello World:

   ```bash
   hzn service log -f ibm.helloworld   # Press Ctrl-c to stop the output display
   ```
   {: codeblock}

6. Se o serviço de borda Hello World não iniciar, execute este comando para ver as mensagens de erro:

   ```bash
   hzn eventlog list -f   # Press Ctrl-c to stop the output display
   ```
   {: codeblock}

7. (opcional) Use o comando **hzn**  neste nó de borda para visualizar serviços, padrões e políticas de implementação no {{site.data.keyword.horizon}} Exchange. Configure suas informações específicas como variáveis de ambiente em seu shell e execute estes comandos:

   ```bash
   eval export $(cat agent-install.cfg)   hzn exchange service list IBM/   hzn exchange pattern list IBM/   hzn exchange deployment listpolicy
   ```
   {: codeblock}

8. Explore todos os subcomandos e sinalizações de comando **hzn**:

   ```bash
   hzn --help
   ```
   {: codeblock}

## O que vem depois

* Use o console do {{site.data.keyword.ieam}} para visualizar os seus nós de borda (dispositivos), serviços, padrões e políticas. Para obter mais informações, consulte [Usando o console de gerenciamento](../console/accessing_ui.md).
* Explore e execute outro exemplo de serviço de borda. Para obter mais informações, consulte [Uso de CPU para o IBM Event Streams](../using_edge_services/cpu_load_example.md).
