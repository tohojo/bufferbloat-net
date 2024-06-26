---
title: More about Bufferbloat
date: 2017-02-10T09:16:12
lastmod: 2022-06-11T11:26:12
type: wiki
---
# More about Bufferbloat

## What _is_ Bufferbloat?
Bufferbloat is the undesirable latency that comes from a router or other network equipment buffering too much data.
For a simple description of bufferbloat, read
[Best Bufferbloat Analogy - Ever.](https://randomneuronsfiring.com/best-bufferbloat-analogy-ever/)

For lots more details about the CoDel (and fq_codel) algorithm, see the
Codel wiki at: http://www.bufferbloat.net/projects/codel/wiki/Wiki

## Why does SQM work so well?

Why do cake, fq_codel, PIE, etc. and other qdisc's work so well? These smart
queue management (SQM) algorithms put each flow's traffic into its own
queue. (A "flow" is typically defined as traffic from a single IP
addresses/port to another address/port.) Then the qdisc makes sure that
none of the queues get "too long". To do this, the qdisc looks at all
the queues, and preferentially chooses to send packets from flows that
have no/small queue. If the queue for a flow gets large, the qdisc can
mark traffic with ECN, or drop a certain percentage of those packets to
allow congestion avoidance to kick in for that flow. (The various queue
management algorithms use different metrics to make these transmit/drop
decisions, avoid starvation, etc.)

## What's wrong with simply configuring QoS?

Quality of Service (QoS) settings will help, but won't solve bufferbloat
completely. Why not? Any prioritization scheme works by pushing certain
packets to the head of the queue, so they're transmitted first. Packets
farther back in the queue still must be sent eventually. New traffic
that hasn't been prioritized gets added to the end of the queue, and
waits behind those previously queued packets. QoS settings don't have
any way to inform the big senders that they're sending too fast/too
much, so packets from those flows simply accumulate, increasing delay
for all.

Furthermore, you can spend **a lot** of time updating priorities,
setting up new filters, and checking to see whether VoIP, gaming, ssh,
netflix, torrent, etc. are "balanced". (There is a whole
cottage industry in updating WonderShaper rule sets. 
[They all have terrible flaws](Wondershaper_Must_Die.md), and they don't help a
lot.) Worst of all, these rules create a maintenance hassle. Each new
rule has to be adjusted in the face of new kinds of traffic. And if the
router changes, or speed changes, or there's new traffic in the mix,
then they need to be adjusted again.

## Setting up a Router Manually

If you can't get SQM/fq_codel in your router, your strategy should be
to adjust the settings to control queue lengths first, then think about
QoS. To do this:

1.  Remove all the QoS/Prioritization rules.
2.  Control the amount of data queued. If your router supports BQL in
    the kernel and some kind of SQM/qdisc, such as fq_codel, PIE, etc.,
    make sure they are enabled. In general, no configuration is required
    at all. These changes are available in modern Linux kernels, the
    OpenWrt and CeroWrt routers, and a growing number of other devices.
    This one change automatically sets up the router to work well:
    - Small flows of data (pings, DNS, ssh sessions, gaming, VoIP, 
        SYN/Ack messages for TCP/web traffic, etc.) 
        go right through with minimal delay
    - Large flows (Netflix, file uploads/downloads, filesharing, etc)
        automatically adjust their rates
    - All traffic gets a fair share of the bottleneck traffic capacity
3.  Measure. Try to detect if all your data types/flows are as
    responsive as you like. We often find that there is no need for
    further configuration because the fq_codel algorithm does such a
    good job of giving priority to the flows that aren't sending
    much data.
4.  If you **can** determine that some traffic needs to priority, then
    set up some QoS rules. The number of rules will probably be small,
    perhaps only applying to a couple specific traffic types.
5.  And finally... If prioritization/QoS
    doesn't solve the problem, it may be necessary to get
    more bandwidth. When SQM is in place, the need for prioritization
    typically arises when there's already too much data to send on a
    long-term basis. Creating the rules simply determines which packets
    go to the head of the queue, and which will be sent later. If there
    is regularly more data than traffic capacity, QoS doesn't
    really help.

