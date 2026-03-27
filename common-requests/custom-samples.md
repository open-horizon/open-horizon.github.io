---
copyright: Contributors to the Open Horizon project
years: 2026
layout: page
title: "Using custom sample services"
description: "How to publish your own sample services with the All-in-One Management Hub"
lastupdated: 2026-03-27
parent: Quick Start
nav_order: 3
---

# Using custom sample services

The Open Horizon All-in-One Management Hub deployment includes a set of default example services that demonstrate edge computing capabilities. You can extend this by publishing your own custom sample services during the deployment process.

## Overview

The Bring Your Own (BYO) Samples feature allows you to specify additional service repositories that will be published to the Exchange during the All-in-One deployment. This is useful for:

- Testing your own edge services in a development environment
- Demonstrating custom solutions to stakeholders
- Learning Open Horizon by working with your own code
- Developing and validating services before production deployment

## How it works

When you set the `BYO_SAMPLES` environment variable, the deployment script:

1. Clones each repository you specify
2. Runs `make publish-only` in each repository
3. Publishes the service definition, service policy, and deployment policy to the Exchange
4. Makes the services available for deployment to edge nodes

Your custom samples are published in addition to the default Open Horizon example services (CPU, GPS, and Hello World).

## Prerequisites

Before using custom samples, ensure that:

- Each service repository follows the Open Horizon service structure
- Each repository contains a Makefile with these targets:
  - `publish-service`: Publishes the service definition
  - `publish-service-policy`: Publishes the service policy  
  - `publish-deployment-policy`: Publishes the deployment policy
- Services are compatible with your target edge node architecture (AMD64, ARM, etc.)

## Step-by-step instructions

### 1. Create a samples file

Create a text file containing the GitHub URLs of your service repositories, one per line:

```text
https://github.com/open-horizon/open-horizon-services/tree/main/web-helloworld-python
https://github.com/your-organization/your-custom-service
https://github.com/your-organization/another-service
```
{: codeblock}

Save this file (for example, as `my-samples.txt`) in a location accessible during deployment.

### 2. Set the environment variable

Before running the deployment script, export the `BYO_SAMPLES` variable:

```bash
export BYO_SAMPLES=my-samples.txt
```
{: codeblock}

### 3. Run the deployment

Run the All-in-One deployment script as usual:

```bash
curl -sSL https://raw.githubusercontent.com/open-horizon/devops/master/mgmt-hub/deploy-mgmt-hub.sh | bash
```
{: codeblock}

The script will automatically detect the `BYO_SAMPLES` variable and publish your custom services along with the default examples.

### 4. Verify the deployment

After deployment completes, verify that your custom services were published:

```bash
export HZN_ORG_ID=myorg
export HZN_EXCHANGE_USER_AUTH=admin:<password>
hzn exchange service list
```
{: codeblock}

You should see your custom services listed along with the default IBM examples.

## Example service repository structure

Your service repository should follow this structure:

```text
your-service/
├── Makefile
├── service.json
├── service.policy.json
├── deployment.policy.json
├── horizon/
│   ├── pattern.json (optional)
│   └── ...
└── src/
    └── ... (your service code)
```

The Makefile must include the `publish-only` target that calls the individual publish targets.

## Troubleshooting

### Service not appearing in Exchange

- Verify the GitHub URL is correct and accessible
- Check that the repository contains all required files
- Review the deployment script output for error messages
- Ensure the Makefile targets are properly defined

### Architecture mismatch

If your service doesn't deploy to your edge node:

- Check that the service supports your node's architecture
- Review the service definition's architecture specifications
- Verify the deployment policy matches your node policy

### Permission errors

If you encounter permission errors during publishing:

- Ensure the Exchange credentials are correctly set
- Verify your user has permission to publish to the organization
- Check that the organization exists in the Exchange

## Additional resources

- [Open Horizon Examples Repository](https://github.com/open-horizon/examples){:target="_blank"}{: .externalLink}
- [Open Horizon Services Catalog](https://github.com/open-horizon/open-horizon-services){:target="_blank"}{: .externalLink}
- [All-in-One Management Hub Documentation](https://github.com/open-horizon/devops/tree/master/mgmt-hub){:target="_blank"}{: .externalLink}
- [Service Development Guide](../docs/developing/developing_edge_services.md)

## Related topics

- [How to use Open Horizon](use.md)
- [Install Open Horizon](install.md)
- [FAQs](../docs/getting_started/faq.md)