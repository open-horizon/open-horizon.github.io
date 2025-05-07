---
copyright: Contributors to the Open Horizon project
years: 2021 - 2025
title: Managing Secrets
description: Guide to creating, updating, and managing secrets in Open Horizon
lastupdated: 2025-05-07
nav_order: 1
parent: Secrets Management
grand_parent: Developing edge services
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}

# Managing Secrets
{: #managing_secrets}

This guide covers how to create, update, and manage secrets in Open Horizon using the CLI.

## Creating secrets
{: #creating_secrets}

### Organization-wide secrets
Organization-wide secrets are created by organization administrators and can be used by any service in the organization.  They can be added for all nodes as shown below, or for a specific node.

```bash
hzn secretsmanager secret add --secretKey <key> --secretDetail <value> <secret-name>
```

Example:
```bash
hzn secretsmanager secret add --secretKey "api-key" --secretDetail "abc123" my-api-secret
```

### User private secrets
User private secrets are only accessible to services owned by the creating user or an organization. They follow the naming convention `user/<username>/<secret-name>`.

```bash
hzn secretsmanager secret add --secretKey <key> --secretDetail <value> user/<username>/<secret-name>
```

Example:
```bash
hzn secretsmanager secret add --secretKey "password" --secretDetail "secure123" user/johndoe/db-password
```

### Node-specific secrets
Node-specific secrets are only accessible to services running on a specific node. They follow the naming convention `node/<node-id>/<secret-name>`.

```bash
hzn secretsmanager secret add --secretKey <key> --secretDetail <value> node/<node-id>/<secret-name>
```

Example:
```bash
hzn secretsmanager secret add --secretKey "cert" --secretDetail "cert-data" node/node1/device-cert
```

## Updating secrets
{: #updating_secrets}

Secrets can be updated using the same command as creation. The existing secret will be overwritten.

```bash
hzn secretsmanager secret add --secretKey <new-key> --secretDetail <new-value> <secret-name>
```

When a secret is updated:
1. The new value is stored in the secrets manager
2. The agbot detects the change
3. An agreement update is sent to affected nodes
4. Services receive the new secret value

## Deleting secrets
{: #deleting_secrets}

To remove a secret that is no longer needed:

```bash
hzn secretsmanager secret remove <secret-name>
```

Example:
```bash
hzn secretsmanager secret remove my-api-secret
```

## Listing secrets
{: #listing_secrets}

### List all organization-wide secrets
```bash
hzn secretsmanager secret list
```

### List user private secrets
```bash
hzn secretsmanager secret list user/<username>
```

### List node-specific secrets
```bash
hzn secretsmanager secret list node/<node-id>
```

## Access control
{: #access_control}

### Organization administrators can:
- Create, read, update, and delete organization-wide secrets
- Create, read, update, and delete their own user private secrets
- Delete (but not read) other users' private secrets
- List all secrets in the organization

### Regular users can:
- List organization-wide secrets (but not read their contents)
- Create, read, update, and delete their own user private secrets
- List their own user private secrets

## Best practices
{: #best_practices}

1. **Naming conventions**
   - Use descriptive but non-revealing names
   - Follow the naming patterns for user and node secrets
   - Avoid using special characters in secret names

2. **Secret management**
   - Rotate secrets regularly
   - Use different secrets for different purposes
   - Keep track of which services use which secrets

3. **Security**
   - Never store secrets in service definitions
   - Use appropriate access controls
   - Monitor secret usage and access

4. **Organization**
   - Document secret purposes and owners
   - Maintain a secret inventory
   - Clean up unused secrets

## Troubleshooting
{: #troubleshooting}

Common issues and solutions:

1. **Secret not found**
   - Verify the secret name is correct
   - Check if you have permission to access the secret
   - Ensure the secret exists in the correct scope

2. **Secret update not reflected**
   - Check if the service is properly configured to receive updates
   - Verify the agreement update was received
   - Check service logs for errors

3. **Access denied**
   - Verify your user permissions
   - Check if you're using the correct scope
   - Ensure you're authenticated properly 