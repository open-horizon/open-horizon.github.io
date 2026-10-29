# Hello world with a secret

This example teaches you how to develop an Open Horizon service that uses secrets. Secrets ensure that login credentials and other sensitive information are kept secure.

## Before you begin

Complete the prerequisite steps in [Preparing to create an edge service](https://open-horizon.github.io/docs/developing/service_containers/index.md). As a result, these environment variables should be set, these commands should be installed, and these files should exist:

```
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID"
which git jq make
ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem
cat /etc/default/horizon
```

## Procedure

This example is part of the [Open Horizon](https://github.com/open-horizon/) open-source project. Follow the steps in [Creating Your Own Hello Secret Service](https://github.com/open-horizon/examples/blob/master/edge/services/helloSecretWorld/CreateService.md) and then return here.

## What to do next

- Try the other edge service examples at [Developing an edge service for devices](https://open-horizon.github.io/docs/developing/developing/index.md).

## Further reading

- [Using Secrets](https://open-horizon.github.io/docs/secrets/index.md)
