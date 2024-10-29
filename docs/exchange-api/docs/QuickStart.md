---
copyright:
years: 2024
lastupdated: "2024-10-22"
layout: page
title: "Exchange API Server"
description: "Quick start"

nav_order: 3
parent: Management Hub
---

# Exchange API Server quick start

## Intro

This document describes the environment and the set of steps aiming to create a
local development and debugging environment.

## Prerequisites

* OS: Ubuntu 24.04 LTS.

## Dependencies

* [Java 17](https://www.java.com/en/)
* [SBT](https://www.scala-sbt.org/)
* [PostgreSQL](https://www.postgresql.org/)

## Installation

### Create a new user (optional)

For development purposes recommended not to use root user. Command below will create
a new Ubuntu user.

```bash
useradd -d /home/new_user -s /bin/bash -m new_user
sudo passwd new_user
usermod -aG sudo new_user
```

### Install Java 17

```bash
sudo apt-get update
sudo apt install openjdk-17-jdk -y
```

### Install SBT

```bash
sudo apt-get update
sudo apt-get install apt-transport-https curl gnupg -yqq
echo "deb https://repo.scala-sbt.org/scalasbt/debian all main" | sudo tee /etc/apt/sources.list.d/sbt.list
echo "deb https://repo.scala-sbt.org/scalasbt/debian /" | sudo tee /etc/apt/sources.list.d/sbt_old.list
curl -sL "https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x2EE0EA64E40A89B84B2DF73499E82A75642AC823" | sudo -H gpg --no-default-keyring --keyring gnupg-ring:/etc/apt/trusted.gpg.d/scalasbt-release.gpg --import
sudo chmod 644 /etc/apt/trusted.gpg.d/scalasbt-release.gpg
sudo apt-get update
sudo apt-get install sbt
```

### Install Postgresql

```bash
sudo apt-get update
sudo apt-get install postgresql
sudo systemctl status postgresql
```

### Configure firewall rule for Postgresql port 5432

```bash
sudo iptables -A INPUT -p tcp --dport 5432 -m state --state NEW,ESTABLISHED -j ACCEPT
```

### Create a new DB

```bash
sudo -u postgres psql
postgres=# CREATE USER new_user WITH PASSWORD 'password';
postgres=# CREATE DATABASE horizon OWNER new_user;
\q
```

### Test connection to DB

```bash
psql "host=localhost dbname=horizon user=kevin password='password'"
```

### Export environment variables

```bash
export EXCHANGE_DB_NAME=openhorizon
export EXCHANGE_DB_PW=password
export EXCHANGE_DB_USER=new_user
export EXCHANGE_ROOT_PW=root_password
```

### Clone exchange-api and run it

```bash
https://github.com/open-horizon/exchange-api.git
~/exchange-api$ sbt
sbt:amd64_exchange-api> reStart
```
