---
copyright: Contributors to the Open Horizon project
years: 2020 - 2026
title: Installing a K3s edge cluster
description: Documentation for Installing and configuring a K3s edge cluster
lastupdated: 2026-02-11
nav_order: 1
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

# Installing and configuring a K3s edge cluster
{: #install_k3s_edge_cluster}

## Introduction
{: #intro}

This content provides a summary of how to install k3s (rancher), a lightweight and small Kubernetes cluster, on a recent Ubuntu LTS distribution. For more information, see the [k3s documentation ](https://rancher.com/docs/k3s/latest/en/){:target="_blank"}{: .externalLink}.

## Pre-requisites
{: #reqs}

* Architecture must be either x86_64 (amd64) or arm64
* Operating system must be modern {{site.data.keyword.linux}} variant with 64-bit and systemd support

**Note**: If installed, uninstall kubectl before completing the following steps.

## Installing
{: #steps}

1. Either login as **root** or elevate to **root** with `sudo -i`

2. Confirm that the full hostname of your machine contains at least two dots:

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
   1. Create the persistent volume claim:

      ```bash
      kubectl apply -f https://raw.githubusercontent.com/open-horizon/open-horizon.github.io/master/docs/installing/k3s-persistent-claim.yaml
      ```
      {: codeblock}

   2. Verify that the persistent volume claim was created and is in "Pending" status

      ```bash
      kubectl get pvc
      ```
      {: codeblock}

   4. Create the registry deployment and service:

      ```bash
      kubectl apply -f https://raw.githubusercontent.com/open-horizon/open-horizon.github.io/master/docs/installing/k3s-registry-deployment.yaml
      ```
      {: codeblock}

   5. Verify that the service was created:

      ```bash
      kubectl get deployment
      kubectl get service
      ```
      {: codeblock}

      Which will issue a response similar to:

      ```text
      NAME              READY   UP-TO-DATE   AVAILABLE   AGE
      docker-registry   1/1     1            1           21s
      NAME                      TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
      kubernetes                ClusterIP   10.43.0.1      <none>        443/TCP          3h46m
      docker-registry-service   NodePort    10.43.46.175   <none>        5000:31466/TCP   67s
      ```

   6. Define the registry endpoint:

      ```bash
      export REGISTRY_ENDPOINT=$(kubectl get service docker-registry-service | grep docker-registry-service | awk '{print $3;}'):5000
      ```
      {: codeblock}

      To verify that it was set properly:

      ```bash
      echo $REGISTRY_ENDPOINT
      ```

      Which will respond with something similar to:

      ```text
      10.43.46.175:5000
      ```

   7. Add it to K3s configuration:

      ```bash
      cat << EOF >> /etc/rancher/k3s/registries.yaml
      mirrors:
        "$REGISTRY_ENDPOINT":
          endpoint:
            - "http://$REGISTRY_ENDPOINT"
      EOF

      ```
      {: codeblock}

      To verify that it wrote the file properly:

      ```bash
      cat /etc/rancher/k3s/registries.yaml
      ```

      Which will respond with something similar to:

      ```text
      mirrors:
        "10.43.46.175:5000":
          endpoint:
            - "http://10.43.46.175:5000"
      ```

   8. Restart k3s to pick up the change to the K3s configuration:

      ```bash
      systemctl restart k3s
      ```
      {: codeblock}

5. Define this registry in {{site.data.keyword.docker}} as an insecure registry:

   1. Install {{site.data.keyword.docker}} (if not already installed):

      NOTE: If `docker --version` responds with a version number, then it is installed.

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

   3. Restart {{site.data.keyword.docker}} to pick up the change:

      ```bash
      systemctl restart docker
      ```
      {: codeblock}

## What's next

* [Installing the edge cluster agent](./edge_cluster_agent.md)
