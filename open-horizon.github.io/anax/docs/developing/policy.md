---

copyright:
years: 2020 - 2022
lastupdated: "2022-03-17"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Hello world
{: #policy}

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) uses policies to establish and manage service and model deployments, which give administrators the flexibility and scalability that is needed to work with large numbers of edge nodes. {{site.data.keyword.ieam}} policy is an alternative to deployment patterns. It provides a greater separation of concerns, allowing edge nodes owners, service code developers, and business owners to independently articulate policies.

This is a minimal "Hello, world" example to introduce you to {{site.data.keyword.edge_notm}} deployment policies.

Types of Horizon policies:

* Node policy (provided at registration by the node owner)
* Service policy (can be applied to a published service in the Exchange)
* Deployment policy (also sometimes referred to as business policy, which approximately corresponds to a deployment pattern)

Policies provide more control over defining agreements between Horizon Agents on Edge Nodes and the Horizon AgBots.

## Using a policy to run the hello world sample
{: #helloworld_policy}

See [Using the Hello World Example Edge Service with Deployment Policy ](https://github.com/open-horizon/examples/blob/master/edge/services/helloworld/PolicyRegister.md#using-the-hello-world-example-edge-service-with-deployment-policy){:target="_blank"}{: .externalLink}.

## Related information

* [Deploying edge services](../using_edge_services/detailed_policy.md)
* [Deployment policy use cases](../using_edge_services/policy_user_cases.md)
