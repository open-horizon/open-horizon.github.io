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

* Installation de l'un des types de clusters de périphérie suivants :
  * [Installation d'un cluster de périphérie OCP](#install_ocp_edge_cluster)
  * [Installation et configuration d'un cluster de périphérie k3s](#install_k3s_edge_cluster)
  * [Installation et configuration d'un cluster de périphérie microk8s](#install_microk8s_edge_cluster) (pour les phases de développement et de test, mais non de production)
* [Collecte des informations et des fichiers nécessaires aux clusters de périphérie](#gather_info)

## Installation d'un cluster de périphérie OCP
{: #install_ocp_edge_cluster}

1. Installez OCP en suivant les instructions d'installation de la [documentation {{site.data.keyword.open_shift_cp}} ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://docs.openshift.com/container-platform/4.4/welcome/index.html).

2. Installez l'interface de ligne de commande Kubernetes (**kubectl**) et l'interface de ligne de commande du client Openshift (**oc**) sur l'hôte admin à partir duquel vous administrez votre cluster OCP (le même hôte que celui à partir duquel vous exécuterez le script d'installation de l'agent). Voir [Installation de cloudctl, kubectl et oc](../installing/cloudctl_oc_cli.md).

## Installation et configuration d'un cluster de périphérie k3s
{: #install_k3s_edge_cluster}

Cette section présente un résumé de la façon d'installer k3s (rancher), un cluster Kubernetes simple et léger, sous Ubuntu 18.04. (Pour des instructions détaillées, voir la [documentation k3s ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://rancher.com/docs/k3s/latest/en/).)

1. Connectez-vous en tant que **root** ou en tant que **root** avec `sudo -i`

2. Installez k3s :

   ```bash
   curl -sfL https://get.k3s.io | sh -
   ```
   {: codeblock}

3. Créez le service de registre d'images : 

   1. Créez un fichier appelé **k3s-registry-deployment.yml** avec le contenu suivant :

      ```yaml
      apiVersion: apps/v1
      kind: Deployment
      metadata:
        name: docker-registry
        labels:
          app: docker-registry
      spec:
        replicas: 1
        selector:
          matchLabels:
            app: docker-registry
        template:
          metadata:
            labels:
              app: docker-registry
          spec:
            containers:
            - name: docker-registry
              image: registry
              ports:
              - containerPort: 5000
              volumeMounts:
              - name: storage
                mountPath: /var/lib/registry
            volumes:
            - name: storage
              emptyDir: {} # FIXME: make this a persistent volume if using in production
      ---
      apiVersion: v1
      kind: Service
      metadata:
        name: docker-registry-service
      spec:
        selector:
          app: docker-registry
        type: NodePort
        ports:
          - protocol: TCP
            port: 5000
      ```
      {: codeblock}

   2. Créez le service de registre :

      ```bash
      kubectl apply -f k3s-registry-deployment.yml
      ```
      {: codeblock}

   3. Vérifiez que le service a été créé :

      ```bash
      kubectl get deployment
      kubectl get service
      ```
      {: codeblock}

   4. Définissez le noeud final du registre :

      ```bash
      export REGISTRY_ENDPOINT=$(kubectl get ep docker-registry-service | grep docker-registry-service | awk '{print $2}')
      cat << EOF >> /etc/rancher/k3s/registries.yaml
      mirrors:
        "$REGISTRY_ENDPOINT":
          endpoint:
            - "http://$REGISTRY_ENDPOINT"
      EOF
      ```
      {: codeblock}

   5. Redémarrez k3s pour appliquer les modifications apportées à **/etc/rancher/k3s/registries.yaml** :

      ```bash
      systemctl restart k3s
      ```
      {: codeblock}

4. Définissez ce registre sur Docker en tant que registre non sécurisé :

   1. Créez-le ou ajoutez-le à **/etc/docker/daemon.json** (en remplaçant la valeur de `$REGISTRY_ENDPOINT`) :

      ```json
      {
        "insecure-registries": [ "$REGISTRY_ENDPOINT" ]
      }
      ```
      {: codeblock}

   2. Redémarrez Docker pour appliquer les changements :

      ```bash
      systemctl restart docker
      ```
      {: codeblock}

## Installation et configuration d'un cluster de périphérie microk8s
{: #install_microk8s_edge_cluster}

Cette section présente un résumé de la façon d'installer microk8s, un cluster Kubernetes simple et léger, sous Ubuntu 18.04. (Pour des instructions détaillées, voir la [documentation microk8s ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://microk8s.io/docs).)

Remarque : Ce type de cluster de périphérie est conçu pour le développement et les tests, car un cluster Kubernetes d'un noeud worker unique ne fournit pas d'évolutivité ni de haute disponibilité.

1. Installez microk8s :

   ```bash
   sudo snap install microk8s --classic --channel=stable
   ```
   {: codeblock}

2. Si vous n'êtes pas connecté en tant que **root**, ajoutez votre utilisateur au groupe **microk8s** :

   ```bash
   sudo usermod -a -G microk8s $USER
   sudo chown -f -R $USER ~/.kube
   su - $USER   # create new session for group update to take place
   ```
   {: codeblock}

3. Activez les modules DNS et de stockage dans microk8s :

   ```bash
   microk8s.enable dns
   microk8s.enable storage
   ```
   {: codeblock}

4. Vérifiez le statut :

   ```bash
   microk8s.status --wait-ready
   ```
   {: codeblock}

5. La commande microK8s kubectl s'appelle **microk8s.kubectl** afin d'éviter des conflits éventuels avec une commande **kubectl** déjà installée. Si vous n'avez pas déjà installé **kubectl**, ajoutez cet alias pour **microk8s.kubectl**.

   ```bash
   echo 'alias kubectl=microk8s.kubectl' >> ~/.bash_aliases
   source ~/.bash_aliases
   ```
   {: codeblock}

6. Activez le registre de conteneur et configurez Docker pour qu'il accepte le registre non sécurisé :

   1. Activez le registre de conteneur :

      ```bash
      microk8s.enable registry
      export REGISTRY_ENDPOINT=localhost:32000
      ```
      {: codeblock}

   2. Installez Docker (si ce n'est pas déjà fait) :

      ```bash
      curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
      add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
      apt-get install docker-ce docker-ce-cli containerd.io
      ```
      {: codeblock}

   3. Définissez ce registre sur Docker en tant que registre non sécurisé. Créez-le ou ajoutez-le à **/etc/docker/daemon.json** (en remplaçant la valeur de `$REGISTRY_ENDPOINT`) :

      ```json
      {
        "insecure-registries": [ "$REGISTRY_ENDPOINT" ]
      }
      ```
      {: codeblock}

   4. Redémarrez Docker pour appliquer les changements :

      ```bash
      sudo systemctl restart docker
      ```
      {: codeblock}

## Etapes suivantes

* [Installation de l'agent](edge_cluster_agent.md)
