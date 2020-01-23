---
title: Getting SQM Running Right
date: 2016-07-04T12:00:00
lastmod: 2020-01-23T18:10:12
type: wiki
---

# Getting SQM Running Right

The Smart Queue Management (SQM) system on OpenWrt makes it easy to configure a
rate limiter on your router. The goal is to set the software shaper to a
bandwidth that is slightly lower than the actual (bloated) bottleneck in the
hardware, so we can control the queue using FQ-CoDel or CAKE. In many cases,
there is no real ground truth about the right setting, but we can find one by
trial and error (tuning and doing repeated measurements until things improve).


## A walk-through of a tuning session

This is a report of Dave Täht's experience tuning Cerowrt's Smart Queue Management (SQM) system for a cable modem at Jim Reisert's home. The SQM system (which works on any Linux-derived system) uses HTB + fq_codel underneath to give low latency to competing streams, and the codel AQM system to keep overall queue lengths short. 

*Note: The following example describes a tuning session for CeroWrt, but it is identical
to configuring SQM in modern OpenWrt firmware.*

It took 4 tries (and 5 minutes) to get a setting that worked well! When we were done, we watched a videoconference and ran screen sharing session over skype while saturating the network with a RRUL test for 5 minutes.

Download and upload speeds remained high, latency remained low, and there was no observable effect on the video conference. It was *perfect*.

**How to read the RRUL plots below**

The [RRUL test](./RRUL_Chart_Explanation.md) normally runs for 70 seconds: 5 seconds of idle (to give a baseline), 60 seconds of full-rate data transfer, and 5 more seconds of idle. There are three graphs:

1. Download speed (top)
2. Upload speed (middle)
3. Latency (msec, bottom)

The (four) **colored lines** indicate separate, simultaneous TCP sessions.
The **black line** represents the average of those four upload/downloads;
multiply that value by four to get the actual data rates. 

For example, the top chart shows (1.2 mbps * 4 = about 4.8mbps); 
middle chart shows (7mbps * 4 = about 28 mbps), 
and latency starting low, 
but ramping to over 1000 msec (over one second) during the test. 

<!-- ![](/attachments/sqm-setup-ipv6_withsqm-24-4400-long.svg) -->

![](/attachments/sqm-setup-ipv6_withsqm-3.svg)

*Dave picks up the narrative...*

"After installing the latest CeroWrt and leaving SQM *turned off*, I ran the RRUL test remotely. 
This was how his cable connection behaved without any latency control. 
*(See charts above.)* 
We see the usual 1-2 seconds worth of induced latency common to (and bedeviling!) current cable deployments. 
_(Note: the up and download figures for all these charts are reversed since I was running RRUL from a remote server, not from within Jim's network, as is normally done.)_

"While awesome to be able to run this test over native IPv6, 1.2 seconds of latency left something to be desired. (The latency problem has nothing to do with IPv6, or IPv4, but bufferbloat in the modem and CMTS).

"The early spike here of extra bandwidth is due to speedboost kicking in for 10 seconds and providing some extra bandwidth, but even as it begins to kick in latencies are already skyrocketing.

"So taking a guess at the bandwidth from the averages (the black line * 4) on the up/down graphs, we tried setting setting CeroWrt's Smart Queue Management system (SQM) to 38mbits down and 8 up. 
(Well, actually I goofed when I looked at the graphs: 7*4 = 28, not 38). Note also that the black lines do not correctly add in the bandwidth used up by the tcp acks in the opposite direction. On some systems you need to factor in ~1/40th the bandwidth used in the opposite direction for a more correct estimate.

![](/attachments/sqm-setup-ipv6.svg)

"A little better, but it still looks as if the data was taking a side jaunt to the moon!

"Taking another guess, we tried, 24mbps down and 6mbps up.

![](/attachments/sqm-setup-ipv6_withsqm-24-6.svg)

"Much better! But given the increase in latency and the average where it was, it was apparent that 6 mbit up was still too much, so we knocked that down to 4400 (kbps, or 4.4 mbps), and got this:

![](/attachments/sqm-setup-ipv6_withsqm-24-4400.svg)

"A total increase of observable latency over the baseline of 65ms of 10 milliseconds (vs 1.2 seconds! A 110x improvement... ) and good sharing between streams and good throughput. And thus, we declared victory, and then talked for an hour doing various other tests while the videoconference continued to rock.

**Final Notes:**

These tests were on CeroWrt against a Comcast connection with IPv6 enabled, taken with a Motorola SB6141 cablemodem running firmware SB_KOMODO-1.0.6.10-SCM00-NOSH. OpenWrt's Qos-scripts use similar techniques to CeroWrt's SQM system, but are not IPv6 compatible, neither are most versions of wondershaper. It is unknown to what extent other smart queue management systems (gentoo, ipfire, streamboost, gargoyle) handle IPv6 at present. (and CeroWrt gets the same good results with any combination of IPv4 and IPv6)

_Update 2014-5-17:_

I reran the plots to clean up the plotting bug that we'd had in an earlier version. Since this test series was first run the netperf-wrapper tool (now called ["Flent"](http://flent.org)) has gained the ability to compare multiple test runs. Previously, we were well aware that disabling powerboost (as we currently do) gives consistent latency, but leaves some bandwidth on the floor. How much was kind of an unknown.

Now we know. The speedboost algorithm is fairly well documented, and we do think that with some tweaks and fixes to the htb rate limiter to allow for more burstyness we can keep latencies reliably low and get closer to the full bandwidth available from a cable modem, all the time.
(But we have no funding, and we're focused on fixing wireless next.)

Losing that initial bit of bandwidth, in light of always getting good latency, seems like the bigger win, for the time being. 
