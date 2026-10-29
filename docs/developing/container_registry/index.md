# Using a private container registry

If an edge service image includes assets that are not appropriate to include in a public registry, you can use a private Docker® container registry, for example, the OpenShift Image Registry or the IBM Cloud Container Registry, where access is tightly controlled.

If you have not done so already, follow the steps in [Developing an edge service for devices](https://open-horizon.github.io/docs/developing/developing/index.md) to create and deploy at least one example edge service to ensure you are familiar with the basic process.

This page describes two registries you can store edge service images in: * [Using the OpenShift image registry](#ocp_image_registry) * [Using the IBM Cloud Container Registry](#ibm_cloud_container_registry)

These also serve as examples of how you can use any private image registry with Open Horizon (Open Horizon).

## Using the OpenShift image registry

### Before you begin

- If you have not already done so, install the [IBM Cloud Pak CLI (**cloudctl**) and OpenShift client CLI (**oc**)](https://open-horizon.github.io/docs/cli/cloudctl_oc_cli/index.md) commands.

**Note**: Because the local registry usually has a smaller disk, it might fill quickly. In some cases, this can adversely affect the management hub to the point that it could become non-functional. Due to this, consider using OpenShift local image registries only if preventative monitoring is implemented in your environment; otherwise, use external image registries.

### Procedure

**Note**: For more information about command syntax, see [Conventions used in this document](https://open-horizon.github.io/docs/getting_started/document_conventions/index.md).

1. Ensure that you are connected to your OpenShift cluster with cluster administrator privileges.

```
cloudctl login -a <cluster-url> -u <user> -p <password> -n kube-system --skip-ssl-validation
```

1. Determine if a default route for the OpenShift image registry has been create such that it is accessible from outside of the cluster:

```
oc get route default-route -n openshift-image-registry --template='\{\{ .spec.host \}\}'
```

If the command response indicates the **default-route** is not found, then create it (see [Exposing the registry](https://docs.openshift.com/container-platform/4.6/registry/securing-exposing-registry.html) for details):

```
oc patch configs.imageregistry.operator.openshift.io/cluster --patch '{"spec":{"defaultRoute":true}}' --type=merge
```

1. Retrieve the repository route name that you need to use:

```
export OCP_DOCKER_HOST=`oc get route default-route -n openshift-image-registry --template='\{\{ .spec.host \}\}'`
```

1. Create a new project to store your images in:

```
export OCP_PROJECT=<your-new-project>
oc new-project $OCP_PROJECT
```

1. Create a service account with a name of your choosing:

```
export OCP_USER=<service-account-name>
oc create serviceaccount $OCP_USER
```

1. Add a role to your service account for the current project:

```
oc policy add-role-to-user edit system:serviceaccount:$OCP_PROJECT:$OCP_USER
```

1. Get the token assigned to your service account:

```
export OCP_TOKEN=`oc serviceaccounts get-token $OCP_USER`
```

1. Get the OpenShift certificate and have docker trust it:

```
echo | openssl s_client -connect $OCP_DOCKER_HOST:443 -showcerts | sed -n "/-----BEGIN CERTIFICATE-----/,/-----END CERTIFICATE-----/p" > ca.crt
```

On Linux:

```
mkdir -p /etc/docker/certs.d/$OCP_DOCKER_HOST
cp ca.crt /etc/docker/certs.d/$OCP_DOCKER_HOST
systemctl restart docker.service
```

On macOS:

```
mkdir -p ~/.docker/certs.d/$OCP_DOCKER_HOST
cp ca.crt ~/.docker/certs.d/$OCP_DOCKER_HOST
```

On macOS, restart docker by clicking on the whale icon on the right-hand side of the desktop menu bar and selecting **Restart**.

1. Log in to the OCP Docker® host:

```
echo "$OCP_TOKEN" | docker login -u $OCP_USER --password-stdin $OCP_DOCKER_HOST
```

1. Configure additional trust stores for image registry access using ca.crt file from step 8:

   ```
   oc create configmap registry-config --from-file=<file_path_to_ca.crt> -n openshift-config
   ```

1. Edit the new `registry-config`:

   ```
   oc edit image.config.openshift.io cluster
   ```

1. Update the `spec:` section with the following lines:

   ```
   spec:
     additionalTrustedCA:
      name: registry-config
   ```

1. Build your image with this path format, for example:

```
export BASE_IMAGE_NAME=myservice
docker build -t $OCP_DOCKER_HOST/$OCP_PROJECT/${BASE_IMAGE_NAME}_amd64:1.2.3 -f ./Dockerfile.amd64 .
```

1. In preparation for publishing your edge service, modify your **service.definition.json** file such that its **deployment** section references your image registry path. You can create service and pattern definition files like this using:

```
hzn dev service new -s $BASE_IMAGE_NAME -i $OCP_DOCKER_HOST/$OCP_PROJECT/$BASE_IMAGE_NAME
```

The **\<BASE_IMAGE_NAME>** should be your base image name without the arch or version. You can then edit the variables in the created file **horizon/hzn.json** as necessary.

Or, if you have created your own service definition file, ensure the **deployment.services.<service-name>.image** field references your image registry path.

1. When your service image is ready to be published, push the image to your private container registry and publish the image to Horizon exchange:

```
hzn exchange service publish -r "$OCP_DOCKER_HOST:$OCP_USER:$OCP_TOKEN" -f horizon/service.definition.json
```

The **-r "$OCP_DOCKER_HOST:$OCP_USER:$OCP_TOKEN"** argument gives Open Horizon edge nodes the credentials to be able to pull the service image.

The command completes these tasks:

- Pushes the Docker® images to your IBM Cloud Container Registry, and get the digest of the image in the process.
- Signs the digest and the deployment information with your private key.
- Puts the service metadata (including the signature) into Horizon exchange.
- Puts your public key into Horizon exchange under the service definition so Horizon edge nodes can automatically retrieve the definition to verify your signatures when needed.
- Puts the OpenShift user and token into Horizon exchange under the service definition so Horizon edge nodes can automatically retrieve the definition when needed.

### Using your service on Horizon edge nodes

To allow your edge nodes to pull the necessary service images from the OCP image registry, you must configure docker on each edge node to trust the OpenShift certificate. Copy the **ca.crt** file to each edge node and then:

On Linux:

```
mkdir -p /etc/docker/certs.d/$OCP_DOCKER_HOST
cp ca.crt /etc/docker/certs.d/$OCP_DOCKER_HOST
systemctl restart docker.service
```

On macOS:

```
mkdir -p ~/.docker/certs.d/$OCP_DOCKER_HOST
cp ca.crt ~/.docker/certs.d/$OCP_DOCKER_HOST
```

On macOS restart docker by clicking on the whale icon on the right hand side of the desktop menu bar and selecting **Restart**.

Now Horizon has everything that it needs to get this edge service image from the OpenShift image registry and deploy it to edge nodes as specified by the deployment pattern or policy you have created.

## Using the IBM Cloud Container Registry

### Before you begin

- Install the [IBM Cloud CLI tool (ibmcloud)](https://cloud.ibm.com/docs/cli?topic=cloud-cli-install-ibmcloud-cli) .
- Ensure you have **Cluster administrator** or **team administrator** access level in your IBM Cloud account.

### Procedure

1. Log in to the IBM Cloud from a system that has an operating system supported by the [IBM Cloud CLI tool (ibmcloud)] and target your organization:

```
ibmcloud login -a cloud.ibm.com -u <cloud-username> -p <cloud-password
ibmcloud target -o <organization-id> -s <space-id>
```

If you do not know your organization ID and space ID, you can log in to the [IBM Cloud console](https://cloud.ibm.com/) find or create them.

1. Create a cloud API key:

```
ibmcloud iam api-key-create <key-name> -d "<key-description>"
```

Save the API key value (displayed in the line that starts with **API Key**) in a secure place and set it in this environment variable:

```
export CLOUD_API_KEY=<your-cloud-api-key>
```

**Note**: This API key is different from the OpenShift API key you created to use with the `hzn` command.

1. Get the container-registry plugin and create your private registry namespace. (This registry namespace will be part of the path used to identify your docker image.)

```
ibmcloud plugin install container-registry
export REGISTRY_NAMESPACE=<your-registry-namespace>
ibmcloud cr namespace-add $REGISTRY_NAMESPACE
```

**Note**: Alternatively, you can use the [IBM Cloud console](https://cloud.ibm.com/) to create the registry namespace.

1. On the system where you are developing the service, set the following environment variables:

```
export ENTITLED_REGISTRY=<location>.icr.io
export ENTITLED_REGISTRY_USER=iamapikey
export ENTITLED_REGISTRY_KEY=<api-key-created-from-above>
export REGISTRY_NAMESPACE=<your-registry-namespace>
```

1. Use the following docker login command to log in to your registry:

```
docker login "$ENTITLED_REGISTRY" -u "$ENTITLED_REGISTRY_USER" -p "$ENTITLED_REGISTRY_KEY"
```

1. Build your image with this path format, for example:

```
export BASE_IMAGE_NAME=myservice
docker build -t us.icr.io/${REGISTRY_NAMESPACE}/${BASE_IMAGE_NAME}_amd64:1.2.3 -f ./Dockerfile.amd64 .
```

1. In preparation for publishing your edge service, modify your **service.definition.json** file such that its **deployment** section references your image registry path. You can create service and pattern definition files like this using:

```
hzn dev service new -s ${BASE_IMAGE_NAME} -i us.icr.io/${REGISTRY_NAMESPACE}/${BASE_IMAGE_NAME}
```

The **\<BASE_IMAGE_NAME>** should be your base image name without the arch or version. You can then edit the variables in the created file **horizon/hzn.json** as necessary.

Or, if you have created your own service definition file, ensure the **deployment.services.<service-name>.image** field references your image registry path.

1. When your service image is ready to be published, push the image to your private container registry and publish the image to Horizon exchange:

```
hzn exchange service publish -r "us.icr.io:iamapikey:$CLOUD_API_KEY" -f horizon/service.definition.json
```

The **-r "us.icr.io:iamapikey:$CLOUD_API_KEY"** argument gives Open Horizon edge nodes the credentials to be able to pull the service image.

The command completes these tasks:

- Pushes the Docker® images to your IBM Cloud Container Registry, and get the digest of the image in the process.
- Signs the digest and the deployment information with your private key.
- Puts the service metadata (including the signature) into Horizon exchange.
- Puts your public key into Horizon exchange under the service definition so Horizon edge nodes can automatically retrieve the definition to verify your signatures when needed.
- Puts your IBM Cloud API key into Horizon exchange under the service definition so Horizon edge nodes can automatically retrieve the definition when needed.
- From the system where the [IBM Cloud CLI tool (ibmcloud)] is installed, verify that your service image was pushed to the IBM Cloud Container Registry:

```
ibmcloud cr images
```

**Note**: Alternatively, you can use the [IBM Cloud console](https://cloud.ibm.com/) to view the images in the IBM Cloud Container Registry.

1. Publish a deployment pattern or policy that will deploy your service to some edge nodes. For example,:

```
hzn exchange pattern publish -f horizon/pattern.json
```

Now Horizon has everything that it needs to get this edge service image from the IBM Cloud Container Registry and deploy it to edge nodes as specified by the deployment pattern or policy you have created.
