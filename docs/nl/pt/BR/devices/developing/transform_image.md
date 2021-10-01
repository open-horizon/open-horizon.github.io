---

copyright:
years: 2020
lastupdated: "2020-04-09"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Transformar imagem em serviço de borda
{: #transform_image}

Este exemplo orienta você por meio das etapas para publicar uma imagem do Docker existente como um serviço de borda, criar um padrão de implementação associado e registrar seus nós de borda para executar esse padrão de implementação.
{:shortdesc}

## Antes de iniciar
{: #quickstart_ex_begin}

Conclua as etapas de pré-requisito em [Preparando para criar um serviço de borda](service_containers.md). Como resultado, estas variáveis de ambiente devem ser configuradas, estes comandos devem ser instalados e estes arquivos devem existir:

```bash
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID"
which git jq
ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem
cat /etc/default/horizon
```
{: codeblock}

## Procedimento
{: #quickstart_ex_procedure}

Nota: consulte [Convenções usadas neste documento](../../getting_started/document_conventions.md) para obter mais informações sobre a sintaxe de comando.

1. Crie um diretório de projeto.

  1. Em seu host de desenvolvimento, mude para o diretório do projeto do Docker existente. **Se você não tiver um projeto do Docker existente, mas ainda assim desejar continuar com este exemplo**, use estes comandos para criar um Dockerfile simples que possa ser usado com o restante deste procedimento:

    ```bash
    cat << EndOfContent > Dockerfile
    FROM alpine:latest
    CMD while :; do echo "Hello, world."; sleep 3; done
    EndOfContent
    ```
    {: codeblock}

  2. Crie metadados de serviço de borda para o seu projeto:

    ```bash
    hzn dev service new -s myservice -V 1.0.0 -i $DOCKER_HUB_ID/myservice --noImageGen
    ```
    {: codeblock}

    Este comando cria **horizon/service.definition.json** para descrever seu serviço e **horizon/pattern.json** para descrever o padrão de implementação. É possível abrir esses arquivos e navegar no conteúdo.

2. Construa e teste seu serviço.

  1. Construa sua imagem do Docker.
     O nome da imagem deve corresponder ao que é referenciado em **horizon/service.definition.json**.

    ```bash
    eval $(hzn util configconv -f horizon/hzn.json)
    export ARCH=$(hzn architecture)
    sudo docker build -t "${DOCKER_IMAGE_BASE}_$ARCH:$SERVICE_VERSION" .
    unset DOCKER_IMAGE_BASE SERVICE_NAME SERVICE_VERSION
    ```
    {: codeblock}

  2. Execute esta imagem de contêiner de serviço no ambiente do agente simulado do {{site.data.keyword.horizon}}:

    ```bash
    hzn dev service start -S
    ```
    {: codeblock}

  3. Verifique se o contêiner de serviço está em execução:

    ```bash
    sudo docker ps
    ```
    {: codeblock}

  4. Visualize as variáveis de ambiente que foram passadas para o contêiner quando ele foi iniciado. (Estas são as mesmas variáveis de ambiente que o agente completo transmite para o contêiner de serviço).

    ```bash
    sudo docker inspect $(sudo docker ps -q --filter name=myservice) | jq '.[0].Config.Env'
    ```
    {: codeblock}

  5. Visualize o log do contêiner de serviço:

    No **{{site.data.keyword.linux_notm}}**:

    ```bash
    sudo tail -f /var/log/syslog | grep myservice[[]
    ```
    {: codeblock}

    No **{{site.data.keyword.macOS_notm}}**:

    ```bash
    sudo docker logs -f $(sudo docker ps -q --filter name=myservice)
    ```
    {: codeblock}

  6. Pare o serviço:

    ```bash
    hzn dev service stop
    ```
    {: codeblock}

3. Publique o serviço no {{site.data.keyword.edge_devices_notm}}. Agora que você verificou que o código de serviço é executado conforme o esperado no ambiente do agente simulado, publique o serviço no {{site.data.keyword.horizon_exchange}} para disponibilizá-lo para implementação nos nós de borda.

  O comando **publish** a seguir usa o arquivo **horizon/service.definition.json** e seu par de chaves para assinar e publicar o serviço no {{site.data.keyword.horizon_exchange}}. Ele também envia por push a imagem para o Docker Hub.

  ```bash
  hzn exchange service publish -f horizon/service.definition.json
  hzn exchange service list
  ```
  {: codeblock}

4. Publique um padrão de implementação para o serviço. Este padrão de implementação pode ser usado por nós de borda para fazer com que o {{site.data.keyword.edge_devices_notm}} implemente o serviço para eles:

  ```bash
  hzn exchange pattern publish -f horizon/pattern.json
    hzn exchange pattern list
  ```
  {: codeblock}

5. Registre seu nó de borda para executar seu padrão de implementação.

  1. Da mesma forma que você anteriormente registrou os nós de borda com padrões de implementação públicos da organização **IBM**, registre o seu nó de borda com o padrão de implementação que você publicou sob sua própria organização:

    ```bash
    hzn register -p pattern-myservice-$(hzn architecture) -s myservice --serviceorg $HZN_ORG_ID
    ```
    {: codeblock}

  2. Liste o serviço de borda do contêiner do Docker que foi iniciado como resultado:

    ```bash
    sudo docker ps
    ```
    {: codeblock}

  3. Visualize a saída do serviço de borda myservice:

    ```bash
    sudo hzn service log -f myservice
    ```
    {: codeblock}

6. Visualize o nó, o serviço e o padrão que você criou no console do {{site.data.keyword.edge_devices_notm}}. É possível exibir a URL do console com:

  ```bash
  echo "$(awk -F '=|edge-exchange' '/^HZN_EXCHANGE_URL/ {print $2}' /etc/default/horizon)edge"
  ```
  {: codeblock}

7. Cancele o registro do nó de borda e pare o serviço **myservice**:

  ```bash
  hzn unregister -f
  ```
  {: codeblock}

## O que fazer a seguir
{: #quickstart_ex_what_next}

* Tente outros exemplos de serviço de borda em [Desenvolvendo serviços de borda com {{site.data.keyword.edge_devices_notm}}](developing.md).
