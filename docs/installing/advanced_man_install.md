---

copyright:
years: 2021
lastupdated: "2021-02-20"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Advanced manual agent installation and registration
{: #advanced_man_install}

This content describes each manual step to install the {{site.data.keyword.edge_notm}} agent on an edge device and register it. For a more automated method, see [Automated agent installation and registration](automated_install.md).
{:shortdesc}

## Installing the agent
{: #agent_install}

**Note**: For more information about command syntax, see [Conventions used in this document](../getting_started/document_conventions.md).

1. Obtain the `agentInstallFiles-<edge-device-type>.tar.gz` file before you continue and the API Key that is created along with this file before continuing this process.

    As a post-configuration step for [Installing the management hub](../hub/online_installation.md), a compressed file was created for you. This file that contains the necessary files to install the {{site.data.keyword.horizon}} agent on your edge device and register it with the helloworld example.

2. Copy this file to the edge device with a USB stick, the secure copy command, or another method.

3. Expand the tar file:

   ```bash
   tar -zxvf agentInstallFiles-<edge-device-type>.tar.gz
   ```
   {: codeblock}

4. Use whichever following section that applies to your type of edge device.

**Note**: If your Linux is not one of the supported distributions and it supports containers, see [Container Agent Installation](https://github.com/open-horizon/anax/blob/master/docs/agent_container_manual_deploy.md) for instructions about how to use the containerized agent.

### Installing the agent on Linux (ARM 32-bit, ARM 64-bit, ppc64le, or x86_64) edge devices or virtual machines
{: #agent_install_linux}

Follow these steps:

1. Log in, and if you are logged in as a non-root user, switch to a user with root privileges:

   ```bash
   sudo -s
   ```
   {: codeblock}

2. Query the Docker version to check whether it is recent enough:

   ```bash
   docker --version
   ```
   {: codeblock}

      If docker is not installed, or the version is older than `18.06.01`, install the most recent version of Docker:

   ```bash
   curl -fsSL get.docker.com | sh
   docker --version
   ```
   {: codeblock}

3. Install the Horizon packages that you copied to this edge device:

   * For Debian/Ubuntu distributions:
      ```bash
      apt update && apt install ./*horizon*.deb
      ```
      {: codeblock}

   * For Red Hat Enterprise Linux&reg; distributions:
      ```bash
      yum install ./*horizon*.rpm
      ```
      {: codeblock}
   
4. Set your specific information as environment variables:

   ```bash
   eval export $(cat agent-install.cfg)
   ```
   {: codeblock}

5. Point your edge device horizon agent to your {{site.data.keyword.edge_notm}} cluster by populating `/etc/default/horizon` with the correct information:

   ```bash
   sed -i.bak -e "s|^HZN_EXCHANGE_URL=[^ ]*|HZN_EXCHANGE_URL=${HZN_EXCHANGE_URL}|g" -e "s|^HZN_FSS_CSSURL=[^ ]*|HZN_FSS_CSSURL=${HZN_FSS_CSSURL}|g" /etc/default/horizon
   ```
   {: codeblock}

6. Have the horizon agent trust `agent-install.crt`:

   ```bash
   if grep -qE '^HZN_MGMT_HUB_CERT_PATH=' /etc/default/horizon; then sed -i.bak -e "s|^HZN_MGMT_HUB_CERT_PATH=[^ ]*|HZN_MGMT_HUB_CERT_PATH=${PWD}/agent-install.crt|" /etc/default/horizon; else echo "HZN_MGMT_HUB_CERT_PATH=${PWD}/agent-install.crt" >> /etc/default/horizon; fi
   ```
   {: codeblock}
   
7. Restart the agent to pick up the changes to `/etc/default/horizon`:

   ```bash
   systemctl restart horizon.service
   ```
   {: codeblock}

8. Verify that the agent is running and correctly configured:

   ```bash
   hzn version
   hzn exchange version
   hzn node list
   ```
   {: codeblock}  

      The output should look similar to this example (version numbers and URLs might be different):

   ```bash
   $ hzn version
   Horizon CLI version: 2.23.29
   Horizon Agent version: 2.23.29
   $ hzn exchange version
   1.116.0
   $ hzn node list
   {
         "id": "",
         "organization": null,
         "pattern": null,
         "name": null,
         "token_last_valid_time": "",
         "token_valid": null,
         "ha": null,
         "configstate": {
            "state": "unconfigured",
            "last_update_time": ""
         },
         "configuration": {
            "exchange_api": "https://9.30.210.34:8443/ec-exchange/v1/",
            "exchange_version": "1.116.0",
            "required_minimum_exchange_version": "1.116.0",
            "preferred_exchange_version": "1.116.0",
            "mms_api": "https://9.30.210.34:8443/ec-css",
            "architecture": "amd64",
            "horizon_version": "2.23.29"
         },
         "connectivity": {
            "firmware.bluehorizon.network": true,
            "images.bluehorizon.network": true
         }
      }
      ```
   {: codeblock}

9. If you previously switched to the privileged shell, exit it now. You do not need root access for the next step of registering your device.

   ```bash
   exit
   ```
   {: codeblock}

10. Continue on to [Registering the agent](#agent_reg).

### Installing the agent on a macOS edge device
{: #mac-os-x}

1. Import the `horizon-cli` package certificate into your {{site.data.keyword.macOS_notm}} keychain:

   ```bash
   sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain horizon-cli.crt
   ```
   {: codeblock}

      **Note**: You need to complete this step only one time on each {{site.data.keyword.macOS_notm}} machine. With this trusted certificate imported, you can install any future version of the {{site.data.keyword.horizon}} software.

2. Install the {{site.data.keyword.horizon}} CLI package:

   ```bash
   sudo installer -pkg horizon-cli-*.pkg -target /
   ```
   {: codeblock}

3. Enable subcommand name completion for the `hzn` command, by adding the following to `~/.bashrc`:

  ```bash
  source /usr/local/share/horizon/hzn_bash_autocomplete.sh
  ```
  {: codeblock}

4. When you are installing a **new device**, this step is not necessary. But if you installed and started the horizon container on this machine previously, stop it now by running:

  ```bash
  horizon-container stop
  ```
  {: codeblock}
5. Set your specific information as environment variables:

  ```bash
  eval export $(cat agent-install.cfg)
  ```
  {: codeblock}

6. Point your edge device horizon agent to your {{site.data.keyword.edge_notm}} cluster by populating `/etc/default/horizon` with the correct information:

  ```bash
  sudo mkdir -p /etc/default

  sudo sh -c "cat << EndOfContent > /etc/default/horizon
  HZN_EXCHANGE_URL=$HZN_EXCHANGE_URL
  HZN_FSS_CSSURL=$HZN_FSS_CSSURL
  HZN_MGMT_HUB_CERT_PATH=${PWD}/agent-install.crt
  HZN_DEVICE_ID=$(hostname)
  EndOfContent"
  ```
  {: codeblock}

7. Start the {{site.data.keyword.horizon}} agent:

  ```bash
  horizon-container start
  ```
  {: codeblock}

8. Verify that the agent is running and correctly configured:

  ```bash
  hzn version
  hzn exchange version
  hzn node list
  ```
  {: codeblock}

      The output should look similar to this (version numbers and URLs might be different):

  ```bash
  $ hzn version
  Horizon CLI version: 2.23.29
  Horizon Agent version: 2.23.29
  $ hzn exchange version
  1.116.0
  $ hzn node list
      {
         "id": "",
         "organization": null,
         "pattern": null,
         "name": null,
         "token_last_valid_time": "",
         "token_valid": null,
         "ha": null,
         "configstate": {
            "state": "unconfigured",
            "last_update_time": ""
         },
         "configuration": {
            "exchange_api": "https://9.30.210.34:8443/ec-exchange/v1/",
            "exchange_version": "1.116.0",
            "required_minimum_exchange_version": "1.116.0",
            "preferred_exchange_version": "1.116.0",
            "mms_api": "https://9.30.210.34:8443/ec-css",
            "architecture": "amd64",
            "horizon_version": "2.23.29"
         },
         "connectivity": {
            "firmware.bluehorizon.network": true,
            "images.bluehorizon.network": true
         }
      }
  ```
  {: codeblock}

9. Continue on to [Registering the agent](#agent_reg).

## Registering the agent
{: #agent_reg}

1. Set your specific information as **environment variables**:

  ```bash
  eval export $(cat agent-install.cfg)
  export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
  ```
  {: codeblock}

2. View the list of sample edge service deployment patterns:

  ```bash
  hzn exchange pattern list IBM/
  ```
  {: codeblock}

3. The helloworld edge service is the most basic example, which makes it a good place to begin. **Register** your edge device with {{site.data.keyword.horizon}} to run the **helloworld deployment pattern**:

  ```bash
  hzn register -p IBM/pattern-ibm.helloworld
  ```
  {: codeblock}

  **Note**: The node ID shown in the output in the line that starts with **Using node ID**.

4. The edge device will make an agreement with one of the {{site.data.keyword.horizon}} agreement bots (this process typically takes about 15 seconds). **Repeatedly query the agreements** of this device until the `agreement_finalized_time` and `agreement_execution_start_time` fields are complete:

  ```bash
  hzn agreement list
  ```
  {: codeblock}

5. **After the agreement is made**, list the docker container edge service that started as a result:

  ```bash
  sudo docker ps
  ```
  {: codeblock}

6. View the helloworld edge service **output**:

  ```bash
  sudo hzn service log -f ibm.helloworld
  ```
  {: codeblock}

## What to do next
{: #what_next}

Navigate to [CPU usage to IBM Event Streams](../using_edge_services/cpu_load_example.md) to continue with other edge service examples.
