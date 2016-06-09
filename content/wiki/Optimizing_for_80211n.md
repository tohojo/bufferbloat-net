
---
title: Optimizing for 80211n
date: 2011-11-01T23:01:11
lastmod: 2011-11-02T01:01:55
---
Optimizing for 802.11n
======================

Background
----------

### Queue Types

The VI and VO queues have innate properties that are not propagated up
to the rest of the stack, notably they expect sub 100ms and 10ms
latencies respectively. The VO queue does not retry nor aggregate
packets (at present), the VI queue can (and does).

It is silly to inject jitter of greater than 100ms or 10ms into either
of these queues!

### Antennas (MIMO)

802.11n can send data from up to 4 antennas (spacial multiplexing) at
the same time, to different destinations.

Way forward
-----------

### TBQL - Time based Queue Limits

The VO and VI queues should have a drop head queue policy based on time
in queue.

Notes
-----

(THIS ISN'T EVEN A DRAFT. NOR IS IT A CORRECT. CONSIDER YOURSELF WARNED.
READ NO FURTHER)

Classification, fair queuing and active queue managment as it applies to
802.11n have been keeping me up nights. In particular coming up with a
sane way to use DRR or QFQ on 802.11n to any extent has caused some lost
hair...

I've started working on a wiki page to sort all the details out, I just
wanted to mention a few things this morning...

0\) Some form of per destination fair queuing would really help. Enough
detail about the destination is not visible outside of the driver level
to effectively solve the FQ problem, either - strict FQ would destroy
aggregation by splaying

Interestingly the QFQ algorithm (which we need to toss into debloat
testing) has a max MSS of 5 which means it's "mostly fair" but can still
bunch up packets somewhat, which is almost a useful property in the case
of wireless-n aggregation.

It would

1\) Shorter queues really help wireless-n be more 'interactive' under
load, and also punishes g far less (g with n is still terrible). TCP
responds amazingly well to the more modest & frequent levels of packet
loss and yields the link to other traffic much better. While I have a
nice plot of the last set of experiments I hope to do better and have a
repeatable experiment soon...

At the moment I'm using a txqueuelen of 40 \[2\] throughout cerowrt.
After having reduced the hardware tx queues \[3\] to bare minimums, this
seems to be a decent tradeoff. (At present! See numerous caveats in the
footnotes)

Part of why I did that was that it was proving difficult to find
theoretical models/papers that used numbers for buffering in their
simulations of greater than the range 50-100, so rather than feed in the
worlds actual (insane) numbers for buffering \[4\] into models, I
decided to feed in what the theorists used in the first place, into the
real world.

Not so amusingly the bottleneck then moves to the laptop(s), where,
again, a txqueuelen of about 40 'feels' right for HT40. Less and
wireless-n bandwidth really suffers, more and latency and userfriendly
'fairness' between flows goes to hell.

YMMV! - certainly other drivers than the ones I'm using have 'dark
buffers' hidden in them everywhere, exorbitant retries, weird power save
behavior, etc, etc.

Now, I'm not saying that '40' is a right number in any way, either - as
jim is fond of saying

And under sub-optimal (or with g) 40 is too large.

What it does suggest is that there is a reasonable upper bound to
txqueuelen that is much lower than the current default of 1000 on
wireless. With the current structure of the drivers, I tend to think
it's about 3x what I'm using - but to get there would require work (per
destination fair queuing, and each destination also fair queued as it is
aggregated)

The best solution is to implement would actually involve per-destination
micro-queuing which would also keep buffers of about 3x the measured
aggregation

I hate, like hell, suggesting additional buffering at the mac802.11
layer as a solution.

3\) Classification is (as mentioned elsewhere) an aristotlian rathole.
However, on what we are calling 'Ants' \[1\], some classification really
pays off with reduced annoyance levels, and I also somewhat accidentally
found something really nice which I'll get

I have implemented nearly full (and incorrect on several points in the
current patch)

In the previous discussion

\[1\] ANT: ARP, DHCP, DNS, most routing related messages,

I keep getting people that think that TCP ACKS are ANTS and they are
not: TCP ACKs are a different animal entirely. I'm not even sure if I
want to call DNS an ANT - I mostly think of ANTs as 'packets that need
to go very few hops - usually 1 - in less than 2 seconds - to do their
job'

--
