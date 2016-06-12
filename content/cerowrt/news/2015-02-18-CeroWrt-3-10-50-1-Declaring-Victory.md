
---
title: "CeroWrt 3.10.50-1 -- Declaring Victory"
date: 2015-02-18T19:21:11
type: news
author: Rich Brown
aliases:
    - /news/53
---
We are extremely pleased to report that CeroWrt has been highly stable
since it was built over six months ago. We recently surveyed our user
base, and uptimes are terrific - ranging as high as 124 days, with a
lion's share of the reports greater than 80 days. Most of the reasons
for reboots are due to things like power failures. CeroWrt is meeting
its design goals:

-   Reliable, secure, high performance home router
-   Bufferbloat has been controlled with fq\_codel and the sqm-scripts
-   IPv6 just works, either from a native provider, such as Comcast, or
    through a tunnel such as Hurricane Electric
-   DNSSEC just works
-   We've proved the value of routing different interfaces, instead of
    bridging together the 2.4GHz, 5GHz, and Ethernet interfaces
-   And lots more

The latest CeroWrt 3.10.50-1 was resync'd with the OpenWrt sources on 28
July 2014. Therefore, the CeroWrt builds have ceased to change from that
date. You can review the build history from the CeroWrt release notes
at:
http://www.bufferbloat.net/projects/cerowrt/wiki/CeroWrt\_310\_Release\_Notes

That said, there are a few important efforts to take into account:

1.  We have aggressively pushed the interesting changes back into the
    OpenWrt mainline. All these changes are now available through the
    standard OpenWrt builds.
2.  CeroWrt development is dormant at the moment as we begin to think
    about the next step - how to "make wi-fi fast". (There are a number
    of bad behaviors in most wi-fi drivers that lower your wi-fi
    performance far below what is theoretically possible. We want to
    fix this.)
3.  OpenWrt has declared victory on their "Barrier Breaker" (BB)
    firmware evolution based on a Linux 3.10 kernel. They are now
    pursuing their "Chaos Calmer" (CC) build based on 3.18 (or later)
    kernel. CC will have all the goodness of BB, plus the new features
    they're planning.

Advice:

-   If you already own a Netgear WNDR 3800 (or 3700v2), you certainly
    won't go wrong with the CeroWrt 3.10.50-1 build. But don't run out
    and buy one today - they're becoming scarce and expensive.
-   If you're looking for stable, well-supported router firmware for
    your home, consider the OpenWrt BB build. It's available for a wide
    variety of routers, and incorporates most of the major capabilities
    that we put into CeroWrt.
-   If you're willing to put up with a little testing, check out the
    OpenWrt CC builds. That software is undergoing constant development,
    tweaks, and enhancements, and contains all the goodness of CeroWrt.
-   If you really want to live on the bleeding edge, join the CeroWrt
    Developer's list
    https://lists.bufferbloat.net/listinfo/cerowrt-devel to keep an eye
    on (or help with!) developments here. In a few months, we're
    planning to do more work on wi-fi, potentially on new, more
    available, higher performance hardware.

