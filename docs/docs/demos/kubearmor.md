---
copyright: Contributors to the Open Horizon project
years: 2025
title: Workload Runtime Security demo
description: Documentation for Workload Runtime Security demos
lastupdated: 2025-05-03
nav_order: 2
parent: Demonstration videos and code
has_children: False
has_toc: False
---

# Workload Runtime Security demos

## Description

These demos show how to implement Security by Default (SbD) on the host and in container environments by integrating and enforcing security policies as part of workload deployment and lifecycle management.  This solution actively mitigates attacks by bad actors so that they cannot occur.  This method of application hardening sandboxes application behavior so that only pre-specified behavior is allowed.

## Use Cases

Four specific scenarios can demonstrate the power of this approach:

1. Preventing cryptojacking attacks on edge nodes
2. Securing credentials or sensitive assets on edge nodes
3. Preventing lateral movements between devices and/or applications
4. Highlighting preemptive mitigation techniques enabled by KubeArmor + Open Horizon

## Videos

### KubeArmor/Open Horizon demos in one minute (1 minute, no audio)

<div class="embed-youtube">
<iframe src="https://www.youtube.com/embed/ZwDxLMdt6lI" title="YouTube video" width="560" height="315" loading="lazy" allowfullscreen></iframe>
</div>

### Defending against Cryptojacking attacks (2 minutes)

<div class="embed-youtube">
<iframe src="https://www.youtube.com/embed/pV43ttC4Ja0" title="YouTube video" width="560" height="315" loading="lazy" allowfullscreen></iframe>
</div>

### File Integrity Monitoring (FIM) using policies on a K8s cluster (2 minutes)

<div class="embed-youtube">
<iframe src="https://www.youtube.com/embed/WJfHmxm8Gg0" title="YouTube video" width="560" height="315" loading="lazy" allowfullscreen></iframe>
</div>

### Denying malicious binary process before execution (2 minutes)

<div class="embed-youtube">
<iframe src="https://www.youtube.com/embed/n1GpkV3KbQQ" title="YouTube video" width="560" height="315" loading="lazy" allowfullscreen></iframe>
</div>

### Implementing zero trust security policies on a K8s cluster (2 minutes)

<div class="embed-youtube">
<iframe src="https://www.youtube.com/embed/Jni8vJ3IrJc" title="YouTube video" width="560" height="315" loading="lazy" allowfullscreen></iframe>
</div>

### Deploying KubeArmor with Open Horizon (11 minutes)

<div class="embed-youtube">
<iframe src="https://www.youtube.com/embed/691AlW_GE1k" title="YouTube video" width="560" height="315" loading="lazy" allowfullscreen></iframe>
</div>

## Code repositories

* Example [Open Horizon service deploying KubeArmor ](https://github.com/open-horizon/kubearmor-integration)

## Architecture overview

![KubeArmor-Open Horizon integration diagram](https://github.com/open-horizon/kubearmor-integration/raw/main/docs/OH-edge-kubearmor.png)

## Feature Request

[Workload Runtime Security ](https://wiki.lfedge.org/display/OH/OH+Agent+and+Edge+Workload+Runtime+Security)