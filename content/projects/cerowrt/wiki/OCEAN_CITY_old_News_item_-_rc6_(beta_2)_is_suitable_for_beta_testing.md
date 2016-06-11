
---
title: OCEAN CITY old News item - rc6 (beta 2) is suitable for beta testing
date: 2012-03-17T09:19:24
lastmod: 2012-03-17T09:19:24
type: wiki
---
OCEAN CITY old News item - rc6 (beta 2) is suitable for beta testing
====================================================================

**Summary:** rc6 (beta 2) is suitable for beta testing. Originally
published on 19 Sep 2011.

About CeroWrt
=============

CeroWrt is a project built using OpenWrt to resolve endemic problems in
home networking today, and to push the state of the art of edge networks
and routers forward. Projects include proper IPv6 support, tighter
integration with DNSSEC, wireless mesh networking, among others, notably
reducing bufferbloat in both the wired and wireless components of the
stack.

CeroWrt's Goals
===============

CeroWrt is a build of the OpenWrt routing platform intended for use by
individuals, network engineers, researchers, teachers, and students
interested in advancing the state of the art on the Internet, and in
particular, those investigating the problems of latency under load,
bufferbloat, wireless-n, and the inter-relationships between various TCP
& QoS algorithms.

It comes with many network test tools installed and available via
optional packages for network diagnosis and testing - notably netperf,
iperf, nuttcp, httping, bing, fping, and others. Doing the network
testing on the router itself eliminates the variables introduced by
random clients, and makes possible independent analysis of local wired,
local wireless, and performance of both over the LFN.

6 TCP algorithms are included - TCP Westwood+ is the default. Many AQM
algorithms are included - of note, SFB, and DRR.

CeroWrt breaks with home router conventions in several ways. CeroWrt
comes with a high performance integral web server with which you can
establish local web services and provide web content and services 24x7.

IPv6 (6to4) is enabled **by default**.

With IPv6, first class name services become a necessity rather than a
"nice to have" . Manual configuration of name services with IPv4 and
IPv6 literal addresses is no longer feasible by most people, if indeed
it ever was. Toward the goal of "plug and play" home environment able to
publish IPv6 addresses into the global Internet name space without
manual configuration, CeroWrt includes the Bind name server. Security in
the home environment is also a goal, ergo CeroWrt's support for DNSSEC
using ISC Bind in a chrooted jail.

A core goal for CeroWrt is to provide a well understood platform, where
contributors can perform tests with confidence that their results can be
duplicated by others.

CeroWrt is the base on which other specialised builds may be built in
the future. The default build is too big (\~9MB) to be compatible with
more commonly available routers.

There are other features all intended to help make insight into
networking problems easier. In particular, bufferbloat, wherever we
could find it, has been reduced, but not yet eliminated entirely; that
requires the research in AQM and buffer management for which CeroWrt is
intended.

The current draft of the web pages on the router can often be seen at:
http://jupiter.lab.bufferbloat.net/, running on a CeroWrt router, of
course.

Interesting features of this release:
=====================================

Ocean City Release includes:

-   Extensive debloating
-   major surgery on the ath9k (wireless driver) vastly improving its
    aggregation and buffering behavior. Our thanks to Andrew McGregor
    and Felix Fietkau for this great work
-   ISC Bind 9 with DNSSEC, running in a chroot jail
-   Numerous debugging and diagnostic tools
-   ECN is enabled
-   Multiple TCP algorithms (Cubic, Bic, Westwood+, Vegas)
-   Multiple traffic shapers (now including DRR and SFB)
-   Simulations are possible of packet loss and delay by using NETEM
-   Native, 6to4, and 6in4 IPv6 support
-   Mesh routing (babel 1.2)
-   The polipo web proxy
-   Local lighttpd Web Server
-   Rsync
-   netperf is installed by default
-   Bridging different radios and ethernet has become very problematic,
    particularly in the face of multicast traffic and radically
    different wireless bandwidth. CeroWrt routes all networks rather
    than bridges
-   Many additional packages are not installed by default, but are
    available in the CeroWrt package repository. These include nuttcp,
    iperf, httping, bing, dibbler, and many others.

While we have tried very hard to produce a usable web interface for the
normal use of CeroWrt as your primary Internet router (and do desire you
use it as such and give us feedback!), some things, such as
configuration of the web proxy, or alternate TCP algorithms can require
non-GUI editing via SSH.

As this is a research and development platform, there will be no long
term support for this release and future RCs will likely require a
complete reflashing and reconfiguration of your router. We apologize for
the inconvenience but the state of the art and the problems we are
trying to solve are rapidly moving targets that we must track closely.
We will feed back the results of this work into stable distributions.

The Beta 2 "Ocean City" release (RC6)
=====================================

CeroWrt is aimed at (currently) a single hardware platform for which
fully open drivers are available: the Netgear WNDR3700v2, a current
802.11abgn router using the Atheros AR7161 rev 2 with gigabit Ethernet
ports. CeroWrt runs on the WNDR3700v2 only as it requires more than
8Mbytes of flash. Note that there may still be WNDR3700v1's in the
retail channel. Information on distinguishing them can be found in the
bufferbloat wiki at
http://www.bufferbloat.net/projects/bismark/wiki/Wndr3700v2

The Ocean City release is based on Linux 3.0.4; the DNS server is ISC
Bind 9.8.1 running from xinetd and in a chroot jail.

Systematic testing of this software has begun and the performance of the
router is at this date unknown relative to other firmware.

Release candidate RC6 firmware can be downloaded from:

http://huchra.bufferbloat.net/\~cero1/cerowrt-wndr3700-1.0rc6/

Installation directions can be found at:\
http://www.bufferbloat.net/projects/cerowrt/wiki/OCEAN\_CITY\_INSTALLATION\_GUIDE

Release notes are at:\
http://www.bufferbloat.net/projects/cerowrt/wiki/OCEAN\_CITY\_RELEASE\_NOTES

FAQs are at:\
http://www.bufferbloat.net/projects/cerowrt/wiki/OCEAN\_CITY\_FAQ

IRC discussions on CeroWrt take place at irc.freenode.net:
\#bufferbloat\
IRC discussions on OpenWrt in general take place on:irc.freenode.net:
\#openwrt

The roadmap for rc7 can be found at:
http://www.bufferbloat.net/projects/cerowrt/roadmap

Mailing lists:

General discussion about CeroWrt takes place on the bloat-devel list
found at:\
https://lists.bufferbloat.net/listinfo/bloat-devel

General bufferbloat discussions can be found at:\
https://lists.bufferbloat.net/listinfo/bloat

Thanks for giving CeroWrt a try!

The network you save may be your own.
