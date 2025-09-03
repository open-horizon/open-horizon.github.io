---
copyright: Contributors to the Open Horizon project
years: 2020 - 2025
title: Automated agent installation and registration
description: Documentation for Automated agent installation and registration
lastupdated: 2025-09-02
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Automated agent installation and registration
{: #method_one}

Note: These steps are the same for all edge device types (architectures).

1. If you don't already have your authorization information, get it now. For details about how to get the authorization information, see [Authentication overview](../anax/docs/authentication_overview.md).

2. Log in to your edge device and set the same environment variables that you obtained in step 1:

   ```bash
   export HZN_ORG_ID=<your-exchange-organization>
   export HZN_EXCHANGE_USER_AUTH=<authentication string>
   export HZN_EXCHANGE_URL= # example http://open-horizon.lfedge.iol.unh.edu:3090/v1
   export HZN_FSS_CSSURL= # example http://open-horizon.lfedge.iol.unh.edu:9443/
   export HZN_AGBOT_URL= # example http://open-horizon.lfedge.iol.unh.edu:3111
   export HZN_FDO_SVC_URL= # example http://open-horizon.lfedge.iol.unh.edu:9008/api
   ```
   {: codeblock}

   Note: To prevent errors, the exchange URL should not have a trailing slash.

3. If you are not using an admin prepared installation bundle, download the **agent-install.sh** script from the Cloud Sync Service (CSS) to your device and make it executable:

   ```bash
   curl -u "$HZN_ORG_ID/$HZN_EXCHANGE_USER_AUTH" -k -o agent-install.sh $HZN_FSS_CSSURL/api/v1/objects/IBM/agent_files/agent-install.sh/data
   chmod +x agent-install.sh
   ```
   {: codeblock}

4. Run **agent-install.sh** to get the necessary files from CSS (Cloud Sync Service), install and configure the {{site.data.keyword.horizon}} agent, and register your edge device to run the helloworld sample edge service:

   ```bash
   sudo -s -E ./agent-install.sh -i 'css:' -p IBM/pattern-ibm.helloworld -w '*' -T 120
   ```
   {: codeblock}

   To see all available **agent-install.sh** flag descriptions run: **./agent-install.sh -h**

   Note: On {{site.data.keyword.macOS_notm}}, the agent will be run in a docker container running as root.

5. View the helloworld output:

   ```bash
   hzn service log -f ibm.helloworld
   # Press Ctrl-c to stop the output display
   ```
   {: codeblock}

6. If the helloworld edge service does not start, run this command to see error messages:

   ```bash
   hzn eventlog list -f
   # Press Ctrl-c to stop the output display
   ```
   {: codeblock}

7. (optional) Use the **hzn** command on this edge node to view services, patterns, and deployment policies in the {{site.data.keyword.horizon}} Exchange. Set your specific information as environment variables in your shell and run these commands:

   ```bash
   eval export $(cat agent-install.cfg)
   hzn exchange service list IBM/
   hzn exchange pattern list IBM/
   hzn exchange deployment listpolicy
   ```
   {: codeblock}

8. Explore all of the **hzn** command flags and subcommands:

   ```bash
   hzn --help
   ```
   {: codeblock}

## What's next

* Use the {{site.data.keyword.ieam}} console to view your edge nodes (devices), services, patterns, and policies.
* Explore and run another edge service example. For more information, see [CPU usage to IBM Event Streams](../using_edge_services/cpu_load_example.md).
