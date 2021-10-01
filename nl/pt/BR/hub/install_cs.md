---

copyright:
years: 2020
lastupdated: "2020-06-03"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Instalação de Serviços Comuns

## Pré-requisito
{: #prereq}

### {{site.data.keyword.ocp_tm}}
Assegure-se de que você tenha uma instalação do {{site.data.keyword.open_shift_cp}} [apropriadamente dimensionada](cluster_sizing.md) e suportada. Incluindo os serviços de registro e de armazenamento instalados e funcionando no cluster. Para obter mais informações sobre como instalar o {{site.data.keyword.open_shift_cp}}, consulte a documentação do
{{site.data.keyword.open_shift}} para obter as versões suportadas abaixo:

* [Documentação do {{site.data.keyword.open_shift_cp}} 4.3 ![Abre em uma nova guia](../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://www.ibm.com/links?url=https%3A%2F%2Fdocs.openshift.com%2Fcontainer-platform%2F4.3%2Fwelcome%2Findex.html)
* [Documentação do {{site.data.keyword.open_shift_cp}} 4.4 ![Abre em uma nova guia](../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://www.ibm.com/links?url=https%3A%2F%2Fdocs.openshift.com%2Fcontainer-platform%2F4.4%2Fwelcome%2Findex.html)

### Outros Pré-requisitos

* Docker 1.13+
* [{{site.data.keyword.open_shift}}CLI do cliente (oc) 4.4 ![Abre em uma nova guia](../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest-4.4/)

## Processo de Instalação

1. [Faça download do pacote desejado a partir do IBM Passport Advantage](part_numbers.md) para seu ambiente de instalação e descompacte a mídia de instalação:
    ```
    tar -zxvf ibm-eam-{{site.data.keyword.semver}}-x86_64.tar.gz
    cd ibm-eam-{{site.data.keyword.semver}}-x86_64
    ```
    {: codeblock}

2. Prepare o diretório a ser usado pela instalação e copie o arquivo zip da licença para que seja aceito como parte da instalação:

    ```
    mkdir -p /opt/common-services-3.2.7/ibm-eam-{{site.data.keyword.semver}}-licenses && \
    cp ibm-eam-{{site.data.keyword.semver}}-licenses.zip /opt/common-services-3.2.7/ibm-eam-{{site.data.keyword.semver}}-licenses
    ```
    {: codeblock}

3. Assegure-se de que o serviço do Docker esteja em execução e descompacte/carregue as imagens do Docker a partir do tarball de instalação:

    ```
    systemctl enable docker
    systemctl start docker
    tar -zvxf common-services-boeblingen-2004-x86_64.tar.gz -O | sudo docker load
    ```
    {: codeblock}

    **Nota:** pode demorar alguns minutos para que a saída seja mostrada, pois ele está descompactando várias imagens

4. Prepare-se para a configuração de instalação e extraia-a:

    ```
    cd /opt/common-services-3.2.7 && \
    sudo docker run --rm -v $(pwd):/data:z -e LICENSE=accept -v $(pwd)/ibm-eam-{{site.data.keyword.semver}}-licenses:/installer/cfc-files/license:z --security-opt label:disable ibmcom/icp-inception-amd64:3.2.7 cp -r cluster /data
    ```
    {: codeblock}

5. Configure um novo local do KUBECONFIG, **Preencha as informações de cluster corretas** no comando **oc login** abaixo (obtido a partir da instalação do cluster do {{site.data.keyword.open_shift}}) e copie o arquivo **$KUBECONFIG** para o diretório de configuração da instalação:

    ```
    export KUBECONFIG=$(pwd)/myclusterconfig
    ```
    {: codeblock}

    ```
    oc login https://<API_ENDPOINT_HOST>:<PORT> -u <ADMIN_USER> -p <ADMIN_PASSWORD> --insecure-skip-tls-verify=true && \
    cp $KUBECONFIG $(pwd)/cluster/kubeconfig && \
    cd cluster
    ```
    {: codeblock}

6. Atualize o arquivo config.yaml:

   * Determine em quais nós você deseja configurar o planejamento do {{site.data.keyword.common_services}} usando os nós **principais**:

     ```
     # oc get nodes
     NAME               STATUS   ROLES    AGE  VERSION
     master0.test.com   Ready    master   8h   v1.17.1
     master1.test.com   Ready    master   8h   v1.17.1
     master2.test.com   Ready    master   8h   v1.17.1
     worker0.test.com   Ready    worker   8h   v1.17.1
     worker1.test.com   Ready    worker   8h   v1.17.1
     worker2.test.com   Ready    worker   8h   v1.17.1
    ```

     Dentro do cluster/config.yaml (aqui, **master** faz referência a um conjunto específico de serviços que fazem parte de {{site.data.keyword.common_services}} e **não** se refere à função de nó **principal**):

     ```
     # A list of OpenShift nodes that used to run services components
     cluster_nodes:
       master:
         - worker0.test.com
       proxy:
         - worker0.test.com
       management:
         - worker0.test.com
     ```
     Nota: o valor dos parâmetros master, proxy e management é uma matriz e pode ter diversos nós e o mesmo nó pode ser usado para cada parâmetro. A configuração acima destina-se a uma instalação **mínima**, para uma instalação de **produção**, inclua esses nós do trabalhador para cada parâmetro.

   * Escolha sua **storage_class** preferencial para dados persistentes para alavancar o armazenamento dinâmico:

     ```
     # oc get storageclass
     NAME                               PROVISIONER                     AGE
     rook-ceph-block-internal           rook-ceph.rbd.csi.ceph.com      8h
     rook-ceph-cephfs-internal          rook-ceph.cephfs.csi.ceph.com   8h
     rook-ceph-delete-bucket-internal   ceph.rook.io/bucket             8h
     ```

     Dentro do cluster/config.yaml:

     ```
     # Storage Class
storage_class: rook-ceph-cephfs-internal
     ```

     Consulte o seguinte para obter as [opções de armazenamento e as instruções de configuração dinâmicas suportadas do {{site.data.keyword.open_shift}} ![Abre em uma nova guia](../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://docs.openshift.com/container-platform/4.4/storage/understanding-persistent-storage.html)

   * Defina uma **default_admin_password** de 32 caracteres ou mais:

     ```
     # default_admin_password:
     # password_rules:
     #   - '^([a-zA-Z0-9\-]{32,})$'
     default_admin_password: <YOUR-32-CHARACTER-OR-LONGER-ADMIN-PASSWORD>
     ```

   * Inclua uma linha definindo o **cluster_name** para identificar o cluster com exclusividade:

     ```
     cluster_name: <INSERT_YOUR_UNIQUE_CLUSTER_NAME>
     ```

     Nota: sem esta definição, um nome padrão de **mycluster** será escolhido. Esta é uma etapa importante para nomear de modo adequado seu cluster, já que o **cluster_name** será usado para definir vários componentes para o {{site.data.keyword.edge_notm}}

7. Abra a rota padrão para o registro de imagem interno do {{site.data.keyword.open_shift}}:

    ```
    oc patch configs.imageregistry.operator.openshift.io/cluster --type merge -p '{"spec":{"defaultRoute":true}}'
    ```
    {: codeblock}

8. Instale o {{site.data.keyword.common_services}}

    ```
    sudo docker run -t --net=host -e LICENSE=accept -v $(pwd)/../ibm-eam-{{site.data.keyword.semver}}-licenses:/installer/cfc-files/license:z -v $(pwd):/installer/cluster:z -v /var/run:/var/run:z -v /etc/docker:/etc/docker:z --security-opt label:disable ibmcom/icp-inception-amd64:3.2.7 install-with-openshift
    ```
    {: codeblock}
    **Nota:** o tempo de instalação variará de acordo com as velocidades de rede, já que se espera que nenhuma saída seja vista por algum tempo durante a tarefa 'Carregando imagens'.

Anote a URL da saída de instalação, ela será necessária para a próxima etapa de [Instalação do {{site.data.keyword.ieam}}](offline_installation.md).
