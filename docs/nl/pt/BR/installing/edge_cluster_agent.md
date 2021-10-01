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

# Instalando o agente
{: #importing_clusters}

**Nota**: para fazer a instalação do agente do {{site.data.keyword.ieam}} é necessário possuir acesso de administrador no cluster de borda.

Comece instalando o agente do {{site.data.keyword.edge_notm}} em um desses tipos de clusters de borda do Kubernetes:

* [Instalando o agente no cluster de borda do {{site.data.keyword.ocp}} Kubernetes](#install_kube)
* [Instalando o agente nos clusters de borda k3s e microk8s](#install_lite)

Em seguida, implemente um serviço de borda no cluster de borda:

* [Implementando serviços em seu cluster de borda](#deploying_services)

Caso seja necessário remover o agente:

* [Removendo o agente do cluster de borda](../using_edge_services/removing_agent_from_cluster.md)

## Instalando o agente em um cluster de borda do {{site.data.keyword.ocp}} Kubernetes
{: #install_kube}

Este conteúdo descreve como instalar o agente do {{site.data.keyword.ieam}} no cluster de borda do {{site.data.keyword.ocp}}. Execute estas etapas em um host que tenha acesso de administrador ao cluster de borda:

1. Efetue login no cluster de borda como **admin**:

   ```bash
   oc login https://<api_endpoint_host>:<port> -u <admin_user> -p <admin_password> --insecure-skip-tls-verify=true
   ```
   {: codeblock}

2. Se você não tiver concluído as etapas em [Criando sua chave API](../hub/prepare_for_edge_nodes.md), faça isso agora. Esse processo cria uma chave de API, localiza alguns arquivos e reúne os valores de variáveis de ambiente necessários para a configuração de nós de borda. Configure as mesmas variáveis de ambiente neste cluster de borda:

  ```bash
  export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>   export HZN_ORG_ID=<your-exchange-organization>   export HZN_FSS_CSSURL=https://<ieam-management-hub-ingress>/edge-css/
  ```
  {: codeblock}

3. Configure a variável de namespace do agente como seu valor padrão (ou de qualquer namespace no qual você deseja instalar explicitamente o agente):

   ```bash
   export AGENT_NAMESPACE=openhorizon-agent
   ```
   {: codeblock}

4. Configure a classe de armazenamento que você deseja que o agente use, seja uma classe de armazenamento integrada ou uma que você criou. É possível visualizar as classes de armazenamento disponíveis com o primeiro dos dois comandos a seguir e, em seguida, substituir o nome daquele que você deseja usar no segundo comando. Uma classe de armazenamento deve ser rotulada `(default)`:

   ```bash
   oc get storageclass    export EDGE_CLUSTER_STORAGE_CLASS=<rook-ceph-cephfs-internal>
   ```
   {: codeblock}

5. Determine se uma rota padrão para o registro de imagem do {{site.data.keyword.open_shift}} foi criada para que ela seja acessível de fora do cluster:

   ```bash
   oc get route default-route -n openshift-image-registry --template='{{ .spec.host }}'
   ```
   {: codeblock}

   Se a resposta de comando indicar que **default-route** não foi localizado, será necessário expô-lo (consulte [Expondo o registro](https://docs.openshift.com/container-platform/4.6/registry/securing-exposing-registry.html) para obter detalhes):

   ```bash
   oc patch configs.imageregistry.operator.openshift.io/cluster --patch '{"spec":{"defaultRoute":true}}' --type=merge
   ```
   {: codeblock}

6. Recupere o nome da rota do repositório que precisa ser usada:

   ```bash
   export OCP_IMAGE_REGISTRY=`oc get route default-route -n openshift-image-registry --template='{{ .spec.host }}'`
   ```
   {: codeblock}

7. Crie um novo projeto para armazenar as suas imagens:

   ```bash
   export OCP_PROJECT=$AGENT_NAMESPACE    oc new-project $OCP_PROJECT
   ```
   {: codeblock}

8. Crie uma conta de serviço com um nome de sua escolha:

   ```bash
   export OCP_USER=<service-account-name>    oc create serviceaccount $OCP_USER
   ```
   {: codeblock}

9. Inclua uma função em sua conta de serviço para o projeto atual:

   ```bash
   oc policy add-role-to-user edit system:serviceaccount:$OCP_PROJECT:$OCP_USER
   ```
   {: codeblock}

10. Configure o seu token de conta do serviço para a variável de ambiente a seguir:

   ```bash
   export OCP_TOKEN=`oc serviceaccounts get-token $OCP_USER`
   ```
   {: codeblock}

11. Obter o certificado do {{site.data.keyword.open_shift}} e permitir que o Docker confie nele:

   ```bash
   echo | openssl s_client -connect $OCP_IMAGE_REGISTRY:443 -showcerts | sed -n "/-----BEGIN CERTIFICATE-----/,/-----END CERTIFICATE-----/p" > ca.crt
   ```
   {: codeblock}

   No {{site.data.keyword.linux_notm}}:

   ```bash
   mkdir -p /etc/docker/certs.d/$OCP_IMAGE_REGISTRY    cp ca.crt /etc/docker/certs.d/$OCP_IMAGE_REGISTRY    systemctl restart docker.service
   ```
   {: codeblock}

   No {{site.data.keyword.macOS_notm}}:

   ```bash
   mkdir -p ~/.docker/certs.d/$OCP_IMAGE_REGISTRY    cp ca.crt ~/.docker/certs.d/$OCP_IMAGE_REGISTRY
   ```
   {: codeblock}

   No {{site.data.keyword.macOS_notm}}, use o ícone de área de trabalho do Docker no lado direito da barra de menu da área de trabalho para reiniciar o Docker clicando em **Reiniciar** no menu suspenso.

12. Efetue login no host Docker do {{site.data.keyword.ocp}}:

   ```bash
   echo "$OCP_TOKEN" | docker login -u $OCP_USER --password-stdin $OCP_IMAGE_REGISTRY
   ```
   {: codeblock}

13. Configure armazenamentos confiáveis adicionais para acesso de registro de imagem:   

    ```bash
    oc create configmap registry-config --from-file=$OCP_IMAGE_REGISTRY=ca.crt -n openshift-config
    ```
    {: codeblock}

14. Edite a nova `registry-config`:

    ```bash
    oc edit image.config.openshift.io cluster
    ```
    {: codeblock}

15. Atualize a seção `spec:`:

    ```bash
    spec:       additionalTrustedCA:        name: registry-config
    ```
    {: codeblock}

16. O script **agent-install.sh** armazena o agente do {{site.data.keyword.ieam}} no registro de contêiner do cluster de borda. Configure o usuário de registro, a senha e o caminho completo da imagem (menos a tag):

   ```bash
   export EDGE_CLUSTER_REGISTRY_USERNAME=$OCP_USER    export EDGE_CLUSTER_REGISTRY_TOKEN="$OCP_TOKEN"    export IMAGE_ON_EDGE_CLUSTER_REGISTRY=$OCP_IMAGE_REGISTRY/$OCP_PROJECT/amd64_anax_k8s
   ```
   {: codeblock}

   **Nota**: a imagem do agente {{site.data.keyword.ieam}} é armazenada no registro do cluster de borda local porque o cluster de borda Kubernetes precisa de acesso contínuo a ela, caso seja necessário reiniciá-la ou movê-la para outro pod.

17. Faça download do script **agent-install.sh** em Cloud Sync Service (CSS) e torne-o executável:

   ```bash
   curl -u "$HZN_ORG_ID/$HZN_EXCHANGE_USER_AUTH" -k -o agent-install.sh $HZN_FSS_CSSURL/api/v1/objects/IBM/agent_files/agent-install.sh/data    chmod +x agent-install.sh
   ```
   {: codeblock}

18. Execute **agent-install.sh** para obter os arquivos necessários do CSS, instale e configure o agente {{site.data.keyword.horizon}}, e registre seu cluster de borda com a política:

   ```bash
   ./agent-install.sh -D cluster -i 'css:'
   ```
   {: codeblock}

   **Notas**:
   * Para ver todas as sinalizações disponíveis, execute: **./agent-install.sh -h**
   * Se houver um erro que cause a falha de **agent-install.sh**, corrija o erro e execute **agent-install.sh** novamente. Se isso não funcionar, execute **agent-uninstall.sh** (consulte [Removendo agente do cluster de borda](../using_edge_services/removing_agent_from_cluster.md)) antes de executar o **agent-install.sh** novamente.

19. Mude para o namespace do agente (também conhecido como projeto) e verifique se o pod do agente está em execução:

   ```bash
   oc project $AGENT_NAMESPACE    oc get pods
   ```
   {: codeblock}

20. Agora que o agente está instalado no cluster de borda, você pode executar estes comandos se quiser se familiarizar com os recursos do Kubernetes associados ao agente:

   ```bash
   oc get namespace $AGENT_NAMESPACE    oc project $AGENT_NAMESPACE   # ensure this is the current namespace/project    oc get deployment -o wide    oc get deployment agent -o yaml   # get details of the deployment    oc get configmap openhorizon-agent-config -o yaml    oc get secret openhorizon-agent-secrets -o yaml    oc get pvc openhorizon-agent-pvc -o yaml   # persistent volume
   ```
   {: codeblock}

21. Normalmente, quando um cluster de borda é registrado para política, mas não possui uma política de nó especificada pelo usuário, nenhuma das políticas de implementação implementará serviços de borda nele. Este é o caso com os exemplos do Horizon. Prossiga para [Implementando serviços em seu cluster de borda](#deploying_services) para configurar a política de nó para que um serviço de borda seja implementado neste cluster de borda.

## Instalando o agente nos clusters de borda k3s e microk8s
{: #install_lite}

Esse conteúdo descreve como instalar o agente {{site.data.keyword.ieam}} em [k3s](https://k3s.io/) ou [microk8s](https://microk8s.io/), clusters Kubernetes leves e pequenos:

1. Efetue login no cluster de borda como **root**.

2. Se você não tiver concluído as etapas em [Criando sua chave API](../hub/prepare_for_edge_nodes.md), faça isso agora. Esse processo cria uma chave de API, localiza alguns arquivos e reúne os valores de variáveis de ambiente necessários para a configuração de nós de borda. Configure as mesmas variáveis de ambiente neste cluster de borda:

  ```bash
  export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>   export HZN_ORG_ID=<your-exchange-organization>   export HZN_FSS_CSSURL=https://<ieam-management-hub-ingress>/edge-css/
  ```
  {: codeblock}

3. Copie o script **agent-install.sh** em seu novo cluster de borda.

4. O script **agent-install.sh** armazenará o agente {{site.data.keyword.ieam}} no registro de imagem de cluster de borda. Configure o caminho completo da imagem (menos a tag) que deve ser usado. Por exemplo:

   * No k3s:

      ```bash
      REGISTRY_ENDPOINT=$(kubectl get service docker-registry-service | grep docker-registry-service | awk '{print $3;}'):5000       export IMAGE_ON_EDGE_CLUSTER_REGISTRY=$REGISTRY_ENDPOINT/openhorizon-agent/amd64_anax_k8s
      ```
      {: codeblock}

   * No microk8s:

      ```bash
      export IMAGE_ON_EDGE_CLUSTER_REGISTRY=localhost:32000/openhorizon-agent/amd64_anax_k8s
      ```
      {: codeblock}

   **Nota**: a imagem do agente {{site.data.keyword.ieam}} é armazenada no registro do cluster de borda local porque o cluster de borda Kubernetes precisa de acesso contínuo a ela, caso seja necessário reiniciá-la ou movê-la para outro pod.

5. Instrua o **agent-install.sh** a usar a classe de armazenamento padrão:

   * No k3s:

      ```bash
      export EDGE_CLUSTER_STORAGE_CLASS=local-path
      ```
      {: codeblock}

   * No microk8s:

      ```bash
      export EDGE_CLUSTER_STORAGE_CLASS=microk8s-hostpath
      ```
      {: codeblock}

6. Execute **agent-install.sh** para obter os arquivos necessários do CSS (Cloud Sync Service), instale e configure o agente {{site.data.keyword.horizon}} e registre seu cluster de borda com política:

   ```bash
   ./agent-install.sh -D cluster -i 'css:'
   ```
   {: codeblock}

   **Notas**:
   * Para ver todas as sinalizações disponíveis, execute: **./agent-install.sh -h**
   * Se houver um erro que faça com que **agent-install.sh** não seja concluído com êxito, corrija o erro exibido e execute **agent-install.sh** novamente. Se isso não funcionar, execute **agent-uninstall.sh** (consulte [Removendo agente do cluster de borda](../using_edge_services/removing_agent_from_cluster.md)) antes de executar o **agent-install.sh** novamente.

7. Verifique se o pod do agente está em execução:

   ```bash
   kubectl get namespaces    kubectl -n openhorizon-agent get pods
   ```
   {: codeblock}

8. Geralmente, quando um cluster de borda é registrado para política, mas não possui nenhuma política de nó especificada pelo usuário, nenhuma das políticas de implementação implementará serviços de borda nele. Isso é esperado. Prossiga para [Implementando serviços em seu cluster de borda](#deploying_services) para configurar a política de nó para que um serviço de borda seja implementado neste cluster de borda.

## Implementando serviços em seu cluster de borda
{: #deploying_services}

A configuração da política de nó neste cluster de borda pode fazer com que as políticas de implementação implantem os serviços de borda aqui. Este conteúdo mostra um exemplo de como fazer isso.

1. Configure alguns aliases para que eles executem o comando `hzn` de modo mais conveniente. (O comando `hzn` está dentro do contêiner do agente, mas esses aliases permitem que o `hzn` seja executado a partir deste host).

   ```bash
   cat << 'END_ALIASES' >> ~/.bash_aliases    alias getagentpod='kubectl -n openhorizon-agent get pods --selector=app=agent -o jsonpath={.items[*].metadata.name}'    alias hzn='kubectl -n openhorizon-agent exec -i $(getagentpod) -- hzn'    END_ALIASES    source ~/.bash_aliases
   ```
   {: codeblock}

2. Verifique se o seu nó de borda está configurado (registrado com o hub de gerenciamento do {{site.data.keyword.ieam}}):

   ```bash
   hzn node list
   ```
   {: codeblock}

3. Para testar o agente de cluster de borda, configure a política de nó com uma propriedade que implemente o operador e o serviço helloworld de exemplo neste nó de borda:

   ```bash
   cat << 'EOF' > operator-example-node.policy.json    {
     "properties":[
       { "name": "openhorizon.example", "value": "operator" }      ]
   }    EOF

   cat operator-example-node.policy.json | hzn policy update -f-    hzn policy list
   ```
   {: codeblock}

   **Nota**:
   * Como o comando **hzn** real está sendo executado dentro do contêiner do agente, para qualquer comando `hzn` que exija um arquivo de entrada, é necessário canalizar o arquivo no comando para que seu conteúdo seja transferido para o contêiner.

4. Depois de um minuto, verifique se há um acordo e se o operador de borda e os contêineres de serviço estão em execução:

   ```bash
   hzn agreement list    kubectl -n openhorizon-agent get pods
   ```
   {: codeblock}

5. Usando os IDs de pod do comando anterior, visualize o log do operador e do serviço de borda:

   ```bash
   kubectl -n openhorizon-agent logs -f <operator-pod-id>    # control-c to get out    kubectl -n openhorizon-agent logs -f <service-pod-id>    # control-c to get out
   ```
   {: codeblock}

6. Também é possível visualizar as variáveis de ambiente que o agente transmite para o serviço de borda:

   ```bash
   kubectl -n openhorizon-agent exec -i <service-pod-id> -- env | grep HZN_
   ```
   {: codeblock}

### Mudando quais serviços são implementados em seu cluster de borda
{: #changing_services}

* Para mudar quais serviços são implementados em seu cluster de borda, mude a política de nó:

  ```bash
  cat <new-node-policy>.json | hzn policy update -f-   hzn policy list
  ```
  {: codeblock}

   Após um minuto ou dois, os novos serviços serão implementados neste cluster de borda.

* **Nota**: em algumas MVs que possuem microk8s, os pods de serviço que estão sendo interrompidos (substituídos) podem travar no estado **Terminating**. Se isso acontecer, execute:

  ```bash
  kubectl delete pod <pod-id> -n openhorizon-agent --force --grace-period=0   pkill -fe <service-process>
  ```
  {: codeblock}

* Se você deseja usar um padrão, em vez de uma política, para executar serviços em seu cluster de borda:

  ```bash
  hzn unregister -f   hzn register -n $HZN_EXCHANGE_NODE_AUTH -p <pattern-name>
  ```
  {: codeblock}
