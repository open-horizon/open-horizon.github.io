---

copyright:
years: 2020
lastupdated: "2020-05-18"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Reunir arquivos de nó de borda
{: #prereq_horizon}

Vários arquivos são necessários para instalar o agente {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) em seus dispositivos de borda e clusters de borda e registrá-los com o {{site.data.keyword.ieam}}. Este conteúdo orienta você por meio de pacote configurável dos arquivos que são necessários para os seus nós de borda. Execute estas etapas em um host admin que esteja conectado ao hub de gerenciamento do {{site.data.keyword.ieam}}.

As etapas a seguir supõem que você tenha instalado os comandos [IBM Cloud Pak CLI (**cloudctl**) e OpenShift client CLI (**oc**)](../cli/cloudctl_oc_cli.md), e que você esteja executando as etapas no diretório de mídia de instalação descompactado **ibm-eam-{{site.data.keyword.semver}}-bundle**. Este script procura os pacotes do {{site.data.keyword.horizon}} necessários no arquivo **agent/edge-packages-{{site.data.keyword.semver}}.tar.gz** e cria a configuração necessária do nó de borda e arquivos de certificado.

1. Efetue login em seu cluster de hub de gerenciamento com credenciais de administrador e o namespace em que você instalou o {{site.data.keyword.ieam}}:
   ```bash
   cloudctl login -a &amp;TWBLT;cluster-url&gt; -u &amp;TWBLT;cluster-admin-user&gt; -p &amp;TWBLT;cluster-admin-password&gt; -n &amp;TWBLT;namespace&gt; --skip-ssl-validation
   ```
   {: codeblock}

2. Configure as variáveis de ambiente a seguir:

   ```bash
   export CLUSTER_URL=https://$(oc get cm management-ingress-ibmcloud-cluster-info -o jsonpath='{.data.cluster_ca_domain}')    oc --insecure-skip-tls-verify=true -n kube-public get secret ibmcloud-cluster-ca-cert -o jsonpath="{.data.ca\.crt}" | base64 --decode &gt; ieam.crt    export HZN_MGMT_HUB_CERT_PATH="$PWD/ieam.crt"    export HZN_FSS_CSSURL=${CLUSTER_URL}/edge-css
   ```
   {: codeblock}

   Defina as variáveis de ambiente de autenticação do Docker a seguir, fornecendo sua própria **ENTITLEMENT_KEY**:
   ```
   export REGISTRY_USERNAME=cp    export REGISTRY_PASSWORD=<ENTITLEMENT_KEY>
   ```
   {: codeblock}

   **Nota:** obtenha sua chave de autorização por meio do [My IBM Key](https://myibm.ibm.com/products-services/containerlibrary).

3. Mova para o diretório **agent** em que **edge-packages-{{site.data.keyword.semver}}.tar.gz** é:

   ```bash
   cd agent
   ```
   {: codeblock}

4. Existem duas maneiras preferenciais de reunir os arquivos para a instalação do nó de borda usando o script **edgeNodeFiles.sh**. Escolha um dos métodos a seguir com base em suas necessidades:

   * Execute o script **edgeNodeFiles.sh** para reunir os arquivos necessários e colocá-los no componente CSS Cloud Sync Service (CSS) do Model Management System (MMS).

     **Nota**: o **script edgeNodeFiles.sh** foi instalado como parte do pacote horizon-cli e deve estar em seu caminho.

     ```bash
     HZN_EXCHANGE_USER_AUTH='' edgeNodeFiles.sh ALL -c -p edge-packages-{{site.data.keyword.semver}} -r cp.icr.io/cp/ieam
     ```
     {: codeblock}

     Em cada nó de borda, use o sinalizador **-i 'css:'** do **agent-install.sh** para obter os arquivos necessários do CSS.

     **Nota**: caso pretenda usar [dispositivos de borda ativados por SDO](../installing/sdo.md), deve-se executar esta forma do comando `edgeNodeFiles.sh`.

   * Como alternativa, use **edgeNodeFiles.sh** para empacotar os arquivos em um arquivo tar:

     ```bash
     edgeNodeFiles.sh ALL -t -p edge-packages-{{site.data.keyword.semver}} -r cp.icr.io/cp/ieam
     ```
     {: codeblock}

     Copie o arquivo tar para cada nó de borda e use o sinalizador **-z** do **agent-install.sh** para obter os arquivos necessários do arquivo tar.

     Se você ainda não instalou o pacote **horizon-cli** neste host, faça isso agora. Consulte [Configuração de pós-instalação](post_install.md#postconfig) para obter um exemplo desse processo.

     Localize os scripts **agent-install.sh** e **agent-uninstall.sh** que foram instalados como parte do pacote **horizon-cli**.    Esses scripts são necessários em cada nó de borda durante a configuração (atualmente **agent-uninstall.sh** suporta apenas clusters de borda):
    * {{site.data.keyword.linux_notm}} exemplo:

     ```
     ls /usr/horizon/bin/agent-{install,uninstall}.sh
     ```
     {: codeblock}

    * Exemplo do macOS:

     ```
     ls /usr/local/bin/agent-{install,uninstall}.sh
     ```
     {: codeblock}

**Nota**: o **edgeNodeFiles.sh** possui mais sinalizações para controlar quais arquivos serão reunidos e onde eles devem ser colocados. Para ver todos os sinalizadores disponíveis, execute: **edgeNodeFiles.sh -h**

## O que vem depois

Antes da configuração dos nós de borda, você ou os técnicos de nó devem criar uma chave de API e reunir outros valores da variável de ambiente. Siga as etapas em [Criando sua chave de API](prepare_for_edge_nodes.md).
