---

copyright: 
years: 2024
lastupdated: "2024-04-08"
title: "Handsfree Device Onboarding demo"

nav_order: 3
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

## Video

## Code repositories

* [FDO code ](https://github.com/fido-device-onboard){:target="_blank"}{: .externalLink}
* [Project EVE code ](https://github.com/lf-edge/eve){:target="_blank"}{: .externalLink}
* [LF Edge Sandbox ](https://wiki.lfedge.org/display/LE/LF+Edge+Sandbox){:target="_blank"}{: .externalLink}

## Architecture overview

