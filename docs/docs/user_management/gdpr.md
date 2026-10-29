---
copyright: Contributors to the Open Horizon project
years: 2020 - 2026
title: GDPR readiness
description: Documentation for Open Horizon considerations for GDPR readiness
lastupdated: 2025-05-03
nav_order: 3
parent: Security
grand_parent: Administering
---

# Open Horizon considerations for GDPR readiness

## Notice

<!-- This is boilerplate text provided by the GDPR team. It cannot be changed. -->

This document is intended to help you prepare for GDPR readiness. It provides Open Horizon feature information that you can configure, and aspects of the product's use to consider when you are preparing your organization for GDPR. This information is not an exhaustive list. Clients can choose and configure features many different ways and use the product in many ways and with third-party applications and systems.

<p class="ibm-h4 ibm-bold">Clients are responsible for ensuring their own compliance with various laws and regulations, including the European Union General Data Protection Regulation. Clients are solely responsible for obtaining advice of competent legal counsel as to the identification and interpretation of any relevant laws and regulations that might affect the clients' business and any actions the clients might need to take to comply with such laws and regulations.</p>

<p class="ibm-h4 ibm-bold">The products, services, and other capabilities that are described here are not suitable for all client situations and might restrict availability. IBM does not provide legal, accounting, or auditing advice or represent or warrant that its services or products ensure that clients are in compliance with any law or regulation.</p>

## Table of Contents

