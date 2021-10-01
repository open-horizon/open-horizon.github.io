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

# Instalando um agente e registrando um cluster de borda
{: #importing_clusters}

É possível instalar agentes nesses clusters de borda:

* Kubernetes
* Kubernetes leve (isso é recomendado para teste)

## Instalando agentes em clusters de borda do Kubernetes
{: #install_kube}

Uma instalação do agente automatizada está disponível executando o script `agent-install.sh`. 

Siga estas etapas no ambiente no qual o script de instalação do agente será executado:

1. Obtenha o arquivo `agentInstallFiles-x86_64-Cluster.tar.gz` e uma chave de API de seu administrador. Estes já deveriam ter sido criados em [Reúna as informações e os arquivos necessários para clusters de borda](preparing_edge_cluster.md).  

2. Configure o nome do arquivo em uma variável de ambiente para etapas subsequentes:

   ```
   export AGENT_TAR_FILE=agentInstallFiles-x86_64-Cluster.tar.gz
   ```
   {: codeblock}

3. Extraia os arquivos do arquivo tar:

   ```
   tar -zxvf agentInstallFiles-x86_64-Cluster.tar.gz
   ```
   {: codeblock}

4. Exporte as credenciais do usuário do Horizon Exchange, que podem estar em uma dessas formas:

   ```
   export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
   ```
   {: codeblock}

   ou

   ```
   export HZN_EXCHANGE_USER_AUTH=<username>/<username>:<password>
   ```
   {: codeblock}

5. Execute o comando `agent-install.sh` para instalar e configurar o agente do Horizon e registrar o seu cluster de borda para executar o serviço de borda de amostra helloworld:

   ```
   ./agent-install.sh -u $HZN_EXCHANGE_USER_AUTH -k agent-install.cfg  -D cluster -p
   ```
   {: codeblock}

   Nota: durante a instalação do agente, é possível ver este prompt: **Deseja sobrescrever o Horizon?[y/N]: **. Selecione **y** e pressione **Enter**; o `agent-install.sh` define a configuração corretamente.

6. (Opcional) Para ver as descrições da sinalização `agent-install.sh` disponíveis: 

   ```
   ./agent-install.sh -h
   ```
   {: codeblock}

7. Liste os recursos do agente em execução no Kubernetes. Agora que o agente está instalado em seu cluster de borda e seu cluster de borda está registrado, é possível listar os recursos de cluster de borda a seguir:

   * Namespace:

   ```
   kubectl get namespace openhorizon-agent
   ```
   {: codeblock}

   * Implementação:

   ```
   kubectl get deployment -n openhorizon-agent
   ```
   {: codeblock}

   Para listar detalhes da implementação do agente:

   ```
   kubectl get deployment -n openhorizon-agent -o yaml
   ```
   {: codeblock}

   * Configmap:

   ```
   kubectl get configmap openhorizon-agent-config -n openhorizon-agent -o yaml
   ```
   {: codeblock}

   * Segredo:
   
   ```
   kubectl get secret openhorizon-agent-secrets -n openhorizon-agent -o yaml
   ```
   {: codeblock}

   * PersistentVolumeClaim:
   
   ```
   kubectl get pvc openhorizon-agent-pvc -n openhorizon-agent -o yaml
   ```
   {: codeblock}

   * Pod:

   ```
   kubectl get pod -n openhorizon-agent
   ```
   {: codeblock}

8. Visualize os logs, obtenha o ID do pod e: 

   ```
   kubectl logs <pod-id> -n openhorizon-agent
   ```
   {: codeblock}

9. Execute o comando `hzn` dentro do contêiner do agente:

   ```
   kubectl exec -it <pod-id> -n openhorizon-agent /bin/bash
   hzn --help
   ```
   {: codeblock}

10. Explore as sinalizações de comando `hzn` e o subcomando:

   ```
   hzn --help
   ```
   {: codeblock}

## Instalando agentes em pequenos clusters de borda do Kubernetes leves

Este conteúdo descreve como instalar o agente no microk8s, um cluster Kubernetes leve e pequeno que pode ser instalado e configurado localmente, incluindo:

* Instalação e configuração do microk8s
* Instalando um agente no microk8s

### Instalando e configurando o microk8s

1. Instale o microk8s:

   ```
   sudo snap install microk8s --classic --channel=1.14/stable
   ```
   {: codeblock}

2. Configure um alias para o microk8s.kubectl:

   Nota: assegure-se de que você não tenha o comando `kubectl`, caso deseje testar no microk8s. 

  * O MicroK8s usa um comando kubectl incluído em um namespace para evitar conflitos com quaisquer instalações existentes do kubectl. Se você não tiver uma instalação existente, é mais fácil incluir um alias (`append to ~/.bash_aliases`): 
   
   ```
   alias kubectl='microk8s.kubectl' 
   ```
   {: codeblock}
  
   * Em
seguida:

   ```
   source ~/.bash_aliases
   ```
   {: codeblock}

3. Ative o dns e o módulo de armazenamento no microk8s:

   ```
   microk8s.enable dns storage
   ```
   {: codeblock}

4. Crie a classe de armazenamento no microk8s. O script de instalação do agente usa `gp2` como a classe de armazenamento padrão para solicitação de volume persistente. Essa classe de armazenamento precisa ser criada no ambiente microk8s antes de instalar o agente. Se o agente de cluster de borda usa outra classe de armazenamento, ele também deve ser criado previamente. 

   A seguir está um exemplo de criação do `gp2` como uma classe de armazenamento:  

   1. Crie um arquivo storageClass.yml: 

      ```
      apiVersion: storage.k8s.io/v1
      kind: StorageClass
      metadata:
       name: gp2
      provisioner: microk8s.io/hostpath
      reclaimPolicy: Delete
      volumeBindingMode: Immediate
      ```
      {: codeblock}

   2. Use o comando `kubectl` para criar objeto storageClass no microk8s:

      ```
      kubectl apply -f storageClass.yml
      ```
      {: codeblock}

### Instalando um agente no microk8s

Siga estas etapas para instalar um agente no microk8s.

1. Conclua as [etapas de 1 a 3](#install_kube).

2. Execute o comando `agent-install.sh` para instalar e configurar o agente do Horizon e registrar o seu cluster de borda para executar o serviço de borda de amostra helloworld:

   ```
   source agent-install.sh -u $HZN_EXCHANGE_USER_AUTH -k agent-install.cfg  -D cluster -p "IBM/pattern-ibm.helloworld"
   ```
   {: codeblock}

   Nota: durante a instalação do agente, é possível ver este prompt: **Deseja sobrescrever o Horizon?[y/N]: **. Selecione **y** e pressione **Enter**; o `agent-install.sh` define a configuração corretamente.

## Remova o agente do cluster leve do Kubernetes 

Nota: como o script de desinstalação do agente não está concluído nesta liberação, a remoção do agente é concluída excluindo-se o namespace openhorizon-agent.

1. Exclua o namespace:

   ```
   kubectl delete namespace openhorizon-agent
   ```
   {: codeblock}

      Nota: ocasionalmente, a exclusão do namespace é paralisada no estado "Finalizando". Nessa situação, consulte [Um namespace está preso no estado Finalizando ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.1.1/troubleshoot/ns_terminating.html) para excluir manualmente o namespace.

2. Exclua o clusterrolebinding: 

   ```
   kubectl delete clusterrolebinding openhorizon-agent-cluster-rule
   ```
   {: codeblock}

<!--If this installation was done as part of a prerequisite for {{site.data.keyword.edge_devices_notm}}, [return to continue that installation](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/devices/installing/install.html).-->
