---
copyright:
years: 2025
lastupdated: "2025-04-11"
title: "All-in-One Mgmt Hub"

parent: Management Hub
nav_order: 2
---
# Horizon Management Hub

## <a id="deploy-all-in-one">Deploy All-in-One Horizon Management Hub, Agent and CLI</a>

This enables you to quickly set up a host with all of the Open Horizon components to facilitate learning and doing development.

Read the notes and then run the following command to deploy the Horizon components on your current host.

**Notes:**

- Currently **only supported on Fedora 36+, Red Hat Enterprise Linux 8.x+ ppc64le, Ubuntu 20.x+, and {{site.data.keyword.macOS_notm}}**
- This script is not yet compatible with Docker installed via Snap. If Docker has already been installed via Snap, remove the existing Docker snap and allow the script to reinstall the latest version of Docker.
- The {{site.data.keyword.macOS_notm}} support is considered **experimental** due to this [docker bug](https://github.com/docker/for-mac/issues/3499). Making some of the recommended changes to my Docker version and settings enables progress past the problem.
- Support for Windows Subsystem for Linux (WSL 1&2) should also considered **experimental** at this time. WSL2's Ubuntu is based on `init.d` instead of the `systemd` used in standard Ubuntu distributions. The Open Horizon Agent requires `systemd` support so workarounds will simulate systemd usiing [this script](https://gist.githubusercontent.com/djfdyuruiry/6720faa3f9fc59bfdf6284ee1f41f950/raw/952347f805045ba0e6ef7868b18f4a9a8dd2e47a/install-sg.sh). This technique may not be stable and reliable.
- Deployments can be customized by overriding environment variables in [deploy-mgmt-hub.sh](https://github.com/open-horizon/devops/blob/master/mgmt-hub/deploy-mgmt-hub.sh). The variables can be found near the top of the script, right after the usage message and command line parsing code.
All `*_PW` and `*_TOKEN` environment variables and variables in the form `VAR_NAME=${VAR_NAME:-defaultvalue}` can be overridden.

Preparation required for **Windows** operating systems:

In order to use this tooling on Windows, you must be running Windows 10 or greater with WSL2 installed. Please follow [these instructions](WSL.md) to prepare your WSL2 environment before proceeding with the steps below.

As **root** run:

```bash
curl -sSL https://raw.githubusercontent.com/open-horizon/devops/master/mgmt-hub/deploy-mgmt-hub.sh | bash
```

### <a id="setup-vm-requirements">System Requirements</a>

The All-in-One environment is intended for use on devices or virtual machines with **at least 4GB RAM and 20GB of storage space**.

Ubuntu Server 20.04 and 22.04 are the preferred operating systems for evaluating and learning Open Horizon for now. You can download Ubuntu Server from [Ubuntu Releases](https://releases.ubuntu.com/).

If you wish to use the All-in-One environment in a virtual machine, please read the [VM setup notes](#setup-vm) further down for details.

### <a id="all-in-one-what-next">What To Do Next</a>

#### Run the Automated Tests

After the Horizon components have been successfully deployed, you can verify that all components are functioning correctly by running the automated tests. Before doing that, you must set the variables for any passwords and tokens that `deploy-mgmt-hub.sh` generated (displayed in its output), and any variables that you overrode. You can set them one of two ways:

1. Export the variables and then run the tests:

   ```bash
   ./test-mgmt-hub.sh
   ```

2. Or set the variables in a config file and pass the file to the test script:

   ```bash
   ./test-mgmt-hub.sh -c <config-file>
   ```

If all tests passed, you will see a green `OK` as the last line of output. Next you can manually run the following commands to learn how to use Horizon:

#### Open Horizon Agent Commands

Note: If you used the `deploy-mgmt-hub.sh -A` flag, the commands in this section won't be available.

- View the status of your edge node: `hzn node list`
- View the agreement that was made to run the helloworld edge service example: `hzn agreement list`
- View the edge service containers that Horizon started: `docker ps`
- View the log of the helloworld edge service: `hzn service log -f ibm.helloworld`
- View the Horizon configuration: `cat /etc/default/horizon`
- View the Horizon agent daemon status: `systemctl status horizon`
- View the steps performed in the agreement negotiation process: `hzn eventlog list`
- View the node policy that was set that caused the helloworld service to deployed: `hzn policy list`

#### Open Horizon Exchange Commands

To view resources in the Horizon exchange, first export environment variables `HZN_ORG_ID` and `HZN_EXCHANGE_USER_AUTH` as instructed in the output of `deploy-mgmt-hub.sh`. Then you can run these commands:

- View all of the `hzn exchange` sub-commands available: `hzn exchange --help`
- View the example edge services: `hzn exchange service list IBM/`
- View the example patterns: `hzn exchange pattern list IBM/`
- View the example deployment policies: `hzn exchange deployment listpolicy`
- Verify the policy matching that resulted in the helloworld service being deployed: `hzn deploycheck all -b policy-ibm.helloworld_1.0.0`
- View your node: `hzn exchange node list`
- View your user in your org: `hzn exchange user list`
- Use the verbose flag to view the exchange REST APIs the `hzn` command calls, for example: `hzn exchange user list -v`
- View the public files in CSS that `agent-install.sh` can use to install/register the agent on edge nodes: `hzn mms -o IBM -u "$HZN_ORG_ID/$HZN_EXCHANGE_USER_AUTH" object list -d -t agent_files`
- Create an MMS file:

  ```bash
  cat << EOF > mms-meta.json
  {
    "objectID": "mms-file",
    "objectType": "stuff",
    "destinationOrgID": "$HZN_ORG_ID",
    "destinationType": "pattern-ibm.helloworld"
  }
  EOF
  echo -e "foo\nbar" > mms-file
  hzn mms object publish -m mms-meta.json -f mms-file
  ```

- View the meta-data of the file: `hzn mms object list -d`
- Get the file: `hzn mms object download -t stuff -i mms-file -f mms-file.downloaded`

#### Open Horizon Exchange System Org Commands

You can view more resources in the system org by switching to the admin user in that org:

```bash
export HZN_ORG_ID=IBM   # or whatever org name you customized EXCHANGE_SYSTEM_ORG to
export HZN_EXCHANGE_USER_AUTH=admin:<password>   # the pw the script displayed, or what you set EXCHANGE_SYSTEM_ADMIN_PW to
```

Then you can run these commands:

- View the user in the system org: `hzn exchange user list`
- View the agbot: `hzn exchange agbot list`
- View the deployment policies the agbot is serving: `hzn exchange agbot listdeploymentpol agbot`
- View the patterns the agbot is serving: `hzn exchange agbot listpattern agbot`

#### Open Horizon Hub Admin Commands

The hub admin can manage Horizon organizations (creating, reading, updating, and deleting them). Switch to the hub admin user:

```bash
export HZN_ORG_ID=root
export HZN_EXCHANGE_USER_AUTH=hubadmin:<password>   # the pw the script displayed, or what you set EXCHANGE_HUB_ADMIN_PW to
```

Then you can run these commands:

- List the organizations: `hzn exchange org list`
- Create a new organization: `hzn exchange org create -d 'my new org' -a IBM/agbot myneworg`
- Configure the agbot to be able to use the example services from this org: `hzn exchange agbot addpattern IBM/agbot IBM '*' myneworg`
- View the patterns the agbot is serving: `hzn exchange agbot listpattern IBM/agbot`
- View the deployment policies the agbot is serving: `hzn exchange agbot listdeploymentpol IBM/agbot`

#### Adding More Edge Devices

You can install additional edge devices and connect them to this Horizon management hub. To enable this, the management hub needs to be listening on an IP address that is reachable by the edge devices and be using HTTPS (unless your management hub and edge devices are all behind a firewall). If you used the default value for `HZN_LISTEN_IP` (127.0.0.1) and `HZN_TRANSPORT` (http) when you initially installed the management hub, you need to reconfigure it:

```bash
./deploy-mgmt-hub.sh -S   # stop the mgmt hub services (but keep the data)
export HZN_LISTEN_IP=<external-ip>   # an IP address the edge devices can reach
export HZN_TRANSPORT=https
./deploy-mgmt-hub.sh
```

Then on each edge node:

```bash
export HZN_ORG_ID=myorg   # or whatever you customized it to
export HZN_EXCHANGE_USER_AUTH=admin:<admin-pw>   # use the pw deploy-mgmt-hub.sh displayed
export HZN_FSS_CSSURL=http://<mgmt-hub-ip>:9443/
curl -sSL https://github.com/open-horizon/anax/releases/latest/download/agent-install.sh | bash -s -- -i anax: -k css: -c css: -p IBM/pattern-ibm.helloworld -w '*' -T 120
```

When complete, you can run `hzn exchange node list` to see your new nodes.

### <a id="try-sdo">Try Out FDO</a>

[The LF Edge FDO project](https://www.lfedge.org/projects/securedeviceonboard/) (FIDO Device Onboard) codebase is embedded in Open Horizon and their technology can configure an edge device and register it with a Horizon instance automatically. Although this is not necessary in this all-in-one environment (because the agent has already been registered), you can easily try out FDO to see it working.

**Note:** FDO is currently only supported in this all-in-one environment on Fedora 36+ and Ubuntu 20.04+. Currently, TLS/https is not supported.

Export these environment variables:

```bash
export HZN_EXCHANGE_USER_AUTH=admin:<password> # FDO Owner Companion Service APIs authenticate and authorize against the Exchange.
```

Optional environment variables:

```bash
export FDO_MFG_DB_PASSWORD=password # <password>. FDO Manufecturer Service database user's password. Generated by default.
export FDO_MFG_SVC_AUTH=apiUser:password # apiUser:<password>. FDO Manufacturer Service API credentials. Generated by default.
export FIDO_DEVICE_ONBOARD_REL_VER=1.1.5 # <version>. https://github.com/fido-device-onboard/release-fidoiot/releases. Only touch if you know what you are doing. All FDO Services and Device must run with the same Intel released version. Do not mix and match versions.
export HZN_ORG_ID=myorg # <organization>. Preset, change only if you customized it in the deploy-mgmt.sh script.
export SUPPORTED_REDHAT_VERSION_APPEND=38 # Fedora and RHEL. <Distro version>. Used by the agent-install.sh script. May be needed for recently released Fedora versions.
```

Run the FDO test script. If you overrode any variables when running `deploy-mgmt-hub.sh`, pass those same variable values to `test-fdo.sh`, by either exporting them or putting them in a config file that you pass to `test-fdo.sh` using the `-c` flag.

```bash
./test-fdo.sh
```

You will see the script do these steps:

- Unregister the Agent (so FDO can register it)
- Verify the FDO Management Hub component is functioning properly
- Verify the FDO Rendezvous Service is functioning properly
- Create a FDO Manufacturer Service instance.
- Configure this host as a simulated FDO-enabled device
- Import the voucher of this device into the FDO management hub component
- Initiate Transfer of Ownership 0 (TO0) protocol.
- Simulate the booting of this device and completing its ownership transfer. This will also verify the Agent has already been installed, and then register it for the helloworld edge service example.

### <a id="all-in-one-pause">"Pausing" the Horizon management hub services</a>

The Horizon management hub services and edge agent use some CPU even in steady state. If you don't need them for a period of time, you can stop the containers by running:

```bash
./deploy-mgmt-hub.sh -S
```

When you want to use the Horizon management hub services and edge agent again, you can start them by running:

```bash
./deploy-mgmt-hub.sh -s
```

### <a id="all-in-one-remove">Removing the Horizon management hub services</a>

If you don't need the Horizon management hub services, or you would like to upgrade them, you can stop and remove the containers by running:

```bash
./deploy-mgmt-hub.sh -SP
```

To clean up any configuration information from the previous running instance, remove the volume:

```bash
docker volume prune -af
```

NOTE: If you do not prune the volume from the previous instance, any new install process may fail or enter an unstable state.

## <a id="setup-vm">Setting up a VM for the All-in-One Environment</a>

Using a Virtual Machine (VM) allows you to learn and experiment with Open Horizon in a safe, controlled environment without affecting your host system. This requires the use of virtualization software that is easily obtainable or even integrated into your host's operating system.

[VirtualBox](#setup-vm-vbox) and [QEMU](#setup-vm-qemu-kvm-boxes) are two popular open-source choices.

#### <a id="setup-vm-vbox">VirtualBox</a>

Oracle VM [VirtualBox](https://www.virtualbox.org/wiki/Downloads) is a virtualization application that runs on {{site.data.keyword.macOS_notm}}, Solaris and Windows as well as Linux.
Its Virtual Machine Manager user interface has a reasonable learning curve for beginners while keeping advanced settings within easy reach.

The Open Horizon website has [a video](/common-requests/install/) detailing the process of setting up a VM in VirtualBox for use with the All-in-One environment.

This is a summary of the setup process:

To create a VM, click on the New button in the VirtualBox Manager's toolbar, then use the settings below as prompted.

Option | Choice
-------|-------
Name and operating system | Set `Name` to personal preference[^vbox-vmname]
Memory size | 4096 MB
Hard disk | `Create a virtual hard disk now`
Hard disk file type | `VDI`
Storage on physical hard disk | `Fixed size`[^vbox-fixedsize]
File location and size | Set Size to 20GB, leave the location unchanged unless advised otherwise.

After the creating the VM, select it on the left hand pane in the VirtualBox Manager, then click on Settings in the toolbar to open up the VM's settings. Make the following changes:

Setting | Choice
--------|-------
General > Advanced | Set `Shared Clipboard` to `Host to Guest`[^vbox-clipboard]
System > Motherboard | Unselect `Floppy`[^vbox-nofloppy]
Network > Adapter 1 | Set `Attached to` to `Bridged Adapter` to share network with host

[^vbox-vmname]: VirtualBox will attempt to set the correct `Type` based on keywords used in the VM's Name. Include the word 'Ubuntu' in the name and VirtualBox will set the `Type` to `Ubuntu`.

[^vbox-fixedsize]: Either setting works, `Fixed Size` has better performance.

[^vbox-clipboard]: Optional. Shared Clipboard allows you to copy and paste commands into the VM through the VM's monitor (this can also be done via SSH).

[^vbox-nofloppy]: It is also good idea to disable unused devices.

#### <a id="setup-vm-fedora">Virtualization on Fedora family distributions</a>

Software stack:
 1. KVM (Kernel-based Virtual Machine): Hypervisor built into the Linux kernel.
    - https://wiki.archlinux.org/title/KVM
 2. QEMU: A generic and open source machine emulator and virtualizer.
    - https://wiki.archlinux.org/title/QEMU
 3. libvirt: A collection of software that provides a convenient way to manage virtual machines and other virtualization functionality
    - https://wiki.archlinux.org/title/Libvirt
 4. virt-manager: A graphical user front end for the Libvirt library which provides virtual machine management services.
    - https://wiki.archlinux.org/title/Virt-Manager
 5. OVMF (Open Virtual Machine Firmware):  A project to enable UEFI support for virtual machines. (Optional)
    - https://wiki.archlinux.org/title/PCI_passthrough_via_OVMF
    - https://wiki.archlinux.org/title/PCI_passthrough_via_OVMF/Examples


```bash
# Via individual packages
sudo dnf install edk2-ovmf libguestfs-tools libvirt python3-libguestfs qemu virt-manager virt-viewer virt-top
```

```bash
# Via package group
sudo dnf install edk2-ovmf libguestfs-tools python3-libguestfs virt-top @virtualization
```

Creating a VM:

1. Follow setup [instructions](https://docs.fedoraproject.org/en-US/quick-docs/getting-started-with-virtualization/)
2. Download a .iso image of Fedora, RHEL, or Ubuntu.
3. [Creating Guests with virt-manager](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/virtualization_deployment_and_administration_guide/sect-creating_guests_with_virt_manager)
   1. Local install media (ISO image or CDROM)
      - (Optional) Choose the operating system you are installing. If undetected.
   2. Memory: `4096` MB
   3. CPUs: Ideally `4`+, This can be further tweaked 
   4. Create a disk image for the virtual machine: `20.0` GB
   5. Name
   6. (Optional) Network selection. If you need to.
   7. (Optional) Customize configuration before install. For OVMF/VFIO/performance. 
      - **NOTE** Chipset and Firmware cannot be changed after VM creation. Change these now if you need to.
      - Outside of the Chipset and Firmware most other seetings and options can be edited at anytime after.
   8. Finish
   9. Customize configuration screen. If selected.
      - Overview
        - Chipset: `Q35` (recommended)
        - Firmware: `UEFI ...`. Based on your needs. Needed for PCI passthrough functions.
      - CPUs (Performance)
        - Configuration
          - `host-passthrough`. Type-in if needed.
        - Topology
          - Manually set CPU Topology
            - Sockets: `1`. Host socket number
            - Cores: `4`. Host core count
            - Threads: `2`. Host threads per core. Beware mixed core CPUs.
      - Disk 1 (Performance)
        - Disk bus: `VirtIO`.
      - Add Hardware. If needed.
   10. Begin Installation.

The first boot of the VM always defaults to the installation media. Every other boot after defaults to the VM's disk.

Running the VM:
1. When booting the VM select `Open` button from the action bar in the Virtual Machine Manager.
2. Select the `Power on the virtual machine` button from the VM's opened window.
3. Shutdown like you normally would. Windows will remain open after the guest terminates.

#### <a id="setup-vm-qemu-kvm-boxes">QEMU with GNOME Boxes</a>

The QEMU virtualization software is preinstalled on most major GNU/Linux distributions.
There are several ways to use QEMU, from third-party VM managers to the command line, but GNOME Boxes is one of the simplest.

Please note that GNOME Boxes is generally only available on GNU/Linux distributions running the GNOME desktop environment. Fedora, Ubuntu, CentOS and RHEL are some distributions that use GNOME by default.

To create a VM in Boxes:

1. Click on the + button on the upper left to start the VM creation process.
2. When the `Create a Virtual Machine` page appears, scroll down and select `Operating System Image File`. In the file browser that appears, navigate to a directory containing an Ubuntu image file and select the image file.
   - Alternatively, Boxes can download the image files for you. Select `Operating System Download`, and on the next page, type 'Ubuntu'. The image file list should show only Ubuntu image files in clear view.
   - Image files downloaded by Boxes are saved to the `Downloads` folder in your `home` directory (i.e. `~/Downloads`).
3. On the `Review and Create` page click `Customize` to reveal options for your VM.
   - Set `Memory` to 4GB and `Maximum Disk Size` to 20GB.
4. Click Create on the upper right corner of the page. The new VM will start automatically after it is created.
5. For subsequent runs, click on the VM you just created in on the main screen to run it.
   - To rename the VM you just created, right-click it in the main screen and select `Properties`. In the dialog box that appears, type a new name into the `Name` field.
   - Advanced users can fine-tune the VM by editing its XML configuration file. To access this, go to the `System` tab and click on `Edit XML`.

All new VMs are configured with bridged networking and thus share the same network as the host.

### <a id="install-os">Installing Ubuntu for the All-in-One Environment</a>

Ubuntu image files (or ISOs) may be configured to use one of these installers:

- [Subiquity](#install-os-subiquity) (identified by a black background and an orange top)

- [Debian-style](#install-os-debstyle) (with a purple background and grey dialog boxes)

#### <a id="install-os-subiquity">Subiquity Installer</a>

Choose the following options when prompted, when installing with Subiquity:

Option | Choice
-----------------|--------------------
Language[^ubuntu-lang] | `English` or `English (UK)`
Installer Update | `Update to the new installer`
Keyboard configuration\* | Whatever most appropriate for your system
Network connections | Use defaults. Change as advised if using a custom network configuration.
Configure proxy | Leave blank if your internet connection does not use a proxy. Otherwise, change the `proxy address` as advised.
Ubuntu archive mirror | Use defaults unless advised otherwise
Guided storage configuration | Use defaults
Storage configuration | Use defaults. Confirm the 'destructive action'.
Profile setup | Use your personal preferences
SSH setup | Enable `Install OpenSSH` server, do not `Import SSH Identities`.
Featured Server Snaps | Do not select any Snaps

Please wait until the entire installation process is complete, including updates.
Only skip updates if the update stalls for an unreasonably long time. Remember to update the system afterwards if you choose to skip updates.

If prompted, press Enter to reboot.

#### <a id="install-os-debstyle">Debian-style Installer</a>

Choose the following options when prompted, when using the Debian-style installer:

Option | Choice
-----------------|--------------------
Select a Language | `English`[^ubuntu-lang]
Select your location | Choose the country you are currently in, or `other` if it is not on the list[^ubuntu-location]
Configure the keyboard (multiple dialogs) | Whatever most appropriate for your system
Configure the network (Hostname) | Use your personal preference, or as advised
Set up users and passwords (multiple dialogs) | Use your personal preferences
Configure the clock | Whatever most appropriate for your location
Partition disks | `Guided - use entire disk`, or as advised
Partition disks (select disks to partition) | Choose the only option, or as advised
Partition disks (write the changes to disks) | `Yes`
Configure the package manager (HTTP proxy) | Leave blank if your internet connection does not use a proxy. Otherwise, change the `proxy address` as advised.
Configuring tasksel (automatic updates) | `No automatic updates`, or as advised
Software selection | Select `OpenSSH server` only
Install the GRUB boot loader... | `Yes`

On the last `Installation complete` dialog box, select `Continue`.

[^ubuntu-lang]: Other languages have not been tested, but no compatibility issues are expected

[^ubuntu-location]: The location list changes according to the language you have selected

#### <a id="install-os-first-run">Ubuntu Server Notes</a>

The first boot after installation may be slow.  A VM may appear to be unresponsive and present a blank screen for up to a few minutes. A login prompt should soon appear.

Log events may be printed over the login prompt and appear to interfere with username and password entry. If this happens, disregard the events and enter your username and password as normal.

Run this command to start a manual update:

```bash
sudo apt-get -y update
```

Once you have set up your VM, you are ready to deploy the all-in-one environment. Instructions are at [the top of this file](#deploy-all-in-one).

#### <a id="vm-ssh">Using SSH with your VM</a>

If your VM is correctly set up with the OpenSSH server, and an SSH client is correctly set up on your host, you can log in to your VM from a terminal on your host by running:

```bash
ssh ohguru@192.168.122.57
```

if you set your username to `ohguru`, and your VM has an IPv4 address at `192.168.122.57`. Notice how the user and hostname in the terminal changed when you log on to your VM. You can return to the host with the `exit` command, or by pressing `Control-D`.

SSH has performance advantages over using a VM monitor, and enables copy-pasting with the VM without the need for additional software in the VM.
