---
layout:             post
title:              "Can I assign a dedicated network between services on a node?"
description:        ""
tags:               
 - Agent
 - Networking
 - Device
author:             joewxboy
excerpt_separator:  <!--more-->
---

# Can I assign a dedicated network between services on a node?

Bright Zheng - While deploying multiple containers within one edge node, is it possible to assign a dedicated Docker network to all these containers so that they can communicate through known hostnames?

<!--more-->

Glen Darling - If you establish dependencies between them, using requiredServces then this private networking is done automatically for you and you can use the name you defined for the service on those networks. The cpu2eventstreams example illustrates this. Note though…. this feature only works on “devices” not on clusters.

Ivan Portilla - Network settings are also described here - https://github.com/open-horizon/anax/blob/master/doc/deployment_string.md
