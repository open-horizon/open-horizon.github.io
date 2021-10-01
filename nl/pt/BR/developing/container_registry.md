---

copyright:
years: 2019, 2020
lastupdated: "2020-01-22"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Usando um registro de contêiner privado
{: #container_registry}

Caso uma imagem de serviço de borda inclua ativos não adequados para serem incluídos em um registro público, é possível usar um registro de contêiner privado do Docker, por exemplo, o Registro de imagem do {{site.data.keyword.open_shift}} ou o {{site.data.keyword.ibm_cloud}} Container Registry, em que o acesso é rigidamente controlado.
{:shortdesc}

Caso ainda não tenha feito isso, siga as etapas em [Desenvolvendo um serviço de borda para dispositivos](../OH/docs/developing/developing.md) para criar e implementar pelo menos um serviço de borda de exemplo, assegurando que você se familiarize com o processo básico.

Esta página descreve dois registros nos quais é possível armazenar imagens do serviço de borda:
* [Usando o registro de imagens do {{site.data.keyword.open_shift}}](#ocp_image_registry)
* [Usando o {{site.data.keyword.cloud_notm}} Container Registry](#ibm_cloud_container_registry)

Eles também servem como exemplo de como é possível usar qualquer registro de imagem privado com o {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}).

## Usando o registro de imagens do {{site.data.keyword.open_shift}}
{: #ocp_image_registry}

### Antes de Começar

* Se você ainda não fez isso, instale os comandos da [CLI do IBM Cloud Pak (**cloudctl**) e da CLI do cliente OpenShift (**oc**)](../cli/cloudctl_oc_cli.md).

**Nota**: Uma vez que o registro local geralmente tem um disco menor, ele pode preencher rapidamente. Em alguns casos, isso pode afetar negativamente o hub de gerenciamento ao ponto que ele pode se tornar não funcional. Devido a isso, considere utilizar registros locais de imagem do {{site.data.keyword.open_shift}} apenas se o monitoramento preventivo estiver implementado em seu ambiente; caso contrário, use registros externos de imagem.

### Procedimento

**Nota**: para obter mais informações sobre a sintaxe de comando, consulte [Convenções usadas neste documento](../getting_started/document_conventions.md).

1. Assegure-se de estar conectado ao seu cluster do {{site.data.keyword.open_shift}} com privilégios de administrador de cluster.

   ```bash
   cloudctl login -a <cluster-url> -u <user> -p <password> -n kube-system --skip-ssl-validation
   ```
   {: codeblock}

2. Determine se uma rota padrão para o registro de imagem do {{site.data.keyword.open_shift}} foi criada de modo que fique acessível de fora do cluster:

   ```bash
   oc get route default-route -n openshift-image-registry --template='{{ .spec.host }}'
   ```
   {: codeblock}

   Se a resposta de comandos indicar que o **default-route** não foi localizado, crie-o (consulte [Expondo o registro](https://docs.openshift.com/container-platform/4.6/registry/securing-exposing-registry.html) para obter detalhes):

   ```bash
   oc patch configs.imageregistry.operator.openshift.io/cluster --patch '{"spec":{"defaultRoute":true}}' --type=merge
   ```
   {: codeblock}

3. Recupere o nome da rota do repositório que precisa ser usada:

   ```bash
   export OCP_DOCKER_HOST=`oc get route default-route -n openshift-image-registry --template='{{ .spec.host }}'`
   ```
   {: codeblock}

4. Crie um novo projeto no qual armazenar as imagens:

   ```bash
   export OCP_PROJECT=<your-new-project>    oc new-project $OCP_PROJECT
   ```
   {: codeblock}

5. Crie uma conta de serviço com um nome de sua escolha:

   ```bash
   export OCP_USER=<service-account-name>    oc create serviceaccount $OCP_USER
   ```
   {: codeblock}

6. Inclua uma função em sua conta de serviço para o projeto atual:

   ```bash
   oc policy add-role-to-user edit system:serviceaccount:$OCP_PROJECT:$OCP_USER
   ```
   {: codeblock}

7. Obtenha o token designado à sua conta de serviço:

   ```bash
   export OCP_TOKEN=`oc serviceaccounts get-token $OCP_USER`
   ```
   {: codeblock}

8. Obtenha o certificado do {{site.data.keyword.open_shift}} e faça com que o Docker confie nele:

   ```bash
   echo | openssl s_client -connect $OCP_DOCKER_HOST:443 -showcerts | sed -n "/-----BEGIN CERTIFICATE-----/,/-----END CERTIFICATE-----/p" > ca.crt
   ```
   {: codeblock}

   No {{site.data.keyword.linux_notm}}:

   ```bash
   mkdir -p /etc/docker/certs.d/$OCP_DOCKER_HOST    cp ca.crt /etc/docker/certs.d/$OCP_DOCKER_HOST    systemctl restart docker.service
   ```
   {: codeblock}

   No {{site.data.keyword.macOS_notm}}:

   ```bash
   mkdir -p ~/.docker/certs.d/$OCP_DOCKER_HOST    cp ca.crt ~/.docker/certs.d/$OCP_DOCKER_HOST
   ```
   {: codeblock}

   No {{site.data.keyword.macOS_notm}}, clique no ícone de baleia no lado direito da barra de menu da área de trabalho e selecione **Reiniciar** para reiniciar o Docker.

9. Efetue login no host Docker do {{site.data.keyword.ocp}}:

   ```bash
   echo "$OCP_TOKEN" | docker login -u $OCP_USER --password-stdin $OCP_DOCKER_HOST
   ```
   {: codeblock}

10. Configure armazenamentos confiáveis adicionais para acesso de registro de imagem:   

    ```bash
    oc create configmap registry-config --from-file=<external-registry-address>=ca.crt -n openshift-config
    ```
    {: codeblock}

11. Edite a nova `registry-config`:

    ```bash
    oc edit image.config.openshift.io cluster
    ```
    {: codeblock}

12. Atualize a seção `spec:` com as linhas a seguir:

    ```bash
    spec:       additionalTrustedCA:        name: registry-config
    ```
    {: codeblock}

13. Construa a imagem com este formato de caminho, por exemplo:

   ```bash
   export BASE_IMAGE_NAME=myservice    docker build -t $OCP_DOCKER_HOST/$OCP_PROJECT/${BASE_IMAGE_NAME}_amd64:1.2.3 -f ./Dockerfile.amd64 .
   ```
   {: codeblock}

14. Na preparação para a publicação do serviço de borda, modifique o arquivo **service.definition.json**, para que a seção **deployment** faça referência ao caminho do registro de imagens. É possível criar arquivos de definição de serviço e de padrão como este usando:

   ```bash
   hzn dev service new -s $BASE_IMAGE_NAME -i $OCP_DOCKER_HOST/$OCP_PROJECT/$BASE_IMAGE_NAME
   ```
   {: codeblock}

   O **&lt;base-image-name&gt;** deve ser o nome da imagem base, sem o arco ou a versão. Em seguida, é possível editar as variáveis no arquivo **horizon/hzn.json** criado, conforme necessário.

   Ou, caso tenha criado seu próprio arquivo de definição de serviço, assegure-se de que o campo **deployment.services.&lt;service-name&gt;.image** faça referência ao caminho do registro de imagem.

15. Quando a imagem de serviço estiver pronta para ser publicada, envie-a por push para o registro de contêiner privado e publique a imagem no {{site.data.keyword.horizon}} Exchange:

   ```bash
   hzn exchange service publish -r "$OCP_DOCKER_HOST:$OCP_USER:$OCP_TOKEN" -f horizon/service.definition.json
   ```
   {: codeblock}

   O argumento **-r "$OCP_DOCKER_HOST:$OCP_USER:$OCP_TOKEN"** fornece aos nós de borda do {{site.data.keyword.horizon_open}} as credenciais para fazer pull da imagem do serviço.

   O comando executa estas tarefas:

   * Envia as imagens do Docker por push para o {{site.data.keyword.cloud_notm}} Container Registry e compila a imagem no processo.
   * Assina a compilação e as informações de implementação com sua chave privada.
   * Coloca os metadados do serviço (incluindo a assinatura) no {{site.data.keyword.horizon}} Exchange.
   * Coloca a chave pública no {{site.data.keyword.horizon}} Exchange sob a definição de serviço, para que os nós de borda do {{site.data.keyword.horizon}} possam recuperar automaticamente a definição para verificar as assinaturas quando necessário.
   * Coloca o usuário e o token do OpenShift no {{site.data.keyword.horizon}} Exchange sob a definição de serviço, para que os nós de borda do {{site.data.keyword.horizon}} possam recuperar automaticamente a definição quando necessário.
   
### Usando o serviço nos nós de borda do {{site.data.keyword.horizon}}
{: #using_service}

Para que os nós de borda possam puxar as imagens de serviço necessárias a partir do registro de imagens do {{site.data.keyword.ocp}}, deve-se configurar o Docker em cada nó de borda para confiar no certificado do {{site.data.keyword.open_shift}}. Copie o arquivo **ca.crt** para cada nó de borda e, em seguida:

No {{site.data.keyword.linux_notm}}:

```bash
mkdir -p /etc/docker/certs.d/$OCP_DOCKER_HOST    cp ca.crt /etc/docker/certs.d/$OCP_DOCKER_HOST    systemctl restart docker.service
```
{: codeblock}

No {{site.data.keyword.macOS_notm}}:

```bash
mkdir -p ~/.docker/certs.d/$OCP_DOCKER_HOST    cp ca.crt ~/.docker/certs.d/$OCP_DOCKER_HOST
```
{: codeblock}

No {{site.data.keyword.macOS_notm}}, reinicie o Docker, clicando no ícone de baleia no lado direito da barra de menus da área de trabalho e selecionando **Reiniciar**.

Agora, o {{site.data.keyword.horizon}} tem tudo o que é necessário para obter a imagem desse serviço de borda a partir do registro de imagens do {{site.data.keyword.open_shift}} e implementá-la nos nós de borda, conforme especificado pelo padrão ou pela política de implementação criados.

## Usando o {{site.data.keyword.cloud_notm}} Container Registry
{: #ibm_cloud_container_registry}

### Antes de Começar

* Instale a [ferramenta CLI (ibmcloud) do {{site.data.keyword.cloud_notm}}](https://cloud.ibm.com/docs/cli?topic=cloud-cli-install-ibmcloud-cli).
* Assegure-se de ter o nível de acesso **Administrador de cluster** ou **Administrador de equipe** em sua conta do {{site.data.keyword.cloud_notm}}.

### Procedimento

1. Efetue login no {{site.data.keyword.cloud_notm}}, visando sua organização:

   ```bash
   ibmcloud login -a cloud.ibm.com -u <cloud-username> -p <cloud-password    ibmcloud target -o <organization-id> -s <space-id>
   ```
   {: codeblock}

   Se você não souber seu ID de organização e ID de espaço, será possível efetuar login no [console do {{site.data.keyword.cloud_notm}}](https://cloud.ibm.com/) ou criá-los.

2. Crie uma chave de API de nuvem:

   ```bash
   ibmcloud iam api-key-create <key-name> -d "<key-description>"
   ```
   {: codeblock}

   Salve o valor da chave de API (exibido na linha que começa com **Chave API**) em um local seguro e configure-o nesta variável de ambiente:

   ```bash
   export CLOUD_API_KEY=<your-cloud-api-key>
   ```
   {: codeblock}

   **Nota**: esta chave de API é diferente da chave de API do {{site.data.keyword.open_shift}} que você criou para usar com o comando `hzn`.

3. Obtenha o plug-in container-registry e crie seu namespace de registro privado. (Este namespace de registro fará parte do caminho usado para identificar sua imagem do Docker.)

   ```bash
   ibmcloud plugin install container-registry    export REGISTRY_NAMESPACE=<your-registry-namespace>    ibmcloud cr namespace-add $REGISTRY_NAMESPACE
   ```
   {: codeblock}

4. Efetue login no namespace de registro do Docker:

   ```bash
   ibmcloud cr login
   ```
   {: codeblock}

   Para obter mais informações sobre o uso do **ibmcloud cr**, consulte [Documentação da web CLI ibmcloud cr](https://cloud.ibm.com/docs/services/Registry/). Adicionalmente, é possível executar este comando para visualizar informações de ajuda:

   ```bash
   ibmcloud cr --help
   ```
   {: codeblock}

   Depois de efetuar login em seu namespace privado no {{site.data.keyword.cloud_registry}}, não é necessário usar `docker login` para efetuar login no registro. É possível usar caminhos de registro de contêiner semelhantes ao seguinte dentro dos comandos **docker push** e **docker pull**:

   ```bash
   us.icr.io/$REGISTRY_NAMESPACE/<base-image-name>_<arch>:<version>
   ```
   {: codeblock}

5. Construa a imagem com este formato de caminho, por exemplo:

   ```bash
   export BASE_IMAGE_NAME=myservice    docker build -t us.icr.io/$REGISTRY_NAMESPACE/${BASE_IMAGE_NAME}_amd64:1.2.3 -f ./Dockerfile.amd64 .
   ```
   {: codeblock}

6. Na preparação para a publicação do serviço de borda, modifique o arquivo **service.definition.json**, para que a seção **deployment** faça referência ao caminho do registro de imagens. É possível criar arquivos de definição de serviço e de padrão como este usando:

   ```bash
   hzn dev service new -s $BASE_IMAGE_NAME -i us.icr.io/$REGISTRY_NAMESPACE/$BASE_IMAGE_NAME
   ```
   {: codeblock}

   O **&lt;base-image-name&gt;** deve ser o nome da imagem base, sem o arco ou a versão. Em seguida, é possível editar as variáveis no arquivo **horizon/hzn.json** criado, conforme necessário.

   Ou, caso tenha criado seu próprio arquivo de definição de serviço, assegure-se de que o campo **deployment.services.&lt;service-name&gt;.image** faça referência ao caminho do registro de imagem.

7. Quando a imagem de serviço estiver pronta para ser publicada, envie-a por push para o registro de contêiner privado e publique a imagem no {{site.data.keyword.horizon}} Exchange:

   ```bash
   hzn exchange service publish -r "us.icr.io:iamapikey:$CLOUD_API_KEY" -f horizon/service.definition.json
   ```
   {: codeblock}

   O argumento **-r "us.icr.io:iamapikey:$CLOUD_API_KEY"** fornece aos nós de borda do {{site.data.keyword.horizon_open}} as credenciais que permitem fazer pull da imagem de serviço.

   O comando executa estas tarefas:

   * Envia as imagens do Docker por push para o {{site.data.keyword.cloud_notm}} Container Registry e compila a imagem no processo.
   * Assina a compilação e as informações de implementação com sua chave privada.
   * Coloca os metadados do serviço (incluindo a assinatura) no {{site.data.keyword.horizon}} Exchange.
   * Coloca a chave pública no {{site.data.keyword.horizon}} Exchange sob a definição de serviço, para que os nós de borda do {{site.data.keyword.horizon}} possam recuperar automaticamente a definição para verificar as assinaturas quando necessário.
   * Coloca a chave de API do {{site.data.keyword.cloud_notm}} no {{site.data.keyword.horizon}} Exchange sob a definição de serviço, para que os nós de borda do {{site.data.keyword.horizon}} possam recuperar automaticamente a definição quando necessário.

8. Verifique se a imagem de serviço foi enviada por push para o {{site.data.keyword.cloud_notm}} Container Registry:

   ```bash
   imagens ibmcloud cr
   ```
   {: codeblock}

9. Publique um padrão ou uma política de implementação que implementará o serviço em alguns nós de borda. Por exemplo,:

   ```bash
   hzn exchange pattern publish -f horizon/pattern.json
   ```
   {: codeblock}

Agora, o {{site.data.keyword.horizon}} tem tudo o que é necessário para obter a imagem desse serviço de borda a partir do {{site.data.keyword.cloud_notm}} Container Registry e implementá-la nos nós de borda, conforme especificado pelo padrão ou pela política de implementação criados.
