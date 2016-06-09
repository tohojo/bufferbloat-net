
---
title: Smart_Queue_Management
date: 2013-12-29T01:38:45
lastmod: 2014-03-23T00:50:14
---
Smart Queue Management
======================

"Smart Queue Management", or "SQM" is shorthand for *an integrated
network system that performs better per-packet/per flow network
scheduling, active queue length management (AQM), traffic shaping/rate
limiting, and QoS (prioritization)*.

"Classic" QoS does prioritization only.

"Classic" AQM manages queue lengths only.

"Classic" packet scheduling does some form of fair queuing only.

"Classic" traffic shaping and policing sets hard limits on queue lengths
and transfer rates

"Classic" rate limiting sets hard limits on network speeds.

It has become apparent that in order to ensure a good internet
experience all of these techniques need to be combined and used as an
integrated whole, and also represented as such to end-users. After years
of debate on the bloat and AQM mailing lists, no name for the idea has
been agreed on. A lot of people object to "smart queue management" as
being too general a phrase ("you can do anything and call it smart"),
but we hope that by defining it as we have above to limit the
mis-appropriations. A trademarked name has been suggested as well...

Probably the first widely deployed fully integrated "smart queue
management" system was the venerated
[wondershaper](http://lartc.org/wondershaper/), which emerged in the
early 2000s as the linux based shaper of choice. It was widely deployed
in internet cafes around the world, and in Linux users' homes and
workplaces. Although for the time it was a breakthrough, it has since
been obsoleted by events and bugs in its design. See <link>Wondershaper
Must Die</link>.

Much work on AQM (active queue length management) technologies like RED
and BLUE took place in the period 1990-2002. Many variants of RED
appeared between 2002 and 2013 - FRED, ARED, LRED, etc, but work mostly
stagnated under variants of the same set of ideas, until the creation of
the bufferbloat effort in 2011, which begat Codel and PIE. Feedback from
the effects of these algorithms have led to improvements in various TCP
implementations as well.

Packet scheduling has a longer and more successful history, starting
with the first research into "fair queueing" in the mid-1980s and
continuing to the present day with ideas like DRR, SFQ, QFQ and SQF.
Along the way it was realized that strictly "fair" queueing was not
desirable, which led to optimizations like WFQ (weighted Fair Queueing),
SQF (shortest queue first), and sparse stream optimizations like those
in fq\_codel. Lacking a better phrase we try to distinguish between
old-style "fair" queuing and new-style "flow aware queueing", but the
common understanding of the abbreviation "FQ" = Fair Queueing is the
source of much confusion.

These techniques ( shaping, prioritization, packet scheduling, and AQM)
are often used in serial, rather than parallel.

It is possible to make things worse by applying only a few of these
techniques, a classic example of this is in NetGear's current QoS system
which allows you to rate limit **but holds the fifo queue lengths
constant**, and does not apply either packet scheduling or AQM, leading
to exorbitant delays. SFQ, used alone at higher bandwidths gets the
bursty tail drop problem an AQM can solve. An AQM, used alone, has
trouble managing bursts. QoS, used alone, only works on what packet
types can be classified easily. And, policing, set incorrectly, can
seriously damage downloads.

WRED was probably the most successful of the packet scheduling/QoS/AQM
hybrids. fq\_codel (the principal candidate for a successor to WRED)
combines smarter packet scheduling with a innovative AQM design into a
single algorithm also, but does not have native support for QoS packet
markings. It is usually combined with something else to do that.

Most QoS systems as shipped today are terrifically elaborate and let you
prioritize certain packet types to your heart's content, but this is of
no help in a world that consists mostly of bursty web traffic on ports
80 and 443.

Rate limiting is presently stuck with token bucket designs descended
from the original CBQ, like HTB. Software rate limiting is far more
abusive of CPU than any of the packet scheduling or AQM algorithms
discussed above, or their hybrids.

Traffic shaping ("policing") was a not very good idea hard limiting
ingress speeds that become common because of the ease of implementation.
It is far saner to apply Smart Queue Management to "police" traffic at
today's higher speeds.

Examples of deployed Smart Queue Management systems include CeroWrt's
<link>SQM</link> implementation, OpenWrt's qos-scripts, IPFire, the
Gargoyle router project, and
[Streamboost](http://www.qualcomm.com/media/releases/2013/01/04/qualcomm-introduces-streamboost-technology-optimize-performance-and)
. WRED is deployed in many locations. France Telecom deploys SFQ.
Free.fr has the first known large-scale fq\_codel deployment, using
three bands of fq\_codel for tiers of QoS. (it is also the largest ECN
enabled end-user deployment). The Streamboost product (now coming
available in multiple 802.11ac routers) combines a bandwidth sensor,
with a packet classification engine, with a multi-band fq\_codel
implementation.

We are beginning to characterise these in an upcoming internet draft on
[comprehensive queue management in home
routers](http://snapon.lab.bufferbloat.net/~d/draft-taht-home-gateway-best-practices-00.html)
