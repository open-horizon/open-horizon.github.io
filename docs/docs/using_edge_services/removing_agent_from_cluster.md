---
copyright: Contributors to the Open Horizon project
years: 2022 - 2025
title: Removing the agent from an edge cluster
description: Documentation for Removing the agent from an edge cluster
lastupdated: 2025-05-03
nav_order: 4
parent: Edge clusters
---

# Removing the agent from an edge cluster

To unregister an edge cluster and remove the Open Horizon agent from that cluster, perform these steps:

1. Extract the **agent-uninstall.sh** script from the tar file:

   ```bash
   tar -zxvf agentInstallFiles-x86_64-Cluster.tar.gz agent-uninstall.sh
   ```

2. Export your Horizon exchange user credentials:

   ```bash
   export HZN_ORG_ID=<your-exchange-organization>
   export HZN_EXCHANGE_USER_AUTH=<authentication string>
   export HZN_EXCHANGE_URL= # example http://open-horizon.lfedge.iol.unh.edu:3090/v1
   export HZN_FSS_CSSURL= # example http://open-horizon.lfedge.iol.unh.edu:9443/
   export HZN_AGBOT_URL= # example http://open-horizon.lfedge.iol.unh.edu:3111
   export HZN_FDO_SVC_URL= # example http://open-horizon.lfedge.iol.unh.edu:9008/api
   ```

3. Remove the agent:

   ```bash
   ./agent-uninstall.sh -u $HZN_EXCHANGE_USER_AUTH -d
   ```

Note: Occasionally, deleting the namespace stalls in the "Terminating" state. In this situation, see [A namespace is stuck in the Terminating state ](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.1.1/troubleshoot/ns_terminating.html) to manually delete namespace.
