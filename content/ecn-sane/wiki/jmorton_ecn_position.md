---
title: Jonathan Morton's Take on ECN
date: 2018-08-30T15:38:14
lastmod: 2018-08-24T15:38:14
type: wiki
tags: ecn-purple

---

# Jonathan Morton's Take on ECN

I would characterise the problem not as "should we use ECN or not",
but "how does ECN need to evolve to reach its potential".  This likely
means changes in both routers and endpoints, but since there is
already some deployment, changes have to be backwards and forwards
compatible.

The DCTCP approach fails primarily because it is not backwards
compatible.  DCTCP endpoints do not react as intended to ECN signals
given by Codel, which was designed very specifically around
RFC-compliant TCP behaviour.  That's why there is concern over BBR2's
proposed handling of ECN, which follows the DCTCP model instead of the
RFC-compliant model.  For similar reasons, other proposals to "soften"
the response to individual CE marks are Bad Ideas.

In my view, ECN is essential for modern congestion control.  Without
it, there is no way to separate random loss and re-ordering from
congestion signals, and signalling congestion incurs application
latency penalties due to HoL blocking in TCP while the lost packets
are retransmitted.  With ECN, congestion can be signalled
unambiguously *as* congestion, and without incurring retransmits;
network engineers who rely on packet loss as a primary metric should
also be pleased by its deployment.

The evidence *against* ECN chiefly consists of its present effect on
inter-flow latency with exemplary-standard flow isolation, under
particular measurement techniques in which the latency-measuring flows
are treated as saturating flows and thus equal to the rest of the
saturating traffic.  This is a remarkably specific and unusual set of
circumstances, which seems unlikely to be replicated by real traffic.
Nevertheless, there are improvements that can sensibly be made without
ditching ECN entirely.

Principal among these is enabling TCP senders to operate at very small
cwnds.  Presently, most appear to operate on the principle that four
packets must be kept in flight at all times (unless application
limited), so that a single lost packet can be reliably detected and
retransmitted within one RTT.  Additionally, some widely-deployed TCP
stacks define the cwnd only in terms of whole MTU-sized packets.  The
net result is that the effective cwnd cannot shrink below 4xMSS, when
sometimes 1xMSS (perhaps still as two, three, or four distinct
packets) would be more appropriate.  In such cases, Codel devolves to
continuously marking all packets in these flows, ensuring that they
remain at their minimum cwnd.

With the advent of TCP pacing, fractional cwnds are theoretically
practical to implement, such that on average there is less than one
packet in flight.  I remain uncertain that such extreme measures are
necessary or desirable, given the re-engineering required
(ie. changing cwnd from a packet to a byte basis) to implement them.
However, pacing out one MSS over an RTT via four separate packets
should be easier to implement and would help the aforementioned case,
by reducing the serialisation delay multiplier in the overall
inter-flow latency equation.  An individual sender implementing this
incurs a slight throughput cost due to greater relative packet
overhead, but may immediately see an application latency improvement
of a few milliseconds in the given scenario - or a larger latency
benefit at very low bandwidths.

As an alternative to the DCTCP model, using the distinction between
ECT(0) and ECT(1) could be a backward-compatible method of providing
"softer" congestion signals to endpoints.  Existing endpoints and
routers would ignore the distinction, treating both as merely
indicating an ECN Capable Transport.  An old RFC suggested using the
distinction to protect the integrity of the ECN signal itself, but
this was never deployed and there are no plans to do so.

Modified routers could detect incipient congestion - which has not yet
merited a CE mark but warrants caution on the part of TCP senders -
and convert some proportion of ECT(0) marks to ECT(1) to give a
fine-grained control signal.  It should be feasible to reflect that
information back to the sender, which can then perform a greater
variety of cwnd evolutions, not just slow-start followed by AIMD.  In
particular, these signals could instruct the sender to drop out of
exponential or polynomial growth in favour of additive-increase, or to
hold cwnd steady instead of oscillating, or to perform
additive-*decrease* to correct a slight overshoot.  Only if the latter
was not sufficient would a CE mark be sent, with the RFC-compliant
response expected.

I certainly don't want to write off ECN before the above measures are
at least tried.
