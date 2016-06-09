
---
title: Dtaht tasks
date: 2011-02-01T07:40:16
lastmod: 2011-07-09T08:34:29
---
Dave Täht's tasks
=================

1\) Reducing the unmanaged buffers on the devices I have (all
Linux-based) and observing the effects on latency and throughput. This
involves a bit of kernel hacking. As kernel hackers go, I'm a little
unusual in that usually I work on rt based kernels in the first place,
because I do audio editing and production. At the moment, I'm merely
using the 2.6.37 kernel as a base, as it's common between all my devices
and the rt patches have frozen at .33.

2\) High on my personal list is exploring the inter-relationship between
the mq qdisc and the wireless device drivers themselves. Buffering is
ok. Unmanaged buffering is not. Wireless has special problems for which
most people have been papering over with excessive buffering and
retransmit settings, especially on newer devices.

3\) Also related to that is playing with the SFB qdisc which seems to
have a lot of potential to manage flows at the gateway and laptop level.

4\) In the context of real-time, I'd like to be exploring the interaction
of HTB and device driver buffering in the context of having smaller
quantums for the kernel and device driver(s) to be making their
decisions.

5\) I'm also helping maintain and upgrade the bufferbloat website, and
keep the public conversation(s) on track, and recruiting
<link>helpers</link> which is eating far more of my time than I'd like.

[RFC Improving DSCP support in Linux]({{< relref "wiki/RFC_Improving_DSCP_support_in_Linux.md" >}})

<link>latency</link>

6\) Writing articles on describing the mis-understood portions of the IP
stack.

I can be found in the \#bufferbloat channel(s) on irc.

<link>Save the Mice</link> [Diffserv statistics]({{< relref "wiki/Diffserv_statistics.md" >}})

[Dtaht test rig]({{< relref "wiki/Dtaht_test_rig.md" >}})

[Experiment - TCP cubic vs TCP vegas]({{< relref "wiki/Experiment_-_TCP_cubic_vs_TCP_vegas.md" >}})

[Experiment - Bloated LAGN vs debloated WNDR5700]({{< relref "wiki/Experiment_-_Bloated_LAGN_vs_debloated_WNDR5700.md" >}})

<link>Improving DSCP support in Linux</link>

[Cool TCP/ip animations](http://www.kehlet.cx/articles/99.html)

-   Random Stuff that I'll catagorize when I have the time

<link>BPR3</link>

There's a rule of thumb for the upper bound in two SIGCOMM-award\
papers; I generally use the simple one from the Mathis paper.

bandwidth = (MSS / RTT) \* (C / sqrt(loss))

MSS = maximum segment size\
RTT = round trip time\
C = a constant between 0.87 and 1.31, depending on the ACK strategy\
and type of loss\
sqrt(loss) = square root of the probability of losing a packet

So, for a given connection, your expected throughput scales linearly\
with the size of your packets, and inversely with the RTT and\
sqrt(loss).

I have an unverified/untested Python implementation of the equations\
at http://www.cs.umd.edu/\~jmccann/tcp\_tput.py

I wonder how jumbo frames play into bufferbloat. When queues are in\
terms of number of packets (not bytes), jumbo frames make the problem\
even worse.

Justin

-   The Macroscopic Behavior of the TCP Congestion Avoidance Algorithm,\
    by Matthew Mathis, Jeffrey Semke, Jamshid Mahdavi, and Teunis Ott,
    CCR\
    27(3), 1997. (pdf:\
    http://ccr.sigcomm.org/archive/1997/jul97/ccr-9707-mathis.pdf)
-   Modeling TCP Throughput: A Simple Model and Its Empirical\
    Validation, by Jitendra Padhye, Victor Firoiu, Don Towsley, and Jim\
    Kurose, Proc. of ACM SIGCOMM 1998. (pdf:\
    http://conferences.sigcomm.org/sigcomm/1998/tp/paper25.pdf)

http://ieeexplore.ieee.org/iel5/11096/35442/01682953.pdf

http://www.freepatentsonline.com/6614808.html

http://systems.cs.colorado.edu/Networking/CommuNet/packet\_aggregation.html

http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.86.6126&rep=rep1&type=pdf

http://kernel.org/doc/

Subject: Re: Understanding Bandwidth-Delay Product in Mobile Ad Hoc
Networks\
X-Boundary: **\_

On 01/18/2011 11:27 AM, Dave Täht wrote:\
&gt;\
&gt; Don't know if anyone sent this one to you yet.\
&gt;\
&gt; http://cairo.cs.uiuc.edu/publications/papers/elsevier2004-bdp.pdf

http://www1.sce.umkc.edu/\~sohrabyk/papers/TcomReport.pdf

http://portal.acm.org/citation.cfm?id=1219649

[VOIP]({{< relref "wiki/VOIP.md" >}})

&gt;\
&gt; Also, PLUGFEST![]()! Sounds like a good spot to do some testing in\
&gt;\
&gt; http://www.networkworld.com/news/2011/030411-ipv6-home-routers.html

No, even better is to educate the UNH Interoperability lab, and have\
them test **everything**.

Dunno if they are competent to test 802.11 full up or not for what we\
need; but the task of educating them will make that clear.

See: http://www.iol.unh.edu/\
- Jim

-   [Network Analysis Tools]({{< relref "wiki/Network_Analysis_Tools.md" >}})

<!-- -->

-   [Bufferbloat and Freeswitch Conference Call March 9]({{< relref "wiki/Bufferbloat_and_Freeswitch_Conference_Call_March_9.md" >}})

[Enable ECN on multiple operating systems]({{< relref "wiki/Enable_ECN_on_multiple_operating_systems.md" >}})

[irc clients]({{< relref "wiki/Irc_clients.md" >}})

[BANA]({{< relref "wiki/BANA.md" >}})
