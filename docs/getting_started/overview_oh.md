---
copyright: Contributors to the Open Horizon project
years: 2021 - 2026
title: Overview of Open Horizon
description: Documentation for Overview of {{site.data.keyword.edge_notm}}
lastupdated: 2025-05-03
nav_order: 4
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

# Overview of {{site.data.keyword.edge_notm}}
{: #overviewofedge}

This section provides an overview of {{site.data.keyword.edge_notm}} ({{site.data.keyword.edge_abbr}}).

## {{site.data.keyword.ieam}} capabilities
{: #capabilities}

{{site.data.keyword.ieam}} provides you with edge computing features to help you manage and deploy workloads from a management hub cluster to edge devices and remote instances of {{site.data.keyword.open_shift_cp}} or other Kubernetes-based clusters.

## Architecture

The goal of edge computing is to harness the disciplines that have been created for hybrid cloud computing to support remote operations of edge computing facilities. {{site.data.keyword.ieam}} is designed for that purpose.

The deployment of {{site.data.keyword.ieam}} includes the management hub that runs in an instance of {{site.data.keyword.open_shift_cp}} installed in your data center. The management hub is where the management of all of your remote edge nodes (edge devices and edge clusters) occurs.

These edge nodes can be installed in remote on-premises locations to make your application workloads local to where your critical business operations physically occur, such as at your factories, warehouses, retail outlets, distribution centers, and more.

The following diagram depicts the high-level topology for a typical edge computing setup:

![Open Horizon overview](../../images/edge/01_OH_overview.svg "Open Horizon overview")

The {{site.data.keyword.ieam}} management hub is designed specifically for edge node management to minimize deployment risks and to manage the service software lifecycle on edge nodes fully autonomously. A Cloud installer installs and manages the {{site.data.keyword.ieam}} management hub components. Software developers develop and publish edge services to the management hub. Administrators define the deployment policies that control where edge services are deployed. {{site.data.keyword.ieam}} handles everything else.

# Components
{: #components}

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) includes several components that are required for functionality. For more information about such components, please see [Components](./components.md).

## What's next

For more information about using {{site.data.keyword.ieam}} and developing edge services, review the topics that are listed in {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) [Welcome page](../index.html) and in the following sections:

* [Accessibility](../getting_started/accessibility.md)
* [Components](../getting_started/components.md)
* [Developer learning path](../getting_started/developer_learning_path.md)
* [Documentation conventions](../getting_started/document_conventions.md)
* [Frequently Asked Questions (FAQ)](../getting_started/faq.md)
* [Known issues and limitations](../getting_started/known_issues.md)
* [Release notes](../getting_started/release_notes.md)
