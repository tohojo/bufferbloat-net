
---
title: "6 weeks of backlogged news"
date: 2011-04-17T19:53:18
type: news
author: Dave Täht
aliases:
    - /news/12
---
I'd intended to write up summaries of bufferbloat related activity once
a month, but am running a bit behind. Both JG and I have been travelling
heavily.

There's been a lot going on under the covers!

Probably the biggest news is that we are working with Georgia Tech on
their bismark project.\[1\] They are out to diagnoise the Internet and
we are out to fix it. The two goals seemed compatible. In particular: we
are trying to de-"heisenbug" the test routers so they can accurately
test the upstream services.

We've also taken the wraps off the "uberwrt" project\[2\], which is an
attempt to get the debloating work TESTED in realistic situations at the
edge and also into openwrt. (Some work from this also flows into
bismark)

I was going to write formal joint press releases on these but have been
too busy traveling, talking and hacking. (if anyone wants to step up to
handle PR?)

Although traffic on the bloat mailing list has been slow of late, the
bismark-devel list has been hopping. Feel free to join bismark/uberwrt
projects and/or the mailing list\[3\], especially if you are interested
in embedded hardware.

Moving on to other topics...

Based on the early difficulties in getting debloat-testing to be a
useful base for the eBDP and A\* algorithms, we started looking around
for ONE driver to work with and have settled on ath9k hardware (for now)
as a base for routers and wireless cards. \[10\] We need to do a little
testing of the laptop cards, but things are looking good. the WNDR3700v2
is AWESOME, actually. 16MB of flash. LUXURY.

Other Patches:

Dan Siemon's pfifo\_fast fix for ECN has been backported into 2.6.37.X
for openwrt's git head as of Saturday. It's also now part of 2.6.39 and
2.6.38 stable.

SFB is in mainline Linux 2.6.39-RCX and woefully undertested in its
current incarnation.

Felix Feitkeu has some patches more fully instrumenting the ath9k driver
(when mildly more complete, these should get slammed into
debloat-testing as well) \[4\]

Dan Siemon has improved both his TC shaper test scripts and ping-exp
\[5\]

Media: There were a couple articles on bufferbloat that went by this
month, I think they were all covered on this list...

There are 236 members of the bloat list now.

Infrastructure:

We are moving a ton of work to a new build server and also moving the
lists machine to that. Regrettably as I write, "huchra" is down due to
finger-foo. It should be back up again Monday.

Multiple other servers in other locations are in the queue. I hope to
get that sorted out with isc while I am in California.

Upcoming Travel:

JG will be in California April 25-30. I will also be in California April
25-30 (in at least one of the same places as JG), and am available for
additional talks/coding/consulting/etc along the western seaboard in
early May if anyone wants me and can cover my expenses. (Sort of
scheduled: Byte and Atheros U) I'll also be visiting Seattle at some
point in May, too.

Travel last month:

JG spent spent several weeks in Europe, first attending the Wireless
BattleMesh conference\[6\], then the IETF, giving a shorter version of
his bufferbloat talk\[7\].

I spent a week in florida gathering strength for my world tour. Then I
spent a week with Georgia Tech helping get their Bismark project off the
ground and hammering out workflow issues.

I was tickled pink when I gave an introductory talk on bufferbloat to a
class there, only to discover when Q&A rolled around that everyone
participating was **already** up to speed on bufferbloat and queueing
disciplines, and peppered me with questions on SFB, RED, eBDP and other
algorithms we are playing with. 3 months ago I would have been met with
blank looks, now it's a struggle to keep up!

I then spent a week with esr getting one of the first near-complete
builds of the wndr3700 working well, working on gpsd (wanted accurate
time on openwrt) and rsnapshot and split dns and a host of
semi-bufferbloat.net-and-uberwrt issues... And we also got a revised
version of the intro to bufferbloat document up on the wiki \[8\].

I'm very happy to see thyrsus.com go ipv6 enabled.

The bufferbloat wiki is still in dire need of love, see the Todo list
for more details \[9\] -

Conclusion:

And that's all the news I can remember this late Sunday evening. It's my
hope that SFB will make it into bismark/uberwrt this week so we can test
SFB a little more while it is still a RC in 2.6.39. I'd VERY MUCH like
to make sure SFB works when it is released to millions of users
worldwide. That will be in 4 weeks or so... I'm feeling a little
schedule pressure here... See dan siemon's scripts... \[5\]

\[1\] http://www.bufferbloat.net/projects/bismark/wiki Georgia Tech's
project\
\[2\] http://www.bufferbloat.net/projects/uberwrt/wiki\
\[3\] https://lists.bufferbloat.net/listinfo/ (bismark, bismark-devel)\
\[4\]
http://www.bufferbloat.net/projects/uberwrt/wiki/Experimental\_patches\
\[5\] http://git.coverfire.com/ PLEASE PLAY WITH TC, SFB, and
PING-EXP![]()![]()\
The bandwidth you save may be your own.\
\[6\] http://battlemesh.org/ has summaries and videos from the
battlemesh\
\[7\] http://mirrors.bufferbloat.net/Talks/PragueIETF/\
\[8\] The original of the bufferbloat introductory piece was extensively
discussed on this mailing list. This versions incorporates most of those
changes. If you don't like this version... It's a wiki document now!
Please feel free to fix, extend, and add links!
http://www.bufferbloat.net/projects/bloat/wiki/Introduction\
\[9\] LOTS of writing left
http://www.bufferbloat.net/projects/bloat/wiki/ToDo

\[10\] After evaluating multiple routers,
http://www.bufferbloat.net/projects/uberwrt/wiki/Hardware\_evaluation

the http://www.bufferbloat.net/projects/bismark/wiki/Wndr3700v2\
seemed like the best choice

**\_\
Bloat-announce mailing list\
Bloat-announce@lists.bufferbloat.net\
https://lists.bufferbloat.net/listinfo/bloat-announce
