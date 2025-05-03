---
copyright: {'years': '2020 - 2022'}
years: 2025
title: Configuration
description: Documentation for Configure {{site.data.keyword.ieam}}
lastupdated: 2025-05-03
nav_order: 2
parent: Installing Management hub
grand_parent: Management Hub
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Configure {{site.data.keyword.ieam}}

## Additional ORG level configuration for high scale environments

To support high scale environments greater than 10,000 edge nodes, adjust the heartbeat intervals that the edge nodes use to check for changes. 

The following command should be issued by a super user:

```bash
hzn exchange org update --heartbeatmin=60 --heartbeatmax=900 --heartbeatadjust=60 <org_name>
```
{: codeblock}

If multiple ORGS used, the command should be issued for each ORG supporting more than 10,000 edge nodes.
