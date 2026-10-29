# FDO agent installation and registration

[FIDO Device Onboard (FDO)](https://github.com/open-horizon/FDO-support/blob/main/README.md) , created by Intel®, makes it easy to add edge devices built with Intel® FDO (FIDO Device Onboard) to an Open Horizon instance by simply importing their associated ownership vouchers and then powering on the devices.

## FDO overview

The software in the FDO git repository provides integration between FDO and Open Horizon, making it easy to use FDO-enabled edge devices with Horizon. The Horizon FDO support consists of these components:

- A docker image of of the FDO Owner service (those that run on the Open Horizon management hub).
- An `hzn fdo voucher` sub-command to import one or more ownership vouchers into Owner service. (An ownership voucher is a file that the device manufacturer gives to the purchaser (owner) along with the physical device.)
- A sample script called `start-mfg.sh` to start the development manufacturing service so that the ownership voucher can be extended to the user to enable them to run through the FDO-enabling steps on a Virtual Machine (VM) device that a device manufacturer would run on a physical device. This allows you to try out the FDO process with your Horizon instance before purchasing FDO-enabled devices.
- A sample script called start-rv.sh that you use to set up a development version of the FDO Rendezvous server. The script creates an environment where you can test the Rendezvous server and simulate the FDO onboarding process. You can also test the voucher exchange process for the device ownership transfer before you deploy FDO-enabled devices. To download the start-rv.sh script, see FDO support (https://github.com/open-horizon/FDO-support/blob/main/sample-rv/start-rv.sh).
- A REST API that authenticates users through the Horizon Exchange and enables importing and querying ownership vouchers.

**Note**: FDO only supports edge devices, not edge clusters.

## Before you begin

FDO requires that the agent files are stored in the Open Horizon Cloud Sync Service (CSS). If this has not been done, ask your administrator to run one of the following commands as described in [Gather edge node files](https://open-horizon.github.io/docs/hub/gather_files/index.md):

`edgeNodeFiles.sh ALL -c ...`

## Trying FDO

Before you purchase FDO-enabled edge devices, you can test FDO support in Open Horizon with a VM that simulates an FDO-enabled device:

1. If you don't already have your authorization information, get it now. For details about how to get the authorization information, see [Authentication overview](https://open-horizon.github.io/docs/anax/docs/authentication_overview/index.md).
1. Contact your Open Horizon administrator to get the values of these environment variables. (You need them in the next step.)

```
export HZN_ORG_ID=<your-exchange-organization>
export HZN_EXCHANGE_USER_AUTH=<authentication string>
export HZN_EXCHANGE_URL= # example http://open-horizon.lfedge.iol.unh.edu:3090/v1
export HZN_FSS_CSSURL= # example http://open-horizon.lfedge.iol.unh.edu:9443/
export HZN_AGBOT_URL= # example http://open-horizon.lfedge.iol.unh.edu:3111
export HZN_FDO_SVC_URL= # example http://open-horizon.lfedge.iol.unh.edu:9008/api
export HZN_MGMT_HUB_CERT_PATH=<path-to-mgmt-hub-self-signed-cert>
export CURL_CA_BUNDLE=$HZN_MGMT_HUB_CERT_PATH
```

1. Follow the steps in the [FIDO Device Onboard (FDO)](https://github.com/open-horizon/FDO-support/blob/main/README.md) to observe FDO automatically install the Open Horizon agent on a device and registers it with your Open Horizon management hub.

## Adding FDO-enabled devices to your Open Horizon domain

If you have purchased FDO-enabled devices and want to incorporate them into your Open Horizon domain:

1. If you did not create FDO owner key pairs when trying out FDO in the previous section, perform these steps:

1. If you don't already have your authorization information, get it now. For details about how to get the authorization information, see [Authentication overview](https://open-horizon.github.io/docs/anax/docs/authentication_overview/index.md).

1. Contact your Open Horizon administrator to get the values of these environment variables. (You need them in the next step.)

   ```
   export HZN_ORG_ID=<your-exchange-organization>
   export HZN_EXCHANGE_USER_AUTH=<authentication string>
   export HZN_EXCHANGE_URL= # example http://open-horizon.lfedge.iol.unh.edu:3090/v1
   export HZN_FSS_CSSURL= # example http://open-horizon.lfedge.iol.unh.edu:9443/
   export HZN_AGBOT_URL= # example http://open-horizon.lfedge.iol.unh.edu:3111
   export HZN_FDO_SVC_URL= # example http://open-horizon.lfedge.iol.unh.edu:9008/api
   export HZN_MGMT_HUB_CERT_PATH=<path-to-mgmt-hub-self-signed-cert>
   export CURL_CA_BUNDLE=$HZN_MGMT_HUB_CERT_PATH
   ```

1. To download the public key for FDO, use the device alias you received from the manufacturer device initialization. Then, use that device alias to download the corresponding public key. For more information, see [Generate Owner Key Pairs](https://github.com/open-horizon/FDO-support/blob/main/README.md) .

1. Using the `hzn` CLI, import the voucher using the following pattern.

   ```
   hzn fdo voucher import [<flags>] <voucher-file>
   ```

1. Use the ownership vouchers you received as `<voucher-file>` when you purchased the devices. The files must have a file type extension of txt, tar, tar.gz, tgz, or zip. If it is any of the tar/zip formats, all .txt files within it will be imported (other files/dirs will be silently ignored).

1. Connect the devices to the network and power them on.

1. Using the `hzn` CLI, monitor the progress of the devices as they come online using `hzn fdo voucher list` to confirm the voucher is listed, and `hzn fdo key list` to see the registered devices.
