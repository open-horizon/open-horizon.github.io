# Transform image to edge service

This example guides you through the steps to publish an existing Docker® image as an edge service, create an associated deployment pattern, and register your edge nodes to run that deployment pattern.

## Before you begin

Complete the prerequisite steps in [Preparing to create an edge service](https://open-horizon.github.io/docs/developing/service_containers/index.md). As a result, these environment variables should be set, these commands should be installed, and these files should exist:

```
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID"
which git jq
ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem
cat /etc/default/horizon
```

## Procedure

**Note**: See [Conventions used in this document](https://open-horizon.github.io/docs/getting_started/document_conventions/index.md) for more information about command syntax.

1. Create a project directory.
1. On your development host, change to your existing Docker project directory. **If you don't have an existing Docker® project, but still want to continue with this example**, use these commands to create a simple Dockerfile that can be used with the rest of this procedure:

```
cat << EndOfContent > Dockerfile
FROM alpine:latest
CMD while :; do echo "Hello, world."; sleep 3; done
EndOfContent
```

1. Create edge service metadata for your project:

```
hzn dev service new -s myservice -V 1.0.0 -i $DOCKER_HUB_ID/myservice --noImageGen
```

This command creates **horizon/service.definition.json** to describe your service and **horizon/pattern.json** to describe the deployment pattern. You can open these files and browse their content.

1. Build and test your service.
1. Build your docker image. The image name must match what is referenced in **horizon/service.definition.json**.

```
eval $(hzn util configconv -f horizon/hzn.json)
export ARCH=$(hzn architecture)
sudo docker build -t "${DOCKER_IMAGE_BASE}_$ARCH:$SERVICE_VERSION" .
unset DOCKER_IMAGE_BASE SERVICE_NAME SERVICE_VERSION
```

1. Run this service container image in the Horizon simulated agent environment:

```
hzn dev service start -S
```

1. Verify that your service container is running:

```
sudo docker ps
```

1. View the environment variables that were passed to the container when it was started. (These are the same environment variables that the full agent passes to the service container.)

```
sudo docker inspect $(sudo docker ps -q --filter name=myservice) | jq '.[0].Config.Env'
```

1. View the service container log:

On **Linux**:

```
sudo tail -f /var/log/syslog | grep myservice[[]
```

On **macOS**:

```
sudo docker logs -f $(sudo docker ps -q --filter name=myservice)
```

1. Stop the service:

```
hzn dev service stop
```

1. Publish your service to Open Horizon. Now that you verified that your service code runs as expected in the simulated agent environment, publish the service to Horizon exchange so that it becomes available for deployment to your edge nodes.

The following **publish** command uses the **horizon/service.definition.json** file and your key pair to sign and publish your service to Horizon exchange. It also pushes your image to Docker® Hub.

```
hzn exchange service publish -f horizon/service.definition.json
hzn exchange service list
```

1. Publish a deployment pattern for the service. This deployment pattern can be used by edge nodes to cause Open Horizon to deploy the service to them:

```
hzn exchange pattern publish -f horizon/pattern.json
hzn exchange pattern list
```

1. Register your edge node to run your deployment pattern.
1. In the same way that you previously registered edge nodes with public deployment patterns from the **IBM** organization, register your edge node with the deployment pattern you published under your own organization:

```
hzn register -p pattern-myservice-$(hzn architecture) -s myservice --serviceorg $HZN_ORG_ID
```

1. List the docker container edge service that has been started as a result:

```
sudo docker ps
```

1. View the myservice edge service output:

```
sudo hzn service log -f myservice
```

1. View the node, service, and pattern that you have created in the Open Horizon console. You can display the console URL with:

```
echo "$(awk -F '=|edge-exchange' '/^HZN_EXCHANGE_URL/ {print $2}' /etc/default/horizon)edge"
```

1. Unregister your edge node and stop the **myservice** service:

```
hzn unregister -f
```

## What to do next

- Try the other edge service examples at [Developing edge services with Open Horizon](https://open-horizon.github.io/docs/developing/developing/index.md).
