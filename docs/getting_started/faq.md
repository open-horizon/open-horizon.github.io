---
copyright:
years: 2020 - 2022
lastupdated: "2022-03-17"
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Frequently asked questions

{: #faqs}

The following are answers to some frequently asked questions (FAQs) about {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}).
{:shortdesc}

- [Is there a way to create a self-contained environment for development purposes?](#one_click)
- [Is {{site.data.keyword.ieam}} software open-sourced?](#open_sourced)
- [How can I use {{site.data.keyword.ieam}} to develop and deploy edge services?](#dev_dep)
- [What edge node hardware platforms does {{site.data.keyword.ieam}} support?](#hw_plat)
- [Can I run any {{site.data.keyword.linux_notm}} distribution on my edge nodes with {{site.data.keyword.ieam}}?](#lin_dist)
- [Which programming languages and environments are supported by {{site.data.keyword.ieam}}?](#pro_env)
- [Is there detailed documentation for the REST APIs provided by the components in {{site.data.keyword.ieam}}?](#rest_doc)
- [Does {{site.data.keyword.ieam}} use Kubernetes?](#use_kube)
- [Does {{site.data.keyword.ieam}} use MQTT?](#use_mqtt)
- [How long does it normally take after I register an edge node before agreements are formed and the corresponding containers start running?](#agree_run)
- [Can the {{site.data.keyword.horizon}} software and all other software or data that is related to {{site.data.keyword.ieam}} be removed from an edge node host?](#sw_rem)
- [Is there a dashboard for visualizing the agreements and services that are active on an edge node?](#db_node)
- [What happens if a container image download is interrupted by a network outage?](#image_download)
- [How is {{site.data.keyword.ieam}} secure?](#ieam_secure)
- [How do I manage AI at the Edge with models vs AI on the Cloud?](#ai_cloud)

## Is there a way to create a self-contained environment for development purposes?

{: #one_click}

You can install the open source management hub (without the {{site.data.keyword.ieam}} management console) with the "all-in-one" installer for developers. The all-in-one installer creates a complete but minimal management hub, not suitable for production use. It also configures an example edge node. This tool enables open source component developers to get started quickly without the time it takes to configure a complete production {{site.data.keyword.ieam}} management hub. For information about the all-in-one installer, see [Open Horizon - Devops ](https://github.com/open-horizon/devops/tree/master/mgmt-hub){:target="_blank"}{: .externalLink}.

## Is {{site.data.keyword.ieam}} software open-sourced?

{: #open_sourced}

{{site.data.keyword.ieam}} is an IBM product. But its core components heavily use the [Open Horizon - EdgeX Project Group ](https://wiki.edgexfoundry.org/display/FA/Open+Horizon+-+EdgeX+Project+Group){:target="_blank"}{: .externalLink} open source project. Many sample and example programs that are available in the {{site.data.keyword.horizon}} project work with {{site.data.keyword.ieam}}. For more information about the project, see [Open Horizon - EdgeX Project Group ](https://wiki.edgexfoundry.org/display/FA/Open+Horizon+-+EdgeX+Project+Group){:target="_blank"}{: .externalLink}.

## How can I develop and deploy edge services with {{site.data.keyword.ieam}}?

{: #dev_dep}

See [Using edge services](../using_edge_services/using_edge_services.md).

## What edge node hardware platforms does {{site.data.keyword.ieam}} support?

{: #hw_plat}

{{site.data.keyword.ieam}} supports different hardware architectures through the Debian {{site.data.keyword.linux_notm}} binary package for {{site.data.keyword.horizon}} or through Docker containers. For more information, see [Installing {{site.data.keyword.horizon}} software](../installing/installing_edge_nodes.md).

## Can I run any {{site.data.keyword.linux_notm}} distribution on my edge nodes with {{site.data.keyword.ieam}}?

{: #lin_dist}

Yes, and no.

You can develop edge software that uses any {{site.data.keyword.linux_notm}} distribution as the base image of the Docker containers (if it uses the Dockerfile `FROM` statement) if that base functions on the host {{site.data.keyword.linux_notm}} kernel on your edge nodes. This means that you can use any distribution for your containers that Docker is able to run on your edge hosts.

However, your edge node host operating system must be able to run a recent version of Docker and be able to run the {{site.data.keyword.horizon}} software. Currently, the {{site.data.keyword.horizon}} software is provided only as a Debian and RPM packages for edge nodes that run {{site.data.keyword.linux_notm}}. For Apple Macintosh machines, a Docker container version is provided. The {{site.data.keyword.horizon}} development team primarily uses Apple Macintosh, or the Ubuntu or Raspberry Pi OS {{site.data.keyword.linux_notm}} distributions.

Additionally, RPM package installation was tested on edge nodes configured with Red Hat Enterprise Linux (RHEL) Version 8.2.

## Which programming languages and environments are supported by {{site.data.keyword.ieam}}?

{: #pro_env}

{{site.data.keyword.ieam}} supports almost any programming language and software library that you are able to configure to run in an appropriate Docker container on your edge nodes.

If your software requires access to specific hardware or operating system services, you might need to provide `docker run`-equivalent arguments to support that access. You can specify supported arguments within the `deployment` section of your Docker container definition file.

## Is there detailed documentation for the REST APIs provided by the components in {{site.data.keyword.ieam}}?

{: #rest_doc}

Yes. For more information, see [{{site.data.keyword.ieam}} APIs](../api/index.md).

## Does {{site.data.keyword.ieam}} use Kubernetes?

{: #use_kube}

Yes. {{site.data.keyword.ieam}} uses [{{site.data.keyword.open_shift_cp}} ](https://docs.openshift.com/container-platform/4.6/welcome/index.html){:target="_blank"}{: .externalLink} Kubernetes services.

## Does {{site.data.keyword.ieam}} use MQTT?

{: #use_mqtt}

{{site.data.keyword.ieam}} does not use Message Queuing Telemetry Transport (MQTT) to support its own internal functions, however the programs you deploy on your edge nodes are free to use MQTT for their own purposes. Example programs are available that use MQTT and other technologies (for example, {{site.data.keyword.message_hub_notm}}, based on the Apache Kafka) to transport data to and from edge nodes.

## How long does it normally take after registering an edge node before agreements are formed, and the corresponding containers start running?

{: #agree_run}

Typically, it takes only a few seconds after registration for the agent and a remote {{site.data.keyword.agbot}} to finalize an agreement to deploy software. After that occurs, the {{site.data.keyword.horizon}} agent downloads (`docker pull`) your containers to the edge node, verify their cryptographic signatures with {{site.data.keyword.horizon_exchange}}, and run them. Depending on the sizes of your containers, and the time it takes them to start and be functional, it can take from just a few more seconds, to many minutes before the edge node is fully operational.

After you have registered an edge node, you can run the `hzn node list` command to view the state of {{site.data.keyword.horizon}} on your edge node. When the `hzn node list` command shows that the state is `configured`, the {{site.data.keyword.horizon}} {{site.data.keyword.agbot}}s are able to discover the edge node and begin to form agreements.

To observe the agreement negotiation process phases, you can use the `hzn agreement list` command.

After an agreement list is finalized, you can use the `docker ps` command to view the running containers. You can also issue `docker inspect <container>` to see more detailed information about the deployment of any specific `<container>`.

## Can the {{site.data.keyword.horizon}} software and all other software or data that is related to {{site.data.keyword.ieam}} be removed from an edge node host?

{: #sw_rem}

Yes. If your edge node is registered, unregister the edge node by running:
{% capture code %}hzn unregister -f -r{% endcapture %}

{% include code_snippet.md code=code language='shell' %}

When the edge node is unregistered, you can remove the installed {{site.data.keyword.horizon}} software, for example for Debian-based systems run:

{% capture code %}sudo apt purge -y bluehorizon horizon horizon-cli{% endcapture %}

{% include code_snippet.md code=code language='shell' %}

## Is there a dashboard for visualizing the agreements and services that are active on an edge node?

{: #db_node}

You can use the {{site.data.keyword.ieam}} web UI to observe your edge nodes and services.

Also, you can use the `hzn` command to obtain information about the active agreements and services by using the local {{site.data.keyword.horizon}} agent REST API on the edge node. Run the following commands to use the API to retrieve the related information:

{% capture code %}hzn node list
hzn agreement list
docker ps{% endcapture %}

{% include code_snippet.md code=code language='shell' %}

## What happens if a container image download is interrupted by a network outage?

{: #image_download}

The docker API is used to download container images. If the docker API terminates the download, it returns an error to the agent. In turn, the agent cancels the current deployment attempt. When the {{site.data.keyword.agbot}} detects the cancellation, it initiates a new deployment attempt with the agent. During the subsequent deployment attempt, the docker API resumes the download from where it left off. This process continues until the image is fully downloaded and the deployment can proceed. The docker binding API is responsible for the image pull, and in case of failure, the agreement is canceled.

## How is {{site.data.keyword.ieam}} secure?

{: #ieam_secure}

- {{site.data.keyword.ieam}} automates and uses cryptographically signed public-private key authentication of edge devices as it communicates with the {{site.data.keyword.ieam}} management hub during provisioning. Communication is always initiated and controlled by the edge node.
- System has node and service credentials.
- Software verification and authenticity using hash verification.

See [Security at the Edge ](https://www.ibm.com/cloud/blog/security-at-the-edge){:target="_blank"}{: .externalLink}.

## How do I manage AI at the Edge with models vs AI on the Cloud?

{: #ai_cloud}

Typically, AI at the edge enables you to perform on-the-spot machine inferencing with subsecond latency, which enables real-time response based on use case and hardware (for example, RaspberryPi, Intel x86, and Nvidia Jetson nano). {{site.data.keyword.ieam}} model management system enables you to deploy updated AI models without any service downtime.

See [Models Deployed at the Edge ](https://www.ibm.com/cloud/blog/models-deployed-at-the-edge){:target="_blank"}{: .externalLink}.
