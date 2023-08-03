---
copyright:
years: 2020 - 2023
lastupdated: "2023-07-01"
title: "FDO agent install"

parent: Edge devices info
grand_parent: Edge devices
nav_order: 6
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# FDO agent installation and registration
{: #fdo}

[FIDO Device Onboard (FDO) ](https://github.com/open-horizon/FDO-support/blob/main/README.md){:target="_blank"}{: .externalLink}, created by Intel, makes it easy to add edge devices built with FDO (FIDO Device Onboard) to an {{site.data.keyword.ieam}} instance by simply importing their associated ownership vouchers and then powering on the devices.

## FDO overview
{: #fdo-overview}

The software in the FDO git repository provides integration between FDO and {{site.data.keyword.ieam}}, making it easy to use FDO-enabled edge devices with Horizon. The Horizon FDO support consists of these components:

* A docker image of of the FDO Owner service (those that run on the {{site.data.keyword.edge_notm}} management hub).
* An `hzn fdo voucher` sub-command to import one or more ownership vouchers into Owner service. (An ownership voucher is a file that the device manufacturer gives to the purchaser (owner) along with the physical device.)
* A sample script called `start-mfg.sh` to start the development manufacturing service so that the ownership voucher can be extended to the user to enable them to run through the FDO-enabling steps on a Virtual Machine (VM) device that a device manufacturer would run on a physical device. This allows you to try out the FDO process with your Horizon instance before purchasing FDO-enabled devices.
* A REST API that authenticates users through the Horizon Exchange and enables importing and querying ownership vouchers.

**Note**: FDO only supports edge devices, not edge clusters.

## Before you begin
{: #before_begin}

FDO requires that the agent files are stored in the {{site.data.keyword.ieam}} Cloud Sync Service (CSS). If this has not been done, ask your administrator to run one of the following commands as described in [Gather edge node files](../hub/gather_files.md):

  `edgeNodeFiles.sh ALL -c ...`

## Trying FDO
{: #trying-fdo}

Before you purchase FDO-enabled edge devices, you can test FDO support in {{site.data.keyword.ieam}} with a VM that simulates an FDO-enabled device:

1. You need an API key. See [Creating your API key](../hub/prepare_for_edge_nodes.md) for instructions to create an API key, if you do not already have one.

2. Contact your {{site.data.keyword.ieam}} administrator to get the values of these environment variables. (You need them in the next step.)

   ```bash
   export HZN_ORG_ID=<exchange-org>
   export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
   export HZN_FDO_SVC_URL=https://<mgmt-hub-ingress>/edge-fdo-ocs/api
   export HZN_MGMT_HUB_CERT_PATH=<path-to-mgmt-hub-self-signed-cert>
   export CURL_CA_BUNDLE=$HZN_MGMT_HUB_CERT_PATH
   ```
   {: codeblock}

3. Follow the steps in the [FIDO Device Onboard (FDO) ](https://github.com/open-horizon/FDO-support/blob/main/README.md){:target="_blank"}{: .externalLink} to observe FDO automatically install the {{site.data.keyword.ieam}} agent on a device and registers it with your {{site.data.keyword.ieam}} management hub.

## Adding FDO-enabled devices to your {{site.data.keyword.ieam}} domain
{: #using-fdo}

If you have purchased FDO-enabled devices and want to incorporate them into your {{site.data.keyword.ieam}} domain:

1. If you did not create FDO owner key pairs when trying out FDO in the previous section, perform these steps:

   1. You need an API key. See [Prepare for setting up edge nodes](../hub/prepare_for_edge_nodes.md) for instructions to create an API key, if you do not already have one.

   2. Contact your {{site.data.keyword.ieam}} administrator to get the values of these environment variables. (You need them in the next step.)

      ```bash
      export HZN_ORG_ID=<exchange-org>
      export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
      export HZN_FDO_SVC_URL=https://<mgmt-hub-ingress>/edge-fdo-ocs/api
      export HZN_MGMT_HUB_CERT_PATH=<path-to-mgmt-hub-self-signed-cert>
      export CURL_CA_BUNDLE=$HZN_MGMT_HUB_CERT_PATH
      ```
      {: codeblock}

   3. To download the public key for FDO, use the device alias you received from the manufacturer device initialization. Then, use that device alias to download the corresponding public key. For more information, see [Generate Owner Key Pairs ](https://github.com/open-horizon/FDO-support/blob/main/README.md){:target="_blank"}{: .externalLink}.

2. [Log in to the {{site.data.keyword.ieam}} management console](../console/accessing_ui.md).

3. On the **Nodes** tab, click **Add node**.

4. Fill in the necessary information to import the ownership vouchers you received when you purchased the devices.

5. Connect the devices to the network and power them on.

6. Back in the management console, watch the progress of the devices as they come online by viewing the **Node** overview page and filtering on the installation name.
