
---
title: Reconciling codel variants
date: 2012-08-11T21:53:21
lastmod: 2012-08-13T15:13:18
---
Reconciling codel variants
==========================

See [Van Jacobson's talk at the recent
ietf](http://recordings.conf.meetecho.com/Recordings/watch.jsp?recording=IETF84_TSVAREA&chapter=part_3)
for an overview of the core concepts in codel and fq\_codel and fairly
current status.

Codel
-----

### The original algorithm

In the original algorithm, as published in the original paper, the count
variable would increase without bound.

This was discovered on the third day of the implementation, and after
several experiments, was discarded in favor of several alternatives.
These alternatives have various theorists and implementors wandering in
different directions, doing different sort of tests. Uniformly the
results of all current variants are pretty good, but not "optimal"...

### Linux 3.5 and cerowrt 3.3.8-17 and prior

The linux version has a more aggressive "decrease the drop schedule"
state, and retains the "increase the drop schedule rapidly when in a
massive drop state" state.

This leads to long-period oscillations in short and overlong RTTs.
However this testing has been not repeated yet, as at the time there was
an initialization bug in the 0 state of the codel algorithm fixed in
net-next and queued up for linux 3.5.x.

It also contains some performance optimizations vs a vs the ns2 models -
notably using fixed point arithmetic, and using a newtonian method to
calculate the increase in the invsqrt (valid), as well as the decrease
(possibly dicey).

### Current ns2 model

The current ns2 model does not exhibit the counting without bound as the
control law is entered more rarely and not during a burst of packets, so
count increments more slowly. The count decrement on re-entering a drop
state is by 2.

### Current ns3 model

Is a close analog to the Linux implementation, including the newtonian
invsqrt but with a decline of 2 packets per re-entry from drop state,
rather than the linux algorithm. It is also missing a critical fix to
the 0 state that is now in Linux 3.5.1.

Fq\_Codel
---------

### ns2 model

The ns2 model as implemented by Kathie and Van is "Packet Fair". It has
the benefit of even more simplicity than the linux model, however it may
not be appropriate in asymmetric bandwidth scenarios.

### Linux 3.5 implementation

The Linux 3.5 implementation is "byte fair", where X amount of bytes are
delivered per quantum X, where quantum X has a range of 256 through 64k
- with a single mtu (1500) being the default. It would be interesting to
see how various quantums behave in various scenarios.

Testing and testers
-------------------

### Kathie Nichols/Van Jacobson

Continues to think upon and modify the core ns2 model to reflect results
reported from the testers.

### Andrew Mcgregor

Works with both a the Linux implementation and his ns3 model. His
primary dumbbell ns3 model is focused on the sorts of special problem
New Zealand faces - with very short on-island RTTs, and very long (230+)
ms RTTs. Until recently most of his work was using a 4500 byte quantum
rather than the default.

### Dave Täht

Is primarily focused on improving latency on the two sides of the edge
devices, at bandwidths ranging from 2Mbit to 20Mbit, as well as the
upcoming issues with wifi.

Works with the ns3 model, the linux kernel on x86, and the cerowrt
implementation, in a variety of scenarios - notably with a live
deployment in Los Gatos california, which is mostly targetted at getting
some long term data on wifi.

He's working better charactising overall codel behavior in an embedded
box with BQL and with soft rate limiting (HTB or HFSC), and with native
ipv6 in the mix.

Internal tests of cerowrt include tests to/from <link>bloat:bloatlab
\#1</link> from various locations around the US, as well across multiple
cerowrt boxes and laptops setup in various scenarios. High on the list
of simulated tests to add is larger RTTs.

Given that smaller quantums had not been explored, cerowrt 3.3.8-17 runs
with a 256 quantum for fq\_codel on almost all queues. Prior work used
3000 byte quantums on wifi, 1500 on ethernet.

### Jim Gettys

Is working with comcast's highest end service, with 100Mbit down/20Mbit
up. (and thus is blowing up dave's 20/4Mbit models)

Is using cerowrt and linux/windows based hardware to servers running
across the continental US at roughly a 100ms RTT, as well as his std
bufferbloat busting bandwidth saturating 10ms scp to MIT test.

### Eric Dumazet

Has a primary focus on improving bufferbloat on 10GigE (and higher)
devices. He typically runs with a much shorter RTT (500us) and target
(20ms) than the default, aiming at good performance in the data center
environment rather than in the web at large.

### Unnamed BigCorp 1

Did an extensive analysis of linux's implementation showing some
difficulties at really high (150 tcp) saturating workloads. (the
oscillation issue noted earlier)

### BigCorp 2

has set up a set of servers in Russia for testing of both short 10GigE
and long RTT links. No results as yet.

### Stanford

Researchers at Stanford have reproduced most of the results of the early
codel and fq\_codel work. [Their work on Codel and
fq\_codel](http://reproducingnetworkresearch.wordpress.com/2012/06/06/solving-bufferbloat-the-codel-way/)

### Others?
