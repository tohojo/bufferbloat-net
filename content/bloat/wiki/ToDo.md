
---
title: ToDo
date: 2011-04-11T07:10:58
lastmod: 2011-04-11T09:08:56
type: wiki
---
ToDo
====

The outline of topics we'd like to address more fully is below:

Demonstration recipes for demonstrating/testing for bufferbloat
---------------------------------------------------------------

-   Servers
-   Home routers
-   Wifi routers
-   Wifi clients
-   Ethernet
-   Broadband gear
-   Core internet
-   3G wireless

Mitigations
-----------

-   Set end-node transmit buffers to something sane
-   Set QOS knobs on routers to keep broadband gear's buffer
    from filling.

Full Solutions
--------------

-   Fixes for routers involve AQM of some sort - Van's modified RED
    (or similar) is really necessary in wireless situations, as classic
    RED isn't easily dynamic, though one could kludge it, of course
-   Proper solutions for end-nodes involve some intelligence in
    buffering; at a minimum control of transmit buffers and
    device rings.

Testing tools
-------------

-   [The ICSI netalyzr](http://netalyzr.icsi.berkeley.edu/)
-   [Measurement Lab
    Tools](http://www.measurementlab.net/measurement-lab-tools)
-   [Speedtest.net](http://www.speedtest.net/)
-   [Pingtest.net](http://www.pingtest.net/)
-   [DSL Reports Smokeping Page](http://www.dslreports.com/smokeping)
-   [Smokeping](http://oss.oetiker.ch/smokeping/)
-   [httping](http://www.vanheusden.com/httping/) - latest version has
    support for persistent connections, and therefore it is easy to test
    against any web server over TCP, to defuse the (overblown) issues
    around ICMP ping. Also available now in the Android marketplace.

Needed tools
------------

-   a "push here to make your network become loaded" test, to drive this
    home to people
-   a tool like [pingplotter](http://www.pingplotter.com/profile.html)
    for Linux and Mac (at least), to help identify bloated links. This
    might be an elaboration of mtr:http://www.bitwizard.nl/mtr/ that
    works properly.
-   For super, duper extra bonus points, a tool that uses the techniques
    of [reverse
    traceroute](http://www.cs.washington.edu/research/networking/astronomy/reverse-traceroute.html)
    to identify problems on the reverse path, since many/most paths in
    the Internet are asymmetric

Papers
------

-   [Netalyzr: Illuminating Edge Network Neutrality, Security, and
    Performance, by Kreibich, Weaver, Nechaev, and
    Paxson](http://www.icsi.berkeley.edu/cgi-bin/pubs/publication.pl?ID=002876)
-   [Understanding broadband speed measurements, by Bauer, Clark and
    Lehr](http://mitas.csail.mit.edu/papers/Bauer_Clark_Lehr_Broadband_Speed_Measurements.pdf)
-   [RED in a Different Light, by V. Jacobson, K. Nichols, K.
    Poduri](http://mirrors.bufferbloat.net/RelevantPapers/Red_in_a_different_light.pdf)
-   [Cable Modem Buffer Management in DOCSIS Networks, by Martin,
    Westall, Shaw, White, Woundy, Finklestein, &
    Hart](http://www.cs.clemson.edu/~jmarty/papers/PID1154937.pdf)

Datasets
--------

-   [M-Labs datasets](http://www.measurementlab.net/data)

Experiments
-----------

-   [Jim Gettys
    experiments](http://people.freedesktop.org/~jg/Experiments/)

Presentations
-------------

-   [A Rant on Queues, Van Jacobson,
    2006](http://pollere.net/Pdfdocs/QrantJul06.pdf)
-   [We have Met the Enemy and \[S/\]He is Us: A View of Internet
    Research and Analysis, Kathleen
    Nichols](http://pollere.net/Pdfdocs/bcit_6.2001.pdf)
-   [Bufferbloat - Dark Buffers in the
    Internet](https://www.bufferbloat.net/documents/1) [Mp3
    audio](http://mirrors.bufferbloat.net/Talks/BellLabs01192011/murray_hill01192011_Bufferbloat_Talk_Edited_For_brevity.mp3)
-   [Bufferbloat FAQ](http://gettys.wordpress.com/bufferbloat-faq/)

Historical data/papers of interest
----------------------------------

-   [HTTP performance -
    1997](http://www.w3.org/Protocols/HTTP/Performance/)
-   [TCP Performance problems caused by interaction between Nagle's
    Algorithm and Delayed ACK
    2005](http://www.stuartcheshire.org/papers/NagleDelayedAck/)

Test equipment
--------------

-   [Gigabit port mirroring
    switch](http://www.dual-comm.com/gigabit_port-mirroring-LAN_switch.htm)

Dave Taht's to-do list:
-----------------------

-   <link>Myths</link>
-   <link>Controversies</link>
-   [Conferences]({{< relref "projects/bloat/wiki/Conferences.md" >}})
-   <link>Linux Traffic Shapers</link>
-   <link>Device Driver Buffering</link>
-   <link>Linux Patches</link>
-   [Linux Tips]({{< relref "projects/bloat/wiki/Linux_Tips.md" >}})
-   <link>Mac Tips</link>
-   [Windows Tips]({{< relref "projects/bloat/wiki/Windows_Tips.md" >}})
-   [Bloated Driver List]({{< relref "projects/bloat/wiki/Bloated_Driver_List.md" >}})
-   [IPv6]({{< relref "projects/bloat/wiki/IPv6.md" >}})
-   [Glossary]({{< relref "projects/bloat/wiki/Glossary.md" >}}) [Dark Buffers]({{< relref "projects/bloat/wiki/Dark_buffers.md" >}}) <link>Latency</link>
    <link>RTT</link> <link>TXQUEUELEN</link> <link>DMA\_TX\_QUEUE</link>
    <link>spiky latency</link>
-   [Experiments]({{< relref "projects/bloat/wiki/Experiments.md" >}})
-   [Equations]({{< relref "projects/bloat/wiki/Equations.md" >}})
-   <link>Qdiscs</link>
-   [Papers]({{< relref "projects/bloat/wiki/Papers.md" >}})
-   <link>Mitigations</link>
-   [Dogfood Principle]({{< relref "projects/bloat/wiki/Dogfood_Principle.md" >}})
-   [Good blog discussions]({{< relref "projects/bloat/wiki/Good_blog_discussions.md" >}})
-   <link>What (bad) stuff happens on a congested network?</link>
-   <link>Mesh Networks</link>
-   [Talks]({{< relref "projects/bloat/wiki/Talks.md" >}})
-   [Experts]({{< relref "projects/bloat/wiki/Experts.md" >}})
-   [sandbox]({{< relref "projects/bloat/wiki/Sandbox.md" >}})
-   [Quotes]({{< relref "projects/codel/wiki/Quotes.md" >}})
-   <link>SACK hall of Fame</link> <link>SACK hall of Shame</link>
-   <link>ECN Hall of Fame</link> <link>ECN hall of Shame</link>
-   [dtaht tasks]({{< relref "projects/bloat/wiki/Dtaht_tasks.md" >}})
-   [humor]({{< relref "projects/bloat/wiki/Humor.md" >}})
-   Gettys blogs reformatted\
    [Mitigations and Solutions]({{< relref "projects/bloat/wiki/Mitigations_and_Solutions.md" >}}) [Mitigations and solutions for Broadband]({{< relref "projects/bloat/wiki/Mitigations_and_solutions_for_Broadband.md" >}}) <link>Mitigations and solutions for
    Wireless</link> [Mitigations and Solutions for Home Gateways]({{< relref "projects/bloat/wiki/Mitigations_and_Solutions_for_Home_Gateways.md" >}})

