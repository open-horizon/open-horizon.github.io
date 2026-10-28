---
copyright: Contributors to the Open Horizon project
years: 2019 - 2026
title: Preparing an edge device
description: Documentation for Preparing an edge device
lastupdated: "2026-10-21"
nav_order: 1
parent: Installing edge device agents
---

# Preparing an edge device

The following instructions guide you through the process of installing the required software on your edge device and registering it with Open Horizon (Open Horizon).

## Supported architectures and operating systems

Open Horizon supports architectures and operating systems with the hardware architectures documented in [System requirements](../hub/requirements.md).

**Notes**:

- Installation of edge devices with SuSE is only supported by the [Advanced manual agent installation and registration](../installing/advanced_man_install.md) method.
- CentOS and Red Hat Enterprise Linux&reg; 8.5 or earlier on Open Horizon only support Docker&reg; as a container engine.
- While Open Horizon supports running Red Hat Enterprise Linux&reg; 8.x with Docker&reg;, it is officially unsupported by Red Hat Enterprise Linux&reg;.
- Open Horizon supports Podman on Red Hat Enterprise Linux&reg; 8.x, 9.x, 10.x and Fedora 36 - 43 Workstation.

## Sizing

The agent requires:

- 100 MB random access memory (RAM), including docker or podman. RAM increases this amount by approximately 100 K per agreement, plus any additional memory that is required by workloads that run on the device.
- 400 MB disk (including docker). Disk increases this amount based on the size of the container images that are used by workloads and the size of the model objects (times 2) that are deployed to the device.

# Installing the agent

The following instructions guide you through the process of installing the required software on your edge device and registering it with Open Horizon.

## Procedures

To install and configure your edge device, click the link that represents your edge device type:

