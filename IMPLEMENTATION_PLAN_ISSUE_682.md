# Implementation Plan for GitHub Issue #682
## New TOC Structure for Agent (anax) Documentation

**Issue**: https://github.com/open-horizon/open-horizon.github.io/issues/682
**Comment**: https://github.com/open-horizon/open-horizon.github.io/issues/682#issuecomment-4092022614

---

## Overview

This issue requires implementing a new Table of Contents (TOC) structure for the Agent (anax) documentation. Due to the multi-repository architecture of Open Horizon documentation, changes must be coordinated across **two repositories**:

1. **open-horizon/anax** - Source repository for agent documentation
2. **open-horizon/open-horizon.github.io** - Main documentation site

---

## Multi-Repository Architecture

According to AGENTS.md, the following directories in open-horizon.github.io are **auto-synced** from other repositories:

```
docs/
├── anax/docs/          # Copied from open-horizon/anax
├── mgmt-hub/docs/      # Copied from open-horizon/devops
├── kubearmor-integration/docs/  # Copied from open-horizon/kubearmor-integration
├── fdo/docs/           # Copied from open-horizon/FDO-support
├── exchange-api/docs/  # Copied from open-horizon/exchange-api
├── release/docs/       # Copied from open-horizon/open-horizon-release
```

**CRITICAL RULE**: Never modify files in `docs/anax/docs/` directly in open-horizon.github.io. All changes must be made in the source repository (open-horizon/anax).

---

## Proposed TOC Structure

Based on the GitHub comment, the new structure should be:

```
Installing edge clusters [prereq for installing an agent, opt: ]
  Installing an OCP cluster ^
  Installing a K3s cluster ^^
  Installing a MicroK8s cluster ^^
  Setup edge cluster local image registry for K3s
  Setup edge cluster local image registry for MicroK8s
  Setting variables to use a remote image registry

Edge node agents (anax) (first para of this topic will mention the synonyms: cluster agent/edge agent/edge node agent/device agent)
  Installing an agent on an edge device (script topic)
  Installing the agent on an edge cluster
    Installing the agent on Red Hat OpenShift Container Platform Kubernetes edge clusters
    Installing the agent on K3s and MicroK8s edge clusters
    Deploying services to your edge cluster
    Configuring a storage class
    Removing the agent from an edge cluster
  Installing an agent in a container
  Configuring authentication
    Authenticating to the management hub (Authentication overview)
    Managing secrets (Open Horizon Secrets Management with open-horizon-wiotp)
  Configuring policies
    Policy-based deployment
    Built-in policy
    Deployment policy
    Service policy
    Model policy
    Node policy
    Properties and constraints
  Defining and deploying services
    Model objects
    Defining and deploying services
    Managing the lifecycle of services/Creating service workload definitions
    Service Definition
    Horizon Deployment Strings
  Upgrading agents automatically
    Using manifests for automatic agent upgrades (Automatic agent upgrades)
    NMP status objects
    Node management policies
    Using NMPs to upgrade agents automatically (Node management overview)
  Advanced features
    High availability node groups
    Namespace scoping for cluster agents (Multi-namespace for cluster agents)
  API Reference
    Horizon APIs
    Attributes for Horizon POST APIs
    Agreement Bot APIs
```

---

## Part 1: Changes in open-horizon/anax Repository

### Repository Location
- **Repo**: https://github.com/open-horizon/anax
- **Directory**: `docs/` (root of anax docs)

### Changes Required

#### 1. Rename Section Title
- **File**: `docs/index.md`
- **Change**: Rename from "Agent (anax)" to "Edge node agents (anax)"
- **Add**: First paragraph mentioning agent synonyms (cluster agent/edge agent/edge node agent/device agent)

#### 2. Create New Parent Section Pages
Create 7 new parent pages to organize content:

1. **`docs/installing_agent_on_edge_cluster.md`**
   - Title: "Installing the agent on an edge cluster"
   - Parent: "Edge node agents (anax)"
   - nav_order: 2

2. **`docs/configuring_authentication.md`**
   - Title: "Configuring authentication"
   - Parent: "Edge node agents (anax)"
   - nav_order: 4

