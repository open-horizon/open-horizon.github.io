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

# Utilisation de CP4MCM avec IEAM
{: #using_cp4mcm}

Suivez les instructions d'installation ci-dessous pour configurer et utiliser {{site.data.keyword.edge_shared_notm}}. Cette procédure prend en charge {{site.data.keyword.edge_servers_notm}} et {{site.data.keyword.edge_devices_notm}}.
{:shortdesc}

## Prérequis
{: #prereq}

Assurez-vous que vous avez [correctement dimensionné](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/servers/cluster_sizing.html) votre cluster pour {{site.data.keyword.icp_server_notm}}.

* Docker 1.13+
* [Interface de ligne de commande client OpenShift (oc) 4.2 ![S'ouvre dans un nouvel onglet](../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest-4.2/)

## Processus d'installation

1. Téléchargez les bundles **ibm-cp4mcm-core** et **ibm-ecm** associés à {{site.data.keyword.edge_servers_notm}} ou {{site.data.keyword.edge_devices_notm}} depuis IBM Passport Advantage vers votre environnement d'installation, selon le produit que vous avez acheté.

2. Préparez le répertoire à utiliser par l'installation, et décompressez le fichier zip de licence nécessaire à l'installation :

    ```
    mkdir -p /opt/ibm-multicloud-manager-1.2 && \
    tar -C /opt/ibm-multicloud-manager-1.2 -zxvf ibm-ecm-4.0.0-x86_64.tar.gz ibm-ecm-4.0.0-x86_64/ibm-ecm-licenses-4.0.zip
    ```
    {: codeblock}

3. Assurez-vous que le service Docker est en cours d'exécution, puis décompressez et chargez les images Docker à partir de l'archive tar d'installation :

    ```
    tar -zvxf ibm-cp4mcm-core-1.2-x86_64.tar.gz -O | sudo docker load
    ```
    {: codeblock}

4. Préparez et extrayez la configuration d'installation :

    ```
    cd /opt/ibm-multicloud-manager-1.2 && \
    sudo docker run --rm -v $(pwd):/data:z -e LICENSE=accept -v $(pwd)/ibm-ecm-4.0.0-x86_64:/installer/cfc-files/license:z --security-opt label:disable ibmcom/mcm-inception-amd64:3.2.3 cp -r cluster /data
    ```
    {: codeblock}

5. Indiquez un nouvel emplacement KUBECONFIG et **renseignez les informations appropriées sur le cluster** dans la commande **oc login** ci-dessous (obtenue lors de l'installation du cluster OpenShift), puis copiez le fichier **$KUBECONFIG** dans le répertoire de la configuration d'installation :

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

6. Mettez à jour le fichier config.yaml :

  * Indiquez les noeuds sur lesquels configurer les services {{site.data.keyword.edge_shared_notm}}. Il est fortement recommandé d'éviter d'utiliser les noeuds **maîtres** :

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

     Dans le fichier cluster/config.yaml (**master** fait ici référence à un ensemble spécifique de services qui font partie de {{site.data.keyword.edge_servers_notm}} et ne fait **pas** référence au rôle du noeud **maître**) :

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
     Remarque : La valeur des paramètres master, proxy et management forme un tableau et peut avoir plusieurs noeuds, et un même noeud peut être utilisé pour chacun de ces paramètres. La configuration ci-dessus concerne une installation **minimale**. Pour une installation de **production**, ajoutez trois noeuds worker pour chaque paramètre.

   * Choisissez votre classe de stockage (**storage_class**) préférée pour les données persistantes :

     ```
     # oc get storageclass
     NAME                               PROVISIONER                     AGE
     rook-ceph-block-internal           rook-ceph.rbd.csi.ceph.com      8h
     rook-ceph-cephfs-internal          rook-ceph.cephfs.csi.ceph.com   8h
     rook-ceph-delete-bucket-internal   ceph.rook.io/bucket             8h
     ```

     Dans le fichier cluster/config.yaml :

     ```
     # Storage Class
storage_class: rook-ceph-cephfs-internal
     ```

   * Définissez un mot de passe administrateur par défaut (**default_admin_password**) d'au moins 32 caractères :

     ```
     # default_admin_password:
     # password_rules:
     #   - '^([a-zA-Z0-9\-]{32,})$'
     default_admin_password: <YOUR-32-CHARACTER-OR-LONGER-ADMIN-PASSWORD>
     ```

   * Ajoutez une ligne permettant d'indiquer que le nom du cluster (**cluster_name**) identifie de manière unique le cluster :

     ```
     cluster_name: <INSERT_YOUR_UNIQUE_CLUSTER_NAME>
     ```

     Remarque : Sans cette ligne, un nom **mycluster** par défaut est attribué. Si vous installez également {{site.data.keyword.edge_devices_notm}}, il est important de nommer correctement votre cluster. Le paramètre **cluster_name** servira à définir plusieurs composants pour ce produit.

7. Ouvrez la route par défaut vers le registre d'images OpenShift interne :

    ```
    oc patch configs.imageregistry.operator.openshift.io/cluster --type merge -p '{"spec":{"defaultRoute":true}}'
    ```
    {: codeblock}

8. Installez {{site.data.keyword.edge_shared_notm}} :

    ```
    sudo docker run -t --net=host -e LICENSE=accept -v $(pwd)/../ibm-ecm-4.0.0-x86_64:/installer/cfc-files/license:z -v $(pwd):/installer/cluster:z -v /var/run:/var/run:z -v /etc/docker:/etc/docker:z --security-opt label:disable ibmcom/mcm-inception-amd64:3.2.3 install-with-openshift
    ```
    {: codeblock}

<!--## Importing a cluster to be managed
There is a known issue with importing clusters, we are working on providing functional documentation steps for this process.

## Next steps
If this installation was done as part of a prerequisite for {{site.data.keyword.edge_devices_notm}}, [return to continue that installation](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/devices/installing/install.html).-->
