---

copyright:
years: 2021 - 2024
lastupdated: "2024-07-15"
title: "Edge clusters"

nav_order: 12
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

# Edge clusters
{: #edge_clusters}

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) edge cluster capability helps you manage and deploy workloads from a management hub cluster to remote instances of OpenShift® Container Platform or other Kubernetes-based clusters. Edge clusters are {{site.data.keyword.ieam}} edge nodes that are Kubernetes clusters. An edge cluster enables use cases at the edge, which require colocation of compute with business operations, or that require more scalability, availability, and compute capability than what can be supported by an edge device. Further, it is not uncommon for edge clusters to provide application services that are needed to support services running on edge devices due to their close proximity to edge devices. {{site.data.keyword.ieam}} deploys edge services to an edge cluster, via a Kubernetes operator, enabling the same autonomous deployment mechanisms used with edge devices. The full power of Kubernetes as a container management platform is available for edge services that are deployed by {{site.data.keyword.ieam}}.

![{{site.data.keyword.horizon_exchange}}, {{site.data.keyword.agbot}}s and agents](../../images/edge/05b_Installing_edge_agent_on_cluster.svg "{{site.data.keyword.horizon_exchange}}, {{site.data.keyword.agbot}}s and agents")

The following sections describe how to install an edge cluster, then how to install the {{site.data.keyword.ieam}} agent on the cluster.  Then we provide documentation on how to deploy services to the cluster, followed up by how to remove an agent from a cluster.

- [Preparing an edge cluster](preparing_edge_cluster.md)
   - [Installing an OCP cluster](./install_ocp_edge_cluster.md)
   - [Installing a K3s cluster](./install_k3s_edge_cluster.md)
   - [Installing a microk8s cluster](./install_microk8s_edge_cluster.md)
- [Installing the agent](./edge_cluster_agent.md)
- [Deploying services to an edge cluster](../using_edge_services/deploying_services_cluster.md)
- [Removing an agent from an edge cluster](../using_edge_services/removing_agent_from_cluster.md)
{: childlinks}
