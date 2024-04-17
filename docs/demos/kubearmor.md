---

copyright: 
years: 2024
lastupdated: "2024-04-17"
title: "Workload Runtime Security demo"

nav_order: 2
has_children: false
has_toc: false
parent: "Demonstration videos and code"
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Workload Runtime Security demos
{: #kubearmor_demos}

## Description

These demos show how to implement Security by Default (SbD) on the host and in container environments by integrating and enforcing security policies as part of workload deployment and lifecycle management.  This solution actively mitigates attacks by bad actors so that they cannot occur.  This method of application hardening sandboxes application behavior so that only pre-specified behavior is allowed.

## Use Cases

Four specific scenarios can demonstrate the power of this approach:

1. Preventing cryptojacking attacks on edge nodes
2. Securing credentials or sensitive assets on edge nodes
3. Preventing lateral movements between devices and/or applications
4. Highlighting preemptive mitigation techniques enabled by KubeArmor + Open Horizon

## Videos

### Defending against Cryptojacking attacks (2 minutes)

{% include youtubePlayer.html id="pV43ttC4Ja0" %}

### File Integrity Monitoring (FIM) using policies on a K8s cluster (2 minutes)

{% include youtubePlayer.html id="WJfHmxm8Gg0" %}

### Denying malicious binary process before execution (2 minutes)

{% include youtubePlayer.html id="n1GpkV3KbQQ" %}

### Implementing zero trust security policies on a K8s cluster (2 minutes)

{% include youtubePlayer.html id="Jni8vJ3IrJc" %}

### Deploying KubeArmor with Open Horizon (11 minutes)

{% include youtubePlayer.html id="691AlW_GE1k" %}

## Code repositories

* Example [Open Horizon service deploying KubeArmor ](https://github.com/open-horizon/kubearmor-integration){:target="_blank"}{: .externalLink}

## Architecture overview

![KubeArmor-Open Horizon integration diagram](https://github.com/open-horizon/kubearmor-integration/raw/main/docs/OH-edge-kubearmor.png)

## Feature Request

[Workload Runtime Security ](https://wiki.lfedge.org/display/OH/OH+Agent+and+Edge+Workload+Runtime+Security){:target="_blank"}{: .externalLink}