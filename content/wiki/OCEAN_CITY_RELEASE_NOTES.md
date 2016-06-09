
---
title: OCEAN CITY RELEASE NOTES
date: 2011-06-24T08:47:33
lastmod: 2012-01-28T17:58:52
---
CEROWRT-1.0 "OCEAN CITY" RELEASE NOTES
======================================

### THIS DOCUMENT IS OBSOLETE

See the <link>OCEAN CITY</link> page.

### CEROWRT-RC6

These release notes apply to RC6 and may or may not apply to earlier
release candidates. RC6 consists of:

-   Linux kernel 3.0.4
-   iptables 1.4.12.1
-   wireless-testing 2011-09-14

as well as too many
[features](http://cero2.bufferbloat.net/cerowrt/features.html) to
enumerate here.

Note that there are desired features that have not yet landed; e.g.
IPsec tunnels, DHCPv6-PD, and completion of DNS support. The DNS vision
is that you should be able to plug a named machine into your network and
its IPv6 address be automatically published into the global DNS without
any manual configuration needed whatsoever. This capability has been
made to work in prototype form, but is not yet present in CeroWrt.
Preliminary performance numbers for IPSEC were about 20MBPS on the
WNDR3700, well beyond current commercial offerings costing much more. If
you are so inclined, help with any of these would be greatly
appreciated!

eBDP is not currently in Cerowrt; we are considering test builds in RC7
of this AQM algorithm. The current tuning of queue lengths may (almost
certainly is) sub-optimal and not yet comparable to factory firmware for
bandwidth performance.

1.  If you haven't installed a router yet, the current draft of the web
    pages on the router can often be seen at:
    http://cero2.bufferbloat.net/
2.  Performance testing has just begun and you may very well uncover a
    bug or a problem with default configuration which need to be fixed.\
    Note that this means that naive testing may produce unexpectedly
    poor bandwidth results: for example, when we were testing CeroWrt
    directly plugged directly into a gigabit network with 10G back haul,
    we saw poorer Large, Fat Network (LFN) router performance than the
    commercial firmware on identical hardware, due to our configuration
    for use in a more typical home environment. This is hardly
    surprising, as Linux drivers have been tuned extensively for use at
    that speed in data centers (to the detriment of latency); when
    re-configured identically to factory firmware, CeroWrt outperformed
    the commercial firmware in this example.
3.  Reduced TXQUEUELEN accoss all ethernet and wireless interfaces.
    Since this is a home router, when operating locally, delay is very
    low, so the queue can be short without losing TCP performance; when
    operating remotely, the upstream bandwidth limit means the buffering
    can again be low. Transmit queues only need to be large when you
    have both high bandwidth, and high delay paths.
    -   Reduced buffering in the ethernet switch
    -   Reduced driver buffering across all ethernet and wireless
        interfaces\
        This initial tuning is probably too aggressive, and will be
        tuned further.

4.  There is ongoing performance testing against various smoketests
    going on in \#262\
    We are in the VERY early stages of performance testing and have all
    sorts of variables - oprofile being enabled, HT40 not being enabled
    by default, queue lengths, lab setup, and problems with the tests
    themselves ... all left to resolve. Please draw no conclusions from
    the performance test results thus far, and note that rc6 contains
    the latest and greatest wireless-testing, not tested on bug \#262.
5.  CeroWrt is still not independently buildable until the patch set
    settles some more and more patches pushed into OpenWrt head.
6.  Our current opinion is that HT40 should only be enabled by default
    at 5ghz only, and not at 2.4ghz, as it makes the router enough more
    noise sensitive as to probably cause too many people trouble (though
    will lab benchmark more poorly unless enabled, of course). Differing
    opinions are welcome about this default choice.
7.  CeroWrt routes rather than bridges between networks. It has an mdns
    forwarder to handle the case of a home network using MDNS to
    locate services. "A little multicast can ruin your whole day
    on wireless".
8.  Note that the router is configured with <link>default network
    numbering</link> to use network 172 addresses to try to stay out of
    your existing network's way. This may make renumbering if you have
    an existing static numbering plan in your house somewhat
    a challenge. We plan changes in RC7 so that the low addresses are
    left free for static numbering, as that is the most common
    configuration people have. If you modify your RC6 configuration for
    interface se00 (found in */etc/config/network*) to enable access to
    low IP addresses, remember that you must also fix all references to
    33 in your bind configuration files (found in
    *root@OpenWrt:/etc/chroot/named/etc/bind/master*) so that
    gw.home.lan will work.
9.  For IPv6, we are most concerned about the following bug: \#266
    -   dibbler is in the RC6 build: volunteers to play with DHCPv6-PD
        and test would be great
    -   If the WAN interface is allocated a routeable IPv4 address (e.g.
        directly plugged into your broadband gear) the router will turn
        on 6to4 by default and advertise IPv6 routes. Please give us
        feedback as to whether this causes trouble. Comcast has put in
        many more geographically dispersed 6to4 relays so using 6to4 is
        much less problematic than it was even a year ago often
        exhibiting very good performance and reliability on
        that network.

10. The eBDP algorithm for wireless queue management is not yet present
    in CeroWrt builds; it awaits some further testing.
11. QoS enabled by default; you *should* tune your QOS settings for your
    connection as covered in the
    <link>OCEAN\_CITY\_FAQ\#How-can-I-improve-latency-problems-with-a-Cerowrt-router</link>,
    or you **will** have performance problems of some sort.
12. Something like 20+ new packages are now available, including
    [dibbler](https://github.com/tomaszmrugalski/dibbler/tree/master/doc),
    [gpsd](http://gpsd.berlios.de/),
    [nuttcp](http://www.nuttcp.net/nuttcp/Welcome%20Page.html),
    [pimd](http://troglobit.com/pimd.shtml), and
    [ccnx](http://www.ccnx.org/).
13. Mesh routing is in CeroWrt, using the [Babel
    protocol](http://www.pps.jussieu.fr/~jch/software/babel/) using
    bandwidth diversity and
    [ahcp](http://www.pps.jussieu.fr/~jch/software/ahcp/) for
    address distribution.
    -   Note that the router does **not** warn you in some trivial way
        (blinking light, highlight on the status page) that it may be
        meshed rather than using its WAN port. Feature \#270
    -   Babeld updated to port 6696 and version 1.2
        (incompatable change)

14. Bugs \#195 (ethernet unaligned transfers), \#240 (ssh problems),
    \#243 (iptables), \#256 (ntpdate) are believed fixed in RC6 and are
    being tested.
15. Bug \#205 is a PITA for DNS lookup; the current workaround may slow
    boot by several minutes; there are fixes possible, but not in time
    for RC6
16. Babeld moved to IANA port 6696 - this is a non-backward compatible
    change
17. Addition of TCP background (BP) and TCP yeah algorithms
18. Web10g support - note: we have not found a real use for this and may
    pull it from the next release
19. Tcp\_low\_latency made the default
20. IPv6 works now on the secured and unsecured interfaces by default
21. Basic support for the cosmic background bufferbloat detector
22. The
    [roadmap](http://www.bufferbloat.net/projects/cerowrt/roadmap?tracker_ids%5B%5D=1&tracker_ids%5B%5D=2&completed=1&with_subprojects=0&with_subprojects=1)
    has other known issues scheduled for resolution in RC7; please check
    that list before starting a new bug report

<link>cerowrt-1.0-rc7</link> Plan
---------------------------------
