---

copyright:
years: 2020 - 2022
lastupdated: "2022-03-17"
title: "Preparing an edge cluster"

parent: Edge clusters
nav_order: 1
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Preparing an edge cluster
{: #preparing_edge_cluster}

Perform the following tasks to install an edge cluster and get it ready for the {{site.data.keyword.edge_notm}} agent:

Install one of these edge clusters and prepare it for the {{site.data.keyword.edge_notm}} agent:
- [Preparing an edge cluster](#preparing_edge_cluster)
  - [Install an OCP edge cluster](#install_ocp_edge_cluster)
  - [Install and configure a k3s edge cluster](#install_k3s_edge_cluster)
  - [Install and configure a microk8s edge cluster](#install_microk8s_edge_cluster) (for development and test, not recommended for production)
  - [What's next](#whats-next)

## Install an OCP edge cluster
{: #install_ocp_edge_cluster}

1. Install OCP by following the installation instructions in the [{{site.data.keyword.open_shift_cp}} Documentation ](https://docs.openshift.com/container-platform/4.6/welcome/index.html){:target="_blank"}{: .externalLink}. ({{site.data.keyword.ieam}} only supports OCP on x86_64 platforms.)

2. Install the Kubernetes CLI (**kubectl**), Openshift client CLI (**oc**) and Docker on the admin host where you administer your OCP edge cluster. This is the same host where you run the agent installation script. For more information, see [Installing cloudctl, kubectl, and oc](../cli/cloudctl_oc_cli.md).

## Install and configure a k3s edge cluster
{: #install_k3s_edge_cluster}

This content provides a summary of how to install k3s (rancher), a lightweight and small Kubernetes cluster, on Ubuntu 18.04. For more information, see the [k3s documentation ](https://rancher.com/docs/k3s/latest/en/){:target="_blank"}{: .externalLink}.

**Note**: If installed, uninstall kubectl before completing the following steps.

1. Either login as **root** or elevate to **root** with `sudo -i`

2. The full hostname of your machine must contain at least two dots. Check the full hostname:

   ```bash
   hostname
   ```
    {: codeblock}

   If the full hostname of your machine contains fewer than two dots, change the hostname:

   ```bash
   hostnamectl set-hostname <your-new-hostname-with-2-dots>
   ```
   {: codeblock}

   For more information, see [github issue ](https://github.com/rancher/k3s/issues/53){:target="_blank"}{: .externalLink}.

3. Install k3s:

   ```bash
   curl -sfL https://get.k3s.io | sh -
   ```
   {: codeblock}

4. Create the image registry service:
   1. Create a file called **k3s-persistent-claim.yml** with this content:
      ```yaml
      apiVersion: v1
      kind: PersistentVolumeClaim
      metadata:
        name: docker-registry-pvc
      spec:
        storageClassName: "local-path"
        accessModes:
          - ReadWriteOnce
        resources:
          requests:
            storage: 10Gi
      ```
      {: codeblock}

   2. Create the persistent volume claim:

      ```bash
      kubectl apply -f k3s-persistent-claim.yml
      ```
      {: codeblock}

   3. Verify that the persistent volume claim was created and it is in "Pending" status

      ```bash
      kubectl get pvc
      ```
      {: codeblock}

   4. Create a file called **k3s-registry-deployment.yml** with this content:

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
            volumes:
            - name: registry-pvc-storage
              persistentVolumeClaim:
                claimName: docker-registry-pvc
            containers:
            - name: docker-registry
              image: registry
              ports:
              - containerPort: 5000
              volumeMounts:
              - name: registry-pvc-storage
                mountPath: /var/lib/registry
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

   5. Create the registry deployment and service:

      ```bash
      kubectl apply -f k3s-registry-deployment.yml
      ```
      {: codeblock}

   6. Verify that the service was created:

      ```bash
      kubectl get deployment
      kubectl get service
      ```
      {: codeblock}

   7. Define the registry endpoint:

      ```bash
      export REGISTRY_ENDPOINT=$(kubectl get service docker-registry-service | grep docker-registry-service | awk '{print $3;}'):5000
      cat << EOF >> /etc/rancher/k3s/registries.yaml
      mirrors:
        "$REGISTRY_ENDPOINT":
          endpoint:
            - "http://$REGISTRY_ENDPOINT"
      EOF
      ```
      {: codeblock}

   8. Restart k3s to pick up the change to **/etc/rancher/k3s/registries.yaml**:

      ```bash
      systemctl restart k3s
      ```
      {: codeblock}

5. Define this registry to docker as an insecure registry:

   1. Create or add to **/etc/docker/daemon.json** (replacing `<registry-endpoint>` with the value of the `$REGISTRY_ENDPOINT` environment variable you obtained in a previous step).

      ```json
      {
        "insecure-registries": [ "<registry-endpoint>" ]
      }
      ```
      {: codeblock}

   2. (optional) If needed, verify that docker is on your machine:

      ```bash
      curl -fsSL get.docker.com | sh
      ```
      {: codeblock}

   3. Restart docker to pick up the change:

      ```bash
      systemctl restart docker
      ```
      {: codeblock}

## Install and configure a microk8s edge cluster
{: #install_microk8s_edge_cluster}

This content provides a summary of how to install microk8s, a lightweight and small Kubernetes cluster, on Ubuntu 18.04. (For more detailed instructions, see the [microk8s documentation](https://microk8s.io/docs).)

**Note**: This type of edge cluster is meant for development and test because a single worker node Kubernetes cluster does not provide scalability or high availability.

1. Install microk8s:

   ```bash
   sudo snap install microk8s --classic --channel=stable
   ```
   {: codeblock}

2. If you are not running as **root**, add your user to the **microk8s** group:

   ```bash
   sudo usermod -a -G microk8s $USER
   sudo chown -f -R $USER ~/.kube
   su - $USER   # create new session for group update to take place
   ```
   {: codeblock}

3. Enable dns and storage modules in microk8s:

   ```bash
   microk8s.enable dns
   microk8s.enable storage
   ```
   {: codeblock}

   **Note**: Microk8s uses `8.8.8.8` and `8.8.4.4` as upstream name servers by default. If these name servers cannot resolve the management hub hostname, you must change the name servers that microk8s is using:

   1. Retrieve the list of upstream name servers in `/etc/resolv.conf` or `/run/systemd/resolve/resolv.conf`.

   2. Edit `coredns` configmap in the `kube-system` namespace. Set the upstream nameservers in the `forward` section.

      ```bash
      microk8s.kubectl edit -n kube-system cm/coredns
      ```
      {: codeblock}

   3. For more information about Kubernetes DNS, see the [Kubernetes documentation](https://kubernetes.io/docs/tasks/administer-cluster/dns-custom-nameservers/).


4. Check the status:

   ```bash
   microk8s.status --wait-ready
   ```
   {: codeblock}

5. The microK8s kubectl command is called **microk8s.kubectl** to prevent conflicts with an already installed **kubectl** command. Assuming that  **kubectl** is not installed, add this alias for **microk8s.kubectl**:

   ```bash
   echo 'alias kubectl=microk8s.kubectl' >> ~/.bash_aliases
   source ~/.bash_aliases
   ```
   {: codeblock}

6. Enable the container registry and configure docker to tolerate the insecure registry:

   1. Enable the container registry:

      ```bash
      microk8s.enable registry
      export REGISTRY_ENDPOINT=localhost:32000
      export REGISTRY_IP_ENDPOINT=$(kubectl get service registry -n container-registry | grep registry | awk '{print $3;}'):5000
      ```
      {: codeblock}

   2. Install docker (if not already installed):

      ```bash
      curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
      add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
      apt-get install docker-ce docker-ce-cli containerd.io
      ```
      {: codeblock}

   3. Define this registry as insecure to docker. Create or add to **/etc/docker/daemon.json** by replacing `<registry-endpoint>` with the `$REGISTRY_ENDPOINT` environment variable value that you obtained in a previous step. Also, replace `<registry-ip-endpoint>` with the value of the `$REGISTRY_IP_ENDPOINT` environment variable value that you obtained in a previous step.

      ```json
      {
        "insecure-registries": [ "<registry-endpoint>", "<registry-ip-endpoint>" ]
      }
      ```
      {: codeblock}

   4. (optional) Verify that docker is on your machine:

      ```bash
      curl -fsSL get.docker.com | sh
      ```
      {: codeblock}

   5. Restart docker to pick up the change:

      ```bash
      sudo systemctl restart docker
      ```
      {: codeblock}

## What's next

* [Installing the agent](edge_cluster_agent.md)
