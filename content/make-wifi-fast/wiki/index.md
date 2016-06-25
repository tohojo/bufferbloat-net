---
title: Make-Wifi-Fast Wiki
date: 2013-12-30T21:36:28
lastmod: 2015-10-16T13:26:14
type: wiki
aliases:
    - /make-wifi-fast/wiki/Wiki
---
Make Wi-Fi Fast Wiki
====================

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

Manifesto - Wi-Fi does not need to be slow!
-------------------------------------------

We are focusing on reducing latency throughout the wifi stack, firmware,
and hardware. We believe that we can achieve the same sort of
performance improvements (an order of magnitude or more) that the
Bufferbloat project has already seen in Ethernet based systems.

See the latest presentation and status of [the make-wifi-project
here](https://www.youtube.com/watch?v=-vWrFCZXOWk)

Goals
-----

-   Reduce latency on a single AP, single station connected at the
    lowest rate (6mbits) to under 30ms under load, down from the
    commonly observed 600ms or more, while not sacrificing peak
    throughput under real world conditions
-   Develop new packet scheduling and AQM techniques applicable to
    aggregated, parking lot network types
-   Improve the stack sufficiently for 802.11ac MU-MIMO to actually work
-   Save the world

The Make Wi-Fi Fast Plan
------------------------

The current working draft is at:
https://docs.google.com/document/d/1Se36svYE1Uzpppe1HWnEyat\_sAGghB3kE285LElJBW4/edit

Other LInks
-----------

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
-   **Re-working Wi-Fi:** Read the [Wifi Stack Rework](Wifi_Stack_Rework.md) page.

