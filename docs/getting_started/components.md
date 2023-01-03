---

copyright:
years: 2019 - 2022
lastupdated: "2022-07-07"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Components

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) includes several components that are bundled with the product.
{:shortdesc}

View the following table for a description of the {{site.data.keyword.ieam}} components:

|Component|Version|Description|
|---------|-------|----|
|Agbot|{{site.data.keyword.anax_ver}}|Agreement bot (agbot) instances are created centrally and are responsible for deploying workloads and machine learning models to {{site.data.keyword.ieam}}.|
|MMS |1.6.12-660|The Model Management System (MMS) facilitates the storage, delivery, and security of models, data, and other metadata packages needed by edge services. This enables edge nodes to easily send and receive models and metadata to and from the cloud.|
|Exchange API|2.87.4-605|The Exchange provides the REST API that holds all the definitions (patterns, policies, services, and so on) used by all the other components in {{site.data.keyword.ieam}}.|
|Secure Device Onboard|1.11.14-40|The SDO component enables technology that is created by Intel to make it simple and secure to configure edge devices and associate them with an edge management hub.|
|Cluster Agent|{{site.data.keyword.anax_ver}}|This is a container image, which is installed as an agent on edge clusters to enable node workload management by {{site.data.keyword.ieam}}.|
|Device Agent|{{site.data.keyword.anax_ver}}|This component is installed on edge devices to enable node workload management by {{site.data.keyword.ieam}}.|
|Secrets Manager|1.1.1-208|The Secrets Manager is the repository for secrets deployed to edge devices, enabling services to securely receive credentials used to authenticate to their upstream dependencies.|
