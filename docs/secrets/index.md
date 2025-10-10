---
copyright: Contributors to the Open Horizon project
years: 2021 - 2025
title: Secrets Management
description: Comprehensive guide to managing secrets in Open Horizon
lastupdated: 2025-10-10
nav_order: 1
parent: Developing edge services
has_children: True
has_toc: True
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Secrets Management in Open Horizon
{: #secrets_management}

Open Horizon provides a secure mechanism for managing sensitive information like authentication credentials, certificates, and encryption keys. This documentation guides you through all aspects of secrets management in Open Horizon.

## What are secrets?
{: #what_are_secrets}

Secrets are sensitive pieces of information that your edge services need to function properly. They can be:
- Authentication credentials (usernames and passwords)
- API keys
- Certificates
- Encryption keys
- Any other sensitive data

## Why use secrets management?
{: #why_secrets_management}

Secrets managent in Open Horizon provides several key benefits:
- **Security**: Secrets are stored securely and only accessible to authorized services
- **Flexibility**: Secrets can be updated without redeploying services
- **Organization**: Secrets can be managed at organization or user level
- **Node-specific**: Secrets can be specific to individual nodes
- **Audit**: All secret operations are tracked and logged

## Basic concepts
{: #basic_concepts}

### Secrets Manager
The Secrets Manager is a component of Open Horizon that securely stores and manages secrets. Compatible secrets backend providers include OpenBao and HashiCorp Vault.

### Secret types
- **Organization-wide secrets**: Accessible to all services and nodes in an organization
- **User private secrets**: Only accessible to services and nodes owned by a specific user
- **Node-specific user private secrets**: Specific to individual edge nodes registered to a specific user
- **Node-specific organization-wide secrets**: Specific to individual edge nodes in an organization

### Secret lifecycle
1. Creation: Secrets are created by organization admins or users
2. Binding: Secrets are bound to services in deployment patterns or policies
3. Deployment: Secrets are securely deployed to edge nodes
4. Usage: Services access secrets through [mounted files](https://github.com/open-horizon/examples/blob/master/edge/services/helloSecretWorld/CreateService.md#using-secrets-in-the-service-code)
5. Updates: Secrets can be updated without service redeployment
6. Deletion: Secrets can be removed when no longer needed

### Format of secret in a service
- **json**: Mounted in service as a json file with a key and value. This is the default.
- **value only**: Mounted in service in a file with only the value if `format:value_only` is used in service definition.

## Quick start
{: #quick_start}

To get started with secrets management:

1. Create a secret:
   ```bash
   hzn secretsmanager secret add --secretKey <key> --secretDetail <value> <secret-name>
   ```

2. Add the secret to your service definition:
   ```json
   "secrets": {
     "my_secret": { "description": "My secret description" }
   }
   ```

3. Bind the secret in your deployment pattern or policy:
   ```json
   "secretBinding": [
     {
       "serviceOrgid": "yourOrg",
       "serviceUrl": "yourService",
       "secrets": [
         {"my_secret": "your-secret-name"}
       ]
     }
   ]
   ```

4. Access the secret in your service:
   ```bash
   cat /open-horizon-secrets/my_secret
   ```

## Next steps
{: #next_steps}

- Learn more about [managing secrets](managing_secrets.md)
- Understand how to [develop services with secrets](developing_with_secrets.md)
- Explore [advanced topics](advanced_topics.md)
- Try the [Hello Secret World example](examples.md) 
