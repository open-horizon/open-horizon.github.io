---
copyright: Contributors to the Open Horizon project
years: 2022 - 2025
title: Exchange API Server
description: Open Horizon Exchange API Documentation
lastupdated: 2025-06-03
nav_order: 3
parent: Management Hub
layout: page
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
    - set this to your IP:

      ```bash
      export MY_IP=<my-ip>
      echo "host all all $MY_IP/32 trust" >> /usr/local/var/postgres/pg_hba.conf
      sed -i -e "s/#listen_addresses = 'localhost'/listen_addresses = '$MY_IP'/" /usr/local/var/postgres/postgresql.conf
      brew services start postgresql
      ```

      or if it is already running, `brew services restart postgresql`
  - Or if your test machine is on a private subnet:
    - trust all clients on your subnet:

      ```bash
      echo 'host all all 192.168.1.0/24 trust' >> /usr/local/var/postgres/pg_hba.conf
      ```

    - listen on all interfaces:

      ```bash
      sed -i -e "s/#listen_addresses = 'localhost'/listen_addresses = '*'/" /usr/local/var/postgres/postgresql.conf
      brew services start postgresql` or if it is already running `brew services restart postgresql
      ```

  - Or you can run postgresql in a container and connect it to the docker network `exchange-api-network`
  - Test:

    ```bash
    psql "host=$MY_IP dbname=postgres user=<myuser> password=''"
    ```

- The following minimum set of environment variables are required to run an Exchange instance. Additional configuration options are available via TypeSafe Config.

  ```bash
  # Example
  export EXCHANGE_DB_NAME=openhorizon
  export EXCHANGE_DB_PW=mydbuserpasswd
  export EXCHANGE_DB_USER=mydbuser
  export EXCHANGE_ROOT_PW=myrootpasswd
  ```

- If someone hasn't done it already, create the TLS private key and certificate:

  ```bash
  # Example
  export EXCHANGE_KEY_PW=<pass-phrase>
  make gen-key
  ```

- Otherwise, get files `exchangecert.pem`, `keypassword`, and `keystore` from the person who created them and put them in `./keys/etc`.

## Building and Running in Local Sandbox

