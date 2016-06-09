
---
title: Capetown_Installation
date: 2011-05-11T11:26:18
lastmod: 2011-05-11T12:43:48
---
Bismark "Capetown" Installation Guide
=====================================

Capetown releases can be had (Currently) at
http://huchra.bufferbloat.net/\~bismark/capetown

<link>Capetown QA</link> <link>Capetown Issues</link> <link>Capetown
Testing</link> <link>South Africa Locations</link>

-   Please remember that to configure the router, you will need to go to
    the address:81, at least at present.

<link>WNDR3700v2</link>
-----------------------

New (factory firmware) routers can be installed via the standard Netgear
firmware upload web interface.

A full sysupgrade -n or tftp factory reflash is still required for new
builds. Sorry.

You can also flash the router via tftp - see the bismark installation
instructions for details

http://www.bufferbloat.net/projects/bismark/wiki/Flashing\_instruction\_for\_Mac

The router will come up on 192.168.42.1

Buffalo
-------

The router will come up on 192.168.62.1

<link>Nanostation M5</link>
---------------------------

The router will come up on 192.168.52.1

<link>X86 KVM</link>
--------------------

General Notes
-------------

-   There is a great deal of polish needed but most of the core
    functionality and packages are in there now. I'm aware of a half
    dozen small bugs already, what I'm concerned about are big (crash)
    bugs. Please file the bugs in the Issues database!

<!-- -->

-   Anything other than the wndr3700v2 is mostly untested and is
    probably at least somewhat misconfigured.

<!-- -->

-   If anyone already has the kvm virtual machine code installed and
    working on their main hardware, please see if you can get the kvm
    instance running and let us know how on the wiki.

<!-- -->

-   opkg.conf still points to the wrong place. Please see also the [bug
    database](http://www.bufferbloat.net/projects/bismark/issues)

