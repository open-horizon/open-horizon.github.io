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

# Préparation d'un cluster de périphérie
{: #preparing_edge_cluster}

Effectuez les tâches suivantes pour installer un cluster de périphérie et le préparer en vue de son utilisation avec l'agent d'{{site.data.keyword.edge_notm}} :

Installez l'un de ces clusters de périphérie et préparez-le pour l'agent {{site.data.keyword.edge_notm}} :
* [Installation d'un cluster de périphérie OCP](#install_ocp_edge_cluster)
* [Installation et configuration d'un cluster de périphérie k3s](#install_k3s_edge_cluster)
* [Installation et configuration d'un cluster de périphérie microk8s](#install_microk8s_edge_cluster) (pour les phases de développement et de test, mais non de production)

## Installation d'un cluster de périphérie OCP
{: #install_ocp_edge_cluster}

1. Installez OCP en suivant les instructions d'installation de la [documentation {{site.data.keyword.open_shift_cp}}](https://docs.openshift.com/container-platform/4.6/welcome/index.html). ({{site.data.keyword.ieam}} prend uniquement en charge OCP sur les plateformes x86_64.)

2. Installez l'interface de ligne de commande Kubernetes (**kubectl**), l'interface de ligne de commande du client Openshift (**oc**) et Docker sur l'hôte d'administration sur lequel vous administrez votre cluster de périphérie OCP. Il s'agit du même hôte que celui sur lequel vous exécutez le script d'installation d'agent. Pour plus d'informations, voir [Installation de cloudctl, kubectl et oc](../cli/cloudctl_oc_cli.md).

## Installation et configuration d'un cluster de périphérie k3s
{: #install_k3s_edge_cluster}

Ce contenu fournit un récapitulatif de la procédure d'installation de k3s (rancher), un cluster Kubernetes léger et de petite taille, sur Ubuntu 18.04. Pour plus d'informations, voir la [documentation k3s](https://rancher.com/docs/k3s/latest/en/).

**Remarque **: S'il est installé, désinstallez kubectl avant d'effectuer les étapes suivantes.

1. Connectez-vous en tant que **root** ou en tant que **root** avec `sudo -i`

2. Le nom d'hôte complet de votre machine doit contenir au moins deux points. Vérifiez le nom d'hôte complet :

   ```bash
   hostname
   ```
    {: codeblock}

   Si le nom d'hôte complet de votre machine contient moins de deux points, changez le nom d'hôte :

   ```bash
   hostnamectl set-hostname <your-new-hostname-with-2-dots>
   ```
   {: codeblock}

   Pour plus d'informations, voir [Problème github](https://github.com/rancher/k3s/issues/53).

3. Installez k3s :

   ```bash
   curl -sfL https://get.k3s.io | sh -
   ```
   {: codeblock}

4. Créez le service de registre d'images :
   1. Créez un fichier appelé **k3s-persistent-claim.yml** avec le contenu suivant :
      ```yaml       apiVersion: v1       kind: PersistentVolumeClaim       metadata:         name: docker-registry-pvc       spec:         storageClassName: "local-path"         accessModes:
          - ReadWriteOnce         resources:           requests:             storage: 10Gi
      ```
      {: codeblock}

   2. Créez la réservation de volume persistant :

      ```bash
      kubectl apply -f k3s-persistent-claim.yml
      ```
      {: codeblock}

   3. Vérifiez que la réservation de volume persistant a été créée et se trouve à l'état "En attente" :

      ```bash
      kubectl get pvc
      ```
      {: codeblock}

   4. Créez un fichier appelé **k3s-registry-deployment.yml** avec le contenu suivant :

      ```yaml
      apiVersion: apps/v1       kind: Deployment       metadata:         name: docker-registry         labels:           app: docker-registry       spec:         replicas: 1         selector:           matchLabels:             app: docker-registry         template:           metadata:             labels:               app: docker-registry           spec:             volumes:
            - name: registry-pvc-storage               persistentVolumeClaim:                 claimName: docker-registry-pvc             containers:
            - name: docker-registry               image: registry               ports:
              - containerPort: 5000               volumeMounts:
              - name: registry-pvc-storage                 mountPath: /var/lib/registry
      ---
      apiVersion: v1       kind: Service       metadata:         name: docker-registry-service       spec:         selector:           app: docker-registry         type: NodePort         ports:
          - protocol: TCP             port: 5000
      ```
      {: codeblock}

   5. Créez le déploiement et le service du registre :

      ```bash
      kubectl apply -f k3s-registry-deployment.yml
      ```
      {: codeblock}

   6. Vérifiez que le service a été créé :

      ```bash
      kubectl get deployment       kubectl get service
      ```
      {: codeblock}

   7. Définissez le noeud final du registre :

      ```bash
      export REGISTRY_ENDPOINT=$(kubectl get service docker-registry-service | grep docker-registry-service | awk '{print $3;}'):5000       cat << EOF >> /etc/rancher/k3s/registries.yaml       mirrors:         "$REGISTRY_ENDPOINT":           endpoint:
            - "http://$REGISTRY_ENDPOINT"       EOF
      ```
      {: codeblock}

   8. Redémarrez k3s pour appliquer les modifications apportées à **/etc/rancher/k3s/registries.yaml** :

      ```bash
      systemctl restart k3s
      ```
      {: codeblock}

5. Définissez ce registre sur Docker en tant que registre non sécurisé :

   1. Créez ou ajoutez l'instruction suivante à **/etc/docker/daemon.json** (en remplaçant `<registry-endpoint>` par la valeur de la variable d'environnement `$REGISTRY_ENDPOINT` que vous avez obtenue lors d'une étape précédente).

      ```json
      {
        "insecure-registries": [ "<registry-endpoint>" ]       }
      ```
      {: codeblock}

   2. (facultatif) Si nécessaire, vérifiez que Docker se trouve sur votre machine :

      ```bash
      curl -fsSL get.docker.com | sh
      ```
      {: codeblock}     

   3. Redémarrez Docker pour appliquer les changements :

      ```bash
      systemctl restart docker
      ```
      {: codeblock}

## Installation et configuration d'un cluster de périphérie microk8s
{: #install_microk8s_edge_cluster}

Ce contenu fournit un récapitulatif de la procédure d'installation de microk8s, un petit cluster Kubernetes léger, sur Ubuntu 18.04. (Pour des instructions détaillées, voir la [documentation microk8s](https://microk8s.io/docs).)

**Remarque** : ce type de cluster de périphérie est conçu à des fins de développement et de test car un cluster Kubernetes de noeud worker unique ne permet pas l'évolutivité ou la haute disponibilité.

1. Installez microk8s :

   ```bash
   sudo snap install microk8s --classic --channel=stable
   ```
   {: codeblock}

2. Si vous n'êtes pas connecté en tant que **root**, ajoutez votre utilisateur au groupe **microk8s** :

   ```bash
   sudo usermod -a -G microk8s $USER    sudo chown -f -R $USER ~/.kube    su - $USER   # create new session for group update to take place
   ```
   {: codeblock}

3. Activez les modules DNS et de stockage dans microk8s :

   ```bash
   microk8s.enable dns    microk8s.enable storage
   ```
   {: codeblock}

   **Remarque **: Microk8s utilise par défaut `8.8.8.8` et `8.8.4.4` comme serveurs de noms en amont. Si ces serveurs de noms ne peuvent pas résoudre le nom d'hôte du concentrateur de gestion, vous devez changer les serveurs de noms que microk8s utilise :
   
   1. Accédez à la liste des serveurs de noms en amont dans `/etc/resolv.conf` ou `/run/systemd/resolve/resolv.conf`.

   2. Éditez le configmap `coredns` dans l'espace de nom `kube-system`. Définissez les serveurs de noms en amont dans la section `forward`.
   
      ```bash
      microk8s.kubectl edit -n kube-system cm/coredns
      ```
      {: codeblock}
   
   3. Pour plus d'informations sur le DNS Kubernetes, consultez la [documentation de Kubernetes](https://kubernetes.io/docs/tasks/administer-cluster/dns-custom-nameservers/).


4. Vérifiez le statut :

   ```bash
   microk8s.status --wait-ready
   ```
   {: codeblock}

5. La commande microK8s kubectl s'appelle **microk8s.kubectl** afin d'éviter des conflits éventuels avec une commande **kubectl** déjà installée. Si **kubectl** n'est pas installé, ajoutez cet alias pour **microk8s.kubectl** :

   ```bash
   echo 'alias kubectl=microk8s.kubectl' >> ~/.bash_aliases    source ~/.bash_aliases
   ```
   {: codeblock}

6. Activez le registre de conteneur et configurez Docker pour qu'il accepte le registre non sécurisé :

   1. Activez le registre de conteneur :

      ```bash
      microk8s.enable registry       export REGISTRY_ENDPOINT=localhost:32000
      ```
      {: codeblock}

   2. Installez Docker (si ce n'est pas déjà fait) :

      ```bash
      curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -       add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"       apt-get install docker-ce docker-ce-cli containerd.io
      ```
      {: codeblock}

   3. Définissez ce registre comme non sécurisé pour Docker. Créez ou ajoutez l'instruction suivante à **/etc/docker/daemon.json** (en remplaçant `<registry-endpoint>` par la valeur de la variable d'environnement `$REGISTRY_ENDPOINT` que vous avez obtenue lors d'une étape précédente).

      ```json
      {
        "insecure-registries": [ "<registry-endpoint>" ]       }
      ```
      {: codeblock}

   4. (Facultatif) Vérifiez que Docker se trouve sur votre machine :

      ```bash
      curl -fsSL get.docker.com | sh
      ```
      {: codeblock}   

   5. Redémarrez Docker pour appliquer les changements :

      ```bash
      sudo systemctl restart docker
      ```
      {: codeblock}

## Etapes suivantes

* [Installation de l'agent](edge_cluster_agent.md)
