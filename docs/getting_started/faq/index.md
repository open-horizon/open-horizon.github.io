# Frequently asked questions

The following are answers to some frequently asked questions (FAQs) about Open Horizon (Open Horizon).

- [Is there a way to create a self-contained environment for development purposes?](#one_click)
- [Is Open Horizon software open-sourced?](#open_sourced)
- [How can I use Open Horizon to develop and deploy edge services?](#dev_dep)
- [What edge node hardware platforms does Open Horizon support?](#hw_plat)
- [Can I run any Linux distribution on my edge nodes with Open Horizon?](#lin_dist)
- [Which programming languages and environments are supported by Open Horizon?](#pro_env)
- [Is there detailed documentation for the REST APIs provided by the components in Open Horizon?](#rest_doc)
- [Does Open Horizon use Kubernetes?](#use_kube)
- [Does Open Horizon use MQTT?](#use_mqtt)
- [How long does it normally take after I register an edge node before agreements are formed and the corresponding containers start running?](#agree_run)
- [Can the Horizon software and all other software or data that is related to Open Horizon be removed from an edge node host?](#sw_rem)
- [Is there a dashboard for visualizing the agreements and services that are active on an edge node?](#db_node)
- [What happens if a container image download is interrupted by a network outage?](#image_download)
- [How is Open Horizon secure?](#ieam_secure)
- [How do I manage AI at the Edge with models vs AI on the Cloud?](#ai_cloud)
- [How can I include text in an Open Horizon resource that contains a `$` character?](#env_variable)

## Is there a way to create a self-contained environment for development purposes?

You can install the open source management hub with the All-in-One installer for developers. The All-in-One installer creates a complete but minimal management hub, not suitable for production use. It also configures an example edge node. This tool enables open source component developers to get started quickly without the time it takes to configure a complete production Open Horizon management hub. For information about the All-in-One installer, see [Open Horizon - Devops](https://github.com/open-horizon/devops/tree/master/mgmt-hub) GitHub repository.

The All-in-One installer publishes a default set of sample services during deployment. You can customize which sample services are published by setting the `BYO_SAMPLES` environment variable to point to a text file that contains GitHub URLs of your own service repositories. This enables you to test and develop with your own custom services in addition to the default samples. For detailed instructions, see the [Using Custom Sample Services](https://open-horizon.github.io/docs/hub/custom_samples/index.md).

## Is Open Horizon software open-sourced?

Yes [Open Horizon](https://www.lfedge.org/projects/openhorizon/) is an open source project. For more information about the Open Horizon project see the [GitHub repository](https://github.com/openhorizon/) .

There are also commercial downstream products such as IBM® Edge Application Manager which is an IBM product whose core components heavily use the [Open Horizon](https://www.lfedge.org/projects/openhorizon/) open source project.

## How can I develop and deploy edge services with Open Horizon?

See [Using edge services](https://open-horizon.github.io/docs/using_edge_services/using_edge_services/index.md).

## What edge node hardware platforms does Open Horizon support?

Open Horizon supports different hardware architectures through the Debian Linux and RPM binary packages for Horizon or through Docker® or Podman containers. For more information, see [Installing Horizon software](https://open-horizon.github.io/docs/installing/installing_edge_nodes/index.md).

## Can I run any Linux distribution on my edge nodes with Open Horizon?

Yes, and no.

You can develop edge software that uses any Linux distribution as the base image of the Docker containers (if it uses the Dockerfile `FROM` statement) if that base functions on the host Linux kernel on your edge nodes. This means that you can use any distribution for your containers that Docker® is able to run on your edge hosts.

However, your edge node host operating system must be able to run a recent version of Docker or Podman and be able to run the Horizon software. Currently, the Horizon software is provided only as a Debian and RPM packages for edge nodes that run Linux. For some platforms, such as Apple Macintosh machines, a Docker® container version is provided. The Horizon development team primarily uses Apple Macintosh, or the Ubuntu or Raspberry Pi OS Linux distributions.

Additionally, RPM package installation was tested on edge nodes configured with Red Hat Enterprise Linux® (RHEL).

## Which programming languages and environments are supported by Open Horizon?

Open Horizon supports almost any programming language and software library that you are able to configure to run in an appropriate Docker® container on your edge nodes.

If your software requires access to specific hardware or operating system services, you might need to provide `docker run`-equivalent arguments to support that access. You can specify supported arguments within the `deployment` section of your Docker® container definition file.

## Is there detailed documentation for the REST APIs provided by the components in Open Horizon?

Yes. For more information, see [Open Horizon APIs](https://open-horizon.github.io/docs/api/index.md).

## Does Open Horizon use Kubernetes?

Yes. The Open Horizon management hub can run in a Kubernetes environment and Open Horizon supports an edge cluster agent that runs in Kubernetes. See [Installing edge clusters](https://open-horizon.github.io/docs/installing/edge_clusters/index.md).

## Does Open Horizon use MQTT?

Open Horizon does not use Message Queuing Telemetry Transport (MQTT) to support its own internal functions, however the programs you deploy on your edge nodes are free to use MQTT for their own purposes. Example programs are available that use MQTT and other technologies (for example, Apache Kafka, based on the Apache Kafka) to transport data to and from edge nodes.

## How long does it normally take after registering an edge node before agreements are formed, and the corresponding containers start running?

Typically, it takes under a minute after registration for the agent and a remote Agbot to finalize an agreement to deploy software. After that occurs, the Horizon agent downloads (`docker pull`) your containers to the edge node, verify their cryptographic signatures with Horizon exchange, and run them. Depending on the sizes of your containers, and the time it takes them to start and be functional, it can take from just a few more seconds, to many minutes before the edge node is fully operational.

After you have registered an edge node, you can run the `hzn node list` command to view the state of Horizon on your edge node. When the `hzn node list` command shows that the state is `configured`, the Horizon Agbots are able to discover the edge node and begin to form agreements.

To observe the agreement negotiation process phases, you can use the `hzn agreement list` command.

For an edge device agent, after an agreement list is finalized, you can use the `docker ps` or (`podman ps`) command to view the running containers. You can also issue `docker inspect <container>` (or `podman inspect <container>`) to see more detailed information about the deployment of any specific `<container>`.

## Can the Open Horizon software and all other software or data that is related to Open Horizon be removed from an edge node host?

Yes. If your edge node is registered, unregister the edge node by running:

```
hzn unregister -f -r
```

When the edge node is unregistered, you can remove the installed Open Horizon software. For example for Debian-based systems run:

```
sudo apt purge -y horizon horizon-cli
```

and for Red Hat Enterprise Linux® (RHEL)

```
sudo dnf remove  -y horizon horizon-cli
```

## Is there a dashboard for visualizing the agreements and services that are active on an edge node?

No. There is not a web UI to observe your edge nodes and services provided with Open Horizon.

However, you can use the `hzn` command to obtain information about the active agreements and services by using the local Open Horizon agent REST API on the edge node. Run the following commands to use the API to retrieve the related information:

```
hzn node list
hzn agreement list
```

## What happens if a container image download is interrupted by a network outage?

The docker API is used to download container images. If the docker API terminates the download, it returns an error to the agent. In turn, the agent cancels the current deployment attempt. When the Agbot detects the cancellation, it initiates a new deployment attempt with the agent. During the subsequent deployment attempt, the docker API resumes the download from where it left off. This process continues until the image is fully downloaded and the deployment can proceed. The docker binding API is responsible for the image pull, and in case of failure, the agreement is canceled.

## How is Open Horizon secure?

- Open Horizon automates and uses cryptographically signed public-private key authentication of edge devices as it communicates with the Open Horizon management hub during provisioning. Communication is always initiated and controlled by the edge node.
- System has node and service credentials.
- Software verification and authenticity using hash verification.

See [Security at the Edge](https://www.ibm.com/cloud/blog/security-at-the-edge) .

## How do I manage AI at the Edge with models vs AI on the Cloud?

Typically, AI at the edge enables you to perform on-the-spot machine inferencing with subsecond latency, which enables real-time response based on use case and hardware (for example, RaspberryPi, Intel® x86, ppc64le, and Nvidia Jetson nano). Open Horizon model management system enables you to deploy updated AI models without any service downtime.

See [Models Deployed at the Edge](https://www.ibm.com/cloud/blog/models-deployed-at-the-edge) .

## How can I include text in an Open Horizon resource that contains a `$` character?

When using `hzn` commands to publish resources like service definitions or deployment policies, the `hzn` CLI expects the `$` character to indicate an environment variable. To include text that actually includes the `$` character, you can use

```
export DOLLAR_CHAR=$
cat << EOF | hzn exchange business addpolicy MyPolicy -f- 
{
  "service": { "name": "my-service", "org": "myorg", "arch": "*", "serviceVersions": [ { "version": "1.0.0" } ] },
  "userInput": [
    {
      "serviceOrgid": "myorg",
      "serviceUrl": "my-service",
      "serviceVersionRange": "[0.0.0,INFINITY)",
      "inputs": [
        {
          "name": "ACCOUNT_PASSWORD",
          "value": "piDMB\${DOLLAR_CHAR}7C\${DOLLAR_CHAR}1zg"
        }
      ]
    }
  ],
  "constraints": [ "my_constraint == true" ]
}
EOF
```
