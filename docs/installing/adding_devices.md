---

copyright:
years: 2019 - 2022
lastupdated: "2022-05-19"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Preparing an edge device
{: #installing_the_agent}

The following instructions guide you through the process of installing the required software on your edge device and registering it with {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}).

## Supported architectures and operating systems
{: #suparch-horizon}

{{site.data.keyword.ieam}} supports architectures and operating systems with the following hardware architectures:

- x86_64
  - {{site.data.keyword.linux_bit_notm}} devices or virtual machines that run Ubuntu 22.x (jammy), Ubuntu 20.x (focal), Ubuntu 18.x (bionic), Debian 10 (buster), Debian 9 (stretch)
  - {{site.data.keyword.rhel}} 8.1, 8.2, 8.3, 8.4, 8.5 and 8.6
  - {{site.data.keyword.Fedora} Workstation 32, 36
  - CentOS 8.1, 8.2, 8.3, 8.4 and 8.5
  - SuSE 15 SP2
- ppc64le
  - {{site.data.keyword.linux_ppc64le_notm}} devices or virtual machines that run Ubuntu 20.x (focal) or Ubuntu 18.x (bionic)
  - {{site.data.keyword.rhel}} 7.6, 7.9, 8.1, 8.2, and 8.3
- ARM (32-bit)
  - {{site.data.keyword.linux_notm}} on ARM (32-bit), for example Raspberry Pi, running Raspberry Pi OS buster or bullseye
- ARM (64-bit)
  - {{site.data.keyword.linux_notm}} on ARM (64-bit), for example NVIDIA Jetson Nano, TX1, or TX2, running Ubuntu 18.x (bionic)
- Mac
  - {{site.data.keyword.macOS_notm}}

**Notes**:

- Installation of edge devices with Fedora or SuSE is only supported by the [Advanced manual agent installation and registration](../installing/advanced_man_install.md) method.
- CentOS and {{site.data.keyword.rhel}} on {{site.data.keyword.ieam}} {{site.data.keyword.version}} only support Docker as a container engine.
- While {{site.data.keyword.ieam}} {{site.data.keyword.version}} supports running {{site.data.keyword.rhel}} 8.x with Docker, it is officially unsupported by {{site.data.keyword.rhel}}.
- {{site.data.keyword.ieam}} {{site.data.keyword.version}} supports Podman 4.x on {{site.data.keyword.rhel}} 8.6 and Fedora Workstation.

## Sizing
{: #size}

The agent requires:

- 100 MB random access memory (RAM), including docker. RAM increases this amount by approximately 100 K per agreement, plus any additional memory that is required by workloads that run on the device.
- 400 MB disk (including docker). Disk increases this amount based on the size of the container images that are used by workloads and the size of the model objects (times 2) that are deployed to the device.

# Installing the agent
{: #installing_the_agent}

The following instructions guide you through the process of installing the required software on your edge device and registering it with {{site.data.keyword.ieam}}.

## Procedures
{: #install-config}

To install and configure your edge device, click the link that represents your edge device type:

- [{{site.data.keyword.linux_bit_notm}} devices or virtual machines](#x86-machines)
- [{{site.data.keyword.rhel}} 8.x devices or virtual machines](#rhel8)
- [{{site.data.keyword.linux_ppc64le_notm}} devices or virtual machines](#ppc64le-machines)
- [{{site.data.keyword.linux_notm}} on ARM (32-bit)](#arm-32-bit); for example, Raspberry Pi running Raspberry Pi OS
- [{{site.data.keyword.linux_notm}} on ARM (64-bit)](#arm-64-bit); for example, NVIDIA Jetson Nano, TX1, or TX2
- [{{site.data.keyword.macOS_notm}}](#mac-os-x)

## {{site.data.keyword.linux_bit_notm}} devices or virtual machines
{: #x86-machines}

### Hardware requirements
{: #hard-req-x86}

- 64-bit Intel&reg; or AMD device or virtual machine
- An internet connection for your device (wired or wifi)
- (optional) Sensor hardware: Many {{site.data.keyword.horizon}} edge services require specialized sensor hardware.

### Procedure
{: #proc-x86}

Prepare your device by installing a Debian, {{site.data.keyword.rhel}}, or Ubuntu {{site.data.keyword.linux_notm}}. The instructions in this content are based on a device that uses Ubuntu 18.x.

Install the most recent version of Docker or Podman on your device. For more information, see [Install Docker ](https://docs.docker.com/engine/install/ubuntu/){:target="_blank"}{: .externalLink} or [Podman.io ](https://podman.io/){:target="_blank"}{: .externalLink}.

Now that your edge device is prepared, continue on to [Installing the agent](registration.md).

## {{site.data.keyword.rhel}} 8.x devices or virtual machines
{: #rhel8}

### Hardware requirements
{: #hard-req-rhel8}

- 64-bit Intel&reg; device, AMD device, ppc64le device, or virtual machine
- An internet connection for your device (wired or wifi)
- (optional) Sensor hardware: Many {{site.data.keyword.horizon}} edge services require specialized sensor hardware.

### Procedure
{: #proc-rhel8}

Prepare your device by installing {{site.data.keyword.rhel}} 8.x.

If you are running {{site.data.keyword.rhel}} 8.6, install the podman 4.x packages by installing the container-tools:rhel8 module.

```sh
dnf module install container-tools:rhel8
```

If you are running {{site.data.keyword.rhel}} 8.5 or below, remove Podman and other pre-included packages, then install Docker as described here.

1. Uninstall packages:

   ```sh
   yum remove buildah skopeo podman containers-common atomic-registries docker container-tools
   ```
   {: codeblock}

2. Remove remaining artifacts & files:

   ```sh
   rm -rf /etc/containers/* /var/lib/containers/* /etc/docker /etc/subuid* /etc/subgid*
   ```
   {: codeblock}

3. Delete any associated container storage:

   ```sh
   cd ~ && rm -rf /.local/share/containers/
   ```
   {: codeblock}

4. Install Docker by following the instructions for [Docker CENTOS Installation ](https://docs.docker.com/engine/install/centos/){:target="_blank"}{: .externalLink}.

5. Configure Docker to start on boot by default and follow any other [Docker post installation steps ](https://docs.docker.com/engine/install/linux-postinstall/){:target="_blank"}{: .externalLink}.

   ```sh
   sudo systemctl enable docker.service
   sudo systemctl enable containerd.service
   ```
   {: codeblock}

Now that your edge device is prepared, continue on to [Installing the agent](registration.md).

## {{site.data.keyword.linux_ppc64le_notm}} devices or virtual machines
{: #ppc64le-machines}

### Hardware requirements
{: #hard-req-ppc64le}

- ppc64le device or virtual machine
- An internet connection for your device (wired or wifi)
- (optional) Sensor hardware: Many {{site.data.keyword.horizon}} edge services require specialized sensor hardware.

### Procedure
{: #proc-ppc64le}

Prepare your device by installing {{site.data.keyword.rhel}}.

Install the most recent version of Docker on your device.

Now that your edge device is prepared, continue on to [Installing the agent](registration.md).

## {{site.data.keyword.linux_notm}} on ARM (32-bit)
{: #arm-32-bit}

### Hardware requirements
{: #hard-req-pi}

- Raspberry Pi 3A+, 3B, 3B+, or 4 (preferred)
- Raspberry Pi A+, B+, 2B, Zero-W, or Zero-WH
- MicroSD flash card (32 GB preferred)
- An appropriate power supply for your device (2 Amp or greater preferred)
- An internet connection for your device (wired or wifi).
  **Note**: Some devices require extra hardware for supporting wifi.
- (optional) Sensor hardware: Many {{site.data.keyword.horizon}} edge services require specialized sensor hardware.

### Procedure
{: #proc-pi}

1. Prepare your Raspberry Pi device.
   1. Flash the [Raspberry Pi OS ](https://www.raspberrypi.com/software/){:target="_blank"}{: .externalLink} {{site.data.keyword.linux_notm}} image onto your MicroSD card.

      For more information about how to flash MicroSD images from many operating systems, see [Raspberry Pi Foundation ](https://www.raspberrypi.org/documentation/installation/installing-images/README.md){:target="_blank"}{: .externalLink}.
      These instructions use Raspberry Pi OS for wifi and SSH configurations.

      **Warning:** Flashing an image onto your MicroSD card permanently erases any data that is already on your card.

   2. (optional) If you plan to use wifi to connect to your device, edit your newly flashed image to provide the appropriate WPA2 wifi credentials.

      If you plan to use a wired network connection, you do not need to complete this step.

      On your MicroSD card, create a file that is named `wpa_supplicant.conf` within the root level folder that contains your wifi credentials. These credentials include your network SSID name and passphrase. Use the following format for your file:

      ```txt
      country=US
      ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev update_config=1
      network={
      ssid="<your-network-ssid>"
      psk="<your-network-passphrase"
      key_mgmt=WPA-PSK>
      }
      ```
      {: codeblock}

   3. (optional) If you want or need to run a Raspberry Pi device with no monitor or keyboard, you need to enable SSH connection access to your device. SSH access is unavailable by default.

      To enable the SSH connection, create an empty file on your MicroSD card that is named `ssh`. Include this file in the root level folder for your card. The inclusion of this file provides you with the ability to connect to your device with the default credentials.

   4. Unmount your MicroSD card. Ensure that you safely eject the card from the device that you are using to edit the card so that all of your changes are written.

   5. Insert the MicroSD card into your Raspberry Pi device. Attach any optional sensor hardware and connect the device to your power supply.

   6. Start your device.

   7. Change the default password for your device. In Raspberry Pi OS flash images, the default account uses the login name `pi` and the default password `raspberry`.

      Log in to this account. Use the standard {{site.data.keyword.linux_notm}} `passwd` command to change the default password:

      ```sh
      passwd
      Enter new UNIX password:
      Retype new UNIX password:
      passwd: password updated successfully
      ```
      {: codeblock}

   8. Install the most recent version of Docker on your device. For more information, see [Install Docker ](https://docs.docker.com/engine/install/debian/){:target="_blank"}{: .externalLink}.

Now that your edge device is prepared, continue on to [Installing the agent](registration.md).

## {{site.data.keyword.linux_notm}} on ARM (64-bit)
{: #arm-64-bit}

### Hardware requirements
{: #hard-req-nvidia}

- NVIDIA Jetson Nano, or TX2 (recommended)
- NVIDIA Jetson TX1
- HDMI Business Monitor, USB hub, USB keyboard, USB mouse
- Storage: at least 10 GB (SSD recommended)
- An internet connection for your device (wired or wifi)
- (optional) Sensor hardware: Many {{site.data.keyword.horizon}} edge services require specialized sensor hardware.

### Procedure
{: #proc-nvidia}

1. Prepare your NVIDIA Jetson device.
   1. Install the most recent NVIDIA JetPack on your device. For more information, see:
      - (TX1) [Jetson TX1 ](https://elinux.org/Jetson_TX1){:target="_blank"}{: .externalLink}
      - (TX2) [Harness AI at the Edge with the Jetson TX2 Developer Kit ](https://developer.nvidia.com/embedded/jetson-tx2-developer-kit){:target="_blank"}{: .externalLink}
      - (Nano) [Getting Started With Jetson Nano Developer Kit ](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit){:target="_blank"}{: .externalLink}

      You need to install this software and any prerequisite software before you install the {{site.data.keyword.horizon}} software.

   2. Change the default password. In the JetPack installation procedure, the default account uses the login name `nvidia` and the default password `nvidia`.

      Log in to this account. Use the standard {{site.data.keyword.linux_notm}} `passwd` command to change the default password:

      ```sh
      passwd
      Enter new UNIX password:
      Retype new UNIX password:
      passwd: password updated successfully
      ```
      {: codeblock}

   3. Install the most recent version of Docker on your device. For more information, see [Install Docker ](https://docs.docker.com/engine/install/debian/){:target="_blank"}{: .externalLink}.

Now that your edge device is prepared, continue on to [Installing the agent](registration.md).

## {{site.data.keyword.macOS_notm}}
{: #mac-os-x}

### Hardware requirements
{: #hard-req-mac}

- 2010 or later 64-bit {{site.data.keyword.intel}} Mac device
- MMU virtualization is required.
- MacOS X version 10.11 ("El Capitan") or later
- An internet connection for your machine (wired or wifi)
- (optional) Sensor hardware: Many {{site.data.keyword.horizon}} edge services require specialized sensor hardware.

### Procedure
{: #proc-mac}

1. Prepare your device.
   1. Install the most recent version of Docker on your device. For more information, see [Install Docker ](https://docs.docker.com/docker-for-mac/install/){:target="_blank"}{: .externalLink}{:target="_blank"}{: .externalLink}.

   2. **Install socat**. You can use either of the following methods to install socat:

      - [Use Homebrew to install socat ](https://brewinstall.org/install-socat-on-mac-with-brew/){:target="_blank"}{: .externalLink}{:target="_blank"}{: .externalLink}.

      - If MacPorts are already installed, use it to install socat:

        ```sh
        sudo port install socat
        ```
        {: codeblock}

## What's next

- [Installing the agent](registration.md)
- [Updating the agent](updating_the_agent.md)

## Related information

- [Install {{site.data.keyword.ieam}}](../hub/online_installation.md)
- [Advanced manual installation and registration of an agent](advanced_man_install.md)
