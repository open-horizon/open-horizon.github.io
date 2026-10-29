# Advanced manual device agent installation and registration

This content describes each manual step to install the Open Horizon agent on an edge device and register it. For a more automated method, see [Automated agent installation and registration](https://open-horizon.github.io/docs/installing/automated_install/index.md).

## Installing the agent

**Note**: For more information about command syntax, see [Conventions used in this document](https://open-horizon.github.io/docs/getting_started/document_conventions/index.md).

1. Obtain the `agentInstallFiles-<edge-device-type>.tar.gz` file before you continue and the API Key that is created along with this file before continuing this process.

   As a post-configuration step for [Installing the management hub](https://open-horizon.github.io/docs/hub/online_installation/index.md), a compressed file was created for you. This file that contains the necessary files to install the Horizon agent on your edge device and register it with the helloworld example.

1. Copy this file to the edge device with a USB stick, the secure copy command, or another method.

1. Expand the tar file:

```
tar -zxvf agentInstallFiles-<edge-device-type>.tar.gz
```

1. Use whichever following section that applies to your type of edge device.

**Note**: If your Linux® is not one of the supported distributions and it supports containers, see [Container Agent Installation](https://open-horizon.github.io/docs/anax/docs/agent_container_manual_deploy/index.md) for instructions about how to use the containerized agent.

### Installing the agent on Linux® (ARM 32-bit, ARM 64-bit, ppc64le, or x86_64) edge devices or virtual machines

Follow these steps:

1. Log in, and if you are logged in as a non-root user, switch to a user with root privileges:

```
sudo -s
```

1. Query the OCI container runtime version to check whether it is recent enough:

1. Docker®

   ```
   docker --version
   ```

   If docker is not installed, or the version is older than `18.06.01`, install the most recent version of Docker®.

   ```
   curl -fsSL get.docker.com | sh
   docker --version
   ```

1. Podman (Red Hat Enterprise Linux® or Fedora)

   ```
   podman --version
   ```

   If podman is not installed, or the version is older than `4.0`, install the most recent version of Podman.

   ```
   dnf install podman netavark
   podman --version
   ```

   Switch the network stack from CNI to Netavark. The Horizon agent requires the network backend to be configured to use netavark instead of cni so that the agent can set up networking scenarios such as dependent services between containers. Follow the steps in the Red Hat documentation [switching the network stack](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html-single/building_running_and_managing_containers/index#proc_switching-the-network-stack-from-cni-to-netavark_assembly_setting-container-network-modes) chapter.

1. Install the Horizon packages that you copied to this edge device:

1. For Debian / Ubuntu distributions:

   ```
   apt update && apt install ./*horizon*.deb
   ```

1. For Red Hat Enterprise Linux® or Fedora distributions:

   ```
   yum install ./*horizon*.rpm
   ```

1. Set your specific information as environment variables:

```
eval export $(cat agent-install.cfg)
```

1. Point your edge device Horizon agent to your Open Horizon cluster by populating `/etc/default/horizon` with the correct information:

```
sed -i.bak -e "s|^HZN_EXCHANGE_URL=[^ ]*|HZN_EXCHANGE_URL=${HZN_EXCHANGE_URL}|g" -e "s|^HZN_FSS_CSSURL=[^ ]*|HZN_FSS_CSSURL=${HZN_FSS_CSSURL}|g" /etc/default/horizon
```

1. Have the horizon agent trust `agent-install.crt`:

```
if grep -qE '^HZN_MGMT_HUB_CERT_PATH=' /etc/default/horizon; then sed -i.bak -e "s|^HZN_MGMT_HUB_CERT_PATH=[^ ]*|HZN_MGMT_HUB_CERT_PATH=${PWD}/agent-install.crt|" /etc/default/horizon; else echo "HZN_MGMT_HUB_CERT_PATH=${PWD}/agent-install.crt" >> /etc/default/horizon; fi
```

1. Restart the agent to pick up the changes to `/etc/default/horizon`:

```
systemctl restart horizon.service
```

1. Verify that the agent is running and correctly configured:

```
hzn version
hzn exchange version
hzn node list
```

The output should look similar to this example (version numbers and URLs might be different):

```
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

1. If you previously switched to the privileged shell, exit it now. You do not need root access for the next step of registering your device.

```
exit
```

1. Continue on to [Registering the agent](#agent_reg).

### Installing the agent on a macOS (Intel® or Apple Silicon M1 / M2) edge device

1. Import the `horizon-cli` package certificate into your macOS keychain:

```
sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain horizon-cli.crt
```

```
  **Note**: You need to complete this step only one time on each macOS machine. With this trusted certificate imported, you can install any future version of the Horizon software.
```

1. Install the Horizon CLI package:

```
sudo installer -pkg horizon-cli-*.pkg -target /
```

1. Enable subcommand name completion for the `hzn` command, by adding the following to `~/.bashrc`:

```
source /usr/local/share/horizon/hzn_bash_autocomplete.sh
```

1. When you are installing a **new device**, this step is not necessary. But if you installed and started the Horizon container on this machine previously, stop it now by running:

```
horizon-container stop
```

1. Set your specific information as environment variables:

```
eval export $(cat agent-install.cfg)
```

1. Point your edge device Horizon agent to your Open Horizon cluster by populating `/etc/default/horizon` with the correct information:

```
sudo mkdir -p /etc/default

sudo sh -c "cat << EndOfContent > /etc/default/horizon
HZN_EXCHANGE_URL=$HZN_EXCHANGE_URL
HZN_FSS_CSSURL=$HZN_FSS_CSSURL
HZN_MGMT_HUB_CERT_PATH=${PWD}/agent-install.crt
HZN_DEVICE_ID=$(hostname)
EndOfContent"
```

1. Start the Horizon agent:

```
horizon-container start
```

1. Verify that the agent is running and correctly configured:

```
hzn version
hzn exchange version
hzn node list
```

The output should look similar to this (version numbers and URLs might be different):

```
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

1. Continue on to [Registering the agent](#agent_reg).

## Registering the agent

1. Set your specific information as **environment variables**:

```
eval export $(cat agent-install.cfg)

# or 

export HZN_ORG_ID=<your-exchange-organization>
export HZN_EXCHANGE_USER_AUTH=<authentication string>
export HZN_EXCHANGE_URL= # example http://open-horizon.lfedge.iol.unh.edu:3090/v1
export HZN_FSS_CSSURL= # example http://open-horizon.lfedge.iol.unh.edu:9443/
export HZN_AGBOT_URL= # example http://open-horizon.lfedge.iol.unh.edu:3111
export HZN_FDO_SVC_URL= # example http://open-horizon.lfedge.iol.unh.edu:9008/api
```

1. View the list of sample edge service deployment patterns:

```
hzn exchange pattern list IBM/
```

1. The helloworld edge service is the most basic example, which makes it a good place to begin. **Register** your edge device with Horizon to run the **helloworld deployment pattern**:

```
hzn register -p IBM/pattern-ibm.helloworld
```

**Note**: The node ID shown in the output in the line that starts with **Using node ID**.

1. The edge device will make an agreement with one of the Horizon agreement bots (this process typically takes about 15 seconds). **Repeatedly query the agreements** of this device until the `agreement_finalized_time` and `agreement_execution_start_time` fields are complete:

```
hzn agreement list
```

1. **After the agreement is made**, list the docker container edge service that started as a result:

```
sudo docker ps
```

1. View the helloworld edge service **output**:

```
sudo hzn service log -f ibm.helloworld
```

## What to do next

Navigate to [CPU usage to IBM Event Streams](https://open-horizon.github.io/docs/using_edge_services/cpu_load_example/index.md) to continue with other edge service examples.
