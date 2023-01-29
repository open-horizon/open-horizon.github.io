---

copyright:
years: 2021
lastupdated: "2021-02-20"
title: Troubleshooting tips

parent: Help and Support
grand_parent: Docs
nav_order: 2
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Troubleshooting tips and frequently asked questions
{: #troubleshooting}

Review the troubleshooting tips and frequently asked questions to help you troubleshoot issues that you might encounter.
{:shortdesc}

* [Troubleshooting tips](#ts_tips)
* [Frequently asked questions](../getting_started/faq.md)

The following troubleshooting content describes the main components of {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) and how to investigate the included interfaces to determine the state of the system.

## Troubleshooting tools
{: #ts_tools}

Many interfaces that are included with {{site.data.keyword.ieam}} provide information that can be used to diagnose problems. This information is available through the {{site.data.keyword.gui}}, and HTTP REST APIs and a {{site.data.keyword.linux_notm}} shell tool, `hzn`.

On an edge node you might need to troubleshoot host issues, Horizon software issues, Docker issues, or issues in your configuration or the code in service containers. Edge node host issues are beyond the scope of this document. If you need to troubleshoot Docker issues, you can use many Docker commands and interfaces. For more information, see the Docker documentation.

If the service containers you are running use {{site.data.keyword.message_hub_notm}} (which is based on Kafka) for messaging, you can manually connect to the Kafka streams for {{site.data.keyword.ieam}} to diagnose problems. You can either subscribe to a message topic to observe what was received by {{site.data.keyword.message_hub_notm}}, or you can publish to a message topic to simulate messages from another device. The `kafkacat` {{site.data.keyword.linux_notm}} command is a way to publish or subscribe to {{site.data.keyword.message_hub_notm}}. Use the most recent version of this tool. {{site.data.keyword.message_hub_notm}} also provides graphical web pages that you can use to access some information.

On any edge node where {{site.data.keyword.horizon}} is installed, use the `hzn` command to debug issues with the local {{site.data.keyword.horizon}} agent and the remote {{site.data.keyword.horizon_exchange}}. Internally, the `hzn` command interacts with the provided HTTP REST APIs. The `hzn` command simplifies access and provides a better user experience than the REST APIs themselves. The `hzn` command often provides more descriptive text in its output, and it includes a built-in online help system. Use the help system to obtain information and details about what commands to use and details about command syntax and arguments. To view this help information, run the `hzn --help` or `hzn <subcommand> --help` commands.

On edge nodes where {{site.data.keyword.horizon}} packages are not supported or installed, you can directly interact with the underlying HTTP REST APIs instead. For example, you can use the `curl` utility or other REST API CLI utilities. You can also write a program in a language that supports REST queries.

For example, run the `curl` utility to check the status of your edge node:
```
curl localhost:8510/status
```

## Troubleshooting tips
{: #ts_tips}

To help troubleshoot specific issues, review the questions about your system state and any associated tips about the following topics. For each question, a description is provided of why the question is relevant to troubleshooting your system. For some questions, tips or a detailed guide is provided to learn how to obtain the related information for your system.

These questions are based on the nature of debugging issues and are related to different environments. For example, when troubleshooting issues on an edge node, you might need complete access to and control of the node, which can increase your capability to collect and view information.

* [Troubleshooting tips](index.md)

  Review the common issues that you might encounter when you use {{site.data.keyword.ieam}}.
  
## {{site.data.keyword.ieam}} risks and resolution
{: #risks}

Although {{site.data.keyword.ieam}} creates unique opportunities, it also presents challenges. For example, it transcends the cloud data center physical boundaries, which can expose security, addressability, management, ownership, and compliance issues. More importantly, it multiplies the scaling issues of cloud-based management techniques.

Edge networks increase the number of compute nodes by an order of magnitude. Edge gateways increase that by another order of magnitude. Edge devices increase that number by 3 to 4 orders of magnitude. If DevOps (continuous delivery and continuous deployment) are critical to managing a hyper-scale cloud infrastructure, then zero-ops (operations with no human intervention) is critical to managing at the massive scale that {{site.data.keyword.ieam}} represents.

It is critical to deploy, update, monitor, and recover the edge compute space without human intervention. All of these activities and processes must be:

* Fully automated
* Capable of independent decision-making about work allocation
* Able to recognize and recover from changing conditions without intervention.

All of these activities must be secure, traceable, and defensible.
