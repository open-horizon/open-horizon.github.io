---
copyright:
years: 2020 - 2023
lastupdated: "2023-09-12"
title: "Installing the agent"

parent: Edge devices info
grand_parent: Edge devices
nav_order: 2
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Installing the agent
{: #registration}

When you install the {{site.data.keyword.horizon}} agent software on your edge device, you can register your edge device with {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) to add your device into the edge computing management domain and run edge services. The following instructions register your new edge device with the minimal helloworld example edge service to confirm the edge device is working properly. The helloworld edge service can easily be stopped when you are ready to run your own edge services on the edge device.
{:shortdesc}

## Before you begin
{: #before_begin}

You must complete the steps in [Preparing an edge device](adding_devices.md).

## Installing and registering edge devices
{: #installing_registering}

Five different methods are provided to install the agent on and register edge devices. Each is useful in different circumstances:

* [Automated agent installation and registration](automated_install.md) - install and register one edge device with a minimum of steps. **First-time users should use this method.**
* [Advanced manual agent installation and registration](advanced_man_install.md) - do each step yourself to install and register one edge device. Use this method if you need to do something out of the ordinary and the script that is used in Method 1 does not have the required flexibility. You can also use this method if you want to understand exactly what is required to set up an edge device.
* [Agent in a Container](/docs/anax/docs/agent_container_manual_deploy/) - start and register the agent in a container.
* [Bulk agent installation and registration](many_install.md#batch-install) - install and register many edge devices at one time.
* [FDO agent installation and registration](fdo.md) - automatic install with FDO devices.

## Questions and troubleshooting
{: #questions_ts}

If you have any difficulties with any of these steps, review the provided troubleshooting and frequently asked question topics. For more information, see:

* [Troubleshooting](../troubleshoot/troubleshooting.md)
* [Frequently asked questions](../getting_started/faq.md)
