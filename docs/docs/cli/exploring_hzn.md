---
copyright: Contributors to the Open Horizon project
years: 2020 - 2025
title: hzn Command
description: Documentation for Exploring the hzn CLI
lastupdated: 2025-05-03
nav_order: 2
parent: CLI
---

# Exploring the hzn CLI

On Horizon edge nodes, use the `hzn` command to inspect many aspects of the state of the local system and of the larger Open Horizon ecosystem outside your edge node. Use the `hzn` command to interact with the system and change the state of resources you own.

You can get help for the `hzn` command, including more details about any of the subcommands by using the `--help` (or `-h`) flag at any subcommand level. For example, try the following commands:

```bash
hzn --help
hzn node --help
hzn exchange pattern --help
```

You can use the `--verbose` (or `-v`) flag in the `hzn` command to provide more detailed output. Most often `hzn` commands are convenience wrappers over the REST APIs that are provided by Horizon components, and the `--verbose` flag typically shows the details of the REST interactions behind the scenes. For example, try:

```bash
hzn node list -v
```  

The output of that command shows the two REST `GET` method invocations on `localhost` URLs where the local Horizon agent responds to REST requests.

For example:

```bash
[verbose] GET http://localhost:8510/node
[verbose] HTTP code: 200
...
[verbose] GET http://localhost:8510/status
[verbose] HTTP code: 200
```  
