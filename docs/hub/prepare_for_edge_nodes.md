---
copyright: Contributors to the Open Horizon project
years: 2020 - 2025
title: Prepare for setting up edge nodes
description: Documentation for Prepare for setting up edge nodes
lastupdated: 2025-05-03
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

This content explains how to use your issued authentication credentials and related environment variable values to install the anax Agent on edge nodes. Perform these steps on an edge host that can connect to your {{site.data.keyword.ieam}} management hub cluster.

## Before you begin

- Contact your {{site.data.keyword.ieam}} administrator for the information that you need to log in to the desired management hub instance.  If you do not have one, you may choose to install an [all-in-one instance](https://open-horizon.github.io/docs/mgmt-hub/docs/) locally on an x86 machine, or you can request an account on [the LF Edge Community Lab developer instances](https://wiki.lfedge.org/display/LE/Open+Horizon+Management+Hub+Developer+Instance).

## Procedure

1. Each user who is setting up edge nodes must have an authentication string. You can use the same authentication string to set up all of your edge nodes (it is not saved on the edge nodes). An administrator can create a new user from the CLI:

   ```bash
   hzn exchange user create -o <existing organization ID> [-A] <desired username> <desired password> <user email address>
   ```
   {: codeblock}

   Note the optional `-A` flag which grants organization admin privileges.  The authentication string will be a combination of `username` and `password` separated by a colon.  Both values should begin with an alpha character, not a number.  Neither should contain spaces.

2. If you have not already installed the **horizon-cli** package on this host, do that now. See [Post installation configuration](post_install.md#postconfig) for an example of this process.

3. Locate the **agent-install.sh** and **agent-uninstall.sh** scripts that were installed as part of the **horizon-cli** package. These scripts are required on each edge node during setup (currently **agent-uninstall.sh** only supports edge clusters):

   - {{site.data.keyword.linux_notm}} example:

     ```bash
     ls /usr/horizon/bin/agent-{install,uninstall}.sh
     ```
     {: codeblock}

   - {{site.data.keyword.macOS_notm}} example:

     ```bash
     ls /usr/local/bin/agent-{install,uninstall}.sh
     ```
     {: codeblock}

4. Contact your {{site.data.keyword.ieam}} administrator for help in setting these environment variables:

   ```bash
   export HZN_ORG_ID=<your-exchange-organization>
   export HZN_EXCHANGE_USER_AUTH=<authentication string>
   export HZN_EXCHANGE_URL= # example http://open-horizon.lfedge.iol.unh.edu:3090/v1
   export HZN_FSS_CSSURL= # example http://open-horizon.lfedge.iol.unh.edu:9443/
   export HZN_AGBOT_URL= # example http://open-horizon.lfedge.iol.unh.edu:3111
   export HZN_FDO_SVC_URL= # example http://open-horizon.lfedge.iol.unh.edu:9008/api
   ```
   {: codeblock}

## What's next

When you are ready to set up edge nodes, follow the steps in [Installing edge nodes](../installing/installing_edge_nodes.md).
