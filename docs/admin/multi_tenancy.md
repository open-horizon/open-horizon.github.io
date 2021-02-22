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

# Multi-tenancy
{: #multit}

## Tenants in {{site.data.keyword.edge_notm}}
{: #tenants}

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) supports the general IT concept of multi-tenancy through organizations, where each tenant has their own organization. Organizations separate resources; therefore, users within each organization cannot create or modify resources in a different organization. Furthermore, resources in an organization can be viewed only by users in that organization, unless the resources are marked as public.

### Common use cases

Two broad use cases are used to leverage multi-tenancy in {{site.data.keyword.ieam}}:

* An enterprise has multiple business units, where each business unit is a separate organization in the same {{site.data.keyword.ieam}} management hub. Consider the legal, business, or technical reasons why each business unit ought to be a separate organization with its own set of {{site.data.keyword.ieam}} resources which are by default not accessible by the other business units. Note that even with separate organizations, the enterprise still has the option to use a common group of organization administrators to manage all of the organizations.
* An enterprise hosts {{site.data.keyword.ieam}} as a service for its customers, where each of their customers has one or more organizations in the management hub. In this case, the organization administrators are unique to each customer.

The use case you choose determines how you configure {{site.data.keyword.ieam}} and Identity and Access Manager ([IAM](https://www.ibm.com/support/knowledgecenter/SSHKN6/iam/landing_iam.html)).

### Types of {{site.data.keyword.ieam}} users
{: #user-types}

{{site.data.keyword.ieam}} supports these user roles:

| **Role** | **Access** |
|--------------|-----------------|
| **Hub admin** | Manages the list of {{site.data.keyword.ieam}} organizations by creating, modifying, and deleting organizations as necessary, and by creating organization admins within each organization. |
| **Organization admin** | Manages the resources in one or more {{site.data.keyword.ieam}} organizations. Organization admins can create, view, or modify any resource (user, node, service, policy, or pattern) within the organization, even if they are not the owner of the resource. |
| **Regular user** | Creates nodes, services, policies, and patterns within the organization and modifies or deletes the resources that they have created. Views all of the services, policies, and patterns in the organization that other users have created. |
{: caption="Table 1. {{site.data.keyword.ieam}} user roles" caption-side="top"}

See [Role-based access control](../user_management/rbac.md) for a description of all {{site.data.keyword.ieam}} roles.

## The relationship between IAM and {{site.data.keyword.ieam}}
{: #iam-to-ieam}

The IAM (Identity and Access Manager) service manages users for all Cloud Pak based products, including {{site.data.keyword.ieam}}. IAM in turn uses LDAP to store the users. Each IAM user can be a member of one or more IAM teams. Because each IAM team is associated with an IAM account, an IAM user can indirectly be a member of one or more IAM accounts. See [IAM multi-tenancy](https://www.ibm.com/support/knowledgecenter/SSHKN6/iam/3.x.x/multitenancy/multitenancy.html) for details.

The {{site.data.keyword.ieam}} exchange provides authentication and authorization services for the other {{site.data.keyword.ieam}} components. The exchange delegates the authentication of users to IAM, which means IAM user credentials are passed to the exchange and it relies on IAM to determine if they are valid. Each user role (hub admin, organization admin, or regular user) is defined in the exchange, and that determines the actions that users are allowed to perform in {{site.data.keyword.ieam}}.

Each organization in the {{site.data.keyword.ieam}} exchange is associated with an IAM account. Therefore IAM users in an IAM account are automatically members of the corresponding {{site.data.keyword.ieam}} organization. The one exception to this rule is that the {{site.data.keyword.ieam}} hub admin role is considered to be outside of any specific organization; therefore, it does not matter what IAM account the hub admin IAM user is in.

To summarize the mapping between IAM and {{site.data.keyword.ieam}}:

| **IAM** | **Relationship** | **{{site.data.keyword.ieam}}** |
|--------------|----------|-----------------|
| IAM Account | maps to | {{site.data.keyword.ieam}} Organization |
| IAM User | maps to | {{site.data.keyword.ieam}} User |
| There is no IAM counterpart for role | none | {{site.data.keyword.ieam}} role |
{: caption="Table 2. IAM - {{site.data.keyword.ieam}} mapping" caption-side="top"}

The credentials used to log in to the {{site.data.keyword.ieam}} console are the IAM user and password. The credentials used for the {{site.data.keyword.ieam}} CLI (`hzn`) is an IAM API key.

## The initial organization
{: #initial-org}

By default, an organization was created during {{site.data.keyword.ieam}} installation with a name that you provided. If you do not need the multi-tenant capabilities of {{site.data.keyword.ieam}}, this initial organization is sufficient for your use of {{site.data.keyword.ieam}}, and you can skip the rest of this page.

## Creating a hub admin user
{: #create-hub-admin}

The first step of using {{site.data.keyword.ieam}} multi-tenancy is to create one or more hub admins that can create and manage the organizations. Before you can do this, you must create or choose an IAM account and user that will have the hub admin role assigned to it.

1. Use `cloudctl` to log in to the {{site.data.keyword.ieam}} management hub as the cluster administrator. (If you have not already installed `cloudctl`, see [Installing cloudctl, kubectl, and oc](../cli/cloudctl_oc_cli.md) for instructions.)

   ```bash
   cloudctl login -a <cluster-url> -u admin -p <password> --skip-ssl-validation
   ```
   {: codeblock}

2. If you have not already connected an LDAP instance to IAM, do so now by following [Connecting to your LDAP directory](https://www.ibm.com/support/knowledgecenter/SSHKN6/iam/3.x.x/configure_ldap.html).

3. The hub admin user must be in an IAM account. (It does not matter which account.) If you do not already have an IAM account you want the hub admin user to be in, create one:

   ```bash
   IAM_ACCOUNT_NAME='hub admin account'   # or choose another name
   cloudctl iam account-create "$IAM_ACCOUNT_NAME" -d 'account for the hub admin users'
   IAM_ACCOUNT_ID=$(cloudctl iam account "$IAM_ACCOUNT_NAME" | grep -E '^ID' | awk '{print $2}')
   IAM_TEAM_ID=$(cloudctl iam teams -s | grep -m 1 "$IAM_ACCOUNT_NAME" | awk '{print $1}')
   ```
   {: codeblock}

4. Create or choose an LDAP user that will be dedicated to the {{site.data.keyword.ieam}} hub admin role. **Note:** Do not use the same user as both an {{site.data.keyword.ieam}} hub admin and an {{site.data.keyword.ieam}} organization admin (or regular {{site.data.keyword.ieam}} user).

5. Import the user to IAM:

   ```bash
   HUB_ADMIN_USER=<the IAM/LDAP user name of the hub admin user>
   cloudctl iam user-import -u $HUB_ADMIN_USER
   cloudctl iam user-onboard $IAM_ACCOUNT_ID -r PRIMARY_OWNER -u $HUB_ADMIN_USER
   IAM_RESOURCE_ID=$(cloudctl iam resources | grep ':n/ibm-edge:')
   cloudctl iam resource-add $IAM_TEAM_ID -r $IAM_RESOURCE_ID
   ```
   {: codeblock}

6. Assign the hub admin role to the IAM user:

   ```bash
   EXCHANGE_ROOT_PW=<password for the exchange root user>
   export HZN_ORG_ID=root
   export HZN_EXCHANGE_USER_AUTH=root/root:$EXCHANGE_ROOT_PW
   export HZN_EXCHANGE_URL=<the URL of your exchange>
   curl -sS -w %{http_code} -u "$HZN_EXCHANGE_USER_AUTH" -X POST -H Content-Type:application/json -d '{"hubAdmin":true,"password":"","email":""}' $HZN_EXCHANGE_URL/orgs/root/users/$HUB_ADMIN_USER | jq
   ```
   {: codeblock}

   **Note:** If the `curl` command fails because the user already exists, run the same command except with `-X PUT`.

7. Verify that the user has the hub admin user role. In the output of the following command, you should see `"hubAdmin": true` .

   ```bash
   hzn exchange user list $HUB_ADMIN_USER
   ```
   {: codeblock}

### Use the hub admin user with the {{site.data.keyword.ieam}} CLI
{: #verify-hub-admin}

Create an API key for the hub admin user and verify it has the hub admin capabilities:

1. Use `cloudctl` to log in to the {{site.data.keyword.ieam}} management hub as the hub admin:

   ```bash
   cloudctl login -a <cluster-url> -u $HUB_ADMIN_USER -p <hub-admin-password> -c $IAM_ACCOUNT_ID --skip-ssl-validation
   ```
   {: codeblock}

2. Create an API key for the hub admin user:

   ```bash
   cloudctl iam api-key-create "${HUB_ADMIN_USER}-api-key" -d "API key for $HUB_ADMIN_USER"
   ```
   {: codeblock}

   Find the API key value in the command output line that starts with **API Key**. Save the key value in a safe location for future use because you cannot query it from the system later. Also, set it in this variable for the subsequent commands:

   ```bash
   HUB_ADMIN_API_KEY=<IAM API key you just created>
   ```
   {: codeblock}

3. Display all the organizations in the management hub. You should see the initial organization that is created during installation, as well as the **root** and **IBM** organizations:

   ```bash
   export HZN_ORG_ID=root
   export HZN_EXCHANGE_USER_AUTH=root/iamapikey:$HUB_ADMIN_API_KEY
   hzn exchange org list -o root
   ```
   {: codeblock}

4. Log in to the [{{site.data.keyword.ieam}} management console](../console/accessing_ui.md) with your hub admin IAM user and password. The organization administration console will be displayed because your login credentials have the hub admin role. Use this console to view, manage, and add organizations. Or, if you prefer, you can add organizations using the CLI in the following section.

## Creating an organization using the CLI
{: #create-org}

Organizations can be created using the CLI, as an alternative to using the {{site.data.keyword.ieam}} organization administration console. A prerequisite to creating an organization is to create or choose an IAM account that will be associated with the organization. Another prerequisite is to create or choose an IAM user that will be assigned the organization admin role.

Perform these steps:

1. If you have not already done so, create a hub admin user by performing the steps in the previous section. Ensure that the hub admin API key is set in the following variable:

   ```bash
   HUB_ADMIN_API_KEY=<IAM API key of the hub admin user>
   ```
   {: codeblock}

2. Use `cloudctl` to log in to the {{site.data.keyword.ieam}} management hub as the cluster administrator and create an IAM account that the new {{site.data.keyword.ieam}} organization will be associated with. (If you have not already installed `cloudctl`, see [Installing cloudctl, kubectl, and oc](../cli/cloudctl_oc_cli.md).)

   ```bash
   cloudctl login -a <cluster-url> -u admin -p <password> --skip-ssl-validation
   NEW_ORG_ID=<new organization name>
   IAM_ACCOUNT_NAME="$NEW_ORG_ID"
   cloudctl iam account-create "$IAM_ACCOUNT_NAME" -d "$IAM_ACCOUNT_NAME account"
   IAM_ACCOUNT_ID=$(cloudctl iam account "$IAM_ACCOUNT_NAME" | grep -E '^ID' | awk '{print $2}')
   IAM_TEAM_ID=$(cloudctl iam teams -s | grep -m 1 "$IAM_ACCOUNT_NAME" | awk '{print $1}')
   ```
   {: codeblock}

3. Create or choose an LDAP user that will be assigned the organization admin role and import it to IAM. **Note:** You cannot use a hub admin user as an organization admin user. But you can use the same organization admin user in more than one IAM account, and therefore allow them to manage more than one {{site.data.keyword.ieam}} organization.

   ```bash
   ORG_ADMIN_USER=<the IAM/LDAP user name of the organization admin user>
   cloudctl iam user-import -u $ORG_ADMIN_USER
   cloudctl iam user-onboard $IAM_ACCOUNT_ID -r PRIMARY_OWNER -u $ORG_ADMIN_USER
   IAM_RESOURCE_ID=$(cloudctl iam resources | grep ':n/ibm-edge:')
   cloudctl iam resource-add $IAM_TEAM_ID -r $IAM_RESOURCE_ID
   ```
   {: codeblock}

4. Set these environment variables, create the {{site.data.keyword.ieam}} organization, and verify that it exists:
   ```bash
   export HZN_ORG_ID=root
   export HZN_EXCHANGE_USER_AUTH=root/iamapikey:$HUB_ADMIN_API_KEY
   export HZN_EXCHANGE_URL=<URL of your exchange>
   hzn exchange org create -a IBM/agbot -t "cloud_id=$IAM_ACCOUNT_ID" --description "$NEW_ORG_ID organization" $NEW_ORG_ID
   hzn exchange agbot addpattern IBM/agbot IBM '*' $NEW_ORG_ID
   hzn exchange org list $NEW_ORG_ID
   ```
   {: codeblock}

5. Assign the organization admin user role to the IAM user you previously chose and verify the user was created in the {{site.data.keyword.ieam}} exchange with the organization admin role:

   ```bash
   hzn exchange user create -o $NEW_ORG_ID -A $ORG_ADMIN_USER "" "<email-address>"
   hzn exchange user list -o $NEW_ORG_ID $ORG_ADMIN_USER
   ```
   {: codeblock}

   In the listing of the user, you should see: `"admin": true`

**Note:** If you create multiple organizations and want the same organization admin to manage all of the organizations, use the same value for `ORG_ADMIN_USER` each time through this section.

The organization admin can now use the [{{site.data.keyword.ieam}} management console](../console/accessing_ui.md) to manage {{site.data.keyword.ieam}} resources within this organization.

### Enabling the organization admin to use the CLI

In order for an organization admin to use the `hzn exchange` command to manage {{site.data.keyword.ieam}} resources using the CLI, they must:

1. Use `cloudctl` to log in to the {{site.data.keyword.ieam}} management hub and create an API key:

   ```bash
   cloudctl login -a <cluster-url> -u $ORG_ADMIN_USER -p <hub-admin-password> -c $IAM_ACCOUNT_ID --skip-ssl-validation
   cloudctl iam api-key-create "${ORG_ADMIN_USER}-api-key" -d "API key for $ORG_ADMIN_USER"
   ```
   {: codeblock}

   Find the API key value in the command output line that starts with **API Key**. Save the key value in a safe location for future use because you cannot query it from the system later. Also, set it in this variable for the subsequent commands:

   ```bash
   ORG_ADMIN_API_KEY=<IAM API key you just created>
   ```
   {: codeblock}

   **Tip:** If you add this user to additional IAM accounts in the future, you do not need to create an API key for each account. The same API key will work in all IAM accounts this user is a member of, and therefore in all {{site.data.keyword.ieam}} organizations this user is a member of.

2. Verify the API key works with the `hzn exchange` command:

   ```bash
   export HZN_ORG_ID=<organization id>
   export HZN_EXCHANGE_USER_AUTH=root/iamapikey:$ORG_ADMIN_API_KEY
   hzn exchange user list
   ```
   {: codeblock}


The new organization is ready to use. To set a maximum number of edge nodes in this organization, or customize the default edge node heartbeat settings, see [Organization Configuration](#org-config).

## Non-admin users within an organization
{: #org-users}

A new user can be added to an organization by importing and onboarding the IAM user (as a `MEMBER`) to the corresponding IAM account. You do not need to explicitly add the user to the {{site.data.keyword.ieam}} exchange, because that occurs automatically when necessary.

The user can then use the [{{site.data.keyword.ieam}} management console](../console/accessing_ui.md). In order for the user to use the `hzn exchange` CLI, they must:

1. Use `cloudctl` to log in to the {{site.data.keyword.ieam}} management hub and create an API key:

   ```bash
   IAM_USER=<iam user>
   cloudctl login -a <cluster-url> -u $IAM_USER -p <hub-admin-password> -c $IAM_ACCOUNT_ID --skip-ssl-validation
   cloudctl iam api-key-create "${IAM_USER}-api-key" -d "API key for $IAM_USER"
   ```
   {: codeblock}

   Find the API key value in the command output line that starts with **API Key**. Save the key value in a safe location for future use because you cannot query it from the system later. Also, set it in this variable for the subsequent commands:

   ```bash
   IAM_USER_API_KEY=<IAM API key you just created>
   ```
   {: codeblock}

3. Set these environment variables and verify the user:

```bash
export HZN_ORG_ID=<organization-id>
export HZN_EXCHANGE_USER_AUTH=iamapikey:$IAM_USER_API_KEY
hzn exchange user list
```
{: codeblock}

## The IBM organization
{: #ibm-org}

The IBM organization is a unique organization that provides predefined services and patterns that are intended to be technology examples that are usable by any user in any organization. The IBM organization is automatically created when the {{site.data.keyword.ieam}} management hub is installed.

**Note:** Although the resources in the IBM organization are public, the IBM organization is not intended to hold all public content in the {{site.data.keyword.ieam}} management hub.

## Organization Configuration
{: #org-config}

Every {{site.data.keyword.ieam}} organization has the following settings. The default values for these settings are often sufficient. If you choose to customize any of the settings, run the command `hzn exchange org update -h` to see the command flags that can be used.

| **Setting** | **Description** |
|--------------|-----------------|
| `description` | A description of the organization. |
| `label` | The name of the organization. This value is used to display the organization name in the {{site.data.keyword.ieam}} management console. |
| `heartbeatIntervals` | How often edge node agents in the organization poll the management hub for instructions. See the following section for details. |
| `limits` | Limits for this organization. Currently the only limit is `maxNodes`, which is the maximum number of edge nodes allowed in this organization. There is a practical limit to the total number of edge nodes that a single {{site.data.keyword.ieam}} management hub can support. This setting enables the hub admin user to limit the number of nodes that each organization can have, which prevents one organization from using all of the capacity. A value of `0` means no limit. |
{: caption="Table 3. Organization settings" caption-side="top"}

### Agent heartbeat polling interval
{: #agent-hb}

The {{site.data.keyword.ieam}} agent that is installed on every edge node periodically heartbeats to the management hub to let the management hub know it is still running and connected, and to receive instructions. You only need to change these settings for exceedingly high scale environments.

The heartbeat interval is the amount of time the agent waits between heartbeats to the management hub. The interval is adjusted automatically over time to optimize responsiveness and reduce the load on the management hub. The interval adjustment is controlled by three settings:

| **Setting** | **Description**|
|-------------|----------------|
| `minInterval` | The shortest amount of time (in seconds) the agent should wait between heartbeats to the management hub. When an agent is registered, it starts polling at this interval. The interval will never be less than this value. A value of `0` means use the default value. |
| `maxInterval` | The longest amount of time (in seconds) the agent should wait between heartbeats to the management hub. A value of `0` means use the default value. |
| `intervalAdjustment` | The number of seconds to add to the current heartbeat interval when the agent detects that it can increase the interval. After successfully heartbeating to the management hub, but receiving no instructions for some time, the heartbeat interval is gradually increased until it reaches the maximum heartbeat interval. Likewise, when instructions are received, the heartbeat interval is decreased to ensure that subsequent instructions are processed quickly. A value of `0` means use the default value. |
{: caption="Table 4. heartbeatIntervals settings" caption-side="top"}

The heartbeat polling interval settings in the organization are applied to nodes that have not explicitly configured the heartbeat interval. To check whether a node has explicitly set the heartbeat interval setting, use `hzn exchange node list <node id>`.

For more information about configuring settings in high-scale environments, see [Scaling Configuration](../hub/configuration.md#scale).
