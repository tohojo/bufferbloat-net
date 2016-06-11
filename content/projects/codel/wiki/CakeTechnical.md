
---
title: CakeTechnical
date: 2015-08-14T04:34:53
lastmod: 2015-08-17T13:44:40
type: wiki
---
Cake Technical Information
==========================

Introduction
------------

Cake is a *comprehensive queue management* system, implemented as a
*queue discipline* (qdisc) for the Linux kernel. It is designed to
replace and improve upon the complex hierarchy of simple qdiscs
presently required to effectively tackle the bufferbloat problem at the
network edge.

For installation and configuration instructions, please see the main
[Cake]({{< relref "projects/codel/wiki/Cake.md" >}}) page.

Philosophy
----------

Cake's fundamental design goal is *perceived simplicity*. This is
achieved by integrating lots of functionality into one qdisc, resulting
in:

-   Information sharing between functional components, improving
    latency performance.
-   Eliminated message-passing overhead (improving throughput
    performance), and unmanaged queuing between qdiscs.
-   Greatly simplified configuration for common use-cases, compared to
    building equivalent functionality using existing qdiscs.

Cake is logically arranged as several layers of functionality:

-   Shaper
-   Priority queue
-   Flow isolation
-   AQM
-   Packet management

Each of the above layers is based on state-of-the-art techniques, many
of which have improvements not previously realised. These are briefly
explained below.

Additionally, most calculations are now performed on a time basis, with
the remainder on a bytes basis. This is a fundamental improvement over
many qdiscs which count only packets, which in practice vary greatly in
size.

Shaper
------

