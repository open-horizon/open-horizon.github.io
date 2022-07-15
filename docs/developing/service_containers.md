---

copyright:
years: 2020 - 2022
lastupdated: "2022-07-15"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Preparing to create an edge service
{: #service_containers}

Use {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) to develop services within {{site.data.keyword.docker}} containers for your edge devices. You can use any appropriate {{site.data.keyword.linux_notm}} base, programming languages, libraries, or utilities to create your edge services.
{:shortdesc}

After you push, sign, and publish your services, {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) uses fully autonomous agents on your edge devices to download, validate, configure, install, and monitor your services.

Edge services often use cloud ingest services to store and further process edge analysis results. This process includes the development workflow for edge and cloud code.

{{site.data.keyword.ieam}} is based on the open-source [{{site.data.keyword.horizon_open}} ](https://github.com/open-horizon/){:target="_blank"}{: .externalLink} project and uses the `hzn` {{site.data.keyword.horizon}} {{site.data.keyword.linux_notm}} command to run some processes.

## Before you begin
{: #service_containers_begin}

1. Configure your development host for use with {{site.data.keyword.ieam}} by installing the {{site.data.keyword.horizon}} agent on your host and register your host with {{site.data.keyword.horizon_exchange}}. See [Install the {{site.data.keyword.horizon}} agent on your edge device and register it with the hello world example](../installing/registration.md).

2. Create a [Docker Hub ](https://hub.docker.com/){:target="_blank"}{: .externalLink} ID. This is required because the instructions in this section include publishing your service container image to Docker Hub.

## Procedure
{: #service_containers_procedure}

**Note**: See [Conventions used in this document](../getting_started/document_conventions.md) for more information about command syntax.

1. When you performed the steps in [Install the {{site.data.keyword.horizon}} agent on your edge device and register it with the hello world example](../installing/registration.md) you set your Exchange credentials. Confirm that your credentials are still set correctly by verifying that this command does not display an error:

   ```bash
   hzn exchange user list
   ```
   {: codeblock}

2. If you are using {{site.data.keyword.macOS_notm}} as your development host, configure Docker to store credentials in `~/.docker`:

   1. Open the Docker **Preferences** dialog.
   2. Uncheck **Securely store Docker logins in {{site.data.keyword.macOS_notm}} keychain**.

      * If you cannot uncheck this box follow these steps:

        1. Check **Include VM in Time Machine backups**.
        2. Uncheck **Securely store Docker logins in {{site.data.keyword.macOS_notm}} keychain**.
        3. (Optional) Uncheck **Include VM in Time Machine backups**.
        4. Click **Apply & Restart**.

   3. If you have a file that is called `~/.docker/plaintext-passwords.json`, remove it.

3. Log in to Docker Hub with the Docker Hub ID that you previously created:

   ```bash
   export DOCKER_HUB_ID="<dockerhubid>"
   echo "<dockerhubpassword>" | docker login -u $DOCKER_HUB_ID --password-stdin
   ```
   {: codeblock}

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
   {: codeblock}

   Where `companyname` is used as the x509 organization, and `youremailaddress` is used as the x509 CN.

5. Install a few development tools:

   On **{{site.data.keyword.linux_notm}}** (for Ubuntu / Debian distributions):

   ```bash
   sudo apt install -y git jq make
   ```
   {: codeblock}

   On **{{site.data.keyword.linux_notm}}** ({{site.data.keyword.rhel}} or {{site.data.keyword.fedora}} distributions):

   ```bash
   sudo dnf install git jq make
   ```
   {: codeblock}

   On **{{site.data.keyword.macOS_notm}}**:

   ```bash
   brew install git jq make
   ```
   {: codeblock}

   **Note**: See [homebrew ](https://brew.sh/){:target="_blank"}{: .externalLink} for details about installing brew if needed.

## What to do next
{: #service_containers_what_next}

* Use your credentials and signing key to complete the [development examples](developing.md#edge_devices_ex_examples). These examples show you how to build simple edge services and learn the basics for developing for {{site.data.keyword.edge_notm}}.
* If you already have a docker image that you want {{site.data.keyword.edge_notm}} to deploy to edge nodes, see [Transform image to edge service](transform_image.md).
