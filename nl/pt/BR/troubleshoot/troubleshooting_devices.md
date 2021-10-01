---

copyright:
years: 2019, 2020, 2021
lastupdated: "2021-09-01"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Dicas de resolução de problemas
{: #troubleshooting_devices}

Revise as perguntas a seguir quando encontrar um problema com o {{site.data.keyword.edge_notm}}. As dicas e os guias de cada pergunta podem ajudá-lo a resolver problemas comuns e obter informações para identificar as causas raiz.
{:shortdesc}

  * [As versões liberadas atualmente dos pacotes do {{site.data.keyword.horizon}} estão instaladas?](#install_horizon)
  * [O agente do {{site.data.keyword.horizon}} está ativo e ativamente em execução no momento?](#setup_horizon)
  * [O nó de borda está configurado para interagir com o {{site.data.keyword.horizon_exchange}}?](#node_configured)
  * [Os contêineres do Docker necessários foram iniciados para a execução do nó de borda?](#node_running)
  * [As versões do contêiner de serviço esperadas estão em execução?](#run_user_containers)
  * [Os contêineres esperados estão estáveis?](#containers_stable)
  * [Os contêineres do Docker estão conectados à rede corretamente?](#container_networked)
  * [Os contêineres de dependência estão acessíveis no contexto do seu contêiner?](#setup_correct)
  * [Os contêineres definidos pelo usuário estão emitindo mensagens de erro para o log?](#log_user_container_errors)
  * [É possível usar a instância da organização do bloker {{site.data.keyword.message_hub_notm}} Kafka?](#kafka_subscription)
  * [Seus contêineres estão publicados no {{site.data.keyword.horizon_exchange}}?](#publish_containers)
  * [Seu padrão de implementação publicado inclui todos os serviços e as versões necessários?](#services_included)
  * [Dicas de resolução de problemas específicos para o ambiente do {{site.data.keyword.open_shift_cp}}](#troubleshooting_icp)
  * [Resolução de problemas de erros do nó](#troubleshooting_node_errors)
  * [Como desinstalar o Podman no RHEL?](#uninstall_podman)

## As versões dos pacotes do {{site.data.keyword.horizon}} liberadas atualmente estão instaladas?
{: #install_horizon}

Assegure-se de que o software do {{site.data.keyword.horizon}} que está instalado em seus nós de borda esteja sempre na versão mais recente liberada.

Em um sistema {{site.data.keyword.linux_notm}}, geralmente é possível verificar a versão de seus pacotes instalados do {{site.data.keyword.horizon}} executando este comando:  
```
dpkg -l | grep horizon
```
{: codeblock}

É possível atualizar seus pacotes do {{site.data.keyword.horizon}} que usam o gerenciador de pacotes em seu sistema. Por exemplo, em um sistema {{site.data.keyword.linux_notm}} baseado em Ubuntu, use os comandos a seguir para atualizar o {{site.data.keyword.horizon}} para a versão atual:
```
sudo apt update sudo apt install -y blue horizon
```

## O agente do {{site.data.keyword.horizon}} está ativo e ativamente em execução?
{: #setup_horizon}

É possível verificar se o agente está em execução usando este comando da CLI do {{site.data.keyword.horizon}}:
```
hzn node list | jq .
```
{: codeblock}

Também é possível usar o software de gerenciamento do sistema do host para verificar o status do agente do {{site.data.keyword.horizon}}. Por exemplo, em um sistema {{site.data.keyword.linux_notm}} baseado em Ubuntu, é possível usar o utilitário `systemctl`:
```
sudo systemctl status horizon
```
{: codeblock}

Uma linha semelhante à seguinte é mostrada quando o agente está ativo:
```
Active: active (running) since Thu 2020-10-01 17:56:12 UTC; 2 weeks 0 days ago
```
{: codeblock}

## O nó de borda está configurado para interagir com o {{site.data.keyword.horizon_exchange}}? 
{: #node_configured}

Para verificar se é possível se comunicar com o {{site.data.keyword.horizon_exchange}}, execute este comando:
```
hzn exchange version
```
{: codeblock}

Para verificar se o seu {{site.data.keyword.horizon_exchange}} está acessível, execute este comando:
```
hzn exchange user list
```
{: codeblock}

Depois que o nó de borda for registrado com o {{site.data.keyword.horizon}}, será possível verificar se o nó está interagindo com o {{site.data.keyword.horizon_exchange}} visualizando a configuração do agente do {{site.data.keyword.horizon}} local. Execute este comando para visualizar a configuração do agente:
```
hzn node list | jq .configuration.exchange_api
```
{: codeblock}

## Os contêineres do Docker necessários para o nó de borda estão em execução?
{: #node_running}

Quando o nó de borda é registrado com o {{site.data.keyword.horizon}}, um Robô de contrato do {{site.data.keyword.horizon}} cria um contrato com seu nó de borda para executar os serviços referenciados no tipo de gateway (padrão de implementação). Se este contrato não for criado, conclua essas verificações para solucionar o problema.

Confirme se o seu nó de borda está no estado `configured` e se tem os valores `id` e `organization` corretos. Além disso, confirme se a arquitetura que o {{site.data.keyword.horizon}} está relatando é a mesma arquitetura que você usou nos metadados para seus serviços. Execute este comando para listar essas configurações:
```
hzn node list | jq .
```
{: codeblock}

Se esses valores forem os esperados, é possível verificar o status de concordância do nó de borda executando: 
```
hzn agreement list | jq .
```
{: codeblock}

Se este comando não mostrar nenhum contrato, esses contratos podem ter sido formados, mas um problema pode ter sido descoberto. Se isso ocorrer, o contrato poderá ser cancelado antes de poder ser exibido na saída do comando anterior. Se este cancelamento de contrato ocorrer, o contrato cancelado mostrará um status de `terminated_description` na lista de contratos arquivados. É possível visualizar a lista arquivada executando este comando: 
```
hzn agreement list -r | jq .
```
{: codeblock}

Também é possível que ocorra um problema antes da criação do contrato. Se esse problema ocorrer, revise o log de eventos do agente {{site.data.keyword.horizon}} para identificar possíveis erros. Execute este comando para visualizar o log: 
```
hzn eventlog list
``` 
{: codeblock}

O log de eventos pode incluir: 

* A assinatura dos metadados do serviço, especificamente o campo `deployment`, não pode ser verificada. Esse erro geralmente significa que a chave pública de assinatura não foi importada no nó de borda. É possível importar a chave usando o comando `hzn key import -k<pubkey>`. É possível visualizar as chaves que são importadas para o nó de borda local usando o comando `hzn key list`. É possível verificar se os metadados do serviço no {{site.data.keyword.horizon_exchange}} são assinados com a sua chave usando este comando:
  ```
  hzn exchange service verify -k $PUBLIC_KEY_FILE <service-id>
  ```
  {: codeblock} 

Substitua `<service-id>` pelo ID do seu serviço. Esse ID pode ser semelhante ao formato de amostra a seguir: `workload-cpu2wiotp_${CPU2WIOTP_VERSION}_${ARCH2}`.

* O caminho da imagem do Docker no campo `deployment` do serviço está incorreto. Confirme se no nó de borda pode efetuar `docker pull` nesse caminho da imagem.
* O agente do {{site.data.keyword.horizon}} no nó da borda não tem acesso ao registro do Docker que contém as imagens do Docker. Se as imagens do Docker no registro do Docker remoto não forem legíveis para todos, você deverá incluir as credenciais no nó de borda usando o comando `docker login`. É necessário concluir essa etapa apenas uma vez, uma vez que as credenciais são lembradas no nó de borda.
* Se um contêiner estiver reiniciando continuamente, revise o log do contêiner para obter detalhes. Um contêiner pode ser reinicializado continuamente quando é listado por apenas alguns segundos ou permanece listado como reiniciando quando você executa o comando `docker ps`. É possível visualizar o log do contêiner para obter detalhes executando este comando:
  ```
  grep --text -E ' <service-id>\[[0-9]+\]' /var/log/syslog
  ```
  {: codeblock}

## As versões do contêiner de serviço esperadas estão em execução?
{: #run_user_containers}

Suas versões do contêiner são controladas por um contrato que é criado após a inclusão do serviço no padrão de implementação e após o registro do nó de borda nesse padrão. Verifique se o seu nó de borda possui um contrato atual para seu padrão executando este comando:

```
hzn agreement list | jq .
```
{: codeblock}

Se você confirmou o contrato correto para seu padrão, use este comando para visualizar os contêineres em execução. Assegure-se de que os contêineres definidos pelo usuário estejam listados e estejam em execução:
```
docker ps
```
{: codeblock}

Depois que o agente do {{site.data.keyword.horizon}} aceitar o contrato poderá levar vários minutos para que os contêineres correspondentes sejam transferidos por download, sejam verificados e comecem a ser executados. Este contrato depende principalmente dos tamanhos dos próprios contêineres, que devem ser puxados dos repositórios remotos.

## Os contêineres esperados estão estáveis?
{: #containers_stable}

Verifique se seus contêineres estão estáveis executando este comando:
```
docker ps
```
{: codeblock}

A partir da saída de comando, é possível ver a duração da execução de cada contêiner. Se ao longo do tempo, você observar que os contêineres estão sendo reiniciados inesperadamente, verifique os logs do contêiner em busca de erros.

Como uma melhor prática de desenvolvimento, considere configurar a criação de log de serviço individual executando os comandos a seguir (somente sistemas {{site.data.keyword.linux_notm}}):
```bash
cat <<'EOF' > /etc/rsyslog.d/10-horizon-docker.conf $template DynamicWorkloadFile,"/var/log/workload/%syslogtag:R,ERE,1,DFLT:.*workload-([^\[]+)--end%.log"  :syslogtag, startswith, "workload-" -?DynamicWorkloadFile & stop :syslogtag, startswith, "docker/" -/var/log/docker_containers.log & stop :syslogtag, startswith, "docker" -/var/log/docker.log & stop EOF service rsyslog restart
```
{: codeblock}

Se você concluir a etapa anterior, então os logs para seus contêineres serão registrados dentro de arquivos separados dentro do diretório `/var/log/workload/`. Use o comando `docker ps` para localizar os nomes completos dos contêineres. É possível localizar o arquivo de log com esse nome, com um sufixo `.log`, nesse diretório.

Se a criação de log serviço individual não estiver configurada, seus logs de serviço serão incluídos ao log do sistema com todas as outras mensagens de log. Para revisar os dados de seus contêineres, é necessário procurar o nome do contêiner na saída de log do sistema dentro do arquivo `/var/log/syslog`. Por exemplo, é possível pesquisar no log, executando um comando semelhante a:
```
grep --text -E 'YOURSERVICENAME\[[0-9]+\]' /var/log/syslog
```
{: codeblock}

## Seus contêineres do Docker estão em rede corretamente?
{: #container_networked}

Assegure-se de que seus contêineres estejam em rede com o Docker adequadamente, para que eles possam acessar os serviços necessários. Execute este comando para assegurar que seja possível visualizar as redes virtuais do Docker ativas em seu nó de borda:
```
docker network list
```
{: codeblock}

Para visualizar mais informações sobre redes, use o comando `docker inspect X`, em que `X` é o nome da rede. A saída de comando lista todos os contêineres que são executados na rede virtual.

Também é possível executar o comando `docker inspect Y` em cada contêiner, em que `Y` é o nome do contêiner, para obter mais informações. Por exemplo, revise as informações do contêiner do `NetworkSettings` e procure o contêiner `Networks`. Dentro desse contêiner, é possível visualizar a sequência de ID de rede e informações relevantes sobre como o contêiner está representado na rede. Essas informações de representação incluem o `IPAddress` do contêiner e a lista de aliases de rede que estão nesta rede. 

Os nomes de alias estão disponíveis para todos os contêineres nessa rede virtual e esses nomes geralmente são usados pelos contêineres em seu padrão de implementação de código para descobrir outros contêineres na rede virtual. Por exemplo, é possível nomear o seu serviço `myservice`. Em seguida, outros contêineres podem usar esse nome diretamente para acessá-lo na rede, usando o comando `ping myservice`. O nome do alias do seu contêiner é especificado no campo `deployment` de seu arquivo de definição de serviço que você transferiu para o comando `hzn exchange service publish`.

Para obter mais informações sobre os comandos suportados pela interface da linha de comandos do Docker, consulte [Referência de comando do Docker](https://docs.docker.com/engine/reference/commandline/docker/#child-commands).

## Os contêineres de dependência são acessíveis dentro do contexto do seu contêiner?
{: #setup_correct}

Insira o contexto de um contêiner em execução para solucionar problemas no tempo de execução usando o comando `docker exec`. Use o comando `docker ps` para localizar o identificador do contêiner em execução e, em seguida, use um comando semelhante ao seguinte para inserir o contexto. Substitua `CONTAINERID` pelo identificador do contêiner:
```
docker exec -it CONTAINERID /bin/sh
```
{: codeblock}

Se o seu contêiner incluir bash, talvez você queira especificar `/bin/bash` no término do comando anterior em vez de `/bin/sh`.

Quando dentro do contexto do container, é possível usar comandos como `ping` ou `curl` para interagir com os containers necessários e verificar a conectividade.

Para obter mais informações sobre os comandos suportados pela interface da linha de comandos do Docker, consulte [Referência de comando do Docker](https://docs.docker.com/engine/reference/commandline/docker/#child-commands).

## Os contêineres definidos pelo usuário estão emitindo mensagens de erro para o log?
{: #log_user_container_errors}

Se você configurou a criação de log de serviço individual, cada um dos contêineres registram em log em um arquivo separado dentro do diretório `/var/log/workload/`. Use o comando `docker ps` para localizar os nomes completos dos contêineres. Em seguida, procure um arquivo com esse nome e que inclua o sufixo `.log`, dentro desse diretório.

Se a criação de log de serviço individual não estiver configurada, o serviço será registrado no log do sistema com todos os outros detalhes. Para revisar os dados, procure o log do contêiner na saída de log do sistema dentro do diretório `/var/log/syslog`. Por exemplo, faça uma procura no log, executando um comando semelhante a:
```
grep --text -E 'YOURSERVICENAME\[[0-9]+\]' /var/log/syslog
```
{: codeblock}

## É possível usar a instância da sua organização do broker {{site.data.keyword.message_hub_notm}} Kafka?
{: #kafka_subscription}

Assinar a instância do Kafka da sua organização a partir do {{site.data.keyword.message_hub_notm}} pode ajudá-lo a verificar se as credenciais do usuário Kafka estão corretas. Essa assinatura também pode ajudar a verificar se a instância de serviço Kafka está em execução na nuvem e se o nó de borda está enviando dados quando os dados estão sendo publicados.

Para se inscrever no seu broker Kafka, instale o programa `kafkacat`. Por exemplo, em um sistema {{site.data.keyword.linux_notm}} Ubuntu, use este comando:

```bash
sudo apt install kafkacat
```
{: codeblock}

Após a instalação, será possível assinar usando um comando semelhante ao seguinte exemplo que usa as credenciais que você costuma colocar em referências de variáveis de ambiente:

```bash
kafkacat -C -q -o end -f "%t/%p/%o/%k: %s\n" -b $EVTSTREAMS_BROKER_URL -X api.version.request=true -X security.protocol=sasl_ssl -X sasl.mechanisms=PLAIN -X sasl.username=token -X sasl.password=$EVTSTREAMS_API_KEY -t $EVTSTREAMS_TOPIC
```
{: codeblock}

Em que `EVTSTREAMS_BROKER_URL` é a URL para o broker do Kafka, `EVTSTREAMS_TOPIC` é o tópico do Kafka e `EVTSTREAMS_API_KEY` é a chave de API para autenticação na API do {{site.data.keyword.message_hub_notm}}.

Se o comando de assinatura for bem-sucedido, ele será bloqueado indefinidamente. O comando aguarda qualquer publicação no seu broker Kafka e recupera e exibe quaisquer mensagens resultantes. Se não for exibida nenhuma mensagem do nó de borda após alguns minutos, revise o log do serviço para obter mensagens de erro.

Por exemplo, para revisar o log do serviço `cpu2evtstreams`, execute este comando:

* Para o {{site.data.keyword.linux_notm}} e o {{site.data.keyword.windows_notm}} 

```bash
tail -n 500 -f /var/log/syslog | grep -E 'cpu2evtstreams\[[0-9]+\]:'
```
{: codeblock}

* Para macOS

```bash
docker logs -f $(docker ps --filter 'name=-cpu2evtstreams' | tail -n +2 | awk '{print $1}')
```
{: codeblock}

## Seus contêineres são publicados no {{site.data.keyword.horizon_exchange}}?
{: #publish_containers}

O {{site.data.keyword.horizon_exchange}} é o warehouse central para metadados sobre o código que é publicado para os nós de borda. Se você não assinou e publicou seu código no {{site.data.keyword.horizon_exchange}}, o código não poderá ser puxado para seus nós de borda, que são verificados e executados.

Execute o comando `hzn` com os argumentos a seguir para visualizar a lista de códigos publicados para verificar se todos os contêineres de serviço foram publicados com sucesso:

```
hzn exchange service list | jq .
hzn exchange service list $ORG_ID/$SERVICE | jq .
```
{: codeblock}

O parâmetro `ORG_ID` é o ID da organização e `$SERVICE` é o nome do serviço sobre o qual você está obtendo informações.

## O padrão de implementação publicado inclui todos os serviços e as versões necessários?
{: #services_included}

Em qualquer nó de borda em que o comando `hzn` esteja instalado, é possível usar este comando para obter detalhes sobre qualquer padrão de implementação. Execute o comando `hzn` com os argumentos a seguir para obter a lista de padrões de implementação a partir do {{site.data.keyword.horizon_exchange}}: 

```
hzn exchange pattern list | jq .
hzn exchange pattern list $ORG_ID/$PATTERN | jq .
```
{: codeblock}

O parâmetro `$ORG_ID` é seu ID de organização e `$PATTERN` é o nome do padrão de implementação sobre o qual você está obtendo informações.

## Dicas de resolução de problemas específicos para o ambiente {{site.data.keyword.open_shift_cp}}
{: #troubleshooting_icp}

Revise este conteúdo para ajudá-lo a solucionar problemas comuns com ambientes do {{site.data.keyword.open_shift_cp}} relacionados ao {{site.data.keyword.edge_notm}}. Essas dicas podem ajudá-lo a resolver problemas comuns e obter informações para identificar causas raiz.
{:shortdesc}

### Suas credenciais do {{site.data.keyword.edge_notm}} estão configuradas corretamente para uso no ambiente do {{site.data.keyword.open_shift_cp}}?
{: #setup_correct}

É necessária uma conta do usuário do {{site.data.keyword.open_shift_cp}} para concluir qualquer ação dentro do {{site.data.keyword.edge_notm}} neste ambiente. Também é necessária uma chave de API criada a partir dessa conta.

Para verificar suas credenciais do {{site.data.keyword.edge_notm}} neste ambiente, execute este comando:

   ```
   hzn exchange user list
   ```
   {: codeblock}

Se uma entrada formatada por JSON for retornada a partir do Exchange mostrando um ou mais usuários, as credenciais do {{site.data.keyword.edge_notm}} estão configuradas corretamente.

Se uma resposta de erro for retornada, é possível executar as etapas para solucionar problemas de configuração de credenciais.

Se a mensagem de erro indicar uma chave de API incorreta, é possível criar uma nova chave de API que use os comandos a seguir.

Consulte [Criando sua chave de API](../hub/prepare_for_edge_nodes.md).

## Resolução de problemas de erros do nó
{: #troubleshooting_node_errors}

O {{site.data.keyword.edge_notm}} publica um subconjunto de logs de eventos no Exchange que é visualizável na {{site.data.keyword.gui}}. Esses erros se vinculam à orientação de resolução de problemas.
{:shortdesc}

  - [Erro de carregamento de imagem](#eil)
  - [Erro de configuração de implementação](#eidc)
  - [Erro de início do contêiner](#esc)
  - [Erro interno do TLS do cluster de borda do OCP](#tls_internal)

### Erro de carregamento de imagem
{: #eil}

Este erro ocorre quando a imagem de serviço que é referenciada na definição de serviço não existe no repositório de imagem. Para resolver esse erro:

1. Publique novamente o serviço sem a sinalização **-I**.
    ```
    hzn exchange service publish -f <service-definition-file>
    ```
    {: codeblock}

2. Envie por push a imagem de serviço diretamente para o repositório de imagem. 
    ```
    docker push <image name>
    ```
    {: codeblock} 
    
### Erro de configuração de implementação
{: #eidc}

Este erro ocorre quando as configurações de implementação de definições de serviço especificam uma ligação a um arquivo protegido por raiz. Para resolver esse erro:

1. Ligue o contêiner a um arquivo que não esteja protegido por raiz.
2. Mude as permissões de arquivo para permitir que os usuários leiam e gravem no arquivo.

### Erro de início do contêiner
{: #esc}

Este erro ocorre quando o Docker encontra um erro quando ele inicia o contêiner de serviço. Esta mensagem de erro pode conter detalhes que indicam o motivo pelo qual o contêiner iniciou com falha. As etapas de resolução de erro dependem do erro. Os seguintes erros podem ocorrer:

1. O dispositivo já está usando uma porta publicada que é especificada pelas configurações de implementação. Para resolver o erro: 

    - Mapeie uma porta diferente para a porta do contêiner de serviço. O número da porta exibido não precisa corresponder ao número da porta de serviço.
    - Pare o programa que está usando a mesma porta.

2. Uma porta publicada que é especificada pelas configurações de implementação não é um número de porta válido. Os números de porta devem ser um número no intervalo de 1 a 65535.
3. Um nome de volume nas configurações de implementação não é um caminho de arquivo válido. Os caminhos de volume devem ser especificados pelos seus caminhos absolutos (não relativos). 

### Erro interno do TLS do cluster de borda do OCP

  ```
  Error from server: error dialing backend: remote error: tls: internal error
  ```
  {: codeblock} 

Se você vir esse erro no término do processo de instalação do agente de cluster ou ao tentar interagir com o pod do agente, poderá haver um problema com as solicitações de assinatura de certificado (CSR) de seu cluster do OCP. 

1. Verifique se você tem alguma CSR no estado Pendente:

    ```
    oc get csr
    ```
    {: codeblock} 

2. Aprove as CSRs pendentes:

  ```
  oc adm certificate approve <csr-name>
  ```
  {: codeblock}
    
**Nota**: é possível aprovar todas as CSRs com um comando:

  ```
  for i in `oc get csr |grep Pending |awk '{print $1}'`; do oc adm certificate approve $i; done
  ```
  {: codeblock}

### Informações adicionais

Para obter informações adicionais, consulte
  * [Resolução de problemas](../troubleshoot/troubleshooting.md)
