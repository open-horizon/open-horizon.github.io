---

copyright:
years: 2020 - 2022
lastupdated: "2022-06-24"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Prepare for setting up edge nodes
{: #prepare_for_edge_nodes}

This content explains how to create an API key and gather some files and environment variable values that are needed when you set up edge nodes. Perform these steps on an admin host that can connect to your {{site.data.keyword.ieam}} management hub cluster.

## Before you begin

- If you have not already installed **cloudctl**, see [Installing cloudctl, oc, and kubectl](../cli/cloudctl_oc_cli.md) to do that.
- Contact your {{site.data.keyword.ieam}} administrator for the information that you need to log in to the management hub via **cloudctl**.

## Procedure

1. Use `cloudctl` to log in to the {{site.data.keyword.ieam}} management hub. Specify the user that you want to create an API key for:

   ```bash
   cloudctl login -a <cluster-url> -u <user> -p <password> --skip-ssl-validation
   ```
   {: codeblock}

2. Each user who is setting up edge nodes must have an API key. You can use the same API key to set up all of your edge nodes (it is not saved on the edge nodes). Create an API key:

   ```bash
   cloudctl iam api-key-create "<choose-an-api-key-name>" -d "<choose-an-api-key-description>"
   ```
   {: codeblock}

   Find the key value in the command output; this is the line that starts with **API Key**. Save the key value for future use because you cannot query it from the system later.

3. If you have not already installed the **horizon-cli** package on this host, do that now. See [Post installation configuration](post_install.md#postconfig) for an example of this process.

4. Locate the **agent-install.sh** and **agent-uninstall.sh** scripts that were installed as part of the **horizon-cli** package. These scripts are required on each edge node during setup (currently **agent-uninstall.sh** only supports edge clusters):

   - {{site.data.keyword.linux_notm}} example:

     ```bash
     ls /usr/horizon/bin/agent-{install,uninstall}.sh
     ```
     {: codeblock}

   - {{site.data.keyword.macOS}} example:

     ```bash
     ls /usr/local/bin/agent-{install,uninstall}.sh
     ```
     {: codeblock}

5. Contact your {{site.data.keyword.ieam}} administrator for help in setting these environment variables:

   ```bash
   export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
   export HZN_ORG_ID=<your-exchange-organization>
   mgmtHubIngress=$(oc get cm management-ingress-ibmcloud-cluster-info -o jsonpath='{.data.cluster_ca_domain}')
   export HZN_FSS_CSSURL=https://$mgmtHubIngress/edge-css/
   echo "export HZN_FSS_CSSURL=$HZN_FSS_CSSURL"
   ```
   {: codeblock}

## What's next

When you are ready to set up edge nodes, follow the steps in [Installing edge nodes](../installing/installing_edge_nodes.md).
