---

copyright:
years: 2021 - 2023
lastupdated: "2023-02-17"
layout: page
title: "Developer learning path"
description: A set of sequential resources for the developer learning about Open Horizon

parent: Quick Start
nav_order: 5
---

# Edge developer learning path

This is a set of resources compiled from new developers who have found them to be useful.  If you have any proposed improvements, please [open an issue](https://github.com/open-horizon/open-horizon.github.io/issues/new){:target="_blank"}{: .externalLink} and suggest it.

## Resources to learn more about the Open Horizon components

The following set of resources consisting of links to past Open Horizon meetings, videos and readme sections are useful to get started with the various segments of the Open Horizon project (excluding the SDO-services and Edge Sync Service).

1. Introduction:

    a. Get an idea of what Open Horizon is all about from [https://www.lfedge.org/projects/openhorizon/](https://www.lfedge.org/projects/openhorizon/){:target="_blank"}{: .externalLink}

    b. Introductory videos by OH member Glen Darling
    1. An overview of Open Horizon - [video](https://www.youtube.com/watch?v=g59RTLV22fw&list=PLgohd895XSUddtseFy4HxCqTqqlYfW8Ix&index=2){:target="_blank"}{: .externalLink}.
    2. More technical details - [video](https://www.youtube.com/watch?v=WyZaKiI4wLE&list=PLgohd895XSUddtseFy4HxCqTqqlYfW8Ix&index=7){:target="_blank"}{: .externalLink}.

    c. An overview of the Agent's role in OH - First [meeting recording](https://zoom.us/rec/share/tPFREb__zGpObc-V10GPVPA6IKT7eaa81iUbrPcOz0nRkgZlvoon4BvQjZ_73kqH?startTime=1595863993000){:target="_blank"}{: .externalLink} of the Agent WG.

    d. Another descriptory video from the [meeting recording](https://zoom.us/rec/play/87yiQniSZ0VtHPh6Roz_HLyfOGcDV6Cpx2nosQhR4Z9Ed52JlGB3bxYBbAVYwDzZpWJxu-UfaToBTab8.85GZKncg_KFrO0uP?continueMode=true&_x_zm_rtaid=oC4Wb8hjTtCHn49H1M6i9g.1613742221653.b2e466b17a6979e0fba21e9209e5acfc&_x_zm_rhtaid=626){:target="_blank"}{: .externalLink} of the QA Working Group.

2. Services, policies and patterns (Important)

    a. Glen’s introductory [video](https://www.youtube.com/watch?v=alcHKc3Upbk&list=PLgohd895XSUddtseFy4HxCqTqqlYfW8Ix&index=4){:target="_blank"}{: .externalLink} on patterns and policies.

    b. An [introduction](https://zoom.us/rec/share/6eheFpXwq3JLYo3duXDBf7wDLp-5T6a82nRN-vRfzUuBm-ELkKqZmz1kthR-uAAf?startTime=1598282577000){:target="_blank"}{: .externalLink} to services.

    c. [Service networking](https://www.youtube.com/watch?v=jUeMvr87jz8&list=PLgohd895XSUddtseFy4HxCqTqqlYfW8Ix&index=8){:target="_blank"}{: .externalLink} demo.

3. Getting started:

    a. Get [started](https://zoom.us/rec/play/uJV_dOqhp2g3TNLGswSDAqMvW47uffmsgylM8_AMzE_hWngLYACmbrEQYbR6DRGSdV9GsMJms2rXWT5P){:target="_blank"}{: .externalLink} with contributing to Anax.

    b. Helpful installation guides from the docs
    1. [Install and setup environment](../../common-requests/install.md)
    2. [How to use](../../common-requests/use.md).

    c. Using the all-in-one deployment (for the hands on practicals next)
    1. [Recording](https://zoom.us/rec/play/IlrDE_zkKkCcjYrqNp5RSo1-Up2EcIrkTlMndE3BtjtPK8GvZ8FGD3914gZGjZMRp4rltFFrslaEo5Xq.0QGVy6YtQRaZTZ55?startTime=1598534658000&_x_zm_rtaid=oC4Wb8hjTtCHn49H1M6i9g.1613742221653.b2e466b17a6979e0fba21e9209e5acfc&_x_zm_rhtaid=626){:target="_blank"}{: .externalLink} from the Management Hub WG.
    2. [Readme](/docs/mgmt-hub/docs/index.md) guide.

    d. Hands on practical
    1. [Demo](https://www.youtube.com/watch?v=Fk9zJyExELU&list=PLgohd895XSUddtseFy4HxCqTqqlYfW8Ix&index=3){:target="_blank"}{: .externalLink} - without policies.
    2. [Advanced](https://www.youtube.com/watch?v=vgUuOIefamA&list=PLgohd895XSUddtseFy4HxCqTqqlYfW8Ix&index=5){:target="_blank"}{: .externalLink} - deploying with patterns vs policies.
    3. Glen's Easy Open Horizon [repository](https://github.com/TheMosquito/easy-open-horizon){:target="_blank"}{: .externalLink}.

4. Useful references

    a. [Setup](https://github.com/open-horizon/anax/tree/master/test){:target="_blank"}{: .externalLink} e2edev test environment

    b. [Create](https://github.com/open-horizon/examples/blob/master/edge/services/helloworld/CreateService.md){:target="_blank"}{: .externalLink} your own service.

    c. [Deploy](https://github.com/open-horizon/examples/tree/master/edge/services/helloworld){:target="_blank"}{: .externalLink} your own service.

    d. Get [started](https://github.com/open-horizon/exchange-api/blob/master/README.md){:target="_blank"}{: .externalLink} with contributions to exchange-api.

## Sequential tasks to gradually introduce you to common features

Here is a suggested list that is designed to progressively create familiarity with all of the common features of the Open Horizon platform.

1. **Get started**: Install all-in-one

2. **Get familiar**: unregister node, re-register node, (optionally add a node), publish an example service

3. **Get published**: Create a service definition file for an existing container and publish it to the exchange, then register your node for the service.

4. **Get containerized**: Take an existing (micro-)service and turn it into a Docker container, then publish and register.

5. **Get patterned**: Compose a pattern definition file of several existing services, publish, register.

6. **Make policy**: Create/modify your node policy file and publish to exchange.  Create a business/deployment policy and confirm that agreement made and service deployed.

7. **Operator?**  If you have a cluster available, make an operator to deploy your service using Glen's Operator Helper.

8. **In Sync**: Get the sync service to sync a hello world file.

9. **Sync Squared**: Using Glen's MMS Helper, modify a service to watch for a file dependency to be updated.