3. **`docs/configuring_policies.md`**
   - Title: "Configuring policies"
   - Parent: "Edge node agents (anax)"
   - nav_order: 5

4. **`docs/defining_deploying_services.md`**
   - Title: "Defining and deploying services"
   - Parent: "Edge node agents (anax)"
   - nav_order: 6

5. **`docs/upgrading_agents_automatically.md`**
   - Title: "Upgrading agents automatically"
   - Parent: "Edge node agents (anax)"
   - nav_order: 7

6. **`docs/advanced_features.md`**
   - Title: "Advanced features"
   - Parent: "Edge node agents (anax)"
   - nav_order: 8

7. **`docs/api_reference.md`**
   - Title: "API Reference"
   - Parent: "Edge node agents (anax)"
   - nav_order: 9

#### 3. Update Front Matter for Existing Files

Update the following fields in all affected files:
- `parent`: Update to new parent section names
- `grand_parent`: Add "Edge node agents (anax)" where needed
- `nav_order`: Reorder according to new structure
- `lastupdated`: Update to current date (2026-04-07)
- `years`: Update to include 2026 if not already present

**Files to Update** (30+ files):

**Installing agent on edge cluster section:**
- `installing_ocp_edge_cluster_agent.md` - nav_order: 1, parent: "Installing the agent on an edge cluster"
- `installing_k3s_microk8s_agent.md` - nav_order: 2, parent: "Installing the agent on an edge cluster"
- `deploying_services_cluster.md` - nav_order: 3, parent: "Installing the agent on an edge cluster"
- `configuring_storage_class.md` - nav_order: 4, parent: "Installing the agent on an edge cluster"
- `removing_agent_from_cluster.md` - nav_order: 5, parent: "Installing the agent on an edge cluster"

**Configuring authentication section:**
- `authentication_overview.md` - nav_order: 1, parent: "Configuring authentication"
- `secrets.md` - nav_order: 2, parent: "Configuring authentication"

**Configuring policies section:**
- `policy.md` - nav_order: 1, parent: "Configuring policies"
- `built_in_policy.md` - nav_order: 2, parent: "Configuring policies"
- `deployment_policy.md` - nav_order: 3, parent: "Configuring policies"
- `service_def.md` (if service policy) - nav_order: 4, parent: "Configuring policies"
- `model_policy.md` - nav_order: 5, parent: "Configuring policies"
- `node_policy.md` - nav_order: 6, parent: "Configuring policies"
- `properties_and_constraints.md` - nav_order: 7, parent: "Configuring policies"

**Defining and deploying services section:**
- (Identify and update relevant files for model objects, service definitions, deployment strings)

**Upgrading agents automatically section:**
- `managed_workloads.md` (or similar) - nav_order: 1, parent: "Upgrading agents automatically"
- `node_management_status.md` - nav_order: 2, parent: "Upgrading agents automatically"
- `node_management_policy.md` - nav_order: 3, parent: "Upgrading agents automatically"
- `node_management_overview.md` - nav_order: 4, parent: "Upgrading agents automatically"

**Advanced features section:**
- `ha_groups.md` - nav_order: 1, parent: "Advanced features"
- `agent_in_multi_namespace.md` - nav_order: 2, parent: "Advanced features"

**API Reference section:**
- `api.md` - nav_order: 1, parent: "API Reference"
- `attributes.md` - nav_order: 2, parent: "API Reference"
- `agreement_bot_api.md` - nav_order: 3, parent: "API Reference"

#### 4. Workflow for anax Repository

1. Fork open-horizon/anax repository
2. Create branch: `issue-682-toc-restructure`
3. Make all changes listed above
4. Test locally with Jekyll
5. Submit PR to open-horizon/anax
6. Wait for PR approval and merge
7. Wait for automated sync to open-horizon.github.io

---

## Part 2: Changes in open-horizon/open-horizon.github.io Repository

### Repository Location
- **Repo**: https://github.com/open-horizon/open-horizon.github.io
- **Directory**: `docs/installing/`

### Changes Required

#### 1. Replace 3 Cluster Installation Files

According to the GitHub comment, replace these files with versions from the anax repository:

