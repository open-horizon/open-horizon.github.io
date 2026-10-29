# Automated agent installation and registration

Note: These steps are the same for all edge device types (architectures).

1. If you don't already have your authorization information, get it now. For details about how to get the authorization information, see [Authentication overview](https://open-horizon.github.io/docs/anax/docs/authentication_overview/index.md).
1. Log in to your edge device and set the same environment variables that you obtained in step 1:

```
export HZN_ORG_ID=<your-exchange-organization>
export HZN_EXCHANGE_USER_AUTH=<authentication string>
export HZN_EXCHANGE_URL= # example http://open-horizon.lfedge.iol.unh.edu:3090/v1
export HZN_FSS_CSSURL= # example http://open-horizon.lfedge.iol.unh.edu:9443/
export HZN_AGBOT_URL= # example http://open-horizon.lfedge.iol.unh.edu:3111
export HZN_FDO_SVC_URL= # example http://open-horizon.lfedge.iol.unh.edu:9008/api
```

Note: To prevent errors, the exchange URL should not have a trailing slash.

1. If you are not using an admin prepared installation bundle, download the **agent-install.sh** script from the Cloud Sync Service (CSS) to your device and make it executable:

```
curl -u "$HZN_ORG_ID/$HZN_EXCHANGE_USER_AUTH" -k -o agent-install.sh $HZN_FSS_CSSURL/api/v1/objects/IBM/agent_files/agent-install.sh/data
chmod +x agent-install.sh
```

1. Run **agent-install.sh** to get the necessary files from CSS (Cloud Sync Service), install and configure the Horizon agent, and register your edge device to run the helloworld sample edge service:

```
sudo -s -E ./agent-install.sh -i 'css:' -p IBM/pattern-ibm.helloworld -w '*' -T 120
```

To see all available **agent-install.sh** flag descriptions run: **./agent-install.sh -h**

Note: On macOS, the agent will be run in a docker container running as root.

1. View the helloworld output:

```
hzn service log -f ibm.helloworld
# Press Ctrl-c to stop the output display
```

1. If the helloworld edge service does not start, run this command to see error messages:

```
hzn eventlog list -f
# Press Ctrl-c to stop the output display
```

1. (optional) Use the **hzn** command on this edge node to view services, patterns, and deployment policies in the Horizon Exchange. Set your specific information as environment variables in your shell and run these commands:

```
eval export $(cat agent-install.cfg)
hzn exchange service list IBM/
hzn exchange pattern list IBM/
hzn exchange deployment listpolicy
```

1. Explore all of the **hzn** command flags and subcommands:

```
hzn --help
```

## What's next

- Use the Open Horizon console to view your edge nodes (devices), services, patterns, and policies.
- Explore and run another edge service example. For more information, see [CPU usage to IBM Event Streams](https://open-horizon.github.io/docs/using_edge_services/cpu_load_example/index.md).
