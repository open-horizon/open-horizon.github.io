# Overview of Open Horizon

This section provides an overview of Open Horizon (OH).

## Open Horizon capabilities

Open Horizon provides you with edge computing features to help you manage and deploy workloads from a management hub cluster to edge devices and remote instances of OpenShift Container Platform or other Kubernetes-based clusters.

## Architecture

The goal of edge computing is to harness the disciplines that have been created for hybrid cloud computing to support remote operations of edge computing facilities. Open Horizon is designed for that purpose.

The deployment of Open Horizon includes the management hub that runs in an instance of OpenShift Container Platform installed in your data center. The management hub is where the management of all of your remote edge nodes (edge devices and edge clusters) occurs.

These edge nodes can be installed in remote on-premises locations to make your application workloads local to where your critical business operations physically occur, such as at your factories, warehouses, retail outlets, distribution centers, and more.

The following diagram depicts the high-level topology for a typical edge computing setup:

The Open Horizon management hub is designed specifically for edge node management to minimize deployment risks and to manage the service software lifecycle on edge nodes fully autonomously. A Cloud installer installs and manages the Open Horizon management hub components. Software developers develop and publish edge services to the management hub. Administrators define the deployment policies that control where edge services are deployed. Open Horizon handles everything else.

# Components

Open Horizon (Open Horizon) includes several components that are required for functionality. For more information about such components, please see [Components](https://open-horizon.github.io/docs/getting_started/components/index.md).

## What's next

For more information about using Open Horizon and developing edge services, review the topics that are listed in Open Horizon (Open Horizon) [Welcome page](https://open-horizon.github.io/docs/index.md) and in the following sections:

- [Accessibility](https://open-horizon.github.io/docs/getting_started/accessibility/index.md)
- [Components](https://open-horizon.github.io/docs/getting_started/components/index.md)
- [Developer learning path](https://open-horizon.github.io/docs/getting_started/developer_learning_path/index.md)
- [Documentation conventions](https://open-horizon.github.io/docs/getting_started/document_conventions/index.md)
- [Frequently Asked Questions (FAQ)](https://open-horizon.github.io/docs/getting_started/faq/index.md)
- [Known issues and limitations](https://open-horizon.github.io/docs/getting_started/known_issues/index.md)
- [Release notes](https://open-horizon.github.io/docs/getting_started/release_notes/index.md)
