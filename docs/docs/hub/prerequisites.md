---
copyright: Contributors to the Open Horizon project
years: 2021 - 2026
title: Prerequisites for full installation
description: Documentation for Install Open Horizon
lastupdated: "2026-10-21"
nav_order: 2
parent: Installing Open Horizon
---

# Install Open Horizon

You must install and configure a [management hub](../hub/overview.md) before you start the Open Horizon node tasks.

## Prerequisites for full installation

Ensure that the requirements specified in [System requirements](requirements.md) are met. The installation can run on the bare hardware or in a VM.  The Hub **cannot** run on arm64-based hardware.

Several files are needed to install the Open Horizon agent on your edge devices and edge clusters and register them with Open Horizon. These agent files are stored in the CSS Cloud Sync Service (CSS) component of the Model Management System (MMS). If you know the components of the Exchange that you want to use, and their IP addresses and ports, you can bundle those edge node files now. However, if you are uncertain of those details, you might want to bundle those files after you install Open Horizon. For more information, see [Gather edge node files](gather_files.md).

## What's Next

Continue setting up your new management hub by performing the steps in [Install Open Horizon](online_installation.md).
