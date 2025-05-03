---
copyright: Contributors to the Open Horizon project
years: 2021 - 2025
title: Troubleshooting tips
description: Documentation for Troubleshooting tips
lastupdated: 2025-05-03
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Troubleshooting tips
{: #troubleshooting_devices}

Review the following questions when you encounter an issue with {{site.data.keyword.edge_notm}}. The tips and guides for each question can help you resolve common issues and obtain information to identify root causes.
{:shortdesc}

- [Are the currently released versions of the {{site.data.keyword.horizon}} packages installed?](#install_horizon)
- [Is the {{site.data.keyword.horizon}} agent currently up and actively running?](#setup_horizon)
- [Is the edge node configured to interact with the {{site.data.keyword.horizon_exchange}}?](#node_configured)
- [Are the required Docker containers started for the edge node running?](#node_running)
- [Are the expected service containers versions running?](#run_user_containers)
- [Are the expected containers stable?](#containers_stable)
- [Are your Docker containers networked correctly?](#container_networked)
- [Are the dependency containers reachable within the context of your container?](#setup_correct)
- [Are your user-defined containers emitting error messages to the log?](#log_user_container_errors)
- [Can you use your organization's instance of {{site.data.keyword.message_hub_notm}} Kafka broker?](#kafka_subscription)
- [Are your containers published to {{site.data.keyword.horizon_exchange}}?](#publish_containers)
- [Does your published deployment pattern include all required services and versions?](#services_included)
- [Troubleshooting tips specific to the {{site.data.keyword.open_shift_cp}} environment](#troubleshooting_icp)
- [Troubleshooting node errors](#troubleshooting_node_errors)
- [Are you encountering HTTP error, while executing deploy-mgmt-hub.sh?](#deploy_mgmt_http_error)

## Are the currently released versions of the {{site.data.keyword.horizon}} packages installed?
{: #install_horizon}

Ensure that the {{site.data.keyword.horizon}} software that is installed on your edge nodes is always on the latest released version.

On a {{site.data.keyword.linux_notm}} system, you can usually check the version of your installed {{site.data.keyword.horizon}} packages by running this command:

```bash
dpkg -l | grep horizon
```
{: codeblock}

You can update your {{site.data.keyword.horizon}} packages that use the package manager on your system. For example, on an Ubuntu-based {{site.data.keyword.linux_notm}} system, use the following commands to update {{site.data.keyword.horizon}} to the current version:

```bash
sudo apt update
sudo apt install -y blue horizon
```

## Is the {{site.data.keyword.horizon}} agent up and actively running?
{: #setup_horizon}

You can verify that the agent is running by using this {{site.data.keyword.horizon}} CLI command:

```bash
hzn node list | jq .
```
{: codeblock}

You can also use the host's system management software to check on the status of the {{site.data.keyword.horizon}} agent. For example, on an Ubuntu-based {{site.data.keyword.linux_notm}} system, you can use the `systemctl` utility:

```bash
sudo systemctl status horizon
```
{: codeblock}

A line similar to the following is shown if the agent is active:

```bash
Active: active (running) since Thu 2020-10-01 17:56:12 UTC; 2 weeks 0 days ago
```
{: codeblock}

## Is the edge node configured to interact with the {{site.data.keyword.horizon_exchange}}?
{: #node_configured}

To verify that you can communicate with the {{site.data.keyword.horizon_exchange}}, run this command:

```bash
hzn exchange version
```
{: codeblock}

To verify that your {{site.data.keyword.horizon_exchange}} is accessible, run this command:

```bash
hzn exchange user list
```
{: codeblock}

After your edge node is registered with {{site.data.keyword.horizon}}, you can verify whether the node is interacting with {{site.data.keyword.horizon_exchange}} by viewing the local {{site.data.keyword.horizon}} agent configuration. Run this command to view the agent configuration:

```bash
hzn node list | jq .configuration.exchange_api
```
{: codeblock}

## Are the required Docker containers for the edge node running?
{: #node_running}

When your edge node is registered with {{site.data.keyword.horizon}}, a {{site.data.keyword.horizon}} {{site.data.keyword.agbot}} creates an agreement with your edge node to run the services that are referenced in your gateway type (deployment pattern). If that agreement is not created, complete these checks to troubleshoot the issue.

Confirm that your edge node is in the `configured` state and has the correct `id`, `organization` values. Additionally, confirm that the architecture that {{site.data.keyword.horizon}} is reporting is the same architecture that you used in the metadata for your services. Run this command to list these settings:

```bash
hzn node list | jq .
```
{: codeblock}

If those values are as expected, you can check the agreement status of the edge node by run:

```bash
hzn agreement list | jq .
```
{: codeblock}

If this command does not show any agreements; those agreements might have formed, but a problem might have been discovered. If this occurs, the agreement can be cancelled before it can display in the output from the previous command. If an agreement cancellation occurs, the cancelled agreement shows a status of `terminated_description` in the list of archived agreements. You can view the archived list by running this command:

```bash
hzn agreement list -r | jq .
```
{: codeblock}

A problem might also occur before an agreement is created. If this problem occurs, review the event log for the {{site.data.keyword.horizon}} agent to identify possible errors. Run this command to view the log:

```bash
hzn eventlog list
```
{: codeblock}

The event log can include:

- The signature of the service metadata, specifically the `deployment` field, cannot be verified. This error usually means that your signing public key is not imported into your edge node. You can import the key by using the `hzn key import -k <pubkey>` command. You can view the keys that are imported to your local edge node by using the `hzn key list` command. You can verify that the service metadata in the {{site.data.keyword.horizon_exchange}} is signed with your key by using this command:

  ```bash
  hzn exchange service verify -k $PUBLIC_KEY_FILE <service-id>
  ```
  {: codeblock}

Replace `<service-id>` with the ID for your service. This ID can resemble the following sample format: `workload-cpu2wiotp_${CPU2WIOTP_VERSION}_${ARCH2}`.

- The path of Docker image in the service `deployment` field is incorrect. Confirm that your edge node can `docker pull` that image path.
- The {{site.data.keyword.horizon}} agent on your edge node does not have access to the Docker registry that holds your Docker images. If the Docker images in the remote Docker registry are not world-readable, you must add the credentials to your edge node by using the `docker login` command. You need to complete this step once as the credentials are remembered on the edge node.
- If a container is continually restarting, review the container log for details. A container can be continually restarting when it is listed for only a few seconds or remains listed as restarting when you run the `docker ps` command. You can view the container log for details by running this command:

  ```bash
  grep --text -E ' <service-id>\[[0-9]+\]' /var/log/syslog
  ```
  {: codeblock}

## Are the expected service container versions running?
{: #run_user_containers}

Your container versions are governed by an agreement that is created after you add your service to the deployment pattern, and after you register your edge node for that pattern. Verify that your edge node has a current agreement for your pattern, by running this command:

```bash
hzn agreement list | jq .
```
{: codeblock}

If you confirmed the correct agreement for your pattern, use this command to view the running containers. Ensure that your user-defined containers are listed and are running:

```bash
docker ps
```
{: codeblock}

The {{site.data.keyword.horizon}} agent can take several minutes after the agreement is accepted before the corresponding containers are downloaded, verified, and start to run. This agreement is mostly dependent upon the sizes of the containers themselves, which must be pulled from remote repositories.

## Are the expected containers stable?
{: #containers_stable}

Check whether your containers are stable by running this command:

```bash
docker ps
```
{: codeblock}

From the command output, you can see the duration that each container is running. If over time, you observe that your containers are restarting unexpectedly, check the container logs for errors.

As a development best practice, consider configuring individual service logging by running the following commands ({{site.data.keyword.linux_notm}} systems only):

```bash
cat <<'EOF' > /etc/rsyslog.d/10-horizon-docker.conf
$template DynamicWorkloadFile,"/var/log/workload/%syslogtag:R,ERE,1,DFLT:.*workload-([^\[]+)--end%.log"

:syslogtag, startswith, "workload-" -?DynamicWorkloadFile
& stop
:syslogtag, startswith, "docker/" -/var/log/docker_containers.log
& stop
:syslogtag, startswith, "docker" -/var/log/docker.log
& stop
EOF
service rsyslog restart
```
{: codeblock}

If you complete the previous step, then the logs for your containers are recorded within separate files inside the `/var/log/workload/` directory. Use the `docker ps` command to find the full names of your containers. You can find the log file of that name, with a `.log` suffix, in this directory.

If individual service logging is not configured, your service logs are added to the system log with all other log messages. To review the data for your containers, you need to search for the container name in the system log output within the `/var/log/syslog` file. For instance, you can search the log by running a command similar:

```bash
grep --text -E 'YOURSERVICENAME\[[0-9]+\]' /var/log/syslog
```
{: codeblock}

## Are your containers Docker networked correctly?
{: #container_networked}

Ensure that your containers are properly Docker networked, so they can access required services. Run this command to ensure that you can view the Docker virtual networks active on your edge node:

```bash
docker network list
```
{: codeblock}

To view more information about networks, use the `docker inspect X` command, where `X` is the name of the network. The command output lists all containers that run on the virtual network.

You can also run the `docker inspect Y` command on each container, where `Y` is the name of the container, to get more information. For instance, review the `NetworkSettings` container information and search the `Networks` container. Within this container, you can view the relevant network ID string and information about how the container is represented on the network. This representation information includes the container `IPAddress`, and the list of network aliases that are on this network.

Alias names are available to all of the containers on this virtual network, and these names are typically used by the containers in your code deployment pattern for discovering other containers on the virtual network. For example, you can name your service `myservice`. Then, other containers can use that name directly to access it on the network, such as with the command `ping myservice`. The alias name of your container is specified in the `deployment` field of its service definition file that you passed to the `hzn exchange service publish` command.

For more information about the commands supported by the Docker command line interface, see [Docker command reference ](https://docs.docker.com/engine/reference/commandline/docker/#child-commands){:target="_blank"}{: .externalLink}.

## Are the dependency containers reachable within the context of your container?
{: #setup_correct}

Enter the context of a running container to troubleshoot issues at run time by using the `docker exec` command. Use the `docker ps` command to find the identifier of your running container, then use a command that resembles the following to enter the context. Replace `CONTAINERID` with your container's identifier:

```bash
docker exec -it CONTAINERID /bin/sh
```
{: codeblock}

If your container includes bash, you might want to specify `/bin/bash` at the end of the preceding command instead of `/bin/sh`.

When inside the container context, you can use commands like `ping` or `curl` to interact with the containers it requires and verify connectivity.

For more information about the commands supported by the Docker command line interface, see [Docker command reference ](https://docs.docker.com/engine/reference/commandline/docker/#child-commands){:target="_blank"}{: .externalLink}.

## Are your user-defined containers emitting error messages to the log?
{: #log_user_container_errors}

If you configured individual service logging, each of your containers log in to a separate file within the `/var/log/workload/` directory. Use the `docker ps` command to find the full names of your containers. Then, look for a file of that name, and that includes the `.log` suffix, within this directory.

If individual service logging is not configured, your service logs to the system log with all other details. To review the data, search for the container log in the system log output within the `/var/log/syslog` directory. For instance, search the log by running a command similar to:

```bash
grep --text -E 'YOURSERVICENAME\[[0-9]+\]' /var/log/syslog
```
{: codeblock}

## Can you use your organization's instance of {{site.data.keyword.message_hub_notm}} Kafka broker?
{: #kafka_subscription}

Subscribing to the Kafka instance for your organization from {{site.data.keyword.message_hub_notm}} can help you verify that your Kafka user credentials are correct. This subscription can also help you verify that your Kafka service instance is running in the cloud, and that your edge node is sending data when data is being published.

To subscribe to your Kafka broker, install the `kafkacat` program. For example, on an Ubuntu {{site.data.keyword.linux_notm}} system, use this command:

```bash
sudo apt install kafkacat
```
{: codeblock}

After installation, you can subscribe by using a command similar following example that uses the credentials you usually place in environment variable references:

```bash
kafkacat -C -q -o end -f "%t/%p/%o/%k: %s\n" -b $EVTSTREAMS_BROKER_URL -X api.version.request=true -X security.protocol=sasl_ssl -X sasl.mechanisms=PLAIN -X sasl.username=token -X sasl.password=$EVTSTREAMS_API_KEY -t $EVTSTREAMS_TOPIC
```
{: codeblock}

Where `EVTSTREAMS_BROKER_URL` is the URL to your Kafka broker, `EVTSTREAMS_TOPIC` is your Kafka topic, and `EVTSTREAMS_API_KEY` is your API key for authenticating with {{site.data.keyword.message_hub_notm}} API.

If the subscription command is successful, the command blocks indefinitely. The command waits for any publication to your Kafka broker and retrieves and displays any resulting messages. If you do not see any messages from your edge node after a few minutes, review the service log for error messages.

For example, to review the log for the `cpu2evtstreams` service, run this command:

- For {{site.data.keyword.linux_notm}} and {{site.data.keyword.windows_notm}}

  ```bash
 tail -n 500 -f /var/log/syslog | grep -E 'cpu2evtstreams\[[0-9]+\]:'
  ```
  {: codeblock}

- For {{site.data.keyword.macOS_notm}}

  ```bash
  docker logs -f $(docker ps --filter 'name=-cpu2evtstreams' | tail -n +2 | awk '{print $1}')
  ```
  {: codeblock}

## Are your containers published to {{site.data.keyword.horizon_exchange}}?
{: #publish_containers}

{{site.data.keyword.horizon_exchange}} is the central warehouse for metadata about the code that is published for your edge nodes. If you have not signed and published your code to the {{site.data.keyword.horizon_exchange}}, the code cannot be pulled to your edge nodes, which are verified, and run.

Run the `hzn` command with the following arguments to view the list of published code to verify that all of your service containers were successfully published:

```bash
hzn exchange service list | jq .
hzn exchange service list $ORG_ID/$SERVICE | jq .
```
{: codeblock}

The parameter `$ORG_ID` is your organization ID, and `$SERVICE` is the name of the service you are obtaining information about.

## Does your published deployment pattern include all required services and versions?
{: #services_included}

On any edge node where the `hzn` command is installed, you can use this command to get details about any deployment pattern. Run the `hzn` command with the following arguments to pull the listing of deployment patterns from the {{site.data.keyword.horizon_exchange}}:

```bash
hzn exchange pattern list | jq .
hzn exchange pattern list $ORG_ID/$PATTERN | jq .
```
{: codeblock}

The parameter `$ORG_ID` is your organization ID, and `$PATTERN` is the name of the deployment pattern you are obtaining information about.

## Troubleshooting tips specific to the {{site.data.keyword.open_shift_cp}} environment
{: #troubleshooting_icp}

Review this content to help you troubleshoot common issues with {{site.data.keyword.open_shift_cp}} environments related to {{site.data.keyword.edge_notm}}. These tips can help you resolve common issues and obtain information to identify root causes.
{:shortdesc}

### Are your {{site.data.keyword.edge_notm}} credentials configured correctly for use in the {{site.data.keyword.open_shift_cp}} environment?
{: #setup_correct}

You need an {{site.data.keyword.open_shift_cp}} user account to complete any action within {{site.data.keyword.edge_notm}} in this environment. You also require an API key created from that account.

To verify your {{site.data.keyword.edge_notm}} credentials in this environment, run this command:

```bash
hzn exchange user list
```
{: codeblock}

If a JSON-formatted entry is returned from the Exchange showing one or more users, the {{site.data.keyword.edge_notm}} credentials are configured properly.

If an error response is returned, you can take steps to troubleshoot your credentials setup.

If the error message indicates an incorrect API key, you can create a new API key that uses the following commands.

See [Gather the necessary information and files](../hub/prepare_for_edge_nodes.md).

## Troubleshooting node errors
{: #troubleshooting_node_errors}

{{site.data.keyword.edge_notm}} publishes a subset of event logs to the exchange that is viewable in the {{site.data.keyword.gui}}. These errors link to troubleshooting guidance.
{:shortdesc}

- [Image load error](#eil)
- [Deployment configuration error](#eidc)
- [Container start error](#esc)
- [OCP edge cluster TLS internal error](#tls_internal)

### Image load error
{: #eil}

This error occurs when the service image that is referenced in the service definition does not exist in the image repository. To resolve this error:

1. Republish the service without the **-I** flag.

   ```bash
   hzn exchange service publish -f <service-definition-file>
   ```
   {: codeblock}

2. Push the service image directly to the image repository.

   ```bash
   docker push <image name>
   ```
   {: codeblock}

### Deployment configuration error
{: #eidc}

This error occurs when the service definitions deployment configurations specify a bind to a root-protected file. To resolve this error:

1. Bind the container to a file that is not root protected.
2. Change the file permissions to allow users to read and write to the file.

### Container start error
{: #esc}

This error occurs when docker encounters an error when it starts the service container. The error message might contain details that indicate why the container start failed. Error resolution steps depend on the error. The following errors can occur:

1. The device is already using a published port that is specified by the deployment configurations. To resolve the error:

   - Map a different port to the service container port. The displayed port number does not have to match the service port number.
   - Stop the program that is using the same port.

2. A published port that is specified by the deployment configurations is not a valid port number. Port numbers must be a number in the range 1 -  65535.
3. A volume name in the deployment configurations is not a valid file path. Volume paths must be specified by their absolute (not relative) paths.

## Are you encountering HTTP error, while executing deploy-mgmt-hub.sh?
{: #deploy_mgmt_http_error}

If you are encountering following error while executing `deploy-mgmt-hub.sh`

```bash
 ------- Downloading/installing/configuring Horizon agent and CLI...
Downloading the Horizon agent and CLI packages...
Installing the Horizon agent and CLI packages...
Configuring the Horizon agent and CLI...
Publishing /tmp/horizon-all-in-1/agent-install.cfg in CSS as public object agent-install.cfg in the IBM org...
Digital sign with SHA1 will be performed for data integrity. It will delay the MMS object publish.
Start hashing the file...
Data hash is generated. Start digital signing with the data hash...
Digital sign finished.
Error: Encountered HTTP error: Put "http://127.0.0.1:9443/api/v1/objects/IBM/agent_files/agent-install.cfg": read tcp 127.0.0.1:59088->127.0.0.1:9443: read: connection reset by peer calling Model Management Service REST API PUT http://127.0.0.1:9443/api/v1/objects/IBM/agent_files/agent-install.cfg. HTTP status: .
Error: exit code 5 from: publishing /tmp/horizon-all-in-1/agent-install.cfg in CSS as a public object
```

1. Export MONGO_IMAGE_TAG:
  
   ```bash
   export MONGO_IMAGE_TAG=4.0.6
   ```
   {: codeblock}

2. Stop and purge management hub services and agent:

   ```bash
   ./deploy-mgmt-hub.sh -S -P
   ```
   {: codeblock}

3. Re-Run deploy-mgmt-hub.sh as root:

   ```bash
   ./deploy-mgmt-hub.sh
   ```
   {: codeblock}

### {{site.data.keyword.ocp}} edge cluster TLS internal error

```bash
Error from server: error dialing backend: remote error: tls: internal error
```
{: codeblock}

If you see this error at the end of the cluster agent-install process or while trying to interact with the agent pod, there might be an issue with the Certificate Signing Requests (CSR) of your OCP cluster.

1. Check if you have any CSRs in the Pending state:

   ```bash
   oc get csr
   ```
   {: codeblock}

2. Approve the pending CSRs:

   ```bash
   oc adm certificate approve <csr-name>
   ```
   {: codeblock}

   **Note**: You can approve all of the CSRs with one command:

   ```bash
   for i in `oc get csr |grep Pending |awk '{print $1}'`; do oc adm certificate approve $i; done
   ```
   {: codeblock}

### Additional information

For more information, see:

- [Troubleshooting](../troubleshoot/troubleshooting.md)
