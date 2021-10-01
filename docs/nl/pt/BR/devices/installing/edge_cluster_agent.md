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

Inicie instalando o agente {{site.data.keyword.edge_notm}} em um desses tipos de clusters de borda do Kubernetes:

* [Instalando o agente no cluster de borda do {{site.data.keyword.ocp}} Kubernetes](#install_kube)
* [Instalando o agente nos clusters de borda k3s e microk8s](#install_lite)

Em seguida, implemente um serviço de borda em seu cluster de borda:

* [Implementando serviços em seu cluster de borda](#deploying_services)

Caso seja necessário remover o agente:

* [Removendo o agente do cluster de borda](#remove_agent)

## Instalando o agente em um cluster de borda do {{site.data.keyword.ocp}} Kubernetes
{: #install_kube}

Esta seção descreve como instalar o agente {{site.data.keyword.ieam}} em seu cluster de borda do {{site.data.keyword.ocp}}. Siga estas etapas em um host que tenha acesso de administrador ao cluster de borda:

1. Efetue login no cluster de borda como **admin**:

   ```bash
	oc login https://<API_ENDPOINT_HOST>:<PORT> -u <ADMIN_USER> -p <ADMIN_PASSWORD> --insecure-skip-tls-verify=true
   ```
   {: codeblock}

2. Configure a variável de namespace do agente como seu valor padrão (ou de qualquer namespace no qual você deseja instalar explicitamente o agente):

   ```bash
   export AGENT_NAMESPACE=openhorizon-agent
   ```
   {: codeblock}

3. Configure a classe de armazenamento que você deseja que o agente use para uma classe de armazenamento integrada ou para uma que você criou. Por exemplo:

   ```bash
   export EDGE_CLUSTER_STORAGE_CLASS=rook-ceph-cephfs-internal
   ```
   {: codeblock}

4. Para configurar o registro da imagem em seu cluster de borda, execute as etapas de 2 a 8 de [Usando o registro de imagem do OpenShift](../developing/container_registry.md##ocp_image_registry) com esta mudança: na etapa 4, configure **OCP_PROJECT** para: **$AGENT_NAMESPACE**.

5. O script **agent-install.sh** armazenará o agente {{site.data.keyword.ieam}} no registro de contêiner de cluster de borda. Configure o usuário de registro, a senha e o caminho completo da imagem (menos a tag) que devem ser usados:

   ```bash
   export EDGE_CLUSTER_REGISTRY_USERNAME=$OCP_USER
   export EDGE_CLUSTER_REGISTRY_TOKEN="$OCP_TOKEN"
   export IMAGE_ON_EDGE_CLUSTER_REGISTRY=$OCP_DOCKER_HOST/$OCP_PROJECT/amd64_anax_k8s
   ```
   {: codeblock}

   **Nota:** a imagem do agente {{site.data.keyword.ieam}} é armazenada no registro de cluster de borda local, porque o Kubernetes do cluster de borda precisa continuar o acesso a ele, caso em que ele precisa reiniciá-lo ou movê-lo para o pod.

6. Exporte suas credenciais de usuário do Horizon Exchange:

   ```bash
   export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
   ```
   {: codeblock}

7. Obtenha o arquivo **agentInstallFiles-x86_64-Cluster.tar.gz** e uma chave de API de seu administrador. Estes já deveriam ter sido criados em [Reúna as informações e os arquivos necessários para clusters de borda](preparing_edge_cluster.md).  

8. Extraia o script **agent-install.sh** a partir do arquivo tar:

   ```bash
   tar -zxvf agentInstallFiles-x86_64-Cluster.tar.gz agent-install.sh
   ```
   {: codeblock}

9. Execute o comando **agent-install.sh** para instalar e configurar o agente Horizon e registrar o cluster de borda na política:

   ```bash
   ./agent-install.sh -D cluster -z agentInstallFiles-x86_64-Cluster.tar.gz -d <node-id>
   ```
   {: codeblock}

   ** Notas: **
   * Para ver todas as sinalizações disponíveis, execute: **./agent-install.sh -h**
   * Caso ocorra um erro que impeça a conclusão de **agent-install.sh**, execute **agent-uninstall.sh** (consulte [Removendo o agente do cluster de borda](#remove_agent)) e, em seguida, repita as etapas nesta seção.

10. Mude para o namespace ou projeto do agente e verifique se o pod do agente está em execução:

   ```bash
   oc project $AGENT_NAMESPACE
   oc get pods
   ```
   {: codeblock}

11. Agora que o agente está instalado em seu cluster de borda, é possível executar estes comandos se você deseja familiarizar-se com os recursos do Kubernetes associados ao agente:

   ```bash
   oc get namespace $AGENT_NAMESPACE
   oc project $AGENT_NAMESPACE   # ensure this is the current namespace/project
   oc get deployment -o wide
   oc get deployment agent -o yaml   # get details of the deployment
   oc get configmap openhorizon-agent-config -o yaml
   oc get secret openhorizon-agent-secrets -o yaml
   oc get pvc openhorizon-agent-pvc -o yaml   # persistent volume
   ```
   {: codeblock}

12. Frequentemente, quando um cluster de borda é registrado para a política, mas não tem nenhuma política de nó especificada pelo usuário, nenhuma das políticas de implementação implantarão os serviços de borda nele. Este é o caso com os exemplos do Horizon. Prossiga para [Implementando serviços em seu cluster de
borda](#deploying_services) para configurar a política de nó para que um serviço de borda seja implementado neste cluster de borda.

## Instalando o agente nos clusters de borda k3s e microk8s
{: #install_lite}

Esta seção descreve como instalar o agente {{site.data.keyword.ieam}} em clusters do Kubernetes k3s ou microk8s, que são leves e pequenos:

1. Efetue login no cluster de borda como **root**.

2. Obtenha o arquivo **agentInstallFiles-x86_64-Cluster.tar.gz** e uma chave de API de seu administrador. Estes já deveriam ter sido criados em [Reúna as informações e os arquivos necessários para clusters de borda](preparing_edge_cluster.md).  

3. Extraia o script **agent-install.sh** a partir do arquivo tar:

   ```bash
   tar -zxvf agentInstallFiles-x86_64-Cluster.tar.gz agent-install.sh
   ```
   {: codeblock}

4. Exporte suas credenciais de usuário do Horizon Exchange:

   ```bash
   export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
   ```
   {: codeblock}

5. O script **agent-install.sh** armazenará o agente {{site.data.keyword.ieam}} no registro de imagem de cluster de borda. Configure o caminho completo da imagem (menos a tag) que deve ser usado. Por exemplo:

   ```bash
   export IMAGE_ON_EDGE_CLUSTER_REGISTRY=$REGISTRY_ENDPOINT/openhorizon-agent/amd64_anax_k8s
   ```
   {: codeblock}

   **Nota:** a imagem do agente {{site.data.keyword.ieam}} é armazenada no registro de cluster de borda local, porque o Kubernetes do cluster de borda precisa continuar o acesso a ele, caso em que ele precisa reiniciá-lo ou movê-lo para o pod.

6. Instrua o **agent-install.sh** a usar a classe de armazenamento padrão:

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

7. Execute o comando **agent-install.sh** para instalar e configurar o agente Horizon e registrar o cluster de borda na política:

   ```bash
   ./agent-install.sh -D cluster -z agentInstallFiles-x86_64-Cluster.tar.gz -d <node-id>
   ```
   {: codeblock}

   ** Notas: **
   * Para ver todas as sinalizações disponíveis, execute: **./agent-install.sh -h**
   * Caso haja um erro que impeça a conclusão de **agent-install.sh**, execute **agent-uninstall.sh** (consulte [Removendo o agente do cluster de borda](#remove_agent)) antes de executar **agent-install.sh** novamente.

8. Verifique se o pod do agente está em execução:

   ```bash
   kubectl get namespaces
   kubectl -n openhorizon-agent get pods
   ```
   {: codeblock}

9. Frequentemente, quando um cluster de borda é registrado para a política, mas não tem nenhuma política de nó especificada pelo usuário, nenhuma das políticas de implementação implantarão os serviços de borda nele. Este é o caso com os exemplos do Horizon. Prossiga para [Implementando serviços em seu cluster de
borda](#deploying_services) para configurar a política de nó para que um serviço de borda seja implementado neste cluster de borda.

## Implementando serviços em seu cluster de borda
{: #deploying_services}

A configuração da política de nó neste cluster de borda pode fazer com que as políticas de implementação implantem os serviços de borda aqui. Esta seção mostra um exemplo de como fazer isso.

1. Configure alguns aliases para que eles executem o comando `hzn` de modo mais conveniente. (O comando `hzn` está dentro do contêiner do agente, mas esses aliases permitem que o `hzn` seja executado a partir deste host).

   ```bash
   cat << 'END_ALIASES' >> ~/.bash_aliases
   alias getagentpod='kubectl -n openhorizon-agent get pods --selector=app=agent -o jsonpath={.items[*].metadata.name}'
   alias hzn='kubectl -n openhorizon-agent exec -i $(getagentpod) -- hzn'
   END_ALIASES
   source ~/.bash_aliases
   ```
   {: codeblock}

2. Verifique se o seu nó de borda está configurado (registrado com o hub de gerenciamento do {{site.data.keyword.ieam}}):

   ```bash
   hzn node list
   ```
   {: codeblock}

3. Para testar seu agente de cluster de borda, configure sua política de nó com uma propriedade que resultará na implementação do operador e do serviço helloworld neste nó de borda:

   ```bash
   cat << 'EOF' > operator-example-node.policy.json
   {
     "properties":[
       { "name": "openhorizon.example", "value": "operator" }
     ]
   }
   EOF

   cat operator-example-node.policy.json | hzn policy update -f-
   hzn policy list
   ```
   {: codeblock}

   **Nota:**
   * Como o comando **hzn** real está sendo executado dentro do contêiner do agente, para quaisquer subcomandos de `hzn` que requeiram um arquivo de entrada, é necessário canalizar o arquivo no comando, para que seu conteúdo seja transferido para o contêiner.

4. Depois de um minuto, verifique se há um acordo e se o operador de borda e os contêineres de serviço estão em execução:

   ```bash
   hzn agreement list
   kubectl -n openhorizon-agent get pods
   ```
   {: codeblock}

5. Usando os IDs de pod do comando anterior, visualize o log do operador e do serviço de borda:

   ```bash
   kubectl -n openhorizon-agent logs -f <operator-pod-id>
   # control-c to get out
   kubectl -n openhorizon-agent logs -f <service-pod-id>
   # control-c to get out
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
  cat <new-node-policy>.json | hzn policy update -f-
  hzn policy list
  ```
  {: codeblock}

   Após um minuto ou dois, os novos serviços serão implementados neste cluster de borda. 

* Nota: com o microk8s em alguns tipos de VMs, os pods de serviço que estão sendo interrompidos (substituídos) podem travar no estado **Finalizando**. Se isso acontecer, também é possível limpá-los executando:

  ```bash
  kubectl delete pod <pod-id> -n openhorizon-agent --force --grace-period=0
  pkill -fe <service-process>
  ```
  {: codeblock}

* Se você deseja usar um padrão, em vez de uma política, para executar serviços em seu cluster de borda:

  ```bash
  hzn unregister -f
  hzn register -n $HZN_EXCHANGE_NODE_AUTH -p <pattern-name>
  ```
  {: codeblock}

## Removendo o agente do cluster de borda
{: #remove_agent}

Para cancelar o registro de um cluster de borda e remover o agente {{site.data.keyword.ieam}} do cluster, execute estas etapas:

1. Extraia o script **agent-uninstall.sh** a partir do arquivo tar:

   ```bash
   tar -zxvf agentInstallFiles-x86_64-Cluster.tar.gz agent-uninstall.sh
   ```
   {: codeblock}

2. Exporte suas credenciais de usuário do Horizon Exchange:

   ```bash
   export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
   ```
   {: codeblock}

3. Remova o agente:

   ```bash
   ./agent-uninstall.sh -u $HZN_EXCHANGE_USER_AUTH -d
   ```
   {: codeblock}

Nota: ocasionalmente, a exclusão do namespace fica paralisada no estado "Terminating". Nessa situação, consulte [Um namespace está preso no estado Finalizando ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.1.1/troubleshoot/ns_terminating.html) para excluir manualmente o namespace.
