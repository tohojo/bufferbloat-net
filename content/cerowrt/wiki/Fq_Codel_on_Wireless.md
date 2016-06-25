---
title: Fq Codel on Wireless
date: 2012-07-03T14:07:50
lastmod: 2014-08-03T08:36:08
type: wiki
---
FQ Codel on Wireless-n
======================

Cerowrt was originally started to probe the epidemic of
bufferbloat-related problems observed with the current wifi deployments.

That proved too hard, and we went and worked first on fixing ethernet.
With BQL and fq\_codel we think we've made a real dent in that. Sadly
100s of ethernet drivers remain to be BQL-enabled, and soft-rate
limiting is finicky, so we are a long way away from seeing that set of
proven fixes ( [SQM](SQM.md) ) widely deployed.

3 years later... Cerowrt is now experimenting with various forms of
fq\_codel on top of the wireless stack. The problems in wireless-n are
so legion that it's difficult to know where to start.

We anticipate that making wireless-n work well will be a multi-year
re-architectural project in linux, requiring a half dozen people to do.
We have multiple brilliant folk working on the ideas in their spare
time.

-   Andrew McGregor - The original [minstrel rate control
    algorithm](http://linuxwireless.org/en/developers/Documentation/mac80211/RateControl/minstrel/)
    co-author
-   Felix Feitkau - current minstrel maintainer, also maintainer of the
    ath9k driver
-   Dave Täht - just [this
    guy](http://the-edge.blogspot.com/2010/10/who-invented-embedded-linux-based.html)

and a few others, with notable contributions from various bloat email
list members that also had something to do with linux wifi. Certainly we
welcome anyone else that wants to help fix the internet to join in, but
all we can offer is karmic rewards.

We totally lack a

-   QA person
-   Test Developer
-   Funding

It bugs us that there are million activations of android a day with a
wifi stack that can be so dramatically improved by a variety of queue
management techniques - and 10s of millions of APs and 100s of millions
of deployed wifi devices, all with problems -

most of which that would benefit HUGELY from the work, and yet we can
only work on this in our spare time.

So, lacking funding, in the meantime, we hack.

At the moment, felix is enabling new knobs in the ath9k driver, andrew
is working on various ns3 simulations, and Dave is experimenting with
reducing hw queue lengths and applying fq\_codel on top of wifi in
cerowrt.

fq\_codel at the qdisc layer for wifi is the "wrong thing" as:

1\) Wireless-n does packet aggregation to gain bandwidth. FQ on an AP
splits up streams into often non-aggregatable chunks.\
2) Reducing the hw queue length has a negative effect on throughput
over-all in the current driver design\
3) TXOPs, not bytes are the limiting factor\
4) You need **a** queue as a shock absorber, but you don't need 4 queues
to manage the hw queues, one that can feed 4 queues would be better and
save on memory use besides.

The principal usage of the fq\_codel and hw queue changes in cerowrt
3.3.8-10 and later is to observe how well or how badly codel reacts to
sudden, rapid bandwidth changes common in wifi. Losing good aggregation
in the short term is a good thing as it normalizes some results.

The "right thing", long term, appears to be:

0\) come up with a way to fund and test the work\
1) tie the codel aqm and minstrel's rate algorithms together better\
2) add per station queues to the wifi stack\
3) move codel into the mac80211 layer and make it's maxtarget value
account for the number of active stations and their aggregate queue
lengths\
4) fair queue inside each queue\
5) come up with additional sane drop strategies within aggregates\
6) Address the hidden management frames problem
