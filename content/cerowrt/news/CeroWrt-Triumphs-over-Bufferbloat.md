
---
title: "CeroWrt Triumphs over Bufferbloat"
date: 2015-03-10T07:47:37
type: news
author: Rich Brown
---
The CeroWrt project, and its implementation of fq\_codel as seen in the
current build of the firmware, eliminates the problem of bufferbloat.
These changes have been pushed into Linux kernel and the OpenWrt
mainline ("Barrier Breaker" release), and are now widely available.

Bufferbloat is the undesirable latency that comes from a router or other
network equipment buffering too much data. It has plagued network
routers from the early days. The problem was made worse as RAM became
cheaper: network engineers worried that dropping packets would make the
network slow, so there was an incentive to buffer more and more packets.
This had the paradoxical effect of retaining too many packets, which
hold up all the traffic behind those buffers.

Many efforts through the 1990s and 2000's attempted to address the
problem. Random Early Drop (RED) and its variants showed promise, but
didn't monitor the proper variables, and were thus hard to configure
properly and would hurt performance if not tuned correctly. Various
quality of service (QoS) policies can give priority to certain types of
traffic, but they're hard to configure. As traffic types change and
evolve, these policies become a maintenance hassle, since they need to
be rewritten on a regular basis.

In early 2012, Kathie Nichols took another look at the problem of
overbuffered routers and designed the CoDel (pronounced "coddle')
algorithm. The major insight was that the best way to avoid "too much
buffering" was to monitor a packet's *sojourn time* - the time elapsed
between when it was queued for transmssion and dequeued. If that time
exceeds a certain threshold (generally 5 msec), it indicated that the
packet had been queued for a long time. CoDel would then drop a
percentage of those packet to provide feedback to the sender that it was
using more than its share of the available capacity. An elaboration to
the CoDel algorithm - fq\_codel from Eric Dumazet - placed packets for
each source/destination flow in a separate queue, and applied the CoDel
algorithm to each queue to extremely good effect.

The resulting fq\_codel qdisc was put in to the Linux 3.5 kernel in July
2012.
