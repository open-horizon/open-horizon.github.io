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

Commencez par installer l'agent {{site.data.keyword.edge_notm}} sur l'un des types de clusters de périphérie Kubernetes suivants :

* [Installation d'un agent sur un cluster de périphérie Kubernetes {{site.data.keyword.ocp}}](#install_kube)
* [Installation d'un agent sur des clusters de périphérie k3s et microk8s](#install_lite)

Déployez ensuite un service de périphérie sur votre cluster de périphérie :

* [Déploiement de services sur votre cluster de périphérie](#deploying_services)

Si vous avez besoin de supprimer l'agent :

* [Retrait d'un agent du cluster de périphérie](#remove_agent)

## Installation d'un agent sur un cluster de périphérie Kubernetes {{site.data.keyword.ocp}}
{: #install_kube}

Cette section vous explique comment installer l'agent {{site.data.keyword.ieam}} sur votre cluster de périphérie {{site.data.keyword.ocp}}. Procédez comme suit sur un hôte disposant d'un accès administrateur sur votre cluster de périphérie :

1. Connectez-vous à votre cluster de périphérie en tant qu'**admin** :

   ```bash
	oc login https://<API_ENDPOINT_HOST>:<PORT> -u <ADMIN_USER> -p <ADMIN_PASSWORD> --insecure-skip-tls-verify=true
   ```
   {: codeblock}

2. Définissez la variable d'espace de nom de l'agent sur sa valeur par défaut (ou un espace de nom dans lequel vous voulez explicitement installer l'agent) :

   ```bash
   export AGENT_NAMESPACE=openhorizon-agent
   ```
   {: codeblock}

3. Choisissez la classe de stockage devant être utilisée par l'agent, à savoir une classe de stockage intégrée ou l'une de vos classes. Par exemple :

   ```bash
   export EDGE_CLUSTER_STORAGE_CLASS=rook-ceph-cephfs-internal
   ```
   {: codeblock}

4. Si vous souhaitez définir le registre d'images sur votre cluster de périphérie, effectuez les étapes 2 à 8 de la section [Utilisation du registre d'images d'OpenShift](../developing/container_registry.md##ocp_image_registry) à une différence près : à l'étape 4, définissez **OCP_PROJECT** sur **$AGENT_NAMESPACE**. 

5. Le script **agent-install.sh** stocke l'agent {{site.data.keyword.ieam}} dans le registre de conteneurs du cluster de périphérie. Configurez l'utilisateur et le mot de passe du registre, ainsi que le chemin d'accès complet vers l'image (moins la balise) que vous souhaitez utiliser :

   ```bash
   export EDGE_CLUSTER_REGISTRY_USERNAME=$OCP_USER
   export EDGE_CLUSTER_REGISTRY_TOKEN="$OCP_TOKEN"
   export IMAGE_ON_EDGE_CLUSTER_REGISTRY=$OCP_DOCKER_HOST/$OCP_PROJECT/amd64_anax_k8s
   ```
   {: codeblock}

   **Remarque** : L'image d'agent {{site.data.keyword.ieam}} est stockée dans le registre de cluster de périphérie local, car Kubernetes a besoin d'un accès permanent à celui-ci au cas où il devrait le redémarrer ou le déplacer vers un autre pod.

6. Exportez vos données d'identification d'utilisateur Horizon Exchange :

   ```bash
   export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
   ```
   {: codeblock}

7. Procurez-vous le fichier **agentInstallFiles-x86_64-Cluster.tar.gz** et une clé d'interface de programmation (clé d'API) auprès de votre administrateur. Ceux-ci doivent avoir été créés à la section [Collecte des informations et des fichiers nécessaires aux clusters de périphérie](preparing_edge_cluster.md).  

8. Extrayez le script **agent-install.sh** du fichier tar :

   ```bash
   tar -zxvf agentInstallFiles-x86_64-Cluster.tar.gz agent-install.sh
   ```
   {: codeblock}

9. Exécutez la commande **agent-install.sh** pour installer et configurer l'agent Horizon et enregistrez votre cluster de périphérie auprès de la règle :

   ```bash
   ./agent-install.sh -D cluster -z agentInstallFiles-x86_64-Cluster.tar.gz -d <node-id>
   ```
   {: codeblock}

   **Remarques :**
   * Pour afficher tous les indicateurs disponibles, exécutez : **./agent-install.sh -h**
   * Si une erreur empêche l'exécution du script **agent-install.sh**, exécutez **agent-uninstall.sh** (voir [Retrait d'un agent du cluster de périphérie](#remove_agent)) et répétez les étapes de cette section.

10. Accédez à l'espace de nom/au projet de l'agent et vérifiez que le pod d'agent est en cours d'exécution :

   ```bash
   oc project $AGENT_NAMESPACE
   oc get pods
   ```
   {: codeblock}

11. A présent que l'agent est installé sur votre cluster de périphérie, vous pouvez exécuter les commandes ci-dessous pour vous familiariser avec les ressources Kubernetes associées à l'agent :

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

12. Souvent, lorsqu'un cluster de périphérie est enregistré auprès d'une règle, mais qu'aucune règle de noeud n'est spécifiée par l'utilisateur, aucune règle de déploiement ne permet de déployer les services de périphérie sur ce cluster. C'est le cas des exemples Horizon. Passez à la section [Déploiement de services sur votre cluster de périphérie](#deploying_services) afin de définir une règle de noeud permettant de déployer un service de périphérie sur ce cluster de périphérie.

## Installation d'un agent sur des clusters de périphérie k3s et microk8s
{: #install_lite}

Cette section vous explique comment installer l'agent {{site.data.keyword.ieam}} sur k3s ou microk8s, des clusters Kubernetes simples et légers :

1. Connectez-vous à votre cluster de périphérie en tant que **root**.

2. Procurez-vous le fichier **agentInstallFiles-x86_64-Cluster.tar.gz** et une clé d'interface de programmation (clé d'API) auprès de votre administrateur. Ceux-ci doivent avoir été créés à la section [Collecte des informations et des fichiers nécessaires aux clusters de périphérie](preparing_edge_cluster.md).  

3. Extrayez le script **agent-install.sh** du fichier tar :

   ```bash
   tar -zxvf agentInstallFiles-x86_64-Cluster.tar.gz agent-install.sh
   ```
   {: codeblock}

4. Exportez vos données d'identification d'utilisateur Horizon Exchange :

   ```bash
   export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
   ```
   {: codeblock}

5. Le script **agent-install.sh** stocke l'agent {{site.data.keyword.ieam}} dans le registre d'images du cluster de périphérie. Indiquez le chemin complet vers l'image (sans la balise) à utiliser. Par exemple :

   ```bash
   export IMAGE_ON_EDGE_CLUSTER_REGISTRY=$REGISTRY_ENDPOINT/openhorizon-agent/amd64_anax_k8s
   ```
   {: codeblock}

   **Remarque** : L'image d'agent {{site.data.keyword.ieam}} est stockée dans le registre de cluster de périphérie local, car Kubernetes a besoin d'un accès permanent à celui-ci au cas où il devrait le redémarrer ou le déplacer vers un autre pod.

6. Invitez le script **agent-install.sh** à utiliser la classe de stockage par défaut :

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

7. Exécutez la commande **agent-install.sh** pour installer et configurer l'agent Horizon et enregistrez votre cluster de périphérie auprès de la règle :

   ```bash
   ./agent-install.sh -D cluster -z agentInstallFiles-x86_64-Cluster.tar.gz -d <node-id>
   ```
   {: codeblock}

   **Remarques :**
   * Pour afficher tous les indicateurs disponibles, exécutez : **./agent-install.sh -h**
   * Si une erreur empêche l'exécution du script **agent-install.sh**, exécutez **agent-uninstall.sh** (voir [Retrait d'un agent du cluster de périphérie](#remove_agent)) avant d'exécuter à nouveau **agent-install.sh**.

8. Vérifiez que le pod d'agent est en cours d'exécution :

   ```bash
   kubectl get namespaces
   kubectl -n openhorizon-agent get pods
   ```
   {: codeblock}

9. Souvent, lorsqu'un cluster de périphérie est enregistré auprès d'une règle, mais qu'aucune règle de noeud n'est spécifiée par l'utilisateur, aucune règle de déploiement ne permet de déployer les services de périphérie sur ce cluster. C'est le cas des exemples Horizon. Passez à la section [Déploiement de services sur votre cluster de périphérie](#deploying_services) afin de définir une règle de noeud permettant de déployer un service de périphérie sur ce cluster de périphérie.

## Déploiement de services sur votre cluster de périphérie
{: #deploying_services}

La configuration d'une règle de noeud sur ce cluster de périphérie peut conduire les règles de déploiement à déployer des services de périphérie ici. Cette section montre un exemple de cette situation.

1. Définissez des alias afin de faciliter l'exécution de la commande `hzn`. (La commande `hzn` se trouve dans le conteneur d'agent, mais les alias permettent d'exécuter cette commande à partir de l'hôte.)

   ```bash
   cat << 'END_ALIASES' >> ~/.bash_aliases
   alias getagentpod='kubectl -n openhorizon-agent get pods --selector=app=agent -o jsonpath={.items[*].metadata.name}'
   alias hzn='kubectl -n openhorizon-agent exec -i $(getagentpod) -- hzn'
   END_ALIASES
   source ~/.bash_aliases
   ```
   {: codeblock}

2. Vérifiez que votre noeud de périphérie est configuré (enregistré auprès du concentrateur de gestion d'{{site.data.keyword.ieam}}) :

   ```bash
   hzn node list
   ```
   {: codeblock}

3. Si vous souhaitez tester l'agent de votre cluster de périphérie, définissez votre règle de noeud avec une propriété permettant de déployer l'exemple d'opérateur et de service helloworld sur ce noeud de périphérie :

   ```bash
   cat << 'EOF' > operator-example-node.policy.json
   {
     "properties": [
       { "name": "openhorizon.example", "value": "operator" }
     ]
   }
   EOF

   cat operator-example-node.policy.json | hzn policy update -f-
   hzn policy list
   ```
   {: codeblock}

   **Remarque :**
   * La commande **hzn** réelle s'exécutant dans le conteneur d'agent, pour toutes les sous-commandes `hzn`, qui nécessitent un fichier d'entrée, vous devez établir un pipe entre le fichier et la commande pour que son contenu soit transféré dans le conteneur.

4. Au bout d'une minute, recherchez un accord ainsi que les conteneurs de l'opérateur et du service de périphérie en cours d'exécution :

   ```bash
   hzn agreement list
   kubectl -n openhorizon-agent get pods
   ```
   {: codeblock}

5. A l'aide des ID de pod de la commande précédente, consultez le journal de l'opérateur et du service de périphérie :

   ```bash
   kubectl -n openhorizon-agent logs -f <operator-pod-id>
   # control-c to get out
   kubectl -n openhorizon-agent logs -f <service-pod-id>
   # control-c to get out
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
  cat <new-node-policy>.json | hzn policy update -f-
  hzn policy list
  ```
  {: codeblock}

   Après une minute ou deux, les nouveaux services sont déployés sur ce cluster de périphérie.

* Remarque : Lorsque microk8s est installé sur certains types de machines virtuelles, les pods de service en cours d'arrêt (remplacement) restent bloqués à l'état **Arrêt en cours**. Si cela se produit, supprimez-les en exécutant :

  ```bash
  kubectl delete pod <pod-id> -n openhorizon-agent --force --grace-period=0
  pkill -fe <service-process>
  ```
  {: codeblock}

* Si vous souhaitez utiliser un pattern, au lieu d'une règle, pour exécuter des services sur votre cluster de périphérie :

  ```bash
  hzn unregister -f
  hzn register -n $HZN_EXCHANGE_NODE_AUTH -p <pattern-name>
  ```
  {: codeblock}

## Retrait d'un agent du cluster de périphérie
{: #remove_agent}

Pour annuler l'enregistrement d'un cluster de périphérie et retirer l'agent d'{{site.data.keyword.ieam}} de ce cluster, procédez comme suit :

1. Extrayez le contenu du script **agent-uninstall.sh** du fichier tar :

   ```bash
   tar -zxvf agentInstallFiles-x86_64-Cluster.tar.gz agent-uninstall.sh
   ```
   {: codeblock}

2. Exportez vos données d'identification d'utilisateur Horizon Exchange :

   ```bash
   export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
   ```
   {: codeblock}

3. Supprimez l'agent :

   ```bash
   ./agent-uninstall.sh -u $HZN_EXCHANGE_USER_AUTH -d
   ```
   {: codeblock}

Remarque : Il arrive parfois que la suppression de l'espace de nom se bloque à l'état "Arrêt en cours". Si cela se produit, consultez la rubrique [A namespace is stuck in the Terminating state ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.1.1/troubleshoot/ns_terminating.html) pour supprimer manuellement l'espace de nom.
