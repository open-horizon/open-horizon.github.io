---

copyright:
years: 2020 - 2022
lastupdated: "2022-03-17"
title: "Installing cloudctl, kubectl, and oc"
description: ""

parent: CLI
nav_order: 3
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Installing cloudctl, kubectl, and oc
{: #cloudctl_oc_cli}

Follow these steps to install the command line tools that are needed to manage aspects of the {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) management hub and edge clusters:

## cloudctl

1. Browse your {{site.data.keyword.ieam}} web UI at: `https://&lt;CLUSTER_URL&gt;/common-nav/cli`

2. Expand the **IBM Cloud Pak CLI** section and select your **OS**.

3. Copy the displayed **curl** command and run it to download the **cloudctl** binary.

4. Make the file executable and move it to **/usr/local/bin**:
  
   ```bash
   chmod 755 cloudctl-*
   sudo mv cloudctl-* /usr/local/bin/cloudctl
   ```
   {: codeblock}

5. Ensure **/usr/local/bin** is in your PATH and then verify that **cloudctl** is working:
  
   ```bash
   cloudctl --help
   ```
   {: codeblock}

## oc

1. Download the {{site.data.keyword.open_shift_cp}} CLI tar file from [OpenShift client CLI (oc)](https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest/). Select the file **openshift-client-\*-\*.tar.gz** for your operating system.

2. Find the downloaded tar file and unpack it:
  
   ```bash
   tar -zxvf openshift-client-*-*.tar.gz
   ```
   {: codeblock}

3. Move the **oc** command to **/usr/local/bin**:
  
   ```bash
   sudo mv oc /usr/local/bin/
   ```
   {: codeblock}

4. Ensure **/usr/local/bin** is in your PATH and verify that **oc** is working:
  
   ```bash
   oc --help
   ```
   {: codeblock}

Alternatively, use [homebrew](https://brew.sh/) to install **oc** on {{site.data.keyword.macOS_notm}}:
  
   ```bash
   brew install openshift-cli
   ```
   {: codeblock}

## Kubectl

Follow the instructions in [Install and Set Up kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/).
