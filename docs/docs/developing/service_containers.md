---
copyright: Contributors to the Open Horizon project
years: 2020 - 2026
title: Preparing to create an edge service
description: Documentation for Preparing to create an edge service
lastupdated: 2025-05-03
nav_order: 1
parent: Edge services for devices
grand_parent: Developing edge services
---

# Preparing to create an edge service

Use Open Horizon to develop services within Docker&reg; containers for your edge devices. You can use any appropriate Linux base, programming languages, libraries, or utilities to create your edge services.

After you push, sign, and publish your services, Open Horizon uses fully autonomous agents on your edge devices to download, validate, configure, install, and monitor your services.

Edge services often use cloud ingest services to store and further process edge analysis results. This process includes the development workflow for edge and cloud code.

Open Horizon is based on the open-source [Open Horizon ](https://github.com/open-horizon/) project and uses the `hzn` Horizon Linux command to run some processes.

## Before you begin

1. Configure your development host for use with Open Horizon by installing the Horizon agent on your host and register your host with Horizon exchange. See [Install the Horizon agent on your edge device and register it with the hello world example](../installing/registration.md).

2. Create a [Docker Hub ](https://hub.docker.com/) ID. This is required because the instructions in this section include publishing your service container image to Docker&reg; Hub.

## Procedure

**Note**: See [Conventions used in this document](../getting_started/document_conventions.md) for more information about command syntax.

1. When you performed the steps in [Install the Horizon agent on your edge device and register it with the hello world example](../installing/registration.md) you set your Exchange credentials. Confirm that your credentials are still set correctly by verifying that this command does not display an error:

   ```bash
   hzn exchange user list
   ```

2. If you are using macOS as your development host, configure Docker&reg; to store credentials in `~/.docker`:

   1. Open the Docker&reg; **Preferences** dialog.
   2. Uncheck **Securely store Docker&reg; logins in macOS keychain**.

      * If you cannot uncheck this box follow these steps:

        1. Check **Include VM in Time Machine backups**.
        2. Uncheck **Securely store Docker&reg; logins in macOS keychain**.
        3. (Optional) Uncheck **Include VM in Time Machine backups**.
        4. Click **Apply & Restart**.

   3. If you have a file that is called `~/.docker/plaintext-passwords.json`, remove it.

3. Log in to Docker Hub with the Docker&reg; Hub ID that you previously created:

   ```bash
   export DOCKER_HUB_ID="<dockerhubid>"
   echo "<dockerhubpassword>" | docker login -u $DOCKER_HUB_ID --password-stdin
   ```

   Output example:

   ```text
   WARNING! Your password will be stored unencrypted in ~userName/.docker/config.json.
   Configure a credential helper to remove this warning. See
   https://docs.docker.com/engine/reference/commandline/login/#credentials-store

   Login Succeeded
   ```

4. Create a cryptographic signing key pair. This enables you to sign services when publishing them to the exchange.

   **Note**: You only need to perform this step one time.

   ```bash
   hzn key create "<companyname>" "<youremailaddress>"
   ```

   Where `companyname` is used as the x509 organization, and `youremailaddress` is used as the x509 CN.

5. Install a few development tools:

   On **Linux** (for Ubuntu / Debian distributions):

   ```bash
   sudo apt install -y git jq make
   ```

   On **Linux** (Red Hat Enterprise Linux&reg; or Fedora distributions):

   ```bash
   sudo dnf install git jq make
   ```

   On **macOS**:

   ```bash
   brew install git jq make
   ```

   **Note**: See [homebrew ](https://brew.sh/) for details about installing brew if needed.

## What to do next

* Use your credentials and signing key to complete the [development examples](developing.md#edge_devices_ex_examples). These examples show you how to build simple edge services and learn the basics for developing for Open Horizon.
* If you already have a docker image that you want Open Horizon to deploy to edge nodes, see [Transform image to edge service](transform_image.md).
