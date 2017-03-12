---
title: Make-Wifi-Fast Project
date: 2017-03-12T13:00:14
lastmod: 2017-03-12T13:00:14
type: wiki
aliases:
    - /make-wifi-fast/wiki/Wiki
---
# Make Wi-Fi Fast Project

This project focuses on reducing latency throughout the wifi stack, firmware,
and hardware. 

**Our Manifesto - Wi-Fi does not need to be slow!**

The hardware now available for Wi-Fi can accomplish tremendous performance, but it is hobbled by software designs that guarantee high latency under load. 
This, in turn, dramatically lowers performance in real-world settings (multiple users, home routers, commercial access points) leading to the *myth* that "Wi-Fi is always slow."

We believe that the same sort of systems thinking that went on in the Bufferbloat Project can lead to 
performance improvements of an order of magnitude or more in Wi-Fi.

## Current Status

As of early 2017, we have achieved many of these improvements, specifically a decrease of latency by at least an order of magnitude, with fair sharing of air time across fast and slow devices.

* Working software is available in <a href="https://lede-project.org" target="blank">LEDE firmware</a> that runs on off-the-shelf routers, x86 boxes, and embedded systems.
* An academic paper has been published to describe the current state of the working software, 
<a href="https://arxiv.org/abs/1703.00064">Ending the Anomaly: Achieving Low Latency and Airtime Fairness in Wifi</a> (preprint)
* An earlier recorded presentation and status of [the Make Wifi Fast Project](https://www.youtube.com/watch?v=-vWrFCZXOWk)

## Rationale

WiFi may be the single most successful internet access technology. It is
used by over a billion people. Unregulated use has enabled an explosion
of products and deployments using WiFi. Individuals can take immediate
action as no network operator has to be asked to install or extend a
WiFi network, and this contrasts strongly with centrally managed and
deployed systems such as the cellular telephone based communications
systems. One WiFi hop is between any company and a large fraction of its
users; yet we have paid scant attention to how well WiFi functions, and
nearly none at all at how it will continue to scale to the next 300
million hotspots, and 10 billion new users and devices in the next 4
years. WiFi devices now cost as little as US$3, Linux WiFi devices as
little as US$9. A large fraction of these devices run/will run Linux, and
the current Linux WiFi stack and drivers are far from optimal.

There has been little cross-fertilization between the participants of
the IETF, who understand how the Internet's end to end protocols
function, and the IEEE participants in the 802.11 standards process who
are primarily radio and hardware engineers. WiFi downward compatibility
constraints causes increasing complexity and problems with every
succeeding generation of the technology. We must attack the problems in
today's WiFi as it is between us and almost all devices, much or all of
the time.

## Goals of the Project

-   Reduce latency on a single AP, single station connected at the
    lowest rate (6mbits) to under 30ms under load, down from the
    commonly observed 600ms or more, while not sacrificing peak
    throughput under real world conditions
-   Develop new packet scheduling and AQM techniques applicable to
    aggregated, parking lot network types
-   Improve the stack sufficiently for 802.11ac MU-MIMO to actually work
-   Save the world

## The Make Wi-Fi Fast Plan


The current working draft is at:
https://docs.google.com/document/d/1Se36svYE1Uzpppe1HWnEyat\_sAGghB3kE285LElJBW4/edit

## Other Links 

-   **The Hardware:** Presently the most open wifi drivers are those
    based on the ath9k and mt76 chipsets. All other drivers contain
    binary blobs in precisely the places we need to hack on, and are
    currently unsuitable for further development. We MAY acquire a
    firmware license to deal with one or more 802.11ac chips. Read more
    in the [Hardware Plan](Hardware_Plan.md) and the [RFP](RFP.md) pages.
-   **BQL on Everything:** It really doesn't fit into the context of
    make-wifi-fast, but an active effort to get BQL on more hardware
    that can support it, and to get it better documented so that more
    new drivers use it, would be good.
-   **Re-working Wi-Fi:** Read the [Wifi Stack Rework](Wifi_Stack_Rework.md) page,
    or more importantly, read the <a href="https://arxiv.org/abs/1703.00064">Ending the Anomaly</a> paper.

