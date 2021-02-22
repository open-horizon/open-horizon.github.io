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

# Gather edge node files
{: #prereq_horizon}

Several files are needed to install the {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) agent on your edge devices and edge clusters and register them with {{site.data.keyword.ieam}}. This content guides you through bundling the files that are needed for your edge nodes. Perform these steps on an admin host that is connected to the {{site.data.keyword.ieam}} management hub.

The following steps assume that you have installed the **cloudctl** and **oc** CLIs, and that you are running the steps from within the unpacked installation media directory **ibm-eam-{{site.data.keyword.semver}}-agent-x86_64**. This script searches for the required {{site.data.keyword.horizon}} packages in the **agent/edge-packages-{{site.data.keyword.semver}}.tar.gz** file, and creates the necessary edge node configuration and certificate files.

1. Set the following environment variables. This assumes you are still logged in to **oc** as a result of the management hub installation steps.

   ```bash
   export CLUSTER_URL=https://$(oc get cm management-ingress-ibmcloud-cluster-info -o jsonpath='{.data.cluster_ca_domain}')
   export CLUSTER_USER=$(oc -n ibm-common-services get secret platform-auth-idp-credentials -o jsonpath='{.data.admin_username}' | base64 --decode)
   export CLUSTER_PW=$(oc -n ibm-common-services get secret platform-auth-idp-credentials -o jsonpath='{.data.admin_password}' | base64 --decode)
   oc --insecure-skip-tls-verify=true -n kube-public get secret ibmcloud-cluster-ca-cert -o jsonpath="{.data.ca\.crt}" | base64 --decode > ieam.crt
   export HZN_MGMT_HUB_CERT_PATH="$PWD/ieam.crt"
   export HZN_FSS_CSSURL=${CLUSTER_URL}/edge-css
   ```
   {: codeblock}

2. Move into the **agent** directory where **edge-packages-{{site.data.keyword.semver}}.tar.gz** is:

   ```bash
   cd agent
   ```
   {: codeblock}

3. Run the **edgeNodeFiles.sh** script to gather the necessary files and put them in the CSS (Cloud Sync Service) component of the Model Management System. (The **edgeNodeFiles.sh** script was installed as part of the **horizon-cli** package and should be in your path.)

   ```bash
   HZN_EXCHANGE_USER_AUTH='' edgeNodeFiles.sh ALL -c -p edge-packages-4.2.0
   ```
   {: codeblock}

   On each edge node use the **-i 'css:'** flag of **agent-install.sh** to have it get the needed files from CSS.

   **Note:** If you plan to use [SDO-enabled edge devices](../installing/sdo.md), you must run this form of the `edgeNodeFiles.sh` command.

4. Alternatively, use **edgeNodeFiles.sh** to bundle the files in a tar file:

   ```bash
   edgeNodeFiles.sh ALL -t -p edge-packages-4.2.0
   ```
   {: codeblock}

   Copy the tar file to each edge node and use the **-z** flag of **agent-install.sh** to get the needed files from tar file.

**Note:** **edgeNodeFiles.sh** has more flags to control what files are gathered and where they should be placed. To see all of the available flags, run: **edgeNodeFiles.sh -h**

## What's next

Before edge nodes are set up, you or your node technicians must create an API key and gather other environment variable values. Follow the steps in [Prepare for setting up edge nodes](prepare_for_edge_nodes.md).
