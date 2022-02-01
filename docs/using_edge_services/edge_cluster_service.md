---

copyright:
years: 2021
lastupdated: "2021-02-20"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Edge cluster service
{: #Edge_cluster_service}

In general, developing a service to run in an edge cluster is similar to developing an edge service that runs on an edge device, but the difference is in how the edge service is deployed. To deploy a containerized edge service to an edge cluster, a developer must first build a Kubernetes operator that deploys the containerized edge service in a Kubernetes cluster. After the operator is written and tested, the developer creates and publishes the operator as an {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) service. The operator service can be deployed to edge clusters with policy or pattern as any {{site.data.keyword.edge_notm}} service would be.

{{site.data.keyword.ieam}}  exchange contains a service called `nginx-operator` that allows you to expose a port on your edge cluster that can be accessed externally using the `curl` command. To deploy this example service to your edge cluster, see [Horizon Operator Example Edge Service ![Opens in a new tab](../images/icons/launch-glyph.svg "Opens in a new tab")](https://github.com/open-horizon/examples/tree/master/edge/services/nginx-operator#using-operator-policy).
