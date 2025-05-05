---
copyright: Contributors to the Open Horizon project
years: 2021 - 2025
title: Developing Services with Secrets
description: Guide to developing services that use secrets in Open Horizon
lastupdated: 2025-05-03
nav_order: 2
parent: Secrets Management
grand_parent: Developing edge services
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}

# Developing Services with Secrets
{: #developing_with_secrets}

This guide explains how to develop services that use secrets in Open Horizon, including how to configure services to use secrets and how to access them in your containerized applications.

## Service definition
{: #service_definition}

To use secrets in your service, you need to declare them in your service definition. The `secrets` field specifies which secrets your service needs and provides descriptions for them.

Example service definition:
```json
{
  "label": "my-service",
  "description": "A service that uses secrets",
  "public": true,
  "documentation": "",
  "url": "my.company.com.services.my-service",
  "version": "1.0.0",
  "arch": "amd64",
  "sharable": "multiple",
  "requiredServices": [],
  "userInput": [],
  "deployment": {
    "services": {
      "my-service": {
        "image": "my-service:1.0.0",
        "secrets": {
          "api_key": { "description": "API key for external service" },
          "db_password": { "description": "Database password" }
        }
      }
    }
  }
}
```

## Secret binding
{: #secret_binding}

Secrets are bound to services in deployment patterns or policies. The `secretBinding` field associates service secret names with actual secrets in the secrets manager.

Example pattern with secret binding:
```json
{
  "label": "My Pattern",
  "description": "Pattern that uses secrets",
  "public": true,
  "services": [
    {
      "serviceUrl": "my.company.com.services.my-service",
      "serviceOrgid": "myOrg",
      "serviceArch": "amd64",
      "serviceVersionRange": "[0.0.0,INFINITY)"
    }
  ],
  "secretBinding": [
    {
      "serviceOrgid": "myOrg",
      "serviceUrl": "my.company.com.services.my-service",
      "serviceArch": "amd64",
      "serviceVersionRange": "[0.0.0,INFINITY)",
      "secrets": [
        {"api_key": "cloud-api-key"},
        {"db_password": "user/johndoe/db-password"}
      ]
    }
  ]
}
```

## Accessing secrets in containers
{: #accessing_secrets}

When a service is deployed, its secrets are mounted as files in the `/open-horizon-secrets` directory. Each secret is stored in a file named after the secret name used in the service definition.

Example of accessing secrets in a container:
```bash
#!/bin/bash

# Read the API key
API_KEY=$(cat /open-horizon-secrets/api_key | jq -r '.value')

# Read the database password
DB_PASSWORD=$(cat /open-horizon-secrets/db_password | jq -r '.value')

# Use the secrets
curl -H "Authorization: Bearer $API_KEY" https://api.example.com
```

The secret files contain JSON with both the key and value:
```json
{
  "key": "api-key",
  "value": "abc123"
}
```

## Handling secret updates
{: #secret_updates}

When a secret is updated in the secrets manager, the file in the container is automatically updated. Your service can detect these changes using the agent's REST API.

Example of checking for secret updates:
```bash
#!/bin/bash

# Function to check for secret updates
check_secret_updates() {
  local secret_name=$1
  local current_hash=$(md5sum /open-horizon-secrets/$secret_name | awk '{print $1}')
  
  # Check if secret has changed
  if [ "$current_hash" != "$(cat /tmp/${secret_name}_hash 2>/dev/null)" ]; then
    echo "Secret $secret_name has been updated"
    echo $current_hash > /tmp/${secret_name}_hash
    return 0
  fi
  return 1
}

# Monitor secrets for changes
while true; do
  if check_secret_updates "api_key"; then
    # Handle API key update
    API_KEY=$(cat /open-horizon-secrets/api_key | jq -r '.value')
    # Restart service or reload configuration
  fi
  
  if check_secret_updates "db_password"; then
    # Handle database password update
    DB_PASSWORD=$(cat /open-horizon-secrets/db_password | jq -r '.value')
    # Update database connection
  fi
  
  sleep 60
done
```

## Best practices
{: #development_best_practices}

1. **Secret handling**
   - Never log secret values
   - Use environment variables for secret paths
   - Implement proper error handling for missing secrets

2. **Security**
   - Validate secret values before use
   - Implement proper access controls
   - Use secure communication channels

3. **Updates**
   - Implement graceful handling of secret updates
   - Test update scenarios thoroughly
   - Maintain backward compatibility

4. **Testing**
   - Test with different secret types
   - Verify update mechanisms
   - Test error scenarios

## Common patterns
{: #common_patterns}

1. **Configuration injection**
   ```bash
   # Read configuration from secrets
   CONFIG=$(cat /open-horizon-secrets/config | jq -r '.value')
   
   # Start service with configuration
   my-service --config "$CONFIG"
   ```

2. **Credential rotation**
   ```bash
   # Check for credential updates
   if check_secret_updates "credentials"; then
     # Reload credentials
     reload_credentials
   fi
   ```

3. **Secure communication**
   ```bash
   # Read certificate from secret
   CERT=$(cat /open-horizon-secrets/cert | jq -r '.value')
   
   # Use certificate for secure communication
   curl --cert "$CERT" https://secure.example.com
   ``` 