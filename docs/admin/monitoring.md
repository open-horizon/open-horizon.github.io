---

copyright:
years: 2020
lastupdated: "2020-2-2"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}


# Monitoring

## Accessing the {{site.data.keyword.ieam}} Grafana Dashboard 
{: #monitoring_dashboard}

1. Follow the steps in [Using the management console](../console/accessing_ui.md) to ensure that you can access the {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) management console.
2. Navigate to `https://<cluster-url>/grafana` to view the grafana dashboard. 
3. In the lower left corner, there is a profile icon. Hover over it and select the switch org option. 
4. Select the `ibm-edge` org. If you installed {{site.data.keyword.ieam}} in a different namespace, select that org instead.
5. Search for "{{site.data.keyword.ieam}}" so you can monitor the overall CPU, memory, and network pressure of your {{site.data.keyword.ieam}} install.

   <img src="../images/edge/ieam_monitoring_dashboard.png" style="margin: 3%" alt="IEAM Monitoring Dashboard" width="85%" height="85%" align="center">


# Monitoring edge nodes and services
{: #monitoring_edge_nodes_and_services}

[Log in to the management console](../console/accessing_ui.md) to monitor {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) edge nodes and services.

* Monitor edge nodes:
  * The Nodes dashboard is first page that is displayed, and it includes a donut chart that shows the state of all of the edge nodes.
  * To see all of the nodes in a particular state, click that color in the donut chart. For example, to see all of the edge nodes with errors (if any exist), click the color that the legend indicates is used for **Has error**.
  * A list of the nodes with errors is displayed. To drill down into one node to see the specific error, click the node name.
  * In the node details page that is displayed, the section **Edge agent errors** shows the services that have errors, the specific error message, and the timestamp.
* Monitor edge services:
  * In the **Services** tab, click the service that you want to drill down into, which displays the edge service details page.
  * In the **Deployment** section of the details page, you can see the policies and patterns that are deploying this service to edge nodes.
* Monitor edge services on an edge node:
  * In the **Nodes** tab, switch to the list view, and click the edge node you want to drill down into.
  * In the node details page, the **Services** section shows what edge services are currently running on that edge node.
