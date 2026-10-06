---
copyright: Contributors to the Open Horizon project
years: 2020 - 2026
title: Installing edge device agents
description: Documentation for Installing edge nodes
lastupdated: 2026-08-20
nav_order: 5
has_children: True
has_toc: False
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Installing edge nodes
{: #installing_edge_nodes}

Edge computing places enterprise applications closer to where the data is created, and where actions need to be taken. More importantly, the negotiation, agreement, execution, and validation of management actions is autonomously carried out between the {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) hub and each edge endpoint that is running a lightweight agent. This autonomous management is a new form of management that addresses the scale, variability, and rate of change of edge topologies including edge nodes: devices and clusters, edge gateways, and network edges.

Typically, edge devices have a prescriptive purpose, provide (often limited) compute capabilities, and are located near or at the data source. Edge clusters usually run workloads in remote, sometimes disconnected, locations near the data source (outside of a data center or cloud environment).

An edge device provides an entry point into enterprise or service provider core networks. Examples include smartphones, security cameras, or even an internet-connected microwave oven.

{{site.data.keyword.edge_notm}} is available for management hub or servers, including distributed devices. See the following sections for details about how to install the {{site.data.keyword.ieam}} lightweight agent on edge devices:

* [Preparing an edge device](../installing/adding_devices.md)
* [Installing the agent](../installing/registration.md)
* [Updating the agent](../installing/updating_the_agent.md)

All edge devices (edge nodes) require the {{site.data.keyword.horizon_agent}} software to be installed. The {{site.data.keyword.horizon_agent}} also depends upon [{{site.data.keyword.docker}} ](https://www.docker.com/){:target="_blank"}{: .externalLink} software.

Focusing in on the edge device, the following diagram shows the flow of the steps you perform to set up the edge device, and what the agent does after it is started.

![{{site.data.keyword.horizon_exchange}}, {{site.data.keyword.agbot}} and agents](../../images/edge/05a_Installing_edge_agent_on_device.svg "{{site.data.keyword.horizon_exchange}}, {{site.data.keyword.agbot}} and agents")

For more information about installing the required software for {{site.data.keyword.edge_notm}} for nodes, see:

* [Commandline Interface (CLI)](../cli/hzn_cli.md)
* [Edge clusters](../installing/edge_clusters.md)