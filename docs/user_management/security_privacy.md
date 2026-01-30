---
copyright: Contributors to the Open Horizon project
years: 2021 - 2026
title: Security and privacy
description: Documentation for Security and privacy
lastupdated: 2025-05-03
nav_order: 1
parent: Security
grand_parent: Administering
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Security and privacy
{: #security_privacy}

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}), based on [Open Horizon ](https://github.com/open-horizon){:target="_blank"}{: .externalLink}, uses several different security technologies to ensure that it is secure against attacks and safeguards privacy. {{site.data.keyword.ieam}} relies on geographically distributed autonomous agent processes for edge software management. As a result, both the {{site.data.keyword.ieam}} management hub and the agents represent potential targets for security breaches. This document explains how {{site.data.keyword.ieam}} mitigates or eliminates threats.
{:shortdesc}

## Management Hub
The {{site.data.keyword.ieam}} management hub is deployed into an {{site.data.keyword.open_shift_cp}}; thus, it inherits all of the inherent security mechanism benefits. All of the {{site.data.keyword.ieam}} management hub network traffic traverses a TLS-secured entry point. Management hub network communication between the {{site.data.keyword.ieam}} management hub components is performed without TLS.

## Secure Control Plane
{: #dc_pane}

The {{site.data.keyword.ieam}} management hub and distributed agents communicate over the control plane to deploy workloads and models to edge nodes. In contrast to typical centralized Internet of Things (IoT) platforms and cloud-based control systems, the {{site.data.keyword.ieam}} control plane is mostly decentralized. Each actor within the system has a limited scope of authority so that each actor has only the minimum level of authority that is needed to complete its tasks. No single actor can assert control over the entire system. Furthermore, a single actor cannot gain access to all of the edge nodes in the system by compromising any single edge node, host, or software component.

The control plane is implemented by three different software entities:
* Open {{site.data.keyword.horizon}} agents
* Open {{site.data.keyword.horizon_agbots}}
* Open {{site.data.keyword.horizon_exchange}}

Open {{site.data.keyword.horizon}} agents and {{site.data.keyword.agbot}}s are the primary actors within the control plane. The {{site.data.keyword.horizon_exchange}} facilitates discovery and secure communication between the agents and {{site.data.keyword.agbot}}s. Together, they provide message-level protection by using an algorithm that is called Perfect Forward Secrecy.

By default, agents and {{site.data.keyword.agbot}}s communicate with the exchange via TLS 1.3. But TLS itself does not provide enough security. {{site.data.keyword.ieam}} encrypts every control message that flows between agents and {{site.data.keyword.agbot}}s before it is sent over the network. Each agent and {{site.data.keyword.agbot}} generates a 2048-bit RSA key pair and publishes its public key in the exchange. The private key is stored in each actor's root-protected storage. Other actors in the system use the message receiver's public key to encrypt a symmetric key that is used to encrypt control plane messages. This ensures that only the intended receiver can decrypt the symmetric key; thus, the message itself. Perfect Forward Secrecy use in the control plane provides extra security, such as preventing man-in-the-middle attacks, which TLS does not prevent.

### Agents
{: #agents}

{{site.data.keyword.horizon_open}} agents outnumber all of the other actors in {{site.data.keyword.ieam}}. An agent runs on each of the managed edge nodes. Each agent has authority to manage only that edge node. A compromised agent does not have any authority to affect any other edge nodes, or any other component of the system. Each node has unique credentials that are stored in its own root protected storage. The {{site.data.keyword.horizon_exchange}} ensures that a node can only access its own resources. When a node is registered, by using the `hzn register` command, it is possible to provide an authentication token. However, it is best practice to allow the agent to generate its own token so that no person is aware of the node credentials, which reduces the potential for compromising the edge node.

The agent is secure from network attacks because it has no listening ports on the host network. All communication between the agent and the management hub is accomplished by the agent polling the management hub. Furthermore, users are highly encouraged to protect edge nodes with a network firewall that prevents intrusion to the node's host. Despite these protections, if the agent's host operating system or the agent process itself is hacked or otherwise compromised, then only that edge node is compromised. All other parts of the {{site.data.keyword.ieam}} system are unaffected.

The agent is responsible for downloading and starting containerized workloads. To ensure that the downloaded container image and its configuration are not compromised, the agent verifies the container image digital signature and the deployment configuration digital signature. When a container is stored in a container registry, the registry provides a digital signature for the image (for example, a SHA256 hash). The container registry manages the keys that are used to create the signature. When an {{site.data.keyword.ieam}} service is published by using the `hzn exchange service publish` command, it obtains the image signature and stores it with the published service in the {{site.data.keyword.horizon_exchange}}. The image's digital signature is passed to the agent over the secure control plane, which allows the agent to verify the container image signature against the downloaded image. If the image signature does not match the image, the agent does not start the container. The process is similar for the container configuration, with one exception. The `hzn exchange service publish` command signs the container configuration and stores the signature in the {{site.data.keyword.horizon_exchange}}. In this case, the user (publishing the service) must provide the RSA key pair that is used to create the signature. The `hzn key create` command can be used to generate keys for this purpose if the user does not already have any keys. The public key is stored in the exchange with the signature of the container configuration and passed to the agent over the secure control plane. The agent can then use the public key to verify the container configuration. If you prefer to use a different key pair for each container configuration, the private key used to sign this container configuration can be discarded now, as it is no longer needed. See [Developing edge services](../developing/index.md) for more details on publishing a workload.

When a model is deployed to an edge node, the agent downloads the model and verfies the model's signature to ensure that it has not been tampered with in transit. The signature and verification key are created when the model is published to the management hub. The agent stores the model in root protected storage on the host. A credential is provided to each service when it is started by the agent. The service uses that credential to identify itself and enable access to the models that the service is allowed to access. Every model object in {{site.data.keyword.ieam}} indicates the list of services, which can access the model. Each service gets a new credential each time it is restarted by {{site.data.keyword.ieam}}. The model object is not encrypted by {{site.data.keyword.ieam}}. Because the model object is treated as a bag of bits by {{site.data.keyword.ieam}}, a service implementation is free to encrypt the model if necessary. For more about how to use the MMS, see [Model management details](../developing/model_management_details.md).

### {{site.data.keyword.agbot}}s
{: #agbots}

The {{site.data.keyword.ieam}} management hub contains several instances of an {{site.data.keyword.agbot}}, which are responsible for initiating the deployment of workloads to all the edge nodes registered with the management hub. {{site.data.keyword.agbot}}s periodically look at all the deployment policies and patterns that have been published to the exchange, ensuring that the services in those patterns and policies are deployed on all the correct edge nodes. When an {{site.data.keyword.agbot}} initiates a deployment request, it sends the request over the secure control plane. The deployment request contains everything the agent needs to verify the workload and its configuration, should the agent decide to accept the request. See [Agents](./security_privacy.md#agents) for security details on what the agent does. The {{site.data.keyword.agbot}} also directs the MMS where and when to deploy models. See [Agents](./security_privacy.md#agents) for security details on how models are managed.

A compromised {{site.data.keyword.agbot}} can attempt to propose malicious workload deployments, but the proposed deployment must meet the security requirements that are stated in the agent section. Even though the {{site.data.keyword.agbot}} initiates workload deployment it has no authority to create workloads and container configurations and therefore is unable to propose its own malicious workloads.

## {{site.data.keyword.horizon_exchange}}
{: #exchange}

{{site.data.keyword.horizon_exchange}} is a centralized, replicated, and load balanced REST API server. It functions as a shared database of metadata for users, organizations, edge nodes, published services, policies, and patterns. It also enables the distributed agents and {{site.data.keyword.agbot}}s to deploy containerized workloads by providing the storage for the secure control plane, until the messages can be retrieved. The {{site.data.keyword.horizon_exchange}} is unable to read the control messages because it does not possess the private RSA key to decrypt the message. Thus a compromised {{site.data.keyword.horizon_exchange}} is incapable of spying on the control plane traffic. For more information on the role of the exchange, see [Overview of {{site.data.keyword.edge}}](../getting_started/overview_oh.md).

## Privileged mode services
{: #priv_services}
On a host machine, some tasks can only be performed by an account with root access. The equivalent for containers is privileged mode. While containers generally do not need privileged mode on the host, there are some use cases where it is required. In {{site.data.keyword.ieam}} you have the ability to specify that an application service should be deployed with privileged process execution enabled. By default, it is disabled. You must explicitly enable it in the [deployment configuration](https://github.com/open-horizon/anax/blob/master/docs/deployment_string.md){:target="_blank"}{: .externalLink} of the respective Service Definition file for each service that needs to run in  this mode. And further, any node on which you want to deploy that service must also explicitly allow privileged mode containers. This ensures that node owners have some control over which services are executing on their edge nodes. For an example of how to enable privileged mode policy on an edge node, see [privileged node policy](https://github.com/open-horizon/anax/blob/master/cli/samples/privileged_node_policy.json){:target="_blank"}{: .externalLink}. If the service definition or one of its dependencies requires privileged mode, the node policy must also allow privileged mode, or else none of the services will not be deployed to the node. For an indepth discussion of privileged mode see [What is privileged mode and do I need it?](https://wiki.lfedge.org/pages/viewpage.action?pageId=44171856){:target="_blank"}{: .externalLink}.  See also [RBAC](./rbac.md).

## Denial-of-service attack
{: #denial}

The {{site.data.keyword.ieam}} management hub is a centralized service. Centralized services in typical cloud based environments are generally vulnerable to denial-of-service attacks. The agent requires a connection only when it is first registered to the hub or when it is negotiating the deployment of a workload. At all other times, the agent continues to operate normally even while disconnected from the {{site.data.keyword.ieam}} management hub.  This ensures that the {{site.data.keyword.ieam}} agent remains active on edge node even if the management hub is under attack.

## Model Management System
{: #malware}

{{site.data.keyword.ieam}} does not perform a malware or virus scan on data that is uploaded to the MMS. Ensure that any uploaded data has been scanned before uploading it to the MMS.

## Data at REST
{: #drest}

{{site.data.keyword.ieam}} does not encrypt data at rest. Encryption of data at rest should be implemented with a utility that is appropriate for the host operating system on which the {{site.data.keyword.ieam}} management hub or agent is running.

## Security Standards
{: #standards}

The following security standards are used within {{site.data.keyword.ieam}}:
* TLS 1.3 (HTTPS) is used for encryption of data in transit to and from the management hub.
* AES 256-bit encryption is used for data in transit, specifically the messages that flow over the secure control plane.
* 2048-bit RSA key pairs are used for data in transit, specifically the AES 256 symmetric key that flows over the secure control plane.
* RSA keys provided by a user to sign container deployment configurations when using the **hzn exchange service publish** command.
* RSA key pair as generated by the **hzn key create** command, if the user chooses to use this command. The bit size of this key is 4096 by default, but can be changed by the user.

## Summary
{: #summary}

{{site.data.keyword.edge_notm}} uses hashes, cryptographic signatures, and encryption to ensure security against unwanted access. By being mostly decentralized, {{site.data.keyword.ieam}} avoids exposure to most attacks that are typically found in edge computing environments. By constraining the scope of authority of participant roles, {{site.data.keyword.ieam}} contains the potential damage from a compromised host, or compromised software component to that part of the system. Even large-scale external attacks on the centralized services of the {{site.data.keyword.horizon}} services that are used in {{site.data.keyword.ieam}} have minimal impact on the execution of workloads at the edge.

## Next

See [Security](./security.md) topics page for related information.