- `sbt`
- `reStart`
- Once the server starts, to see the swagger output, browse: [http://localhost:8080/v1/swagger](http://localhost:8080/v1/swagger){:target="_blank"}{: .externalLink}
- To try a simple rest method curl: `curl -X GET "http://localhost:8080/v1/admin/version"`. You should get the exchange version number as the response.
- When testing the exchange in an OpenShift Cluster the variables `EXCHANGE_IAM_ORG`, `EXCHANGE_IAM_KEY` and `EXCHANGE_MULT_ACCOUNT_ID` must be set accordingly.
- A convenience script `src/test/bash/primedb.sh` can be run to prime the DB with some exchange resources to use in manually testing:

```bash
# Example
export EXCHANGE_USER=<my-user-in-IBM-org>
export EXCHANGE_PW=<my-pw-in-IBM-org>
src/test/bash/primedb.sh
```

- `primedb.sh` will only create what doesn't already exist, so it can be run again to restore some resources you have deleted.
- To locally test the exchange against an existing ICP cluster:

```bash
# Example
export ICP_EXTERNAL_MGMT_INGRESS=<icp-external-host>:8443
```

## Tips on Using Sbt

When at the `sbt` sub-command prompt:

- Get a list of tasks: `task -V`
- Start your app such that it will restart on code changes: `reStart`
- Clean all built files (if the incremental build needs to be reset): `clean`
- Check and attempt to resolve any binary incompatibilities in dependency stack: `evicted`

## Running the Automated Tests in Local Sandbox

- (Optional) To include tests for IBM agbot ACLs: `export EXCHANGE_AGBOTAUTH=myibmagbot:abcdef`
- (Optional) To include tests for IBM IAM platform key authentication:

```bash
# Example
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

  - See [the Preconditions section](#preconditions) for the options for configuring postgresql to listen on an IP address that your exchange docker container will be able to reach. (Docker will not let it reach your host's `localhost` or `127.0.0.1` .)
  - Set the `EXCHANGE_DB_...` environment variables to use that IP address, for example:

    ```bash
    # Example
    export EXCHANGE_DB_HOST=192.168.1.9
    export EXCHANGE_DB_NAME=postgres
    export EXCHANGE_DB_PORT=5432
    ```

- To compile your local code, build the exchange container, and run it locally, run:

  ```bash
  make .docker-exec-run-no-https
  ```

  - If you need to rerun the container without changing any code:

    ```bash
    rm .docker-exec-run-no-https && make .docker-exec-run-no-https
    ```

- Log output of the exchange svr can be seen via `docker logs -f exchange-api`, or might also go to `/var/log/syslog` depending on the docker and syslog configuration.
- Manually test container locally: `curl -sS -w %{http_code} http://localhost:8080/v1/admin/version`
- Run the automated tests: `sbt test`
- **Note:** Swagger does not yet work in the local docker container.
- At this point you probably want to run `docker rm -f amd64_exchange-api` to stop your local docker container so it stops listening on your 8080 port. Otherwise you may be very confused when you go back to running the exchange via `sbt`, but it doesn't seem to be executing your tests.


### Notes About the Docker Image Build Process

- Uses the sbt-native-packager plugin.
- Build docker image: `sbt docker:publishLocal`
- Manually build and run the exchange executable
  - `make runexecutable`
- To see the dockerfile that gets created:
  - `sbt docker:stage`
  - `cat target/docker/stage/Dockerfile`

## Test the Exchange with Anax

- If you will be testing with anax on another machine, push just the version-tagged exchange image to docker hub, so it will be available to the other machines: `make docker-push-version-only`
- Just the first time: on an ubuntu machine, clone the anax repo and define this e2edev script:

```bash
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

```bash
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

The exchange root user password is set via the environment variable `EXCHANGE_ROOT_PW`.

And then set the environment variable `export EXCHANGE_ROOT_PW=rootuserpassword` and restart the Exchange.

### Disabling Root User

If you want to reduce the attack surface of the exchange, you can disable the exchange root user, because it is only needed under special circumstances. Before disabling root, we suggest you do:

- Create a local exchange user in the IBM org. (This can be used if you want to update the sample services, patterns, and policies at some point with `https://raw.githubusercontent.com/open-horizon/examples/master/tools/exchangePublishScript.sh`.):

  ```bash
  hzn exchange user create -u "root/root:PUT-ROOT-PW-HERE" -o IBM -A PUT-USER-HERE PUT-PW-HERE PUT-EMAIL-HERE
  ```

- Give 1 of the IBM Cloud users `admin` privilege:

  ```bash
  hzn exchange user setadmin -u "root/root:PUT-ROOT-PW-HERE" -o PUT-IBM-CLOUD-ORG-HERE PUT-USER-HERE true
  ```

Now you can disable root by setting the environment variable `export EXCHANGE_ROOT_ENABLED=false` or unsetting the environment variable `unset EXCHANGE_ROOT_PW`.

## Using TLS With The Exchange

- You need a PKCIS #12 cryptographic store (.pk12). https://en.wikipedia.org/wiki/PKCS_12
  - See Makefile targets `target/localhost.crt` (line 236), `/etc/horizon/exchange/localhost.p12` (line 243), and `truststore` (line 250) for a skeleton to use with OpenSSL.
  - OpenSSL is used for the creation of (1) self-signed certificate stating the application server is who it says it is, (2) the server's private key, and (3) the PKCS #12 which is just a portable secure store for everything.
  - The PKCS #12 is password protected.
    - Set `export EXCHANGE_TRUST_PW=` when wishing to not have a password on the PKCS #12
- Set the environement variables `EXCHANGE_TLS_PASSWORD` and `EXCHANGE_TLS_TRUSTSTORE`
  - ```bash
    # Example
    export EXCHANGE_TLS_PASSWORD=mytruststorepassword
    export EXCHANGE_TLS_TRUSTSTORE=/etc/horizon/exchange/localhost.p12
    ```
  - `truststore` expects the absolute (full) path to your intended PCKS #12 as a string.
    - Setting this is the mechanism by which the Exchange knows to attempt to set up TLS in the application server.
    - Use `"truststore": null` to disable.
  - `password` expects the PKCS #12's password.
    - The Exchange will throw an error and self terminate on start if this password is not set or set `null`.
    - `EXCHANGE_TLS_PASSWORD` defaults to `null`.
    - When using a PKCS #12 that does not have a set password, set the environment variable `export EXCHANGE_TLS_PASSWORD=""` to an empty string.
- The default ports are `8080` for unencrypted traffic and `8083` for Encrypted.
  - These can be adjusted via the environment variables `EXCHANGE_PEKKO_HTTP_PORT` and `EXCHANGE_PEKKO_HTTPS_PORT`.
  - The Exchange is capable of hosting both HTTP and HTTPS traffic at the same time as well as mutually exclusively one. Freedom to mix-and-match.
    - HTTP and HTTPS are required to run on different ports. The Exchange always defaults to HTTP exclusively when in conflict.
    - If ports are manually undefined in the Exchange's HTTP on port `8080` is defaulted.
  - The Exchange does not support mixing HTTP and HTTPS traffic on either port.
- Only `TLSv1.3` is supported by the Exchange with TLS enabled.
  - `TLS_AES_256_GCM_SHA384` and `TLS_CHACHA20_POLY1305_SHA256` are the only supported TLSv1.3 ciphers in the Exchange.
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
