---

copyright:
years: 2020 - 2022
lastupdated: "2022-03-17"

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

For a full list of open issues for the {{site.data.keyword.ieam}} OpenSource layer, review the GitHub issues in each of the [Open Horizon repositories](https://github.com/open-horizon/).

{:shortdesc}

## Known issues for {{site.data.keyword.ieam}} {{site.data.keyword.version}}

These are known issues and limitations for {{site.data.keyword.ieam}}.

* [Private image repositories](../developing/container_registry.md) are not supported for service creation in the management console.

* {{site.data.keyword.ieam}} does not perform a malware or virus scan on data that is uploaded to the model management system (MMS). For more information about MMS security, see [Security and privacy](../user_management/security_privacy.md#malware).

* The **-f &lt;directory&gt;** flag of **edgeNodeFiles.sh** does not have the intended effect. Instead, the files are collected in the current directory. For more information, see [issue 2187](https://github.com/open-horizon/anax/issues/2187). The work-around is to run the command like this:

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

* Installation of edge devices with Fedora or SuSE is only supported by the [Advanced manual agent installation and registration](../installing/advanced_man_install.md) method.

For the full list of open issues for the {{site.data.keyword.ieam}} OpenSource layer, review the GitHub issues in each of the [Open Horizon repositories ](https://github.com/open-horizon/){:target="_blank"}{: .externalLink}.
