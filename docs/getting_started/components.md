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

# Components

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) includes several components that are bundled with the product.
{:shortdesc}

View the following table for a description of the {{site.data.keyword.ieam}} components:

|Component|Version|Description|
|---------|-------|----|
|[IBM Cloud Platform Common Services![Opens in a new tab](../images/icons/launch-glyph.svg "Opens in a new tab")](https://www.ibm.com/support/knowledgecenter/SSHKN6/kc_welcome_cs.html)|3.5.x|This is a set of foundational components that are installed automatically as part of the {{site.data.keyword.ieam}} operator installation.|
|Agbot|2.27.0-173|Agreement bot (agbot) instances are created centrally and are responsible for deploying workloads and machine learning models to {{site.data.keyword.ieam}}.|
|Cloud Sync Service |1.4.1-173|The CSS is the component of the Model Management System (MMS) that stores machine learning models for later deployment to edge devices.|
|Exchange API|2.54.0-176|The Exchange provides the REST API that holds all the definitions (patterns, policies, services, and so on) used by all the other components in {{site.data.keyword.ieam}}.|
|Management console|1.3.27-207|The web UI used by {{site.data.keyword.ieam}} administrators to view and manage the other components of  {{site.data.keyword.ieam}}.|
|Secure Device Onboard|1.8.6-83|The SDO component enables technology created by Intel to make it easy and secure to configure edge devices and associate them with an edge management hub.|
|Cluster Agent|2.27.0-173|This is a container image which is installed as an agent on edge clusters to enable node workload management by {{site.data.keyword.ieam}}.|
|Device Agent|2.27.0-173|This component is installed on edge devices to enable node workload management by {{site.data.keyword.ieam}}.|
