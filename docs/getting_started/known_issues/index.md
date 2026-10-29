# Known issues and limitations

These are known issues and limitations for Open Horizon.

For a full list of open issues for the Open Horizon open source layer, review the GitHub issues in each of the [Open Horizon repositories](https://github.com/open-horizon/) .

## Known issues for Open Horizon current release

These are known issues and limitations for Open Horizon.

- Open Horizon does not perform a malware or virus scan on data that is uploaded to the model management system (MMS). For more information about MMS security, see [Security and privacy](https://open-horizon.github.io/docs/user_management/security_privacy/#malware).
- The **-f <directory>** flag of **edgeNodeFiles.sh** does not have the intended effect. Instead, the files are collected in the current directory. For more information, see [issue 2187](https://github.com/open-horizon/anax/issues/2187) . The work-around is to run the command like this:

```
(cd <dir> && edgeNodeFiles.sh ... )
```

- When you are upgrading from Raspberry Pi OS 10 (buster) or Raspberry Pi OS 11 (bullseye), a previously installed, configured, and running agent might require reinstallation. In some instances, the agent enters a restart loop that reinstallation solves. Run `ps -aux | grep "anax"` several times to observe if the agent PID is incrementing after the upgrade. This indicates whether a loop is encountered after the upgrade.
- When you test a service that uses `hzn dev service start`, a 403 http log error occurs if the dependent service container uses the [Model Management System](https://open-horizon.github.io/docs/developing/model_management_system/index.md) (MMS) and if it is in a different organization from the top-level service.

## Limitations for Open Horizon current release

- The Open Horizon agent does not support bidirectional communication between service dependencies. A service that is used as a required service cannot communicate with the service (the requiring service) that depends on it. For more information, see [Agent does not support bidirectional comms between service dependencies](https://github.com/open-horizon/anax/issues/2095) . To work around this problem, remove the required service and add the required service's containers to the service definition of the requiring service.
- If you change the **owner** or **public** attributes of services, patterns, or deployment policies in the exchange, it can take as long as five minutes to access those resources to view the change. Similarly, when you give an exchange user admin privilege, it can take as long as five minutes for that change to propagate to all of the exchange instances. The length of time can be reduced by setting `api.cache.resourcesTtlSeconds` to a lower value (the default is 300 seconds) in the exchange `config.json` file, at the cost of slightly lower performance.
- The agent does not support the [Model Management System](https://open-horizon.github.io/docs/developing/model_management_system/index.md) (MMS) for dependent services.
- The secret binding does not work for an agreement-less service defined in a pattern, because secrets management functionality was added after patterns were no longer recommended for production usage.
- The edge cluster agent does not support K3S v1.21.3+k3s1 because the mounted volume directory only has 0700 permission. See [Cannot write data to local PVC](https://github.com/k3s-io/k3s/issues/3704) for a temporary solution.
- Each Open Horizon edge node agent initiates all network connections with the Open Horizon management hub. The management hub never initiates connections to its edge nodes. Therefore, an edge node can be behind a NAT firewall if the firewall has TCP connectivity to the management hub. However, edge nodes cannot currently communicate with the management hub through a SOCKS proxy.
- For services built with the operator SDK for deploying Helm charts on edge clusters, make sure that all variables in the templates and Helm charts have assigned values. A good practice is to ensure that all variables have assigned default values in the templates. Variables without assigned values will prevent the application from deploying successfully.

For the full list of open issues, see the GitHub issues in each of the [Open Horizon repositories](https://github.com/open-horizon/) .
