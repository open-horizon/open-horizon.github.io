---

copyright:
years: 2020
lastupdated: "2020-4-24"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Preparando um cluster de borda
{: #preparing_edge_cluster}

## Antes de iniciar

Considere o seguinte antes de começar a trabalhar com clusters de borda:

* [Pré-requisitos](#preparing_clusters)
* [Reúna as informações e os arquivos necessários para os clusters de borda](#gather_info)

## Pré-requisitos
{: #preparing_clusters}

Antes de instalar um agente em um cluster de borda:

1. Instale o Kubectl no ambiente no qual o script de instalação do agente é executado.
2. Instale a CLI do {{site.data.keyword.open_shift}} Client (oc) no ambiente no qual o script de instalação do agente é executado.
3. Obtenha o acesso de administrador de cluster, que é necessário para criar recursos de cluster relevantes.
4. Tenha um registro de cluster de borda para hospedar a imagem do docker do agente.
5. Instale os comandos **cloudctl** e **kubectl** e extraia **ibm-edge-computing-4.1-x86_64.tar.gz**. Consulte [Processo de instalação](../installing/install.md#process).

## Reúna as informações e os arquivos necessários para clusters de borda
{: #gather_info}

Vários arquivos são necessários para instalar e registrar seus clusters de borda com o {{site.data.keyword.edge_notm}}. Esta
seção orienta você na reunião desses arquivos em um arquivo tar, que poderá, então, ser usado em cada um de seus clusters de borda.

1. Configure as variáveis de ambiente **CLUSTER_URL**:

    ```
    export CLUSTER_URL=<cluster-url>
   export USER=<your-icp-admin-user>
   export PW=<your-icp-admin-password>
    ```
    {: codeblock}

    Como alternativa, depois de se conectar ao cluster com **oc login**, é possível executar:

    ```
    export CLUSTER_URL=https://$(oc get routes icp-console -o jsonpath='{.spec.host}')
    ```
    {: codeblock}
    
2. Use os privilégios de administrador de cluster para conectar-se ao seu cluster e, em seguida, selecione **kube-system** como o namespace e preencha a senha que você definiu no config.yaml durante o {{site.data.keyword.mgmt_hub}} [Processo de instalação](../installing/install.md#process):

    ```
    cloudctl login -a $CLUSTER_URL -u admin -p <your-icp-admin-password> -n kube-system --skip-ssl-validation
    ```
    {: codeblock}    

3. Configure o nome do usuário do registro do cluster de borda, a senha e o nome de imagem completo no registro do cluster de borda nas variáveis de ambiente. O valor de IMAGE_ON_EDGE_CLUSTER_REGISTRY é especificado neste formato:

    ```
    <registry-name>/<repo-name>/<image-name>.
    ```
    {: codeblock} 

    Se estiver usando o hub do docker como o registro, especifique o valor neste formato:
    
    ```
    <docker-repo-name>/<image-name>
    ```
    {: codeblock}
    
    Por exemplo:
    
    ```
    export EDGE_CLUSTER_REGISTRY_USER=<your-edge-cluster-registry-username>
    export EDGE_CLUSTER_REGISTRY_PW=<your-edge-cluster-registry-password>
    export IMAGE_ON_EDGE_CLUSTER_REGISTRY=<full-image-name-on-your-edge-cluster registry>
    ```
    {: codeblock}
    
4. Faça download da versão mais recente de **edgeDeviceFiles.sh**:

   ```
   curl -O https://raw.githubusercontent.com/open-horizon/examples/master/tools/edgeDeviceFiles.sh
   chmod +x edgeDeviceFiles.sh
   ```
   {: codeblock}

5. Execute o script **edgeDeviceFiles.sh** para reunir os arquivos necessários:

   ```
   ./edgeDeviceFiles.sh x86_64-Cluster -t -r -o <hzn-org-id> -n <node-id> <other flags>
   ```
   {: codeblock}
    
   Isso cria um arquivo chamado agentInstallFiles-x86_64-Cluster..tar.gz. 
    
**Argumentos do Comando**
   
Nota: especifique x86_64-Cluster para instalar o agente em um cluster de borda.
   
|Argumento do Comando|Resultado|
|-----------------|------|
|pa                |Crie um arquivo **agentInstallFiles-&lt;edge-device-type&gt;.tar.gz** que contenha todos os arquivos reunidos. Se essa sinalização não for configurada, os arquivos reunidos serão colocados no diretório atual.|
|f                |Especifique um diretório para o qual os arquivos reunidos serão movidos. Se o diretório não existir, ele será criado. O diretório atual é o padrão|
|r                |O **EDGE_CLUSTER_REGISTRY_USER**, o **EDGE_CLUSTER_REGISTRY_PW** e o **IMAGE_ON_EDGE_CLUSTER_REGISTRY** precisam ser configurados em uma variável de ambiente (etapa 1), caso esta sinalização esteja sendo usada. Em 4.1, é uma sinalização necessária.|
|ão                |Especifique **HZN_ORG_ID**. Este valor é usado para registro de cluster de borda.|
|n                |Especifique **NODE_ID**, que deve ser o valor de seu nome do cluster de borda. Esse valor é usado para o registro do cluster de borda.|
|s                |Especifique a classe de armazenamento de cluster a ser usada por solicitação de volume persistente. A classe de armazenamento padrão é "gp2".|
|i                |A versão de imagem do agente a ser implementada no cluster de borda.|


Quando você estiver pronto para instalar o agente no cluster de borda, consulte [Instalando um agente e registrando um cluster de borda](importing_clusters.md).

<!--DELETE DOWN TO    
   The following flags are only supported for x86_64-Cluster:

    * **-r**: specify edge cluster registry if edge cluster is not using Openshift image registry. "EDGE_CLUSTER_REGISTRY_USER", "EDGE_CLUSTER_REGISTRY_PW" and "EDGE_CLUSTER_REGISTRY_REPONAME" need to be set in environment variable (step 1) if using this flag.
    * **-s**: specify cluster storage class to be used by persistent volume claim. Default storage class is "gp2".
    * **-i**: agent image version to be deployed on edge cluster
    * **-o**: specify HZN_ORG_ID. This value is used for edge cluster registration.
    * **-n**: specify NODE_ID. NODE_ID should be the value of your edge cluster name. This value is used for edge cluster registration. 

4. The command in the previous step creates a file that is called **agentInstallFiles-&lt;edge-device-type&gt;.tar.gz**. If you have other types of edge devices (different architectures), repeat the previous step for each type.

5. Take note of the API key that was created and displayed by the **edgeDeviceFiles.sh** command.

6. Now that you are logged in via **cloudctl**, if you need to create additional API keys for users to use with the {{site.data.keyword.horizon}} **hzn** command:

   ```
   cloudctl iam api-key-create "<choose-an-api-key-name>" -d "<choose-an-api-key-description>"
   ```
   {: codeblock}

   In the output of the command look for the key value in the line that starts with **API Key** and save the key value for future use.

7. When you are ready to set up edge devices, follow [Getting started using {{site.data.keyword.edge_devices_notm}}](../getting_started/getting_started.md).

Lily - is the pointer in step 7 above still correct?-->

## Próximos passos

* [Instalando um agente e registrando um cluster de borda](importing_clusters.md)

## Informações relacionadas

* [Clusters de borda](edge_clusters.md)
* [Iniciando a Utilização do {{site.data.keyword.edge_notm}}](../getting_started/getting_started.md)
* [Processo de instalação](../installing/install.md#process)
