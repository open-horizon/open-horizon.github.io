---
copyright: Contributors to the Open Horizon project
years: 2021 - 2025
title: Examples
description: Examples of using secrets in Open Horizon services
lastupdated: 2025-06-03
nav_order: 4
parent: Secrets Management
grand_parent: Developing edge services
---

# Examples {: #examples }

This guide provides practical examples of using secrets in Horizon services, including [the Hello Secret World example](https://github.com/open-horizon/examples/tree/master/edge/services/helloSecretWorld).

## Hello Secret World

The Hello Secret World example demonstrates how to create and use a simple service that uses secrets. This example is a good starting point for understanding secrets management in Open Horizon.

### Prerequisites

1. Install the Open Horizon management hub infrastructure
2. Set up your exchange user credentials
3. Install the Open Horizon agent on your edge device
4. Configure your environment variables
5. Unregister your node (if previously registered)

### Step 1: Create a secret

Create an organization-wide secret:
```bash
hzn secretsmanager secret add --secretKey "greeting" --secretDetail "Hello World" hw-secret-name
```

### Step 2: Register with the pattern

Register your edge node with the hello-secret pattern:
```bash
hzn register -p IBM/pattern-ibm.hello-secret -s ibm.hello-secret --serviceorg IBM
```

### Step 3: Monitor the service

View the service output:
```bash
hzn service log -f ibm.hello-secret
```

The output looks like this:
```
Hello World says: Hello World!
```

### Step 4: Update the secret

Update the secret value:
```bash
hzn secretsmanager secret add --secretKey "greeting" --secretDetail "Hello Open Horizon" hw-secret-name
```

After some time, the output changes to:
```
Hello Open Horizon says: Hello Open Horizon!
```

### Step 5: Clean up

Unregister your node:
```bash
hzn unregister -f
```

## Real-world examples

Here are three example code snippets demonstrating how to use secrets for common activities.

### API Authentication

Example service that uses an API key from a secret:
```json
{
  "services": {
    "api-service": {
      "image": "api-service:1.0.0",
      "secrets": {
        "api_key": { "description": "API key for external service" }
      }
    }
  }
}
```

Access the API key in the service:
```bash
#!/bin/bash

# Read the API key
API_KEY=$(cat /open-horizon-secrets/api_key | jq -r '.value')

# Use the API key
curl -H "Authorization: Bearer $API_KEY" https://api.example.com/data
```

### Database Connection

Example service that uses database credentials:
```json
{
  "services": {
    "db-service": {
      "image": "db-service:1.0.0",
      "secrets": {
        "db_user": { "description": "Database username" },
        "db_password": { "description": "Database password" }
      }
    }
  }
}
```

Connect to the database:
```bash
#!/bin/bash

# Read credentials
DB_USER=$(cat /open-horizon-secrets/db_user | jq -r '.value')
DB_PASSWORD=$(cat /open-horizon-secrets/db_password | jq -r '.value')

# Connect to database
mysql -u "$DB_USER" -p"$DB_PASSWORD" -h db.example.com
```

### Certificate-based Authentication

Example service that uses SSL certificates:
```json
{
  "services": {
    "secure-service": {
      "image": "secure-service:1.0.0",
      "secrets": {
        "ssl_cert": { "description": "SSL certificate" },
        "ssl_key": { "description": "SSL private key" }
      }
    }
  }
}
```

Use the certificates:
```bash
#!/bin/bash

# Read certificates
SSL_CERT=$(cat /open-horizon-secrets/ssl_cert | jq -r '.value')
SSL_KEY=$(cat /open-horizon-secrets/ssl_key | jq -r '.value')

# Write certificates to files
echo "$SSL_CERT" > /etc/ssl/cert.pem
echo "$SSL_KEY" > /etc/ssl/key.pem

# Start service with SSL
my-service --ssl-cert /etc/ssl/cert.pem --ssl-key /etc/ssl/key.pem
```

## Common patterns

The following demonstrate three code patterns you may encounter.

### Configuration injection

Inject configuration from secrets:
```bash
#!/bin/bash

# Read configuration
CONFIG=$(cat /open-horizon-secrets/config | jq -r '.value')

# Start service with configuration
my-service --config "$CONFIG"
```

### Credential rotation

Handle credential updates:
```bash
#!/bin/bash

# Function to check for updates
check_updates() {
  local secret=$1
  local current_hash=$(md5sum /open-horizon-secrets/$secret | awk '{print $1}')
  local stored_hash=$(cat /tmp/${secret}_hash 2>/dev/null)
  
  if [ "$current_hash" != "$stored_hash" ]; then
    echo $current_hash > /tmp/${secret}_hash
    return 0
  fi
  return 1
}

# Monitor credentials
while true; do
  if check_updates "credentials"; then
    reload_credentials
  fi
  sleep 60
done
```

### Secure communication

Use secrets for secure communication:
```bash
#!/bin/bash

# Read certificate
CERT=$(cat /open-horizon-secrets/cert | jq -r '.value')

# Use certificate
curl --cert "$CERT" https://secure.example.com
``` 