---

copyright:
years: 2021
lastupdated: "2021-07-01"
title: "Deploying edge services"

parent: Using edge services
nav_order: 2
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

# Deploying edge services
{: #detailed_deployment_policy}

You can deploy {{site.data.keyword.edge_notm}} {{site.data.keyword.ieam}} policies using policies or patterns. For a more comprehensive overview of various system components, see [Overview of {{site.data.keyword.edge_notm}}](../getting_started/overview_oh.md) and [Deployment policy use cases](policy_user_cases.md). For a hands-on policy example, see [CI-CD process for Edge services](../developing/cicd_process.md).

This section discusses policy and patterns concepts and includes a use case scenario.

Because an administrator cannot simultaneously manage thousands of edge nodes, scaling up to tens of thousands or beyond creates an impossible situation. To achieve this level of scaling, {{site.data.keyword.edge_notm}} uses policies to determine where and when to autonomously deploy services and machine learning models. 

A policy is expressed through a flexible policy language that is applied to models, nodes, services, and deployment policies. The policy language defines attributes (called `properties`) and asserts specific requirements (called `constraints`). This allows each part of the system to provide input to the {{site.data.keyword.edge_notm}} deployment engine. Before services can be deployed, the models, nodes, services, and deployment policies constraints are checked to ensure that all requirements are met.

Due to the fact that nodes (where services are deployed) can express requirements, {{site.data.keyword.edge_notm}} policy is described as a bi-directional policy system. Nodes are not slaves in the {{site.data.keyword.edge_notm}} policy deployment system. As a result, policies provide finer control over service and model deployment than patterns. When policy is in use, {{site.data.keyword.edge_notm}} searches for nodes where it can deploy a given service and analyzes existing nodes to ensure they remain in compliance (in policy). A node is in policy when the node, service, and deployment policies that originally deployed the service remain in effect, or when changes to one of those policies do not affect policy compatibility. The use of policy provides a greater separation of concerns, allowing edge node owners, service developers, and business owners to independently articulate their own policies.

Policies are an alternative to deployment patterns. You can publish patterns to the {{site.data.keyword.ieam}} hub after a developer published an edge service in the horizon exchange. The hzn CLI provides capabilities to list and manage patterns in the Horizon exchange, including commands to list, publish, verify, update, and remove service deployment patterns. It also provides a way to list and remove cryptographic keys that are associated with a specific deployment pattern.

* [Deployment policy use cases](policy_user_cases.md)
* [Using patterns](using_patterns.md)
