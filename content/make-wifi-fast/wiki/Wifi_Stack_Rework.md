---
title: Wifi Stack Rework
date: 2014-08-03T09:11:00
lastmod: 2015-10-14T04:20:05
type: wiki
---
Wifi Stack Rework
=================

None of the aqm and packet scheduling algorithms apply very well to
aggregated macs, notably those in wifi 802.11n and 802.11ac. We
anticipate that the work on improving the performance of these will also
apply to other aggregated packet delivery technologies, notably cable,
3g and 4g, and 802.14 and 6lowpan, but fixing wifi is up first.
(incidentally a better title for this section is needed)

this wiki page is out of date, the full description of everything we
have fixed or have fixes in the pipeline for is in the battlemesh talk
and pdf

https://www.youtube.com/watch?v=-vWrFCZXOWk

and there is a much larger document, currently in word format, that goes
deeper than the below.

Goals
-----

1.  Reduce latency on a single AP, single station connected at the
    lowest rate (6mbits) to under 30ms under load, down from the
    commonly observed 600ms or more, while not sacrificing peak
    throughput under real world conditions
2.  Develop new packet scheduling and AQM techniques applicable to
    aggregated, parking lot network types
3.  Improve the stack sufficiently for 802.11ac MU-MIMO to actually work
4.  Save the world

AP, mesh, mode rework
---------------------

### Improvements to the minstrel rate selection algorithm

The minstrel rate selection algorithm was originally developed against
wireless-g technologies in an era (2006) when competing access points
were far less prevalent. While updated significantly for wireless-n a
thorough analysis has not been performed in the wide variety of rates
and modern conditions. Also, some new mathematical techniques have been
developed since 2009 that might make for better rate control overall. A
new ns3 model will be developed to mirror these potential changes and a
sample implementation produced for the ath9k chipset (at minimum).
Minstrel2, tenatively named "BARD", will do a much better job on
agreggation and in MU-MIMO conditions.

### Sort on dequeue

An aggregate of packets arrives and is decoded all at once, and then
delivered in FIFO order at a high rate (memory speeds) to another
device, usually ethernet. However that high rate is often still too slow
for a fq\_codel qdisc attached to that ethernet device to actually do
any good, so it would be better to sort on the dequeue (of up to 42
packets), then deliver them to the next device.

We believe that if the delivery is sorted (fair queued), that more
important packets will arrive first elsewhere and achieve better flow
balance for multiple applications. Multiple chipsets deal with packet
aggregation in different ways, as does firmware - some can't decode any
but the entire aggregate when encrypted, for example, they arrive as a
binary blob, and there are numerous other chipset and stack specific
problems.

### Reducing retransmits

Retransmit attempts should move from a counter based to a time and other
workload based scheduler. This will help keep bad stations from
overwhelming the good, and reduce latencies overall. Losing more packets
is fine in the pursuit of lower latency for all.

### Selective retransmit

Currently all Linux wifi drivers are dumb when it comes to
retransmitting portions of an aggregate that fail, attempting to
perfectly transmit the entire aggregate. In the general case, not all
packets need to be retransmitted - examples include all but the final
tcp ack in a flow, all but the last voip packet in a flow, and so on.

### Single queue promotion to 802.11e and per station queueing

The current structure of the linux wifi stack exposes only the 802.11e
wifi queues, not multicast, and not the queues needed for multiple
stations to be sanely supported. Repeated tests of the 802.11e mechanism
shows it to be poorly suited for a packet aggregation world. By reducing
the exposed QoS queue to one, we can instead expose a per-station queue
(including a multicast queue) and manage each TXOP far more sanely.

There are a few other options as to what layer this sort of rework goes
into. Given the current structure of the mac80211 stack, it may be that
all this work (exposure of the station id), has to take place at that
layer, rather than the higher level qdisc layer.

### Power aware scheduling

It may be possible to do transmits at "just the right power" for the
receiving station. Code for this exists but has not been tried outside
academia.

### codel

While codel appears to be a great start in managing overall queue
length, it is apparent that modifications would be needed to manage
txops rather than packets, and the parking lot half duplex topology in
wifi leads to having to manage the target parameter (at least) as a
function of the number of active stations, and closer integration into
minstrel for predictive scheduling seems needed also.

### fq\_codel

See above. A perhaps saner approach than a stochastic hash is merely to
attempt to better "pack" aggregates with different flows whenever
possible, taking into account loss patterns, etc. Setting aside 42
buckets for each station is not a lot of overhead.

### MU-MIMO support

Nearly all of the changes above have potentally great benefit in a
MU-MIMO world, and are in fact, needed in that world. Regrettably none
of the major chipset makers nor router makers seem to be co-ordinating
on a standard api structure for doing this right, and it is hoped that
by finding and targetting at least one MU MIMO chipset that progress
will be made.

Station improvements
--------------------

While many of the above improvements also apply to stations, the
benefits are more limited. The overall approach should be to do better
mixing and scheduling of the aggregates that a station generates, and to
hold the queue size below 2 full aggregates whenever possible. Further
improvements in station behavior include predictive codel-ing for
measuring the how and when EDCA scheduling opportunities are occuring,
and so on.

Better Benchmarks and tools
---------------------------

Leveraging the netperf-wrapper test suite, we hope to encourage industry
and users to look at the real problems of wifi on voip,
videoconferencing, gaming, and web traffic. There are other benchmarks
being developed that look hard at the problems in bursty traffic as
well.
