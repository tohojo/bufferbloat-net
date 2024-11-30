---
title: Make-Wifi-Fast Project
date: 2018-02-14T15:38:14
lastmod: 2018-02-14T15:38:14
type: wiki
aliases:
    - /make-wifi-fast/wiki/Wiki
---
# Make Wi-Fi Fast Project

This project focuses on reducing latency throughout the wifi stack, firmware,
and hardware. 

> **The Make Wi-Fi Fast Manifesto - Wi-Fi does not need to be slow!**
> 
> The hardware now available for Wi-Fi can accomplish tremendous performance, but it is hobbled by software designs that guarantee high latency under load. 
> This, in turn, dramatically lowers performance in real-world settings (multiple users, home routers, commercial access points) leading to the *myth* that "Wi-Fi is slow."

> We believe that the same sort of systems thinking that went on in the Bufferbloat Project can lead to 
performance improvements of an order of magnitude or more in Wi-Fi.

## Current Status

In late 2024, we have decreased Wi-Fi
latency by at least an order of magnitude,
with fair sharing of airtime across fast and slow devices.

* Working software is available in the Linux kernel,
  as well as the [OpenWrt firmware](https://openwrt.org)
  that runs on off-the-shelf routers, x86 boxes, and embedded systems.

* An academic paper describing the mechanism has been published at the
  2017 USENIX Annual Technical Conference: [Ending the Anomaly: Achieving Low Latency and Airtime Fairness in Wifi](https://www.usenix.org/conference/atc17/technical-sessions/presentation/hoilan-jorgesen).

* Ongoing work was discussed at the Linux network developers conference
  (NetDev 2.2) in November 2017. The session was recorded
  [and is available from the NetDev web site](https://www.netdevconf.org/2.2/session.html?jorgensen-wifistack-talk).

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
    or more importantly, read the [Ending the Anomaly](https://www.usenix.org/conference/atc17/technical-sessions/presentation/hoilan-jorgesen) paper.

