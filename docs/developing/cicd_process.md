---
copyright: Contributors to the Open Horizon project
years: 2020 - 2025
title: CI-CD process
description: Documentation for CI-CD process for edge services
lastupdated: 2025-05-03
nav_order: 2
parent: Further reading for devices
grand_parent: Developing edge services
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# CI-CD process for edge services
{: #edge_native_practices}

A set of evolving edge services is essential for the effective use of {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}), and a robust Continuous Integration and Continuous Deployment (CI/CD) process is a critical component.

Use this content to lay out the building blocks available for you to create your own CI/CD process. Then, learn more about this process in the [`open-horizon/examples` repository ](https://github.com/open-horizon/examples){:target="_blank"}{: .externalLink}.

## Configuration variables
{: #config_variables}

As an Edge services developer, consider the service container size under development. Based on that information, you might need to divide your service features into separate containers. In this situation, configuration variables that are used for testing purposes can help simulate data that comes from a not-yet developed container. In the [cpu2evtstreams service definition file ](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/cpu2evtstreams/horizon/service.definition.json){:target="_blank"}{: .externalLink}, you can see input variables like **PUBLISH** and **MOCK**. If you examine the `service.sh` code, you see that it uses these, and other configuration variables to control its behavior. **PUBLISH** controls if the code attempts to send messages to IBM Event Streams. **MOCK** controls if service.sh attempts to contact the REST APIs and its dependent services (cpu and gps) or if `service.sh` creates fake data.

At the time of service deployment, you can override the configuration variable default values by specifying them in the node definition or on the `hzn register` command.

## Cross-compiling
{: #cross_compiling}

You can use Docker to build a containerized service for multiple architectures from a single amd64 machine. Similarly, you can develop edge services with compiled programming languages that support cross-compilation, such as Go. For example, if you are writing code on your Mac (an amd64 architecture device) for an arm device (a Raspberry Pi), you might need to build a Docker container that specifies parameters like GOARCH to target arm. This set up can prevent deployment errors. See [open-horizon gps service ](https://github.com/open-horizon/examples/tree/master/edge/services/gps){:target="_blank"}{: .externalLink}.

## Testing
{: #testing}

Frequent and automated testing is an important part of the development process. To facilitate testing, you can use the `hzn dev service start` command to run your service in a simulated Horizon agent environment. This approach is also useful in devops environments where it might be problematic to install and register the full Horizon agent. This method automates services tests in the `open-horizon examples` repository with the **make test** target. See [make test target ](https://github.com/open-horizon/examples/blob/305c4f375aafb09733f244ec9a899ce136b6d311/edge/services/helloworld/Makefile#L30){:target="_blank"}{: .externalLink}.

Run **make test** to build and run the service that uses **hzn dev service start**. After that is running, [serviceTest.sh ](https://github.com/open-horizon/examples/blob/master/tools/serviceTest.sh){:target="_blank"}{: .externalLink} monitors the service logs to locate data that indicates the service is running correctly.

## Testing deployment
{: #testing_deployment}

When you are developing a new service version, access to a full, real-world test is ideal. To do this, you can deploy your service to edge nodes; however, because this is a test, you might not want to initially deploy your service to all of your edge nodes.

To do this, create a deployment policy or pattern that refers only to your new service version. Then, register your testing nodes with this new policy or pattern. If using a policy, one option is to set a property on an edge node. For example, "name": "mode", "value": "testing"), and add that constraint to your deployment policy ("mode == testing"). This lets you be sure only the nodes you set aside for testing receive the new version of your service.

Note: You can create a deployment policy or pattern using the {{site.data.keyword.edge_notm}} CLI.

## Production deployment
{: #production_deployment}

After you move the new version of your service from a testing to a production environment, issues that were not encountered during testing can occur. Your deployment policy or pattern rollback settings are useful in addressing these issues. In a pattern or deployment policy `serviceVersions` section, you can specify multiple, older versions of your service. Give each version a priority for your edge node to roll back to if there is an error with your new version. In addition to assigning a priority to each rollback version, you can specify things like number and duration of retry attempts before falling back to a lower priority version of the specified service. For the specific syntax, see [this deployment policy example ](https://github.com/open-horizon/anax/blob/master/cli/samples/business_policy.json){:target="_blank"}{: .externalLink}.

## Viewing your edge nodes
{: #viewing_edge_nodes}

After deploying a new version of your service to nodes, it is important to be able to monitor the health of your edge nodes easily. Use the {{site.data.keyword.ieam}} {{site.data.keyword.gui}} for this task. For example, when you are in the [Testing deployment](#testing_deployment) or [Production deployment](#production_deployment) process, you can quickly search for nodes that use your deployment policy, or nodes with errors.

## Migrating services
{: #migrating_services}

At some point, you might need to move services, patterns, or policies from one instance of {{site.data.keyword.ieam}} to another. Similarly, you might need to move services from one exchange organization to another. This might happen if you installed a new instance of {{site.data.keyword.ieam}} to a different host environment. Alternatively, you might need to move services if you have two {{site.data.keyword.ieam}} instances, one dedicated to development and another for production. To facilitate this process, you can use the [`loadResources` script ](https://github.com/open-horizon/examples/blob/master/tools/loadResources){:target="_blank"}{: .externalLink} in the open-horizon examples repository.

## Automated pull request testing with Travis
{: #testing_with_travis}

You can automate testing whenever a pull request (PR) is opened to your GitHub repository by using [Travis CI ](https://travis-ci.com){:target="_blank"}{: .externalLink}.

Continue reading this content to learn how to leverage Travis and the techniques in the open-horizon examples GitHub repository.

In the examples repository, Travis CI is used to build, test, and publish samples. In the [`.travis.yml` file ](https://github.com/open-horizon/examples/blob/master/.travis.yml){:target="_blank"}{: .externalLink}, a virtual environment is set up to run as a Linux amd64 machine with hzn, Docker, and [qemu ](https://github.com/multiarch/qemu-user-static){:target="_blank"}{: .externalLink} for building on multiple architectures.

In this scenario, kafkacat is also installed to let cpu2evtstreams send data to IBM Event Streams. Similar to using the command line, Travis can use environment variables like `EVTSTREAMS_TOPIC` and `HZN_DEVICE_ID` for use with the sample edge services. The HZN_EXCHANGE_URL is set to point to the staging exchange for publishing any modified services. 

The [travis-find ](https://github.com/open-horizon/examples/blob/master/tools/travis-find){:target="_blank"}{: .externalLink} script is then used to identify services that have been modified by the opened pull request.

If a sample has been modified, the `test-all-arches` target in the **makefile** of that service runs. With the qemu containers of the supported architectures running, cross-architecture builds run with this **makefile** target by setting the `ARCH` environment variable immediately before building and testing.

The `hzn dev service start` command runs the edge service, and the [serviceTest.sh ](https://github.com/open-horizon/examples/blob/master/tools/serviceTest.sh){:target="_blank"}{: .externalLink} file monitors the service logs to determine if the service is operating correctly.

See [helloworld Makefile ](https://github.com/open-horizon/examples/blob/afd4a5822aede44616eb5da7cd9dafd4d78f12ec/edge/services/helloworld/Makefile#L24){:target="_blank"}{: .externalLink} to view the dedicated `test-all-arches` Makefile target.

The following scenario demonstrates a more thorough end-to-end test. If one of the modified samples includes `cpu2evtstreams`, an instance of IBM Event Streams can be monitored in the background and checked for HZN_DEVICE_ID. It can pass the test and be added to a list of all the passing services, only if it finds the **travis-test** node ID in the data read from the cpu2evtstreams topic. This requires an IBM Event Streams API key and broker url that are set as secret environment variables.

After the PR is merged, this process is repeated, and the list of passing services is used to identify which services can be published to the exchange. The Travis secret environment variables that are used in this example include everything that is needed to push, sign, and publish services to the exchange. This includes Docker credentials, HZN_EXCHANGE_USER_AUTH, and a cryptographic signing key pair that can be obtained with the `hzn key create` command. In order to save the signing keys as secure environment variables, they must be base64 encoded.

The list of services that passed the functional test is used to identify which services should be published with the dedicated publish `Makefile` target. See [helloworld sample ](https://github.com/open-horizon/examples/blob/afd4a5822aede44616eb5da7cd9dafd4d78f12ec/edge/services/helloworld/Makefile#L45){:target="_blank"}{: .externalLink}.

Because the services have been built and tested, this target publishes the service, service policy, pattern, and deployment policy in all architectures to the exchange.
