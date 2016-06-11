
---
title: Glossary
date: 2011-01-26T18:32:42
lastmod: 2012-02-14T19:25:25
type: wiki
---
Glossary
========

These terms are defined in the context of the overall topic,
Bufferbloat, and their relevance to the recognition, detection,
description, mitigation of this problem. As such, references to others'
definitions may be given for completeness but should be prefaced or
augmented by subjective and/or objective definition of the relationship
to the Bufferbloat problem.

Bufferbloat
===========

Bufferbloat is the cause of much of the poor performance and human pain
experienced using today’s Internet. It can be the cause of a form of
congestion collapse of networks, though with slightly different symptoms
than that of the 1986 NSFnet collapse. Since [discussion of the best
terminology for the problem reached no
consensus](http://mailman.postel.org/pipermail/end2end-interest/2009-September/007769.html)
, <link>Jim Gettys</link> invented a term that might best convey the
sense of the problem.

> Bufferbloat\[1\] is the existence of excessively large (bloated)
> buffers in systems, particularly network communication systems.

See <link>Bufferbloat</link> for extended definition - [Also now defined
on Wikipedia](http://en.wikipedia.org/wiki/Bufferbloat)

*please leave this term at the top of the list*

Active Queue Management (AQM)
-----------------------------

[Wikipedia](http://en.wikipedia.org/wiki/Active_queue_management) : "In
Internet routers, active queue management (AQM) is a technique that
consists in dropping or ECN-marking packets before a router's queue is
full." This is important because the dropped/marked packets are critical
to the proper operation of network protocols such as TCP. AQM techniques
help to reduce symptoms of <link>bufferbloat</link>, where networks work
fine when there's not much traffic/load on the network but degrade
dramatically when there is load.

### Random Early Detection (RED, RED 93, nRED)

definition needed (should this be moved to AQM?)

### Stochastic Fair Blue (SFB)

definition needed - should other queuing protocols be put here too, or
in Alphabetical order?

Congestion Control (TCP)
------------------------

definition needed - references to TCP Vegas, TCP cubic and others? or
separate definitions?

{{include(Dark Buffers)}}
-------------------------

Explicit Congestion Notification (ECN)
--------------------------------------

Defined in [RFC3168](http://www.ietf.org/rfc/rfc3168.txt) defines a
method (negotiated using ECN bits in packets) whereby a router sets a
bit on the transited packet if congestion is impending - and the
receiving program in turn sets the bit on the ACK packet back to the
sending program, which then is to act as if a packet had been dropped
(as far as shutting the congestion window size). ECN cannot eliminate
packet loss but can, if used with reasonable AQM, pre-warn and possibly
prevent much packet loss.

Fairness
--------

definition needed

Goodput
-------

The actual payload throughput of a link, stripped of all the traffic
that is retries and other overhead. Application sender to Application
receiver. More detail at
[Wikipedia](http://en.wikipedia.org/wiki/Goodput)

Latency
-------

The delay between transmission of information and its arrival. Network
latency is more important than throughput in user perception of how
smooth and responsive an interface is. You can read a more technical
definition at
[Wikipedia](http://en.wikipedia.org/wiki/Latency_%28engineering%29)

Jim Gettys adds: As a UI guy, my metrics have always been (since I
learned this stuff first hand in the 1980s), that:

\* No perceptible delay to all human interactions requires less than
20ms (rubber banding is hardest)\
\* semi-tolerable rubber banding needs less than 50ms\
\* typing needs to be less than 50ms to be literally imperceptible\
\* typing echo needs to be less than 100ms to to be usually not
objectionable\
\* echo cancellation gets harder as well (the best echo cancellation
needs to be done as close to all participants as possible, even the
latency over a broadband link is undesirable).\
\* then there are serious gamers for whom even a millisecond may be an
advantage and the difference between life and death

### Latency under Load

definition needed (generic - basic loading paradigm, specific - how it
is measured/reported - updated as we define this measurement)

Packet Loss
-----------

definition needed

Queuing discipline
------------------

A quueing discipline (Qdisc fir short) is an algorithm for controlling
when packets are shipped out of a buffer to a downstream link.
Well-tuned queuing disciplines increase network performance while
decreasing peak load. Poorly-tuned ones wreak havoc. A list of
well-known Qdiscs used on TCP/IP networks follows:

-   RED
-   nRED
-   SFB
-   ESFQ
-   SFQ
-   HTB
-   HSFC
-   MQ
-   [Choke](http://lwn.net/Articles/422477/)

Throughput (network throughput)
-------------------------------

Aggregate total of packet traffic on the link which may include TCP
retries and other overhead not directly contributing to the "Goodput"
(application sender to application receiver) traffic.

Utilization (network utilization)
---------------------------------

definition needed

Window (Congestion Window)
--------------------------

definition needed

Windows XP Problem
------------------

(the ongoing retirement of and its potential effect on the overall
internet)

definition needed
