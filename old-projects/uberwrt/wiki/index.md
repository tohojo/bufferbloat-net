
---
title: Wiki
date: 2011-03-19T12:14:13
lastmod: 2011-07-09T10:02:06
type: wiki
---
Wiki
====

Why Uberwrt?
------------

Other name suggestions welcomed! The goal is to have a name that is
wrt-like AND easily google-able.

From a [death metal
perspective](http://en.wikipedia.org/wiki/Metal_umlaut) ubërwrt looks
better but what it sounds like or what it means....

At the moment the project is divided into 4 parts:

<link>cerowrt:wiki|CeroWrt</link> is the upcoming (July 30) release.
(cero is Spanish for "zero". "Zero Warts") This is basically the base
platform for debloat-testing, ipv6, bind9, and mesh networking, based on
the wndr3700v2, kvm, and nanostation M5. Please go there for the most up
to date information, and flashable images. A release candidate is
available.

<link>bismark:wiki|Bismark</link> is the work we are doing with Georgia
Tech to create a "de-heisenbugged" wireless router for their test
project. That project is now fairly far along, and is where much of the
[bugs and features](http://www.bufferbloat.net/projects/uberwrt/issues)
that should be documented on uberwrt, are at currently. They have very
<link>bismark:CAPETOWN|working builds</link> already.

And there is also an obsolete <link>ISCWRT:build|iSCWRT build</link>-
(dnsmasq replaced with ISC-bind9 and ISC-dhcp and DHCP6, lots of ipv6
stuff. Much of this is now folded into cerowort. Similarly, an obsolete
<link>wisp6:Wiki|wisp6</link> build is out there...

This is not a very public project yet. In addition to naming and funding
and political issues, it's technically slowed by \#35 \#36 \#32 \#29
\#25 on the infrastructure
[roadmap](http://www.bufferbloat.net/projects/sysadmin/versions/2") as
well as outstanding issues from the [first
buildout](http://www.bufferbloat.net/projects/sysadmin/versions/1) -

Right now we're in a burn-in and **prototyping** phase, do discuss your
ideas on the bloat list!\
There are some <link>experimental patches</link> under test, not checked
in anywhere.

Philosophy
----------

The goal is to produce something closer to a <link>perfect wireless
router</link> - debloated, and <link>IPv6 enabled</link>.

The goal is NOT to fork openwrt, but to be able to experiment with
techniques and patches inside a branch that we hope to rapidly see
emerge in openwrt itself and its related downstream projects.

We will be helping the openwrt project by adding our build server to
their buildbot based server(s) as well as doing testing.

OBSOLETE URLS: The <link>build configuration</link>. Some useful
<link>openwrt tips</link> Some <link>ideas</link> for useful tools

Main target
-----------

We seem to be coalescing around the <link>bismark:wndr3700v2|Netgear
WNDR3700</link> as <link>good hardware</link> for a primary target. The
open source support for it is extensive, it has 16MB of flash and 64MB
of ram and support for a USB flash stick, they are inexpensive (\$
139.00), AND at least 7 people on the bloat list have one already, with
80+ in the pipeline over at GATECH.

Related to that, we hope to distribute ath9k based mini-pci cards to
developers so that we can continue to improve the wifi portion of a well
understood device and propagate that out to other devices.

Other targets
-------------

-   Noxbox

<!-- -->

-   Nanostation M5 (normal and <link>wisp6</link> enabled)

<!-- -->

-   Guru/dreamplug (freedombox?)

<!-- -->

-   Other hardware platform suggestions are welcomed. We've discarded
    some options already as <link>useless hardware</link> in our
    <link>hardware evaluation</link>.

<link>dtaht</link>
