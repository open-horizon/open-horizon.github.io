---

copyright:
years: 2021
lastupdated: "2021-02-20"
title: hzn CLI
description: ""
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Installing the hzn CLI
{: #using_hzn_cli}

When you install the {{site.data.keyword.ieam}} agent software on an edge node, the **hzn** CLI is automatically installed. But you can also install the **hzn** CLI without the agent. For example, an edge administrator might want to query the {{site.data.keyword.ieam}} exchange or an edge developer might want to test with **hzn dev** commands.

1. Get the **agentInstallFiles-&lt;edge-device-type&gt;.tar.gz** file from your management hub administrator, where **&lt;edge-device-type&gt;** matches the host where you installing **hzn**. They were already created in [Gather the necessary information and files for edge devices](../hub/gather_files.md#prereq_horizon). Copy this file to the host where you are installing **hzn**.

2. Set the file name in an environment variable for subsequent steps:

   ```bash
   export AGENT_TAR_FILE=agentInstallFiles-<edge-device-type>.tar.gz
   ```
   {: codeblock}

3. Extract the horizon CLI package from the tar file:

   ```bash
   tar -zxvf $AGENT_TAR_FILE 'horizon-cli*'
   ```
   {: codeblock}

   * Confirm that the package version is the same as the device agent listed in [Components](../getting_started/components.md).

4. Install the **horizon-cli** package:

   * On a debian-based distro:

     ```bash
     sudo apt update && sudo apt install horizon-cli*.deb
     ```
     {: codeblock}

   * On {{site.data.keyword.macOS_notm}}:

     ```bash
     sudo installer -pkg horizon-cli-*.pkg -target /
     ```
     {: codeblock}

     Note: On {{site.data.keyword.macOS_notm}}, you can also install the horizon-cli pkg file from Finder: Double-click the file to open the installer. If you get an error message that says the program "cannot be opened because it is from an unidentified developer," right-click the file and select **Open**. Click **Open** again when prompted "Are you sure you want to open it?". Then, follow the prompts to install the CLI horizon package, ensuring your ID has administrator privileges.

## Uninstalling the hzn CLI

If you want to remove the **horizon-cli** package from a host:

* Uninstall **horizon-cli** from a debian-based distro:

  ```bash
  sudo apt-get remove horizon-cli
  ```
  {: codeblock}

* Or uninstall **horizon-cli** from {{site.data.keyword.macOS_notm}}:

  ```bash
  sudo horizon-cli-uninstall.sh
  ```
  {: codeblock}
