---
copyright: Contributors to the Open Horizon project
years: 2020 - 2025
title: Updating the agent
description: Documentation for Updating the agent
lastupdated: 2025-05-03
nav_order: 3
parent: Edge devices info
grand_parent: Edge devices
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Updating the agent
{: #updating_the_agent}

If you received updated {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) agent packages, you can easily update your edge device:

1. Perform the steps in [Gather the necessary information and files for edge devices](../hub/gather_files.md#prereq_horizon) to create the updated **agentInstallFiles-&lt;edge-device-type&gt;.tar.gz** file with the newer agent packages.
  
2. For each edge device, perform the steps in [Automated agent installation and registration](automated_install.md#method_one), except that when running the **agent-install.sh** command, specify the service and pattern or policy you want to run on the edge device.
