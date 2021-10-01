---

copyright:
years: 2019,2020
lastupdated: "2020-01-28"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Preparando para criar um serviço de borda
{: #service_containers}

Use o {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) para desenvolver serviços dentro de contêineres do {{site.data.keyword.docker}} para seus dispositivos de borda. É possível usar qualquer {{site.data.keyword.linux_notm}} base, linguagem de programação, biblioteca ou utilitário apropriado para criar os serviços de borda.
{:shortdesc}

Depois que você enviar por push, assinar e publicar os serviços, o {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) usará agentes totalmente autônomos nos dispositivos de borda para fazer download, validar, configurar, instalar e monitorar seus serviços. 

Em geral, os serviços de borda usam os serviços de alimentação em nuvem para armazenar e processar ainda mais resultados de análise de borda. Esse processo inclui o fluxo de trabalho de desenvolvimento para código de borda e nuvem.

O {{site.data.keyword.ieam}} baseia-se no projeto open source [{{site.data.keyword.horizon_open}}](https://github.com/open-horizon/) e usa o comando `hzn` {{site.data.keyword.horizon}} {{site.data.keyword.linux_notm}} para executar alguns processos.

## Antes de Começar
{: #service_containers_begin}

1. Configure seu host de desenvolvimento para uso com o {{site.data.keyword.ieam}} instalando o agente do {{site.data.keyword.horizon}} em seu host e registre seu host com o {{site.data.keyword.horizon_exchange}}. Consulte [Instalar o agente do {{site.data.keyword.horizon}} no dispositivo de borda e registrá-lo usando o exemplo hello world](../installing/registration.md).

2. Crie um ID do [Hub do Docker](https://hub.docker.com/). Isso é necessário porque as instruções nesta seção incluem publicar a imagem de contêiner de serviço para o Docker Hub.

## Procedimento
{: #service_containers_procedure}

**Nota**: consulte [Convenções usadas neste documento](../getting_started/document_conventions.md) para obter mais informações sobre sintaxe de comando.

1. Depois de executar as etapas em [Instalar o agente do {{site.data.keyword.horizon}} no dispositivo de borda e registrá-lo usando o exemplo hello world](../installing/registration.md), configure as credenciais do Exchange. Confirme se as suas credenciais ainda estão configuradas corretamente verificando se este comando não exibe um erro:

  ```
  hzn exchange user list
  ```
  {: codeblock}

2. Se você estiver usando o {{site.data.keyword.macOS_notm}} como seu host de desenvolvimento, coloque suas credenciais de registro do hub do Docker em `~/.docker/plaintext-passwords.json`:

  ```
  export DOCKER_HUB_ID="&amp;TWBLT;yourdockerhubid&gt;"   export DOCKER_HUB_PW="&amp;TWBLT;yourdockerhubpassword&gt;"   echo "{ \"auths\": { \"https://index.docker.io/v1/\": { \"auth\": \"$(printf "${DOCKER_HUB_ID:?}:${DOCKER_HUB_PW:?}" | base64)\" } } }" &gt; ~/.docker/plaintext-passwords.json

  ```
  {: codeblock}

3. Efetue login no Docker Hub com o ID do Docker Hub que você criou anteriormente:

  ```
  export DOCKER_HUB_ID="&amp;TWBLT;yourdockerhubid&gt;"   export DOCKER_HUB_PW="&amp;TWBLT;yourdockerhubpassword&gt;"   echo "$DOCKER_HUB_PW" | docker login -u $DOCKER_HUB_ID --password-stdin
  ```
  {: codeblock}

  Exemplo de saída:
  ```
  WARNING! Your password will be stored unencrypted in ~userName/.docker/config.json.
  Configure a credential helper to remove this warning. See     https://docs.docker.com/engine/reference/commandline/login/#credentials-store

  O login foi efetuado com sucesso
  ```

4. Crie um par de chaves de assinatura criptográfica. Isso permite que você assine os serviços ao publicá-los no Exchange. 

   **Nota**: essa etapa só precisa ser executada uma vez.

  ```
  hzn key create "<companyname>" "<youremailaddress>"
  ```
  {: codeblock}
  
  Em que `companyname` é usado como a organização x509 e `youremailaddress` é usado como o x509 CN.

5. Instale algumas ferramentas de desenvolvimento:

  Em **{{site.data.keyword.linux_notm}}** (para distribuições Ubuntu/Debian):

  ```
  sudo apt install -y git jq make
  ```
  {: codeblock}

  No **{{site.data.keyword.macOS_notm}}**:

  ```
  brew install git jq make
  ```
  {: codeblock}
  
  **Nota**: consulte [homebrew](https://brew.sh/) para obter detalhes sobre a instalação de brew se necessário.

## O que fazer em seguida
{: #service_containers_what_next}

* Use as suas credenciais e a chave de assinatura para concluir os [exemplos de desenvolvimento](../OH/docs/developing/developing.md). Esses exemplos mostram como construir serviços de borda simples e aprender os fundamentos do desenvolver para {{site.data.keyword.edge_notm}}.
* Se você já tiver uma imagem do Docker na qual queira que o {{site.data.keyword.edge_notm}} implemente os nós da borda, consulte [Transformar uma imagem em um serviço de borda](transform_image.md).
