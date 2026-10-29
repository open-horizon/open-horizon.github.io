# Node policy

Every registered node has a node policy. It consists of [built-in node properties](https://open-horizon.github.io/docs/anax/docs/built_in_policy/index.md) which are read-only as well as properties and constraints which can be set by the node owner. Node policies have several sections with repeated fields. This is due to the dual function served by node policies. Firstly, the deployment and top-level sections of node policies are used by agbots to determine service deployment on the nodes. For more information, refer to the node [policy](https://open-horizon.github.io/docs/anax/docs/policy/index.md) documentation. Secondly, the management and top-level node policy sections are used by the nodes to determine what node management policies they should execute. For more information, refer to the [node management policy](https://open-horizon.github.io/docs/anax/docs/node_management_policy/index.md) documentation. The command `hzn policy new` will return an empty node policy with comments on how to fill it out.

The node policies have three pairs of properties and constraints. If they are not empty, the deployment and management properties and constraints will used in determining compatibility. The deployment properties or management properties are merged with the top-level properties to be used for determining eligibility for deployment or management policies respectively. If a property in the deployment or management section shares the name with a property in the top-level section, the value in deployment or management property will be used. The constraints from the deployment or management section will be used for determining eligibility for deployment or management policies respectively. If the relevant section is empty, the top-level constraints will be used. Node policies in the older format that had only one pair of properties and constraints will be interpreted as equivalent to the deployment section of the new policy format.

While top level properties can be used to match deployment policy constraints and management policy constraints, it is recommended that intents for service deployments be placed in the deployment properties and intents for management controls be placed in the management properties.

The following is an example of a node policy.

```
{
  "properties": [
    {
       "name": "openhorizon.arch",
       "value": "amd64"
    }
  ],
  "constraints": [
       "station > 15"
  ],
  "deployment": {
      "properties": [
        {
           "name": "application-version",
           "value": "1.2.3"
        }
      ],
      "constraints": [
         "equipment == camera"
      ]
  },
  "management": {
      "properties": [
        {
           "name": "latest-version",
           "value": true
        }
      ],
      "constraints": [
         "node1 == true"
      ]
  }
}
```
