---

copyright:
years: 2022 - 2023
lastupdated: "2023-02-25"
title: "Installing the agent"

parent: Edge clusters
nav_order: 1
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Installing the agent
{: #importing_clusters}

**Note**: {{site.data.keyword.ieam}} agent installation requires cluster admin access on the edge cluster.
Additionally, the jq command-line JSON processor must be installed prior to running the agent install script.

Begin by installing the {{site.data.keyword.edge_notm}} agent on one of these types of Kubernetes edge clusters:

* [Installing agent on {{site.data.keyword.ocp}} Kubernetes edge cluster](#install_kube)
* [Installing agent on k3s and microk8s edge clusters](#install_lite)

Then, deploy an edge service to your edge cluster:

* [Deploying services to your edge cluster](#deploying_services)

If you need to remove the agent:

* [Removing agent from edge cluster](../using_edge_services/removing_agent_from_cluster.md)

## Installing agent on {{site.data.keyword.ocp}} Kubernetes edge cluster
{: #install_kube}

This content describes how to install the {{site.data.keyword.ieam}} agent on your {{site.data.keyword.ocp}} edge cluster. Follow these steps on a host that has admin access to your edge cluster:

1. Log in to your edge cluster as **admin**:

   ```bash
   oc login https://<api_endpoint_host>:<port> -u <admin_user> -p <admin_password> --insecure-skip-tls-verify=true
   ```
   {: codeblock}

2. If you have not completed the steps in [Creating your API key](../hub/prepare_for_edge_nodes.md), do that now. This process creates an API key, locates some files, and gathers environment variable values that are needed when you set up edge nodes. Set the same environment variables for this edge cluster.  Set the `HZN_NODE_ID` of the edge cluster.

   ```bash
   export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
   export HZN_ORG_ID=<your-exchange-organization>
   export HZN_FSS_CSSURL=https://<management-hub-ingress>/edge-css/
   export HZN_NODE_ID=<edge-cluster-node-name>
   ```
   {: codeblock}

3. Set the agent namespace variable to its default value (or whatever namespace you want to explicitly install the agent into):

   ```bash
   export AGENT_NAMESPACE=openhorizon-agent
   ```
   {: codeblock}

4. Set the storage class that you want the agent to use - either a built-in storage class or one that you created. You can view the available storage classes with the first of the following two commands, then substitute the name of the one you want to use into the second command. One storage class should be labeled `(default)`:

   ```bash
   oc get storageclass
   export EDGE_CLUSTER_STORAGE_CLASS=<rook-ceph-cephfs-internal>
   ```
   {: codeblock}

5. Determine whether a default route for the {{site.data.keyword.open_shift}} image registry has been created so that it is accessible from outside of the cluster:

   ```bash
   oc get route default-route -n openshift-image-registry --template='{{ .spec.host }}'
   ```
   {: codeblock}

   If the command response indicates the **default-route** is not found, you need to expose it (see [Exposing the registry ](https://docs.openshift.com/container-platform/4.6/registry/securing-exposing-registry.html){:target="_blank"}{: .externalLink} for details):

   ```bash
   oc patch configs.imageregistry.operator.openshift.io/cluster --patch '{"spec":{"defaultRoute":true}}' --type=merge
   ```
   {: codeblock}

6. Retrieve the repository route name that you need to use:

   ```bash
   export OCP_IMAGE_REGISTRY=`oc get route default-route -n openshift-image-registry --template='{{ .spec.host }}'`
   ```
   {: codeblock}

7. Create a new project to store your images:

   ```bash
   export OCP_PROJECT=$AGENT_NAMESPACE
   oc new-project $OCP_PROJECT
   ```
   {: codeblock}

8. Create a service account with a name of your choosing:

   ```bash
   export OCP_USER=<service-account-name>
   oc create serviceaccount $OCP_USER
   ```
   {: codeblock}

9. Add a role to your service account for the current project:

   ```bash
   oc policy add-role-to-user edit system:serviceaccount:$OCP_PROJECT:$OCP_USER
   ```
   {: codeblock}

10. Set your service account token to the following environment variable:

    ```bash
    export OCP_TOKEN=`oc serviceaccounts get-token $OCP_USER`
    ```
    {: codeblock}

11. Get the {{site.data.keyword.open_shift}} certificate and allow docker to trust it:

    ```bash
    echo | openssl s_client -connect $OCP_IMAGE_REGISTRY:443 -showcerts | sed -n "/-----BEGIN CERTIFICATE-----/,/-----END CERTIFICATE-----/p" > ca.crt
    ```
    {: codeblock}

    On {{site.data.keyword.linux_notm}}:

    ```bash
    mkdir -p /etc/docker/certs.d/$OCP_IMAGE_REGISTRY
    cp ca.crt /etc/docker/certs.d/$OCP_IMAGE_REGISTRY
    systemctl restart docker.service
    ```
    {: codeblock}

    On {{site.data.keyword.macOS_notm}}:

    ```bash
    mkdir -p ~/.docker/certs.d/$OCP_IMAGE_REGISTRY
    cp ca.crt ~/.docker/certs.d/$OCP_IMAGE_REGISTRY
    ```
    {: codeblock}

    On {{site.data.keyword.macOS_notm}}, use the Docker Desktop icon on the right side of the desktop menu bar to restart Docker by clicking **Restart** in the dropdown menu.

12. Log in to the {{site.data.keyword.ocp}} Docker host:

    ```bash
    echo "$OCP_TOKEN" | docker login -u $OCP_USER --password-stdin $OCP_IMAGE_REGISTRY
    ```
    {: codeblock}

13. Configure additional trust stores for image registry access:

    ```bash
    oc create configmap registry-config --from-file=$OCP_IMAGE_REGISTRY=ca.crt -n openshift-config
    ```
    {: codeblock}

14. Edit the new `registry-config`:

    ```bash
    oc edit image.config.openshift.io cluster
    ```
    {: codeblock}

15. Update the `spec:` section:

    ```bash
    spec:
      additionalTrustedCA:
        name: registry-config
    ```
    {: codeblock}

16. The **agent-install.sh** script stores the {{site.data.keyword.ieam}} agent in the edge cluster container registry. Set the registry user, password, and full image path (minus the tag):

    ```bash
    export EDGE_CLUSTER_REGISTRY_USERNAME=$OCP_USER
    export EDGE_CLUSTER_REGISTRY_TOKEN="$OCP_TOKEN"
    export IMAGE_ON_EDGE_CLUSTER_REGISTRY=$OCP_IMAGE_REGISTRY/$OCP_PROJECT/amd64_anax_k8s
    ```
    {: codeblock}

   **Note**: The {{site.data.keyword.ieam}} agent image is stored in the local edge cluster registry because the edge cluster Kubernetes needs ongoing access to it, in case it needs to restart it or move it to another pod.

17. Download the **agent-install.sh** script from the Cloud Sync Service (CSS) and make it executable:

    ```bash
    curl -u "$HZN_ORG_ID/$HZN_EXCHANGE_USER_AUTH" -k -o agent-install.sh $HZN_FSS_CSSURL/api/v1/objects/IBM/agent_files/agent-install.sh/data
    chmod +x agent-install.sh
    ```
    {: codeblock}

18. Run **agent-install.sh** to get the necessary files from CSS, install and configure the {{site.data.keyword.horizon}} agent, and register your edge cluster with policy:

    ```bash
    ./agent-install.sh -D cluster -i 'css:'
    ```
    {: codeblock}

   **Notes**:
   * To see all of the available flags, run: **./agent-install.sh -h**
   * If an error causes **agent-install.sh** to fail, correct the error and run **agent-install.sh** again. If that does not work, run **agent-uninstall.sh** (see [Removing agent from edge cluster](../using_edge_services/removing_agent_from_cluster.md)) before running **agent-install.sh** again.

19. Change to the agent namespace (also known as project) and verify that the agent pod is running:

    ```bash
    oc project $AGENT_NAMESPACE
    oc get pods
    ```
    {: codeblock}

20. Now that the agent is installed on your edge cluster, you can run these commands if you want to familiarize yourself with the Kubernetes resources associated with the agent:

    ```bash
    oc get namespace $AGENT_NAMESPACE
    oc project $AGENT_NAMESPACE   # ensure this is the current namespace/project
    oc get deployment -o wide
    oc get deployment agent -o yaml   # get details of the deployment
    oc get configmap openhorizon-agent-config -o yaml
    oc get secret openhorizon-agent-secrets -o yaml
    oc get pvc openhorizon-agent-pvc -o yaml   # persistent volume
    ```
    {: codeblock}

21. Often, when an edge cluster is registered for policy, but does not have user-specified node policy, none of the deployment policies will deploy edge services to it. That is the case with the Horizon examples. Proceed to [Deploying services to your edge cluster](#deploying_services) to set node policy so that an edge service will be deployed to this edge cluster.

## Installing agent on k3s and microk8s edge clusters
{: #install_lite}

This content describes how to install the {{site.data.keyword.ieam}} agent on [k3s ](https://k3s.io/){:target="_blank"}{: .externalLink} or [microk8s ](https://microk8s.io/){:target="_blank"}{: .externalLink}, lightweight and small Kubernetes clusters:

1. Log in to your edge cluster as **root**.

2. If you have not completed the steps in [Creating your API key](../hub/prepare_for_edge_nodes.md), do that now. This process creates an API key, locates some files, and gathers environment variable values that are needed when setting up edge nodes. Set the same environment variables on this edge cluster:

   ```bash
   export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
   export HZN_ORG_ID=<your-exchange-organization>
   export HZN_FSS_CSSURL=https://<ieam-management-hub-ingress>/edge-css/
   ```
   {: codeblock}

3. Copy the **agent-install.sh** script to your new edge cluster.

4. The **agent-install.sh** script will store the {{site.data.keyword.ieam}} agent in the edge cluster image registry. Set the full image path (minus the tag) that should be used. For example:

   * On k3s:

      ```bash
      REGISTRY_ENDPOINT=$(kubectl get service docker-registry-service | grep docker-registry-service | awk '{print $3;}'):5000
      export IMAGE_ON_EDGE_CLUSTER_REGISTRY=$REGISTRY_ENDPOINT/openhorizon-agent/amd64_anax_k8s
      ```
      {: codeblock}

   * On microk8s:

      ```bash
      export IMAGE_ON_EDGE_CLUSTER_REGISTRY=localhost:32000/openhorizon-agent/amd64_anax_k8s
      ```
      {: codeblock}

   **Note**: The {{site.data.keyword.ieam}} agent image is stored in the local edge cluster registry because the edge cluster Kubernetes needs ongoing access to it, in case it needs to restart it or move it to another pod.

5. Instruct **agent-install.sh** to use the default storage class:

   * On k3s:

      ```bash
      export EDGE_CLUSTER_STORAGE_CLASS=local-path
      ```
      {: codeblock}

   * On microk8s:

      ```bash
      export EDGE_CLUSTER_STORAGE_CLASS=microk8s-hostpath
      ```
      {: codeblock}

6. Run **agent-install.sh** to get the necessary files from CSS (Cloud Sync Service), install and configure the {{site.data.keyword.horizon}} agent, and register your edge cluster with policy:

   ```bash
   ./agent-install.sh -D cluster -i 'css:'
   ```
   {: codeblock}

   **Notes**:
   * To see all of the available flags, run: **./agent-install.sh -h**
   * If an error occurs causing **agent-install.sh** to not complete successfully, correct the error that is displayed, and run **agent-install.sh** again. If that does not work, run **agent-uninstall.sh** (see [Removing agent from edge cluster](../using_edge_services/removing_agent_from_cluster.md)) before running **agent-install.sh** again.

7. Verify that the agent pod is running:

   ```bash
   kubectl get namespaces
   kubectl -n openhorizon-agent get pods
   ```
   {: codeblock}

8. Usually, when an edge cluster is registered for policy, but does not have any user-specified node policy, none of the deployment policies deploy edge services to it. This is expected. Proceed to [Deploying services to your edge cluster](#deploying_services) to set node policy so that an edge service will be deployed to this edge cluster.

## Deploying services to your edge cluster
{: #deploying_services}

Setting node policy on this edge cluster can cause deployment policies to deploy edge services here. This content shows an example of doing that.

1. Set some aliases to make it more convenient to run the `hzn` command. (The `hzn` command is inside the agent container, but these aliases make it possible to run `hzn` from this host.)

   ```bash
   cat << 'END_ALIASES' >> ~/.bash_aliases
   alias getagentpod='kubectl -n openhorizon-agent get pods --selector=app=agent -o jsonpath={.items[].metadata.name}'
   alias hzn='kubectl -n openhorizon-agent exec -i $(getagentpod) -- hzn'
   END_ALIASES
   source ~/.bash_aliases
   ```
   {: codeblock}

2. Verify that your edge node is configured (registered with the {{site.data.keyword.ieam}} management hub):

   ```bash
   hzn node list
   ```
   {: codeblock}

3. To test your edge cluster agent, set your node policy with a property that deploys the example helloworld operator and service to this edge node:

   ```bash
   cat << 'EOF' > operator-example-node.policy.json
   {
     "properties": [
       { "name": "openhorizon.example", "value": "nginx-operator" }
     ]
   }
   EOF

   cat operator-example-node.policy.json | hzn policy update -f-
   hzn policy list
   ```
   {: codeblock}

   **Note**:
   * Because the real **hzn** command is running inside the agent container, for any `hzn` commands that require an input file, you need to pipe the file into the command so its content will be transferred into the container.

4. After a minute, check for an agreement and the running edge operator and service containers:

   ```bash
   hzn agreement list
   kubectl -n openhorizon-agent get pods
   ```
   {: codeblock}

5. Using the pod IDs from the previous command, view the log of edge operator and service:

   ```bash
   kubectl -n openhorizon-agent logs -f <operator-pod-id>
   # control-c to get out
   kubectl -n openhorizon-agent logs -f <service-pod-id>
   # control-c to get out
   ```
   {: codeblock}

6. You can also view the environment variables that the agent passes to the edge service:

   ```bash
   kubectl -n openhorizon-agent exec -i <service-pod-id> -- env | grep HZN_
   ```
   {: codeblock}

### Changing what services are deployed to your edge cluster
{: #changing_services}

* To change what services are deployed to your edge cluster, change the node policy:

  ```bash
  cat <new-node-policy>.json | hzn policy update -f-
  hzn policy list
  ```
  {: codeblock}

   After a minute or two, the new services will be deployed to this edge cluster.

* **Note**: On some VMs with microk8s, the service pods that are being stopped (replaced) might stall in the **Terminating** state. If that happens, run:

  ```bash
  kubectl delete pod <pod-id> -n openhorizon-agent --force --grace-period=0
  pkill -fe <service-process>
  ```
  {: codeblock}

* If you want to use a pattern, instead of policy, to run services on your edge cluster:

  ```bash
  hzn unregister -f
  hzn register -n $HZN_EXCHANGE_NODE_AUTH -p <pattern-name>
  ```
  {: codeblock}