**Files to Replace:**
1. **`docs/installing/install_ocp_edge_cluster.md`**
   - Source: `https://github.com/open-horizon/anax/blob/master/docs/install_ocp_edge_cluster.md`
   - Update front matter: parent: "Installing edge clusters", nav_order: 1

2. **`docs/installing/install_k3s_edge_cluster.md`**
   - Source: `https://github.com/open-horizon/anax/blob/master/docs/install_k3s_cluster.md`
   - Update front matter: parent: "Installing edge clusters", nav_order: 2

3. **`docs/installing/install_microk8s_edge_cluster.md`**
   - Source: `https://github.com/open-horizon/anax/blob/master/docs/install_microk8s_cluster.md`
   - Update front matter: parent: "Installing edge clusters", nav_order: 3

#### 2. Create "Installing edge clusters" Parent Page

Create new file: **`docs/installing/installing_edge_clusters.md`**

```yaml
---
copyright:
  years: 2020 - 2026
lastupdated: "2026-04-07"
layout: page
title: "Installing edge clusters"
description: "Prerequisites for installing an agent"
nav_order: 1
parent: Installing
has_children: true
has_toc: false
---

# Installing edge clusters

Before installing an Open Horizon agent, you must first set up an edge cluster. This section covers the installation of various Kubernetes distributions that can serve as edge clusters.

## Available cluster types

- Red Hat OpenShift Container Platform (OCP)
- K3s - Lightweight Kubernetes
- MicroK8s - Lightweight Kubernetes

Choose the cluster type that best fits your edge computing requirements.
```

#### 3. Update Existing Files in docs/installing/

Update front matter for files related to image registries:
- Update `parent` references if needed
- Update `nav_order` to fit new structure
- Update `lastupdated` and `years` fields

#### 4. Workflow for open-horizon.github.io Repository

1. Create branch: `issue-682-installing-section`
2. Copy 3 files from anax repository
3. Update front matter in copied files
4. Create new parent page
5. Update related files
6. Test locally with Jekyll
7. Submit PR to open-horizon/open-horizon.github.io
8. Wait for PR approval and merge

---

## Coordination Strategy

### Timing

1. **Phase 1**: Submit PR to open-horizon/anax first
   - Wait for approval and merge
   - Wait for automated sync to complete

2. **Phase 2**: Submit PR to open-horizon/open-horizon.github.io
   - Only after anax changes are synced
   - This ensures consistency across repositories

### Testing

1. **Local Testing**: Build Jekyll site locally in both repositories
2. **Navigation Testing**: Verify all links work correctly
3. **Hierarchy Testing**: Confirm parent/child relationships are correct
4. **Cross-Repository Testing**: After sync, verify anax content appears correctly in main site

---

## Checklist

### open-horizon/anax Repository
- [ ] Fork and clone repository
- [ ] Create branch `issue-682-toc-restructure`
- [ ] Update docs/index.md (rename section, add agent synonyms)
- [ ] Create 7 new parent section pages
- [ ] Update front matter for 30+ existing files
- [ ] Test locally with Jekyll
- [ ] Submit PR
- [ ] Wait for merge and sync

### open-horizon/open-horizon.github.io Repository
- [ ] Create branch `issue-682-installing-section`
- [ ] Copy 3 cluster installation files from anax
- [ ] Update front matter in copied files
- [ ] Create "Installing edge clusters" parent page
- [ ] Update related files in docs/installing/
- [ ] Test locally with Jekyll
- [ ] Submit PR
- [ ] Wait for merge

### Final Verification
- [ ] Verify navigation structure on live site
- [ ] Test all internal links
- [ ] Verify breadcrumbs are correct
- [ ] Check mobile responsiveness
- [ ] Validate accessibility

---

## Notes

- All changes must respect the multi-repository architecture
- Never modify files in auto-synced directories directly
- Always update `lastupdated` and `years` fields in front matter
- Follow Jekyll front matter conventions
- Test thoroughly before submitting PRs
- Coordinate timing between repositories to avoid inconsistencies

---

## References

- GitHub Issue: https://github.com/open-horizon/open-horizon.github.io/issues/682
- AGENTS.md: Multi-Repository Sources section
- Jekyll Documentation: https://jekyllrb.com/docs/
- Open Horizon Documentation: https://open-horizon.github.io/