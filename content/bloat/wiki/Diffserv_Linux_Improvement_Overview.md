
---
title: Diffserv Linux Improvement Overview
date: 2011-06-19T15:22:26
lastmod: 2011-09-02T12:04:22
type: wiki
---
Diffserv Linux Improvement Overview
-----------------------------------

In my efforts to improve QoS possibilities under Linux by fully
implementing [RFC4594](http://tools.ietf.org/html/rfc4594) I've come to
understand why it hasn't been tried.

(See git repo at https://github.com/dtaht/Diffserv for the test
implementation which attempts to update RFC4594 for modern conditions in
the home and business. The scripts therein will clearly show why I'm
suggesting some of these new iptables (and/or tc) matches and targets.)

Adequate DSCP classification rules can number in the hundreds using
straightforward existing iptables methods, or thousands with existing tc
methods. Where iptables is like programming in symbolic assembler, tc is
like coding in machine language.

In early testing of an iptables version, my first attempt cut the
performance of a given router from \~140Mb/sec to 42Mb/sec.

And yet: it seems very possible to make DSCP classification highly
performant as the 6 bit value therein maps conveniently into 64 bit
bitmaps.

So many problems can be solved by some new iptables or tc matches and
targets.

So here are my thoughts. Perhaps code to do some of this sort of stuff
already exists out of tree?

RFC4594 rigorously attempted to avoid making any given traffic class
predominant over another - EF traffic is suggested to be limited to 30%
of available bandwidth, for example - the goal was to produce fairness
between flows, as is mine. I'd like to be able to listen to internet
radio, while others in my family are uploading to facebook, watching
movies from netflix, and making phone calls and playing games.

In reading the following discussion it is very useful to have the
relevant rfc, and the manual pages for iptables and ip6tables and tc
handy. Some familiarity with all this concepts is required as well as a
mental model as to how the Linux networking stack actually functions.
For a large diagram of the below chart, see
http://l7-filter.sourceforge.net/PacketFlow.png

![](http://l7-filter.sourceforge.net/PacketFlow.png)

You'll note it elides the complexities of the various tc qdiscs,
filters, and policers, and the complexities of the networking device
drivers themselves. A flow diagram of each would also take pages to
describe!

Anyway, it is interesting and useful to try classifying your own traffic
using the diffserv\_dbg script as provided in the Diffserv repository. I
would appreciate [a look at your results](Diffserv_statistics.md)
(particularly the ANT packets overall, and icmpv6 packets) via

    iptables -v -t mangle -L
    ip6tables -v -t mangle -L 
    iptables -t filter -L
    ip6tables -t filter -L

in order to see why, in part, I feel extensive classification is more
necessary today than ever before.

The largest problem with the design as it stands is that the initial
classification rules should probably take place within the tc subsystem.
The problem there is that tc is even more primitive than iptables. A
subsequent version of this proposal will attempt to use tc to solve many
of these problems.
