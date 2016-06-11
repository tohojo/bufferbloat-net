
---
title: Wiki
date: 2011-05-28T06:59:53
lastmod: 2015-11-29T16:41:10
type: wiki
---
Overview of the CeroWrt Project
===============================

![](http://huchra.bufferbloat.net/~d/images/a9.jpg)

Bufferbloat is the undesirable latency that comes from a router or other
network equipment buffering too much data. It is a huge drag on Internet
performance created, ironically, by previous attempts to make it work
better. Eric Raymond wrote this one-sentence summary of the problem:
"Bloated buffers lead to network-crippling latency spikes." You can read
more about this problem at the main
[Bufferbloat]({{< relref "bloat/wiki/Introduction.md" >}}) site.

CeroWrt was a project built upon the [OpenWrt
firmware](http://openwrt.org) to resolve these endemic problems in home
networking today, and to push the state of the art of edge networks and
routers forward. Projects include proper IPv6 support, tighter
integration with DNSSEC, and most importantly, reducing bufferbloat in
both the wired and wireless components of the stack.

The code was 100% open source, top to bottom. No binary blobs
whatsoever. Every aspect of the code and hardware can be inspected
and/or modified. As a project, most of the results have been pushed up
into mainline linux, OpenWrt "Chaos Calmer" and "Barrier Breaker"
releases, many firewall and router distributions and it is beginning to
appear in commercial firmware. Active research (due to lack of funding,
and succeeding in the primary goals) has ceased, with the exception of
ongoing work into standardization efforts, and into something even
better than fq\_codel, called [cake]({{< relref "codel/wiki/Cake.md" >}}), which is not
ready for prime time yet.

Is your internet connection bloated? You can find out right now using
the [Quick Test for Bufferbloat.]({{< relref "cerowrt/wiki/Quick_Test_for_Bufferbloat.md" >}}) - or see the [dslreports new
speedtest](http://dslreports.com/speedtest) .

News
----

[**CeroWrt 3.10.50-1 Works!**](http://www.bufferbloat.net/news/53) This
build has been very stable since it was released on 28 July 2014. We
strongly recommend replacing all earlier builds with this build. Read
the [News](http://www.bufferbloat.net/news/53) item for the update. See
the [CeroWrt 3.10 Release Notes]({{< relref "cerowrt/wiki/CeroWrt_310_Release_Notes.md" >}})
and the [mailing
list](https://lists.bufferbloat.net/listinfo/cerowrt-devel) for more
details.

*Note:* All the important features of the CeroWrt software are now
available in mainline [OpenWrt](http://openwrt.org) Barrier Breaker and
Chaos Calmer builds. You may be better served by installing one of those
supported builds that are available on a much wider range of router
hardware.

Roadmap
-------

Our plan has always been to produce a stable build that can be used as
both a production router, and as a platform for further research into
algorithms for solving state of the art problems in networking. The
CeroWrt 3.10 series of builds include the following features and
capabilities

-   Linux 3.10 kernel. Most of the fixes for bufferbloat are being
    implemented in this 3.10 kernel, so we are tracking these
    developments carefully. http://kernel.org
-   We have included a version of the
    [CoDel](http://www.bufferbloat.net/projects/codel/wiki) algorithm
    from Kathie Nicols and Van Jacobson, along with Eric Dumazet's [flow
    queueing](https://tools.ietf.org/html/draft-hoeiland-joergensen-aqm-fq-codel-00) fq\_codel.
    These in turn rely on the Byte Queue Limits for line rate networks
    and on htb for the [SQM]({{< relref "cerowrt/wiki/SQM.md" >}}) QoS system. These replace
    earlier Active Queue Management fixes for bufferbloat including:
    Stochastic Fair Queueing-Random Early Drop (SFQRED), and other
    queue disciplines.
-   There are also two <link>newer versions of fq\_codel</link> under
    test, as well as an implementation of the current ns2 model of
    codel itself.
-   IPv6 support. Another major goal of CeroWrt is to make IPv6
    networking in the home as simple as IPv4.
-   Babel mesh routing protocol with <link>source sensitive
    routing</link>. RA, bgp, rip, ripng, and ospf are also supported via
    the Quagga optional package.
-   DNSSEC - Secure extensions to the DNS system.
-   OpenWrt features. Because we track the OpenWrt code base carefully,
    we incorporate most of the capabilities of that distribution. We
    actively push our changes/enhancements back toward the
    OpenWrt trunk. http://openwrt.org
-   An attractive web GUI for configuration - LuCI

Sources of Information about the Bufferbloat Project
----------------------------------------------------

Glossary for Bufferbloat Topics: [Glossary]({{< relref "bloat/wiki/Glossary.md" >}})\
General Bufferbloat list: https://lists.bufferbloat.net/listinfo/bloat\
CeroWrt-devel list:
https://lists.bufferbloat.net/listinfo/cerowrt-devel\
CeroWrt-Commits list:
https://lists.bufferbloat.net/pipermail/cerowrt-commits/\
IRC: Find us on [IRC on
chat.freenode.net](irc://chat.freenode.net:6667/bufferbloat),
\#bufferbloat channel\
[Assorted Bufferbloat Videos]({{< relref "cerowrt/wiki/Bloat-videos.md" >}})

Try the Software
----------------

The current build is solid. We believe it solves virtually all the
bufferbloat problem, and deserves wider use. Lots of people are using it
as their production router. Download the current CeroWrt 3.10.50-1
build:

-   [CeroWrt 3.10.50-1 for
    WNDR3700v2](http://www.bufferbloat.net/attachments/download/226/openwrt-ar71xx-generic-wndr3700v2-squashfs-factory3.10.50-1.img)
-   [CeroWrt 3.10.50-1 for
    WNDR3800](http://www.bufferbloat.net/attachments/download/227/openwrt-ar71xx-generic-wndr3800-squashfs-factory3.10.50-1.img)
-   [All CeroWrt Builds](http://snapon.cs.kau.se./~cero2/cerowrt/wndr/)
    (mirrored
    on[snapon](http://snapon.lab.bufferbloat.net/~cero2/cerowrt/wndr/))

Hardware Requirements
---------------------

To minimize the effects of hardware dependencies, we have chosen the
Netgear WNDR3700v2 and WNDR3800 as the sole hardware for the
experiments. **Note:** The WNDR3700v3 and v4 models do *not* work with
CeroWrt; purchase the WNDR3800 if you want to be future-proof.

The open source support for these two models is extensive, they have a
capable processor with 16MB of flash and 64MB of RAM, they support a USB
flash stick, they are inexpensive (around \$100). The WNDR3800 has more
RAM (128MB instead of 64), but either of these models will be fine for
these experiments. As of October 2015, both the target router models
have become scarce. You can search for "WNDR3800" on amazon.com,
frys.com, ebay.com, etc. but might be better served by looking at the
[OpenWrt](http://openwrt.org) software which is available for a wide
variety of common routers.

There are ubnt builds available as well, but specialized for a specific
deployment scenario. Ask if you want them.

As noted above, OpenWrt and DD-WRT support fq\_codel now in their QoS
systems, so you can adopt one of the 150+ platforms supported there and
see what happens.... YMMV, but please report here:
[Hardware Reports on FQ CODEL]({{< relref "cerowrt/wiki/Hardware_Reports_on_FQ_CODEL.md" >}})

Documents
---------

-   [Installation Guide]({{< relref "cerowrt/wiki/Installation_Guide.md" >}})
-   [Flashing Instructions]({{< relref "cerowrt/wiki/Cerowrt_flashing_instructions.md" >}})
-   [Automated Configuration of CeroWrt]({{< relref "cerowrt/wiki/Automated_Configuration_of_CeroWrt.md" >}})
-   [Frequently Asked Questions]({{< relref "cerowrt/wiki/FAQ.md" >}})
-   <link>How is CeroWrt different from OpenWrt?</link>

Tech Notes for CeroWrt
----------------------

The following give detailed descriptions of CeroWrt's operation.

-   [Setting up SQM]({{< relref "cerowrt/wiki/Setting_up_SQM_for_CeroWrt_310.md" >}})
-   [Default interface naming scheme]({{< relref "cerowrt/wiki/Device_naming_scheme.md" >}})
-   [Default network numbering     scheme]({{< relref "cerowrt/wiki/Default_network_numbering.md" >}})
-   [Changing IP, DNS, and     SSID]({{< relref "cerowrt/wiki/Changing_your_cerowrt_ip_addresses.md" >}})
-   [Monitoring CeroWrt with SNMP and     NetFlow]({{< relref "cerowrt/wiki/Monitoring_CeroWrt.md" >}})
-   <link>Using Bonjour, mDNS, or ZeroConf with CeroWrt</link>
-   [Getting an IPv6 address via Hurricane Electric     Tunnelbroker.net]({{< relref "cerowrt/wiki/IPv6_Tunnel.md" >}})
-   [Useful scripts to use with CeroWrt]({{< relref "cerowrt/wiki/CeroWrtScripts.md" >}})

Older Information
-----------------

The documents below describe the older Linux 3.7 and earlier builds.

-   [CeroWrt 3.7 Release Notes]({{< relref "cerowrt/wiki/CeroWrt_37_Release_Notes.md" >}})
-   [Building CeroWrt on     your own machine]({{< relref "cerowrt/wiki/Building_Cerowrt_on_your_own_machine.md" >}}) (tested for CeroWrt 3.3, not with
    CeroWrt 3.7)
-   [Setting QoS If You Can't Use CoDel]({{< relref "cerowrt/wiki/Setting_QoS_If_You_Can't_Use_CoDel.md" >}})

The [Historical Documents]({{< relref "cerowrt/wiki/Historical_Documents.md" >}}) page links to many documents that
describe the history and earlier releases of the project.

### Attachments
{{< attachment name="flanders320fade.jpg" type="image/jpeg" description="" filename="120122121434_flanders320fade.jpg" >}}
