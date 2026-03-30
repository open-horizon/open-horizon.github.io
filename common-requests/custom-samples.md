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

The {{site.data.keyword.ieam}} All-in-One {{site.data.keyword.mgmt_hub}} deployment includes a set of default example services that demonstrate edge computing capabilities. You can extend this by publishing your own custom sample services during the deployment process.

## Overview

The Bring Your Own (BYO) Samples feature allows you to specify additional service repositories that are published to the Exchange during the All-in-One deployment. This is useful for:

- Testing your own edge services in a development environment
- Demonstrating custom solutions to stakeholders
- Learning {{site.data.keyword.ieam}} by working with your own code
- Developing and validating services before production deployment

## How it works

When you set the `BYO_SAMPLES` environment variable, the deployment script:

1. Clones each repository you specify
2. Runs `make publish-only` in each repository
3. Publishes the service definition, service policy, and deployment policy to the Exchange
4. Makes the services available for deployment to edge nodes

Your custom samples are published in addition to the default {{site.data.keyword.ieam}} example services (CPU, GPS, and Hello World).

## Prerequisites

Before using custom samples, ensure that:

- Each service repository follows the {{site.data.keyword.ieam}} service structure
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

The script automatically detects the `BYO_SAMPLES` variable and publishes your custom services along with the default examples.

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

Your service repository must follow this structure:

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