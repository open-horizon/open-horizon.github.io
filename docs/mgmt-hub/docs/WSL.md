# Windows WSL2 Installation Instructions

## Pre-requisites

Use a Windows computer, or download an official VM: https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/.

Ensure VxT and Virtualization enabled in BIOS

In "Control Panel" -> "Programs" -> "Turn Windows features on or off" enable the following features.  You may be required to reboot your machine or VM afterwards.
* Hyper-V
* Containers
* Virtual Machine Platform
* Windows Hypervisor Platform
* Windows Subsystem for Linux

If Windows Store has it available, install WSL2 there.  You may need to search for "Windows Subsystem" to find it.

## WSL2 is required

Note that WSL2 (i.e., version 2 of Windows Subsystemn for Linux) is required to run the Linux-based Agent on Windows 10 and 11. Virtualization support must also be enabled for WSL2. If you do not have WSL2 installed and verified, please follow the official Windows WSL2 instructions to install and verify WSL2 with an official WSL2 ubuntu image:

[https://docs.microsoft.com/en-us/windows/wsl/install](https://docs.microsoft.com/en-us/windows/wsl/install)

NOTE: Soon a version of WSL will be available in the Windows Store (without the version 2 appellation) that should also optionally allow systemd to work without third-party emulation scripts.  When that becomes available, this approach will be deprecated in favor of that.

## Docker Desktop is Required

Docker Desktop must also be installed in both Windows and in the WSL environment. Follow the official Docker instructions to install and verify Docker Desktop with WSL2:

[https://docs.docker.com/desktop/windows/install/](https://docs.docker.com/desktop/windows/install/)

## Initialization

Open CMD as Administrator

wsl --set-default-version 2
wsl --update
wsl --install -d Ubuntu-20.04

If successful, WSL will boot Ubuntu and prompt you to create a unix account and password.  Then update Ubuntu as root:

```bash
sudo -i
apt-get -y update
apt-get -y upgrade
exit
```

## Emulating `systemd`

The Open Horizon scripts use `systemd` to deploy daemon processes but the WSL2 Ubuntu image uses `init.d` as PID 1 instead of `systemd`. This prevents the installation of our daemons. A work-around, described below, simuulates a `systemd` environment inside the WSL2 Ubuntu environment when you run the "genie" command.

In a **WSL2 terminal shell**, run these commands to modify your WSL2 Ubuntu to simulate `systemd`:

```bash
sudo apt-get -y update

cd /tmp
wget --content-disposition \
  "https://gist.githubusercontent.com/djfdyuruiry/6720faa3f9fc59bfdf6284ee1f41f950/raw/952347f805045ba0e6ef7868b18f4a9a8dd2e47a/install-sg.sh"

chmod +x /tmp/install-sg.sh

/tmp/install-sg.sh && rm /tmp/install-sg.sh
```

Exit the WSL2 terminal by typing `exit` and then shutdown the WSL2 environment in the CMD shell:

```wsl --shutdown```

Now you can open a new **WSL2 terminal shell** in a Windows CMD shell being run as Administrator and simulate "systemd":

```bash
wsl -d Ubuntu-20.04
sudo -i
genie -l
```

The first time you run this, it will take awhile to complete.  It is not frozen, so don't kill the window.  At the end of the run, it may notify you about three or more "systemd" units that failed.  This is expected, and should not interfere with our task.

Test that the `systemd` support is working by running this command. It should run without error:

```sudo systemctl status time-sync.target```

### Other Required `systemd` Units?

It is recommended that you also run the command below to discover any `systemd` units that did not start up in this simulated environment:
 
```systemctl list-units --failed```

If you see any units in that list that you think are required, you may be able to fix them using recipes in this wiki:

[https://github.com/arkane-systems/genie/wiki/Systemd-units-known-to-be-problematic-under-WSL](https://github.com/arkane-systems/genie/wiki/Systemd-units-known-to-be-problematic-under-WSL)

## Prepare to Install the Management Hub

Skip this section if you will not be installing an instance of the Management Hub locally.  Alternatives include using the [LF Edge Community Lab instance](https://wiki.lfedge.org/display/LE/Open+Horizon+Management+Hub+Developer+Instance).

If you have previously setup a Management Hub on this node, use  Docker Desktop to remove all of those old containers before continuing.  

### Become `root` to install the Management Hub

In a **WSL2 terminal shell**, run 

```
sudo -i
```

### Download, modify, then run the installer

Instead of using the command shown in the main README.md to start the All-In-One setup, it is recommnded in the WSL2 environment to first install only the Manageement Hub, then separately install the Agent, if desired. Follow these steps to install the Management Hub (as `root`). First, download the installer script: 
 
```bash
curl -sSL https://raw.githubusercontent.com/open-horizon/devops/master/mgmt-hub/deploy-mgmt-hub.sh -o deploy-mgmt-hub.sh
```

Open the script in test editor of choice, set ```EXCHANGE_WAIT_ITERATIONS``` to ```120```

Run this command (as `root`) to install the Management Hub but **not** install the Agent:

```bash
./deploy-mgmt-hub.sh -A
```

Save the output of that command so you can retrieve the credentials required to interact witth youor new Management Hub. It is recommended that you create a credential file (e.g., `mycreds`) as follows, filling in values from that output:

```bash
export HZN_EXCHANGE_URL=http://127.0.0.1:3090/v1
export HZN_FSS_CSSURL=http://127.0.0.1:3090/edge-css
export HZN_ORG_ID=myorg
export HZN_DEVICE_TOKEN=<get from output>
export EXCHANGE_ROOT_PW==<get from output>
export EXCHANGE_HUB_ADMIN_PW=<get from output>
export EXCHANGE_SYSTEM_ADMIN_PW=<get from output>
export EXCHANGE_USER_ADMIN_PW=<get from output>
export HZN_EXCHANGE_USER_AUTH=admin:<get from output>
export AGBOT_TOKEN=<get from output>
export VAULT_UNSEAL_KEY=<get from output>
export VAULT_ROOT_TOKEN=<get from output>
```

## Installing the agent

Export the credentials from above into the current shell, e.g., assuming you used the filename "mycreds.env":

```bash
source mycreds.env
```

Or, if you are using the [Community Lab instance](https://wiki.lfedge.org/display/LE/Open+Horizon+Management+Hub+Developer+Instance), you will have been provided credentials like the following.  Run those:

```bash
export HZN_ORG_ID=examples
export HZN_DEVICE_TOKEN= # specify a string value for a token
export HZN_DEVICE_ID= # specify a string value for the node ID
export HZN_EXCHANGE_USER_AUTH= # place your login:password value here
export HZN_EXCHANGE_URL=http://132.177.125.232:3090/v1
export HZN_FSS_CSSURL=http://132.177.125.232:9443/
export HZN_AGBOT_URL=http://132.177.125.232:3111
export HZN_SDO_SVC_URL=http://132.177.125.232:9008/api
```

Then place the last four of those key=value pairs in a text file named "agent-install.cfg"

```text
HZN_EXCHANGE_URL=http://132.177.125.232:3090/v1
HZN_FSS_CSSURL=http://132.177.125.232:9443/
HZN_AGBOT_URL=http://132.177.125.232:3111
HZN_SDO_SVC_URL=http://132.177.125.232:9008/api
```

Last, run the installation while pointing to the "agent-install.cfg" file:

NOTE: Ensure that the below is a single line, not multiple lines.

```bash
curl -sSL https://github.com/open-horizon/anax/releases/latest/download/agent-install.sh | bash -s -- -i anax: -k ./agent-install.cfg -c css: -p IBM/pattern-ibm.helloworld -w '*' -T 120
```

To confirm that it is installed and working:

```bash
hzn version
hzn node list
hzn exchange user list
```

## WSL2 Notes

If you are getting errors running commands in your WSL2 terminal, ensure you are inside the genie (simulated `systemd`) shell by running:

```genie -b```

## Credits

Thanks to [Demopans](https://github.com/Demopans) for figuring out how to use this tooling uunder WSL2.

