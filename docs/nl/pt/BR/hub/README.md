# IBM&reg; Edge Application Manager

## Introdução

O IBM Edge Application Manager fornece uma **Plataforma de gerenciamento de aplicativos** de ponta a ponta para aplicativos implementados em dispositivos de borda típicos, em implementações de IoT. Essa plataforma fornece automatização completa, liberando os desenvolvedores de aplicativos da tarefa de implementar com segurança as revisões de cargas de trabalho de borda em milhares de dispositivos de borda implementados em campo. Por sua vez, o desenvolvedor de aplicativos pode se concentrar na tarefa de gravação do código do aplicativo em qualquer linguagem de programação, como um contêiner do Docker que pode ser implementado de forma independente. Essa plataforma se encarrega da implementação da solução de negócios completa, como uma orquestração de vários níveis de contêineres do Docker em todos os dispositivos de forma simples e segura.

https://www.ibm.com/cloud/edge-application-manager

## Pré-requisito

Consulte o seguinte para obter os [Pré-requisitos](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/hub/offline_installation.html#prereq).

## Requisitos de SecurityContextConstraints do Red Hat OpenShift

O nome de `SecurityContextConstraints` padrão: [`restricted`](https://ibm.biz/cpkspec-scc) foi verificado para este gráfico. Esta liberação limita-se à implementação no namespace `kube-system` e cria contas de serviço para o gráfico
principal e contas de serviço adicionais para os subgráficos de banco de dados locais padrão.

## Detalhes do Gráfico

Este gráfico do Helm instala e configura os contêineres certificados do IBM Edge Application Manager em um ambiente OpenShift. Serão instalados os seguintes componentes:

* IBM Edge Application Manager - Exchange
* IBM Edge Application Manager - AgBots
* IBM Edge Application Manager - Cloud Sync Service (como parte do Model Management System)
* IBM Edge Application Manager - Interface com o usuário (console de gerenciamento)

## Recursos necessários

Consulte o seguinte para obter o [Dimensionamento](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/hub/cluster_sizing.html).

## Requisitos de armazenamento e de banco de dados

São necessárias três instâncias de banco de dados para armazenar os dados do componente do IBM Edge Application Manager.

Por padrão, o gráfico instalará três bancos de dados persistentes com os tamanhos de volume abaixo, usando uma classe de armazenamento dinâmica do Kubernetes padrão (ou configurada pelo usuário). Se estiver usando uma classe de armazenamento que não segue a expansão de volume, assegure-se de permitir a expansão de modo apropriado.

**Nota:** esses bancos de dados padrão não se destinam ao uso de produção. Para usar seus próprios bancos de dados gerenciados, consulte os requisito abaixo e siga as etapas na seção **Configurar bancos de dados remotos**.

* PostgreSQL: armazenamento de dados do Exchange e do AgBot
  * São necessárias duas instâncias separadas, cada uma com pelo menos 20 GB de armazenamento
  * A instância deve suportar pelo menos 100 conexões
  * Para o uso de produção, essas instâncias devem ser altamente disponíveis
* MongoDB: armazenamento de dados do Serviço de sincronização em nuvem
  * É necessária uma instância com pelo menos 50 GB de armazenamento. **Nota:** o tamanho necessário depende muito do tamanho e do número dos modelos e arquivos de serviços de borda utilizados.
  * Para o uso de produção, esta instância deve ser altamente disponível

**Nota:** você é responsável pelos procedimentos de backup/restauração para esses bancos de dados padrão, bem como para seus próprios bancos de dados gerenciados.
Consulte a seção **Backup e recuperação** para obter os procedimentos de banco de dados padrão.

## Monitorando recursos

Quando o IBM Edge Application Manager é instalado, ele configura automaticamente algum monitoramento básico dos recursos do produto em execução no Kubernetes. Os dados de monitoramento podem ser visualizados no painel do Grafana do console de gerenciamento, no local a seguir:

* `https://<MANAGEMENT_URL:PORT>/grafana/d/kube-system-ibm-edge-overview/ibm-edge-overview`

## Configuração

#### Configurar bancos de dados remotos

1. Para usar seus próprios bancos de dados gerenciados, procure em `values.yaml` o parâmetro de configuração do Helm mostrado a seguir e altere seu valor para `false`:

```yaml
localDBs:
  enabled: true
```

2. Crie um arquivo (chamado `dbinfo.yaml`, por exemplo) iniciando com este conteúdo de modelo:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: ibm-edge-remote-dbs
  labels:
    release: ibm-edge
type: Opaque
stringData:
  # agbot postgresql connection settings
  agbot-db-host: "Single hostname of the remote database"
  agbot-db-port: "Single port the database runs on"
  agbot-db-name: "The name of the database to utilize on the postgresql instance"
  agbot-db-user: "Username used to connect"
  agbot-db-pass: "Password used to connect"
  agbot-db-ssl: "SSL Options: <disable|require|verify-full>"

  # exchange postgresql connection settings
  exchange-db-host: "Single hostname of the remote database"
  exchange-db-port: "Single port the database runs on"
  exchange-db-name: "The name of the database to utilize on the postgresql instance"
  exchange-db-user: "Username used to connect"
  exchange-db-pass: "Password used to connect"
  exchange-db-ssl: "SSL Options: <disable|require|verify-full>"

  # css mongodb connection settings
  css-db-host: "Comma separate <hostname>:<port>,<hostname2>:<port2>"
  css-db-name: "The name of the database to utilize on the mongodb instance"
  css-db-user: "Username used to connect"
  css-db-pass: "Password used to connect"
  css-db-auth: "The name of the database used to store user credentials"
  css-db-ssl: "SSL Options: <true|false>"

  trusted-certs: |-
    -----BEGIN CERTIFICATE-----
    ....
    -----END CERTIFICATE-----
    -----BEGIN CERTIFICATE-----
    ....
    -----END CERTIFICATE-----
```

3. Edite `dbinfo.yaml` para fornecer as informações de acesso para os bancos de dados fornecidos. Preencha todas as informações contidas entre as aspas duplas (mantendo os valores entre aspas). Ao incluir os certificados confiáveis, certifique-se de que cada linha tenha quatro espaços de indentação, para assegurar a leitura correta do arquivo yaml. Caso dois ou mais bancos de dados usem o mesmo certificado, **não** é necessário repetir o certificado em `dbinfo.yaml`. Salve o arquivo e, em seguida, execute:

```bash
oc --namespace kube-system apply -f dbinfo.yaml
```


#### Configuração Avançada

Para mudar qualquer um dos parâmetros de configuração padrão do Helm, revise os parâmetros e suas descrições usando o comando `grep` abaixo e, em seguida, visualize ou edite os valores correspondentes em `values.yaml`:

```bash
grep -v -E '(^ *#|__metadata)' ibm_cloud_pak/values-metadata.yaml
vi values.yaml   # or use any editor
```

## Instalando o gráfico

** Notas: **

* Esta é uma instalação feita exclusivamente a partir da CLI; a instalação a partir da GUI não é suportada

* Assegure-se de que as etapas em [Instalando a infraestrutura do IBM Edge Application Manager - Processo de instalação](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/hub/offline_installation.html#process) tenham sido concluídas.
* Por haver apenas uma instância do IBM Edge Application Manager instalada por cluster e ela só pode ser instalada no namespace `kube-system`.
* O upgrade a partir do IBM Edge Application Manager 4.0 não é suportado

Execute o script de instalação fornecido para instalar o IBM Edge Application Manager. As principais etapas executadas pelo script são: instalação do gráfico do Helm e configuração do ambiente após a instalação (criação do robô de contrato, da organização e do serviço de padrão/política).

```bash
ibm_cloud_pak/pak_extensions/support/ieam-install.sh
```

**Nota:** dependendo da velocidade da rede, serão necessários alguns minutos para o download das imagens e para a implementação de todos os recursos de gráfico.

### Verificando o gráfico

* O script acima verifica se os pods estão em execução e se o robô de contrato e o Exchange estão respondendo. Procure pelas mensagens "RUNNING" e "PASSED" perto do fim da instalação.
* Em caso de "FAILED", a saída solicitará que você consulte logs específicos para obter mais informações
* Em caso de "PASSED", a saída mostrará detalhes dos testes que foram executados e a URL da IU de gerenciamento
  * Navegue para o console da IU do IBM Edge Application Manager usando a URL fornecida no final do log.
    * `https://<MANAGEMENT_URL:PORT>/edge`

## Após a Instalação

Siga as etapas em [Configuração de pós-instalação](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/hub/post_install.html).

## Desinstalando o Gráfico

Siga as etapas em [Desinstalando o hub de
gerenciamento](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/hub/uninstall.html).

## Acesso baseado em função

* Para instalar e gerenciar esse produto, é necessário ter a autoridade de administrador de cluster no namespace `kube-system`.
* As contas de serviço, as funções e as ligações de função são criadas para este gráfico e para os seus subgráficos com base no nome da liberação.
* Autenticação e funções do Exchange:
  * A autenticação de todos os administradores e usuários do Exchange é fornecida pelo IAM, por meio de chaves de API geradas com o comando `cloudctl`
  * Os administradores do Exchange devem receber o privilégio `admin` dentro do Exchange. Com esse privilégio, é possível gerenciar todos os usuários, nós, serviços, padrões e políticas dentro da organização do Exchange
  * Os usuários não administradores do Exchange podem gerenciar apenas usuários, nós, serviços, padrões e políticas que eles mesmos criaram

## Segurança

* O TLS é usado para todos os dados que entram/saem do cluster do OpenShift por meio de ingresso. Nessa liberação, o TLS não é usado **dentro** do cluster do OpenShift para a comunicação do nó. Se desejado, configure a malha de serviço do Red Hat OpenShift para a comunicação entre microsserviços. Consulte [Entendendo a malha de serviços do Red Hat OpenShift](https://docs.openshift.com/container-platform/4.4/service_mesh/service_mesh_arch/understanding-ossm.html#understanding-ossm).
* Esse gráfico não fornece criptografia dos dados em repouso.  O administrador é responsável por configurar o armazenamento na criptografia de rest.

## Backup e Recuperação

Siga as etapas em [Backup e recuperação](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/admin/backup_recovery.html).

## Limitations

* Limites de instalação: este produto pode ser instalado apenas uma vez e somente no namespace `kube-system`

## Documentação

* Consulte a documentação [Instalação](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/hub/hub.html) do Knowledge Center para obter informações adicionais.

## Direitos Autorais

© Copyright IBM Corporation 2020. All Rights Reserved.