Cake's shaper is *not* a [token bucket filter
(TBF)](http://linux-ip.net/articles/Traffic-Control-HOWTO/classful-qdiscs.html).
It operates in *deficit mode*, which is essentially the opposite way to
how a TBF works.

A major drawback of TBFs is that they require the bucket size to be
configured explicitly. This not only runs counter to Cake's goal of
perceived simplicity, but limits latency performance in the typical Cake
application, immediately upstream of a bottleneck link's dumb FIFO. On
flow startup, a TBF will dump the contents of its bucket into the FIFO
immediately, so the rate of the TBF must be reduced significantly below
the link rate in order to let the FIFO drain. Meanwhile, latency suffers
proportionally to the size of the bucket.

Cake instead schedules packets based on time deficits. If no deficit
exists when a packet is requested, it can be sent immediately. The
transmit time of the following packet is then calculated, and until that
time the shaper is placed in deficit mode. While in deficit mode,
packets are scheduled using a watchdog timer whenever a request arrives
too soon, and transmission times are calculated for a continuous packet
train. This continues until the queue drains; if a packet is requested,
but none are available *and* the next transmission time has been
reached, the shaper returns to the quiescent state in which the next
packet can be sent immediately.

Deficit mode makes the burst size dependent only on hardware and kernel
latency (including timer resolution), and minimises bursts without
requiring manual tuning. Cake's shaper can therefore be set much closer
to the actual link speed without jeopardising latency performance.
Modern hardware can achieve sub-millisecond bursts in most cases.

CPU efficiency is also improved by inverting the user's "bytes per time"
setting into a "time per byte" measurement, so that the packet
scheduling operation is essentially a multiply-accumulate rather than
involving a division. This is implemented using a manual floating-point
representation (mantissa and shift) for maximum precision and dynamic
range. This contributes to improved throughput on low-end CPUs.

Priority Queue
--------------

Diffserv is poorly specified, and not widely deployed outside
environments where Highly Paid Consultants are available to set it up.
Cake's priority layer aims to improve that situation by making a basic
yet robust Diffserv-based priority queue available with no end-user
effort. Hopefully, application support will follow.

Cake provides four traffic classes by default, nominally corresponding
to the four classes provided by 802.11e and 801.2p. However, the precise
mapping between Diffserv codepoints (DSCPs) and traffic classes is
different. In increasing order of nominal priority:

-   Bulk, with no bandwidth threshold
-   Best Effort, with 15/16 bandwidth threshold
-   Video, with 3/4 bandwidth threshold
-   Voice, with 1/4 bandwidth threshold

Most traffic falls into the Best Effort class. VoIP, NTP and gaming
traffic should be directed to the Voice class, BitTorrent should be
directed to the Bulk class, and the Video class is available for any
bulk traffic that requires elevated priority.

Cake implements *soft admission control*, and so is robust against
starvation attacks relying on strict priority, which would otherwise be
easy to trigger by accident. If a traffic class (including all traffic
in higher classes than itself) exceeds its bandwidth threshold, it is
demoted in priority until it falls below the threshold again. Hence, if
there is no competing traffic, any traffic class can use the full link
bandwidth, but it is always possible for new traffic in a different
class to start up.

The bandwidth threshold is tracked using the same algorithm as in the
shaper, at bandwidths which are scaled from the shaper's overall
bandwidth setting. Packets are not actually delayed at this layer; the
actual transmission time is merely checked against the deficit schedule.
Priority itself is implemented using a Weighted Deficit Round Robin
scheme, with the weight of each class depending on whether its threshold
is exceeded or not.

The progression of the bandwidth thresholds is roughly inverse to
priority. As with DRR++ (below), the assumption is that more
latency-sensitive traffic generally requires less bandwidth, and that
there is a fundamental tradeoff between priority and bandwidth which is
required for network stability. Enforcing that tradeoff in this manner
should encourage applications to choose an appropriate DSCP for their
traffic, rather than lazily applying the highest available priority for
"maximum" performance.

Flow Isolation
--------------

This was the original core of Cake, inheriting the basic design of
[fq\_codel's](https://tools.ietf.org/html/draft-ietf-aqm-fq-codel) flow
isolation scheme. It consists of a hash function over the 5-tuple flow
identifier to distribute packets to a large number of queues, and a
scheme similar to
"DRR+*":http://www.researchgate.net/profile/Mike\_MacGregor/publication/3867218\_Deficits\_for\_bursty\_latency-critical\_flows\_DRR/links/54a20b700cf256bf8baf7c61.pdf
to choose which queue to service. A separate set of queues and DRR*+
state is provided for each traffic class.

Cake's DRR++ scheme uses two lists of active queues. Newly active queues
are placed in the "new flow" list, which is served with strict priority
over the "old flow" list. After servicing, queues are always placed in
the "old flow" list. Queues found to be empty on servicing are removed
from the active lists. This relatively simple scheme naturally
prioritises "sparse" flows over "bulk" flows, on the assumption that
latency-sensitive traffic is likely to be sparse.

A major enhancement in Cake over fq\_codel is replacement of the plain
hash function with an 8-way set-associative version. Plain hashes are
susceptible to the "birthday problem" in which the probability of hash
collision reaches 50% when the table occupancy reaches the square root
of the table size (32 flows for 1024 queues), assuming a high-quality
hash; we have also found that the hash function fq\_codel relies on is
suboptimal.

In the set-associative hash, the set of queues is divided into *sets* of
8 *ways*. Ways are tagged with the flow identifier last assigned to
them, allowing hash collisions to be detected and avoided if another way
in the same set is available; either already tagged for the correct
flow, or empty and inactive. This is similar to the way set-associative
caches in CPUs work.

Active Queue Management
-----------------------

Cake uses a variant of the [CoDel
AQM](https://tools.ietf.org/html/draft-ietf-aqm-codel), instantiated for
each flow-isolation queue. This arrangement is again inherited from
fq\_codel, but subsequently modified for improved performance. The major
changes to date are:

-   The `count` variable now saturates rather than wrapping, and thus
    handles overload conditions far better. These are most likely seen
    with unresponsive and anti-responsive flows with a high packet rate.
-   The `target` and `interval` parameters are auto-tuned based on the
    shaper bandwidth. Target is never less than 1.5 MTUs' link
    occupancy, and Interval is never less than 8 times target. This
    improves throughput on slow links (under 1Mbps), and has been tested
    successfully down to 64Kbps. At higher bandwidths, `target` defaults
    to 5ms and `interval` to 100ms; these are also the defaults for
    standard CoDel.
-   When the dropping state is rapidly left and re-entered, `count` is
    halved rather than decremented. This improves the long-term
    stability of the signalling frequency.
-   Entering drop state now depends on how quickly the sojourn time
    is increasing. This effectively gives `interval` a 6:1 dynamic range
    around its nominal value, rather than a fixed value. Hence response
    to TCP's rapid slow-start growth is sharpened and to slow
    congestion-avoidance growth is dulled.
-   CoDel can now be instructed to ignore ECN capability by the
    packet-management layer, in case of an out-of-control queue length;
    it will then drop instead of marking, and mark the following packet
    instead (if it is ECN capable). This improves robustness against
    maliciously unresponsive flows and ECN washing.

Packet Management
-----------------

In addition to the four major layers, there are a number of
miscellaneous functions which are grouped here for convenience:

-   Maximum queue length in bytes (not packets) is dynamically
    calculated based on shaper bandwidth.
-   Queue overflow is handled by dropping from the head of the
    longest queue. The active queue lists are used to optimise
    search time.
-   Downstream packet encapsulation can be accounted for, both as a
    constant overhead and as ATM cell quantisation.
-   GRO/GSO aggregates are peeled into individual MTU-sized packets
    when appropriate. This greatly improves flow isolation on Ethernet
    hardware with excessively aggressive aggregation.

Configuration
-------------

Sensible defaults are provided for every aspect of Cake's configuration.
There are no mandatory parameters. All parameters can be specified using
a single 'tc' invocation, and most parameters can be updated without
losing packets using tc's "change" command.

In many cases, it is only necessary to set Cake's "bandwidth" parameter,
which sets up the shaper layer and performs auto-tuning in several other
places. If omitted, the shaper is set to infinite bandwidth (zero time
per byte) and thus effectively disabled. This can be made explicit by
specifying the "unlimited" keyword instead.

The priority-queue layer is configured using the "besteffort" (disables
it), "precedence" (legacy mode, 8 classes), "diffserv8" and "diffserv4"
keywords. The default, described above, is "diffserv4".

The flow-isolation layer is configured using "flowblind" (disables it),
"hosts" (ignores protocol and port fields), "dsthost" (uses only
destination address), "srchost" (analogous), and "flows" (default, uses
entire 5-tuple).

The AQM layer has no configuration options. However, it is planned to
add simple tuning options for different prevailing RTTs that may be
significantly different from the Internet-scale 100ms currently assumed.
Satellite links tend to impose longer RTTs, and enclosed LANs tend to
have much shorter RTTs.

Encapsulation compensation has a rich set of shortcut keywords,
corresponding to typical ADSL and VDSL configurations and
straightforward variants thereof. The "overhead" parameter and ATM
compensation flag ("atm" vs. "noatm") can also be specified directly.
Overhead compensation is turned off completely with the "raw" keyword,
and the "conservative" keyword sets up a quick-fix, with ATM cells and a
full cell of overhead, for where the actual overhead is uncertain.

Statistics
----------

Cake produces a rich set of statistics detailing the performance of the
various algorithms, and this can also be used to infer information about
the traffic passing through it. Simply run `tc -s qdisc`.

As of the 'fishcake' release, the statistics for each traffic class are:

-   **rate** - the priority layer's threshold bandwidth.
-   **target** and **interval** - the AQM layer's tuned parameters.
-   **Pk/Av/Sp delay** - the peak, average and sparse-flow delays
    experienced by recent packets. These are tracked using [biased
    EWMAs](https://en.wikipedia.org/wiki/Peak_programme_meter).
-   **pkts** - the total number of packets sent.
-   **way inds/miss/cols** - the set-associative hash reports 'indirect
    hits', 'misses' and 'collisions' whenever it needs to search
    the set. All other packets are 'direct hits' and are not
    directly counted.
-   **bytes** - total bytes sent.
-   **drops** and **marks** - number of packets dropped (by AQM or
    queue overflow) and ECN-marked (by AQM).

Additional statistics are planned in the near future, which will require
enlarging the stats struct and breaking compatibility with existing
versions of userspace code (tc).
