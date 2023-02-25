---

copyright:
years: 2020 - 2023
lastupdated: "2022-02-25"
title: "Known issues and limitations"

parent: Release notes
nav_order: 1
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Known issues and limitations
{: #knownissues}

These are known issues and limitations for {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) {{site.data.keyword.version}}.

For a full list of open issues for the {{site.data.keyword.ieam}} open source layer, review the GitHub issues in each of the [Open Horizon repositories ](https://github.com/open-horizon/){:target="_blank"}{: .externalLink}.

{:shortdesc}

## Known issues for {{site.data.keyword.ieam}} {{site.data.keyword.version}}

These are known issues and limitations for {{site.data.keyword.ieam}}.

* [Private image repositories](../developing/container_registry.md) are not supported for service creation in the management console.

* {{site.data.keyword.ieam}} does not perform a malware or virus scan on data that is uploaded to the model management system (MMS). For more information about MMS security, see [Security and privacy](../user_management/security_privacy.md#malware).

* The **-f &lt;directory&gt;** flag of **edgeNodeFiles.sh** does not have the intended effect. Instead, the files are collected in the current directory. For more information, see [issue 2187 ](https://github.com/open-horizon/anax/issues/2187){:target="_blank"}{: .externalLink}. The work-around is to run the command like this:

   ```bash
   (cd <dir> && edgeNodeFiles.sh ... )
   ```
   {: codeblock}

* When you are upgrading from Raspberry Pi OS 10 (buster) or Raspberry Pi OS 11 (bullseye), a previously installed, configured, and running agent might require reinstallation. In some instances, the agent enters a restart loop that reinstallation solves. Run `ps -aux | grep "anax"` several times to observe if the agent PID is incrementing after the upgrade. This indicates whether a loop is encountered after the upgrade.

* When you test a service that uses `hzn dev service start`, a 403 http log error occurs if the dependent service container uses the [Model Management System](../developing/model_management_system.md) (MMS) and if it is in a different organization from the top-level service.

## Limitations for {{site.data.keyword.ieam}} {{site.data.keyword.version}}

* {{site.data.keyword.ieam}} product documentation is translated for participating geographies, but the English version is updated continually. Discrepancies between English and translated versions can appear in between translation cycles. Check the English version to see whether any discrepancies were resolved after the translated versions were published.

* The {{site.data.keyword.ieam}} agent does not support bidirectional communication between service dependencies. A service that is used as a required service cannot communicate with the service (the requiring service) that depends on it. For more information, see [Agent does not support bidirectional comms between service dependencies ](https://github.com/open-horizon/anax/issues/2095){:target="_blank"}{: .externalLink}. To work around this problem, remove the required service and add the required service's containers to the service definition of the requiring service.

* If you change the **owner** or **public** attributes of services, patterns, or deployment policies in the exchange, it can take as long as five minutes to access those resources to view the change. Similarly, when you give an exchange user admin privilege, it can take as long as five minutes for that change to propagate to all of the exchange instances. The length of time can be reduced by setting `api.cache.resourcesTtlSeconds` to a lower value (the default is 300 seconds) in the exchange `config.json` file, at the cost of slightly lower performance.

* The agent does not support the [Model Management System](../developing/model_management_system.md) (MMS) for dependent services.

* The secret binding does not work for an agreement-less service defined in a pattern.
 
* The edge cluster agent does not support K3S v1.21.3+k3s1 because the mounted volume directory only has 0700 permission. See [Cannot write data to local PVC ](https://github.com/k3s-io/k3s/issues/3704){:target="_blank"}{: .externalLink} for a temporary solution.
 
* Each {{site.data.keyword.ieam}} edge node agent initiates all network connections with the {{site.data.keyword.ieam}} management hub. The management hub never initiates connections to its edge nodes. Therefore, an edge node can be behind a NAT firewall if the firewall has TCP connectivity to the management hub. However, edge nodes cannot currently communicate with the management hub through a SOCKS proxy.
  
* Installation of edge devices with {{site.data.keyword.fedora}} or SuSE is only supported by the [Advanced manual agent installation and registration](../installing/advanced_man_install.md) method.
  
* For services built with the operator SDK for deploying Helm charts on edge clusters, make sure that all variables in the templates and Helm charts have assigned values. A good practice is to ensure that all variables have assigned default values in the templates. Variables without assigned values will prevent the application from deploying successfully.

For the full list of open issues for the {{site.data.keyword.ieam}} OpenSource layer, review the GitHub issues in each of the [Open Horizon repositories ](https://github.com/open-horizon/){:target="_blank"}{: .externalLink}.
