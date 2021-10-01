---

copyright:
  years: 2019, 2020
lastupdated: "2020-02-13"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Usando o CP4MCM com o IEAM
{: #using_cp4mcm}

Siga estas etapas de instalação para configurar e ativar o uso do {{site.data.keyword.edge_shared_notm}}. Esta instalação suporta o {{site.data.keyword.edge_servers_notm}} e o {{site.data.keyword.edge_devices_notm}}.
{:shortdesc}

## Pré-requisitos
{: #prereq}

Assegure-se de haver [dimensionado corretamente](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/servers/cluster_sizing.html) o cluster para o {{site.data.keyword.icp_server_notm}}.

* Docker 1.13+
* [CLI do cliente OpenShift (oc) 4.2
![Abre em uma nova guia](../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest-4.2/)

## Processo de instalação

1. Faça download dos pacotes configuráveis **ibm-cp4mcm-core** e **ibm-ecm** para o {{site.data.keyword.edge_servers_notm}} ou o {{site.data.keyword.edge_devices_notm}} do IBM Passport Advantage para seu ambiente de instalação, dependendo do produto adquirido.

2. Prepare o diretório a ser usado pela instalação e descompacte o arquivo zip da licença para ser aceito como parte da instalação:

    ```
    mkdir -p /opt/ibm-multicloud-manager-1.2 && \
    tar -C /opt/ibm-multicloud-manager-1.2 -zxvf ibm-ecm-4.0.0-x86_64.tar.gz ibm-ecm-4.0.0-x86_64/ibm-ecm-licenses-4.0.zip
    ```
    {: codeblock}

3. Assegure-se de que o serviço do Docker esteja em execução e descompacte/carregue as imagens do Docker a partir do tarball de instalação:

    ```
    tar -zvxf ibm-cp4mcm-core-1.2-x86_64.tar.gz -O | sudo docker load
    ```
    {: codeblock}

4. Prepare-se para a configuração de instalação e extraia-a:

    ```
    cd /opt/ibm-multicloud-manager-1.2 && \
    sudo docker run --rm -v $(pwd):/data:z -e LICENSE=accept -v $(pwd)/ibm-ecm-4.0.0-x86_64:/installer/cfc-files/license:z --security-opt label:disable ibmcom/mcm-inception-amd64:3.2.3 cp -r cluster /data
    ```
    {: codeblock}

5. Especifique um novo local KUBECONFIG, **preencha as informações de cluster corretas** no comando **oc login** abaixo (obtido a partir da instalação do cluster OpenShift) e copie o arquivo **$KUBECONFIG** para o diretório de configuração da instalação:

    ```
    export KUBECONFIG=$(pwd)/myclusterconfig
    ```
    {: codeblock}

    ```
    oc login https://<API_ENDPOINT_HOST>:<PORT> -u <ADMIN_USER> -p <ADMIN_PASSWORD> --insecure-skip-tls-verify=true && \
    cp $KUBECONFIG /opt/ibm-multicloud-manager-1.2/cluster/kubeconfig && \
    cd cluster
    ```
    {: codeblock}

6. Atualize o arquivo config.yaml:

  * Determine em quais nós você deseja configurar o planejamento dos serviços do {{site.data.keyword.edge_shared_notm}}. É altamente recomendado evitar o uso de nós **master**:

     ```
     # oc get nodes
     NAME               STATUS   ROLES    AGE  VERSION
     master0.test.com   Ready    master   8h   v1.14.6+c07e432da
     master1.test.com   Ready    master   8h   v1.14.6+c07e432da
     master2.test.com   Ready    master   8h   v1.14.6+c07e432da
     worker0.test.com   Ready    worker   8h   v1.14.6+c07e432da
     worker1.test.com   Ready    worker   8h   v1.14.6+c07e432da
     worker2.test.com   Ready    worker   8h   v1.14.6+c07e432da
     ```

     Dentro do cluster/config.yaml (aqui, **master** faz referência a um conjunto específico de serviços que fazem parte de {{site.data.keyword.edge_servers_notm}} e **não** se refere à função de nó **principal**):

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

   * Escolha sua **storage_class** preferencial para dados persistentes:

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

     Nota: sem esta definição, um nome padrão de **mycluster** será escolhido. Se também for instalar o {{site.data.keyword.edge_devices_notm}}, a escolha de um nome adequado para o cluster é uma etapa importante. O **cluster_name** será usado para definir vários componentes para esse produto.

7. Abra a rota padrão para o registro de imagem do OpenShift interno:

    ```
    oc patch configs.imageregistry.operator.openshift.io/cluster --type merge -p '{"spec":{"defaultRoute":true}}'
    ```
    {: codeblock}

8. Instale o {{site.data.keyword.edge_shared_notm}}:

    ```
    sudo docker run -t --net=host -e LICENSE=accept -v $(pwd)/../ibm-ecm-4.0.0-x86_64:/installer/cfc-files/license:z -v $(pwd):/installer/cluster:z -v /var/run:/var/run:z -v /etc/docker:/etc/docker:z --security-opt label:disable ibmcom/mcm-inception-amd64:3.2.3 install-with-openshift
    ```
    {: codeblock}

<!--## Importing a cluster to be managed
There is a known issue with importing clusters, we are working on providing functional documentation steps for this process.

## Next steps
If this installation was done as part of a prerequisite for {{site.data.keyword.edge_devices_notm}}, [return to continue that installation](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/devices/installing/install.html).-->