- [Linux x86_64 devices or virtual machines](#x86-machines)
- [Red Hat Enterprise Linux&reg; 8.x / 9.x / 10.x devices or virtual machines](#rhel8)
- [Linux ppc64le devices or virtual machines](#ppc64le-machines)
- [Linux on ARM (32-bit)](#arm-32-bit); for example, Raspberry Pi running Raspberry Pi OS
- [Linux on ARM (64-bit)](#arm-64-bit); for example, NVIDIA Jetson Nano, TX1, or TX2
- [macOS](#mac-os-x)

## Linux x86_64 devices or virtual machines {: #x86-machines }

### Hardware requirements

- 64-bit Intel&reg; or AMD device or virtual machine
- An internet connection for your device (wired or WiFi)
- (optional) Sensor hardware: Many Horizon edge services require specialized sensor hardware

### Procedure

Prepare your device by installing an operating system that meets the requirements specified in [System requirements](../hub/requirements.md).

Install the most recent version of Docker or Podman on your device. For more information, see [Install Docker&reg; ](https://docs.docker.com/engine/install/ubuntu/) or [Podman.io ](https://podman.io/).

Now that your edge device is prepared, continue on to [Installing the agent](registration.md).

## Red Hat Enterprise Linux&reg; 8.x / 9.x / 10.x devices or virtual machines {: #rhel8 }

### Hardware requirements

- 64-bit Intel&reg; device, AMD device, ppc64le device, or virtual machine
- An internet connection for your device (wired or WiFi)
- (optional) Sensor hardware: Many Horizon edge services require specialized sensor hardware

### Procedure

Prepare your device by installing Red Hat Enterprise Linux&reg; 8.x or 9.x or 10.x

1. Install packages:

   If you are running Red Hat Enterprise Linux&reg; 9.0 or above, install the required Podman and Netavark packages.

   ```bash
   dnf install podman netavark
   ```

   If you are running Red Hat Enterprise Linux&reg; 8.6 or above, install the Podman packages by installing the `container-tools:rhel8` module.

   ```bash
   dnf module install container-tools:rhel8
   ```

2. Switch the network stack from Container Network Interface (CNI) to Netavark. The Horizon agent requires the network backend to be configured to use Netavark instead of CNI so that the agent can set up networking scenarios such as dependent services between containers. Follow the steps in the Red Hat documentation [switching the network stack ](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html-single/building_running_and_managing_containers/index#proc_switching-the-network-stack-from-cni-to-netavark_assembly_setting-container-network-modes) chapter.

If you are running Red Hat Enterprise Linux&reg; 8.5 (or earlier), remove Podman and other pre-included packages, then install Docker&reg; as described here.

1. Uninstall packages:

   ```bash
   yum remove buildah skopeo podman containers-common atomic-registries docker container-tools
   ```

2. Remove remaining artifacts and files:

   ```bash
   rm -rf /etc/containers/* /var/lib/containers/* /etc/docker /etc/subuid* /etc/subgid*
   ```

3. Delete any associated container storage:

   ```bash
   cd ~ && rm -rf /.local/share/containers/
   ```

4. Install Docker by following the instructions for [Docker&reg; CENTOS Installation ](https://docs.docker.com/engine/install/centos/).

5. Configure Docker to start on boot by default and follow any other [Docker&reg; post installation steps ](https://docs.docker.com/engine/install/linux-postinstall/).

   ```bash
   sudo systemctl enable docker.service
   sudo systemctl enable containerd.service
   ```

Now that your edge device is prepared, continue on to [Installing the agent](registration.md).

## Linux ppc64le devices or virtual machines {: #ppc64le-machines }

### Hardware requirements

- ppc64le device or virtual machine
- An internet connection for your device (wired or WiFi)
- (optional) Sensor hardware: Many Horizon edge services require specialized sensor hardware

### Procedure

Prepare your device by installing Red Hat Enterprise Linux&reg;.

Install the most recent version of Podman on your device.

Now that your edge device is prepared, continue on to [Installing the agent](registration.md).

## Linux on ARM (32-bit) {: #arm-32-bit }

### Hardware requirements

- Raspberry Pi 3A+, 3B, 3B+, or 4 (preferred)
- Raspberry Pi A+, B+, 2B, Zero-W, or Zero-WH
- MicroSD flash card (32 GB preferred)
- An appropriate power supply for your device (2 Amp or greater preferred)
- An internet connection for your device (wired or WiFi)
  **Note**: Some devices require extra hardware for supporting WiFi
- (optional) Sensor hardware: Many Horizon edge services require specialized sensor hardware

### Procedure

1. Prepare your Raspberry Pi device.
   1. Flash the [Raspberry Pi OS ](https://www.raspberrypi.com/software/) Linux image onto your MicroSD card.

      For more information about how to flash MicroSD images from many operating systems, see [Raspberry Pi Foundation ](https://www.raspberrypi.org/documentation/installation/installing-images/README.md).
      These instructions use Raspberry Pi OS for WiFi and SSH configurations.

      **Warning:** Flashing an image onto your MicroSD card permanently erases any data that is already on your card.

   2. (optional) If you plan to use WiFi to connect to your device, edit your newly flashed image to provide the appropriate WPA2 WiFi credentials.

      If you plan to use a wired network connection, you do not need to complete this step.

      On your MicroSD card, create a file that is named `wpa_supplicant.conf` within the root level folder that contains your WiFi credentials. These credentials include your network SSID name and passphrase. Use the following format for your file:

      ```txt
      country=US
      ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev update_config=1
      network={
      ssid="<your-network-ssid>"
      psk="<your-network-passphrase>"
      key_mgmt=WPA-PSK>
      }
      ```

   3. (optional) If you want or need to run a Raspberry Pi device with no monitor or keyboard, you need to enable SSH connection access to your device. SSH access is unavailable by default.

      To enable the SSH connection, create an empty file on your MicroSD card that is named `ssh`. Include this file in the root level folder for your card. The inclusion of this file provides you with the ability to connect to your device with the default credentials.

   4. Unmount your MicroSD card. Ensure that you safely eject the card from the device that you are using to edit the card so that all of your changes are written.

   5. Insert the MicroSD card into your Raspberry Pi device. Attach any optional sensor hardware and connect the device to your power supply.

   6. Start your device.

   7. Change the default password for your device. In Raspberry Pi OS flash images, the default account uses the login name `pi` and the default password `raspberry`.

      Log in to this account. Use the standard Linux `passwd` command to change the default password:

      ```bash
      passwd
      Enter new UNIX password:
      Retype new UNIX password:
      passwd: password updated successfully
      ```

   8. Install the most recent version of Docker on your device. For more information, see [Install Docker&reg; ](https://docs.docker.com/engine/install/debian/).

Now that your edge device is prepared, continue on to [Installing the agent](registration.md).

## Linux on ARM (64-bit) {: #arm-64-bit }

### Hardware requirements

- NVIDIA Jetson Nano, or TX2 (recommended)
- NVIDIA Jetson TX1
- HDMI Business Monitor, USB hub, USB keyboard, USB mouse
- Storage: at least 10 GB (SSD recommended)
- An internet connection for your device (wired or WiFi)
- (optional) Sensor hardware: Many Horizon edge services require specialized sensor hardware.

### Procedure

1. Prepare your NVIDIA Jetson device.
   1. Install the most recent NVIDIA JetPack on your device. For more information, see:
      - (TX1) [Jetson TX1 ](https://elinux.org/Jetson_TX1)
      - (TX2) [Harness AI at the Edge with the Jetson TX2 Developer Kit ](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-tx2/)
      - (Nano) [Getting Started With Jetson Nano Developer Kit ](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit)

      You need to install this software and any prerequisite software before you install the Horizon software.

   2. Change the default password. In the JetPack installation procedure, the default account uses the login name `nvidia` and the default password `nvidia`.

      Log in to this account. Use the standard Linux `passwd` command to change the default password:

      ```bash
      passwd
      Enter new UNIX password:
      Retype new UNIX password:
      passwd: password updated successfully
      ```

   3. Install the most recent version of Docker on your device. For more information, see [Install Docker&reg; ](https://docs.docker.com/engine/install/debian/).

Now that your edge device is prepared, continue on to [Installing the agent](registration.md).

## macOS {: #mac-os-x }

### Hardware requirements

- 2010 or later 64-bit Intel&reg; Mac device
- 2020 or later 64-bit arm64 Apple M1 / M2 / M3 / M4  Mac device
- MMU virtualization is required
- macOS X version 10.11 ("El Capitan") or later
- An internet connection for your machine (wired or WiFi)
- (optional) Sensor hardware: Many Horizon edge services require specialized sensor hardware

### Procedure

1. Prepare your device.
   1. If using Docker, purchase a Docker Desktop license, if necessary, and install the most recent version of Docker on your device. For more information, see the [Docker&reg; installation for Mac ](https://docs.docker.com/docker-for-mac/install/) documentation.

   2. If using Podman, when the machine is initialized with `podman machine init`, the vmtype cannot be `applehv`. You may have to install a different provider with
      ```bash
      brew tap slp/krunkit
      brew install krunkit
      ```
      and then edit ~/.config/containers/containers.conf` to add
      ```bash
      [machine]
      provider = "libkrun"
      ```

   3. [Use Homebrew&reg; to install socat ](https://macappstore.org/socat/)

## What's next

- [Installing the agent](registration.md)
- [Updating the agent](updating_the_agent.md)

## Related information

- [Install Open Horizon](../hub/online_installation.md)
- [Advanced manual installation and registration of an agent](advanced_man_install.md)
