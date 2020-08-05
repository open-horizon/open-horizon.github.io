---
layout: page
title: "How to Use Open Horizon"
description: "TBD"
---

# How to Use Open Horizon

## Now that I have it installed, what next?

Let's start by getting familiar with the CLI (Command Line Interface), 
which is the primary way you can interact directly with the Anax Agent and the Management Hub services.  The CLI uses a short, easy-to-remember synonym for the word "horizon", `hzn`.  If you remember nothing else about how to use Open Horizon, just type in `hzn` from the command prompt to get a complete view of how to get started using the CLI.

## Your first command

The first command to try can be the simple "version", which will tell you the version numbers of both the CLI and the Agent.  If the CLI can't tell you the Agent version, or it doesn't match the CLI version, you have a problem.  This will most likely not happen.  Give it a try:

``` shell
hzn version
```

At the time we wrote the documentation, that command returned this:

``` text
Horizon CLI version: 2.26.12
Horizon Agent version: 2.26.12
```

## Get the Agent's configuration

Now that we've established that the CLI is working, let's use the "node" command to get the node's configuration from the Agent:

``` shell
hzn node list
```

Notice that the typical pattern we're following here is [CLI] [Object Noun] [Action Verb]. 
The response that you will get back will look vaguely like this JSON example:

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

This output will require a little more explanation. 
Beginning with the first two lines, `id` refers to the ID we assigned to this edge node, and `organization` refers to the ad-hoc group that the device "belongs" to. 

Next, take a look at the `configstate.state` property.  If the value is "configured", then this tells you that the edge node is currently registered for a service.

Last, look at the `configuration.exchange_version` property.  If you do not see a version number as the value, this is most likely because the Agent cannot query the Exchange service for the version, which may mean that your Agent is not connected to the Management Hub.  This will most likely not happen using the all-in-one installation.

## Look at the Agreement formed when your node registered for a service

``` shell
hzn agreement list
```

This command will display a JSON array of objects showing one or more active agreements between the edge node and AgBots:

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

Pay attention to the following properties:
* `0.agreement_creation_time` - When the agreement was proposed by the AgBot
* `0.agreement_accepted_time` - When the agreement was accepted by the edge node
* `0.agreement_finalized_time` - When the agreement was completed
* `0.agreement_execution_start_time` - When the edge node began downloading the container image(s)

Once you see a value for `agreement_execution_start_time`, you should expect to be able to run `docker ps` to see the workloads starting.

## Other things to try

To see the logs of the sample "helloworld" service installed by default, try `hzn service log -f ibm.helloworld`.

To view all of the steps logged in the process of negotiating an agreement, type `hzn eventlog list`.

And to view the node's policy that triggered deployment of the "helloworld" service, try `hzn policy list`.

## One last thing ...

We've been using the CLI to communicate with the Anax agent.  There's a whole other set of commands to run that have you communicating with the Exchange.  To get those working, you'll need to set two environment variables.  To do so, you'll need one important bit of information from the all-in-one installation summary message.  Hopefully you saved that information.  It should look something like this:

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

Using the "User org admin user generated password" from the message above, export the following two environment variables with the substitution shown below:

``` shell
export HZN_ORG_ID=myorg
export HZN_EXCHANGE_USER_AUTH=admin:[User org admin user generated password]
```

Once you've done that, you should be able to connect to the Exchange with the CLI.  Try `hzn exchange status` or `hzn exchange node list` to confirrm that it is working with no errors.  Also, `hzn exchange user list` will show you what user account you are currently using, and if it is successfully authenticated.

Here are three commands you can now run:

* View the example edge services: `hzn exchange service list IBM/`
* View the example patterns: `hzn exchange pattern list IBM/`
* View the example deployment policies: `hzn exchange deployment listpolicy`

## Want some more?

To view other commands to run, try exploring by using the following pattern "hzn [command] (sub-command) -h".