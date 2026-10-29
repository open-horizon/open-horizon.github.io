# Using NMPs to upgrade agents automatically

## Automatic agent upgrade

Automatic agent upgrade is a policy-based node management feature that allows an org admin to create node management policies that deploy upgrade jobs to nodes and manages them autonomously. This allows the admin to ensure that all the nodes in the system are using the intended versions.

This feature utilizes existing agent artifacts that reside in Cloud Sync Service (CSS) from the edgeNodeFiles.sh installation script.

Here is a video showing the agent auto-upgrade feature:

{% include youtubePlayer.html id="f0emDR9AIGg" %}

### How to set-up an Automatic agent upgrade policy

The following steps describe how to set up an Automatic agent upgrade policy.

1. Determine the manifestID for the new version of agent software.

1. List the available manifests present in the IBM org on your system. Execute the following

   ```
   hzn nodemanagement manifest list -o IBM -u $HZN_ORG_ID/$HZN_EXCHANGE_USER_AUTH
   ```

1. Alternatively, if a custom manifest has been created (see [here](https://open-horizon.github.io/docs/anax/docs/agentfile_manifest/index.md)), those can be listed in the customers org by executing

   ```
   hzn nodemanagement manifest list -o $HZN_ORG_ID -u $HZN_ORG_ID/$HZN_EXCHANGE_USER_AUTH
   ```

1. Create a node management policy.

1. Use the following command to save a node management policy (NMP) template to a file. An NMP determines which nodes to upgrade, when to do the upgrade, and what to upgrade. In this example, the file is named `nmp.json`

   ```
   hzn exchange nmp new > nmp.json
   ```

   **Note**: For more detailed information about NMP's, see [here](https://open-horizon.github.io/docs/anax/docs/node_management_policy/index.md)

1. Using a text editor, edit the NMP file to set the parameters of the upgrade. In this example, `constraints` and `properties` are used to identify the nodes to upgrade, the `start` and `startWindows` values indicate the upgrade will be attempted with a randomized start time of 300 seconds from now, and the `manifestID` indicates to use manifest `edgeNodeFiles_manifest_2.30.0-123` found in the IBM org.

   ```
   {
     "label": "Sample NMP",
     "description": "A sample description of the NMP",
     "constraints": [
        "myconstraint == myvalue"
     ],
     "properties": [
       {
       "name": "myproperty",
       "value": "myvalue"
       }
     ],
     "enabled": true,
     "start": "now",
     "startWindow": 300,
     "agentUpgradePolicy": {
        "manifest": "IBM/edgeNodeFiles_manifest_2.30.0-123",
        "allowDowngrade": false
     }
   }
   ```

1. (Optional) Verify the impacted edge nodes. The following command can be used to check which nodes the NMP applies to before publishing the NMP to the Exchange. This is useful to confirm the NMP parameters will target the desired edge nodes only.

```
hzn exchange nmp add sample_nmp -f nmp.json --dry-run --applies-to
```

1. Add the NMP to the Exchange.

```
hzn exchange nmp add sample_nmp -f nmp.json
```

1. (Optional) Observe the status of the upgrade job.

1. Now that the NMP has been published, it will soon get picked up by the worker on the agent to perform the upgrade. The status of the NMP can then be observed using the following command.

   ```
   hzn exchange nmp status sample-nmp
   ```

   or

   ```
   hzn exchange node management status {node-name}
   ```
