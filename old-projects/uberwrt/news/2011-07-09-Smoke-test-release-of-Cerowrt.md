
---
title: "Smoke test release of Cerowrt"
date: 2011-07-09T10:47:17
type: news
author: Dave Täht
aliases:
    - /news/17
---
After a long gestation, we're happy to announce the existence of a
'smoke test' release of 'CeroWrt', for the NETGEAR WNDR3700v2 series of
routers.

Documentation, flash images, and installation guide are at:

http://www.bufferbloat.net/projects/cerowrt/wiki/OCEAN\_CITY\_INSTALLATION\_GUIDE

This smoke test release is only for the brave... of whom I hope there
are many on these lists.

I hope to put out one release candidate per week for the next month,
until this is baked enough to freeze for a while.

The existing bug/feature database is out of date, I'll be updating that
soon, but as this is hopefully baked enough for others than myself, jg,
esr, and evan hunt to be be using, I'd love it if more people could get
one of these routers and try out this code.

What the heck is CeroWrt?

Cerowrt is the outgrowth of trying to de-heisenbug debloat-testing. The
results we were getting on conventional boxes were not repeatable on
conventional routers, until now. The project gradually grew from OpenWrt
into a kitchen sink worth of useful network analysis stuff from other
projects until it became... CeroWrt. Much of it has been pushed back
into openwrt...

To quote from it's integral help screen:

CeroWrt is an OpenWrt router platform for use by individuals,
researchers, and students interested in advancing the state of the art
on the Internet. Specifically, it is aimed at investigating the problems
of latency under load, bufferbloat, wireless-n, QoS, and the effects of
various TCP algorithms on shared networks. The features of this release
include:

-   linux 2.6.39.2 with a few bloat-related patches
-   Bind9 DNS services with DNSSEC
-   extensive network diagnostic, performance measurement, and
    simulation tools
-   support for TCP bic, cubic, westwood, and reno
-   comprehensive IPv6 support
-   integral web and rsync servers
-   support for mesh networking
-   a web proxy server

and most importantly, extensive debloating throughout the stack.

For more details please see the wiki pages and bug database, and check
in on the \#bufferbloat irc channel. I will be at Georgia Tech all next
week working on getting their test tools up and running on it, but will
be available for help and upgrades on the mailing lists and

Additional details on on the wiki.

http://www.bufferbloat.net/projects/cerowrt/wiki/

Happy debloating!
