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

# Post installation configuration

## Prerequisites

* [IBM Cloud Pak CLI (**cloudctl**) and OpenShift client CLI (**oc**)](../cli/cloudctl_oc_cli.md)
* [**jq** ![Opens in a new tab](../images/icons/launch-glyph.svg "Opens in a new tab")](https://stedolan.github.io/jq/download/)
* [**git** ![Opens in a new tab](../images/icons/launch-glyph.svg "Opens in a new tab")](https://git-scm.com/downloads)
* [**docker** ![Opens in a new tab](../images/icons/launch-glyph.svg "Opens in a new tab")](https://docs.docker.com/get-docker/) version 1.13 or greater
* **make**

## Installation verification

1. Complete the steps in [Install {{site.data.keyword.ieam}}](online_installation.md)
2. Ensure that all pods in the {{site.data.keyword.ieam}} namespace are either **Running** or **Completed**:

   ```
   oc get pods
   ```
   {: codeblock}

   This is an example of what should be seen with local databases installed. Some initialization restarts are expected, multiple restarts usually indicate an issue.:
   ```
   $ oc get pods
   NAME                                           READY   STATUS      RESTARTS   AGE
   create-agbotdb-cluster-j4fnb                   0/1     Completed   0          88m
   create-exchangedb-cluster-hzlxm                0/1     Completed   0          88m
   ibm-common-service-operator-68b46458dc-nv2mn   1/1     Running     0          103m
   ibm-eamhub-operator-7bf99c5fc8-7xdts           1/1     Running     0          103m
   ibm-edge-agbot-5546dfd7f4-4prgr                1/1     Running     0          81m
   ibm-edge-agbot-5546dfd7f4-sck6h                1/1     Running     0          81m
   ibm-edge-agbotdb-keeper-0                      1/1     Running     0          88m
   ibm-edge-agbotdb-keeper-1                      1/1     Running     0          87m
   ibm-edge-agbotdb-keeper-2                      1/1     Running     0          86m
   ibm-edge-agbotdb-proxy-7447f6658f-7wvdh        1/1     Running     0          88m
   ibm-edge-agbotdb-proxy-7447f6658f-8r56d        1/1     Running     0          88m
   ibm-edge-agbotdb-proxy-7447f6658f-g4hls        1/1     Running     0          88m
   ibm-edge-agbotdb-sentinel-5766f666f4-5qm9x     1/1     Running     0          88m
   ibm-edge-agbotdb-sentinel-5766f666f4-5whgr     1/1     Running     0          88m
   ibm-edge-agbotdb-sentinel-5766f666f4-9xjpr     1/1     Running     0          88m
   ibm-edge-css-5c59c9d6b6-kqfnn                  1/1     Running     0          81m
   ibm-edge-css-5c59c9d6b6-sp84w                  1/1     Running     0          81m
   ibm-edge-css-5c59c9d6b6-wf84s                  1/1     Running     0          81m
   ibm-edge-cssdb-server-0                        1/1     Running     0          88m
   ibm-edge-exchange-b6647db8d-k97r8              1/1     Running     0          81m
   ibm-edge-exchange-b6647db8d-kkcvs              1/1     Running     0          81m
   ibm-edge-exchange-b6647db8d-q5ttc              1/1     Running     0          81m
   ibm-edge-exchangedb-keeper-0                   1/1     Running     1          88m
   ibm-edge-exchangedb-keeper-1                   1/1     Running     0          85m
   ibm-edge-exchangedb-keeper-2                   1/1     Running     0          84m
   ibm-edge-exchangedb-proxy-6bbd5b485-cx2v8      1/1     Running     0          88m
   ibm-edge-exchangedb-proxy-6bbd5b485-hs27d      1/1     Running     0          88m
   ibm-edge-exchangedb-proxy-6bbd5b485-htldr      1/1     Running     0          88m
   ibm-edge-exchangedb-sentinel-6d685bf96-hz59z   1/1     Running     1          88m
   ibm-edge-exchangedb-sentinel-6d685bf96-m4bdh   1/1     Running     0          88m
   ibm-edge-exchangedb-sentinel-6d685bf96-mxv2b   1/1     Running     1          88m
   ibm-edge-sdo-0                                 1/1     Running     0          81m
   ibm-edge-ui-545d694f6c-4rnrf                   1/1     Running     0          81m
   ibm-edge-ui-545d694f6c-97ptz                   1/1     Running     0          81m
   ibm-edge-ui-545d694f6c-f7bf6                   1/1     Running     0          81m
   ```
   {: codeblock}

   Notes:
   * For more information about any pods in the **Pending** state due to resource or scheduling issues, see the [cluster sizing](cluster_sizing.md) page. This includes information about how to reduce scheduling costs of components.
   * For more information about any other errors, see [troubleshooting](../admin/troubleshooting.md).
3. Ensure that all pods in the **ibm-common-services** namespace are either **Running** or **Completed**:

   ```
   oc get pods -n ibm-common-services
   ```
   {: codeblock}

4. [Download the agent package from IBM Passport Advantage](part_numbers.md) to your installation environment and unpack the installation media:
    ```
    tar -zxvf ibm-eam-{{site.data.keyword.semver}}-agent-x86_64.tar.gz && \
    cd ibm-eam-{{site.data.keyword.semver}}-agent-x86_64/tools
    ```
    {: codeblock}
5. Validate the installation state:
    ```
    ./service_healthcheck.sh
    ```
    {: codeblock}

    See the following example output:
    ```
    $ ./service_healthcheck.sh
    ==Running service verification tests for IBM Edge Application Manager==
    SUCCESS: IBM Edge Application Manager Exchange API is operational
    SUCCESS: IBM Edge Application Manager Cloud Sync Service is operational
    SUCCESS: IBM Edge Application Manager Agbot database heartbeat is current
    SUCCESS: IBM Edge Application Manager SDO API is operational
    SUCCESS: IBM Edge Application Manager UI is properly requiring valid authentication
    ==All expected services are up and running==
    ```

   * If there are **service_healthcheck.sh** command failures, if you experience issues running the commands below, or if there are issues during runtime, see [troubleshooting](../admin/troubleshooting.md).


## Post installation configuration
{: #postconfig}

The following process must run on a host that supports installation of the **hzn** CLI, which currently can be installed on a Debian/apt based Linux, amd64 Red Hat/rpm Linux, or macOS host. These steps use the same media downloaded from PPA in the Installation verification section.

1. Install the **hzn** CLI using the instructions for your supported platform:
  * Navigate to the **agent** directory and unpack the agent files:
    ```
    cd ibm-eam-{{site.data.keyword.semver}}-agent-x86_64/agent && \
    tar -zxvf edge-packages-{{site.data.keyword.semver}}.tar.gz
    ```
    {: codeblock}

    * Debian {{site.data.keyword.linux_notm}} example:
      ```
      sudo apt-get install ./edge-packages-{{site.data.keyword.semver}}/linux/deb/amd64/horizon-cli*.deb
      ```
      {: codeblock}

    * Red Hat {{site.data.keyword.linux_notm}} example:
      ```
      sudo dnf install -yq ./edge-packages-{{site.data.keyword.semver}}/linux/rpm/x86_64/horizon-cli-*.x86_64.rpm
      ```
      {: codeblock}

    * macOS example:
      ```
      sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain edge-packages-{{site.data.keyword.semver}}/macos/pkg/x86_64/horizon-cli.crt && \
      sudo installer -pkg edge-packages-{{site.data.keyword.semver}}/macos/pkg/x86_64/horizon-cli-*.pkg -target /
      ```
      {: codeblock}

2. Run the post installation script. This script performs all the necessary initialization to create your first organization. (Organizations are how {{site.data.keyword.ieam}} separates resources and users to enable multi-tenancy. Initially, this first organization is sufficient. You can configure more organizations later. For more information, see [Multi-tenancy ![Opens in a new tab](../images/icons/launch-glyph.svg "Opens in a new tab")](../admin/multi_tenancy.md)).

   **Note:** **ibm** and **root** are internal use orgs and can not be chosen as your initial org.

   ```
   ./post_install.sh <choose-your-org-name>
   ```
   {: codeblock}

3. Run the following to print the {{site.data.keyword.ieam}} {{site.data.keyword.ieam}} management console link for your installation:
   ```
   echo https://$(oc get cm management-ingress-ibmcloud-cluster-info -o jsonpath='{.data.cluster_ca_domain}')/edge
   ```
   {: codeblock}

## LDAP and API keys

If not previously configured, create an LDAP connection by using the {{site.data.keyword.open_shift_cp}} management console. After you establish an LDAP connection, create a team, grant that team access to the namespace the {{site.data.keyword.edge_notm}} operator was deployed to, and add users to that team. This grants individual users the permission to create API keys.

**Note:** API-keys are used for authentication with the {{site.data.keyword.edge_notm}} CLI and permissions that are associated with API keys are identical to the user they are generated with. For more information about LDAP, see [Configuring LDAP connection ![Opens in a new tab](../images/icons/launch-glyph.svg "Opens in a new tab")](https://www.ibm.com/support/knowledgecenter/SSHKN6/iam/3.x.x/configure_ldap.html).

## What's Next

After completing the steps in [Post installation configuration](#postconfig), follow the process on the [Gather edge node files](gather_files.md) page to prepare installation media for your edge nodes.
