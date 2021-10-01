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

# Installation de l'agent
{: #importing_clusters}

**Remarque** : L'installation de l'agent {{site.data.keyword.ieam}} nécessite un accès d'administrateur de cluster sur le cluster de périphérie.

Commencez par installer l'agent {{site.data.keyword.edge_notm}} sur l'un des types de clusters de périphérie Kubernetes suivants :

* [Installation d'un agent sur un cluster de périphérie Kubernetes {{site.data.keyword.ocp}}](#install_kube)
* [Installation d'un agent sur des clusters de périphérie k3s et microk8s](#install_lite)

Déployez ensuite un service de périphérie sur votre cluster de périphérie :

* [Déploiement de services sur votre cluster de périphérie](#deploying_services)

Si vous avez besoin de retirer l'agent :

* [Retrait d'un agent du cluster de périphérie](../using_edge_services/removing_agent_from_cluster.md)

## Installation d'un agent sur un cluster de périphérie Kubernetes {{site.data.keyword.ocp}}
{: #install_kube}

Ce contenu vous explique comment installer l'agent {{site.data.keyword.ieam}} sur votre cluster de périphérie {{site.data.keyword.ocp}}. Procédez comme suit sur un hôte disposant d'un accès administrateur sur votre cluster de périphérie :

1. Connectez-vous à votre cluster de périphérie en tant que **admin** :

   ```bash
   oc login https://<api_endpoint_host>:<port> -u <admin_user> -p <admin_password> --insecure-skip-tls-verify=true
   ```
   {: codeblock}

2. Si vous n'avez pas effectué les étapes de la section [Création de votre clé d'API](../hub/prepare_for_edge_nodes.md), faites-le maintenant. Ce processus crée une clé d'API, localise certains fichiers et rassemble les valeurs de variables d'environnement nécessaires lorsque vous définissez des nœuds de périphérie. Définissez les mêmes variables d'environnement sur ce cluster de périphérie :

  ```bash
  export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>   export HZN_ORG_ID=<votre-organisation-exchange>   export HZN_FSS_CSSURL=https://<entrée-concentrateur-gestion-ieam>/edge-css/
  ```
  {: codeblock}

3. Définissez la variable d'espace de nom de l'agent sur sa valeur par défaut (ou un espace de nom dans lequel vous voulez explicitement installer l'agent) :

   ```bash
   export AGENT_NAMESPACE=openhorizon-agent
   ```
   {: codeblock}

4. Définissez la classe de stockage à utiliser par l'agent : une classe de stockage intégrée ou une classe de stockage que vous avez créée. Vous pouvez afficher les classes de stockage disponibles à l'aide de la première des deux commandes ci-dessous, puis entrez le nom de celle que vous souhaitez utiliser dans la deuxième commande. Une classe de stockage doit être intitulée `(par défaut)` :

   ```bash
   oc get storageclass exportEDGE_CLUSTER_STORAGE_CLASS=<rook-ceph-cephfs-internal>
   ```
   {: codeblock}

5. Déterminez si une route par défaut pour le {{site.data.keyword.open_shift}} registre d'images a été créée de sorte qu'elle soit accessible de l'extérieur du cluster :

   ```bash
   oc get route default-route -n openshift-image-registry --template='{{ .spec.host }}'
   ```
   {: codeblock}

   Si la réponse de la commande indique que le paramètre **default-route** est introuvable, vous devez l'exposer (voir [Exposition du registre](https://docs.openshift.com/container-platform/4.6/registry/securing-exposing-registry.html) pour plus d'informations) :

   ```bash
   oc patch configs.imageregistry.operator.openshift.io/cluster --patch '{"spec":{"defaultRoute":true}}' --type=merge
   ```
   {: codeblock}

6. Récupérez le nom de la route du référentiel que vous devez utiliser :

   ```bash
   export OCP_IMAGE_REGISTRY=`oc get route default-route -n openshift-image-registry --template='{{ .spec.host }}'`
   ```
   {: codeblock}

7. Créez un projet pour stocker vos images :

   ```bash
   export OCP_PROJECT=$AGENT_NAMESPACE oc new-project $OCP_PROJECT
   ```
   {: codeblock}

8. Créez un compte de service avec le nom de votre choix :

   ```bash
   export OCP_USER=<service-account-name>    oc create serviceaccount $OCP_USER
   ```
   {: codeblock}

9. Ajoutez un rôle à votre compte de service pour le projet en cours :

   ```bash
   oc policy add-role-to-user edit system:serviceaccount:$OCP_PROJECT:$OCP_USER
   ```
   {: codeblock}

10. Paramétrez votre jeton de compte de service sur la variable d'environnement suivante :

   ```bash
   export OCP_TOKEN=`oc serviceaccounts get-token $OCP_USER`
   ```
   {: codeblock}

11. Obtenez le certificat {{site.data.keyword.open_shift}} et permettez à Docker de l'approuver :

   ```bash
   echo | openssl s_client -connect $OCP_IMAGE_REGISTRY:443 -showcerts | sed -n "/-----BEGIN CERTIFICATE-----/,/-----END CERTIFICATE-----/p" > ca.crt
   ```
   {: codeblock}

   Sous {{site.data.keyword.linux_notm}} :

   ```bash
   mkdir -p /etc/docker/certs.d/$OCP_IMAGE_REGISTRY cp ca.crt /etc/docker/certs.d/$OCP_IMAGE_REGISTRY systemctl restart docker.service
   ```
   {: codeblock}

   Sous {{site.data.keyword.macOS_notm}} :

   ```bash
   mkdir -p ~/.docker/certs.d/$OCP_IMAGE_REGISTRY cp ca.crt ~/.docker/certs.d/$OCP_IMAGE_REGISTRY
   ```
   {: codeblock}

   Sur {{site.data.keyword.macOS_notm}}, utilisez l'icône de bureau Docker située à droite de la barre de menus du bureau pour redémarrer Docker en cliquant sur **Redémarrer** dans le menu déroulant.

12. Connectez-vous à l'hôte Docker d'{{site.data.keyword.ocp}} :

   ```bash
   echo "$OCP_TOKEN" | docker login -u $OCP_USER --password-stdin $OCP_IMAGE_REGISTRY
   ```
   {: codeblock}

13. Configurez des magasins de clés supplémentaires pour l'accès au registre d'images :   

    ```bash
    oc create configmap registry-config --from-file=$OCP_IMAGE_REGISTRY=ca.crt -n openshift-config
    ```
    {: codeblock}

14. Editez le nouveau `registry-config` :

    ```bash
    oc edit image.config.openshift.io cluster
    ```
    {: codeblock}

15. Mettez à jour la section `spec:` :

    ```bash
    spec:additionalTrustedCA: name: registry-config
    ```
    {: codeblock}

16. Le script **agent-install.sh** stocke l'agent {{site.data.keyword.ieam}} dans le registre de conteneurs du cluster de périphérie. Définissez l'utilisateur et le mot de passe du registre, ainsi que le chemin d'accès complet (sans la balise) :

   ```bash
   export EDGE_CLUSTER_REGISTRY_USERNAME=$OCP_USER export EDGE_CLUSTER_REGISTRY_TOKEN="$OCP_TOKEN" export IMAGE_ON_EDGE_CLUSTER_REGISTRY=$OCP_IMAGE_REGISTRY/$OCP_PROJECT/amd64_anax_k8s
   ```
   {: codeblock}

   **Remarque** : l'image d'agent {{site.data.keyword.ieam}} est stockée dans le registre de cluster de périphérie local, car le cluster de périphérie Kubernetes nécessite un accès permanent à celui-ci au cas où il devrait le redémarrer ou le transférer vers un autre pod.

17. Téléchargez le script **agent-install.sh** à partir du service de synchronisation du cloud (CSS) et exécutez-le :

   ```bash
   curl -u "$HZN_ORG_ID/$HZN_EXCHANGE_USER_AUTH" -k -o agent-install.sh $HZN_FSS_CSSURL/api/v1/objects/IBM/agent_files/agent-install.sh/data   chmod +x agent-install.sh
   ```
   {: codeblock}

18. Exécutez **agent-install.sh** pour obtenir les fichiers nécessaires à partir de CSS, installez et configurez l'agent {{site.data.keyword.horizon}} et enregistrez votre cluster de périphérie avec la règle :

   ```bash
   ./agent-install.sh -D cluster -i 'css:'
   ```
   {: codeblock}

   **Remarques** :
   * Pour afficher tous les indicateurs disponibles, exécutez : **./agent-install.sh -h**
   * Si une erreur entraîne l'échec d'**agent-install.sh**, corrigez l'erreur et exécutez à nouveau **agent-install.sh**. Si cette solution ne fonctionne pas, exécutez **agent-uninstall.sh** (voir [Retrait d'un agent du cluster de périphérie](../using_edge_services/removing_agent_from_cluster.md)) avant d'exécuter à nouveau **agent-install.sh**.

19. Accédez à l'espace de nom de l'agent (également appelé projet) et vérifiez que le pod de l'agent est en cours d'exécution :

   ```bash
   oc project $AGENT_NAMESPACE    oc get pods
   ```
   {: codeblock}

20. Une fois l'agent installé sur votre cluster de périphérie, vous pouvez exécuter ces commandes si vous souhaitez vous familiariser avec les ressources Kubernetes associées à l'agent :

   ```bash
   oc get namespace $AGENT_NAMESPACE    oc project $AGENT_NAMESPACE   # ensure this is the current namespace/project    oc get deployment -o wide    oc get deployment agent -o yaml   # get details of the deployment    oc get configmap openhorizon-agent-config -o yaml    oc get secret openhorizon-agent-secrets -o yaml    oc get pvc openhorizon-agent-pvc -o yaml   # persistent volume
   ```
   {: codeblock}

21. Souvent, lorsqu'un cluster de périphérie est enregistré auprès d'une règle, mais qu'aucune règle de nœud n'est spécifiée par l'utilisateur, aucune règle de déploiement ne permet de déployer les services de périphérie sur ce cluster. C'est le cas des exemples Horizon. Passez à la section [Déploiement de services sur votre cluster de périphérie](#deploying_services) afin de définir une règle de noeud permettant de déployer un service de périphérie sur ce cluster de périphérie.

## Installation d'un agent sur des clusters de périphérie k3s et microk8s
{: #install_lite}

Ce contenu explique comment installer l'agent {{site.data.keyword.ieam}} sur des clusters Kubernetes légers et de petite taille [k3s](https://k3s.io/) ou [microk8s](https://microk8s.io/) :

1. Connectez-vous à votre cluster de périphérie en tant que **root**.

2. Si vous n'avez pas effectué les étapes de la section [Création de votre clé d'API](../hub/prepare_for_edge_nodes.md), faites-le maintenant. Ce processus crée une clé d'API, localise certains fichiers et rassemble les valeurs de variables d'environnement nécessaires lors de la définition des nœuds de périphérie. Définissez les mêmes variables d'environnement sur ce cluster de périphérie :

  ```bash
  export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>   export HZN_ORG_ID=<votre-organisation-exchange>   export HZN_FSS_CSSURL=https://<entrée-concentrateur-gestion-ieam>/edge-css/
  ```
  {: codeblock}

3. Copiez le script **agent-install.sh** dans votre nouveau cluster de périphérie.

4. Le script **agent-install.sh** stocke l'agent {{site.data.keyword.ieam}} dans le registre d'images du cluster de périphérie. Indiquez le chemin complet vers l'image (sans la balise) à utiliser. Par exemple :

   * Sous k3s :

      ```bash
      REGISTRY_ENDPOINT=$(kubectl get service docker-registry-service | grep docker-registry-service | awk '{print $3;}'):5000       export IMAGE_ON_EDGE_CLUSTER_REGISTRY=$REGISTRY_ENDPOINT/openhorizon-agent/amd64_anax_k8s
      ```
      {: codeblock}

   * Sous microk8s :

      ```bash
      export IMAGE_ON_EDGE_CLUSTER_REGISTRY=localhost:32000/openhorizon-agent/amd64_anax_k8s
      ```
      {: codeblock}

   **Remarque** : l'image d'agent {{site.data.keyword.ieam}} est stockée dans le registre de cluster de périphérie local, car le cluster de périphérie Kubernetes nécessite un accès permanent à celui-ci au cas où il devrait le redémarrer ou le transférer vers un autre pod.

5. Invitez le script **agent-install.sh** à utiliser la classe de stockage par défaut :

   * Sous k3s :

      ```bash
      export EDGE_CLUSTER_STORAGE_CLASS=local-path
      ```
      {: codeblock}

   * Sous microk8s :

      ```bash
      export EDGE_CLUSTER_STORAGE_CLASS=microk8s-hostpath
      ```
      {: codeblock}

6. Exécutez **agent-install.sh** pour obtenir les fichiers nécessaires à partir de CSS (Cloud Sync Service), installez et configurez l'agent {{site.data.keyword.horizon}} et enregistrez votre cluster de périphérie avec la règle :

   ```bash
   ./agent-install.sh -D cluster -i 'css:'
   ```
   {: codeblock}

   **Remarques** :
   * Pour afficher tous les indicateurs disponibles, exécutez : **./agent-install.sh -h**
   * Si une erreur se produit et provoque l'échec d'**agent-install.sh**, corrigez l'erreur affichée et exécutez à nouveau **agent-install.sh**. Si cette solution ne fonctionne pas, exécutez **agent-uninstall.sh** (voir [Retrait d'un agent du cluster de périphérie](../using_edge_services/removing_agent_from_cluster.md)) avant d'exécuter à nouveau **agent-install.sh**.

7. Vérifiez que le pod d'agent est en cours d'exécution :

   ```bash
   kubectl get namespaces    kubectl -n openhorizon-agent get pods
   ```
   {: codeblock}

8. Généralement, lorsqu'un cluster de périphérie est enregistré pour la règle, mais qu'il ne comporte pas de stratégie de nœud spécifiée par l'utilisateur, aucune des règles de déploiement ne déploie de services de périphérie sur ce cluster. Ceci arrive fréquemment. Passez à la section [Déploiement de services sur votre cluster de périphérie](#deploying_services) afin de définir une règle de noeud permettant de déployer un service de périphérie sur ce cluster de périphérie.

## Déploiement de services sur votre cluster de périphérie
{: #deploying_services}

La configuration d'une règle de noeud sur ce cluster de périphérie peut conduire les règles de déploiement à déployer des services de périphérie ici. Ce contenu montre un exemple de cette situation.

1. Définissez des alias afin de faciliter l'exécution de la commande `hzn`. (La commande `hzn` se trouve dans le conteneur d'agent, mais les alias permettent d'exécuter cette commande à partir de l'hôte.)

   ```bash
   cat << 'END_ALIASES' >> ~/.bash_aliases    alias getagentpod='kubectl -n openhorizon-agent get pods --selector=app=agent -o jsonpath={.items[*].metadata.name}'    alias hzn='kubectl -n openhorizon-agent exec -i $(getagentpod) -- hzn'    END_ALIASES    source ~/.bash_aliases
   ```
   {: codeblock}

2. Vérifiez que votre noeud de périphérie est configuré (enregistré auprès du concentrateur de gestion d'{{site.data.keyword.ieam}}) :

   ```bash
   hzn node list
   ```
   {: codeblock}

3. Pour tester votre agent de cluster de périphérie, définissez votre stratégie de nœud à l'aide d'une propriété qui déploie l'opérateur et le service helloworld d'exemple sur ce nœud de périphérie :

   ```bash
   cat << 'EOF' > operator-example-node.policy.json    {
     "properties": [
       { "name": "openhorizon.example", "value": "operator" }      ]
   }    EOF

   cat operator-example-node.policy.json | hzn policy update -f-    hzn policy list
   ```
   {: codeblock}

   **Remarque** :
   * Comme la commande **hzn** réelle s'exécute dans le conteneur d'agent, pour toutes les commandes `hzn` nécessitant un fichier d'entrée, vous devez diriger le fichier dans la commande afin que son contenu soit transféré dans le conteneur.

4. Au bout d'une minute, recherchez un accord ainsi que les conteneurs de l'opérateur et du service de périphérie en cours d'exécution :

   ```bash
   hzn agreement list    kubectl -n openhorizon-agent get pods
   ```
   {: codeblock}

5. A l'aide des ID de pod de la commande précédente, consultez le journal de l'opérateur et du service de périphérie :

   ```bash
   kubectl -n openhorizon-agent logs -f <operator-pod-id>    # control-c to get out    kubectl -n openhorizon-agent logs -f <service-pod-id>    # control-c to get out
   ```
   {: codeblock}

6. Vous pouvez également afficher les variables d'environnement transmises par l'agent au service de périphérie :

   ```bash
   kubectl -n openhorizon-agent exec -i <service-pod-id> -- env | grep HZN_
   ```
   {: codeblock}

### Modification des services déployés sur votre cluster de périphérie
{: #changing_services}

* Si vous voulez modifier les services qui sont déployés sur votre cluster de périphérie, modifiez la règle de noeud :

  ```bash
  cat <new-node-policy>.json | hzn policy update -f-   hzn policy list
  ```
  {: codeblock}

   Après une minute ou deux, les nouveaux services sont déployés sur ce cluster de périphérie.

* **Remarque **: Lorsque microk8s est installé sur certains types de machines virtuelles, les pods de service en cours d'arrêt (remplacement) restent bloqués à l'état **Arrêt en cours**. Si cela se produit, exécutez ce qui suit :

  ```bash
  kubectl delete pod <pod-id> -n openhorizon-agent --force --grace-period=0   pkill -fe <service-process>
  ```
  {: codeblock}

* Si vous souhaitez utiliser un pattern, au lieu d'une règle, pour exécuter des services sur votre cluster de périphérie :

  ```bash
  hzn unregister -f   hzn register -n $HZN_EXCHANGE_NODE_AUTH -p <pattern-name>
  ```
  {: codeblock}
