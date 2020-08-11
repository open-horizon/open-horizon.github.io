---
layout: page
title: "How to use Open Horizon"
description: "Basic instructions and examples for using the Open Horizon projects CLI"
---

# How to use Open Horizon

## Now that I have it installed, what next?

You should become familiar with the Command Line Interface (CLI). This is the primary way to interact with the Anax agent and management hub services.

> Note: Type `hzn` to view information about getting started with the CLI.

## Try a command

Use "version" to view the CLI and agent version numbers:

{% capture code %}hzn version{% endcapture %}
{% include code_snippet.md code=code language='shell' %}

In this example, the command returns:

``` text
Horizon CLI version: 2.26.12
Horizon Agent version: 2.26.12
```

## Find the edge nodes configuration

Use `node` to find the node configuration from the agent:

{% capture code %}hzn node list{% endcapture %}
{% include code_snippet.md code=code language='shell' %}

> Note the typical [CLI] [Object Noun] [Action Verb] pattern.

The response should be similar to this JSON example:

``` json
{
  "id": "node1",
  "organization": "myorg",
  "pattern": "",
  "name": "node1",
  "nodeType": "device",
  "token_last_valid_time": "2020-08-04 16:00:30 -0400 EDT",
  "token_valid": true,
  "ha": false,
  "configstate": {
    "state": "configured",
    "last_update_time": "2020-08-04 16:00:31 -0400 EDT"
  },
  "configuration": {
    "exchange_api": "http://host.docker.internal:3090/v1/",
    "exchange_version": "2.37.0",
    "required_minimum_exchange_version": "2.23.0",
    "preferred_exchange_version": "2.23.0",
    "mms_api": "http://host.docker.internal:9443",
    "architecture": "amd64",
    "horizon_version": "2.26.12"
  }
}
```

### Example details

In the first two lines, `id` is the ID assigned to this edge node and `organization` is the ad-hoc group that owns the device.

If the `configstate.state` property value is **configured**, the edge node is currently registered for a service.

Lastly, if you do not see a version number value in the `configuration.exchange_version` property, this is probably because the agent cannot query the exchange service for the version. This might indicate that your agent is not connected to the management hub, but this is not typical in all-in-one installations.

## Check the agreement

Check the agreement formed when your edge node registered for a service:

{% capture code %}hzn agreement list{% endcapture %}
{% include code_snippet.md code=code language='shell' %}

This command displays a JSON array of objects showing one or more active agreements between the edge node and AgBots:

``` json
[
  {
    "name": "Policy for myorg/node1 merged with myorg/policy-ibm.helloworld_1.0.0",
    "current_agreement_id": "83785680de5d22c874a0f54dc229738a0e744db22b2c0deeb320b9fdf0967138",
    "consumer_id": "IBM/agbot",
    "agreement_creation_time": "2020-08-04 16:44:36 -0400 EDT",
    "agreement_accepted_time": "",
    "agreement_finalized_time": "",
    "agreement_execution_start_time": "",
    "agreement_data_received_time": "",
    "agreement_protocol": "Basic",
    "workload_to_run": {
      "url": "ibm.helloworld",
      "org": "IBM",
      "version": "1.0.0",
      "arch": "amd64"
    }
  }
]
```

Note the following properties:

| Property | Description |
| --- | --- |
| `0.agreement_creation_time` | When the agreement was proposed by the AgBot |
| `0.agreement_accepted_time` | When the agreement was accepted by the edge node |
| `0.agreement_finalized_time` | When the agreement was completed |
| `0.agreement_execution_start_time` | When the edge node began downloading the container image(s) |

After you see the `agreement_execution_start_time` value, you can run `docker ps` to confirm that the workloads have started.

## More activities

| Task | Command |
| --- | --- |
| View the default "helloworld" sample service | `hzn service log -f ibm.helloworld` |
| View the agreement negotiation logged steps | `hzn eventlog list` |
| View the node policy | `hzn policy list` |

## Communicate with the exchange

To use the exchange communication commands, set up two environment variables.

### Pre-requisite

You need this information from the all-in-one installation summary message displayed when you installed the management hub, agent, and CLI.  The summary message is similar to this example:

``` text
----------- Summary of what was done:
  1. Started Horizon management hub services: agbot, exchange, postgres DB, CSS, mongo DB
  2. Created exchange resources: system org (IBM) admin user, user org (myorg) and admin user, and agbot
     - Exchange root user generated password: 1234567890
     - System org admin user generated password: AbcDEfg
     - Agbot generated token: Abc123YZ
     - User org admin user generated password: XLmdsg236
     - Node generated token: uingtw398J
     Important: save these generated passwords/tokens in a safe place. You will not be able to query them from Horizon.
  3. Installed the Horizon agent and CLI (hzn)
  4. Created a Horizon developer key pair
  5. Installed the Horizon examples
  6. Created and registered an edge node to run the helloworld example edge service
For what to do next, see: https://github.com/open-horizon/devops/blob/master/mgmt-hub/README.md#all-in-1-what-next
```

Use the "User org admin user generated password" in the previous message to export the following environment variables, using the substitution shown below:

``` shell
export HZN_ORG_ID=myorg
export HZN_EXCHANGE_USER_AUTH=admin:[User org admin user generated password]
```

> Now, you should be able to connect to the exchange with the CLI.

Use `hzn exchange status` or `hzn exchange node list` to confirm that it works with no errors. Additionally, `hzn exchange user list` displays the user account that you are currently using and if it is authenticated successfully.

These commands are available now:

| Task | Command |
| --- | --- |
| View the example edge services | `hzn exchange service list IBM/` |
| View the example patterns | `hzn exchange pattern list IBM/` |
| View the example deployment policies | `hzn exchange deployment listpolicy` |

## More information

Use the hzn [command] (sub-command) -h pattern to explore other commands.

Example:

* `hzn -h`
* `hzn exchange -h`
* `hzn exchange status -h`
