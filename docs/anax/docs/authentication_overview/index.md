# Authenticating to the management hub

There are two ways a user can authenticate in order to run CLI commands: with a username and password, or with an API key.

## User/password authentication

An org administrator can create additional users in the same organization. The password is set when the user is created. The syntax for creating a new user is

```
hzn exchange user create -o $HZN_ORG_ID -u $HZN_EXCHANGE_USER_AUTH <user> <pw>
```

Once the user is created, the agent uses these credentials to communicate with the management hub. The syntax is

```
export HZN_EXCHANGE_USER_AUTH=<user>:<pw>
export HZN_ORG_ID=<your_org>
hzn exchange status
```

## API key authentication

Once a user is created, an API key can be created for that user by an org admin or by the user itself. The API key can then be used for subsequent authentication to the management hub. If an API key is ever compromised or exposed, the API key can be revoked and a new one generated. The syntax for creating an API key is

```
hzn exchange user createkey <user> <description>
```

**Note**: The API key is only revealed when it is created. You must copy the key to a safe location since you cannot recover the API key later. If you lose your API key, you would need to create a new one.

Once the API key is created, the agent uses these credentials to communicate with the management hub. The syntax is

```
export HZN_EXCHANGE_USER_AUTH=apikey:<apikey>
export HZN_ORG_ID=<your_org>
hzn exchange status
```
