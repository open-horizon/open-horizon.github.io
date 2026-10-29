# Setting up a local image registry for a Red Hat OpenShift Container Platform edge cluster

The image registry is the location of the agent image and agent cronjob image. If an edge service image includes assets that are not appropriate to include in a public registry, you can use a local image registry, where access is tightly controlled. Use this procedure to specify the local image registry that you want to use.

Organization administrators can see all the organization users and their API keys in the Open Horizon console, and can delete keys too.

## Procedure

1. Verify that a default route for the OpenShift image registry is created and that it is accessible from outside of the cluster:

```
oc get route default-route -n openshift-image-registry --template='{% raw %}{{ .spec.host }}{% endraw %}'
```

If the command response indicates the `default-route` is not found, you need to expose it (see [Exposing the registry](https://docs.openshift.com/container-platform/4.6/registry/securing-exposing-registry.html) for details):

```
oc patch configs.imageregistry.operator.openshift.io/cluster --patch '{"spec":{"defaultRoute":true}}' --type=merge
```

1. Retrieve the repository route name that you need to use:

```
export OCP_IMAGE_REGISTRY=`oc get route default-route -n openshift-image-registry --template='{% raw %}{{ .spec.host }}{% endraw %}'`
```

1. Create a new project to store your images:

```
export OCP_PROJECT=$AGENT_NAMESPACE
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

1. Set your service account token to the following environment variable:

a. Determine if you can extract the token with this command:

```
oc serviceaccounts get-token $OCP_USER
```

b. If the above command returns a token, run:

```
export OCP_TOKEN=`oc serviceaccounts get-token $OCP_USER`
```

c. If the command from step a did not return a token, run:

```
export OCP_TOKEN=`oc serviceaccounts new-token $OCP_USER`
```

1. Get the OpenShift certificate and allow Docker to trust it:

```
echo | openssl s_client -connect $OCP_IMAGE_REGISTRY:443 -showcerts | sed -n "/-----BEGIN CERTIFICATE-----/,/-----END CERTIFICATE-----/p" > ca.crt
```

On Linux:

```
mkdir -p /etc/docker/certs.d/$OCP_IMAGE_REGISTRY
cp ca.crt /etc/docker/certs.d/$OCP_IMAGE_REGISTRY
systemctl restart docker.service
```

On macOS:

```
mkdir -p ~/.docker/certs.d/$OCP_IMAGE_REGISTRY
cp ca.crt ~/.docker/certs.d/$OCP_IMAGE_REGISTRY
```

Use the Docker Desktop icon on the right side of the desktop menu bar to restart Docker by clicking **Restart** in the dropdown menu.

1. Log in to the OCP Docker host:

```
echo "$OCP_TOKEN" | docker login -u $OCP_USER --password-stdin $OCP_IMAGE_REGISTRY
```

1. Configure additional trust stores for image registry access:

```
oc create configmap registry-config --from-file=$OCP_IMAGE_REGISTRY=ca.crt -n openshift-config
```

1. Edit the new `registry-config`:

   ```
   oc edit image.config.openshift.io cluster
   ```

1. Update the `spec:` section:

   ```
   spec:
     additionalTrustedCA:
       name: registry-config
   ```

1. The `agent-install.sh` script stores the Open Horizon agent in the edge cluster container registry. Set the registry user, password, and the full image path without the tag:

   ```
   export EDGE_CLUSTER_REGISTRY_USERNAME=$OCP_USER
   export EDGE_CLUSTER_REGISTRY_TOKEN="$OCP_TOKEN"
   export IMAGE_ON_EDGE_CLUSTER_REGISTRY=$OCP_IMAGE_REGISTRY/$OCP_PROJECT/amd64_anax_k8s
   ```

   Or for s390x architecture:

   ```
   export IMAGE_ON_EDGE_CLUSTER_REGISTRY=$OCP_IMAGE_REGISTRY/$OCP_PROJECT/s390x_anax_k8s
   ```

   **Note**: The Open Horizon agent image is stored in the local edge cluster registry because the edge cluster Kubernetes needs ongoing access to it, in case it needs to restart it or move it to another pod.

## What's next

- [Installing the agent on Red Hat OpenShift Container Platform Kubernetes edge cluster](https://open-horizon.github.io/docs/anax/docs/installing_ocp_edge_cluster_agent/index.md)
