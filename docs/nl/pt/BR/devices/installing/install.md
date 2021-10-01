---

copyright:
  years: 2020
lastupdated: "2020-04-9"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Instalando o hub de gerenciamento
{: #hub_install_overview}
 
Antes de executar as tarefas do nó do {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}), deve-se instalar e configurar um hub de gerenciamento.

O {{site.data.keyword.ieam}} fornece recursos de computação de borda que o ajudam a gerenciar e implementar cargas de trabalho de um cluster de hub em instâncias remotas do OpenShift® Container Platform 4.2 ou outros clusters baseados em Kubernetes.

O {{site.data.keyword.ieam}} usa o IBM Multicloud Management Core 1.2 para controlar a implementação de cargas de trabalho conteinerizadas nos servidores de borda, gateways e dispositivos que são hospedados por clusters OpenShift® Container Platform 4.2 em locais remotos.

Adicionalmente, o {{site.data.keyword.ieam}} inclui suporte para um perfil de gerenciador de computação de borda. Esse perfil suportado pode ajudar a reduzir o uso de recursos do OpenShift® Container Platform 4.2 quando o OpenShift® Container Platform 4.2 é instalado para ser usado como host para um servidor de borda remoto. Esse perfil coloca nele os serviços mínimos necessários para suportar o gerenciamento remoto robusto desses ambientes de servidor e os aplicativos corporativos críticos que você está hospedando. Com esse perfil, você ainda é capaz de autenticar usuários, coletar dados de log e de evento e implementar cargas de trabalho em um único nó do trabalhador ou em um conjunto de clusters.

# Instalando o hub de gerenciamento

