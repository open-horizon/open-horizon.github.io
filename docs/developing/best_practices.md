---

copyright:
years: 2021
lastupdated: "2021-02-20"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Edge-native development best practices
{: #edge_native_practices}

You will be creating workloads that will operate in the edge – at compute facilities that exist outside the normal confines of your IT data center or cloud environment. That means you need to consider the unique conditions of those environments. This is referred to as the edge-native programming model.

## Best practices for developing edge services
{: #best_practices}

The following best practices and guidelines help you design and develop edge services for use with {{site.data.keyword.edge_notm}} ({{site.data.keyword.edge_abbr}}).
{:shortdesc}

Automating the running of services at the edge is different from automating services in the cloud in the following ways:

* The number of edge nodes can be much greater.
* The networks to edge nodes can be unreliable and much slower. Edge nodes are often behind firewalls so connections usually cannot be initiated from the cloud to the edge nodes.
* Edge nodes are resource-constrained.
* A driving force behind operating workloads at the edge is the ability to reduce latency and optimize network bandwidth. This makes workload placement in relation to where data is generated an important factor. 
* Typically, edge nodes are in remote locations and are not set up by operations staff. After an edge node is set up, staff might not be available to administer the node.
* Edge nodes are also usually less trusted environments than cloud servers.

These differences require different techniques to deploy and manage software on edge nodes. {{site.data.keyword.edge_abbr}} is designed for managing edge nodes. When you are creating services, adhere to the following guidelines to ensure that your services are designed for working with edge nodes.

## Guidelines for developing services
{: #service_guidelines}


* **Cloud-native programming model:** The edge-native programming model inherits many principles from cloud-native programming, including:

  * Componentize and containerize your workloads – construct your application around a set of microservices, each packaged into logically related groups, but balance that grouping to recognize where different containers might operate best at different tiers or edge nodes.
  * Expose APIs to your microservices that enable other parts of your application to find the services they depend on.
  * Design loose-coupling between microservices to enable them to operate independently of each other, and to avoid stateful assumptions that impose affinities between services that would otherwise undermine elastic scaling, failover, and recovery.
  * Exercise continuous-integration and continuous-deployment (CI/CD), coupled with Agile Development practices within a DevOps framework.
  * Consider the following resources for more information about cloud-native programming practices:
    * [10 KEY ATTRIBUTES OF CLOUD-NATIVE APPLICATIONS](https://thenewstack.io/10-key-attributes-of-cloud-native-applications/)
    * [Cloud Native Programming](https://researcher.watson.ibm.com/researcher/view_group.php?id=9957)
    *	[Understanding cloud-native applications](https://www.redhat.com/en/topics/cloud-native-apps)

* **Service availability:** If your service container requires and uses other service containers, your service must be tolerant when those services are absent in some situations. For example, when containers initially start, even though they are started from the end of the dependency graph, moving upward, some services can start more quickly than others. In this situation, your service containers need to retry while they wait for the dependencies to be fully functional. Similarly, if a dependent service container is automatically updated, then it is restarted. It is a best practice for your services to always be tolerant of interruptions in the services they depend on.
* **Portability:** The world of edge computing spans multiple tiers of the system – including edge devices, edge clusters, and network or metro edge locations. Where your containerized edge workload will eventually be placed depend on a combination of factors, including its dependence on certain resources, such as sensor data and actuators, end latency requirements, and available compute capacity. You should design your workload to tolerate being placed in different tiers of the system depending on the needs of the context in which your application will be used.
* **Container orchestration:** Further to the previous point about multi-tier portability; typically edge devices will be operated with native Docker runtime – with no local container orchestration. Edge clusters and network/metro edges will be configured with Kubernetes to orchestrate the workload against shared competing resource demands. You should implement your container to avoid any explicit dependence on either Docker or Kubernetes to enable its portability to different tiers of the distributed edge computing world. 
* **Externalize configuration parameters:** Use the built-in support provided by {{site.data.keyword.ieam}} to externalize any configuration variables and resource dependencies so that these can be supplied and updated to values that are specific to the node to which your container is deployed.
* **Secure secrets:** Edge services often require integration with on-prem or cloud based services, which require authentication credentials. Exploit the [secrets manager](secrets_details.md) to securely deploy sensitive information to edge nodes.
* **Size considerations:** Your service containers must be as small as possible so that the services can be deployed over potentially slow networks or to small edge devices. To help you develop smaller service containers, use the following techniques:

  * Use programming languages that can help you build smaller services:
    * Best: go, rust, c, sh
    * OK: c++, python, bash
    * Consider: nodejs, Java and JVM-based languages, such as scala
  * Use techniques that can help you construct smaller Docker images:
    * Use alpine as the base image for {{site.data.keyword.linux_notm}}.
    * To install packages in an alpine-based image, use the command `apk --no-cache --update add` to avoid storing the package cache, which is not needed for runtime.
    * Delete files in the same Dockerfile layer (command) where the files are added. If you use a separate Dockerfile command line to delete the files from the image, you increase the size of the container image. For example, you can use `&&` to group the commands to download, use, and then delete files, all within a single Dockerfile `RUN` command.
    * Do not include build tools in your runtime Docker image. As a best practice, use a [Docker Multi-stage build](https://docs.docker.com/develop/develop-images/multistage-build/) to build the runtime artifacts. Then, selectively copy the required runtime artifacts, such as the executable components, into your runtime Docker image.
* **Keep services self-contained:** Because a service needs to be sent over a network to edge nodes and autonomously started, the service container needs to include everything that the service depends upon. You need to bundle these assets, such as all required certificates, into the container. Do not rely on the availability of administrators for completing tasks to add any required assets to the edge node for a service to run successfully.
* **Data privacy:** Each time that you move private and sensitive data around the network, you increase the vulnerability of that data to attack and exposure. Edge computing offers, as one of its major benefits, the opportunity to keep that data where it is created. Respect that opportunity in your container by protecting it. Ideally, do not pass that data to other services. If you absolutely must pass data to other services or tiers in the system, attempt to remove personally identifying information (PII), personal health information (PHI), or personal financial information (PFI) through obfuscation or de-identification techniques or by encrypting it with a key that is owned entirely within the confines of your service. 
* **Design and configure for automation:** Edge nodes, and the services that run on the nodes, need to be as close to zero-ops as possible. {{site.data.keyword.ieam}} automates the deployment and management of services, but the services must be structured to enable {{site.data.keyword.ieam}} to be able to automate these processes without human intervention. To help design for automation, adhere to the following guidelines:
  * Limit the number of user input variables for a service. Any UserInput variables without default values in the service definition require that values be specified for each edge node. Limit the number of variables, or avoid services that use variables, whenever possible.  
  * If a service requires many configurable settings, use a configuration file for defining the variables. Include a default version of the configuration file within the service container. Then, use the {{site.data.keyword.ieam}} model management system to enable the administrator to provide their own configuration file and update it over time.
  * **Leverage standard platform services:** Many of your application needs can be met by pre-implemented platform services. Rather than creating these capabilities from scratch in your application, consider using what has already been created and is available to you. One source of such platform services includes the IBM Cloud Pak, which covers a wide range of capabilities, many of which have, themselves, been built using cloud-native programming practices, such as:
    * **Data Management:** consider IBM Cloud Pak for Data for your SQL and non-SQL, block, and object storage database requirements; machine learning and AI services, and data lake needs. 
    * **Security:** consider IBM CloudPak for Security for your encryption, code scanning, and intrusion detection needs.
    * **Applications:** consider IBM Cloud Pak for Applications for your web application, serverless, and application framework needs.