* [GDPR](#overview)
* [Product Configuration for GDPR](#productconfig)
* [Data Life Cycle](#datalifecycle)
* [Data Processing](#dataprocessing)
* [Capability for Restricting Use of Personal Data](#datasubjectrights)
* [Appendix](#appendix)

## GDPR {: #overview }

<!-- This is boilerplate text provided by the GDPR team. It cannot be changed. -->
General Data Protection Regulation (GDPR) was adopted by the European Union (EU) and applies from 25 May 2018.

### Why is GDPR important?

GDPR establishes a stronger data protection regulatory framework for processing of personal data of individuals. GDPR brings:

* New and enhanced rights for individuals
* Widened definition of personal data
* New obligations for companies and organizations that are handling personal data
* Significant financial penalties for non-compliance
* Compulsory data breach notification

IBM established a global readiness program that is tasked with preparing IBM's internal processes and commercial offerings for compliance with the GDPR.

### More information

* [EU GDPR Information Portal ](https://gdpr.eu/)
* [ibm.com/GDPR website ](https://www.ibm.com/data-responsibility/gdpr/)

## Product Configuration – considerations for GDPR Readiness {: #productconfig }

The following sections describe aspects of Open Horizon and provide information on capabilities to help clients with GDPR requirements.

### Data Life Cycle {: #datalifecycle }

Open Horizon is an application for developing and managing on-premises, containerized applications. It is an integrated environment for managing container workloads at the edge. It includes the container orchestrator Kubernetes, a private image registry, a management console, an edge node agent, and monitoring frameworks.

As such, Open Horizon works primarily with technical data that is related to the configuration and management of the application, some of which might be subject to GDPR. Open Horizon also deals with information about users who manage the application. This data is described throughout this document for the awareness of clients responsible for meeting GDPR requirements.

This data is persisted on the Open Horizon on local or remote file systems as configuration files or in databases. Applications that are developed to run on Open Horizon might use other forms of personal data subject to GDPR. The mechanisms that are used to protect and manage data are also available to applications that run on Open Horizon. More mechanisms might be needed to manage and protect personal data that is collected by applications that are run on Open Horizon.

To understand Open Horizon data flows, you must understand how Kubernetes, Docker, and Operators work. These open source components are fundamental to the Open Horizon. You use Open Horizon to place instances of application containers (edge services) on edge nodes. The edge services contain the details about the application, and the Docker&reg; images contain all the software packages that your applications need to run.

Open Horizon includes a set of open source edge service examples. To view a list of all the Open Horizon charts, see [open-horizon/examples ](https://github.com/open-horizon/examples). It is the client’s responsibility to determine and implement any appropriate GDPR controls for open source software.

### What types of data flow through Open Horizon

Open Horizon deals with several categories of technical data that might be considered personal data, such as:

* Administrator or operator user ID and password
* IP addresses
* Kubernetes node names

Information about how this technical data is collected and created, stored, accessed, secured, logged, and deleted is described in later sections of this document.

### Personal data used for online contact with IBM

Open Horizon clients can submit online comments, feedback, and requests to IBM about Open Horizon subjects in various ways, primarily:

* The public Open Horizon Slack Community
* Public comments area on pages of Open Horizon product documentation
* Public comments in the Open Horizon space of dW Answers

Typically, only the client name and email address are used to enable personal replies for the subject of the contact. This use of personal data conforms to the [IBM Online Privacy Statement ](https://www.ibm.com/privacy/us/en/).

### Authentication

The Open Horizon authentication manager accepts user credentials from the management console and forwards the credentials to the backend OIDC provider, which validates the user credentials against the enterprise directory. The OIDC provider then returns an authentication cookie (`auth-cookie`) with the content of a JSON Web Token (`JWT`) to the authentication manager. The JWT token persists information such as the user ID and email address, in addition to group membership at the time of the authentication request. This authentication cookie is then sent back to the management console. The cookie is refreshed during the session. It is valid for 12 hours after you sign out of the management console or close your web browser.

For all subsequent authentication requests made from the management console, the front-end NodeJS server decodes the available authentication cookie in the request and validates the request by calling the authentication manager.

The Open Horizon CLI requires the user to provide an API key. API keys are created by using the `cloudctl` command.

The **cloudctl**, **kubectl**, and **oc** CLIs also require credentials to access the cluster. These credentials can be obtained from the management console and expire after 12 hours.

### Role Mapping

Open Horizon supports role-based access control (RBAC). In the role-mapping stage, the username that is provided in the authentication stage is mapped to a user or group role. The roles are used to authorize which activities can be carried out by the authenticated user. See [Role-based access control](rbac.md) for details about Open Horizon roles.

### Pod Security

Pod security policies are used to set up management hub or edge cluster control over what a pod can do or what it can access. For more information about pods, see [Installing the management hub](../hub/hub.md) and [Edge clusters](../installing/edge_clusters.md).

## Data Processing {: #dataprocessing }

Users of Open Horizon can control the way that technical data that is related to configuration and management is processed and secured through system configuration.

* Role-based access control (RBAC) controls what data and functions can be accessed by users.
* Pod security policies are used to set up cluster-level control over what a pod can do or what it can access.
* Data-in-transit is protected by using `TLS`. `HTTPS` (`TLS` underlying) is used for secure data transfer between user client and back-end services. Users can specify the root certificate to use during installation.
* Data-at-rest protection is supported by using `dm-crypt` to encrypt data.
* Data retention periods for logging (ELK) and monitoring (Prometheus) are configurable and deletion of data is supported through provided APIs.

These same mechanisms that are used to manage and secure Open Horizon technical data can be used to manage and secure personal data for user-developed or user-provided applications. Clients can develop their own capabilities to implement further controls.

For more information about certificates, see [Install Open Horizon](../hub/installation.md).

## Capability for Restricting Use of Personal Data {: #datasubjectrights }

Using the facilities summarized in this document, Open Horizon enables a user to restrict usage of any technical data within the application that is considered personal data.

Under GDPR, users have rights to access, modify, and restrict processing. Refer to other sections of this document to control:

* Right to access
  * Open Horizon administrators can use Open Horizon features to provide individuals access to their data.
  * Open Horizon administrators can use Open Horizon features to provide individuals information about what data Open Horizon collects and retains about the individual.
* Right to modify
  * Open Horizon administrators can use Open Horizon features to allow an individual to modify or correct their data.
  * Open Horizon administrators can use Open Horizon features to correct an individual's data for them.
* Right to restrict processing
  * Open Horizon administrators can use Open Horizon features to stop processing an individual's data.

## Appendix - Data logged by Open Horizon {: #appendix }

As an application, Open Horizon deals with several categories of technical data that might be considered as personal data:

* Administrator or operator user ID and password
* IP addresses
* Kubernetes node names.

Open Horizon also deals with information about users who manage the applications that run on Open Horizon and might introduce other categories of personal data that is unknown to the application.

### Open Horizon security

* What data is logged
  * User ID, username, and IP address of logged in users
* When data is logged
  * With login requests
* Where data is logged
  * In the audit logs at `/var/lib/icp/audit`???
  * In the audit logs at `/var/log/audit`???
  * Exchange logs at ???
* How to delete data
  * Search for the data and delete the record from the audit log

### Open Horizon API

* What data is logged
  * User ID, username, and IP address of client in container logs
  * Kubernetes cluster state data in the `etcd` server
  * OpenStack and VMware credentials in the `etcd` server
* When data is logged
  * With API requests
  * Credentials stored from `credentials-set` command
* Where data is logged
  * In container logs, Elasticsearch, and `etcd` server.
* How to delete data
  * Delete container logs (`platform-api`, `platform-deploy`) from containers or delete the user-specific log entries from Elasticsearch.
  * Clear the selected `etcd` key-value pairs by using the `etcdctl rm` command.
  * Remove credentials by calling the `credentials-unset` command.

For more information, see:

* [Kubernetes Logging ](https://kubernetes.io/docs/concepts/cluster-administration/logging/)
* [etcdctl ](https://github.com/coreos/etcd/blob/master/etcdctl/READMEv2.md)

### Open Horizon monitoring

* What data is logged
  * IP address, names of pods, release, image
  * Data scraped from client-developed applications might include personal data
* When data is logged
  * When Prometheus scrapes metrics from configured targets
* Where data is logged
  * In the Prometheus server or configured persistent volumes
* How to delete data
  * Search for and delete data by using the Prometheus API

For more information, see [Prometheus Documentation ](https://prometheus.io/docs/introduction/overview/).

### Open Horizon Kubernetes

* What data is logged
  * Cluster-deployed topology (node information for controller, worker, proxy, and va)
  * Service configuration (k8s configuration map) and secrets (k8s secrets)
  * User ID in apiserver log
* When data is logged
  * When you deploy a cluster
  * When you deploy an application from the Helm catalog
* Where data is logged
  * Cluster deployed topology in `etcd`
  * Configuration and secret for deployed applications in `etcd`
* How to delete data
  * Use the Open Horizon management console
  * Search for and delete data by using the k8s management console (`kubectl`) or `etcd` REST API
  * Search for and delete apiserver log data by using the Elasticsearch API

Use care when you are modifying Kubernetes cluster configuration or deleting cluster data.

For more information, see [Kubernetes kubectl ](https://kubernetes.io/docs/reference/kubectl/overview/).

### Open Horizon Helm API

* What data is logged
  * Username and role
* When data is logged
  * When a user retrieves charts or repositories that are added to a team
* Where data is logged
  * helm-api deployment logs, Elasticsearch
* How to delete data
  * Search for and delete helm-api log data by using the Elasticsearch API

### Open Horizon Service Broker

* What data is logged
  * User ID (only at debug log level 10, not at default log level)
* When data is logged
  * When API requests are made to the service broker
  * When the service broker accesses the service catalog
* Where data is logged
  * Service broker container log, Elasticsearch
* How to delete data
  * Search for and delete the apiserver log that uses Elasticsearch API
  * Search for and delete the log from the apiserver container

    ```bash
    kubectl logs $(kubectl get pods -n kube-system | grep  service-catalogapiserver | awk '{print $1}') -n kube-system | grep admin
    ```

For more information, see [Kubernetes kubectl ](https://kubernetes.io/docs/reference/kubectl/overview/).
