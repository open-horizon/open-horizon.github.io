---

copyright:
years: 2021
lastupdated: "2021-02-20"
title: hzn Command
description: ""
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Exploring the hzn command
{: #exploring-hzn}

On {{site.data.keyword.horizon}} edge nodes, use the `hzn` command to inspect many aspects of the state of the local system and of the larger {{site.data.keyword.edge_notm}} ecosystem outside your edge node. Use the `hzn` command to interact with the system and change the state of resources you own.

You can get help for the `hzn` command, including more details about any of the subcommands by using the `--help` (or `-h`) flag at any subcommand level. For example, try the following commands:

```
hzn --help
hzn node --help
hzn exchange pattern --help
```
{: codeblock}

You can use the `--verbose` (or `-v`) flag in the `hzn` command to provide more detailed output. Most often `hzn` commands are convenience wrappers over the REST APIs that are provided by {{site.data.keyword.horizon}} components, and the `--verbose` flag typically shows the details of the REST interactions behind the scenes. For example, try:

```
hzn node list -v
```  
{: codeblock}

The output of that command shows the two REST `GET` method invocations on `localhost` URLs where the local {{site.data.keyword.horizon}} agent responds to REST requests.

For example:

```
[verbose] GET http://localhost:8510/node
[verbose] HTTP code: 200
...
[verbose] GET http://localhost:8510/status
[verbose] HTTP code: 200
```  
{: codeblock}
