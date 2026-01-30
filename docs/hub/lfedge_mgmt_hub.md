---
copyright: Contributors to the Open Horizon project
years: 2022 - 2025
title: "{{site.data.keyword.ieam}} Management Hub Developer Instance"
description: "Documentation for {{site.data.keyword.ieam}} Management Hub Developer Instance"
lastupdated: 2025-05-03
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# {{site.data.keyword.ieam}} Management Hub Developer Instance
{: #lfedge_mgmt_hub}

The LF Edge's Open Horizon project delivers containerized services and ML assets, and manages the service software lifecycle on edge nodes and clusters.  The project's Management Hub components store the metadata for describing the services, deployment policies, and encrypted communications.  They also propose agreements to edge nodes for potential deployments.  For an edge node or cluster to manage workloads, they must be registered with a Hub instance.  The Open Horizon project is providing a public Hub instance for the LF Edge community to use, provide working examples, and to assist developers.  This Hub instance will be the current release of Open Horizon, and will be replaced whenever a new release is deployed every few months.
{: .text-justify}

## Requesting user account
To obtain a free user account on the Hub, send your request to the *#open-horizon-devops* chat channel on the [Open Horizon chat server ](https://chat.lfx.linuxfoundation.org/){:target="_blank"}{: .externalLink}.

## Adding user account in organization
Before adding the new user, collect the following information:
* Will you need to create a single user account or multiple?
* Which ones need to be an organization admin?
* Will a user account also need to be added to an existing organization?
* What is the preferred org name, user name, user password, user email?

To add a new user, first add a new tenant organization if the user is not being added exclusively to an existing organization by following the below steps:

1. Authenticate with the Hub as a [Hub admin](../admin/multi_tenancy.md#user-types).
2. Create the organization for the user.  Usually the personal organization has the same name as the username.
```bash
hzn exchange org create --description="Personal organization for example code" <org name>
```
3. Verify that the new organization exists:
```bash
hzn exchange org list
```
4. Create the new user account (add -A if the account is for an [Organization admin](../admin/multi_tenancy.md#user-types)):
```bash
hzn exchange user create -o <org name> -A <user login> <user password> <user email>
```
5. Verify that the new user exists:
```bash
hzn exchange user list -o <org name> <user name>
```