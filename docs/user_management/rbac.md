---

copyright:
years: 2019 - 2023
lastupdated: "2023-05-01"
title: "Role-based access control"

parent: Security
grand_parent: Administering
nav_order: 2
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Role-based access control
{: #rbac}

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) supports several roles. Your role determines the actions that you can perform.
{:shortdesc}

## Organizations
{: #orgs}

{{site.data.keyword.ieam}} supports the general concept of multitenancy through organizations, where each tenant has their own organization. Organizations separate resources; therefore, users within each organization cannot create or modify resources in a different organization. Furthermore, resources in an organization can be viewed only by users in that organization (unless the resources are marked as public). Resources that are marked as public are the only resources that can be viewed across organizations.

The IBM organization provides predefined services and patterns. Although the resources in that organization are public, it is not intended to hold all public content in the {{site.data.keyword.ieam}} management hub.

By default, one organization is created during {{site.data.keyword.ieam}} installation with a name that you choose. You can create additional organizations as needed. For more information about adding organizations to your management hub, see [Multi-tenancy](../admin/multi_tenancy.md).

## Identities
{: #ids}

There are four types of identities within {{site.data.keyword.ieam}}:

* Identity and Access Management (IAM) users. IAM users are recognized by all {{site.data.keyword.ieam}} components: UI, exchange, **hzn** CLI, **cloudctl** CLI, **oc** CLI, **kubectl** CLI.
  * IAM provides an LDAP plugin, so LDAP users connected to IAM behave like IAM users
  * IAM API keys (used with the **hzn** command) behave like IAM users
* Exchange-only users: The exchange root user is an example of this. You usually do not need to create other local exchange-only users. As a best practice, manage users in IAM, and use those user credentials (or API keys associated with those users) to authenticate to {{site.data.keyword.ieam}}.
* Exchange nodes (edge devices or edge clusters)
* Exchange {{site.data.keyword.agbot}}s

### Role-Based Access Control (RBAC)
{: #rbac_roles}

{{site.data.keyword.ieam}} includes the following roles:

| **Role**    | **Access**    |
|---------------|--------------------|
| IAM user | Through IAM, can be given these management hub roles: Cluster Administrator, Administrator, Operator, Editor, and Viewer. An IAM role is assigned to users or user groups when you add them to an IAM team. Team access to resources can be controlled by Kubernetes namespace. IAM users can also be given any of the Exchange roles below by using the **hzn exchange** CLI. |
| Exchange root user | Has unlimited privilege in the exchange. This user is defined in the exchange config file. It can be disabled, if desired. |
| Exchange hub admin user | Can view the list of organizations, view the users in an organization, and create or delete organizations. |
| Exchange org admin user | Has unlimited exchange privilege within the organization. |
| Exchange user | Can create exchange resources (nodes, services, patterns, policies) in the organization. Can update or delete resources owned by this user. Can read all services, patterns, and policies in the organization, and public services and patterns in other organizations. Can read nodes owned by this user. |
| Exchange nodes | Can read its own node in the exchange, and read all services, patterns, and policies in the organization, and public service and patterns in other organizations. These are the only credentials that should be saved in the edge node, because they have the minimum privilege necessary to operate the edge node.|
| Exchange {{site.data.keyword.agbot}}s | {{site.data.keyword.agbot}}s in the IBM organization can read all nodes, services, patterns, and policies in all organizations. |
{: caption="Table 1. RBAC roles" caption-side="top"}

## Next

See [Security](./security.md) topics page for related information.
