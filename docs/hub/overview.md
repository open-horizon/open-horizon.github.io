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

# Overview
{: #Overview}

Edge computing is about placing enterprise applications closer to where data is created.
{:shortdesc}

* [Benefits of edge computing](#edge_benefits)
* [Examples](#examples)
* [Concepts](#concepts)
  
Edge computing is an important emerging paradigm that can expand your operating model by virtualizing your cloud beyond a data center or cloud computing center. Edge computing moves application workloads from a centralized location to remote locations, such as factory floors, warehouses, distribution centers, retail stores, transportation centers, and more. Essentially, edge computing provides the capability to move application workloads anywhere that computing is needed outside of your data centers and cloud hosting environment.

{{site.data.keyword.ieam}} provides you with edge computing features to help you manage and deploy workloads from a hub cluster to remote instances of {{site.data.keyword.open_shift_cp}} or other Kubernetes-based clusters.

{{site.data.keyword.ieam}} also includes support for an {{site.data.keyword.edge_profile}}. This supported profile can help you reduce the resource usage of {{site.data.keyword.open_shift_cp}} when {{site.data.keyword.open_shift_cp}} is installed for use in hosting a remote edge cluster. This profile places the minimum services that are needed to support robust remote management of these server environments and the enterprise-critical applications you are hosting there. With this profile, you are still able to authenticate users, collect log and event data, and deploy workloads in a single or set of clustered worker nodes.

## Benefits of edge computing
{: #edge_benefits}

* Value-added change for your organization: Moving application workloads to edge nodes for supporting operations at remote locations where the data is collected instead of sending the data to the central data center for processing.

* Reduce IT staff dependencies: Using {{site.data.keyword.ieam}} can potentially help you to reduce your IT staff dependencies. Use {{site.data.keyword.ieam}} to deploy and manage critical workloads on edge clusters securely and reliably to hundreds of remote locations from a central location. This capability eliminates the need for full-time IT staff at each remote location to manage the workloads onsite.

## Examples
{: #examples}

Edge computing is about placing enterprise applications closer to where data is created. For example, if you operate a factory, your factory floor equipment can include sensors for recording any number of data points that provide details about how your plant is operating. The sensors can record the number of parts that are being assembled per hour, the time that is required for a stacker to return to its starting position, or the operating temperature of a fabricating machine. The information from these data points can be beneficial in helping you determine whether you are operating at peak efficiency, identify the quality levels that you are achieving, or predict when a machine is likely to fail and require preventive maintenance.

In another example, if you have workers in remote locations whose job can result in them working in hazardous situations, such as hot or loud environments, being near exhaust or production fumes, or heavy machinery, you might need to monitor the environment conditions. You can collect information from various sources that can be used at the remote locations. The data from this monitoring can be used by supervisors to determine when to instruct workers to take breaks, rehydrate, or to shut down equipment.

In a further example, you can use video cameras to monitor properties, such as to identify foot traffic into retail stores, restaurants, or entertainment venues, to serve as a security monitor to record acts of vandalism or other unwanted activities, or to recognize emergency conditions. If you also collect data from the videos, you can use edge computing to process video analytics locally to help your workers respond quicker to opportunities and incidents. Restaurant workers can better estimate how much food to prepare, retail managers can determine whether to open more check-out counters, and security personnel can respond faster to emergencies or alert first-responders.

In all of these cases, sending the recorded data to a cloud computing center or data center can add latency to the data processing. This loss of time can have negative consequences when you are trying to respond to critical situations or opportunities.

If the recorded data is data that does not require any special or time-sensitive processing, you can incur substantial network and storage costs for unnecessarily sending this normal data.

Alternatively, if any collected data is also sensitive, such as personal information, you increase the risk of exposing that data every time you move the data to another location from where that data was created.

Additionally, if any of your network connections are unreliable, you also run the risk of interrupting critical operations.

## Concepts
{: #concepts}

**edge device**: A piece of equipment, such as an assembly machine on a factory floor, an ATM, an intelligent camera, or an automobile, that has integrated compute capacity on which meaningful work can be performed and data that is collected or produced.

**edge gateway**: An edge cluster that has services that perform network functions such as protocol translation, network termination, tunneling, firewall protection, or wireless connections. An edge gateway serves as the connection point between an edge device or edge cluster and the cloud or a larger network.

**edge node**: Any edge device, edge cluster, or edge gateway where edge computing takes place.

**edge cluster**: A computer in a remote operations facility that runs enterprise application workloads and shared services. An edge cluster can be used to connect to an edge device, connect to another edge cluster, or serve as an edge gateway for connecting to the cloud or to a larger network.

**edge service**: A service that is designed specifically to be deployed on an edge cluster, edge gateway, or edge device. Visual recognition, acoustic insights, and speech recognition are all examples of potential edge services.

**edge workload**: Any service, microservice, or piece of software that does meaningful work when it runs on an edge node.

Public, private, and content-delivery networks are transforming from simple pipes to higher-value hosting environments for applications in the form of the edge network cloud. Typical use cases for {{site.data.keyword.ieam}} include:

* Edge nodes deployment
* Edge nodes compute operations capacity
* Edge nodes support and optimization

{{site.data.keyword.ieam}} unifies cloud platforms from multiple vendors into a consistent dashboard from on-premises to the edge. {{site.data.keyword.ieam}} is a natural extension that enables the distribution and management of workloads beyond the edge network to edge gateways and edge devices. {{site.data.keyword.ieam}} also recognizes workloads from Enterprise applications with edge components, private and hybrid cloud environments, and public cloud; where {{site.data.keyword.ieam}} provides a new execution environment for distributed AI to reach critical data sources.

In addition, {{site.data.keyword.ieam}} delivers AI tools for accelerated deep learning, visual and speech recognition, and video and acoustic analytics, which enables inferencing on all resolutions and most formats of video and audio conversation services and discovery.

## What's next

- [Sizing and system requirements](cluster_sizing.md)
- [Installing the management hub](hub.md)
