---

copyright:
years: 2021
lastupdated: "2021-07-20"
title: "Secrets Manager"
description: "Overview of Secrets Manager"

nav_order: 5
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Overview of Secrets Manager
{: #overviewofsm}

Services deployed to the edge often require access to cloud services, which means the service needs credentials to authenticate to the cloud service. The Secrets Manager provides a secure mechanism which allows credentials to be stored, deployed and managed without exposing the details within {{site.data.keyword.ieam}} metadata (e.g. service definitions and policies), or to other users in the system that should not have access to the secret. The Secrets Manager is a pluggable component of {{site.data.keyword.ieam}}. Currently, HashiCorp Vault is the only supported Secrets Manager.

A secret is a userid/password, certificate, RSA key, or any other credential that grants access to a protected resource which an edge application needs in order to perform it's function. Secrets are stored in the Secrets Manager. A secret has a name, which is used to identify the secret, but which provides no information about the details of the secret itself. Secrets are administered by the {{site.data.keyword.ieam}} CLI or by an administrator, using the Secrets Manager's UI or CLI.

A service developer declares the need for a secret within an {{site.data.keyword.ieam}} service definition. The service deployer attaches (or binds) a secret from the Secrets Manager to the deployment of the service, by associating the service with a secret from the Secrets Manager. For example; suppose a developer needs to access to the XYZ cloud service via basic auth. The developer updates the {{site.data.keyword.ieam}} service definition to include a secret called myCloudServiceCred. The service deployer sees that the service requires a secret in order to deploy it, and is aware of a secret in the Secrets Manager named cloudServiceXYZSecret that contains basic auth credentials. The service deployer updates the deployment policy (or pattern) to indicate that the service's secret named myCloudServiceCreds should contain the credentials from the Secrets Manager secret named cloudServiceXYZSecret. When the service deployer publishes the deployment policy (or pattern), {{site.data.keyword.ieam}} will securely deploy the details of cloudServiceXYZSecret to all edge nodes that are compatible with the deployment policy (or pattern).
