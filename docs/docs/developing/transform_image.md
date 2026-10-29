---
copyright: Contributors to the Open Horizon project
years: 2020 - 2026
title: Transform image to edge service
description: Documentation for Transform image to edge service
lastupdated: 2025-05-03
nav_order: 2
parent: Edge services for devices
grand_parent: Developing edge services
---

# Transform image to edge service

This example guides you through the steps to publish an existing Docker&reg; image as an edge service, create an associated deployment pattern, and register your edge nodes to run that deployment pattern.

## Before you begin

Complete the prerequisite steps in [Preparing to create an edge service](service_containers.md). As a result, these environment variables should be set, these commands should be installed, and these files should exist:

```bash
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID"
which git jq
ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem
cat /etc/default/horizon
```

## Procedure

**Note**: See [Conventions used in this document](../getting_started/document_conventions.md) for more information about command syntax.

1. Create a project directory.

   1. On your development host, change to your existing Docker project directory. **If you don't have an existing Docker&reg; project, but still want to continue with this example**, use these commands to create a simple Dockerfile that can be used with the rest of this procedure:

   ```bash
   cat << EndOfContent > Dockerfile
   FROM alpine:latest
   CMD while :; do echo "Hello, world."; sleep 3; done
   EndOfContent
   ```

   2. Create edge service metadata for your project:

   ```bash
   hzn dev service new -s myservice -V 1.0.0 -i $DOCKER_HUB_ID/myservice --noImageGen
   ```

   This command creates **horizon/service.definition.json** to describe your service and **horizon/pattern.json** to describe the deployment pattern. You can open these files and browse their content.

2. Build and test your service.

   1. Build your docker image. The image name must match what is referenced in **horizon/service.definition.json**.

   ```bash
   eval $(hzn util configconv -f horizon/hzn.json)
   export ARCH=$(hzn architecture)
   sudo docker build -t "${DOCKER_IMAGE_BASE}_$ARCH:$SERVICE_VERSION" .
   unset DOCKER_IMAGE_BASE SERVICE_NAME SERVICE_VERSION
   ```

   2. Run this service container image in the Horizon simulated agent environment:

   ```bash
   hzn dev service start -S
   ```

   3. Verify that your service container is running:

   ```bash
   sudo docker ps
   ```

   4. View the environment variables that were passed to the container when it was started. (These are the same environment variables that the full agent passes to the service container.)

   ```bash
   sudo docker inspect $(sudo docker ps -q --filter name=myservice) | jq '.[0].Config.Env'
   ```

   5. View the service container log:

   On **Linux**:

   ```bash
   sudo tail -f /var/log/syslog | grep myservice[[]
   ```

   On **macOS**:

   ```bash
   sudo docker logs -f $(sudo docker ps -q --filter name=myservice)
   ```

   6. Stop the service:

   ```bash
   hzn dev service stop
   ```

3. Publish your service to Open Horizon. Now that you verified that your service code runs as expected in the simulated agent environment, publish the service to Horizon exchange so that it becomes available for deployment to your edge nodes.

   The following **publish** command uses the **horizon/service.definition.json** file and your key pair to sign and publish your service to Horizon exchange. It also pushes your image to Docker&reg; Hub.

   ```bash
   hzn exchange service publish -f horizon/service.definition.json
   hzn exchange service list
   ```

4. Publish a deployment pattern for the service. This deployment pattern can be used by edge nodes to cause Open Horizon to deploy the service to them:

   ```bash
   hzn exchange pattern publish -f horizon/pattern.json
   hzn exchange pattern list
   ```

5. Register your edge node to run your deployment pattern.

   1. In the same way that you previously registered edge nodes with public deployment patterns from the **IBM** organization, register your edge node with the deployment pattern you published under your own organization:

   ```bash
   hzn register -p pattern-myservice-$(hzn architecture) -s myservice --serviceorg $HZN_ORG_ID
   ```

   2. List the docker container edge service that has been started as a result:

   ```bash
   sudo docker ps
   ```

   3. View the myservice edge service output:

   ```bash
   sudo hzn service log -f myservice
   ```

6. View the node, service, and pattern that you have created in the Open Horizon console. You can display the console URL with:

   ```bash
   echo "$(awk -F '=|edge-exchange' '/^HZN_EXCHANGE_URL/ {print $2}' /etc/default/horizon)edge"
   ```

7. Unregister your edge node and stop the **myservice** service:

   ```bash
   hzn unregister -f
   ```

## What to do next

* Try the other edge service examples at [Developing edge services with Open Horizon](developing.md).
