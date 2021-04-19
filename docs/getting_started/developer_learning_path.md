---

copyright:
years: 2021
lastupdated: "2021-02-20"
layout: page
title: "Developer Learning Path"
description: A set of sequential resources for the developer learning about Open Horizon

---

## Introduction

This is a set of resources compiled from new developers who have found them to be useful.  If you have any proposed improvements, please [open an issue](https://github.com/open-horizon/open-horizon.github.io/issues/new) and suggest it.

## Resources to learn more about the Open Horizon components

> NOTE: this section is contributed by Debabrata Mandal.

Having spent about a week learning Open Horizon and its different components I think that there is already enough resources for an absolute beginner. It is just they are a bit scattered over the place and not properly hyperlinked. Although I have just scratched the surface, I feel the ones below could be helpful for any newcomer:

1. Introduction:

    a. [https://www.lfedge.org/projects/openhorizon/](https://www.lfedge.org/projects/openhorizon/)

    b. Glen Darling’s introductory videos [1](https://www.youtube.com/watch?v=g59RTLV22fw&list=PLgohd895XSUddtseFy4HxCqTqqlYfW8Ix&index=2), [2](https://www.youtube.com/watch?v=WyZaKiI4wLE&list=PLgohd895XSUddtseFy4HxCqTqqlYfW8Ix&index=7).

    c. First [meeting recording](https://zoom.us/rec/share/tPFREb__zGpObc-V10GPVPA6IKT7eaa81iUbrPcOz0nRkgZlvoon4BvQjZ_73kqH?startTime=1595863993000) of the Agent Working Group.

    d. First [meeting recording](https://zoom.us/rec/play/87yiQniSZ0VtHPh6Roz_HLyfOGcDV6Cpx2nosQhR4Z9Ed52JlGB3bxYBbAVYwDzZpWJxu-UfaToBTab8.85GZKncg_KFrO0uP?continueMode=true&_x_zm_rtaid=oC4Wb8hjTtCHn49H1M6i9g.1613742221653.b2e466b17a6979e0fba21e9209e5acfc&_x_zm_rhtaid=626) of the QA Working Group.

2. Detailed explanation of services, policies and patterns

    a. Glen’s videos [1](https://www.youtube.com/watch?v=alcHKc3Upbk&list=PLgohd895XSUddtseFy4HxCqTqqlYfW8Ix&index=4), [2](https://www.youtube.com/watch?v=jUeMvr87jz8&list=PLgohd895XSUddtseFy4HxCqTqqlYfW8Ix&index=8).

    b. Agent Working Group’s [meeting recording](https://zoom.us/rec/share/6eheFpXwq3JLYo3duXDBf7wDLp-5T6a82nRN-vRfzUuBm-ELkKqZmz1kthR-uAAf?startTime=1598282577000).

    c. [Service networking](https://www.youtube.com/watch?v=jUeMvr87jz8&list=PLgohd895XSUddtseFy4HxCqTqqlYfW8Ix&index=9) video.

3. Getting started:
    a. Anax - meeting [recording](https://zoom.us/rec/play/uJV_dOqhp2g3TNLGswSDAqMvW47uffmsgylM8_AMzE_hWngLYACmbrEQYbR6DRGSdV9GsMJms2rXWT5P).

    b. Installation - from docs [1](https://open-horizon.github.io/common-requests/install.html), [2](https://open-horizon.github.io/common-requests/use.html).

    c. Using the all-in-one deployment (for the hands on practicals) - Management Hub’s [meeting recording](https://zoom.us/rec/play/IlrDE_zkKkCcjYrqNp5RSo1-Up2EcIrkTlMndE3BtjtPK8GvZ8FGD3914gZGjZMRp4rltFFrslaEo5Xq.0QGVy6YtQRaZTZ55?startTime=1598534658000&_x_zm_rtaid=oC4Wb8hjTtCHn49H1M6i9g.1613742221653.b2e466b17a6979e0fba21e9209e5acfc&_x_zm_rhtaid=626), [doc](https://github.com/open-horizon/devops/tree/master/mgmt-hub).

    d. Hands on practical - Mosquito's Easy Open Horizon [repo](https://github.com/TheMosquito/easy-open-horizon) and videos [1](https://www.youtube.com/watch?v=Fk9zJyExELU&list=PLgohd895XSUddtseFy4HxCqTqqlYfW8Ix&index=3), [2](https://www.youtube.com/watch?v=vgUuOIefamA&list=PLgohd895XSUddtseFy4HxCqTqqlYfW8Ix&index=5).

    e. [Quick start](https://github.com/dcmartin/open-horizon/blob/master/QUICKSTART.md) and [helloworld example](https://github.com/dcmartin/open-horizon/blob/master/docs/HELLO_WORLD.md) from dcmartin’s repo.

4. There is also a lot of information available in these specific readme files ([1](https://github.com/open-horizon/anax/tree/master/test), [2](https://github.com/open-horizon/examples/tree/master/edge/services/helloworld), [3](https://github.com/open-horizon/exchange-api/blob/master/README.md)) of the project's repositories.

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

