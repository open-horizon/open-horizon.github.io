---
layout: post
title: "How do I (re)start the agent?"
description: ""
tags:
 - agent
excerpt_separator: <!--more-->
---
# How do I (re)start the agent?

To start the native binary agent (usually on Linux), you would need to run it as root:

``` shell
sudo systemctl start horizon
```

<!--more-->

The method used to start or restart the agent differs slightly depending on two factors:
* your operating system
* if the agent is a native binary or running in a container

If you are running the agent on OSX, it is containerized.  To start the containerized agent, use the following command:

``` shell
horizon-container start
```

