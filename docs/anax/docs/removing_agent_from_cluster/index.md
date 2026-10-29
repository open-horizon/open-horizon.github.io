# Removing the agent from an edge cluster

To unregister an edge cluster and remove the Open Horizon agent from that cluster, perform these steps:

1. Extract the **agent-uninstall.sh** script from the tar file:

```
tar -zxvf agentInstallFiles-x86_64-Cluster.tar.gz agent-uninstall.sh
```

1. Export your Horizon exchange user credentials:

```
export HZN_ORG_ID=<your-exchange-organization>
export HZN_EXCHANGE_USER_AUTH=<authentication string>
export HZN_EXCHANGE_URL= # example http://open-horizon.lfedge.iol.unh.edu:3090/v1
export HZN_FSS_CSSURL= # example http://open-horizon.lfedge.iol.unh.edu:9443
```

1. Remove the agent:

```
./agent-uninstall.sh -u $HZN_EXCHANGE_USER_AUTH -d
```

Note: Occasionally, deleting the namespace stalls in the "Terminating" state. In this situation, see [A namespace is stuck in the Terminating state](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.1.1/troubleshoot/ns_terminating.html) to manually delete namespace.
