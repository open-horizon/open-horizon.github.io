---
copyright: Contributors to the Open Horizon project
years: 2020 - 2025
title: Installing a microk8s edge cluster
description: Documentation for Installing and configuring a microk8s edge cluster
lastupdated: 2025-05-03
nav_order: 2
parent: Preparing an edge cluster
has_children: False
has_toc: False
grand_parent: Edge clusters
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Installing and configuring a microk8s edge cluster
{: #install_microk8s_edge_cluster}

## Introduction
{: #intro}

This content provides a summary of how to install microk8s, a lightweight and small Kubernetes cluster, on an Ubuntu Linux AMD64-based system. (For more detailed instructions, see the [microk8s documentation ](https://microk8s.io/docs){:target="_blank"}{: .externalLink}.)

## Pre-requisites
{: #reqs}

* Architecture must be x86_64
* Operating system must be an Ubuntu LTS distribution

**Note**: This type of single node edge cluster is meant for development and test only. A single worker node Kubernetes cluster does not provide the scalability or high availability performance characteristics that a production system should have.

## Installing
{: #steps}

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

3. Enable "dns" and "storage" modules in microk8s:

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

   3. For more information about Kubernetes DNS, see the [Kubernetes documentation ](https://kubernetes.io/docs/tasks/administer-cluster/dns-custom-nameservers/){:target="_blank"}{: .externalLink}.


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

6. Enable the container registry and configure Docker to tolerate the insecure registry:

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

   4. Restart docker to pick up the change:

      ```bash
      sudo systemctl restart docker
      ```
      {: codeblock}

## What's next

* [Installing the Cluster Agent](./edge_cluster_agent.md)
