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

# Installation des services communs

## Prérequis
{: #prereq}

### {{site.data.keyword.ocp_tm}}
Vérifiez que votre installation {{site.data.keyword.open_shift_cp}} est [correctement dimensionnée](cluster_sizing.md) et prise en charge. Le registre et les services de stockage doivent également être installés et opérationnels dans votre cluster. Pour de plus amples informations sur l'installation d'{{site.data.keyword.open_shift_cp}}, reportez-vous à la documentation des versions {{site.data.keyword.open_shift}} prises en charge ci-dessous :

* [{{site.data.keyword.open_shift_cp}} 4.3 Documentation ![S'ouvre dans un nouvel onglet](../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://www.ibm.com/links?url=https%3A%2F%2Fdocs.openshift.com%2Fcontainer-platform%2F4.3%2Fwelcome%2Findex.html)
* [{{site.data.keyword.open_shift_cp}} 4.4 Documentation ![S'ouvre dans un nouvel onglet](../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://www.ibm.com/links?url=https%3A%2F%2Fdocs.openshift.com%2Fcontainer-platform%2F4.4%2Fwelcome%2Findex.html)

### Autres prérequis

* Docker 1.13+
* [{{site.data.keyword.open_shift}} client CLI (oc) 4.4 ![S'ouvre dans un nouvel onglet](../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest-4.4/)

## Processus d'installation

1. [Téléchargez le package à partir d'IBM Passport Advantage](part_numbers.md) vers votre environnement d'installation et décompressez le support d'installation :
    ```
    tar -zxvf ibm-eam-{{site.data.keyword.semver}}-x86_64.tar.gz
    cd ibm-eam-{{site.data.keyword.semver}}-x86_64
    ```
    {: codeblock}

2. Préparez le répertoire d'installation et copiez le fichier zip de licence nécessaire à l'installation :

    ```
    mkdir -p /opt/common-services-3.2.7/ibm-eam-{{site.data.keyword.semver}}-licenses && \
    cp ibm-eam-{{site.data.keyword.semver}}-licenses.zip /opt/common-services-3.2.7/ibm-eam-{{site.data.keyword.semver}}-licenses
    ```
    {: codeblock}

3. Assurez-vous que le service Docker est en cours d'exécution, puis décompressez et chargez les images Docker à partir de l'archive tar d'installation :

    ```
    systemctl enable docker
    systemctl start docker
    tar -zvxf common-services-boeblingen-2004-x86_64.tar.gz -O | sudo docker load
    ```
    {: codeblock}

    **Remarque** : Cela peut prendre quelques minutes avant que la sortie ne s'affiche en raison du nombre d'images à décompresser.

4. Préparez et extrayez la configuration d'installation :

    ```
    cd /opt/common-services-3.2.7 && \
    sudo docker run --rm -v $(pwd):/data:z -e LICENSE=accept -v $(pwd)/ibm-eam-{{site.data.keyword.semver}}-licenses:/installer/cfc-files/license:z --security-opt label:disable ibmcom/icp-inception-amd64:3.2.7 cp -r cluster /data
    ```
    {: codeblock}

5. Indiquez un nouvel emplacement KUBECONFIG et **renseignez les informations appropriées sur le cluster** dans la commande **oc login** ci-dessous (obtenue lors de l'installation du cluster {{site.data.keyword.open_shift}}), puis copiez le fichier **$KUBECONFIG** dans le répertoire de la configuration d'installation :

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

6. Mettez à jour le fichier config.yaml :

   * Indiquez les noeuds sur lesquels configurer la planification des services {{site.data.keyword.common_services}}, en évitant d'utiliser les noeuds **master** :

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

     Dans le fichier cluster/config.yaml (**master** fait ici référence à un ensemble spécifique de services qui font partie de {{site.data.keyword.common_services}} et ne fait **pas** référence au rôle du noeud **maître**) :

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

   * Choisissez votre classe de stockage (**storage_class**) préférée pour que le stockage dynamique puisse exploiter les données persistantes :

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

     Consultez la page [supported dynamic {{site.data.keyword.open_shift}} storage options and configuration instructions ![S'ouvre dans un nouvel onglet](../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://docs.openshift.com/container-platform/4.4/storage/understanding-persistent-storage.html)

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

     Remarque : Sans cette ligne, un nom **mycluster** par défaut est attribué. Il est important d'attribuer un nom correct à votre cluster, car **cluster_name** sera utilisé pour définir plusieurs composants d'{{site.data.keyword.edge_notm}}.

7. Ouvrez la route par défaut vers le registre d'images {{site.data.keyword.open_shift}} interne :

    ```
    oc patch configs.imageregistry.operator.openshift.io/cluster --type merge -p '{"spec":{"defaultRoute":true}}'
    ```
    {: codeblock}

8. Installez {{site.data.keyword.common_services}}

    ```
    sudo docker run -t --net=host -e LICENSE=accept -v $(pwd)/../ibm-eam-{{site.data.keyword.semver}}-licenses:/installer/cfc-files/license:z -v $(pwd):/installer/cluster:z -v /var/run:/var/run:z -v /etc/docker:/etc/docker:z --security-opt label:disable ibmcom/icp-inception-amd64:3.2.7 install-with-openshift
    ```
    {: codeblock}
    **Remarque** : La durée d'installation dépend de la vitesse du réseau, et il est prévu qu'aucune sortie ne sera visible pendant un certain temps au cours de la tâche de 'chargement des images'.

Notez l'URL de la sortie de l'installation, elle sera nécessaire pour l'étape suivante [Installation d'{{site.data.keyword.ieam}}](offline_installation.md).
