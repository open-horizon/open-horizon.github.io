---
copyright: Contributors to the Open Horizon project
years: 2020 - 2026
title: Installing edge clusters
description: Prerequisites for installing an agent
lastupdated: 2026-04-07
nav_order: 1
parent: Edge clusters
has_children: true
has_toc: false
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Installing edge clusters
{: #installing_edge_clusters}

Before installing an Open Horizon agent, you must first set up an edge cluster. This section covers the installation of various Kubernetes distributions that can serve as edge clusters.
{:shortdesc}

## Available cluster types

Open Horizon supports the following Kubernetes distributions as edge clusters:

- **Red Hat OpenShift Container Platform (OCP)** - Enterprise Kubernetes platform with enhanced security and management features
- **K3s** - Lightweight Kubernetes distribution optimized for edge computing and IoT
- **MicroK8s** - Minimal Kubernetes distribution for development and testing

Choose the cluster type that best fits your edge computing requirements. Each cluster type has specific installation procedures and configuration options.

## What's next

Select the appropriate cluster installation guide for your environment:

- [Installing an OCP cluster](install_ocp_edge_cluster.md)
- [Installing a K3s cluster](install_k3s_edge_cluster.md)
- [Installing a MicroK8s cluster](install_microk8s_edge_cluster.md)