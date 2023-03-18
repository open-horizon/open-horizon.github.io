---

copyright:
years: 2020 - 2023
lastupdated: "2023-03-17"
title: "Installing a K3s edge cluster"

parent: Preparing an edge cluster
nav_order: 2
has_children: false
has_toc: false

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Installing and configuring a K3s edge cluster
{: #install_k3s_edge_cluster}

## Introduction
{: #intro}

This content provides a summary of how to install k3s (rancher), a lightweight and small Kubernetes cluster, on Ubuntu Linux AMD64. For more information, see the [k3s documentation ](https://rancher.com/docs/k3s/latest/en/){:target="_blank"}{: .externalLink}.

## Pre-requisites
{: #reqs}

* Architecture must be either x86_64 or arm64
* Operating system must be modern Linux variant with 64-bit and systemd support

**Note**: If installed, uninstall kubectl before completing the following steps.

## Installing
{: #steps}

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

   1. Install docker (if not already installed):

      ```bash
      curl -fsSL get.docker.com | sh
      ```
      {: codeblock}

   2. Create or add to **/etc/docker/daemon.json** (replacing `<registry-endpoint>` with the value of the `$REGISTRY_ENDPOINT` environment variable you obtained in a previous step).

      ```json
      {
        "insecure-registries": [ "<registry-endpoint>" ]
      }
      ```
      {: codeblock}

   3. Restart docker to pick up the change:

      ```bash
      systemctl restart docker
      ```
      {: codeblock}

## What's next

* [Installing the Cluster Agent](edge_cluster_agent.md)
