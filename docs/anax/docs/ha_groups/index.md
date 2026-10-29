# High availability node groups

## Overview

High availability (HA) node groups allow an administrator or node owner to group nodes together that are running the same service to ensure the service stays running on at least one of the nodes at all times. HA grouping is enforced by the agbot, which will only allow one node in a group to perform an upgrade at a time. Nodes in an HA group still complete agent and service upgrades in a coordinated manner. Nodes can only be in one HA group at a time.

## Creating HA node groups

1. To generate a template for creating HA node groups run:

```
hzn exchange hagroup new
```

1. Copy the output to a file and fill in the required fields. In this example, `new-hagroup.json`

```
{
  "name": "",             /* Optional. The name of the HA group. */
  "description": "",      /* A description of the HA group. */
  "members": [            /* A list of node names that are members of this group. */
    "node1",
    "node2"
  ]
}
```

1. Create the group in the exchange:

```
hzn exchange hagroup add --json-file <new-hagroup.json>
```

While any user can create an HA group, only org administrators or the node's owner can add a node to a group. HA groups become effective as soon as the group is created in the exchange.

## Listing nodes in a HA group

To list the nodes in a HA group run:

```
hzn exchange hagroup list <group-name>
```

## Adding nodes to a HA group

After the HA group exists in the exchange, nodes can be added to it in several ways.

- At node registration, an HA group for the node can be specified with the flag `--ha-group=HA-GROUP` where `HA-GROUP` is the name of the existing HA group.
- A node (that previously exists in the exchange, need not be registered) can be added to a group with the command:

```
hzn exchange hagroup member add <group name> --node=NODE
```

where `NODE` is the node id of the node to add.

Additionally, the HA group template used to originally create the group can be updated with the id of the node to add, then republished with:

```
 hzn exchange hagroup add --json-file new-hagroup.json
```

**Note**: If a node is already in an HA group, it must be removed from the group before it can be added to another.

## Removing nodes from HA groups

Remove nodes from an HA group with this command:

```
hzn exchange hagroup member remove <group name> --node=NODE
```

Lastly, to remove the entire HA group from the exchange:

```
hzn exchange hagroup remove <group name>
```

## Limitations

- This feature is only supported for device type nodes. Cluster nodes are expected to use kubernetes operator capabilities to ensure service availability.
- Services, with current agreements that are running on a node, are still upgraded, even if other nodes in its HA group are offline.
- If a node is added to an HA group while the node has already started a upgrade, the HA group membership of the node is not enforced until the ongoing service or agent upgrade has completed.
