---
copyright: Contributors to the Open Horizon project
years: 2020 - 2025
title: Hello world
description: Documentation for Hello world
lastupdated: 2025-05-03
nav_order: 1
parent: Edge service examples
grand_parent: Using edge services
---

# Hello world

Open Horizon uses policies to establish and manage service and model deployments, which give administrators the flexibility and scalability that is needed to work with large numbers of edge nodes. Open Horizon policy is an alternative to deployment patterns. It provides a greater separation of concerns, allowing edge nodes owners, service code developers, and business owners to independently articulate policies.

This is a minimal "Hello, world" example to introduce you to Open Horizon deployment policies.

Types of Horizon policies:

* Node policy (provided at registration by the node owner)
* Service policy (can be applied to a published service in the Exchange)
* Deployment policy (also sometimes referred to as business policy, which approximately corresponds to a deployment pattern)

Policies provide more control over defining agreements between Horizon Agents on Edge Nodes and the Horizon AgBots.

## Using a policy to run the hello world sample

See [Using the Hello World Example Edge Service with Deployment Policy ](https://github.com/open-horizon/examples/blob/master/edge/services/helloworld/PolicyRegister.md#using-the-hello-world-example-edge-service-with-deployment-policy).

## Related information

* [Deploying edge services](../using_edge_services/detailed_policy.md)
* [Deployment policy use cases](../using_edge_services/policy_user_cases.md)
