---

copyright:
years: 2020 - 2024
lastupdated: "2024-07-15"
title: "Installing an OCP edge cluster"

parent: Preparing an edge cluster
nav_order: 3
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

# Installing an OCP edge cluster
{: #install_ocp_edge_cluster}

1. Install OCP by following the installation instructions in the [{{site.data.keyword.open_shift_cp}} Documentation ](https://docs.openshift.com/container-platform/4.6/welcome/index.html){:target="_blank"}{: .externalLink}. ({{site.data.keyword.ieam}} only supports OCP on x86_64 platforms.)

2. Install the Kubernetes CLI (**kubectl**), Openshift client CLI (**oc**) and Docker on the admin host where you administer your OCP edge cluster. This is the same host where you run the agent installation script. For more information, see [Installing cloudctl, kubectl, and oc](../cli/cloudctl_oc_cli.md).

## What's next

* [Installing the Cluster Agent](./edge_cluster_agent.md)
