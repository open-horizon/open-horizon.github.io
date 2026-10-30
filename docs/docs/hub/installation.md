---
copyright: Contributors to the Open Horizon project
years: 2020 - 2025
title: Installing Open Horizon
description: Documentation for Installation
lastupdated: 2025-05-03
nav_order: 9
has_children: True
has_toc: False
---

# Installation

You can complete the following types of Open Horizon installation:

* Full installation - Install all Open Horizon components. For a list of components, see [Components](../getting_started/components.md).
* Install the management hub only - Install the Open Horizon management hub, the `horizon-cli package`, and an agent. For more information, see [Installing the management hub only](hub.md).
* Custom installations - You can override particular aspects of the platform installation. You can install versions other than the latest, install custom sample services, and more. You use the `deploy-mgmt-hub.sh` script for custom installations. For example, the following command installs the `horizon-cli` package, but not the Open Horizon agent package. The command also doesn't register the edge node or load the custom sample services, policies, and patterns.

  ```shell
  curl -sSL https://raw.githubusercontent.com/open-horizon/devops/master/mgmt-hub/deploy-mgmt-hub.sh | bash -s -- -A -R -E
  ```
  To read about the script and the flags that you can use, see [https://github.com/open-horizon/devops/blob/master/mgmt-hub/deploy-mgmt-hub.sh](https://github.com/open-horizon/devops/blob/master/mgmt-hub/deploy-mgmt-hub.sh).

This section describes the process of installing Open Horizon.

* [Prerequisites](./prerequisites.md)
* [Install Open Horizon](./online_installation.md)
* [Post installation](./post_install.md)
* [Gather edge node files](./gather_files.md)
