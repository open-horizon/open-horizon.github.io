---
copyright: Contributors to the Open Horizon project
years: 2020 - 2025
title: Edge cluster service
description: Documentation for Edge cluster service
lastupdated: 2025-05-03
nav_order: 6
parent: Edge service examples
grand_parent: Using edge services
---

# Edge cluster service

In general, developing a service to run in an edge cluster is similar to developing an edge service that runs on an edge device, but the difference is in how the edge service is deployed. To deploy a containerized edge service to an edge cluster, a developer must first build a Kubernetes operator that deploys the containerized edge service in a Kubernetes cluster. After the operator is written and tested, the developer creates and publishes the operator as an Open Horizon service. The operator service can be deployed to edge clusters with policy or pattern as any Open Horizon service would be.

Open Horizon  exchange contains a service called `nginx-operator` that allows you to expose a port on your edge cluster that can be accessed externally using the `curl` command. To deploy this example service to your edge cluster, see [Horizon Operator Example Edge Service ](https://github.com/open-horizon/examples/tree/master/edge/services/nginx-operator#using-operator-policy).
