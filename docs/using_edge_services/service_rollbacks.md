---

copyright:
years: 2021 - 2022
lastupdated: "2022-03-10"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Updating an edge service with rollback
{: #service_rollback}

Services on edge nodes are usually performing critical functions, so when a new version of an edge service is rolled out to many edge nodes, it is important to monitor the success of the deployment, and if it fails on any edge node, revert the node back to the previous version of the edge service. {{site.data.keyword.edge_notm}} can do this automatically. In patterns or deployment policies, you can define which previous service version or versions should be used when a new service version fails.

The following content provides additional details on how to roll out a new version of an existing edge service and the software development best practices for updating rollback settings in pattern or deployment policies.

## Creating a new edge service definition
{: #creating_edge_service_definition}

As explained in the [Developing edge services with {{site.data.keyword.edge_notm}}](../developing/developing.md) and [Development details](../developing/developing_details.md) sections, the main steps to release a new version of an edge service are:

- Edit the edge service code as needed for the new version.
- Edit the semantic version number of the code in the service version variable in the **hzn.json** configuration file.
- Rebuild your service containers.
- Sign and publish the new edge service version into the Horizon exchange.

## Updating rollback settings in pattern or deployment policy
{: #updating_rollback_settings}

A new edge service specifies its version number in the `version` field of the service definition.

Patterns or deployment policies determine which services are deployed to which edge nodes. To use edge service rollback capabilities, you need to add the reference for your new service version number in the **serviceVersions** section in either the pattern or deployment policy configuration files.

When an edge service is deployed to an edge node as a result of a pattern or policy, the agent deploys the service version with the top priority value.

For example:

```json
 "serviceVersions":
[
 {
   "version": "2.3.1",
   "priority": {
    "priority_value": 2,
    "retries": 1,
    "retry_durations": 1800
   }
 },
 {
   "version": "1.0.0",
   "priority": {
    "priority_value": 6,
    "retries": 1,
    "retry_durations": 2400
   }
  },
  {
   "version": "2.3.0",
   "priority": {
    "priority_value": 4,
    "retries": 1,
    "retry_durations": 3600
   }
  }
]
```
{: codeblock}

Additional variables are provided in the priority section. The `priority_value` property sets the order of which service version to try first, in practical terms a lower number means higher priority. The `retries` variable value defines the number of times Horizon will attempt to start this service version within the time frame that is specified by `retry_durations` before rolling back to the next highest priority version. The `retry_durations` variable defines the specific time interval in seconds. For example, three service failures over the course of a month might not warrant rolling the service back to an earlier version, but 3 failures within 5 mins might be an indication that there is something wrong with the new service version.

Next, either republish your deployment pattern or update the deployment policy with the **serviceVersion** section changes in the Horizon exchange.

Notice that you can also verify the compatibility of the deployment policy or pattern settings updates with the CLI `deploycheck` command. To view more details, issue:

```bash
hzn deploycheck -h
```
{: codeblock}

The {{site.data.keyword.ieam}} {{site.data.keyword.agbot}}s quickly detect the deployment pattern or deployment policy changes. The {{site.data.keyword.agbot}}s then reach out to each agent whose edge node is either registered to run the deployment pattern or is compatible with the updated deployment policy. The {{site.data.keyword.agbot}} and the agent coordinate to download the new containers, stop and remove the old containers, and start the new containers.

As a result, your edge nodes that are either registered to run the updated deployment pattern or are compatible with the deployment policy quickly runs the new edge service version with the top priority value, regardless of where the edge node is geographically located.

## Viewing progress of new service version being rolled out
{: #viewing_rollback_progress}

Repeatedly query the device agreements until the `agreement_finalized_time` and `agreement_execution_start_time` fields are filled in:

```bash
hzn agreement list
```
{: codeblock}

Notice that the listed agreement shows the version that is associated with the service, and the date-time values appear in the variables (for example, "agreement_creation_time": "",)

Additionally, the version field is populated with the new (and operational) service version with the top priority value:

```json
[
  {
    …
    "agreement_creation_time": "2020-04-01 11:55:08 -0600 MDT",
    "agreement_accepted_time": "2020-04-01 11:55:17 -0600 MDT",
    "agreement_finalized_time": "2020-04-01 11:55:18 -0600 MDT",
    "agreement_execution_start_time": "2020-04-01 11:55:20 -0600 MDT",
    "agreement_data_received_time": "",
    "agreement_protocol": "Basic",
    "workload_to_run": {
      "url": "ibm.helloworld",
      "org": "ibm",
      "version": "2.3.1",
      "arch": "amd64"
    }
  }
]
```
{: codeblock}

For additional details, you can inspect the event logs for the current node with the CLI command:

```bash
hzn eventlog list
```
{: codeblock}
