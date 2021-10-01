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

# Installation d'un agent et enregistrement d'un cluster de périphérie
{: #importing_clusters}

Vous pouvez installer des agents sur les clusters de périphérie suivants :

* Kubernetes
* Kubernetes léger et simplifié (recommandé aux fins de tests)

## Installation des agents sur des dispositifs de périphérie Kubernetes
{: #install_kube}

Vous pouvez installer un agent automatisé à l'aide du script `agent-install.sh`. 

Suivez les étapes ci-dessous dans l'environnement d'exécution du script d'installation de l'agent :

1. Procurez-vous le fichier `agentInstallFiles-x86_64-Cluster.tar.gz` et une clé d'interface de programmation (clé d'API) auprès de votre administrateur. Ceux-ci doivent avoir été créés à la section [Collecte des informations et des fichiers nécessaires aux clusters de périphérie](preparing_edge_cluster.md).  

2. Définissez le nom de fichier dans une variable d'environnement pour les étapes suivantes :

   ```
   export AGENT_TAR_FILE=agentInstallFiles-x86_64-Cluster.tar.gz
   ```
   {: codeblock}

3. Extrayez les fichiers du fichier tar :

   ```
   tar -zxvf agentInstallFiles-x86_64-Cluster.tar.gz
   ```
   {: codeblock}

4. Exportez vos données d'identification d'utilisateur Exchange, qui pourraient avoir l'une des formes suivantes :

   ```
   export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
   ```
   {: codeblock}

   ou

   ```
   export HZN_EXCHANGE_USER_AUTH=<username>/<username>:<password>
   ```
   {: codeblock}

5. Exécutez la commande `agent-install.sh` pour installer et configurer l'agent Horizon et pour enregistrer votre cluster de périphérie afin qu'il exécute l'exemple de service de périphérie helloworld :

   ```
   ./agent-install.sh -u $HZN_EXCHANGE_USER_AUTH -k agent-install.cfg  -D cluster -p
   ```
   {: codeblock}

   Remarque : Lors de l'installation de l'agent, il se peut que le système vous demande si vous voulez écraser Horizon : **Do you want to overwrite horizon?[y/N]: **. Sélectionnez **y** et appuyez sur **Entrée** ; `agent-install.sh` définit la configuration de manière appropriée.

6. (Facultatif) Pour afficher les descriptions d'indicateurs `agent-install.sh` disponibles : 

   ```
   ./agent-install.sh -h
   ```
   {: codeblock}

7. Affichez la liste des ressources d'agent s'exécutant sur Kubernetes. A présent que l'agent est installé sur votre cluster de périphérie et que ce dernier est enregistré, vous pouvez afficher la liste des ressources de cluster de périphérie suivantes :

   * Espace de nom :

   ```
   kubectl get namespace openhorizon-agent
   ```
   {: codeblock}

   * Déploiement :

   ```
   kubectl get deployment -n openhorizon-agent
   ```
   {: codeblock}

   Pour afficher les détails du déploiement de l'agent :

   ```
   kubectl get deployment -n openhorizon-agent -o yaml
   ```
   {: codeblock}

   * Configmap :

   ```
   kubectl get configmap openhorizon-agent-config -n openhorizon-agent -o yaml
   ```
   {: codeblock}

   * Secret :
   
   ```
   kubectl get secret openhorizon-agent-secrets -n openhorizon-agent -o yaml
   ```
   {: codeblock}

   * PersistentVolumeClaim :
   
   ```
   kubectl get pvc openhorizon-agent-pvc -n openhorizon-agent -o yaml
   ```
   {: codeblock}

   * Pod :

   ```
   kubectl get pod -n openhorizon-agent
   ```
   {: codeblock}

8. Affichez les journaux, procurez-vous l'ID du pod et exécutez : 

   ```
   kubectl logs <pod-id> -n openhorizon-agent
   ```
   {: codeblock}

9. Exécutez la commande `hzn` depuis le conteneur d'agent :

   ```
   kubectl exec -it <pod-id> -n openhorizon-agent /bin/bash
   hzn --help
   ```
   {: codeblock}

10. Examinez les indicateurs de la commande `hzn` et la sous-commande :

   ```
   hzn --help
   ```
   {: codeblock}

## Installation des agents sur des clusters de périphérie simples et légers Kubernetes

Cette section vous explique comment installer un agent dans microk8s, un cluster Kubernetes simple et léger que vous pouvez installer et configurer localement, ainsi que les tâches suivantes :

* Installation et configuration de microk8s
* Installation d'un agent sur microk8s

### Installation et configuration de microk8s

1. Installez microk8s :

   ```
   sudo snap install microk8s --classic --channel=1.14/stable
   ```
   {: codeblock}

2. Définissez un alias pour microk8s.kubectl :

   Remarque : Vérifiez de ne pas utiliser la commande `kubectl` si vous voulez tester sur microk8s. 

  * MicroK8s utilise une commande kubectl avec espace de nom afin d'éviter les conflits éventuels avec les installations existantes de kubectl. Il est plus facile d'ajouter un alias (`append to ~/.bash_aliases`) si vous n'avez aucune installation existante : 
   
   ```
   alias kubectl='microk8s.kubectl' 
   ```
   {: codeblock}
  
   * Exécutez ensuite la commande ci-dessous :

   ```
   source ~/.bash_aliases
   ```
   {: codeblock}

3. Activez le dns et le module de stockage dans microk8s :

   ```
   microk8s.enable dns storage
   ```
   {: codeblock}

4. Créez la classe de stockage dans microk8s. Le script d'installation de l'agent utilise `gp2` comme classe de stockage par défaut pour la réservation de volume persistant. Cette classe de stockage doit être créée dans l'environnement microk8s avant d'installer l'agent. Si l'agent de cluster de périphérie utilise une autre classe de stockage, celle-ci doit également avoir été créée à l'avance. 

   L'exemple ci-dessous illustre comment créer `gp2` comme classe de stockage :  

   1. Créez un fichier storageClass.yml : 

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

   2. Utilisez la commande `kubectl` pour créer un objet storageClass dans microk8s :

      ```
      kubectl apply -f storageClass.yml
      ```
      {: codeblock}

### Installation d'un agent sur microk8s

Suivez les étapes ci-dessous pour installer un agent sur microk8s.

1. Effectuez les [étapes 1 à 3](#install_kube).

2. Exécutez la commande `agent-install.sh` pour installer et configurer l'agent Horizon et pour enregistrer votre cluster de périphérie afin qu'il exécute l'exemple de service de périphérie helloworld :

   ```
   source agent-install.sh -u $HZN_EXCHANGE_USER_AUTH -k agent-install.cfg  -D cluster -p "IBM/pattern-ibm.helloworld"
   ```
   {: codeblock}

   Remarque : Lors de l'installation de l'agent, il se peut que le système vous demande si vous voulez écraser Horizon : **Do you want to overwrite horizon?[y/N]: **. Sélectionnez **y** et appuyez sur **Entrée** ; `agent-install.sh` définit la configuration de manière appropriée.

## Retirez l'agent du cluster léger Kubernetes 

Remarque : Le script d'installation de l'agent n'étant pas complet dans cette édition, le retrait de l'agent s'effectue en supprimant l'espace de nom openhorizon-agent.

1. Supprimez l'espace de nom comme suit :

   ```
   kubectl delete namespace openhorizon-agent
   ```
   {: codeblock}

      Remarque : Il arrive parfois que la suppression de l'espace de nom se bloque à l'état "Arrêt en cours". Si cela se produit, consultez la rubrique [A namespace is stuck in the Terminating state ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.1.1/troubleshoot/ns_terminating.html) pour supprimer manuellement l'espace de nom.

2. Supprimez clusterrolebinding : 

   ```
   kubectl delete clusterrolebinding openhorizon-agent-cluster-rule
   ```
   {: codeblock}

<!--If this installation was done as part of a prerequisite for {{site.data.keyword.edge_devices_notm}}, [return to continue that installation](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/devices/installing/install.html).-->
