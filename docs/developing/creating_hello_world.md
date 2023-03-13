---
copyright:
years: 2020 - 2023
lastupdated: "2023-03-13"
title: Creating your own hello world for clusters
description: To deploy a containerized edge service to an edge cluster, the first step is to build a Kubernetes Operator that deploys the containerized edge service in a Kubernetes cluster.

parent: Edge services for clusters
grand_parent: Developing edge services
nav_order: 2
---

{:shortdesc: .shortdesc}
{:new_window: target="_blank"}
{:codeblock: .codeblock}
{:pre: .pre}
{:screen: .screen}
{:tip: .tip}
{:download: .download}

# Creating your own hello world for clusters
{: #creating_hello_world}

To deploy a containerized edge service to an edge cluster, the first step is to build a Kubernetes Operator that deploys the containerized edge service in a Kubernetes cluster.

Use this example to learn how to:

* Create an ansible operator by using `operator-sdk`
* Use the operator to deploy a service to an edge cluster
* Expose a port on your edge cluster that you can access externally with the `curl` command

See [Creating Your Own Operator Edge Service ](https://github.com/open-horizon/examples/blob/master/edge/services/nginx-operator/CreateService.md){:target="_blank"}{: .externalLink}.

To run the published `nginx-operator` service, see [Using the Operator Example Edge Service with Deployment Policy ](https://github.com/open-horizon/examples/tree/master/edge/services/nginx-operator#using-operator-policy){:target="_blank"}{: .externalLink}.
