 ---

copyright:
years: 2019 - 2023
lastupdated: "2023-03-14"
title: Components

parent: Overview of Open Horizon
nav_bar: 1
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Components

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) includes several components that are bundled with the product.
{:shortdesc}

View the following table for a description of the {{site.data.keyword.ieam}} components:

[//]: # (Pull from release tags hopefully?)

| Component                                     | Version      | Description                                                                                                                                                                                                                        |
|-----------------------------------------------|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **{{site.data.keyword.ieam}} management hub** | 4.5.0        | The {{site.data.keyword.ieam}} management hub manages the edge nodes and the edge service software lifecycle on each edge node.                                                                                                    |
| Agbot                                         | 2.30.0-1177  | Agreement bot (agbot) instances are created centrally and are responsible for deploying workloads and machine learning models to {{site.data.keyword.ieam}} edge nodes.                                                            |
| Exchange API                                  | 2.110.1-1003 | The Exchange API provides a REST API to all of the {{site.data.keyword.ieam}} resources (patterns, policies, services, nodes, and so on) used by all the other components in {{site.data.keyword.ieam}}.                           |
| Model Management System (MMS)                 | 1.9.10-1177  | The Model Management System (MMS) facilitates the storage, delivery, and security of models and files needed by edge services. This enables edge nodes to easily send and receive models and files to and from the management hub. |
| Secure Device Onboard (SDO)                   | 1.11.16-913  | The Secure Device Onboarding (SDO) service enables SDO-enabled edge devices to be configured with zero touch.                                                                                                                      |
| FIDO Device Onboard (FDO)                     | 1.0.0-110    | The FDO component, FIDO Device Onboard, is a device onboarding scheme from the FIDO Alliance that enables technology created by Intel, which makes it simple and secure to configure edge devices and associate them with an edge management hub.|
| Secrets Manager                               | 1.1.1-641    | The Secrets Manager is the repository for secrets deployed to edge devices, enabling services to securely receive credentials used to authenticate to their upstream dependencies.                                                 |
| **Edge node**                                 |              | Any edge device, edge cluster, or edge gateway where edge computing takes place.                                                                                                                                                   |
| Edge cluster agent                            | 2.30.0-1177  | The agent that is installed on edge clusters to enable node workload management by {{site.data.keyword.ieam}}.                                                                                                                     |
| Edge device agent                             | 2.30.0-1177  | The agent that is installed on edge devices to enable node workload management by {{site.data.keyword.ieam}}.                                                                                                                      |
| ESS                                           | 1.9.10-1177  | The edge node part of MMS that makes AI models and files available to the edge services.                                                                                                                                           |
| Example edge services                         | 2.27.0       | Edge service examples that are useful when exploring {{site.data.keyword.ieam}} and learning how to write your own services.                                                                                                       |
{: caption="Table 1. {{site.data.keyword.ieam}} components" caption-side="top"}
