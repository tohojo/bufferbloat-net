
---
title: "Bufferbloat.net - the first 16 days"
date: 2011-02-12T11:42:02
type: news
author: Dave Täht
aliases:
    - /news/4
---
A summary of goings on at Bufferbloat.net since the launch
==========================================================

Jim Gettys' [presentation on
Bufferbloat](http://mirrors.bufferbloat.net/Talks/BellLabs01192011/) and
the [audio
recording](http://mirrors.bufferbloat.net/Talks/BellLabs01192011/murray_hill01192011_Bufferbloat_Talk_Edited_For_brevity.mp3)
got a LOT of hits (collating the data will take some time, sorry)\
83 people joined the
[bloat](https://lists.bufferbloat.net/listinfo/bloat) mailing list\
19 people joined the
[bloat-devel](https://lists.bufferbloat.net/listinfo/bloat-devel)
mailing list\
24 registrations on the [bufferbloat project web
site](http://www.bufferbloat.net/projects/bloat)\
8 people regularly in the
[\#bufferbloat](irc://chat.freenode.net#bufferbloat) irc channel on
chat.freenode.net

I'm really delighted to see everyone so concerned about Bufferbloat and
so willing to help out!

In the next 15 days I hope we start to get some patches out the door,
and unify several separate lines of development, improve the wiki, and
continue to recruit to more people with perspectives and understandings
of the problem.

Principal threads of conversation so far this month:
----------------------------------------------------

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

Blog posts & media coverage related to Bufferbloat
--------------------------------------------------

  --------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------
  Richard Pitt                                                    "Bufferbloat and your ISP's problem":http://digital-rag.com/article.php/Buffer-Bloat-Packet-Loss
  "Joe Brockmeier":http://www.networkworld.com/community/zonker   "The fight against Bufferbloat":http://www.networkworld.com/community/fight-against-bufferbloat
  Jim Gettys, Dave Täht                                           "Bufferbloat and VOIP podcast":http://www.voipusersconference.org/2011/bufferbloat/
  Jim Gettys                                                      "A call for help with Bufferbloat animations":http://gettys.wordpress.com/2011/02/04/animation-to-show-bufferbloat-badly-needed/
  --------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------

Progress on the wiki and infrastructure
---------------------------------------

[John Linville](http://www.tuxdriver.com/index.html) signed up as a
source code maintainer - [Richard
Scheffenegger](http://tools.ietf.org/html/draft-scheffenegger-tcpm-sack-loss-recovery-00)
put up a [simple NS2 animation of
bufferbloat.](http://www.bufferbloat.net/attachments/15/nam00000.avi) -
[Richard Pitt](http://digital-rag.com/) started a <link>glossary</link>
- [Don Marti](http://zgp.org/~dmarti/) contributed some <link>Linux
Tips</link> - Eric Raymond & Dave Täht are working on an introduction
and site overview - links to various important <link>papers</link> have
been collected - and numerous bits and pieces of the overall picture
have been filled in from Jim Gettys' extensive blog postings. More
definitions, contributions, and organization are direly needed, but the
overall picture is taking shape. The
[index](http://www.bufferbloat.net/projects/bloat/wiki/index) has
various bits of good info in various states of completion, and there's
also an <link>outline</link> of some of what remains to be done.
