---
copyright: Contributors to the Open Horizon project
years: 2025
title: Handsfree Device Onboarding demo
description: Documentation for Handsfree Device Onboarding demo
lastupdated: 2025-05-03
nav_order: 4
parent: Demonstration videos and code
has_children: False
has_toc: False
---

# Handsfree Device Onboarding demo

## Description

This demo show how hardware supporting the FIDO Device Onboard (FDO) specification can be provisioned with zero touch.  It will illustrate this by provisioning an Advantech edge device whose ownership voucher has been loaded into the Open Horizon Management Hub and whose profile has been configured as a Project EVE edge node that will register with the LF Edge Sandbox.  When power and connectivity has been added to the edge node, it will reach out to a rendezvous server, authenticate itself, begin the ownership transfer process, and then download and run an initialization package to register the device with the LF Edge Sandbox ... all in a matter of minutes.

## Videos

### Zero touch edge onboard in 1 minute (no audio)

<div class="embed-youtube">
<iframe src="https://www.youtube.com/embed/QBxuucDkgmQ" title="YouTube video" width="560" height="315" loading="lazy" allowfullscreen></iframe>
</div>

### Zero touch edge onboard with demo (4 minutes)

<div class="embed-youtube">
<iframe src="https://www.youtube.com/embed/OWqZIC6yRI4" title="YouTube video" width="560" height="315" loading="lazy" allowfullscreen></iframe>
</div>

## Code repositories

* [FDO code ](https://github.com/fido-device-onboard)
* [Project EVE code ](https://github.com/lf-edge/eve)
* [LF Edge Sandbox ](https://wiki.lfedge.org/display/LE/LF+Edge+Sandbox)

## Architecture overview

![FIDO Device Onboard solution diagram](https://wiki.lfedge.org/download/attachments/99877254/onesummit-demo.png?version=1&modificationDate=1711462592327&api=v2)

## Commercial Adoption

* IBM Edge Application Manager
* Falcon Tactical Edge