# IBM Edge Computing Manager

## Introdução

O IBM Edge Computing Manager for Devices fornece uma **Plataforma de gerenciamento de aplicativos** de ponta a ponta para aplicativos implementados em dispositivos de borda típicos, em implementações de IoT. Essa plataforma fornece automatização completa, liberando os desenvolvedores de aplicativos da tarefa de implementar com segurança as revisões de cargas de trabalho de borda em milhares de dispositivos de borda implementados em campo. Por sua vez, o desenvolvedor de aplicativos pode se concentrar na tarefa de gravação do código do aplicativo em qualquer linguagem de programação, como um contêiner do Docker que pode ser implementado de forma independente. Essa plataforma se encarrega da implementação da solução de negócios completa, como uma orquestração de vários níveis de contêineres do Docker em todos os dispositivos de forma simples e segura.

## Pré-requisitos

* Red Hat OpenShift Container Platform 4.2
* IBM Multicloud Management core 1.2
* Se estiver hospedando seus próprios bancos de dados, forneça duas instâncias do PostgreSQL e uma instância do MongoDB para armazenar dados para os componentes do IBM Edge Computing Manager for Devices. Consulte a seção **Armazenamento** abaixo para obter detalhes.
* Um host Ubuntu Linux ou macOS a partir do qual conduzir a instalação. Ele deve ter o seguinte software instalado:
  * [CLI do Kubernetes (kubectl)](https://kubernetes.io/docs/tasks/tools/install-kubectl/) versão 1.14.0 ou mais recente
  * [CLI do IBM Cloud Pak (cloudctl)](https://www.ibm.com/support/knowledgecenter/SSFC4F_1.2.0/cloudctl/icp_cli.html)
  * [CLI do OpenShift (oc)](https://docs.openshift.com/container-platform/4.2/cli_reference/openshift_cli/getting-started-cli.html)
  * [CLI do Helm](https://helm.sh/docs/using_helm/#installing-the-helm-client) versão 2.9.1 ou mais recente
  * Outros pacotes de software:
    * jq
    * git
    * docker (versão 18.06.01 ou mais recente)
    * Fazer

## Requisitos de SecurityContextConstraints do Red Hat OpenShift

O nome de `SecurityContextConstraints` padrão: [`restricted`](https://ibm.biz/cpkspec-scc) foi verificado para este gráfico. Esta liberação limita-se à implementação no namespace `kube-system`, usa a conta de serviço `default` e também cria suas próprias contas de serviço para os subgráficos de banco de dados locais opcionais.

## Detalhes do Gráfico

Este gráfico do Helm instala e configura os contêineres certificados do IBM Edge Computing Manager for Devices em um ambiente OpenShift. Serão instalados os seguintes componentes:

* IBM Edge Computing Manager for Devices - Exchange
* IBM Edge Computing Manager for Devices - AgBots
* IBM Edge Computing Manager for Devices - Serviço de sincronização em nuvem (parte do Sistema de gerenciamento de modelo)
* IBM Edge Computing Manager for Devices - Interface com o usuário (console de gerenciamento)

## Recursos necessários

Para obter informações sobre os recursos necessários, consulte [Instalação - Dimensionamento](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/devices/installing/install.html#size).

## Requisitos de armazenamento e de banco de dados

São necessárias três instâncias de banco de dados para armazenar os dados do componente do IBM Edge Computing Manager for Devices.

Por padrão, o gráfico instalará três bancos de dados persistentes com os tamanhos de volume abaixo, usando uma classe de armazenamento dinâmica do Kubernetes padrão (ou configurada pelo usuário).

**Nota:** esses bancos de dados padrão não se destinam ao uso de produção. Para usar seus próprios bancos de dados gerenciados, consulte os requisito abaixo e siga as etapas na seção **Configurar bancos de dados remotos**.

* PostgreSQL: armazenamento de dados do Exchange e do AgBot
  * São necessárias duas instâncias separadas, cada uma com pelo menos 10 GB de armazenamento
  * A instância deve suportar pelo menos 100 conexões
  * Para o uso de produção, essas instâncias devem ser altamente disponíveis
* MongoDB: armazenamento de dados do Serviço de sincronização em nuvem
  * É necessária uma instância com pelo menos 50 GB de armazenamento. **Nota:** o tamanho necessário depende muito do tamanho e do número dos modelos e arquivos de serviços de borda utilizados.
  * Para o uso de produção, esta instância deve ser altamente disponível

**Nota:** ao usar seus próprios bancos de dados gerenciados, você é responsável pelos procedimentos de backup/restauração.
Consulte a seção **Backup e recuperação** para obter os procedimentos de banco de dados padrão.

## Monitorando recursos

Ao ser instalado, o IBM Edge Computing Manager for Devices automaticamente configura o monitoramento do produto e dos pods nos quais ele é executado. Os dados de monitoramento podem ser visualizados no painel do Grafana do console de gerenciamento, nos seguintes locais:

* `https://<MANAGEMENT_URL:PORT>/grafana/d/kube-system-edge-computing-overview/edge-computing-overview`
* `https://<MANAGEMENT_URL:PORT>/grafana/d/kube-system-edge-computing-pod-overview/edge-computing-pod-overview`

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
  name: edge-computing-remote-dbs
  labels:
    release: edge-computing
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

Para alterar qualquer um dos parâmetros de configuração padrão do Helm, é possível revisar os parâmetros e suas descrições usando o comando `grep` abaixo e, em seguida, visualizar/editar os valores correspondentes em `values.yaml`:

```bash
grep -v -E '(^ *#|__metadata)' ibm_cloud_pak/values-metadata.yaml
vi values.yaml   # or use your preferred editor
```

## Instalando o gráfico

** Notas: **

* Esta é uma instalação feita exclusivamente a partir da CLI; a instalação a partir da GUI não é suportada

* Você já deve ter executado as etapas contidas em [Instalando a infraestrutura do IBM Edge Computing Manager for Devices - Processo de instalação](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/devices/installing/install.html#process)
* Por haver apenas uma instância do IBM Edge Computing Manager for Devices instalada por cluster e ela só pode ser instalada no namespace `kube-system`.
* O upgrade a partir do IBM Edge Computing Manager for Devices 3.2 não é suportado

Execute o script de instalação fornecido para instalar o IBM Edge Computing Manager for Devices. As principais etapas executadas pelo script são: instalação do gráfico do Helm e configuração do ambiente após a instalação (criação do robô de contrato, da organização e do serviço de padrão/política).

```bash
ibm_cloud_pak/pak_extensions/full-install/install-edge-computing.sh
```

**Nota:** dependendo da velocidade da rede, serão necessários alguns minutos para o download das imagens, a transferência dos pods para o estado RUNNING e a ativação de todos os serviços.

### Verificando o gráfico

* O script acima verifica se os pods estão em execução e se o robô de contrato e o Exchange estão respondendo. Procure pelas mensagens "RUNNING" e "PASSED" perto do fim da instalação.
* Em caso de "FAILED", a saída solicitará que você consulte logs específicos para obter mais informações
* Em caso de "PASSED", a saída mostrará detalhes dos testes executados e mais dois itens a serem verificados
  * Navegue para o console da IU do IBM Edge Computing Manager usando a URL fornecida no final do log.
    * `https://<MANAGEMENT_URL:PORT>/edge`

## Após a Instalação

Siga as etapas em [Configuração de pós-instalação](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/devices/installing/install.html#postconfig).

## Desinstalando o Gráfico

**Nota:** se você estiver desinstalando com bancos de dados locais configurados, **todos os dados serão excluídos**. Caso queira preservar esses dados antes da desinstalação, consulte a seção **Procedimento de backup** abaixo.

Retorne para o local deste README.md e execute o script de desinstalação fornecido para automatizar as tarefas de desinstalação. As principais etapas executadas pelo script são: desinstalação dos gráficos do Helm e remoção de segredos. Primeiro, efetue login no cluster como um administrador de cluster, usando `cloudctl`. Em
seguida:

```bash
ibm_cloud_pak/pak_extensions/uninstall/uninstall-edge-computing.sh <cluster-name>
```

**Nota:** caso você tenha fornecido bancos de dados remotos, o segredo de autenticação será excluído, mas não serão executadas tarefas para remover/excluir dados desses bancos de dados remotos. Se quiser excluir esses dados, faça-o agora.

## Acesso baseado em função

* Para instalar e gerenciar esse produto, é necessário ter a autoridade de administrador de cluster no namespace `kube-system`.
* Autenticação e funções do Exchange:
  * A autenticação de todos os administradores e usuários do Exchange é fornecida pelo IAM, por meio de chaves de API geradas com o comando `cloudctl`
  * Os administradores do Exchange devem receber o privilégio `admin` dentro do Exchange. Com esse privilégio, é possível gerenciar todos os usuários, nós, serviços, padrões e políticas dentro da organização do Exchange
  * Os usuários não administradores do Exchange podem gerenciar apenas usuários, nós, serviços, padrões e políticas que eles mesmos criaram

## Segurança

* O TLS é usado para todos os dados que entram/saem do cluster do OpenShift por meio de ingresso. Nessa liberação, o TLS não é usado **dentro** do cluster do OpenShift para a comunicação do nó. Se quiser, é possível configurar a malha de serviço do Red Hat OpenShift para a comunicação entre microsserviços. Consulte [Entendendo a malha de serviços do Red Hat OpenShift](https://docs.openshift.com/container-platform/4.2/service_mesh/service_mesh_arch/understanding-ossm.html#understanding-ossm).
* Esse gráfico não fornece criptografia dos dados em repouso.  Cabe ao administrador configurar a criptografia de armazenamento.

## Backup e Recuperação

### Procedimento de Backup

Execute estes comandos depois de conectar-se ao cluster em um local que tenha espaço adequado para armazenar esses backups.


1. Crie um diretório usado para armazenar os backups abaixo e ajuste-o conforme desejado

```bash
export BACKUP_DIR=/tmp/edge-computing-backup/$(date +%Y%m%d_%H%M%S)
mkdir -p $BACKUP_DIR
```

2. Execute o seguinte para fazer backup de autenticação/segredos

```bash
oc -n kube-system get secret edge-computing -o yaml > $BACKUP_DIR/edge-computing-secret.yaml && \
oc -n kube-system get secret edge-computing-agbotdb-postgresql-auth-secret -o yaml > $BACKUP_DIR/edge-computing-agbotdb-postgresql-auth-secret-backup.yaml && \
oc -n kube-system get secret edge-computing-exchangedb-postgresql-auth-secret -o yaml > $BACKUP_DIR/edge-computing-exchangedb-postgresql-auth-secret-backup.yaml && \
oc -n kube-system get secret edge-computing-css-db-ibm-mongodb-auth-secret -o yaml > $BACKUP_DIR/edge-computing-css-db-ibm-mongodb-auth-secret-backup.yaml
```

3. Execute o seguinte para fazer backup do conteúdo do banco de dados

```bash
oc -n kube-system exec edge-computing-exchangedb-keeper-0 -- bash -c "export PGPASSWORD=$(oc -n kube-system get secret edge-computing -o jsonpath="{.data.exchange-db-pass}" | base64 --decode) && pg_dump -U admin -h edge-computing-exchangedb-proxy-svc -F t postgres > /stolon-data/exchange-backup.tar" && \
oc -n kube-system cp edge-computing-exchangedb-keeper-0:/stolon-data/exchange-backup.tar $BACKUP_DIR/exchange-backup.tar
```

```bash
oc -n kube-system exec edge-computing-agbotdb-keeper-0 -- bash -c "export PGPASSWORD=$(oc -n kube-system get secret edge-computing -o jsonpath="{.data.agbot-db-pass}" | base64 --decode) && pg_dump -U admin -h edge-computing-agbotdb-proxy-svc -F t postgres > /stolon-data/agbot-backup.tar" && \
oc -n kube-system cp edge-computing-agbotdb-keeper-0:/stolon-data/agbot-backup.tar $BACKUP_DIR/agbot-backup.tar
```

```bash
oc -n kube-system exec edge-computing-cssdb-server-0 -- bash -c "mkdir -p /data/db/backup; mongodump -u admin -p $(oc -n kube-system get secret edge-computing -o jsonpath="{.data.css-db-pass}" | base64 --decode) --out /data/db/css-backup" && \
oc -n kube-system cp edge-computing-cssdb-server-0:/data/db/css-backup $BACKUP_DIR/css-backup
```

4. Após a verificação dos backups, remova-os dos contêineres stateless

```bash
oc -n kube-system exec edge-computing-exchangedb-keeper-0 -- bash -c "rm -f /stolon-data/exchange-backup.tar"
```

```bash
oc -n kube-system exec edge-computing-agbotdb-keeper-0 -- bash -c "rm -f /stolon-data/agbot-backup.tar"
```

```bash
oc -n kube-system exec edge-computing-cssdb-server-0 -- bash -c "rm -rf /data/db/css-backup"
```

### Procedimento de Restauração

**Nota:** em caso de restauração para um novo clusetr, esse 'nome do cluster' deve corresponder ao nome do cluster a partir do qual os backups foram feitos.

1. Exclua do cluster quaisquer segredos preexistentes
```bash
oc -n kube-system delete secret edge-computing edge-computing-agbotdb-postgresql-auth-secret edge-computing-exchangedb-postgresql-auth-secret edge-computing-css-db-ibm-mongodb-auth-secret;
```

2. Exporte estes valores para a máquina local

```bash
export BACKUP_DIR=/tmp/edge-computing-backup/<Insert desired backup datestamp YYYYMMDD_HHMMSS>
```

3. Execute o seguinte para restaurar autenticação/segredos

```bash
oc apply -f $BACKUP_DIR
```

4. Reinstale o IBM Edge Computing Manager antes de continuar e siga as instruções na seção **Instalando o gráfico**

5. Execute o seguinte para copiar os backups para os contêineres e restaurá-los

```bash
oc -n kube-system cp $BACKUP_DIR/exchange-backup.tar edge-computing-exchangedb-keeper-0:/stolon-data/exchange-backup.tar && \
oc exec -n kube-system edge-computing-exchangedb-keeper-0 -- bash -c "export PGPASSWORD=$(oc get secret edge-computing -o jsonpath="{.data.exchange-db-pass}" | base64 --decode) && pg_restore -U admin -h edge-computing-exchangedb-proxy-svc -d postgres -c /stolon-data/exchange-backup.tar"
```

```bash
oc -n kube-system cp $BACKUP_DIR/agbot-backup.tar edge-computing-agbotdb-keeper-0:/stolon-data/agbot-backup.tar && \
oc exec -n kube-system edge-computing-agbotdb-keeper-0 -- bash -c "export PGPASSWORD=$(oc get secret edge-computing -o jsonpath="{.data.agbot-db-pass}" | base64 --decode) && pg_restore -U admin -h edge-computing-agbotdb-proxy-svc -d postgres -c /stolon-data/agbot-backup.tar"
```

```bash
oc -n kube-system cp $BACKUP_DIR/css-backup edge-computing-cssdb-server-0:/data/db/css-backup && \
oc exec -n kube-system edge-computing-cssdb-server-0 -- bash -c "mongorestore -u admin -p $(oc get secret edge-computing -o jsonpath="{.data.css-db-pass}" | base64 --decode) /data/db/css-backup";
```

6. Execute o seguinte para atualizar as conexões com o banco de dados do pod do Kubernetes
```bash
for POD in $(oc get pods -n kube-system | grep -E '\-agbot\-|\-css\-|\-exchange\-' | awk '{print $1}'); do oc delete pod $POD -n kube-system; done
```

## Limitations

* Limites de instalação: este produto pode ser instalado apenas uma vez e somente no namespace `kube-system`
* Nesta liberação não há privilégios de autorização distintos para administração do produto e operação do produto.

## Documentação

* Consulte o documento [Instalação](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/devices/installing/install.html) do Knowledge Center para obter diretrizes e atualizações adicionais.

## Direitos Autorais

© Copyright IBM Corporation 2020. All Rights Reserved.
