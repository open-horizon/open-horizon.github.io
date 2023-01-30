---

copyright:
years: 2020 - 2022
lastupdated: "2022-03-17"
title: "Using patterns"

parent: Deploying edge services
grand_parent: Using edge services
nav_order: 2
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Using patterns
{: #using_patterns}

Typically, service deployment patterns can be published to the {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) hub after a developer published an edge service in the horizon exchange.

The hzn CLI provides capabilities to list and manage patterns in the {{site.data.keyword.horizon_exchange}}, including commands to list, publish, verify, update, and remove service deployment patterns. It also provides a way to list and remove cryptographic keys that are associated with a specific deployment pattern.

For a full list of CLI commands and further details:

```
hzn exchange pattern -h
```
{: codeblock}

## Example

Sign and create (or update) a pattern resource in the {{site.data.keyword.horizon_exchange}}:

```
hzn exchange pattern publish --json-file=JSON-FILE [<flags>]
```
{: codeblock}

## Using deployment patterns

Using a deployment pattern is a straightforward and simple way to deploy a service to your edge node. You specify the top-level service, or multiple top-level services, to be deployed to your edge node and {{site.data.keyword.ieam}} handles the rest, including the deployment of any dependent services your top-level service might have.

After you create and add a service to the {{site.data.keyword.ieam}} exchange, you need to create a `pattern.json` file, similar to:

```
{
  "IBM/pattern-ibm.cpu2evtstreams": {
    "owner": "root/root",
    "label": "Edge ibm.cpu2evtstreams Service Pattern for arm architectures",
    "description": "Pattern for ibm.cpu2evtstreams sending cpu and gps info to the IBM Event Streams",
    "public": true,
    "services": [
      {
        "serviceUrl": "ibm.cpu2evtstreams",
        "serviceOrgid": "IBM",
        "serviceArch": "arm",
        "serviceVersions": [
          {
            "version": "1.4.3",
            "priority": {},
            "upgradePolicy": {}
          }
        ],
        "dataVerification": {
          "metering": {}
        },
        "nodeHealth": {
          "missing_heartbeat_interval": 1800,
          "check_agreement_status": 1800
        }
      }
    ],
    "agreementProtocols": [
      {
        "name": "Basic"
      }
    ],
    "lastUpdated": "2020-10-24T14:46:44.341Z[UTC]"
  }
}
```
{: codeblock}

This code is an example of a `pattern.json` file for the `ibm.cpu2evtstreams` service for `arm` devices. As shown here, there is no need to specify `cpu_percent` and `gps` (dependent services of `cpu2evtstreams`). That task is taken care of by the `service_definition.json` file, so a successfully registered edge node runs those workloads automatically.

The `pattern.json` file gives you the ability to customize rollback settings in the `serviceVersions` section. You can specify multiple older versions of your service and give each version a priority for your edge node to roll back to if there is an error with your new version. In addition to assigning a priority to each rollback version, you can specify things like number and duration of retry attempts before falling back to a lower priority version of the specified service.

You can also set any configuration variables your service might need to correctly function centrally when you publish your deployment pattern by including them in the `userInput` section near the bottom. When the `ibm.cpu2evtstreams` service is published, it passes with it the credentials necessary to publish data to IBM Event Streams, which can be done with:

```
hzn exchange pattern publish -f pattern.json
```
{: codeblock}

With the pattern published, you can then register an arm device to it:

```
hzn register -p pattern-ibm.cpu2evtstreams-arm
```
{: codeblock}

This command deploys `ibm.cpu2evtstreams` and any dependent services to your node.

**Note**: A `userInput.json` file is not passed into the `hzn register` command above, as it would if you were following the steps in [Using the CPU To IBM Event Streams Edge Service with Deployment Pattern ](https://github.com/open-horizon/examples/tree/master/edge/evtstreams/cpu2evtstreams#-using-the-cpu-to-ibm-event-streams-edge-service-with-deployment-pattern){:target="_blank"}{: .externalLink} repository example. Because user inputs were passed with the pattern itself, any edge node that registers automatically has access to those environment variables.

All `ibm.cpu2evtstreams` workloads can be stopped by unregistering:

```
hzn unregister -fD
```
{: codeblock}
