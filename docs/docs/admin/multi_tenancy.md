---
copyright: Contributors to the Open Horizon project
years: 2020 - 2025
title: Multi-tenancy
description: Software architecture in which a single instance of software runs on server and server multiplies tenants.
lastupdated: 2025-05-03
nav_order: 1
parent: Administering functions
grand_parent: Administering
---

# Multi-tenancy

## Tenants in Open Horizon

Open Horizon (Open Horizon) supports the general IT concept of multi-tenancy through organizations, where each tenant has their own organization. Organizations separate resources; therefore, users within each organization cannot create or modify resources in a different organization. Furthermore, resources in an organization can be viewed only by users in that organization, unless the resources are marked as public.

### Common use cases

Two broad use cases are used to leverage multi-tenancy in Open Horizon:

* An enterprise has multiple business units, where each business unit is a separate organization in the same Open Horizon management hub. Consider the legal, business, or technical reasons why each business unit ought to be a separate organization with its own set of Open Horizon resources, which are by default not accessible by the other business units. Even with separate organizations, the enterprise has the option to use a common group of organization administrators to manage all of the organizations.
* An enterprise hosts Open Horizon as a service for its clients, where each of their clients has one or more organizations in the management hub. In this case, the organization administrators are unique to each client.

The use case that you choose determines how you configure Open Horizon and Identity and Access Manager ([IAM ](https://www.ibm.com/support/knowledgecenter/SSHKN6/iam/landing_iam.html)).

### Types of Open Horizon users {: #user-types }

Open Horizon supports these user roles:

| **Role** | **Access** |
|--------------|-----------------|
| **Hub admin** | Manages the list of Open Horizon organizations by creating, modifying, and deleting organizations as necessary, and by creating organization admins within each organization. |
| **Organization admin** | Manages the resources in one or more Open Horizon organizations. Organization admins can create, view, or modify any resource (user, node, service, policy, or pattern) within the organization, even if they are not the owner of the resource. |
| **Regular user** | Creates nodes, services, policies, and patterns within the organization and modifies or deletes the resources that they have created. Views all of the services, policies, and patterns in the organization that other users have created. |

See [Role-based access control](../user_management/rbac.md) for a description of all Open Horizon roles.

## The relationship between IAM and Open Horizon

The IAM (Identity and Access Manager) service manages users for all Cloud Pak based products, including Open Horizon. IAM in turn uses LDAP to store the users. Each IAM user can be a member of one or more IAM teams. Because each IAM team is associated with an IAM account, an IAM user can indirectly be a member of one or more IAM accounts. See [IAM multi-tenancy ](https://www.ibm.com/support/knowledgecenter/SSHKN6/iam/3.x.x/multitenancy/multitenancy.html) for details.

The Open Horizon exchange provides authentication and authorization services for the other Open Horizon components. The exchange delegates the authentication of users to IAM, which means IAM user credentials are passed to the exchange and it relies on IAM to determine whether they are valid. Each user role (hub admin, organization admin, or regular user) is defined in the exchange, and that determines the actions that users are allowed to perform in Open Horizon.

Each organization in the Open Horizon exchange is associated with an IAM account. Therefore, IAM users in an IAM account are automatically members of the corresponding Open Horizon organization. The one exception to this rule is that the Open Horizon hub admin role is considered to be outside of any specific organization; therefore, it does not matter what IAM account the hub admin IAM user is in.

To summarize the mapping between IAM and Open Horizon:

| **IAM** | **Relationship** | **Open Horizon** |
|--------------|----------|-----------------|
| IAM Account | maps to | Open Horizon Organization |
| IAM User | maps to | Open Horizon User |
| There is no IAM counterpart for role | none | Open Horizon role |

The credentials used to log in to the Open Horizon console are the IAM user and password. The credentials used for the Open Horizon CLI (`hzn`) is an IAM API key.

## The initial organization

By default, an organization was created during Open Horizon installation with a name that you provided. If you do not need the multi-tenant capabilities of Open Horizon, this initial organization is sufficient for your use of Open Horizon, and you can skip the rest of this page.

## The IBM organization

The IBM organization is a unique organization that provides predefined services and patterns that are intended to be technology examples that are usable by any user in any organization. The IBM organization is automatically created when the Open Horizon management hub is installed.

**Note**: Although the resources in the IBM organization are public, the IBM organization is not intended to hold all public content in the Open Horizon management hub.

## Organization Configuration

Every Open Horizon organization has the following settings. The default values for these settings are often sufficient. If you choose to customize any of the settings, run the command `hzn exchange org update -h` to see the command flags that can be used.

| **Setting** | **Description** |
|--------------|-----------------|
| `description` | A description of the organization. |
| `label` | The name of the organization. This value is used to display the organization name in the Open Horizon management console. |
| `heartbeatIntervals` | How often edge node agents in the organization poll the management hub for instructions. See the following section for details. |
| `limits` | Limits for this organization. Currently, the only limit is `maxNodes`, which is the maximum number of edge nodes that are allowed in this organization. There is a practical limit to the total number of edge nodes that a single Open Horizon management hub can support. This setting enables the hub admin user to limit the number of nodes that each organization can have, which prevents one organization from using all of the capacity. A value of `0` means no limit. |

### Agent heartbeat polling interval

The Open Horizon agent that is installed on every edge node periodically heartbeats to the management hub to let the management hub know it is still running and connected, and to receive instructions. You only need to change these settings for exceedingly high scale environments.

The heartbeat interval is the amount of time the agent waits between heartbeats to the management hub. The interval is adjusted automatically over time to optimize responsiveness and reduce the load on the management hub. The interval adjustment is controlled by three settings:

| **Setting** | **Description**|
|-------------|----------------|
| `minInterval` | The shortest amount of time (in seconds) the agent should wait between heartbeats to the management hub. When an agent is registered, it starts polling at this interval. The interval will never be less than this value. A value of `0` means use the default value. |
| `maxInterval` | The longest amount of time (in seconds) the agent should wait between heartbeats to the management hub. A value of `0` means use the default value. |
| `intervalAdjustment` | The number of seconds to add to the current heartbeat interval when the agent detects that it can increase the interval. After successfully heartbeating to the management hub, but receiving no instructions for some time, the heartbeat interval is gradually increased until it reaches the maximum heartbeat interval. Likewise, when instructions are received, the heartbeat interval is decreased to ensure that subsequent instructions are processed quickly. A value of `0` means use the default value. |

The heartbeat polling interval settings in the organization are applied to nodes that have not explicitly configured the heartbeat interval. To check whether a node has explicitly set the heartbeat interval setting, use `hzn exchange node list <node id>`.

For more information about configuring settings in high-scale environments, see [Scaling Configuration](../hub/configuration.md#scale).
