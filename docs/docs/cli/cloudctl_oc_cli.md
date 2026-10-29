---
copyright: Contributors to the Open Horizon project
years: 2020 - 2026
title: Installing cloudctl, kubectl, and oc
description: Documentation for Installing cloudctl, kubectl, and oc
lastupdated: 2025-05-03
nav_order: 3
parent: CLI
---

# Installing cloudctl, kubectl, and oc

Follow these steps to install the command line tools that are needed to manage aspects of the Open Horizon (Open Horizon) management hub and edge clusters:

## cloudctl

1. Browse your Open Horizon web UI at: `https://<CLUSTER_URL>/common-nav/cli`

2. Expand the **IBM Cloud Pak CLI** section and select your **OS**.

3. Copy the displayed **curl** command and run it to download the **cloudctl** binary.

4. Make the file executable and move it to **/usr/local/bin**:

   ```bash
   chmod 755 cloudctl-*
   sudo mv cloudctl-* /usr/local/bin/cloudctl
   ```

5. Ensure **/usr/local/bin** is in your PATH and then verify that **cloudctl** is working:

   ```bash
   cloudctl --help
   ```

## oc

1. Download the OpenShift Container Platform CLI tar file from [OpenShift client CLI (oc) ](https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest/). Select the file **openshift-client-\*-\*.tar.gz** for your operating system.

2. Find the downloaded tar file and unpack it:

   ```bash
   tar -zxvf openshift-client-*-*.tar.gz
   ```

3. Move the **oc** command to **/usr/local/bin**:

   ```bash
   sudo mv oc /usr/local/bin/
   ```

4. Ensure **/usr/local/bin** is in your PATH and verify that **oc** is working:

   ```bash
   oc --help
   ```

Alternatively, use [homebrew ](https://brew.sh/) to install **oc** on macOS:

   ```bash
   brew install openshift-cli
   ```

## Kubectl

Follow the instructions in [Install and Set Up kubectl ](https://kubernetes.io/docs/tasks/tools/install-kubectl/).
