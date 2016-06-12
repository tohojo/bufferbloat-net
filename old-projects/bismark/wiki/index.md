
---
title: Bismark Wiki
date: 2011-03-10T15:16:41
lastmod: 2011-07-18T18:22:34
type: wiki
---
Wiki
====

The BISMark project is deploying programmable gateways in home networks
to perform a combination of passive and active network measurements. We
are currently working on an extension of the study highlighted at the
recent AIMS workshop at CAIDA.
[Slides](http://www.caida.org/workshops/isma/1102/slides/aims1102_ssundaresan.pdf)
The work is also highlighted in this [more recent
talk](http://projectbismark.net/static/talks/bismark-google2011.ppt) at
Google in May 2011.

**Hardware** The primary hardware target is the [NetGear
WNDR3700v2](http://www.amazon.com/Netgear-Wireless-Gigabit-Router-WNDR3700/dp/B002HWRJY4).
We are planning possible support for several other gateways, such as the
<link>atom</link>, across more <link>bismark testers</link> and cable
modem types.

**Release schedule** The first release, codenamed <link>capetown</link>,
was released to a small South African deployment in late May and early
June, 2011. The firmware from that deployment is available at [the
BISMark project Web site](http://projectbismark.net/). The next release,
codenamed <link>Atlanta</link>, is due for release in mid-August 2011.

**More information** For more information, including about the state of
the firmware, shipping plans and release dates, please send email to
bismark-core@projectbismark.net.

Getting Started
---------------

1.  Acquire a <link>wndr3700v2</link> ([link to the NetGear purchase
    site](http://netgear.com/home/products/wirelessrouters/high-performance/WNDR3700.aspx))
2.  Flash the device with the BISMark OpenWRT build. The current images
    are available
    [here](http://mirrors.projectbismark.net/downloads/beta/) .
    -   Flashing from an existing firmware installation
    -   Flashing from scratch (generally, this is fail-safe,
        particularly if you have "bricked" your router)
        -   <link>Flashing\_instruction\_for\_Mac|Mac</link>
        -   <link>Flashing\_instruction\_for\_Linux|Linux</link>
        -   [Generic Instructions from the OpenWRT
            site](http://wiki.openwrt.org/toh/netgear/wndr3700#oem.easy.installation)

3.  <link>Further\_Configuration\_for\_wndr3700|Configure your NetGear
    Router (enable and configure WiFi, etc.)</link>

How to Get Involved
-------------------

### Contributing to BISMark

**Development**

-   Register on github to help develop the BISMark software:
    http://github.com/bismark-devel
-   [Review the open issues,submit bug reports, fix
    bugs](http://www.bufferbloat.net/projects/bismark/issues) with the
    current BISMark build. (Useful, since the image is being
    frequently updated.)

**Hosting Measurement Servers**

-   <link>Setting up a Measurement Server|Set up or host a BISMark
    measurement server</link>

### OpenWRT/BISMark Development

-   Setting up an OpenWRT Toolchain
    -   <link>Setting up a wndr3700 Toolchain at home|On your own
        server</link>
    -   <link>Setting up an OpenWRT Toolchain|On
        huchra.bufferbloat.net</link>
    -   Learn more about [building
        openwrt](http://wiki.openwrt.org/doc/howto/build)
-   Here's a <link>huchra openwrt build procedure|simple procedure that
    works for those building on huchra.bufferbloat.net</link>

Mailing Lists and IRC
---------------------

Mailing lists

-   [Users](http://lists.projectbismark.net/listinfo/bismark-users/)
-   [Devel](https://lists.bufferbloat.net/listinfo/bismark-devel/)
-   [Commit](https://lists.bufferbloat.net/listinfo/bismark-commits/)

IRC Chat Channel: [\#bismark](irc://chat.freenode.net/#bismark)

Development Paths
-----------------

-   Evaluating <link>tools</link> for inclusion in the BISMark
    test suite.
-   Developing a Web front-end for BISMark
-   There are two codenamed builds:
    -   <link>Capetown</link> is now up and released. Please help test.
        (<link>Post Capetown Planning</link>)
    -   <link>Atlanta</link> is in development, and is due for release
        in mid-August.

Other Resources
---------------

-   In July 2011, Georgia Tech hosted a <link>summer-camp-2011|Bismark
    Summer Camp</link>. The notes provide some hints as to the next
    steps for the project, as well as some rough notes on setting up
    your own builds.

Deployment
----------

-   <link>Parallel device flashing from factory firmware</link>
-   <link>Deployment stickers</link>

