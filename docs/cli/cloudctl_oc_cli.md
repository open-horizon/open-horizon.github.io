---

copyright:
years: 2021
lastupdated: "2021-02-20"
title: "Installing cloudctl, kubectl, and oc"
description: ""
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Installing cloudctl, kubectl, and oc

Follow these steps to install the command line tools that are needed to manage aspects of the IBM Edge Application Manager (IEAM) management hub and edge clusters:

### cloudctl

1. Browse your IEAM web UI at: https://<CLUSTER_URL>/common-nav/cli
2. Expand the __IBM Cloud Pak CLI__ section and select your __OS__.
3. Copy the displayed __curl__ command and run it to download the __cloudctl__ binary.
4. Make the file executable and move it to __/usr/local/bin__:

    ```sh
    chmod 755 cloudctl-*
    sudo mv cloudctl-* /usr/local/bin/cloudctl
    ```
5. Ensure __/usr/local/bin__ is in your PATH and then verify that cloudctl is working:

    ```sh
    cloudctl --help
    ```


### OC

1. Download the OpenShift Container Platform CLI tar file from OpenShift client CLI (oc). Select the file __openshift-client-*-*.tar.gz__ for your operating system.
2. Find the downloaded tar file and unpack it:
   
   ```sh
   tar -zxvf openshift-client-*-*.tar.gz
   ```
3. Move the oc command to __/usr/local/bin__:
   
   ```sh
   sudo mv oc /usr/local/bin/
   ```
4. Ensure /usr/local/bin is in your PATH and verify that oc is working:

    ```sh
    oc --help
    ```

Alternatively, use [homebrew](https://www.ibm.com/links?url=https%3A%2F%2Fbrew.sh%2F) to install __oc__ on macOS:

```sh
brew install openshift-cli
```

### Kubectl

Follow the instructions in [Install and Set Up kubectl](https://www.ibm.com/links?url=https%3A%2F%2Fkubernetes.io%2Fdocs%2Ftasks%2Ftools%2Finstall-kubectl%2F).