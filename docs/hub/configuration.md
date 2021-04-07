---

copyright:
years: 2021
lastupdated: "2021-02-20"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Configure {{site.data.keyword.ieam}}

## Additional ORG level configuration for high scale environments

To support high scale environments greater than 10,000 edge nodes, adjust the heartbeat intervals that the edge nodes use to check for changes. 

The following command should be issued by a super user:
```
hzn exchange org update --heartbeatmin=60 --heartbeatmax=900 --heartbeatadjust=60 <org_name>
```
{: codeblock}

If multiple ORGS used, the command should be issued for each ORG supporting more than 10,000 edge nodes.
