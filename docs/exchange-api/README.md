---
copyright:
years: 2022 - 2023
lastupdated: "2023-03-14"
layout: page
title: "Exchange API Server"
description: "Open Horizon Exchange API Documentation"

nav_order: 3
parent: Management Hub
has_children: true
has_toc: false
---

# Open Horizon Exchange Server and REST API

The data exchange API provides API services for the exchange web UI (future), the edge nodes, and agreement Bots.

The exchange service also provides a few key services for BH for areas in which the decentralized P2P tools
do not scale well enough yet. As soon as the decentralized tools are sufficient, they will replace these
services in the exchange.

## <a name="preconditions"></a>Preconditions for Local Development

- [Install scala](http://www.scala-lang.org/download/install.html){:target="_blank"}{: .externalLink}
- [Install sbt](https://www.scala-sbt.org/1.x/docs/Setup.html){:target="_blank"}{: .externalLink}
- (optional) Install conscript and giter8 if you want to get example code from scalatra.org
- Install postgresql locally (unless you have a remote instance you are using). Instructions for installing on Mac OS X:
    - Install: `brew install postgresql`
    - Note: when running/testing the exchange svr in a docker container, it can't reach your postgres instance on `localhost`, so configure it to also listen on your local IP:
      - set this to your IP: `export MY_IP=<my-ip>`
      - `echo "host all all $MY_IP/32 trust" >> /usr/local/var/postgres/pg_hba.conf`
      - `sed -i -e "s/#listen_addresses = 'localhost'/listen_addresses = '$MY_IP'/" /usr/local/var/postgres/postgresql.conf`
      - `brew services start postgresql` or if it is already running `brew services restart postgresql`
    - Or if your test machine is on a private subnet:
      - trust all clients on your subnet: `echo 'host all all 192.168.1.0/24 trust' >> /usr/local/var/postgres/pg_hba.conf`
      - listen on all interfaces: `sed -i -e "s/#listen_addresses = 'localhost'/listen_addresses = '*'/" /usr/local/var/postgres/postgresql.conf`
      - `brew services start postgresql` or if it is already running `brew services restart postgresql`
    - Or you can run postgresql in a container and connect it to the docker network `exchange-api-network`
    - Test: `psql "host=$MY_IP dbname=postgres user=<myuser> password=''"`
- Add a configuration file on your development system at `/etc/horizon/exchange/config.json` with at minimum the following content (this is needed for the automated tests. Defaults and the full list of configuration variables are in `src/main/resources/config.json`):

  ```
  {
    "api": {
      "db": {
        "jdbcUrl": "jdbc:postgresql://localhost/postgres",    // my local postgres db
        "user": "myuser",
        "password": ""
      },
      "logging": {
        "level": "DEBUG"
      },
      "root": {
        "password": "myrootpw"
      }
    }
  }
  ```
- If you want to run the `FrontEndSuite` test class `config.json` should also include `"frontEndHeader": "issuer"` directly after `email` under `root`.
- Set the same exchange root password in your shell environment, for example:
```
export EXCHANGE_ROOTPW=myrootpw
```

- If someone hasn't done it already, create the TLS private key and certificate:
```
export EXCHANGE_KEY_PW=<pass-phrase>
make gen-key
```

- Otherwise, get files `exchangecert.pem`, `keypassword`, and `keystore` from the person who created them and put them in `./keys/etc`.

## Building and Running in Local Sandbox

- `sbt`
- `~reStart`
- Once the server starts, to see the swagger output, browse: [http://localhost:8080/v1/swagger](http://localhost:8080/v1/swagger){:target="_blank"}{: .externalLink}
- To try a simple rest method curl: `curl -X GET "http://localhost:8080/v1/admin/version"`. You should get the exchange version number as the response.  
- When testing the exchange in an OpenShift Cluster the variables `EXCHANGE_IAM_ORG`, `EXCHANGE_IAM_KEY` and `EXCHANGE_MULT_ACCOUNT_ID` must be set accordingly.
- A convenience script `src/test/bash/primedb.sh` can be run to prime the DB with some exchange resources to use in manually testing:
```
export EXCHANGE_USER=<my-user-in-IBM-org>
export EXCHANGE_PW=<my-pw-in-IBM-org>
src/test/bash/primedb.sh
```
- `primedb.sh` will only create what doesn't already exist, so it can be run again to restore some resources you have deleted.
- To locally test the exchange against an existing ICP cluster:
```
export ICP_EXTERNAL_MGMT_INGRESS=<icp-external-host>:8443
```

## Tips on Using Sbt

When at the `sbt` sub-command prompt:

- Get a list of tasks: `task -V`
- Start your app such that it will restart on code changes: `~reStart`
- Clean all built files (if the incremental build needs to be reset): `clean`

## Running the Automated Tests in Local Sandbox

- (Optional) To include tests for IBM agbot ACLs: `export EXCHANGE_AGBOTAUTH=myibmagbot:abcdef`
- (Optional) To include tests for IBM IAM platform key authentication:
```
export EXCHANGE_IAM_KEY=myiamplatformkey
export EXCHANGE_IAM_EMAIL=myaccountemail@something.com
export EXCHANGE_IAM_ACCOUNT=myibmcloudaccountid
```
- Run the automated tests in a second shell (with the exchange server still running in the first): `sbt test`
- Run just 1 of the the automated test suites (with the exchange server still running): `sbt "testOnly **.AgbotsSuite"`
- Run the performance tests: `src/test/bash/scale/test.sh` or `src/test/bash/scale/wrapper.sh 8`
- Make sure to run `primedb.sh` before running the  `AgbotsSuite` test class to run all of the tests.

## Code Coverage Report

  Code coverage is disabled in the project by default. The sbt command `sbt coverage` toggles scoverage checking on/off. To create a report of scoverage:
  
  - Execute `sbt coverage` to enable scoverage.
  - Run all tests see section above (`Running the Automated Tests in Local Sandbox`).
  - Create report running command `sbt coverageReport`.
  - Terminal will display where the report was written and provide a high-level percent summary.

## Linting

  Project uses Scapegoat. To use:
  
  - Run `sbt scapegoat`
  - Terminal will display where the report was written and provide a summary of found errors and warnings.

## Building and Running the Docker Container in Local Sandbox

- Update the version in `src/main/resources/version.txt`
- Add a second configuration file that is specific to running in the docker container:
  - `sudo mkdir -p /etc/horizon/exchange/docker`
  - `sudo cp /etc/horizon/exchange/config.json /etc/horizon/exchange/docker/config.json`
  - See [the Preconditions section](#preconditions) for the options for configuring postgresql to listen on an IP address that your exchange docker container will be able to reach. (Docker will not let it reach your host's `localhost` or `127.0.0.1` .)
  - Set the `jdbcUrl` field in this `config.json` to use that IP address, for example:
    - `"jdbcUrl": "jdbc:postgresql://192.168.1.9/postgres",`
- To compile your local code, build the exchange container, and run it locally, run:
  - `make .docker-exec-run-no-https`
  - If you need to rerun the container without changing any code:
    - `rm .docker-exec-run-no-https && make .docker-exec-run-no-https`
- Log output of the exchange svr can be seen via `docker logs -f exchange-api`, or might also go to `/var/log/syslog` depending on the docker and syslog configuration.
- Manually test container locally: `curl -sS -w %{http_code} http://localhost:8080/v1/admin/version`
- **Note:** The exchange-api does not support HTTPS until issue https://github.com/open-horizon/exchange-api/issues/259 is completed.
- Run the automated tests: `sbt test`
- **Note:** Swagger does not yet work in the local docker container.
- At this point you probably want to run `docker rm -f amd64_exchange-api` to stop your local docker container so it stops listening on your 8080 port. Otherwise you may be very confused when you go back to running the exchange via `sbt`, but it doesn't seem to be executing your tests.

### Notes About `config/exchange-api.tmpl`

- The `config/exchange-api.tmpl` is a application configuration template much like `/etc/horizon/exchange/config.json`. The template file itself is required for building a Docker image, but the content is not. It is recommend that the default content remain as-is when building a Docker image. 
- The content layout of the template exactly matches that of `/etc/horizon/exchange/config.json`, and the content of the config.json can be directly copied-and-pasted into the template. This will set the default Exchange configuration to the hard-coded specifications defined in the config.json when a Docker container is created.
- Alternatively, instead of using hard-coded values the template accepts substitution variables (default content of the `config/exchange-api.tmpl`). At container creation the utility `envsubst` will make a value substitution with any corresponding environmental variables passed into the running container by Docker, Kubernetes, OpenShift, or etc. For example:
    - `config/exchange-api.tmpl`:
        - "jdbcUrl": "$EXCHANGE_DB_URL"
    - Kubernetes config-map (environment variable passed to container at creation):
        - "$EXCHANGE_DB_URL=192.168.0.123"
    - Default `/etc/horizon/exchange/config.json` inside running container:
        - "jdbcUrl": "192.168.0.123"
- It is possible to mix-and-match hard-coded values and substitution values in the template.
- ***WARNING:*** `envsubst` will attempt to substitute any value containing a `$`, which will include the value of `api.root.password` if it is a hashed password. To prevent this either pass the environmental variable `ENVSUBST_CONFIG` with a garbage value, e.g. `ENVSUBST_CONFIG='$donotsubstituteanything'` (this will effectively disable `envsubst`), or pass it with a value containing the exact substitution variables `envsubst` is to substitute (`ENVSUBST_CONFIG='${EXCHANGE_DB_URL} ${EXCHANGE_DB_USER} ${EXCHANGE_DB_PW} ${EXCHANGE_ROOT_PW} ...'`), and of course you have to pass those environment variables values into the container.
    - By default `$ENVSUBST_CONFIG` is set to `$ENVSUBST_CONFIG=''` this causes `envsubst` to use its default opportunistic behavior and will attempt to make any/all substitutions where possible.
- It is also possible to directly pass a `/etc/horizon/exchange/config.json` to a container at creation using a bind/volume mount. This takes precedence over the content of the template `config/exchange-api.tmpl`. The directly passed config.json is still subject to the `envsubst` utility and the above warning still applies.

### Notes About the Docker Image Build Process

- See https://www.codemunity.io/tutorials/dockerising-akka-http/
- Uses the sbt-native-packager plugin. See the above URL for what to add to your sbt-related files
- Build docker image: `sbt docker:publishLocal`
- Manually build and run the exchange executable
  - `make runexecutable`
- To see the dockerfile that gets created:
  - `sbt docker:stage`
  - `cat target/docker/stage/Dockerfile`

## Test the Exchange with Anax

- If you will be testing with anax on another machine, push just the version-tagged exchange image to docker hub, so it will be available to the other machines: `make docker-push-version-only`
- Just the first time: on an ubuntu machine, clone the anax repo and define this e2edev script:
```
mkdir -p ~/src/github.com/open-horizon && cd ~/src/github.com/open-horizon && git clone git@github.com:open-horizon/anax.git
# See: https://github.com/open-horizon/anax/blob/master/test/README.md
if [[ -z "$1" ]]; then
    echo "Usage: e2edev <exchange-version>"
    return
fi
set -e
sudo systemctl stop horizon.service   # this is only needed if you normally use this machine as a horizon edge node
cd ~/src/github.com/open-horizon/anax
git pull
make clean
make
make fss   # this might not be needed
cd test
make
make test TEST_VARS="NOLOOP=1 TEST_PATTERNS=sall" DOCKER_EXCH_TAG=$1
make stop
make test TEST_VARS="NOLOOP=1" DOCKER_EXCH_TAG=$1
echo 'Now run: cd $HOME/src/github.com/open-horizon/anax/test && make realclean && sudo systemctl start horizon.service && cd -'
set +e
```
- Now run the test (this will take about 10 minutes):
```
e2edev <exchange-version>
```

## Deploying the Container to Staging or Production

- Push container to the docker hub registry: `make docker-push-only`
- Deploy the new container to the staging or production docker host
    - Ensure that no changes are needed to the /etc/horizon/exchange/config.json file
- Sniff test the new container : `curl -sS -w %{http_code} https://<exchange-host>/v1/admin/version`

## Building the Container for a Branch

To build an exchange container with code that is targeted for a git branch:
- Create a development git branch A (that when tested you will merge to branch B). Where A and B can be any branch names.
- Locally test the branch A exchange via sbt
- When all tests pass, build the container: `rm -f .docker-compile && make .docker-exec-run TARGET_BRANCH=B`
- The above command will create a container tagged like: 1.2.3-B
- Test the exchange container
- When all tests pass, push it to docker hub: `make docker-push-only TARGET_BRANCH=B`
- The above command will push the container tagged like 1.2.3-B and latest-B
- Create a PR to merge your dev branch A to canonical branch B

## Exchange root User

### Putting Hashed Password in config.json

The exchange root user password is set in the config file (`/etc/horizon/exchange/config.json`). But the password doesn't need to be clear text. You can hash the password with:
```
curl -sS -X POST -H "Authorization:Basic $HZN_ORG_ID/$HZN_EXCHANGE_USER_AUTH" -H "Content-Type: application/json" -d '{ "password": "PUT-PW-HERE" }' $HZN_EXCHANGE_URL/admin/hashpw | jq
```

And then put that hashed value in `/etc/horizon/exchange/config.json` in the `api.root.password` field.

### Disabling Root User

If you want to reduce the attack surface of the exchange, you can disable the exchange root user, because it is only needed under special circumstances. Before disabling root, we suggest you do:
- Create a local exchange user in the IBM org. (This can be used if you want to update the sample services, patterns, and policies at some point with `https://raw.githubusercontent.com/open-horizon/examples/master/tools/exchangePublishScript.sh`.):
  ```bash
  hzn exchange user create -u "root/root:PUT-ROOT-PW-HERE" -o IBM -A PUT-USER-HERE PUT-PW-HERE PUT-EMAIL-HERE
  ```

- Give 1 of the IBM Cloud users `admin` privilege:
  ```
  hzn exchange user setadmin -u "root/root:PUT-ROOT-PW-HERE" -o PUT-IBM-CLOUD-ORG-HERE PUT-USER-HERE true
  ```

Now you can disable root by setting `api.root.enabled` to `false` in `/etc/horizon/exchange/config.json`.

## Using TLS With The Exchange

- You need a PKCIS #12 cryptographic store (.pk12). https://en.wikipedia.org/wiki/PKCS_12
  - See Makefile targets `target/localhost.crt` (line 236), `/etc/horizon/exchange/localhost.p12` (line 243), and `truststore` (line 250) for a skeleton to use with OpenSSL.
  - OpenSSL is used for the creation of (1) self-signed certificate stating the application server is who it says it is, (2) the server's private key, and (3) the PKCS #12 which is just a portable secure store for everything.
  - The PKCS #12 is password protected. Set the environmental variable `EXCHANGE_TRUST_PW` when using the Makefile.
    - Set `export EXCHANGE_TRUST_PW=` when wishing to not have a password on the PKCS #12
- Set `api.tls.truststore` and `api.tls.password` in the Exchange's `/etc/horizon/echange/config.json` file.
  - `truststore` expects the absolute (full) path to your intended PCKS #12 as a string.
    - Setting this is the mechanism by which the Exchange knows to attempt to set up TLS in the application server.
    - Use `"truststore": null` to disable.
  - `password` expects the PKCS #12's password.
    - The Exchange will throw an error and self terminate on start if this password is not set or set `null`.
    - `api.tls.password` defaults to `null`.
    - When using a PKCS #12 that does not have a set password, set `api.tls.password` to `"password": "",` in the `/etc/horizon/exchange/config.json`.
  - See Makefile target `/etc/horizon/exchange/config-https.json` (line 201) for an idea.
- The default ports are `8080` for unencrypted traffic and `8083` for Encrypted.
  - These can be adjusted in the Exchange's `/etc/horizon/echange/config.json` file.
  - `api.service.portEncrypted` for changing the port listening for encrypted traffic.
  - `api.service.port` for changing the port listening for unencrypted traffic.
  - See Makefile target `/etc/horizon/exchange/config-https.json` (line 201) for an idea.
  - The Exchange is capable of hosting both HTTP and HTTPS traffic at the same time as well as mutually exclusively one. Freedom to mix-and-match.
    - HTTP and HTTPS are required to run on different ports. The Exchange always defaults to HTTP exclusively when in conflict.
    - If ports are manually undefined in the Exchange's `/etc/horizon/echange/config.json` file then HTTP on port `8080` is defaulted.
  - The Exchange does not support mixing HTTP and HTTPS traffic on either port.
- Only `TLSv1.3` and `TLSv1.2` HTTPS traffic is supported by the Exchange with TLS enabled.
  - `TLS_AES_256_GCM_SHA384` is the only supported TLSv1.3 cipher in the Exchange.
  - The `TLSv1.3` cipher `TLS_CHACHA20_POLY1305_SHA256` is available starting in Java 14.
  - The supported ciphers for `TLSv1.2` are `TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384` and `TLS_DHE_RSA_WITH_AES_256_GCM_SHA384`.
- [Optional] When using HTTPS with the Exchange the PostgreSQL database can also be configured with TLS turned on.
  - The Exchange does not require an SSL enabled PostgreSQL database to function with TLS enabled. 
  - See https://www.postgresql.org/docs/13/runtime-config-connection.html#RUNTIME-CONFIG-CONNECTION-SSL for more information.
  - Requires separate certificate (.cert) and private key (.key) files.
    - See Makefile target `/postgres.crt` (line 138) for an idea.
  - Requires flag `ssl=true` to be set.
  - Requires flag `ssl_min_protocol_version=TLSv1.3` to be set.
  - See makefile target `target/docker/.run-docker-db-postgres-https` for an idea and how to do this for a PostgreSQL Docker container.
- The Exchange does not support HTTP traffic redirects to HTTPS server-side. HTTPS traffic must be intended client-side.
- See the Makefile target chain `target/docker/.run-docker-icp-https` (line 272) for idea of a running Exchange and database in docker containers using TLS.
- Do to technical limitations the Swagger page will only refer to the Exchange's HTTPS traffic port.

## Configuration Parameters

`src/main/resources/config.json` is the default configuration file for the Exchange. This file is bundled in the Exchange jar. To run the exchange server with different values, copy this to `/etc/horizon/exchange/config.json`. In your version of the config file, you only have to set what you want to override.

### api.acls

| Parameter Name | Description       |
|----------------|-------------------|
| AdminUser      |                   |
| Agbot          |                   |
| Anonymous      | Not actually used |
| HubAdmin       |                   |
| Node           |                   |
| SuperUser      |                   |
| User           |                   |

### api.akka

Akka Actor: https://doc.akka.io/docs/akka/current/general/configuration-reference.html
</br>
Akka-Http: https://doc.akka.io/docs/akka-http/current/configuration.html

| Parameter Name                     | Description                             |
|------------------------------------|-----------------------------------------|
| akka.http.server.backlog           |                                         |
| akka.http.server.bind-timeout      |                                         |
| akka.http.server.idle-timeout      |                                         |
| akka.http.server.linger-timeout    |                                         |
| akka.http.server.max-connections   |                                         |
| akka.http.server.pipelining-limit  |                                         |
| akka.http.server.request-timeout   |                                         |
| akka.http.server.server-header     | Removes the Server header from response |

### api.cache

| Parameter Name         | Description                                                     |
|------------------------|-----------------------------------------------------------------|
| authDbTimeoutSeconds   | Timeout for db access for critical auth info when cache missing |
| IAMusersMaxSize        | The users that are backed by IAM users                          |
| IAMusersTtlSeconds     |                                                                 |
| idsMaxSize             | Includes: local exchange users, nodes, agbots (all together)    |
| idsTtlSeconds          |                                                                 |
| resourcesMaxSize       | Each of: users, agbots, services, patterns, policies            |
| resourcesTtlSeconds    |                                                                 |
| type                   | Currently guava is the only option                              |

### api.db

| Parameter Name               | Description                                                          |
|------------------------------|----------------------------------------------------------------------|
| acquireIncrement             |                                                                      |
| driverClass                  |                                                                      |
| idleConnectionTestPeriod     | In seconds; 0 disables                                               |
| initialPoolSize              |                                                                      |
| jdbcUrl                      | The back-end db the exchange uses                                    |
| maxConnectionAge             | In seconds; 0 is infinite                                            |
| maxIdleTime                  | In seconds; 0 is infinite                                            |
| maxIdleTimeExcessConnections | In seconds; 0 is infinite; culls connections down to the minPoolSize |
| maxPoolSize                  |                                                                      |
| maxStatementsPerConnection   | 0 disables; prepared statement caching per connection                |
| minPoolSize                  |                                                                      |
| numHelperThreads             |                                                                      |
| password                     |                                                                      |
| queueSize                    | -1 for unlimited, 0 to disable                                       |
| testConnectionOnCheckin      |                                                                      |
| upgradeTimeoutSeconds        |                                                                      |
| user                         |                                                                      |

#### api.defaults

- ##### api.defaults.businessPolicy
  | Parameter Name             | Description                                       |
  |----------------------------|---------------------------------------------------|
  | check_agreement_status     |                                                   |
  | missing_heartbeat_interval | Used if the service.nodeHealth section is omitted |
- ##### api.defaults.msgs
  | Parameter Name                | Description                                                            |
  |-------------------------------|------------------------------------------------------------------------|
  | expired_msgs_removal_interval | Number of seconds between deletions of expired node and agbot messages |
- ##### api.defaults.pattern
  | Parameter Name             | Description                                        |
  |----------------------------|----------------------------------------------------|
  | missing_heartbeat_interval | Used if the services.nodeHealth section is omitted |
  | check_agreement_status     |                                                    |

#### api.limits

| Parameter Name         | Description                                                                                                                 |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| maxAgbots              | Maximum number of agbots 1 user is allowed to create, 0 for unlimited                                                       |
| maxAgreements          | Maximum number of agreements 1 node or agbot is allowed to create, 0 for unlimited                                          |
| maxBusinessPolicies    | Maximum number of business policies 1 user is allowed to create, 0 for unlimited                                            |
| maxManagementPolicies  | Maximum number of management policies 1 user is allowed to create, 0 for unlimited                                          |
| maxMessagesInMailbox   | Maximum number of msgs currently in 1 node or agbot mailbox (the sending side is handled by rate limiting), 0 for unlimited |
| maxNodes               | Maximum number of nodes 1 user is allowed to create, 0 for unlimited                                                        |
| maxPatterns            | Maximum number of patterns 1 user is allowed to create, 0 for unlimited                                                     |
| maxServices            | Maximum number of services 1 user is allowed to create, 0 for unlimited                                                     |

#### api.logging

| Parameter Name    | Description                                                                                 |
|-------------------|---------------------------------------------------------------------------------------------|
| level             | For possible values, see http://logback.qos.ch/apidocs/ch/qos/logback/classic/Level.html    |

#### api.resourceChanges

| Parameter Name     | Description                                                                                                                                                                                               |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| cleanupInterval    | Number of seconds between pruning the resourcechanges table in the db of expired changes - 3600 is 1 hour                                                                                                 |
| maxRecordsCap      | Maximum number of records the notification framework route will return                                                                                                                                    |
| ttl                | Number of seconds to keep the history records of resource changes (14400 is 4 hours). When agents miss 1 or more heartbeats, they reset querying the /changes route, so they do not need very old entries |

#### api.root

| Parameter Name   | Description                                            |
|------------------|--------------------------------------------------------|
| enabled          | If set to false it will not honor the root credentials |
| password         | Set this in your own version of this config file       |

#### api.service

| Parameter Name                      | Description                                                                    |
|-------------------------------------|--------------------------------------------------------------------------------|
| host                                |                                                                                |
| port                                | Services HTTP traffic                                                          |
| portEncrypted                       | Services HTTPS traffic                                                         |
| shutdownWaitForRequestsToComplete   | Number of seconds to let in-flight requests complete before exiting the server |

#### api.tls

| Parameter Name | Description                                                                                                |
|----------------|------------------------------------------------------------------------------------------------------------|
| password       | Truststore's password                                                                                      |
| truststore     | Absolute path and name of your pkcs12 (.p12) truststore that contains your tls certificate and private key |

## Todos that may be done in future versions

- Granular (per org) service ACL support:
    - add Access type of BROWSE that will allow to see these fields of services:
      - label, description, public, documentation, url, version, arch
    - add acl table and resource with fields:
      - org
      - resource (e.g. service)
      - resourceList (for future use)
      - requester (org/username)
      - access
    - add GET, PUT, POST to manage these acls
    - add checks on GET service to use these acls
    - (later) consider adding a GET that returns all services of orgs of orgType=IBM
- Add rest method to delete a user's stale devices (carl requested)
- Add ability to change owner of node
- Add patch capability for node registered services
- Consider:
    - detect if pattern contains 2 services that depend on the same exclusive MS
    - detect if a pattern is updated with service that has userInput w/o default values, and give warning
    - Consider changing all creates to POST, and update (via put/patch) return codes to 200
