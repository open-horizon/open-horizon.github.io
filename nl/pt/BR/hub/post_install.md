---

copyright:
years: 2020
lastupdated: "2020-10-28"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Configuração de pós-instalação

## Pré-requisito

* [CLI do IBM Cloud Pak (**cloudctl**) e CLI do cliente OpenShift (**oc**)](../cli/cloudctl_oc_cli.md)
* [**jq**](https://stedolan.github.io/jq/download/)
* [**git**](https://git-scm.com/downloads)
* [**docker**](https://docs.docker.com/get-docker/) versão 1.13 ou superior
* **Fazer**

## Verificação de Instalação

1. Conclua as etapas em [Instalar o {{site.data.keyword.ieam}}](online_installation.md)
2. Assegure-se de que todos os pods no namespace do {{site.data.keyword.ieam}} estejam **Em execução** ou **Concluídos**:

   ```
   oc get pods
   ```
   {: codeblock}

   Este é um exemplo do que deve ser visto com bancos de dados locais e o gerenciador de segredos local instalado. Alguns reinícios de inicialização são esperados, mas vários reinícios geralmente indicam um problema:
   ```
   $ oc get pods NAME READY STATUS RESTARTS AGE create-agbotdb-cluster-j4fnb 0/1 Completed 0 88m create-exchangedb-cluster-hzlxm 0/1 Completed 0 88m ibm-common-service-operator-68b46458dc-nv2mn 1/1 Running 0 103m ibm-eamhub-controller-manager-7bf99c5fc8-7xdts 1/1 Running 0 103m ibm-edge-agbot-5546dfd7f4-4prgr 1/1 Running 0 81m ibm-edge-agbot-5546dfd7f4-sck6h 1/1 Running 0 81m ibm-edge-agbotdb-keeper-0 1/1 Running 0 88m ibm-edge-agbotdb-keeper-1 1/1 Running 0 87m ibm-edge-agbotdb-keeper-2 1/1 Running 0 86m ibm-edge-agbotdb-proxy-7447f6658f-7wvdh 1/1 Running 0 88m ibm-edge-agbotdb-proxy-7447f6658f-8r56d 1/1 Running 0 88m ibm-edge-agbotdb-proxy-7447f6658f-g4hls 1/1 Running 0 88m ibm-edge-agbotdb-sentinel-5766f666f4-5qm9x 1/1 Running 0 88m ibm-edge-agbotdb-sentinel-5766f666f4-5whgr 1/1 Running 0 88m ibm-edge-agbotdb-sentinel-5766f666f4-9xjpr 1/1 Running 0 88m ibm-edge-css-5c59c9d6b6-kqfnn 1/1 Running 0 81m ibm-edge-css-5c59c9d6b6-sp84w 1/1 Running 0 81m
   ibm-edge-css-5c59c9d6b6-wf84s                  1/1     Running     0          81m    ibm-edge-cssdb-server-0                        1/1     Running     0          88m    ibm-edge-exchange-b6647db8d-k97r8              1/1     Running     0          81m    ibm-edge-exchange-b6647db8d-kkcvs              1/1     Running     0          81m    ibm-edge-exchange-b6647db8d-q5ttc              1/1     Running     0          81m    ibm-edge-exchangedb-keeper-0                   1/1     Running     1          88m    ibm-edge-exchangedb-keeper-1                   1/1     Running     0          85m    ibm-edge-exchangedb-keeper-2                   1/1     Running     0          84m    ibm-edge-exchangedb-proxy-6bbd5b485-cx2v8      1/1     Running     0          88m    ibm-edge-exchangedb-proxy-6bbd5b485-hs27d      1/1     Running     0          88m    ibm-edge-exchangedb-proxy-6bbd5b485-htldr      1/1     Running     0          88m    ibm-edge-exchangedb-sentinel-6d685bf96-hz59z   1/1     Running     1          88m    ibm-edge-exchangedb-sentinel-6d685bf96-m4bdh   1/1     Running     0          88m    ibm-edge-exchangedb-sentinel-6d685bf96-mxv2b   1/1     Running     1          88m    ibm-edge-sdo-0                                 1/1     Running     0          81m    ibm-edge-ui-545d694f6c-4rnrf                   1/1     Running     0          81m    ibm-edge-ui-545d694f6c-97ptz                   1/1     Running     0          81m    ibm-edge-ui-545d694f6c-f7bf6                   1/1     Running     0          81m
   ibm-edge-vault-0 1/1 Running 0 81m ibm-edge-vault-bootstrap-k8km9 0/1 Completed 0 80m
   ```
   {: codeblock}

   **Notas**:
   * Para obter mais informações sobre quaisquer pods no estado **Pendente** devido a problemas de recurso ou de planejamento, consulte a página [dimensionamento de cluster](cluster_sizing.md). Isso inclui informações sobre como reduzir custos de planejamento de componentes.
   * Para obter mais informações sobre quaisquer outros erros, consulte [resolução de problemas](../admin/troubleshooting.md).
3. Assegure-se de que todos os pods no namespace **ibm-common-services** estejam **Em execução** ou **Concluídos**:

   ```
   oc get pods -n ibm-common-services
   ```
   {: codeblock}

4. Efetue login, receba e extraia o pacote configurável do agente com a sua chave de autorização por meio do [Registro Autorizado](https://myibm.ibm.com/products-services/containerlibrary):
    ```
    docker login cp.icr.io --username cp &amp;TWBAMP;&amp;TWBAMP; \ docker rm -f ibm-eam-{{site.data.keyword.semver}}-bundle; \ docker create --name ibm-eam-{{site.data.keyword.semver}}-bundle cp.icr.io/cp/ieam/ibm-eam-bundle:{{site.data.keyword.anax_ver}} bash &amp;TWBAMP;&amp;TWBAMP; \ docker cp ibm-eam-{{site.data.keyword.semver}}-bundle:/ibm-eam-{{site.data.keyword.semver}}-bundle.tar.gz ibm-eam-{{site.data.keyword.semver}}-bundle.tar.gz &amp;TWBAMP;&amp;TWBAMP; \ tar -zxvf ibm-eam-{{site.data.keyword.semver}}-bundle.tar.gz &amp;TWBAMP;&amp;TWBAMP; \ cd ibm-eam-{{site.data.keyword.semver}}-bundle/tools
    ```
    {: codeblock}
5. Valide o estado de instalação:
    ```
    ./service_healthcheck.sh
    ```
    {: codeblock}

    Consulte a seguinte saída de exemplo:
    ```
    $ ./service_healthcheck.sh     ==Executando testes de verificação de serviço para o IBM Edge Application Manager==     SUCCESS: a API de troca do IBM Edge Application Manager está operacional     SUCCESS: o serviço de sincronização de nuvem do IBM Edge Application Manager está operacional     SUCCESS: a pulsação do banco de dados do robô de contrato do IBM Edge Application Manager é atual     SUCCESS: a API do SDO do IBM Edge Application Manager está operacional     SUCCESS: a IU do IBM Edge Application Manager está solicitando adequadamente uma autenticação válida     ==Todos os serviços esperados estão funcionando==
    ```

   * Se houver falhas no comando **service_healthcheck.sh**, se você tiver problemas ao executar os comandos abaixo ou se houver problemas durante o tempo de execução, consulte [resolução de problemas](../admin/troubleshooting.md).

## Configuração de pós-instalação
{: #postconfig}

O processo a seguir deve ser executado em um host que suporte a instalação da CLI do **hzn**, que atualmente pode ser instalada em um host Linux baseado em Debian/apt Linux, amd64 Red Hat/rpm Linux ou macOS. Essas etapas usam a mesma mídia transferida por download a partir do PPA na seção Verificação da instalação.

1. Instale a CLI do **hzn** usando as instruções para a sua plataforma suportada:
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

2. Execute o script de pós-instalação. Este script executa toda a inicialização necessária para criar sua primeira organização. (Organizações são como o {{site.data.keyword.ieam}} separa recursos e usuários para permitir ocupação variada. Inicialmente, esta primeira organização é suficiente. Será possível configurar mais organizações posteriormente. Para obter mais informações, consulte [Ocupação variada](../admin/multi_tenancy.md)).

   **Nota**: A **IBM** e **root** são organizações de uso interno e não podem ser escolhidos como sua organização inicial. Um nome de organização não pode conter sublinhado (_), vírgulas (,), espaços em branco ( ), aspas simples (') ou pontos de interrogação (?).

   ```
   ./post_install.sh <choose-your-org-name>
   ```
   {: codeblock}

3. Execute o seguinte para imprimir o link do console de gerenciamento do {{site.data.keyword.ieam}} para a sua instalação:
   ```
   echo https://$(oc get cm management-ingress-ibmcloud-cluster-info -o jsonpath='{.data.cluster_ca_domain}')/edge
   ```
   {: codeblock}

## Autenticação 

A autenticação do usuário é necessária ao acessar o console de gerenciamento do {{site.data.keyword.ieam}}. Uma conta inicial de administrador foi criada por esta instalação e pode ser impressa pelo seguinte comando:
```
echo "$(oc -n ibm-common-services get secret platform-auth-idp-credentials -o jsonpath='{.data.admin_username}' | base64 --decode) // $(oc -n ibm-common-services get secret platform-auth-idp-credentials -o jsonpath='{.data.admin_password}' | base64 --decode)"
```
{: codeblock}

É possível usar essa conta de administrador para autenticação inicial  e, além disso, é possível [configurar o LDAP](https://www.ibm.com/support/knowledgecenter/SSHKN6/iam/3.x.x/configure_ldap.html) acessando o link do console de gerenciamento impresso pelo seguinte comando:
```
echo https://$(oc get cm management-ingress-ibmcloud-cluster-info -o jsonpath='{.data.cluster_ca_domain}')
```
{: codeblock}

Depois de estabelecer uma conexão LDAP, crie uma equipe, conceda a essa equipe acesso ao namespace em que o operador do {{site.data.keyword.edge_notm}} foi implementado e inclua usuários a essa equipe. Isso concede aos usuários individuais a permissão para criar chaves de API.

As chaves de API que são usadas para autenticação com a CLI do {{site.data.keyword.edge_notm}} e as permissões que são associadas às chaves de API são idênticas para o usuário com o qual elas são geradas.

Se você não criou uma conexão LDAP ainda poderá criar chaves de API usando as credenciais de administrador  iniciais; no entanto, lembre-se de que a chave de API terá privilégios de **Administrador de cluster**.

## O que Vem a Seguir

Siga o processo na página [Reunir arquivos de nós de borda](gather_files.md) para preparar a mídia de instalação para os seus nós de borda.
