
---
title: TechnicalIntro
date: 2011-01-25T16:37:45
lastmod: 2015-05-20T21:55:03
type: wiki
---
Technical Introduction to Bufferbloat
=====================================

Bufferbloat is the cause of much of the poor performance and human pain
experienced using today’s Internet. It can be the cause of a form of
congestion collapse of networks, though with slightly different symptoms
than that of the 1986 NSFnet collapse. Since [discussion of the best
terminology for the problem reached no
consensus](http://mailman.postel.org/pipermail/end2end-interest/2009-September/007769.html)
, <link>Jim Gettys</link> invented a term that might best convey the
sense of the problem.

> Bufferbloat[^1] is the undesirable latency that comes from the
> existence of excessively large (bloated) buffers in systems,
> particularly network communication systems.

In a shared network, “bufferbloat” is a phenomenon whereby buffering of
packets causes high latency and jitter, as well as reducing the overall
network throughput.

With TCP/IP, during <link>network congestion</link> bufferbloat causes
extra delays, limiting the speed of internet connections. Other network
protocols are also affected, including UDP-based protocols, partly
because they share buffers in the router with TCP/IP connections. This
can cause problems by restricting the speed of connections, affecting
interactive applications, <link>gaming</link> and [VoIP](VOIP.md). It
has only become apparent in recent years, as more modern network
equipment implements larger buffers as memory prices fall.

The problem is that the TCP congestion avoidance algorithm relies on
packet drops to determine the bandwidth available. A TCP sender
increases the rate at which it sends packets until packets start to
drop, then decreases the rate. Ideally it speeds up and slows down until
it finds an equilibrium equal to the speed of the link. However, for
this to work well, the packet drops must occur in a timely manner, so
that the sender can select a suitable rate. If a router on the path has
a large buffer capacity, the packets can be queued for a long time
waiting until the router can send them across a slow link to the ISP. No
packets are dropped, so the TCP sender doesn't receive information that
it has exceeded the capacity of the bottleneck link. It doesn't slow
down until it has sent so much beyond the capacity of the link that the
buffer fills and drops packets. At this point, the sender has far
overestimated the speed of the link.

In a network router, packets are often queued before being transmitted.
Packets are only dropped if the buffer is full. On older routers,
buffers were fairly small so filled quickly and therefore packets began
to drop shortly after the link became saturated, so the TCP/IP protocol
could adjust. On newer routers buffers have become large enough to hold
several megabytes of data, which can be equivalent to 10 sec. or more of
data. This means that the TCP/IP protocol can't adjust to the speed
correctly, as it appears be able to send for 10 sec without receiving
any feedback that packets are being dropped. This creates rapid speedups
and slowdowns in transmissions.

The problem also affects other protocols. The router's buffer can easily
build up several seconds worth of data before packets start to drop.
Those packets in the queue block (can be ahead of) interactive
applications and cause problems for <link>DNS</link>, <link>ARP</link>,
<link>NTP</link>, <link>DHCP</link>, gamers and [VoIP](VOIP.md). This
is even the case with DiffServ, which has multiples buffers (queues).
HTTP and VoIP may be buffered independently, but each buffer will still
be independently susceptible to bufferbloat.

Systems suffering from bufferbloat will have bad latency under load
under some or all circumstances, depending on if and where the
bottleneck in the communication’s path exists. Bufferbloat encourages
congestion of networks; bufferbloat destroys congestion avoidance in
transport protocols such as HTTP, TCP, Bittorrent, etc. Network
congestion avoidance algorithms depend upon timely packet drops or ECN;
bloated buffers violate this design presumption. Without active queue
management, these bloated buffers will fill, and stay full.

More subtlety, poor latency, besides being painful to users, can cause
complete failure of applications and/or networks, and extremely
aggravated people suffering with them.

Bufferbloat is seldom detected during the design and implementations of
systems as engineers are methodical people, seldom if ever test latency
under load systematically, and today’s memory is so cheap buffers are
often added without thought of the consequences, where it can be hidden
in many different parts of network systems.

You see manifestations of bufferbloat today in your operating systems,
your home network, your broadband connections, possibly your ISP’s and
corporate networks, at busy conference wireless networks, and on 3G
networks. You can use the [DSLReports Speed
Test](http://dslreports.com/speedtest) to measure bufferbloat directly.

Bufferbloat is a mistake we’ve all made together. What's the solution?
We have had extremely good results with the
[CoDel](http://www.bufferbloat.net/projects/codel/wiki) algorithm, and
the related fq\_codel which reduce bufferbloat by several orders of
magnitude.

See also
--------

-   [Bufferbloat wikipedia](http://en.wikipedia.org/wiki/Bufferbloat)
    ,[Dark Buffers](Dark_buffers.md)
-   [The Buffer Bloat Project](index.md)
-   [CoDel](http://www.bufferbloat.net/projects/codel/wiki) and
    fq\_codel

External links
--------------

-   [Jim Gettys
    Ramblings](http://gettys.wordpress.com/category/bufferbloat/)

Footnotes
---------

[^1]: For the English language purists out there, formally, you are
    correct that “buffer bloat” or “buffer-bloat” would be more
    appropriate.
