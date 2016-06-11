
---
title: "The first 34 days"
date: 2011-03-04T11:44:08
type: news
author: Dave Täht
---
The Bufferbloat project news summary, February 17 - March 3, 2011
=================================================================

I'm going to try to put out summary news like this once a month in\
the future. This is just a summary of the past two weeks. For a summary\
of the first two weeks, see [here](http://www.bufferbloat.net/news/4) .

For those of you new to bufferbloat, the fastest way to get up to speed\
is to review Jim Gettys' presentation: [Bufferbloat - Dark buffers on
the Internet](http://mirrors.bufferbloat.net/Talks/BellLabs01192011/)\
and the [audio
recording](http://mirrors.bufferbloat.net/Talks/BellLabs01192011/Bufferbloat_Talk_Edited_For_brevity.mp3)

In March, I hope we start to get some patches tested by lots more
people,\
start getting the qdisc folk to talk to the driver folk (and vice
versa)\
and continue to unify several separate lines of development. I hope
also\
we improve the wiki, and continue to recruit more people with different\
layers of perspectives and understandings of the problem. Late this
month\
a new (8 core) server will come online at isc.org for use for building\
both debloat-testing and openwrt based kernels for various devices.
More\
servers and locations will follow.

Extremely high on the list is getting more testing tools modified not
only\
to detect bufferbloat, but test the new kernel features to see how well
they\
are working.

Development
-----------

The [Debloat-testing](http://git.infradead.org/debloat-testing.git)
Linux\
kernel tree has been updated to 2.6.38-rc7-db. John Linville made an
abortive\
attempt to move it into the qdisc layer. There are other issues...

Statistics
----------

There are now 181 people registered in the [general bufferbloat email
list](https://lists.bufferbloat.net/pipermail/bloat/2011-March/thread.html)\
and 42 in [bufferbloat development
list](https://lists.bufferbloat.net/pipermail/bloat-devel/2011-March/thread.html)

41 people have registered on the [bufferbloat project web
site](http://www.bufferbloat.net/projects/bloat) .\
I seem to be the only one making edits. Is there something broken?

35 people (and one robot) regularly in the
[\#bufferbloat](irc://chat.freenode.net#bufferbloat) irc channel on
chat.freenode.net.

References to "bufferbloat" on google doubled from roughly 30,000 to
61,200 results.

(Bufferbloat is now .00053% as popular as sex)

Web hits on the presentations and site itself are not yet available.

We survived slashdot!
---------------------

The [thoroughly debloated
servers](http://www.bufferbloat.net/projects/bloat/wiki/Dogfood_Principle)
bufferbloat.net is running on survived both a\
[discussion on lwn.net](http://lwn.net/Articles/429931/) and a slo-mo
slashdotting on the\
[Got (bufferbloat)
Bloat](http://linux.slashdot.org/story/11/02/26/038249/Got-Buffer-Bloat)
thread.\
Slashdot unfortunately got the link to the [debloat-testing
tree](http://git.infradead.org/debloat-testing.git) wrong, and never
corrected it.

Blog posts & media coverage related to Bufferbloat (most recent first)
----------------------------------------------------------------------

  --------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  Richard Pitt                                                    "Usage Based Billing - it's all about **perceived** congestion":http://digital-rag.com/article.php/All-About-Perceived-Congestion-UBB
  Jim Gettys                                                      "ECN study results from MIT":http://gettys.wordpress.com/2011/02/22/caida-workshop-aims-2011-bauer-and-beverly-ecn-results/
  Jim Gettys                                                      "Benchmarking Broadband":http://gettys.wordpress.com/2011/02/17/caida-workshop/
  Brian Proffitt                                                  "Latency under Load":http://www.enterprisenetworkingplanet.com/netsp/article.php/39260760
  Richard Pitt                                                    "Bufferbloat and your ISP's problem":http://digital-rag.com/article.php/Buffer-Bloat-Packet-Loss
  "Joe Brockmeier":http://www.networkworld.com/community/zonker   "The fight against Bufferbloat":http://www.networkworld.com/community/fight-against-bufferbloat
  Jim Gettys, Dave Täht                                           "Bufferbloat and VOIP podcast":http://www.voipusersconference.org/2011/bufferbloat/
  Jim Gettys                                                      "A call for help with Bufferbloat animations":http://gettys.wordpress.com/2011/02/04/animation-to-show-bufferbloat-badly-needed/
  --------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

While bufferbloat is not a Linux-specific problem, we're the first
community out the gate with\
solutions and patches. We are actively looking for iphone, ipad, and
android users to test\
some basic assumptions regarding <link>ECN</link>.\
(if you are on an iphone, and having trouble\
accessing this site or [this
mp3](http://mirrors.bufferbloat.net/Talks/BellLabs01192011/Bufferbloat_Talk_Edited_For_brevity.mp3)
, **please** let us know!)

And there are tons of <link>Papers|research papers</link>, tools and
<link>Linux Tips</link> linked to off of our <link>wiki</link> that need
sorting out.

Principal threads of conversation so far this month:
----------------------------------------------------

[Getting more
organized](https://lists.bufferbloat.net/pipermail/bloat/2011-February/000154.html)\
GSO:
https://lists.bufferbloat.net/pipermail/bloat-devel/2011-March/000077.html\
[Usage based
billing](https://lists.bufferbloat.net/pipermail/bloat/2011-March/000178.html)

... (Still ongoing from last month)

[Shifting the
Market](https://lists.bufferbloat.net/pipermail/bloat/2011-February/000066.html)
- How to get the word out? (\#33)\
[SFB](https://lists.bufferbloat.net/pipermail/bloat/2011-February/000026.html)
- Discussion of the features of Stochastic fair blue queuing, with
[Juliusz Chroboczek](http://www.pps.jussieu.fr/~jch/) , the author of
the [SFB patch](http://www.pps.jussieu.fr/~jch/software/sfb/) for the
Linux kernel\
[The dangers of
AQM](https://lists.bufferbloat.net/pipermail/bloat/2011-February/000108.html)
- a cautionary note about Active Queue Management, by [Kathie
Nichols](http://www.pollere.net/about.html) and [Van
Jacobson](http://en.wikipedia.org/wiki/Van_Jacobson)\
[Bufferbloat and
You](https://lists.bufferbloat.net/pipermail/bloat/2011-February/000050.html)
- a draft contributed by [Eric
Raymond](http://en.wikipedia.org/wiki/Eric_Raymond), Much discussion as
to good analogies for how the Internet really works ensued\
[About LEDBAT, µTP and
BitTorrent](https://lists.bufferbloat.net/pipermail/bloat/2011-February/000025.html)
- an exploration of the issues and advantages of bittorrent\
[TCP Vegas vs
Cubic](https://lists.bufferbloat.net/pipermail/bloat/2011-February/000016.html)
- Some <link>Experiment\_-\_TCP\_cubic\_vs\_TCP\_vegas|puzzling data
about TCP vegas</link> with current hardware\
[The wireless problem in a
nutshell](https://lists.bufferbloat.net/pipermail/bloat/2011-February/000068.html)
The unique problems 802.11 introduces for TCP/ip (related: [Wireless
multiqueue
behavior](https://lists.bufferbloat.net/pipermail/bloat/2011-February/000118.html)
)

Progress on the wiki and infrastructure
---------------------------------------

The wiki needs some serious love. Help merely on defining some terms
would be good.
