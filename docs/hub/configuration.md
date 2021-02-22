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

# Configure {{site.data.keyword.ieam}}

## EamHub Custom Resource Configuration
{: #cr}

The main configuration for {{site.data.keyword.ieam}} is done through the EamHub custom resource, particularly the **spec** field of that custom resource.

This document assumes:
* The namespace you are running these commands for is in where the {{site.data.keyword.ieam}} management hub operator is deployed.
* The EamHub custom resource name is the default **ibm-edge**. If it is different, alter the commands to replace **ibm-edge**.
* The binary **jq** is installed, which ensures that the output is displayed in a readable format.


The defined default **spec** is minimal, only containing the license acceptance, which you can view with:
```
$ oc get eamhub ibm-edge -o yaml
...
spec:
  license:
    accept: true
...
```

### Operator Control Loop
{: #loop}

The {{site.data.keyword.ieam}} Management Hub operator runs in a continuous idempotent loop to synchronize the current state of resources with the expected state of resources.

Due to that continuous loop, you need to understand two things when you try to configure your operator-managed resources:
* Any change to the custom resource will be read asyncronously by the control loop. After you make the change, it might take a few minutes for that change to be enacted through the operator.
* Any manual change that is made to a resource the operator controls might be overwritten (undone) by the operator enforcing a specific state. 

Watch the operator pod logs to observe this loop:
```
oc logs $(oc get pods | grep ibm-eamhub-operator | awk '{print $1}') --tail 20 -f
```
{: codeblock}

When a loop finishes, it generates a **PLAY RECAP** summary. To see the most recent summary, run:
```
oc logs $(oc get pods | grep ibm-eamhub-operator | awk '{print $1}') --tail 5000 | grep -A 1 '^PLAY RECAP' | tail -n 1
```
{: codeblock}

The following indicates a loop that completed with no operations taking place (In its current state, the **PLAY RECAP** will always show **changed=1**):
```
$ oc logs $(oc get pods | grep ibm-eamhub-operator | awk '{print $1}') --tail 5000 | grep -A 1 '^PLAY RECAP' | tail -n 1
localhost                  : ok=51   changed=1    unreachable=0    failed=0    skipped=11   rescued=0    ignored=0
```
{: codeblock}

Review these 3 fields when making configuration changes:
* **changed**: When greater than **1** indicates the operator performed a task that altered the state of one or more resources (this could be at your request by altering the custom resource, or the operator reverting a manual change that was made).
* **rescued**: A task failed, however it was a known possible failure and the task will be attempted again on the next loop.
* **failed**: On initial install there are some expected failures, if you are repeatedly seeing the same failure and the message is not clear (or hidden) this likely indicates a problem.

### EamHub Common Configuration Options

Several configuration changes can be made, but some are more likely to be changed than others. This section describes some of the more common settings.

**Note:** Nested configuration values must be added in their entirety (See the [Scaling Configuration](./configuration.md#scale) for an example). This is due to an Ansible operator requirement to define a nested dictionary as a whole.

| Configuration value | Default | Description |
| :---: | :---: | :---: |
| Global values | -- | -- |
| pause_control_loop | false | Pauses the control loop mentioned above, for enabling temporary manual changes for debugging. Not to be used for steady-state. |
| ieam_maintenance_mode | false | Sets all pod replica counts without persistent storage to 0. Used for backup restoration purposes. |
| ieam_local_databases | true | Enables or disables local databases. Switching between states is not supported. See [remote database configuration](./configuration.md#remote). |
| ieam_database_HA | true | Enables or disables HA mode for local databases. This sets the replica count for all database pods to **3** when **true**, and **1** when **false**. |
| hide_sensitive_logs | true | Hides operator logs that deal with setting **Kubernetes Secrets**, if set to **false** task failures might result in the operator logging encoded authentication values. |
| storage_class_name | "" | Uses the default storage class if not set. |

## Remote Database Configuration
{: #remote}

**Note:** Switching between remote and local databases is not supported.

To install with remote databases, create the EamHub custom resource during installation with the extra value in the **spec** field:
```
spec:
  ieam_local_databases: false
  license:
    accept: true
```
{: codeblock}

Fill out the following template to create an authentication secret, be sure to read each comment to ensure it's filled out accurately and save it to **edge-auth-overrides.yaml**:
```
apiVersion: v1
kind: Secret
metadata:
  # NOTE: The name -must- be prepended by the name given to your Custom Resource, this defaults to 'ibm-edge'
  #name: <CR_NAME>-auth-overrides
  name: ibm-edge-auth-overrides
type: Opaque
stringData:
  # agbot postgresql connection settings uncomment and replace with your settings to use
  agbot-db-host: "<Single hostname of the remote database>"
  agbot-db-port: "<Single port the database runs on>"
  agbot-db-name: "<The name of the database to utilize on the postgresql instance>"
  agbot-db-user: "<Username used to connect>"
  agbot-db-pass: "<Password used to connect>"
  agbot-db-ssl: "<disable|require|verify-full>"
  # Ensure proper indentation (four spaces)
  agbot-db-cert: |-
    -----BEGIN CERTIFICATE-----
    ....
    -----END CERTIFICATE-----

  # exchange postgresql connection settings
  exchange-db-host: "<Single hostname of the remote database>"
  exchange-db-port: "<Single port the database runs on>"
  exchange-db-name: "<The name of the database to utilize on the postgresql instance>"
  exchange-db-user: "<Username used to connect>"
  exchange-db-pass: "<Password used to connect>"
  exchange-db-ssl: "<disable|require|verify-full>"
  # Ensure proper indentation (four spaces)
  exchange-db-cert: |-
    -----BEGIN CERTIFICATE-----
    ....
    -----END CERTIFICATE-----

  # css mongodb connection settings
  css-db-host: "<Comma separated list including ports: hostname.domain:port,hostname2.domain:port2 >"
  css-db-name: "<The name of the database to utilize on the mongodb instance>"
  css-db-user: "<Username used to connect>"
  css-db-pass: "<Password used to connect>"
  css-db-auth: "<The name of the database used to store user credentials>"
  css-db-ssl: "<true|false>"
  # Ensure proper indentation (four spaces)
  css-db-cert: |-
    -----BEGIN CERTIFICATE-----
    ....
    -----END CERTIFICATE-----
```
{: codeblock}

Create the secret:
```
oc apply -f edge-auth-overrides.yaml
```
{: codeblock}

Watch the operator logs as documented in the [Operator Control Loop](./configuration.md#remote) section.


## Scaling Configuration
{: #scale}

The EamHub Custom Resource Configuration exposes configuration parameters needed to support a higher number of edge 
nodes from the  {{site.data.keyword.ieam}} Management Hub. 
The OpenShift platform will recognize these updates and automatically apply them
the  {{site.data.keyword.ieam}} PODS running under OCP. 

To support 4,0000 edge nodes, no configurations changes are needed.

In order to support 10,000 or higher edge nodes, the following change is required in the EamHub Custom Resource Configuration. 
Add the following section under **spec**:

```
spec:
  exchange_resources:
    requests:
      memory: 512Mi
      cpu: 10m
    limits:
      memory: 2Gi
      cpu: 5
```
{: codeblock}
   
In order for an installation to support greater than 10,000 edge nodes, additional configuration changes are needed other than the **exchange_resources** noted above.

The way to alter the parameters is as follows. (Note: normal spacing rules for YAML is required.)
1. Run `oc get cm ibm-edge-config -o yaml` and extract the entire section for **agbot_config:** including tag **agbot_config:** and the **|** character.
2. Change **AgreementWorkers** to a value of **30**.
3. Change **ProtocolTimeoutS** to a value of **1200**.
4. Paste this configuration block, including the changes, under under **spec**.
5. Next run `oc get cm ibm-edge-config -o yaml` extract the entire section for **exchange_config:** including the tag **exchange_config:** and the **|** character.
6. Add in a **cache** configuration, paste this into the custom resource. It should look like:
```
spec:
  exchange_config: |
    {
      "api": {
        "cache": {
          "idsTtlSeconds": 4000
        },
        "db": {
          "jdbcUrl": "$EDGE_EXCHANGE_DB_URL",
          "maxConnectionAge": 3600,
          "maxIdleTimeExcessConnections": 0,
          "maxPoolSize": "30",
          "password": "$EDGE_EXCHANGE_DB_PASS",
          "user": "$EDGE_EXCHANGE_DB_USER"
        },
        "logging": {
          "level": "INFO"
        },
        "root": {
          "enabled": "true",
          "password": "$EDGE_EXCHANGE_ROOT_PASS"
        }
      }
    }
```
{: codeblock}

## Additional ORG level configuration for high scale environments

Finally, to support high scale environments greater than 10,000 edge nodes, adjust the heartbeat intervals that the edge nodes use to check for changes. 

The following command should be issued by a super user:
```
hzn exchange org update --heartbeatmin=60 --heartbeatmax=900 --heartbeatadjust=60 <org_name>
```
{: codeblock}

If multiple ORGS used, the command should be issued for each ORG supporting more than 10,000 edge nodes.
