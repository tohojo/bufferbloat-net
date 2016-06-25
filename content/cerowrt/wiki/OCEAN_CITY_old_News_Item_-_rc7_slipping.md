---
title: OCEAN CITY old News Item - rc7 slipping
date: 2012-03-17T09:20:46
lastmod: 2012-03-17T09:20:46
type: wiki
---
OCEAN CITY old News Item - rc7 slipping
=======================================

**Summary:** rc6 testing is going well, kernel.org is down and dave
needs a vacation, so rc7 is going to slip a few weeks. Details of the
rc7 plan below. \[Original News item posted 24Sep2011; moved to the Wiki
17Mar2012\]

As the kernel development process has slowed due the ongoing recovery\
from the kernel.org, bottlenecking changes to cerowrt and\
debloat-testing... and I can't offer anything but empathy to those at\
kernel.org getting things back online....

... and I just arrived in Paris to work out of the lincs.fr lab there\
for the winter, where I hope to be doing some deep analysis of the\
data collected so far, and working on the harder algorithmic and\
theoretical problems...

Now seems like the perfect time to finally take some vacation.

so (sept 30-oct 10) I will be taking some serious time off in Paris\
and Giverny to recharge my batteries, and also find a place near the\
lab to live, and get integrated with matters here...

So, I've slipped cerowrt's dates back a couple weeks. Some pruning of\
the current list is in order if we are ever to get something\
distributable.

Cerowrt-1.0-rc6 is proving stable, however during that process we've\
found a few major issues that are on the roadmap to fix in rc7. At the\
kernel level, many are trivial (yet important - see bugs 266,265)\
fixes that should automagically arrive after the Linux development\
process gets back closer to normal. We're now struggling mostly with\
issues higher on the stack (see bugs 277, 113, 268, etc), and an\
onslought of new packages and feature requests from various parties\
(274, 279) - all of which are too much, combined, to deal with, in my\
exhausted, jetlagged state.

http://www.bufferbloat.net/projects/cerowrt/roadmap

All: Please feel free to add features, bugs, and suggestions to the\
rc7 release and rc7 release plan after reviewing the RC6 release\
notes.

http://www.bufferbloat.net/projects/cerowrt/wiki/OCEAN\_CITY\_RELEASE\_NOTES

All: Also feel free to jump in and fix some of this stuff - much of it\
now is in mainline code, not openwrt or kernel code. Example: bug 224\
is so simple yet crosses so many boundries as to make my head spin -\
and it's all over a SINGLE BIT. The right answer is patches to glib\
and uclibc, or so I think. Another simple set of patches is fixing\
dscp marking under ipv6 for things like openssh.... a great mystery\
regarding TOS setting under IPv6 has been resolved in bug 249...

http://www.bufferbloat.net/issues/249

And do keep testing RC6! Downloads available at:\
http://huchra.bufferbloat.net/\~cero1/

My efforts this coming week will be in getting bloatlab \#1 up and\
fully operational. Preliminary documentaion on that lab is at:

http://www.bufferbloat.net/projects/cerowrt/wiki/BloatLab\_1

and iperf and netperf servers are enabled on jupiter and io.

I'm very happy with how far we have come with the bufferbloat effort\
in the 9 months since the inception of bufferbloat.net - in particular\
the recent lwn.net article (which will be available to non-subscribers\
soon) and the responses to it were heartwarming as to how much people\
'got' what we have been trying describe, diagnose, and fix.

And I'm really glad everyone has been so helpful, and also really glad\
to finally be planning a little time away from the bloat.
