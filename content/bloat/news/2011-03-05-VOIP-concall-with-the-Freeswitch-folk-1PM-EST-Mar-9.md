---
title: "VOIP concall with the Freeswitch folk 1PM EST Mar 9"
date: 2011-03-05T09:31:56
type: news
author: Dave Täht
aliases:
    - /news/8
---
The members of the Bufferbloat project are invited to sit in on
Freeswitch's regular VOIP conference call at 1PM Eastern Time,
Wednesday, March 9th. Please dial into:

PSTN:       USA +1-919-386-9900 or\
               +44-3300-100-295\
SIP:         sip:888@conference.freeswitch.org\
GOOGLETALK: conf+888@conference.freeswitch.org

There will also be chatter on the appropriate irc channels as we attempt
a melding of the minds. More details to follow.

About Freeswitch\[1\]
---------------------

[FreeSWITCH](http://www.freeswitch.org) is a scalable, open source,
cross-platform soft-switch that allows for consolidating various forms
of communication media. It is used primarily for telephony applications
- VoIP and traditional PSTN - but also supports video, chat, and other
forms of communication.

FreeSWITCH was created in 2006 in response to the need for an open
source, freely available telephony platform that could fill the void
left by proprietary commercial offerings. Anthony Minessale is the chief
architect and lead programmer on the FreeSWITCH project. He is joined by
two veteran developers - Brian K West and Michael Jerris. All three of
these experienced engineers spent a number of years developing for the
Asterisk PBX project before starting FreeSWITCH. 

FreeSWITCH was designed with the goals of modularity, stability, and
scalability. It is now used in thousands of servers to power VoIP
communications for business and organizations around the world, and runs
on nearly every operating system.

About the Bufferbloat project
-----------------------------

If you are not already aware of what bufferbloat is, the fastest way to
get up to speed is to peruse the slides and listen to 25 minutes of
audio before the conference call, at:

http://mirrors.bufferbloat.net/Talks/BellLabs01192011/

It would be great to have an informed audience so we can only touch
lightly on the preliminaries and then dive deeper into bufferbloat and
VOIP issues. See also Jim Gettys' blog postings\[2\], discussions on
lwn.net\[3\], and slashdot\[4\], and elsewhere\[5\], as well as two very
busy mailing lists\[6\]

In short, the bufferbloat problem is that there are really big, bloated
network buffers in many (especially new) routers, home (mostly wireless)
gateways, hosts, and ADSL/FIOS/cable modems that can dramatically affect
VOIP performance.

The bufferbloat project\[7\] is attempting to identify equipment and
software where truly bloated buffers exist, and mitigate or fix the
issues with new software algorithms and heightened awareness. Recently
we've released a debloat-testing Linux kernel\[8\] that may help in some
cases. Bufferbloat is not a Linux-specific problem, it exists in all
OSes, and may become more acute as Windows 7 gets rolled out.

\[1\] http://www.freeswitch.org/\
\[2\] http://en.wordpress.com/tag/bufferbloat/\
\[3\] http://lwn.net/Articles/429931/\
\[4\] http://linux.slashdot.org/story/11/02/26/038249/Got-Buffer-Bloat\
\[5\] http://www.bufferbloat.net/projects/bloat/news\
\[6\] https://lists.bufferbloat.net/listinfo/\
\[7\] http://www.bufferbloat.net/projects/bloat/wiki\
\[8\] http://lwn.net/Articles/429943/
