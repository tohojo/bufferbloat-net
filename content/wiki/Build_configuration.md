
---
title: Build configuration
date: 2011-03-20T09:03:33
lastmod: 2011-07-01T14:40:20
---
Build configuration
===================

There will be several different builds for different
[targets]({{< relref "wiki/Targets.md" >}}) as time goes by, but these are the core changes to
the openwrt build that uberwrt enabled builds will have.

We will build both mainline openwrt and the following branches under
control of the main <link>buildbot</link> based openwrt
<link>buildmaster</link>.

Patches
-------

<link>pfifo ECN patches</link>\
<link>bloat:CHOKe</link> and <link>bloat:SFB</link> support\
<link>bloat:eBDP</link>

Mandatory features
------------------

-   <link>bloat:ECN</link>, <link>bloat:SACK</link>,
    <link>bloat:DSACK</link> will be enabled by default

<!-- -->

-   TXQUEUELEN will be reduced by default on wired and wireless

<!-- -->

-   DMA TX queues will be reduced by default on wired and wireless

<!-- -->

-   TX RETRIES on wireless will be reduced by default

<!-- -->

-   IPv6 support, including IPsec, 6rd, ipv6 tunneling, radvd

<!-- -->

-   The polipo proxy will be included by default

<!-- -->

-   Different forms of TCP/ip (Vegas, Reno, Cubic, Bic, Westwood) are
    enabled - westwood+ is the default

<!-- -->

-   Switching to using openssl as the default ssl provider

<!-- -->

-   Web server support (lighttpd)

<!-- -->

-   Shaper scripts will be distributed by default

<!-- -->

-   Gui: Luci

<!-- -->

-   More?

Under debate
------------

-   [perfect wireless router]({{< relref "wiki/Perfect_wireless_router.md" >}})

Optional
--------

Given the load this places on flash, a GUI may end up being optional
and/or loaded on a USB stick.

There are routers with more flash in the pipeline from Buffalo and
others.

Futures
-------

Ultimately some of this may incorporate the more radical changes from
the [wisp6]({{< relref "wiki/Wisp6.md" >}}) project
