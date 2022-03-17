---

copyright:
years: 2020 - 2022
lastupdated: "2022-03-17"

---

{:shortdesc: .shortdesc}
{:new_window: target="_blank"}
{:codeblock: .codeblock}
{:pre: .pre}
{:screen: .screen}
{:tip: .tip}
{:download: .download}

# Developing a Kubernetes operator
{: #kubernetes_operator}

In general, developing a service to run in an edge cluster is similar to developing an edge service that runs on an edge device. The edge service is developed by using [Edge-native development best practices](best_practices.md) development, and it is packaged in a container. The difference is in how the edge service is deployed.

To deploy a containerized edge service to an edge cluster, a developer must first build a Kubernetes operator that deploys the containerized edge service in a Kubernetes cluster. After the operator is written and tested, the developer creates and publishes the operator as an {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) service. This process enables an {{site.data.keyword.ieam}} administrator to deploy the operator service as would be done for any {{site.data.keyword.ieam}} service, with policy or patterns. There is no need to create an {{site.data.keyword.ieam}} service definition for the edge service. When the {{site.data.keyword.ieam}} administrator deploys the operator service, the operator deploys the edge service.

Several sources of information are available when you write a Kubernetes operator. First, read [Kubernetes Concepts - Operator pattern ](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/){:target="_blank"}{: .externalLink}. This site is a good resource to learn about operators. After you are familiar with the operator concepts, writing an operator is accomplished by using the [Operator Framework ](https://operatorframework.io/){:target="_blank"}{: .externalLink}. This web site provides more details about what an operator is and gives a walk-through for creating a simple operator, using the operator Software Development Kit (SDK).

## Considerations when developing an operator for {{site.data.keyword.ieam}}

It is a best practice to make liberal use of the operator's status capability because {{site.data.keyword.ieam}} reports whatever status the operator creates into the {{site.data.keyword.ieam}} management hub. When writing an operator, the operator-framework generates a Kubernetes Custom Resource Definition (CRD) for the operator. Every operator CRD has a status object that should be populated with important status information about the state of the operator and the edge service it is deploying. This is not done automatically by Kubernetes; it needs to be written into the implementation of the operator by the operator developer. The {{site.data.keyword.ieam}} agent in an edge cluster periodically gathers operator status and reports it to the management hub.

The operator can choose to attach the service-specific {{site.data.keyword.ieam}} environment variables to any services that it starts. When the operator is started, the {{site.data.keyword.ieam}} agent creates a Kubernetes configmap called `hzn-env-vars` that contains the service-specific environment variables. The operator can optionally attach that config map to any deployments that it creates, which enables services that it starts to recognize the same service-specific environment variables. These are the same environment variables that are injected into services that run on edge devices. The only exception is the ESS* environment variables because the Model Management System (MMS) is not yet supported for edge cluster services.

If wanted, operators that are deployed by {{site.data.keyword.ieam}} can be deployed into a namespace other than the default namespace. This is accomplished by the operator developer modifying the operator yaml files to point to the namespace. There are two ways to accomplish this:

* Modify the operator's Deployment definition (usually called **./deploy/operator.yaml**) to specify a namespace

or

* Include a namespace definition yaml file with the operator's yaml definition files; for example, in the operator project's **./deploy** directory.

**Note**: When an operator is deployed into a non-default namespace, {{site.data.keyword.ieam}} creates the namespace if it does not exist and removes it when the operator is undeployed by {{site.data.keyword.ieam}}.

## Packaging an operator for {{site.data.keyword.ieam}}

After an operator is written and tested, it needs to be packaged for deployment by {{site.data.keyword.ieam}}:

1. Ensure that the operator is packaged to run as a deployment inside a cluster. This means that the operator is built into a container and pushed to the container registry from which the container is retrieved when deployed by {{site.data.keyword.ieam}}. Typically, this is accomplished by building the operator by using the **operator-sdk build** followed by **docker push** commands. This is described in [Operator Tutorial ](https://sdk.operatorframework.io/docs/building-operators/golang/tutorial/#2-run-as-a-deployment-inside-the-cluster){:target="_blank"}{: .externalLink}..

2. Ensure the service container or containers that are deployed by the operator are also pushed to the registry from which the operator will deploy them.

3. Create an archive that contains the operator's yaml definition files from the operator project:

   ```bash
   cd <operator-project>/<operator-name>/deploy
   tar -zcvf <archive-name>.tar.gz ./*
   ```
   {: codeblock}

   **Note**: For {{site.data.keyword.macos_notm}} users, consider creating a clean archive tar.gz file to ensure that no hidden files exist in the tar.gz file. For example, a .DS_store file can cause problems when you deploy a helm operator. If you suspect that a hidden file exists, extract the tar.gz on your {{site.data.keyword.linux_notm}} system. For more information, see [Tar command in macos ](https://stackoverflow.com/questions/8766730/tar-command-in-mac-os-x-adding-hidden-files-why){:target="_blank"}{: .externalLink}.

   ```bash
   tar -xzpvf x.tar --exclude=".*"
   ```
   {: codeblock}

4. Use the {{site.data.keyword.ieam}} service creation tools to create a service definition for the operator service, for example:

   1. Create a new project:

      ```bash
      hzn dev service new -V <a version> -s <a service name> -c cluster
      ```
      {: codeblock}

   2. Edit the **horizon/service.definition.json** file to point to the operator's yaml archive created previously in step 3.

   3. Create a service signing key, or use one you have already created.

   4. Publish the service

      ```
      hzn exchange service publish -k <signing key> -f ./horizon/service.definition.json
      ```
      {: codeblock}

5. Create a deployment policy or pattern to deploy the operator service to an edge cluster.
