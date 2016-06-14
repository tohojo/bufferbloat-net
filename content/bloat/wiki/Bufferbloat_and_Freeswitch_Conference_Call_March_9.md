
---
title: Bufferbloat and Freeswitch Conference Call March 9
date: 2011-03-10T08:03:32
lastmod: 2011-03-10T08:07:29
type: wiki
---
Bufferbloat and Freeswitch Conference Call SUMMARY 1PM EST March 9
==================================================================

[Freeswitch](http://www.freeswitch.org) is one of the top two open
source VOIP telephony applications, widely deployed throughout the world
as a conference bridge, PBX, and IVR host.

The conference call was an attempt to have a meeting of the minds
between the bufferbloat project's work ongoing and the voice
applications deployed in the field. The call was recorded. If you would
like to participate post-hoc the mp3 is available at:

http://wiki.freeswitch.org/files/conf\_call\_2011-03-09.mp3

If anyone pulls a meaningful detail out of the recording (I know I
missed a few things) please update this wiki page.

Attendees
---------

Bufferbloat-ers: Jim Gettys, Dave Täht, Dave Hart\
Freeswitch-ers: Michael Collins, Anthony Minessale (principal freeswitch
developers) and 28-33 other participants listening in.

This conference call usually runs 30 minutes. It ran for 2 hours as we
discussed all aspects of VOIP as it relates to bufferbloat. (And still
barely scratched the surface)

Discussion
----------

Beforehand, in addition to tweeting the time and sip/skype/gtalk
[methods of connecting to the conference
call](http://www.bufferbloat.net/news/8), I (Dave Täht) posted [How I
came to fear the bloat and join the
project](http://the-edge.blogspot.com/2011/03/beating-my-bloat.html) on
[one of my blogs](http://the-edge.blogspot.com/) - (basically this
pieces remixes several JG's blog posts from Nov-Jan 10)

Since JG was in poor voice I tried out my "Kleinrock has no buffers for
TCP/IP, and buffers = distance and we're going over the moon" rant
(needs polish!), which JG then filled in with some more background from
his [Dark Buffers on the
Internet](http://mirrors.bufferbloat.net/Talks/BellLabs01192011/)
presentation.

It's pretty obvious that we need to have an elevator pitch about what
bufferbloat.net is about. I ended up talking way too much about bug
\[\#33\].

The comcast paper that established [32 as an upper bound for unmanaged
buffering on some home gateways]() in many circumstances was
discussed. Both JG and I stressed it was the formula, not the number,
that was important.

We talked about the [Mesh
Potato](http://www.villagetelco.org/about/mesh-potato/) , the
[IP04](http://www.rowetel.com/blog/?page_id=440) , and [David Rowe's
excellent blog on low power/cost
applications](http://www.rowetel.com/blog/)

The [new ultra-low delay CELT codec](http://www.celt-codec.org/) was
raved about... As codecs go, it really rocks.

I had a chance to talk a little bit about my (now on-hold)
[Wisp6](http://nex-6.taht.net/wiki/wisp6/) project, including showing
off the sites and beam widths on the [Bandwidth for Barrios Google Earth
Map](http://www.teklibre.com/~d/b4barrios10.kml) (zoom in below San Juan
Del Sur, Nicaragua), the
[view](http://www.teklibre.com/~d/casayanqui/masterbedoomviewbetter.jpg)
- the (lack of) legal and regulatory environment, the
[partner](http://www.condor.com.ni) I worked with, and of course, [the
surfing](http://www.nicaraguasurfreport.com/reportlist.php?id_secc=25&amp;x_date=2011-03-05&amp;z_date=%3D%2C%27%2C%27)

We talked a bit about the cellular service lacking [Pityhaya
festival](http://www.earthshippitayafestival.com/) could perhaps
leverage the ongoing [open source BTS/GSM
project](http://openbts.sourceforge.net/) , and also talked about how we
can get the larger BTS/GSM companies to pay attention to bufferbloat.

Somewhere in there we talked about all the features folded into the new
kernel tree,
[debloat-testing](https://lists.bufferbloat.net/pipermail/bloat-devel/2011-February/000061.html)
at present.

There was a really good question asked about how "eBDP" vs [RED in a
different
light](http://mirrors.bufferbloat.net/RelevantPapers/Red_in_a_different_light.pdf)
were supposed to interact. We talked about how RED was inadaquate and a
bit about other AQMs like SFB could work in the presence of VOIP.

It turned out that since freeswitch VOIP servers use RTP for voice and
TCP for command and control functions, that several members of
freeswitch were already using [TCP
Vegas](http://en.wikipedia.org/wiki/TCP_Vegas) because it was latency
sensitive.

The [Freeswitch Ethernet tuning
page](http://wiki.freeswitch.org/wiki/Performance_testing_and_configurations#Ethernet_tuning_in_Linux)
had recommendations that were grossly incorrect for nearly any
circumstance, which we corrected during the call.

We discussed the old wondershaper, and the lack of a good universal
shaper in general and the lack of one that handles dual-stack IPv6/4
traffic in particular. Gained another volunteer to look into the shaping
problem ([Frank Carmickle](http://www.carmickle.com) )

On my ongoing quest to find a ipv6 enabled VOIP conference server on the
East coast, we gained two potential volunteers as well as a potential
site in Europe.

And then the call turned to the effects of virtualization on timing
constraints and buffering. It sounds as though - with a little work -
several virtual server technologies on both Linux and Windows can be
made to "do the right thing" when it comes to timing constraints. Many
of the Freeswitch developers are running on very old kernels (2.6.28,
2.6.18) in virtual environments.

And then the conversation gradually petered out...
