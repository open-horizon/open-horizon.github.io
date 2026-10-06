---
copyright: Contributors to the Open Horizon project
years: 2026
title: System requirements
description: System requirements for installing Open Horizon components
lastupdated: "2026-08-19"
nav_order: 3
parent: Install Open Horizon
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# System requirements
{: #requirements}

The following sections describe the system requirements for each {{site.data.keyword.edge_notm}} component.
{:shortdesc}

## Management hub
{: #hub-requirements}

The management hub requires a machine or virtual machine with the following:

- **RAM**: 4 GB minimum
- **Storage**: 20 GB minimum
- **Operating system**: One of the following:
  - Fedora 36 or later
  - Red Hat Enterprise Linux 8.x or later (ppc64le)
  - Ubuntu 24.x or later (x86_64)
  - macOS (experimental)

**Note**: The management hub cannot run on arm64-based hardware.

For Windows adopters, you must be running Windows 10 or later with WSL2 installed. See [Windows WSL2 installation](../mgmt-hub/docs/WSL.md) for setup instructions. WSL2 support is considered experimental.

## Device agent
{: #device-agent-requirements}

The device agent can be installed on the following operating systems and architectures. Environments marked in **bold** have a corresponding installation package available.

### Linux devices

| Operating system | Versions | Architectures |
|---|---|---|
| Ubuntu | xenial (16.x), bionic (18.x), focal (20.x), jammy (22.x), noble (24.x), resolute (26.x) | **amd64**, **arm64**, **s390x** |
| Raspbian / Raspberry Pi OS | stretch (9), buster (10), bullseye (11), bookworm (12), trixie (13) | **armhf**, **arm64** |
| Debian | stretch (9), buster (10), bullseye (11), bookworm (12), trixie (13) | **amd64**, **armhf**, **arm64**, **s390x** |
| Red Hat Enterprise Linux | 7.6, 7.9, 8.1–8.5 (Docker), 8.6–8.10 and 9.0–9.8 (Podman 4.x or 5.x), 10.0–10.2 (Podman 4.x or 5.x) | **amd64**, **ppc64le**, aarch64, riscv64, **s390x** |
| CentOS | 8.1–8.5 (Docker) | **amd64**, **ppc64le**, aarch64, riscv64 |
| Fedora | 32, 35–44 | **amd64**, **ppc64le**, aarch64, riscv64 |

### macOS devices

| Operating system | Architectures |
|---|---|
| macOS | **amd64**, **M1**, **M2**, **M4** |

For more information, see [Agent installation script](../anax/docs/overview.md).

## Cluster agent
{: #cluster-agent-requirements}

You can deploy the cluster agent to any Kubernetes environment that is certified as part of the [Cloud Native Computing Foundation (CNCF) Certified Kubernetes Conformance program](https://www.cncf.io/certification/software-conformance/). For a list of the versions of Kubernetes that are CNCF certified, see the [Kubernetes Distributions and Platforms spreadsheet](https://docs.google.com/spreadsheets/d/1uF9BoDzzisHSQemXHIKegMhuythuq_GL3N1mlUUK2h0).
