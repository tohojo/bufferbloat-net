---
title: CongestionSymptoms
date: 2011-02-03T09:15:09
lastmod: 2011-04-11T10:26:23
type: wiki
---
Symptoms of bufferbloat-induced congestion
==========================================

Once a network is congested, various service protocols (statistically
insignificant in terms of additional network load, but mission-critical)
**can't do their jobs**. Here are some examples

-   DNS - adding hundreds of ms of latencies to turning a website into
    an IP address is **not** good. With a typical web page doing dozens,
    even hundreds of DNS lookups, DNS not getting through in a timely
    fashion results in vastly slower browsing.

<!-- -->

-   NTP - the network time protocol - relies on somewhat timely delivery
    of packets in order to keep your computer's clock accurate. Lots of
    things rely on accurate timekeeping.

<!-- -->

-   ARP - the address resolution protocol - also relies on timely
    resolution in order to even find other devices on your network.

<!-- -->

-   DHCP - if these packets are lost or excessively delayed, machines
    can't get on the network in the first place.

<!-- -->

-   Routing - many routing protocols depend on packet drops as a way of
    monitoring network health and are time sensitive.

<!-- -->

-   VOIP - needs about a single packet per 10ms flow in order to be
    good, and less than 30ms jitter.

<!-- -->

-   Gamers will get fragged a lot more often with latencies above their
    twitch factor.

<!-- -->

-   IPv6 relies on even more specialized packet types for
    autoconfiguration, e.g. the equivalent of ARP

<!-- -->

-   Encapsulated packets (VPNs, X11 over ssh, IPv6 over 6rd/6to4)
    also suffer.

