---
title: "CeroWrt 3.3rc7-5 build available"
date: 2012-03-17T08:09:19
type: news
author: Rich Brown
aliases:
    - /news/29
---
In [this CeroWrt-devel
message](https://lists.bufferbloat.net/pipermail/cerowrt-devel/2012-March/000128.html),
Dave Täht announced that build 3.3-rc7-5 is available. This build
contains the following features/capabilities:

-   Linux 3.3 kernel. Many of the fixes for bufferbloat are being
    implemented in this 3.3 kernel, so we are tracking these
    developments carefully. http://kernel.org
-   Active Queue Management fixes for bufferbloat including: Byte Queue
    Limits (BQL - already incorporated into the 3.3 kernel), Stochastic
    Fair Queueing-Random Early Drop (SFQRED), working ECN, and other
    queue disciplines http://bufferbloat.net
-   IPv6 support. Another major goal of CeroWrt is to make IPv6
    networking in the home as simple as IPv4.
-   Babel mesh routing protocol (1.3.1-2 release).
-   DNSSEC and DNSSEC proxying - Secure extensions to the DNS system.
    Proxying is currently in testing.
-   OpenWrt features. Because we track the OpenWrt code base carefully,
    we incorporate most of the capabilities of that distribution. We
    actively push our changes/enhancements back toward the
    OpenWrt trunk. http://openwrt.org
-   An attractive web GUI for configuration - LuCI

Read the <link>CeroWrt\_33\_Release\_Notes|CeroWrt 3.3 Release
Notes</link>\
Download CeroWrt 3.3 builds: http://huchra.bufferbloat.net/\~cero1/3.3/
