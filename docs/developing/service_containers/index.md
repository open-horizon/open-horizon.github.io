# Preparing to create an edge service

Use Open Horizon to develop services within Docker® containers for your edge devices. You can use any appropriate Linux base, programming languages, libraries, or utilities to create your edge services.

After you push, sign, and publish your services, Open Horizon uses fully autonomous agents on your edge devices to download, validate, configure, install, and monitor your services.

Edge services often use cloud ingest services to store and further process edge analysis results. This process includes the development workflow for edge and cloud code.

Open Horizon is based on the open-source [Open Horizon](https://github.com/open-horizon/) project and uses the `hzn` Horizon Linux command to run some processes.

## Before you begin

1. Configure your development host for use with Open Horizon by installing the Horizon agent on your host and register your host with Horizon exchange. See [Install the Horizon agent on your edge device and register it with the hello world example](https://open-horizon.github.io/docs/installing/registration/index.md).
1. Create a [Docker Hub](https://hub.docker.com/) ID. This is required because the instructions in this section include publishing your service container image to Docker® Hub.

## Procedure

**Note**: See [Conventions used in this document](https://open-horizon.github.io/docs/getting_started/document_conventions/index.md) for more information about command syntax.

1. When you performed the steps in [Install the Horizon agent on your edge device and register it with the hello world example](https://open-horizon.github.io/docs/installing/registration/index.md) you set your Exchange credentials. Confirm that your credentials are still set correctly by verifying that this command does not display an error:

```
hzn exchange user list
```

1. If you are using macOS as your development host, configure Docker® to store credentials in `~/.docker`:

1. Open the Docker® **Preferences** dialog.

1. Uncheck **Securely store Docker® logins in macOS keychain**.

   - If you cannot uncheck this box follow these steps:

     1. Check **Include VM in Time Machine backups**.
     1. Uncheck **Securely store Docker® logins in macOS keychain**.
     1. (Optional) Uncheck **Include VM in Time Machine backups**.
     1. Click **Apply & Restart**.

1. If you have a file that is called `~/.docker/plaintext-passwords.json`, remove it.

1. Log in to Docker Hub with the Docker® Hub ID that you previously created:

```
export DOCKER_HUB_ID="<dockerhubid>"
echo "<dockerhubpassword>" | docker login -u $DOCKER_HUB_ID --password-stdin
```

Output example:

```
WARNING! Your password will be stored unencrypted in ~userName/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
```

1. Create a cryptographic signing key pair. This enables you to sign services when publishing them to the exchange.

**Note**: You only need to perform this step one time.

```
hzn key create "<companyname>" "<youremailaddress>"
```

Where `companyname` is used as the x509 organization, and `youremailaddress` is used as the x509 CN.

1. Install a few development tools:

On **Linux** (for Ubuntu / Debian distributions):

```
sudo apt install -y git jq make
```

On **Linux** (Red Hat Enterprise Linux® or Fedora distributions):

```
sudo dnf install git jq make
```

On **macOS**:

```
brew install git jq make
```

**Note**: See [homebrew](https://brew.sh/) for details about installing brew if needed.

## What to do next

- Use your credentials and signing key to complete the [development examples](https://open-horizon.github.io/docs/developing/developing/#edge_devices_ex_examples). These examples show you how to build simple edge services and learn the basics for developing for Open Horizon.
- If you already have a docker image that you want Open Horizon to deploy to edge nodes, see [Transform image to edge service](https://open-horizon.github.io/docs/developing/transform_image/index.md).
