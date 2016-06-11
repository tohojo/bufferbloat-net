
---
title: Wiki
date: 2012-05-06T18:52:34
lastmod: 2015-10-14T10:26:53
type: wiki
---
CoDel Overview
==============

CoDel is a novel “no knobs”, “just works”, “handles variable bandwidth
and RTT”, and simple AQM algorithm.

-   It is parameterless — no knobs are required for operators, users, or
    implementers to adjust.
-   It treats good queue and bad queue differently - that is, it keeps
    the delays low while permitting bursts of traffic.
-   It controls delay, while insensitive to round-trip delays, link
    rates, and traffic loads.
-   It adapts to dynamically changing link rates with no negative impact
    on utilization.

CoDel (the name comes from "controlled delay") is the first fundamental
advance in the state of the art of network Active Queue Management in
many, many years.

It is pronounced "coddle", because it handles network streams in a
gentle way.

With the "fq\_codel" variant (Fair/Flow Queueing + Codel) it is possible
to reduce bottleneck delays by several orders of magnitude, and provide
accurate RTT estimates to elephant TCP flows, while allowing shorter
(sparser) flows like DNS, ARP, SYN, routing, etc packets priority
access.

We don't say **several orders of magnitude** lightly. We have [the
benchmarks](http://www.bufferbloat.net/projects/codel/wiki/RRUL_Rogues_Gallery)
to back it up. Some more recent benchmarks on cable systems are here:
http://burntchrome.blogspot.com/2014/05/fixing-bufferbloat-on-comcasts-blast.html
- and there are multiple papers on the subject now of widely varying
quality.

Deployments
-----------

OpenWrt Barrier Breaker, Chaos calmer and later, CeroWrt, dd-wrt, IPfire
and many others now use fq\_codel in their main QoS system.\
Free.fr's revolution V6 router uses it by default. It is also available
in ubnt's edgerouter series of products.\
It is a component of Qualcomm's "streamboost" QoS system. It is in
Netgear's "Dynamic Qos" feature for their X4 product.\
And in many places elsewhere. Linux version 3.6 and greater has support
for it (not turned on by default). The sysctl\
knob landed in 3.12, and systems that use systemd, like fedora 22, now
default to fq\_codel.

We are nearly done creating a successor to fq\_codel and the "sqm"
system, called
[cake](http://www.bufferbloat.net/projects/codel/wiki/CakeTechnical)
which we addresses a few edge cases fq\_codel had, is faster code, and
better all across the board.

Papers and Publications
-----------------------

The most up to date descriptions of codel and fq\_codel are now the
subject of IETF internet drafts.

[Codel](http://tools.ietf.org/html/draft-nichols-tsvwg-codel-02)

[FlowQueueCodel](http://tools.ietf.org/html/draft-hoeiland-joergensen-aqm-fq-codel-00)

Older Papers
------------

[Controlling Queue Delay](http://queue.acm.org/detail.cfm?id=2209336)
ACM Queue, Kathleen Nichols, Van Jacobson, May, 2012\
[Codel](http://www.pollere.net/CoDel.html) page at
[Pollere](http://www.pollere.net) . Pollere does research on and
analysis of network performance via modeling and simulation,
measurement,and laboratory prototypes.\
[Kathie Nichol's
CoDel](http://recordings.conf.meetecho.com/Recordings/watch.jsp?recording=IETF84_TSVAREA&chapter=part_3)
at the IETF-84 Transport Area Open Meeting, 30 July, 2012, Vancouver,
Canada, by Van Jacobson.

Simulations
-----------

Kathie Nichols' and Van Jacobson's original [ns2 simulation of
codel](http://www.pollere.net/CoDel.html)\
Their most current ns2 code is now available [via
git](https://github.com/dtaht/ns2)

We worked on updating the codel and fq\_codel ns3 simulations in a
[github repository](https://github.com/dtaht/ns-3-dev) - but that is now
obsolete. Codel landed in ns3 mainline in sept, 2014, as part of the
Google Summer of Code, and fq\_codel (and variants) are slated for the
next version.

There are now basically 6 slightly different variants of codel (see
[Reconciling codel variants]({{< relref "wiki/codel/Reconciling_codel_variants.md" >}})), flying in loose formation. The
code as published in the original paper is obsolete. Research is
continuing. Come help!

Mailing list and chat room
--------------------------

There is a [CoDel mailing
list](https://lists.bufferbloat.net/listinfo/codel), and discussions
that take place on irc.freenode.net in the \#bufferbloat chat room.\
Please go to the codel mailing list if you have questions.

Linux Code
----------

CoDel - in order to run well at line rate - requires the Linux 3.3 [Byte
Queue Limits](http://lwn.net/Articles/454390/) . It has proven too hard
to backport BQL to Linux 3.2 or earlier (an attempt for 3.2 exists, but
no driver support), so you will need to upgrade to Linux 3.5 or later,
and have a driver that supports BQL (only about 24 as of the present
writing).

If you are doing soft rate limiting (eg shaping with HTB or HFSC), BQL
is **not** required at the driver level. Codel and fq\_codel are in the
Linux 3.5 release - no patches are required, but BQL support is limited,
as noted. There were multiple bugs in HTB fixed prior to Linux 3.11.

While fq\_codel and codel are "no knobs" qdiscs, several other knobs can
be tweaked for the lowest latency results. An example script for doing
that is called "debloat.sh" which is available from [the deBloat
repository](https://github.com/dtaht/deBloat) on github. It tunes up
BQL, turns off various forms off tcp offloads, and offers both a
fq\_codel and codel + qfq model to play with. Turning off BQL is not
really needed since linux 3.8 and later, the autotuning works well. TCP
small queues has evolved to\
where it does the right thing with TCP offloads as of linux 3.12.

So most of the debloat script is no longer needed.

All codel and fq\_codel development was pushed into the linux mainline
as of linux 3.6 and you should look there for the most up to date code.

iproute2 added support for fq\_codel in the 3.6 release and
configuration and statistics should be available by default in most
Linux systems shipped today.

[CeroWrt]({{< relref "wiki/codel/Wiki.md" >}}) Version
-----------------------------------------

The CeroWrt research router project was started, specifically, to test
new AQM technologies, and has been tracking codel closely.

A pretty solid build [is now
available](http://www.bufferbloat.net/projects/cerowrt/wiki/CeroWrt_310_Release_Notes)

The fq\_codel code has already migrated into the OpenWrt mainline (upon
which Cerowrt is based), so the research has paid off! - there is more
to come...

Binary code and kernels for Linux based operating systems:
----------------------------------------------------------

All modern linux distros now ship with fq\_codel.

For servers with tcp-heavy workloads, particularly at 10GigE speeds, for
queue management, we recomend sch\_fq instead of fq\_codel as of linux
3.12.

Either qdisc can be enabled by default via a single sysctl option in
/etc/sysctl.conf

net.core.default\_qdisc = fq\_codel \# best general purpose qdisc

net.core.default\_qdisc = fq \# for fat servers, fq\_codel for routers.
Note that in a virtualized environment the underlying server IS a
router, the guest VMs are hosts and we don't have a lot of data
regarding either qdiscs' performance at 10gigE speeds on vms - and early
data on fq shows fq\_codel's lowered quantums of benefit at 1GigE and
below. We certainly expect fq to continue to improve on hosts and
servers... and we expect fq\_codel to improve also.

Code for other operating systems
--------------------------------

A port of Codel exists for BSD and is available in pfsense and
elsewhere.

Known issues
------------

At very low bandwidths (e.g. .5Mbps) on ADSL, we're having to play with
the target; Kathie did not have to in her simulations. This is due to
inevitable buffering\
in htb or in the device driver. We have a version under development that
does bandwidth limiting without buffering an extra packet, called cake.
It's looking good so far.

People have tried to run CoDel in very big routers, with hundreds of
simultaneous flows, a situation not simulated in advance. There, it
isn't controlling the queue the way it should: whether this is a problem
with the algorithm, or the implementation, is not yet understood.
fq\_codel does better in this case.

It is clear that without lowering the target and interval variables,
CoDel is not appropriate for AQM of traffic solely inside a data center;
it does not react in a timely enough fashion. Whether the modifications
of the ideas in CoDel will solve this problem is not yet known. Again,
this is an area which CoDel was not designed to solve or it simulated in
before publication.
