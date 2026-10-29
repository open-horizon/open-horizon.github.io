# Developing an edge service for devices

To begin developing edge services for Open Horizon (Open Horizon), you need to first set up your credentials for publishing content. Because all services must be signed, you must also create a cryptographic signing key pair. Make sure to complete the prerequisite steps, [Preparing to create an edge service](https://open-horizon.github.io/docs/developing/service_containers/index.md).

This diagram shows the typical interactions between the components within Horizon.

## Examples

Use your credentials and signing keys to complete the development examples. These examples show you how to build simple services and help you learn about Open Horizon development basics.

Each of these development examples demonstrates a few more aspects of developing edge services. For an optimum learning experience, complete the examples in the order they are listed here.

- [Transform image to edge service](https://open-horizon.github.io/docs/developing/transform_image/index.md) - Demonstrates deploying an existing docker image as an edge service.
- [Creating your own hello world edge service](https://open-horizon.github.io/docs/developing/developingstart_example/index.md) - Demonstrates the basics of developing, testing, publishing, and deploying an edge service.
- [CPU to Apache Kafka service](https://open-horizon.github.io/docs/developing/cpu_msg_example/index.md) - Demonstrates how to define edge service configuration parameters, specify that your edge service requires other edge services, and send data to a cloud data ingest service.
- [Hello world using model management](https://open-horizon.github.io/docs/developing/model_management_system/index.md) - Demonstrates how to develop an edge service that uses the model management service. The model management service asynchronously provides file updates to edge services on edge nodes, for example to dynamically update a machine learning model each time it evolves.
- [Hello world using secrets](https://open-horizon.github.io/docs/secrets/examples/index.md) - Demonstrates how to develop an edge service that uses secrets. Secrets are used to protect sensitive data like login credentials or private keys. Secrets are deployed securely to services running on the edge.
- [Updating an edge service with rollback](https://open-horizon.github.io/docs/using_edge_services/service_rollbacks/index.md) - Demonstrates how to monitor the success of the deployment, and if it fails on any edge node, revert the node back to the previous version of the edge service.

After you finish building these example services, review the following documentation for more detailed information about developing services for Open Horizon:

## Further reading

Review the important principles and best practices for Open Horizon software development.

- [Edge-native development best practices](https://open-horizon.github.io/docs/developing/best_practices/index.md)

With Open Horizon, you can optionally put service container images into the IBM private secure container registry instead of the public Docker® Hub. For example, if you have a software image that includes assets that are not appropriate to include in a public registry.

- [Using a private container registry](https://open-horizon.github.io/docs/developing/container_registry/index.md)

You can Open Horizon use to put your service containers into the IBM private secure container registry instead of the public Docker® Hub.

- [Development details](https://open-horizon.github.io/docs/developing/developing_details/index.md)

With Open Horizon, you can develop any service containers that you want for your edge machines.

- [APIs](https://open-horizon.github.io/docs/api/index.md)

Open Horizon provides RESTful APIs for enabling components to collaborate, and to enable your organization's developers and users to control the components.
