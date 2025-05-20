---
copyright: Contributors to the Open Horizon project
years: 2021 - 2025
title: Examples
description: Examples of using secrets in Open Horizon services
lastupdated: 2025-05-07
nav_order: 4
parent: Secrets Management
grand_parent: Developing edge services
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}

# Examples
{: #examples}

This guide provides practical examples of using secrets in Open Horizon services, including [the Hello Secret World example](https://github.com/open-horizon/examples/tree/master/edge/services/helloSecretWorld).

## Hello Secret World
{: #hello_secret_world}

The Hello Secret World example demonstrates how to create and use a simple service that uses secrets. This example is a good starting point for understanding secrets management in Open Horizon.

### Prerequisites
{: #hello_secret_prerequisites}

1. Install the Open Horizon management hub infrastructure
2. Set up your exchange user credentials
3. Install the Open Horizon agent on your edge device
4. Configure your environment variables
5. Unregister your node (if previously registered)

### Step 1: Create a secret
{: #hello_secret_create}

Create an organization-wide secret:
```bash
hzn secretsmanager secret add --secretKey "greeting" --secretDetail "Hello World" hw-secret-name
```

### Step 2: Register with the pattern
{: #hello_secret_register}

Register your edge node with the hello-secret pattern:
```bash
hzn register -p IBM/pattern-ibm.hello-secret -s ibm.hello-secret --serviceorg IBM
```

### Step 3: Monitor the service
{: #hello_secret_monitor}

View the service output:
```bash
hzn service log -f ibm.hello-secret
```

You should see output like:
```
Hello World says: Hello World!
```

### Step 4: Update the secret
{: #hello_secret_update}

Update the secret value:
```bash
hzn secretsmanager secret add --secretKey "greeting" --secretDetail "Hello Open Horizon" hw-secret-name
```

After some time, you should see the output change to:
```
Hello Open Horizon says: Hello Open Horizon!
```

### Step 5: Clean up
{: #hello_secret_cleanup}

Unregister your node:
```bash
hzn unregister -f
```

## Real-world examples
{: #real_world_examples}

### API Authentication
{: #api_auth}

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
{: #db_connection}

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
{: #cert_auth}

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
{: #common_patterns}

### Configuration injection
{: #config_injection}

Inject configuration from secrets:
```bash
#!/bin/bash

# Read configuration
CONFIG=$(cat /open-horizon-secrets/config | jq -r '.value')

# Start service with configuration
my-service --config "$CONFIG"
```

### Credential rotation
{: #credential_rotation}

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
{: #secure_communication}

Use secrets for secure communication:
```bash
#!/bin/bash

# Read certificate
CERT=$(cat /open-horizon-secrets/cert | jq -r '.value')

# Use certificate
curl --cert "$CERT" https://secure.example.com
``` 