O processo de instalação do {{site.data.keyword.edge_notm}} orienta você nas seguintes etapas de instalação e configuração de alto nível:
{:shortdesc}

  - [Resumo de instalação](#sum)
  - [Dimensionando](#size)
  - [Pré-requisitos](#prereq)
  - [Processo de instalação](#process)
  - [Configuração de pós-instalação](#postconfig)
  - [Reunir as informações e os arquivos necessários](#prereq_horizon)
  - [Desinstalando
](#uninstall)

## Resumo da instalação
{: #sum}

* Implemente os componentes do hub de gerenciamento a seguir:
  * API do Exchange {{site.data.keyword.edge_devices_notm}}.
  * Robô de contrato do {{site.data.keyword.edge_devices_notm}}.
  * {{site.data.keyword.edge_devices_notm}} Cloud Sync Service (CSS).
  * Interface com o usuário do {{site.data.keyword.edge_devices_notm}}.
* Verifique se a instalação foi bem-sucedida.
* Preencha os serviços de borda de amostra.

## Dimensionando
{: #size}

As informações de dimensionamento destinam-se apenas a serviços do {{site.data.keyword.edge_notm}} e vão além das recomendações de dimensionamento para o {{site.data.keyword.edge_shared_notm}}, que estão [documentadas aqui](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/servers/cluster_sizing.html).

### Requisitos de armazenamento de banco de dados

* PostgreSQL Exchange
  * 10 GB padrão
* PostgreSQL AgBot
  * 10 GB padrão  
* MongoDB Cloud Sync Service
  * 50 GB padrão

### Requisitos de cálculo

Os serviços que usam [recursos de cálculo do Kubernetes](https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container) serão planejados nos nós de trabalhador disponíveis. São recomendados pelo menos três nós do trabalhador.

* Essas mudanças na configuração suportarão até 10.000 dispositivos de borda:

  ```
  exchange:
    replicaCount: 5
    dbPool: 18
    cache:
      idsMaxSize: 11000
    resources:
      limits:
        cpu: 5
  ```

  Nota: as instruções para fazer essas mudanças são descritas na seção **Configuração avançada** no [README.md](README.md).

* A configuração padrão suporta até 4.000 dispositivos de borda e os totais de gráficos para recursos de cálculo padrão são:

  * Pedidos
     * Menos de 5 GB de RAM
     * Menos de uma CPU
  * Limites
     * 18 GB de RAM
     * 18 CPUs


## Pré-requisitos
{: #prereq}

* Instale o [{{site.data.keyword.edge_shared_notm}}](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/servers/install_edge.html)
* **Um host macOS ou Ubuntu do {{site.data.keyword.linux_notm}}**
* [CLI do cliente OpenShift (oc) 4,2 ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest-4.2/)
* [Download de **jq** ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://stedolan.github.io/jq/download/)
* **git**
* **docker** 1.13+
* **Fazer**
* As CLIs a seguir podem ser obtidas a partir de sua instalação do cluster do {{site.data.keyword.mgmt_hub}} em `https://<CLUSTER_URL_HOST>/common-nav/cli`

    Nota: pode ser necessário navegar para a URL acima duas vezes porque o acesso não autenticado redireciona a navegação para uma página de boas-vindas

  * CLI do Kubernetes (**kubectl**)
  * CLI do Helm (**helm**)
  * CLI do IBM Cloud Pak (**cloudctl**)

Nota: por padrão, os bancos de dados de desenvolvimento local são provisionados como parte da instalação do gráfico. Consulte o [README.md](README.md) para obter orientação sobre como fornecer seus próprios bancos de dados. Você é responsável pelo backup e a restauração de seus bancos de dados.

## Processo de instalação
{: #process}

1. Configure a variável de ambiente **CLUSTER_URL**, cujo valor pode ser obtido a partir da saída da instalação do {{site.data.keyword.mgmt_hub}}:

    ```
    export CLUSTER_URL=<CLUSTER_URL>
    ```
    {: codeblock}

    Como alternativa, depois de se conectar ao cluster com **oc login**, é possível executar:

    ```
    export CLUSTER_URL=https://$(oc get routes icp-console -o jsonpath='{.spec.host}' -n kube-system)
    ```
    {: codeblock}

2. Conecte-se ao cluster com privilégios de administrador de cluster, selecionando **kube-system** como o namespace e **preencha a senha** que foi definida em config.yaml durante a instalação do {{site.data.keyword.mgmt_hub}}:

    ```
    cloudctl login -a $CLUSTER_URL -u admin -p <your-icp-admin-password> -n kube-system --skip-ssl-validation
    ```
    {: codeblock}

3. Defina o host de registro de imagem e configure a CLI do Docker para confiar no certificado autoassinado:

    ```
    export REGISTRY_HOST=$(oc get routes -n openshift-image-registry default-route -o jsonpath='{.spec.host}')

    ```
    {: codeblock}

   Para macOS:

      1. Confiar no certificado

      ```
      mkdir -p ~/.docker/certs.d/$REGISTRY_HOST && \
      echo | openssl s_client -showcerts -connect $REGISTRY_HOST:443 2>/dev/null | openssl x509 -outform PEM > ~/.docker/certs.d/$REGISTRY_HOST/ca.crt && \
      sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain ~/.docker/certs.d/$REGISTRY_HOST/ca.crt

      ```
      {: codeblock}
      
      2. Reinicie o serviço do Docker a partir da barra de menus

   Para Ubuntu:

      1. Confiar no certificado

      ```
      mkdir /etc/docker/certs.d/$REGISTRY_HOST && \
      echo | openssl s_client -showcerts -connect $REGISTRY_HOST:443 2>/dev/null | openssl x509 -outform PEM > /etc/docker/certs.d/$REGISTRY_HOST/ca.crt && \
      service docker restart

      ```
      {: codeblock}

4. Efetue login no registro de imagem do {{site.data.keyword.open_shift_cp}}:

      ```
      docker login $REGISTRY_HOST -u $(oc whoami) -p $(oc whoami -t)
      ```
      {: codeblock}

5. Descompacte o arquivo compactado de instalação do {{site.data.keyword.edge_devices_notm}} que foi transferido por download do IBM Passport Advantage:

    ```
    tar -zxvf ibm-ecm-4.1.0-x86_64.tar.gz && \
    cd ibm-ecm-4.1.0-x86_64
    ```
    {: codeblock}

6. Carregue o conteúdo do archive no catálogo e as imagens no namespace ibmcom do registro:

    ```
    cloudctl catalog load-archive --archive ibm-ecm-prod-catalog-archive-4.1.0.tgz --registry $REGISTRY_HOST/ibmcom
    ```
    {: codeblock}

  Nota: o {{site.data.keyword.edge_devices_notm}} suporta apenas uma instalação orientada pela CLI; a instalação a partir do catálogo não é suportada para esta liberação.

7. Extraia o conteúdo do arquivo compactado do gráfico para o diretório atual e mova-o para o diretório criado:

    ```
    tar -O -zxvf ibm-ecm-prod-catalog-archive-4.1.0.tgz charts/ibm-ecm-prod-4.1.0.tgz | tar -zxvf - && \
    cd ibm-ecm-prod
    ```
    {: codeblock}

8. Defina uma classe de armazenamento padrão, caso não haja uma configurada:

   ```
   # oc get storageclass
   NAME                                 PROVISIONER                     AGE
   rook-ceph-block-internal             rook-ceph.rbd.csi.ceph.com      8h
   rook-ceph-cephfs-internal (default)  rook-ceph.cephfs.csi.ceph.com   8h
   rook-ceph-delete-bucket-internal     ceph.rook.io/bucket             8h
   ```
   
   Se não vir uma linha com a sequência **(default)** acima, marque seu armazenamento preferencial com:

   ```
   oc patch storageclass <PREFERRED_DEFAULT_STORAGE_CLASS_NAME> -p '{"metadata": {"annotations": {"storageclass.kubernetes.io/is-default-class": "true"}}}'
   ```
   {: codeblock}

9. Leia e considere suas opções de configuração, em seguida, siga a seção **Instalando o gráfico** no [README.md](README.md).

  O script instala os componentes do hub de gerenciamento mencionados na seção **Resumo da instalação** acima, executa a verificação de instalação e, em seguida, retorna para a seção **Configuração de pós-instalação** abaixo.

## Configuração de pós-instalação
{: #postconfig}

Execute os comandos a seguir no mesmo host no qual você executou a instalação inicial:

1. Consulte as etapas 1 e 2 na seção **Processo de instalação** acima para efetuar login no cluster
2. Instale a CLI **hzn** com os instaladores de pacotes do Ubuntu {{site.data.keyword.linux_notm}} ou macOS que são localizados em **horizon-edge-packages** no diretório OS/ARCH apropriado do conteúdo compactado extraído na etapa 5 do [Processo de instalação](#process) acima:
  * Exemplo do Ubuntu {{site.data.keyword.linux_notm}}:

    ```
    sudo dpkg -i horizon-edge-packages/linux/ubuntu/bionic/amd64/horizon-cli*.deb
    ```
    {: codeblock}

  * Exemplo do macOS:

    ```
    sudo installer -pkg horizon-edge-packages/macos/horizon-cli-*.pkg -target /
    ```
    {: codeblock}

3. Exporte as variáveis a seguir que são necessárias para as próximas etapas:

    ```
    export EXCHANGE_ROOT_PASS=$(oc -n kube-system get secret edge-computing -o jsonpath="{.data.exchange-config}" | base64 --decode | jq -r .api.root.password)
    export HZN_EXCHANGE_URL=https://$(oc get routes icp-console -o jsonpath='{.spec.host}' -n kube-system)/ec-exchange/v1
    export HZN_EXCHANGE_USER_AUTH="root/root:$EXCHANGE_ROOT_PASS"
    export HZN_ORG_ID=IBM
    ```
    {: codeblock}

4. Confie na Autoridade de certificação do {{site.data.keyword.open_shift_cp}}:
    ```
    oc --namespace kube-system get secret cluster-ca-cert -o jsonpath="{.data['tls\.crt']}" | base64 --decode > /tmp/icp-ca.crt
    ```
    {: codeblock}

  * Exemplo do Ubuntu {{site.data.keyword.linux_notm}}:
     ```
     sudo cp /tmp/icp-ca.crt /usr/local/share/ca-certificates &&sudo update-ca-certificates
     ```
    {: codeblock}

  * Exemplo do macOS:

    ```
    sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain /tmp/icp-ca.crt
    ```
    {: codeblock}

5. Para criar um par de chaves de assinatura. Para obter mais informações, consulte a Etapa 5 em [Preparando para criar um serviço de borda](../developing/service_containers.md).
    ```
    hzn key create <company-name> <owner@email>
    ```
    {: codeblock}

6. Para confirmar se a configuração pode ser comunicar com a API do {{site.data.keyword.edge_devices_notm}} Exchange:
    ```
    hzn exchange status
    ```
    {: codeblock}

7. Preencha os serviços de borda de amostra:

    ```
    curl https://raw.githubusercontent.com/open-horizon/examples/v4.1/tools/exchangePublishScript.sh | bash -s -- -c $(oc get -n kube-public configmap -o jsonpath="{.items[]..data.cluster_name}")
    ```
    {: codeblock}

8. Execute os comandos a seguir para visualizar alguns dos serviços e políticas que foram criados no {{site.data.keyword.edge_devices_notm}} Exchange:

    ```
    hzn exchange service list IBM/
    hzn exchange pattern list IBM/
    hzn exchange service listpolicy
    ```
    {: codeblock}

9. Se ainda não estiver configurada, crie uma conexão LDAP usando o console de gerenciamento do {{site.data.keyword.open_shift_cp}}. Depois de estabelecer uma conexão LDAP, crie uma equipe, conceda a essa equipe acesso a qualquer namespace e inclua usuários nessa equipe. Isso concede aos usuários individuais a permissão para criar chaves de API.

  Nota: as chaves de API são usadas para autenticação com a CLI do {{site.data.keyword.edge_devices_notm}}. Para obter mais informações sobre LDAP, consulte [Configurando a conexão LDAP ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://www.ibm.com/support/knowledgecenter/SSFC4F_1.2.0/iam/3.4.0/configure_ldap.html).


## Reúna as informações e arquivos necessários para dispositivos de borda
{: #prereq_horizon}

Serão necessários vários arquivos para instalar o agente do {{site.data.keyword.edge_devices_notm}} nos dispositivos de borda e registrá-los no {{site.data.keyword.edge_devices_notm}}. Esta seção fornece orientação sobre como reunir esses arquivos em um arquivo tar, que pode, então, ser usado em cada um dos dispositivos de borda.

Supõe-se que os comandos **cloudctl** e **kubectl** já tenham sido instalados e você já tenha extraído **ibm-edge-computing-4.1.0-x86_64.tar.gz** do conteúdo da instalação, conforme descrito anteriormente nesta página.

1. Consulte as etapas 1 e 2 na seção **Processo de instalação** acima para configurar as variáveis de ambiente a seguir:

   ```
   export CLUSTER_URL=<cluster-url>
   export CLUSTER_USER=<your-icp-admin-user>
   export CLUSTER_PW=<your-icp-admin-password>
   ```
   {: codeblock}

2. Faça download da versão mais recente de **edgeDeviceFiles.sh**:

   ```
   curl -O https://raw.githubusercontent.com/open-horizon/examples/v4.0/tools/edgeDeviceFiles.sh
   chmod +x edgeDeviceFiles.sh
   ```
   {: codeblock}

3. Execute o script **edgeDeviceFiles.sh** para reunir os arquivos necessários:

   ```
   ./edgeDeviceFiles.sh <edge-device-type> -t
   ```
   {: codeblock}

   Argumentos de comando:
   * Valores de **<edge-device-type>** suportados: **32-bit-ARM** , **64-bit-ARM**, **x86_64-{{site.data.keyword.linux_notm}}** ou **{{site.data.keyword.macOS_notm}}**
   * **-t**: criar um arquivo **agentInstallFiles-&lt;edge-device-type&gt;.tar.gz** contendo todos os arquivos reunidos. Se essa sinalização não for configurada, os arquivos reunidos serão colocados no diretório atual.
   * **-k**: criar uma nova chave de API, chamada **$USER-Edge-Device-API-Key**. Se essa sinalização não for configurada, haverá uma verificação das chaves de API atuais, em busca de uma chamada **$USER-Edge-Device-API-Key** e, se a chave já existir, a criação será ignorada.
   * **-d** **<distribution>**: ao instalar no **64-bit-ARM** ou **x86_64-Linux**, é possível especificar **-d xenial** para a versão mais antiga do Ubuntu, em vez do biônico padrão. Ao instalar em **32-bit-ARM**, é possível especificar **-d strecth** em vez do buster padrão. A sinalização -d é ignorada com o macOS.
   * **-f** **<directory>**: especificar um diretório para o qual mover os arquivos reunidos. Se o diretório não existir, ele será criado. O padrão é o diretório atual

4. O comando na etapa anterior criará um arquivo chamado **agentInstallFiles-&lt;edge-device-type&gt;.tar.gz**. Caso tenha tipos de dispositivos de borda adicionais (arquiteturas diferentes), repita a etapa anterior para cada tipo.

5. Anote a chave de API que foi criada e exibida pelo comando **edgeDeviceFiles.sh**.

6. Agora que você efetuou login por meio de **cloudctl**, caso seja necessário criar chaves de API adicionais a serem usadas pelo usuário junto com o comando **hzn** do {{site.data.keyword.horizon}}:

   ```
   cloudctl iam api-key-create "<choose-an-api-key-name>" -d "<choose-an-api-key-description>"
   ```
   {: codeblock}

   Na saída do comando, procure o valor da chave na linha que começa com **Chave de API** e salve o valor da chave para uso futuro.

7. Quando estiver pronto para configurar dispositivos de borda, siga [Introdução ao uso do {{site.data.keyword.edge_devices_notm}}](../getting_started/getting_started.md).

## Desinstalação
{: #uninstall}

Nota: por padrão, os **bancos de dados locais** são configurados, em que, neste caso, a desinstalação exclui TODOS os dados persistentes. Assegure-se de ter feito backups de todos os dados persistentes necessários (as instruções de backup estão documentadas no LEIA-MEE) antes de executar o script de desinstalação. Se você tiver configurado **bancos de dados remotos**, esses dados não serão excluídos durante uma desinstalação e deverão ser removidos manualmente, se necessário.

Volte para o local em que o gráfico foi descompactado como parte da instalação e execute o script de desinstalação fornecido. Esse script desinstalará a liberação do Helm e todos os recursos associados. Primeiro, use **cloudctl** para efetuar login no cluster como um administrador de cluster e, em seguida, execute:

```
ibm_cloud_pak/pak_extensions/uninstall/uninstall-edge-computing.sh <cluster-name>
```
{: codeblock}
