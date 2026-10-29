---
copyright: Contributors to the Open Horizon project
years: 2020 - 2026
title: Bulk device agent install
description: Documentation for Bulk agent installation and registration
lastupdated: 2026-08-20
nav_order: 5
parent: Installing edge device agents
---

# Bulk agent installation and registration {: #batch-install }

Use the bulk installation process to set up multiple edge devices of similar types (in other words, same architecture, operating system, and pattern or policy).

**Note**: For this process, target edge devices that are macOS computers are not supported. However, you can drive this process from a macOS computer, if wanted. (In other words, this host can be a macOS computer.)

### Prerequisites

- The devices to be installed and registered must have network access to the management hub.
- The devices must have an installed operating system.
- If you are using DHCP for edge devices, each device must maintain the same IP address until the task is complete (or the same `hostname` if you are using DDNS).
- All edge service user inputs must be specified as defaults in the service definition or in the pattern or deployment policy. No node-specific user inputs can be used.

### Procedure

1. If you have not obtained or created the **agentInstallFiles-&lt;edge-device-type&gt;.tar.gz** file and API key by following [Gather the necessary information and files for edge devices](../hub/gather_files.md#prereq_horizon), do that now. Set the name of the file and the API key value in these environment variables:

   ```bash
   export AGENT_TAR_FILE=agentInstallFiles-<edge-device-type>.tar.gz
   export HZN_ORG_ID=<your-exchange-organization>
   export HZN_EXCHANGE_USER_AUTH=<authentication string>
   ```

2. The **pssh** package includes the **pssh** and **pscp** commands, which enable you to run commands to many edge devices in parallel and copy files to many edge devices in parallel. If you do not have these commands on this host, install the package now:

   - On **Linux** (for Ubuntu / Debian distributions):

     ```bash
     sudo apt install pssh
     alias pssh=parallel-ssh
     alias pscp=parallel-scp
     ```

   - On **Linux** (Red Hat Enterprise Linux&reg; or Fedora distributions):

     ```bash
     sudo dnf install pssh
     ```

   - On macOS:

     ```bash
     brew install pssh
     ```

   (If **brew** is not installed yet, see [Install pssh on macOS computer with Brew ](https://macappstore.org/pssh/).)

3. You can give **pscp** and **pssh** access to your edge devices in several ways. This content describes how to use an ssh public key. First, this host must have an ssh key pair (usually in **~/.ssh/id_rsa** and **~/.ssh/id_rsa.pub**). If it does not have an ssh key pair, generate it:

   ```bash
   ssh-keygen -t rsa
   ```

4. Place the contents of your public key (**~/.ssh/id_rsa.pub**) on each edge device in **/root/.ssh/authorized_keys**.

5. Create a 2-column mapping file called **node-id-mapping.csv** that maps each edge device's IP address or hostname to the Open Horizon node name it should be given during registration. When **agent-install.sh** runs on each edge device, this file tells it what edge node name to give to that device. Use CSV format:

   ```bash
   Hostname/IP, Node Name
   1.1.1.1, factory2-1
   1.1.1.2, factory2-2
   ```

6. Add **node-id-mapping.csv** to the agent tar file:

   ```bash
   gunzip $AGENT_TAR_FILE
   tar -uf ${AGENT_TAR_FILE%.gz} node-id-mapping.csv
   gzip ${AGENT_TAR_FILE%.gz}
   ```

7. Put the list of edge devices you want to bulk install and register in a file named **nodes.hosts** . This will be used with the **pscp** and **pssh** commands. Each line should be in the standard ssh format `<user>@<IP-or-hostname>`:

   ```bash
   root@1.1.1.1
   root@1.1.1.2
   ```

   **Note**: If you use a non-root user for any of the hosts, sudo must be configured to allow sudo from that user without entering a password.

8. Copy the agent tar file to the edge devices. This step can take a few moments:

   ```bash
   pscp -h nodes.hosts -e /tmp/pscp-errors $AGENT_TAR_FILE /tmp
   ```

   **Note**: If you get **[FAILURE]** in the **pscp** output for any of the edge devices, you can see the errors in **/tmp/pscp-errors**.

9. Run **agent-install.sh** on each edge device to install the Horizon agent and register the edge devices. You can use a pattern or a policy to register the edge devices:

   1. Register the edge devices with a pattern:

      ```bash
      pssh -h nodes.hosts -t 0 "bash -c \"tar -zxf /tmp/$AGENT_TAR_FILE agent-install.sh && sudo -s ./agent-install.sh -i . -O $HZN_ORG_ID -u $HZN_EXCHANGE_USER_AUTH -p IBM/pattern-ibm.helloworld -w ibm.helloworld -o IBM -z /tmp/$AGENT_TAR_FILE 2>&1 >/tmp/agent-install.log \" "
      ```

      Instead of registering the edge devices with the **IBM/pattern-ibm.helloworld** deployment pattern, you can use a different deployment pattern by modifying the **-p**, **-w**, and **-o** flags. To see all available **agent-install.sh** flag descriptions:

      ```bash
      tar -zxf $AGENT_TAR_FILE agent-install.sh && ./agent-install.sh -h
      ```

   2. Or, register the edge devices with policy. Create a node policy, copy it to the edge devices, and register the devices with that policy:

      ```bash
      echo '{ "properties": [ { "name": "nodetype", "value": "special-node" } ] }' > node-policy.json
      pscp -h nodes.hosts -e /tmp/pscp-errors node-policy.json /tmp
      pssh -h nodes.hosts -t 0 "bash -c \"tar -zxf /tmp/$AGENT_TAR_FILE agent-install.sh && sudo -s ./agent-install.sh -i . -O $HZN_ORG_ID -u $HZN_EXCHANGE_USER_AUTH -n /tmp/node-policy.json  -z /tmp/$AGENT_TAR_FILE 2>&1 >/tmp/agent-install.log \" "
      ```

      Now the edge devices are ready, but will not start running edge services until you create a deployment policy (business policy) that specifies that a service should be deployed to this type of edge device (in this example, devices with **nodetype** of **special-node**). See [Using deployment policy](../using_edge_services/detailed_policy.md) for details.

10. If you get **[FAILURE]** in the **pssh** output for any of the edge devices, you can investigate the problem by going to the edge device and viewing **/tmp/agent-install.log** .
