---
copyright: Contributors to the Open Horizon project
years: 2021 - 2026
title: Prerequisites for full installation
description: Documentation for Install {{site.data.keyword.ieam}}
lastupdated: "2026-08-19"
nav_order: 1
parent: Installing Open Horizon
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Install {{site.data.keyword.ieam}}
{: #hub_install_overview}

You must install and configure a [management hub](../hub/overview.md) before you start the {{site.data.keyword.edge_notm}} node tasks.

## Prerequisites for full installation
{: #prereq}

Ensure that the requirements specified in [System requirements](requirements.md) are met. The installation can run on the bare hardware or in a VM.  The Hub **cannot** run on arm64-based hardware.

Several files are needed to install the {{site.data.keyword.edge_notm}} agent on your edge devices and edge clusters and register them with {{site.data.keyword.edge_notm}}. These agent files are stored in the CSS Cloud Sync Service (CSS) component of the Model Management System (MMS). If you know the components of the Exchange that you want to use, and their IP addresses and ports, you can bundle those edge node files now. However, if you are uncertain of those details, you might want to bundle those files after you install {{site.data.keyword.edge_notm}}. For more information, see [Gather edge node files](gather_files.md).


## What's Next

Continue setting up your new management hub by performing the steps in [Install {{site.data.keyword.ieam}}](online_installation.md).
