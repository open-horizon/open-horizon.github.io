---

copyright:
years: 2021
lastupdated: "2021-02-20"
title: Container Registry
description: ""
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Using a private container registry
{: #container_registry}

If an edge service image includes assets that are not appropriate to include in a public registry, you can use a private Docker container registry, for example, the {{site.data.keyword.open_shift}} Image Registry or the {{site.data.keyword.ibm_cloud}} Container Registry, where access is tightly controlled.
{:shortdesc}

If you have not done so already, follow the steps in [Developing an edge service for devices](developing.md) to create and deploy at least one example edge service to ensure you are familiar with the basic process.

This page describes two registries you can store edge service images in:
* [Using the {{site.data.keyword.open_shift}} image registry](#ocp_image_registry)
* [Using the {{site.data.keyword.cloud_notm}} Container Registry](#ibm_cloud_container_registry)

These also serve as examples of how you can use any private image registry with {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}).

## Using the {{site.data.keyword.open_shift}} image registry
{: #ocp_image_registry}

### Before you begin

* If you have not already done so, install the [cloudctl command ](https://www.ibm.com/support/knowledgecenter/SSFC4F_1.3.0/cloudctl/install_cli.html){:target="_blank"}{: .externalLink}
* If you have not already done so, install the [{{site.data.keyword.open_shift}} oc command ](https://docs.openshift.com/container-platform/4.4/cli_reference/openshift_cli/getting-started-cli.html){:target="_blank"}{: .externalLink}
* On {{site.data.keyword.macOS_notm}}, you can install the {{site.data.keyword.open_shift}} **oc** command using [homebrew ](https://docs.brew.sh/Installation){:target="_blank"}{: .externalLink}

    ```bash
    brew install openshift-cli
    ```
    {: codeblock}

### Procedure

Note: See [Conventions used in this document](../getting_started/document_conventions.md) for more information about command syntax.

1. Ensure that you are connected to your {{site.data.keyword.open_shift}} cluster with cluster administrator privileges.

   ```bash
   cloudctl login -a <cluster-url> -u <user> -p <password> -n kube-system --skip-ssl-validation
   ```
   {: codeblock}

2. Determine if a default route for the {{site.data.keyword.open_shift}} image registry has been create such that it is accessible from outside of the cluster:

   ```bash
   oc get route default-route -n openshift-image-registry --template=''
   ```
   {: codeblock}

   If the command response indicates the **default-route** is not found, then create it (see [Exposing the registry ](https://docs.openshift.com/container-platform/4.4/registry/securing-exposing-registry.html){:target="_blank"}{: .externalLink} for details):

   ```bash
   oc patch configs.imageregistry.operator.openshift.io/cluster --patch '{"spec":{"defaultRoute":true}}' --type=merge
   ```
   {: codeblock}

3. Retrieve the repository route name you need to use:

   ```bash
   export OCP_DOCKER_HOST=`oc get route default-route -n openshift-image-registry --template=''`
   ```
   {: codeblock}

4. Create a new project to store your images in:

   ```bash
   export OCP_PROJECT=<your-new-project>
   oc new-project $OCP_PROJECT
   ```
   {: codeblock}

5. Create a service account with a name of your choosing:

   ```bash
   export OCP_USER=<service-account-name>
   oc create serviceaccount $OCP_USER
   ```
   {: codeblock}

6. Add a role to your service account for the current project:

   ```bash
   oc policy add-role-to-user edit system:serviceaccount:$OCP_PROJECT:$OCP_USER
   ```
   {: codeblock}

7. Get the token assigned to your service account:

   ```bash
   export OCP_TOKEN=`oc serviceaccounts get-token $OCP_USER`
   ```
   {: codeblock}

8. Get the {{site.data.keyword.open_shift}} certificate and have docker trust it:

   ```bash
   echo | openssl s_client -connect $OCP_DOCKER_HOST:443 -showcerts | sed -n "/-----BEGIN CERTIFICATE-----/,/-----END CERTIFICATE-----/p" > ca.crt
   ```
   {: codeblock}

   On {{site.data.keyword.linux_notm}}:

   ```bash
   mkdir -p /etc/docker/certs.d/$OCP_DOCKER_HOST
   cp ca.crt /etc/docker/certs.d/$OCP_DOCKER_HOST
   systemctl restart docker.service
   ```
   {: codeblock}

   On {{site.data.keyword.macOS_notm}}:

   ```bash
   mkdir -p ~/.docker/certs.d/$OCP_DOCKER_HOST
   cp ca.crt ~/.docker/certs.d/$OCP_DOCKER_HOST
   ```
   {: codeblock}

   On {{site.data.keyword.macOS_notm}}, restart docker by clicking on the whale icon on the right-hand side of the desktop menu bar and selecting **Restart**.

9. Login to the {{site.data.keyword.ocp}} Docker host:

   ```bash
   echo "$OCP_TOKEN" | docker login -u $OCP_USER --password-stdin $OCP_DOCKER_HOST
   ```
   {: codeblock}

10. Configure additional trust stores for image registry access:   

    ```bash
    oc create configmap registry-config --from-file=<external-registry-address>=ca.crt -n openshift-config
    ```
    {: codeblock}

11. Edit the new `registry-config`:

    ```bash
    oc edit image.config.openshift.io cluster
    ```
    {: codeblock}

12. Update the `spec:` section with the following lines:

    ```bash
    spec:
      additionalTrustedCA:
       name: registry-config
    ```
    {: codeblock}

13. Build your image with this path format, for example:

   ```bash
   export BASE_IMAGE_NAME=myservice
   docker build -t $OCP_DOCKER_HOST/$OCP_PROJECT/${BASE_IMAGE_NAME}_amd64:1.2.3 -f ./Dockerfile.amd64 .
   ```
   {: codeblock}

14. In preparation for publishing your edge service, modify your **service.definition.json** file such that its **deployment** section references your image registry path. You can create service and pattern definition files like this using:

   ```bash
   hzn dev service new -s $BASE_IMAGE_NAME -i $OCP_DOCKER_HOST/$OCP_PROJECT/$BASE_IMAGE_NAME
   ```
   {: codeblock}

   The **&lt;base-image-name&gt;** should be your base image name without the arch or version. You can then edit the variables in the created file **horizon/hzn.json** as necessary.

   Or, if you have created your own service definition file, ensure the **deployment.services.&lt;service-name&gt;.image** field references your image registry path.

15. When your service image is ready to be published, push the image to your private container registry and publish the image to {{site.data.keyword.horizon}} exchange:

   ```bash
   hzn exchange service publish -r "$OCP_DOCKER_HOST:$OCP_USER:$OCP_TOKEN" -f horizon/service.definition.json
   ```
   {: codeblock}

   The **-r "$OCP_DOCKER_HOST:$OCP_USER:$OCP_TOKEN"** argument gives {{site.data.keyword.horizon_open}} edge nodes the credentials to be able to pull the service image.

   The command completes these tasks:

   * Pushes the Docker images to your {{site.data.keyword.cloud_notm}} Container Registry, and get the digest of the image in the process.
   * Signs the digest and the deployment information with your private key.
   * Puts the service metadata (including the signature) into {{site.data.keyword.horizon}} exchange.
   * Puts your public key into {{site.data.keyword.horizon}} exchange under the service definition so {{site.data.keyword.horizon}} edge nodes can automatically retrieve the definition to verify your signatures when needed.
   * Puts the OpenShift user and token into {{site.data.keyword.horizon}} exchange under the service definition so {{site.data.keyword.horizon}} edge nodes can automatically retrieve the definition when needed.
   
### Using your service on {{site.data.keyword.horizon}} edge nodes
{: #using_service}

To allow your edge nodes to pull the necessary service images from the {{site.data.keyword.ocp}} image registry, you must configure docker on each edge node to trust the {{site.data.keyword.open_shift}} certificate. Copy the **ca.crt** file to each edge node and then:

On {{site.data.keyword.linux_notm}}:

```bash
mkdir -p /etc/docker/certs.d/$OCP_DOCKER_HOST
cp ca.crt /etc/docker/certs.d/$OCP_DOCKER_HOST
systemctl restart docker.service
```
{: codeblock}

On {{site.data.keyword.macOS_notm}}:

```bash
mkdir -p ~/.docker/certs.d/$OCP_DOCKER_HOST
cp ca.crt ~/.docker/certs.d/$OCP_DOCKER_HOST
```
{: codeblock}

On {{site.data.keyword.macOS_notm}} restart docker by clicking on the whale icon on the right hand side of the desktop menu bar and selecting **Restart**.

Now {{site.data.keyword.horizon}} has everything that it needs to get this edge service image from the {{site.data.keyword.open_shift}} image registry and deploy it to edge nodes as specified by the deployment pattern or policy you have created.

## Using the {{site.data.keyword.cloud_notm}} Container Registry
{: #ibm_cloud_container_registry}

### Before you begin

* Install the [{{site.data.keyword.cloud_notm}} CLI tool (ibmcloud) ](https://cloud.ibm.com/docs/cli?topic=cloud-cli-install-ibmcloud-cli){:target="_blank"}{: .externalLink}.
* Ensure you have **Cluster administrator** or **team administrator** access level in your {{site.data.keyword.cloud_notm}} account.

### Procedure

1. Log in to the {{site.data.keyword.cloud_notm}} and target your organization:

   ```bash
   ibmcloud login -a cloud.ibm.com -u <cloud-username> -p <cloud-password
   ibmcloud target -o <organization-id> -s <space-id>
   ```
   {: codeblock}

   If you do not know your organization ID and space ID, you can log in to the [{{site.data.keyword.cloud_notm}} console ](https://cloud.ibm.com/){:target="_blank"}{: .externalLink} find or create them.

2. Create a cloud API key:

   ```bash
   ibmcloud iam api-key-create <key-name> -d "<key-description>"
   ```
   {: codeblock}

   Save the API key value (displayed in the line that starts with **API Key**) in a secure place and set it in this environment variable:

   ```bash
   export CLOUD_API_KEY=<your-cloud-api-key>
   ```
   {: codeblock}

   Note: This API key is different from the {{site.data.keyword.open_shift}} API key you created to use with the `hzn` command.

3. Get the container-registry plugin and create your private registry namespace. (This registry namespace will be part of the path used to identify your docker image.)

   ```bash
   ibmcloud plugin install container-registry
   export REGISTRY_NAMESPACE=<your-registry-namespace>
   ibmcloud cr namespace-add $REGISTRY_NAMESPACE
   ```
   {: codeblock}

4. Log in to your Docker registry namespace:

   ```bash
   ibmcloud cr login
   ```
   {: codeblock}

   For more information about using **ibmcloud cr**, see [ibmcloud cr CLI web documentation ](https://cloud.ibm.com/docs/Registry){:target="_blank"}{: .externalLink}. Additionally, you can run this command to view help information:

   ```bash
   ibmcloud cr --help
   ```
   {: codeblock}

   After you log in to your private namespace in the {{site.data.keyword.cloud_registry}}, you do not need to use `docker login` to log in to the registry. You can use container registry paths similar to the following within your **docker push** and **docker pull** commands:

   ```bash
   us.icr.io/$REGISTRY_NAMESPACE/<base-image-name>_<arch>:<version>
   ```
   {: codeblock}

5. Build your image with this path format, for example:

   ```bash
   export BASE_IMAGE_NAME=myservice
   docker build -t us.icr.io/$REGISTRY_NAMESPACE/${BASE_IMAGE_NAME}_amd64:1.2.3 -f ./Dockerfile.amd64 .
   ```
   {: codeblock}

6. In preparation for publishing your edge service, modify your **service.definition.json** file such that its **deployment** section references your image registry path. You can create service and pattern definition files like this using:

   ```bash
   hzn dev service new -s $BASE_IMAGE_NAME -i us.icr.io/$REGISTRY_NAMESPACE/$BASE_IMAGE_NAME
   ```
   {: codeblock}

   The **&lt;base-image-name&gt;** should be your base image name without the arch or version. You can then edit the variables in the created file **horizon/hzn.json** as necessary.

   Or, if you have created your own service definition file, ensure the **deployment.services.&lt;service-name&gt;.image** field references your image registry path.

7. When your service image is ready to be published, push the image to your private container registry and publish the image to {{site.data.keyword.horizon}} exchange:

   ```bash
   hzn exchange service publish -r "us.icr.io:iamapikey:$CLOUD_API_KEY" -f horizon/service.definition.json
   ```
   {: codeblock}

   The **-r "us.icr.io:iamapikey:$CLOUD_API_KEY"** argument gives {{site.data.keyword.horizon_open}} edge nodes the credentials to be able to pull the service image.

   The command completes these tasks:

   * Pushes the Docker images to your {{site.data.keyword.cloud_notm}} Container Registry, and get the digest of the image in the process.
   * Signs the digest and the deployment information with your private key.
   * Puts the service metadata (including the signature) into {{site.data.keyword.horizon}} exchange.
   * Puts your public key into {{site.data.keyword.horizon}} exchange under the service definition so {{site.data.keyword.horizon}} edge nodes can automatically retrieve the definition to verify your signatures when needed.
   * Puts your {{site.data.keyword.cloud_notm}} API key into {{site.data.keyword.horizon}} exchange under the service definition so {{site.data.keyword.horizon}} edge nodes can automatically retrieve the definition when needed.

8. Verify that your service image was pushed to the {{site.data.keyword.cloud_notm}} Container Registry:

   ```bash
   ibmcloud cr images
   ```
   {: codeblock}

9. Publish a deployment pattern or policy that will deploy your service to some edge nodes. For example,:

   ```bash
   hzn exchange pattern publish -f horizon/pattern.json
   ```
   {: codeblock}

Now {{site.data.keyword.horizon}} has everything that it needs to get this edge service image from the {{site.data.keyword.cloud_notm}} Container Registry and deploy it to edge nodes as specified by the deployment pattern or policy you have created.
