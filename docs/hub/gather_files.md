---
copyright: Contributors to the Open Horizon project
years: 2021 - 2026
title: Gather edge node files
description: Documentation for Gather edge node files
lastupdated: 2025-10-17
nav_order: 4
parent: Install Open Horizon
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Gather edge node files
{: #prereq_horizon}

Several files are needed to install the {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) agent on your edge devices and edge clusters and register them with {{site.data.keyword.ieam}}. This content guides you through bundling the files that are needed for your edge nodes. The following script can be used to push the {{site.data.keyword.horizon}} packages into the CSS (Cloud Sync Service) component of the Model Management System. Copy the contents of the script and save them in a file. Fill in the correct values for variables that are marked with `<FILL_IN>` before executing. 

Note: If you have not already installed the horizon-cli package on this host, do that now.

```bash
#!/bin/bash

RELEASE="v2.32.0-1739"     # Set to whatever release is desired

PKG="oh-packages"

EXCHANGE_ROOT_PW=<FILL_IN>
export HZN_EXCHANGE_USER_AUTH=root/root:${EXCHANGE_ROOT_PW}

export HZN_LISTEN_IP=<FILL_IN>
export HZN_TRANSPORT=${HZN_TRANSPORT:-http}
export HZN_EXCHANGE_URL=${HZN_EXCHANGE_URL:-${HZN_TRANSPORT}:${HZN_LISTEN_IP}:3090v1}
export HZN_FSS_CSSURL=${HZN_FSS_CSSURL:-${HZN_TRANSPORT}://${HZN_LISTEN_IP}:9443}
export HZN_AGBOT_URL=${HZN_AGBOT_URL:-${HZN_TRANSPORT}://${HZN_LISTEN_IP}:3111}
export HZN_FDO_SVC_URL=${HZN_FDO_SVC_URL:-${HZN_TRANSPORT}://${HZN_LISTEN_IP}:9008/api}
EXTRA_PARMS="-k /tmp/agent-install.crt"    # Only needed if using https

# Fill username and personal access token to GHCR
GHCR_USERNAME=<FILL_IN>
GHCR_PAT=<FILL_IN>

export REGISTRY_USERNAME=${GHCR_USERNAME}
export REGISTRY_PASSWORD=${GHCR_PAT}

FILES=(
  horizon-agent-linux-deb-amd64.tar.gz
  horizon-agent-linux-deb-arm64.tar.gz
  horizon-agent-linux-deb-armhf.tar.gz
  horizon-agent-linux-deb-ppc64el.tar.gz
  horizon-agent-linux-deb-s390x.tar.gz
  horizon-agent-linux-rpm-ppc64le.tar.gz
  horizon-agent-linux-rpm-s390x.tar.gz
  horizon-agent-linux-rpm-x86_64.tar.gz
  horizon-agent-{{site.data.keyword.macOS_notm}}-pkg-arm64.tar.gz
  horizon-agent-{{site.data.keyword.macOS_notm}}-pkg-x86_64.tar.gz
)

for FILE in ${FILES[@]}; do

	echo $FILE
	rm -f ${FILE}
	wget https://github.com/open-horizon/anax/releases/download/${RELEASE}/${FILE}
	rc=$?
	if [[ $rc -ne 0 ]]; then
		echo "Error... Failed retrieving ${FILE}... Exiting"
		exit 2
        fi

	PLATFORM=$( echo "${FILE}" | cut -d - -f 3 )
	DIST=$( echo "${FILE}" | cut -d - -f 4 )
	ARCH=$( echo "${FILE}" | cut -d - -f 5 | cut -d . -f 1 )

	if [[ "${ARCH}" == "ppc64le" ]]; then
		ARCH="ppc64el"
	fi

	DEST=${PKG}/${PKG}/${PLATFORM}/${DIST}/${ARCH}
	mkdir -p ${DEST}

	tar -C ${DEST} -zxf ${FILE}
done

# Build tar.gz of all OH packages that edgeNodeFiles is expecting
rm ${PKG}.tar
cd ${PKG}
tar -cf ../${PKG}.tar *
cd ..
rm ${PKG}.tar.gz
gzip ${PKG}.tar

edgeNodeFiles.sh ALL -c -r ghcr.io/open-horizon -p ${PKG} ${EXTRA_PARMS}
```
{: codeblock}

## What's next

Before edge nodes are set up, you or your node technicians must create authentication variables and gather other environment variable values. Follow the steps in [Prepare for setting up edge nodes](prepare_for_edge_nodes.md).
