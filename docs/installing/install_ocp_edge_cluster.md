---
copyright: Contributors to the Open Horizon project
years: 2020 - 2026
title: Installing an OCP cluster
description: Documentation for Installing an OCP edge cluster
lastupdated: 2026-04-08
nav_order: 1
parent: Installing edge clusters
has_children: false
has_toc: false
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Installing an {{site.data.keyword.open_shift_cp}} cluster
{: #install_ocp_edge_cluster}

1. Install {{site.data.keyword.open_shift_cp}} by following the installation instructions in the [{{site.data.keyword.open_shift_cp}} Documentation](https://docs.openshift.com/container-platform/4.6/welcome/index.html){:target="_blank"}{: .externalLink}. For information about the required cluster architecture, see [Installing the agent on {{site.data.keyword.open_shift_cp}} Kubernetes edge cluster](../anax/docs/installing_ocp_edge_cluster_agent.md).

2. Install the Kubernetes CLI (**kubectl**), {{site.data.keyword.open_shift}} client CLI (**oc**) and Docker on the admin host where you administer your {{site.data.keyword.open_shift_cp}} edge cluster. This is the same host where you run the agent installation script. For more information, see [Installing cloudctl, kubectl, and oc](../cli/cloudctl_oc_cli.md).

3. Choose the image registry types: remote image registry or edge cluster local registry. Image registry is the place that will hold the agent image and agent cronjob image.

   - [Setting variables to use a remote image registry](./setting_remote_image_registry.md)
   - [Setup edge cluster local image registry for K3s](./setup_k3s_image_registry.md)

<!--Question from EOC: Is step 3 relevant to OCP?-->
