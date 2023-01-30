---

copyright:
years: 2021 - 2022
lastupdated: "2022-03-10"
title: "Secrets Manager details"

parent: Further reading for devices
nav_order: 4
---

{:shortdesc: .shortdesc}
{:new_window: target="_blank"}
{:codeblock: .codeblock}
{:pre: .pre}
{:screen: .screen}
{:tip: .tip}
{:download: .download}

# Developing a service using secrets
{: #using secrets}

<img src="../../images/edge/10_Secrets.svg" style="margin: 3%" alt="Developing a service using secrets">

# Secrets Manager details
{: #secrets_details}

The Secrets Manager provides secure storage for sensitive information like authentication credentials or encryption keys. These secrets are securely deployed by {{site.data.keyword.ieam}} so that only the services configured to receive a secret will have access to it. The [Hello Secret World Example](https://github.com/open-horizon/examples/blob/master/edge/services/helloSecretWorld/CreateService.md) provides an overview of how to exploit secrets in an edge service.

{{site.data.keyword.ieam}} supports the use of [Hashicorp Vault](https://www.vaultproject.io/) as the Secrets Manager. Secrets created using the hzn CLI are mapped to Vault secrets using the [KV V2 Secrets Engine](https://www.vaultproject.io/docs/secrets/kv/kv-v2). This means that the details of every {{site.data.keyword.ieam}} secret are composed of a key and a value. Both are stored as part of the details of the secret, and both can be set to any string value. A common usage of this feature is to provide the type of secret on the key and sensitive information as the value. For example, set the key to "basicauth" and set the value to "user:password". In so doing, the service developer can interrogate the type of secret, enabling the service code to handle the value correctly.

The names of secrets in the Secrets Manager are never known by a service implementation. It is not possible to convey information from the vault to a service implementation using the name of a secret.

Secrets are stored in the KV V2 Secrets Engine by prefixing the secret name with openhorizon and the user's organization. This ensures that secrets created by {{site.data.keyword.ieam}} users are isolated from other uses of the Vault by other integrations, and it ensures that multi-tenant isolation is maintained.

Secret names are managed by {{site.data.keyword.ieam}} org admins (or users when using user private secrets). Vault Access Control Lists (ACLs) control which secrets an {{site.data.keyword.ieam}} user is able to manage. This is accomplished through a Vault authentication plugin that delegates user authentication to the {{site.data.keyword.ieam}} exchange. Upon successfully authenticating a user, the authentication plugin in the Vault will create a set of ACL policies specific to this user. A user with admin privileges in the exchange can:
- Add, remove, read and list all organization wide secrets.
- Add, remove, read and list all secrets private to that user.
- Remove and list the user private secrets of other users in the org, but cannot add or read those secrets.

A user without admin privileges can:
- List all organization wide secrets, but cannot add, remove or read them.
- Add, remove, read and list all secrets private to that user.

The {{site.data.keyword.ieam}} {{site.data.keyword.agbot}} also has access to secrets in order to be able to deploy them to edge nodes. The {{site.data.keyword.agbot}} maintains a renewable login to the Vault and is given ACL policies specific to its purposes. An {{site.data.keyword.agbot}} can:
- Read org wide secrets and any user private secret in any org, but it cannot add, remove or list any secrets.

The Exchange root user and Exchange hub admins have no permissions in the Vault. See [Role-Based Access Control](../../user_management/rbac) for more info on these roles.
