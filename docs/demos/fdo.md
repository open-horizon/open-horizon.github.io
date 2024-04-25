---

copyright: 
years: 2024
lastupdated: "2024-04-25"
title: "Handsfree Device Onboarding demo"

nav_order: 4
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

# Handsfree Device Onboarding demo
{: #fdo_demo}

## Description

This demo show how hardware supporting the FIDO Device Onboard (FDO) specification can be provisioned with zero touch.  It will illustrate this by provisioning an Advantech edge device whose ownership voucher has been loaded into the Open Horizon Management Hub and whose profile has been configured as a Project EVE edge node that will register with the LF Edge Sandbox.  When power and connectivity has been added to the edge node, it will reach out to a rendezvous server, authenticate itself, begin the ownership transfer process, and then download and run an initialization package to register the device with the LF Edge Sandbox ... all in a matter of minutes.

## Videos

### Zero touch edge onboard in 1 minute (no audio)

{% include youtubePlayer.html id="QBxuucDkgmQ" %}

### Zero touch edge onboard with demo (4 minutes)

{% include youtubePlayer.html id="OWqZIC6yRI4" %}

## Code repositories

* [FDO code ](https://github.com/fido-device-onboard){:target="_blank"}{: .externalLink}
* [Project EVE code ](https://github.com/lf-edge/eve){:target="_blank"}{: .externalLink}
* [LF Edge Sandbox ](https://wiki.lfedge.org/display/LE/LF+Edge+Sandbox){:target="_blank"}{: .externalLink}

## Architecture overview

![FIDO Device Onboard solution diagram](https://wiki.lfedge.org/download/attachments/99877254/onesummit-demo.png?version=1&modificationDate=1711462592327&api=v2)

## Commercial Adoption

* IBM Edge Application Manager
* Falcon Tactical Edge