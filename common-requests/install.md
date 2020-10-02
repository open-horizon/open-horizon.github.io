---
layout: page
title: "Installation"
description: "Instructions for installing the Open Horizon project's Management Hub, Agent, and CLI all in one VM"
---

# Install

## Pre-requisites

To run the [all-in-one instructions](https://github.com/open-horizon/devops/tree/master/mgmt-hub) for the Management Hub, Agent, and CLI all in one VM, you need a VM with: 

* &gt;= 4GB RAM
* 20GB storage 
* Ubuntu Server 18.04 LTS

This video shows an example of installing Ubuntu Server on VirtualBox 6.1 on OSX Catalina.

{% include youtubePlayer.html id="YQqFnRNL98s" %}
The links for installation
* [Ubuntu Server 18.04 LTS for AMD64](http://cdimage.ubuntu.com/ubuntu/releases/18.04/release/ubuntu-18.04.5-server-amd64.iso)
* [VirtualBox 6.1](https://www.virtualbox.org/wiki/Downloads)
* [Open Horizon Management Hub installation instructions](https://github.com/open-horizon/devops/blob/master/mgmt-hub/README.md)
* [Open Horizon project](https://www.lfedge.org/projects/openhorizon/)  

## Installation

* After Ubuntu Server 18.04 is running, run the installation as root: 

``` shell
sudo -i
```

* Follow the steps in the [all-in-one instructions](https://github.com/open-horizon/devops/tree/master/mgmt-hub) to install the Management Hub/Agent/CLI in a single VM.  

This video shows an installation process example.

{% include youtubePlayer.html id="q4wwaE7z9v8" %}

## What to do next

After installing the Management Hub/Agent/CLI with the all-in-one process, go to [How to Use Open Horizon](./use.html)