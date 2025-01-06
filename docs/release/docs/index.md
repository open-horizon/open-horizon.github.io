---
copyright:
years: 2023 - 2025
lastupdated: "2025-01-02"
layout: page
title: "Building a Release"
description: "Open Horizon Release Documentation"

nav_order: 6
has_children: false
has_toc: true
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# {{site.data.keyword.edge_notm}} Release Documentation
{: #releasedocs}

<div align="left">
  <img src="https://github.com/open-horizon/artwork/blob/master/color/open-horizon-color.png" alt="Badge" width="auto" height="50">
  
<h1 align="center">Building Open Horizon Releases</h1>

<p align="center">
  <a href="https://github.com/open-horizon/Open-Horizon-Release/releases/latest">
    <img src="https://img.shields.io/github/v/release/open-horizon/Open-Horizon-Release" alt="Release">
  </a>
  <a href="https://github.com/open-horizon/Open-Horizon-Release/releases/latest">
    <img src="https://img.shields.io/github/release-date/open-horizon/Open-Horizon-Release" alt="Release Date">
  </a>
</p>
<p align="center">
  This repository is dedicated to releasing Open Horizon components and tracking their versions across repositories.
</p>
</div>

## Table of Contents

- [Introduction](#introduction)
- [Release Manager Workflow](#release-manager-workflow)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Open Horizon Releases is a central repository aimed at managing and coordinating the release process for various Open Horizon components. Open Horizon is an open-source, edge-computing platform for managing the service software lifecycle of containerized workloads and related machine learning assets. It enables autonomous management of applications deployed to distributed webscale fleets of edge computing nodes and devices without requiring on-premise administrators.

## Why is this repository important?

We recognize the critical role of a single source of truth. This repository serves as the authoritative reference for version tracking and streamlined release management, consolidating version information from multiple repositories.

The release page within this repository serves as a hub connecting the main Open Horizon version to specific versions and their respective release pages of the individual components. This integration enables easy tracking of component releases that were tested together as part of the main Open Horizon release.

## Release Manager Workflow

The Release Manager Workflow is used for the tagging and releasing of Open Horizon components. It ensures consistency and reliability in the release process. Here's a step-by-step guide on how to use the Release Manager Workflow in this repository:

### 1. Creating a New Release

When it's time to create a new release for any Open Horizon component, follow these steps:

- **Step 1:** Generate your Release Versions JSON, it must include all of the keys within the example below.

```json
{   
    "amd64_agbot": "2.31.0-1498",
    "amd64_anax": "2.31.0-1498",
    "amd64_anax_k8s": "2.31.0-1498",
    "amd64_cloud-sync-service": "1.10.1-1498",
    "amd64_edge-sync-service": "1.10.1-1498",
    "amd64_exchange-api": "2.117.0-1163",
    "amd64_vault": "1.1.2-806",
    "fdo-owner-services": "2.31.0-1498",
    "sdo-owner-services": "1.11.16-1083"
}
```

- **Step 2:** Navigate to the [Release Manager Workflow Page](https://github.com/open-horizon/Open-Horizon-Release/actions/workflows/release.yml)

- **Step 3:** Click 'Run Workflow'.

- **Step 4:** Paste your Release Versions JSON into the parameter field.

- **Step 5:** Determine and select how the main Open Horizon Version should be incremented.

- **Step 6:** Hit the green 'Run Workflow' button.

- **Step 7:** Wait for the release to be approved by one of the specific contributors that controls the release management process.

### 2. Release Workflow Runtime Processes

- **Step 1:** Trigger Anax Release Manager.

  - Triggers the release.yml workflow within the Anax repository via GitHub's REST API, passes artifact versions from the Release Version JSON
  - Anax release manager pulls artifacts from its build-push.yml workflow, promotes docker images, and creates the release page for Anax
  - Waits for successful completion of the Anax release.yml workflow (checked via API)

- **Step 2:** Trigger Examples Release Manager.

  - Triggers the release.yml workflow within the Examples repository via GitHub's REST API, passes the entire Release Version JSON
  - Examples release manager creates the tested versions file and release page
  - Waits for successful completion of the Examples release.yml workflow (checked via API)

- **Step 3:** Increment Open Horizon Version.

  - Depending on the select option when starting the workflow, we will increment our main Open Horzion semantic version.
  - If major version is incremented, the minor and patch version are set to 0
  - If minor version is incremented, the patch version is set to 0

- **Step 4:** Create Open Horizon Release.

  - Creates the release page in this repository with a file that contains the released versions and links to the releases created in Open Horizon component repositories that are tied to the version of Open Horizon just released.

### 3. Celebrate New Open Horizon Release!

## Contributing

Contributions to Open Horizon Releases are welcome! If you have suggestions, bug reports, or want to contribute to the release process, please follow the guidelines in [CONTRIBUTING.md](https://github.com/open-horizon/.github/blob/master/CONTRIBUTING.md).

## License

This project is licensed under the Apache License 2.0. See [LICENSE](https://github.com/open-horizon/open-horizon-release/blob/main/LICENSE) for more details.
