---

copyright:
years: 2021
lastupdated: "2021-03-23"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Upgrades
{: #hub_upgrade_overview}

## Resumo do upgrade
{: #sum}
* A versão atual do {{site.data.keyword.ieam}} Management Hub é {{site.data.keyword.semver}}.
* {{site.data.keyword.ieam}} {{site.data.keyword.semver}} é suportado no {{site.data.keyword.ocp}} versão 4.6.

Upgrades no mesmo canal do Operator Lifecycle Manager (OLM) para o Hub de Gerenciamento do {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) e [IBM Cloud Platform Common Services](https://www.ibm.com/docs/en/cpfs) ocorrem automaticamente por meio do OLM que vem pré-instalado em seu Cluster {{site.data.keyword.open_shift_cp}} ({{site.data.keyword.ocp}}).

Os canais do {{site.data.keyword.ieam}} são definidos por **versão secundária** (por exemplo v4.2 e v4.3) e atualizarão automaticamente somente as **versões de correção** (por exemplo 4.2.x). Para upgrades da **versão secundária**, deve-se alterar manualmente os canais para iniciar o upgrade. A fim de iniciar um upgrade da **versão secundária**, deve-se estar na mais recente **versão de correção** disponível da **versão secundária** anterior, então a mudança de canais irá iniciar o upgrade.

** Notas: **
* Fazer downgrade não é suportado
* Fazer upgrade do {{site.data.keyword.ieam}} 4.1.x para 4.2.x não é suportado
* Devido a um [problema conhecido do {{site.data.keyword.ocp}}](https://access.redhat.com/solutions/5493011), se você tiver quaisquer `InstallPlans` em seu projeto configurados para Aprovação Manual, então todos os outros `InstallPlans` nesse projeto também têm. Deve-se aprovar manualmente o upgrade do Operador para prosseguir.

### Fazendo upgrade do hub de gerenciamento do {{site.data.keyword.ieam}} da versão 4.2.x para 4.3.x

1. Faça um backup antes de fazer upgrade. Para obter mais informações, consulte [Backup e recuperação](../admin/backup_recovery.md).
2. Navegue até o console da web do {{site.data.keyword.ocp}} para o seu cluster.
3. Navegue até **Operadores** -&gt; **Operadores Instalados**.
4. Procure por **{{site.data.keyword.ieam}}** e clique no resultado do **Hub de gerenciamento do {{site.data.keyword.ieam}}**.
5. Navegue até a guia **Assinatura**.
6. Clique no link **v4.2** na seção **Canal**.
7. Clique no botão de opções para alternar o seu canal ativo para **v4.3** para iniciar o upgrade.

Para verificar se o upgrade está concluído, consulte as [etapas de 1 até 5 na seção pós-instalação de verificação de instalação](post_install.md).

Para atualizar os serviços de exemplo, consulte as [etapas de 1 até 3 na seção de configuração de pós-instalação](post_install.md).

## Fazendo upgrade de nós de borda

Os nós existentes do {{site.data.keyword.ieam}} não são submetidos a upgrade automaticamente. A versão do agente do {{site.data.keyword.ieam}} 4.2.1 (2.28.0-338) é suportada com um hub de gerenciamento do {{site.data.keyword.ieam}} {{site.data.keyword.semver}}. A fim de fazer upgrade do agente do {{site.data.keyword.edge_notm}} em seus dispositivos de borda e clusters de borda, primeiro é necessário colocar os arquivos de nó de borda do {{site.data.keyword.semver}} no Cloud Sync Service (CSS).

Execute as etapas de 1 até 3 sob **Instalando a CLI mais recente para o seu ambiente** mesmo se você não deseja fazer upgrade de seus nós de borda neste momento. Isso garante que novos nós de borda serão instalados com o mais recente código do agente do {{site.data.keyword.ieam}} {{site.data.keyword.semver}}.

### Instalando a CLI mais recente para o seu ambiente
1. Efetue login, receba e extraia o pacote configurável do agente com a sua chave de autorização por meio do [Registro Autorizado](https://myibm.ibm.com/products-services/containerlibrary):
    ```
    docker login cp.icr.io --username cp &amp;TWBAMP;&amp;TWBAMP; \ docker rm -f ibm-eam-{{site.data.keyword.semver}}-bundle; \ docker create --name ibm-eam-{{site.data.keyword.semver}}-bundle cp.icr.io/cp/ieam/ibm-eam-bundle:{{site.data.keyword.anax_ver}} bash &amp;TWBAMP;&amp;TWBAMP; \ docker cp ibm-eam-{{site.data.keyword.semver}}-bundle:/ibm-eam-{{site.data.keyword.semver}}-bundle.tar.gz ibm-eam-{{site.data.keyword.semver}}-bundle.tar.gz &amp;TWBAMP;&amp;TWBAMP; \ tar -zxvf ibm-eam-{{site.data.keyword.semver}}-bundle.tar.gz
    ```
    {: codeblock}
2. Instale a CLI do **hzn** usando as instruções para a sua plataforma suportada:
  * Navegue até o diretório **agente** e descompacte os arquivos do agente:
    ```
    cd ibm-eam-{{site.data.keyword.semver}}-bundle/agent &amp;TWBAMP;&amp;TWBAMP; \     tar -zxvf edge-packages-{{site.data.keyword.semver}}.tar.gz
    ```
    {: codeblock}

    * Exemplo de {{site.data.keyword.linux_notm}} do Debian:
      ```
      sudo apt-get install ./edge-packages-{{site.data.keyword.semver}}/linux/deb/amd64/horizon-cli*.deb
      ```
      {: codeblock}

    * Exemplo de {{site.data.keyword.linux_notm}} do Red Hat:
      ```
      sudo dnf install -yq ./edge-packages-{{site.data.keyword.semver}}/linux/rpm/x86_64/horizon-cli-*.x86_64.rpm
      ```
      {: codeblock}

    * Exemplo do macOS:
      ```
      sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain edge-packages-{{site.data.keyword.semver}}/macos/pkg/x86_64/horizon-cli.crt && \       sudo installer -pkg edge-packages-{{site.data.keyword.semver}}/macos/pkg/x86_64/horizon-cli-*.pkg -target /
      ```
      {: codeblock}
3. Siga as etapas em [Reunir arquivos do nó de borda](../hub/gather_files.md) para enviar os arquivos de instalação do agente para o CSS.

### Fazendo upgrade do agente em nós de borda
1. Efetue login em seu nó de borda como **raiz** em um dispositivo, ou como um **administrador** em seu cluster e configure as variáveis de ambiente do horizon:
```bash
export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>   export HZN_ORG_ID=<your-exchange-organization>   export HZN_FSS_CSSURL=https://<ieam-management-hub-ingress>/edge-css/
```
{: codeblock}

2. Configure as variáveis de ambiente necessárias com base no seu tipo de cluster (pule esta etapa se você estiver fazendo upgrade de um dispositivo):

  * **Nos clusters de borda do OCP:**
  
    Configure a classe de armazenamento que o agente deve usar:
    
    ```bash
    oc get storageclass    export EDGE_CLUSTER_STORAGE_CLASS=<rook-ceph-cephfs-internal>
    ```
    {: codeblock}

    Configure o nome do usuário de registro para o nome da conta do serviço que você criou:
    ```bash     oc get serviceaccount -n openhorizon-agent     export EDGE_CLUSTER_REGISTRY_USERNAME=<service-account-name>
    ```
    {: codeblock}

    Configure o token de registro: 
    ```bash     export EDGE_CLUSTER_REGISTRY_TOKEN=`oc serviceaccounts get-token $EDGE_CLUSTER_REGISTRY_USERNAME`
    ```
    {: codeblock}

  * **No k3s:**
  
    Instrua o **agent-install.sh** a usar a classe de armazenamento padrão:
    
    ```bash
    export EDGE_CLUSTER_STORAGE_CLASS=local-path
    ```
    {: codeblock}

  * **No microk8s:**
  
    Instrua o **agent-install.sh** a usar a classe de armazenamento padrão:
    
    ```bash
    export EDGE_CLUSTER_STORAGE_CLASS=microk8s-hostpath
    ```
    {: codeblock}

3. Extraia o **agent-install.sh** do CSS:
```bash
curl -u $HZN_ORG_ID/$HZN_EXCHANGE_USER_AUTH $HZN_FSS_CSSURL/api/v1/objects/IBM/agent_files/agent-install.sh/data -o agent-install.sh --insecure && chmod +x agent-install.sh
```
{: codeblock}

4. Execute **agent-install.sh** para obter os arquivos atualizados do CSS e configure o agente do Horizon:
  *  **Nos dispositivos de borda:**
    ```bash     sudo -s -E ./agent-install.sh -i 'css:' -s
    ```
    {: codeblock}

  *  **Nos clusters de borda:**
    ```bash     ./agent-install.sh -D cluster -i 'css:' -s
    ```
    {: codeblock}

**Nota**: inclua a opção -s enquanto executa a instalação do agente para ignorar o registro, o que deixa o nó de borda no mesmo estado em que ele estava antes do upgrade.

## Problemas conhecidos e Perguntas Frequentes
{: #FAQ}

### {{site.data.keyword.ieam}} 4.2
* Há um problema conhecido com o banco de dados mongo cssdb local do {{site.data.keyword.ieam}} 4.2.0, que resulta em perda de dados quando o pod é reprogramado. Se você estiver usando bancos de dados locais (padrão), permita que o {{site.data.keyword.ieam}} {{site.data.keyword.semver}} faça o upgrade para concluir antes de atualizar o seu cluster do {{site.data.keyword.ocp}} para 4.6. Para obter mais detalhes, consulte a página de [problemas conhecidos](../getting_started/known_issues.md).

* Não fiz upgrade do meu cluster do {{site.data.keyword.ocp}} anterior à versão 4.4 e o upgrade automático parece estar paralisado.

  * Siga estas etapas para resolver o problema:
  
    1) Faça um backup do atual conteúdo do {{site.data.keyword.ieam}} Management Hub.  É possível localizar a documentação de backup aqui: [Backup e recuperação de dados](../admin/backup_recovery.md).
    
    2) Faça upgrade do cluster do {{site.data.keyword.ocp}} para a versão 4.6.
    
    3) Devido a um problema conhecido com o banco de dados mongo **cssdb** local do {{site.data.keyword.ieam}} 4.2.0, o upgrade na **etapa 2** irá reinicializar o banco de dados.
    
      * Se você tiver aproveitado os recursos de MMS do {{site.data.keyword.ieam}} e estiver preocupado com a perda de dados, use o backup feito na **etapa 1** e siga o **Procedimento de restauração** na página [Backup e recuperação de dados](../admin/backup_recovery.md). (**Nota:** o procedimento de restauração resultará em tempo de inatividade.)
      
      * Como alternativa, execute o seguinte para desinstalar e reinstalar o operador {{site.data.keyword.ieam}} se você não tiver aproveitado os recursos de MMS, não estiver preocupado com a perda de dados de MMS ou estiver usando bancos de dados remotos:
      
        1) Navegue para a página Operadores instalados do cluster do {{site.data.keyword.ocp}}.
        
        2) Localize o operador IEAM Management Hub e abra sua página.
        
        3) No menu Ações à esquerda, escolha desinstalar o operador.
        
        4) Navegue para a página OperatorHub e reinstale o operador IEAM Management Hub.

* O {{site.data.keyword.ocp}} versão 4.5 é suportado?

  * O {{site.data.keyword.ieam}} Management Hub não é testado nem suportado no {{site.data.keyword.ocp}} versão 4.5.  Sugerimos que seja feito upgrade para o {{site.data.keyword.ocp}} versão 4.6.

* Existe alguma maneira de cancelar esta versão do {{site.data.keyword.ieam}} Management Hub?

  * O {{site.data.keyword.ieam}} Management Hub versão 4.2.0 não será mais suportado na liberação da versão {{site.data.keyword.semver}}.
