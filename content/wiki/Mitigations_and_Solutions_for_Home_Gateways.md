
---
title: Mitigations and Solutions for Home Gateways
date: 2011-02-02T17:47:22
lastmod: 2011-02-02T17:47:22
---
Mitigations and Solutions for Home Gateways
===========================================

Mitigations and Solutions of Bufferbloat in Home Routers and Operating
Systems\
By gettys

As discussed several days ago we can mitigate (but not solve) broadband
bufferbloat to a decent, if not ideal, degree by using bandwidth shaping
facilities found in many recent home routers. Unfortunately, life is
more complicated and home routers themselves are often typically at
fault (if you find a recently designed home router that works right, it
may want to be enshrined in a museum where its DNA and evolution
analyzed, and its implementors both admired for their accomplishment and
despised, for not telling us about what they discovered. Complete robust
solutions, unfortunately, will be difficult in the short term (wireless
makes it an “interesting” problem) for reasons I’ll get to in this and
future posts.

Confounding the situation further, your computer’s/ smartphone/
netbook’s/ tablet’s operating system may also be suffering from
bufferbloat, and the its severity may/almost certainly does depend upon
the hardware. Your mileage will vary.

You may or may not have enough access to the devices to even manipulate
the bufferbloat parameters. Locked down systems come back to bite you.
But again, you can probably make the situation much better for you
personally, if you at a minimum understand what is causing your pain,
and are willing to experiment.\
Conclusions

Since any number you pick for buffering is guaranteed to be wrong for
many use cases we care about, the general solution will await operating
systems implementers revisiting buffering strategies to deal with the
realities of the huge dynamic range of today’s networks, but we can
mitigate the problem (almost) immediately by tuning without waiting for
nirvana to arrive.

As an end user, you may suffer in your home router or your computer
anytime when the bandwidth (“goodput”) you get over a wireless hop is
less than the provisioned and actually provided broadband bandwidth.
This is why I immediately saw problems on the Verizon FIOS wireless
routers (the traces show both problems on the wired and wireless side;
but the wireless side is much worse). On that typically symmetric
service at my in-law’s FIOS 20/20 service, 802.11g is usually running
more slowly than the broadband connection. I also see bufferbloat
regularly at home on my router using my Comcast service, which I
recently changed to 50/10 service; there are parts of my house where it
is now easy to get enough insufficient bandwidth over wireless.
Bufferbloat is nothing if not elusive. It’s been like hunting the will
o’ the wisp on wireless, until I had a firm mental grasp on what was
happening.

Remember: you see bufferbloat only on the buffers adjacent to the
bottleneck in the path you are using. Buffers elsewhere in the path you
are probing remain invisible, unless and until they become the
bottleneck hop.\
Mitigating the inbound home router wireless bufferbloat problem

Whenever the bandwidth from your ISP exceeds that of your wireless
“goodput”, you’ll likely see bufferbloat in your home router (since the
bottleneck is the wireless hop between you and the router). Full
solutions to the problem are beyond the scope of today’s posting (coming
soon), and will require some research, though ways forward exist. In
short, complete solutions will require active queue management (e.g. RED
or similar algorithms), since the mitigation strategy of bandwidth
shaping to “hide” the buffer we showed in a previous post will not lend
itself well to the highly variable bandwidth & goodput of wireless.
Outbound, it is very likely in your operating system where the bloat
will occur (since your router is generally connected to the broadband
gear either internally (as in the FIOS router I experimented with) or
via a 100Mbps or 1Gps ethernet. You’ll most likely experience this, as
one of the replies to this posting points out, when uploading large
files, doing backups, or similar operations. I only realized OS
bufferbloat occurs after I started investigating home routers and did
not get the results I expected immediately. With some disbelief, I got
confirmation with the simple experiments I reported on.

If you can “log in” to a shell prompt on your wireless router (many are
running Linux, and a few have known ways to break into them), or are
willing to install open source firmware on your router, you can go
further, by mitigating the excessive buffering in the ways explained
below for Linux. Remember, that this only affects the down stream
direction (home router to your laptop). Note that the only one of these
open source projects I have found that has close to turnkey
classification and mitigation of broadband bufferbloat is Gargolye. Paul
Bixel has worked hard on mitigating broadband bufferbloat, but has not
attempted wireless bufferbloat mitigation. As noted in a previous post,
many mid to high end home routers have enough capability to mitigate
broadband bufferbloat.

OS Bufferbloat Mitigation

As explained in fun with your switch, fun with wireless, and the
criminal mastermind postings, and in future blog postings, we have bad
behavior all over the Internet, though I focused on the home environment
in most of the postings so far. In all of the common operating systems,
there is at least one, if not two places (and maybe more undiscovered)
where bloat has been demonstrated. Please go find and fix them. All OS’s
therefore suffer to some extent or another.

Your most immediate mitigation may be to literally move either your
laptop or your home router to where the bandwidth equation is different,
shifting bufferbloat to a (possibly) less painful point. But there are
also potentially some quick mitigations you can perform on your laptop,
and as some others in replies to previous postings have demonstrated,
that are more general. The first order mitigation is to set your
buffering in your operating system to something reasonable, as explained
below (details of the Linux commands can be found in “fun with your
switch” and “fun with wireless“.\
Linux

I’ll discuss Linux first, as in my testing, it has problems that may
affect you even if you don’t run Linux, as Linux is often used in home
routers. But then again, as I use Linux for everything, there may be
more buffers on other operating systems that I have not run into; my
testing on Mac and Windows has been very small relative to Linux. We all
live in a glass house; don’t go throwing stones. Be polite. Demonstrate
real problems. But be insistent, for the health of the internet.

Note the total amount of buffering causes TCP and other congestion
avoiding protocols indigestion: in Linux’s case, it is both the device
driver rings (which I believe I see in other operating systems) and the
“transmit queue” buffering. I gather some of the BSD systems may have
unlimited device driver buffering. Some hardware may also be doing
further buffering below the register level in smart devices (I susped
the Marvell wireless device we used on OLPC might, for example).

As discussed in fun with your switch, I detected two different sources
of excessive buffering in Linux, both typically resulting from device
drivers (therefore shared in common with other operating systems).
Device drivers hint to the operating system a “transmit queue length”,
which is controllable on Linux by use of the “txqueuelen” parameter
settable using the “ifconfig” command. By default, many/most modern
ethernet and wireless NIC’s are telling Linux to be willing to buffer up
to 1000 packets. In my experiments on (most) of my hardware, since the
ethernet and wireless rings are both at a minimum quite large, I could
set txqueuelen to zero without causing any immediate problems.

But note that if you set buffering to zero in both device drivers (and
the transmit queue), if there is no other buffering you don’t happen to
know about, your system will just stop transmitting entirely; so some
care is in order. This depends on the exact details of the hardware.
Buffering is necessary; just not the huge amounts currently common,
particularly at these speeds and low latencies.

Also note that many device drivers (e.g. the Intel IWL wireless driver)
do not support the controls to set the ring buffer sizes, and at least
one device I played with it seemed to have no effect whatsoever
(implying buffering present, but no control over the size of those
buffers).

A possible reason for the transmit queue (others with first hand
knowledge of the history, please chime in), is that on some old
hardware, e.g.old serial devices being used with modems, had essentially
no buffering, and you might experience excessive packet loss on those
devices. It may have also been really necessary for performance before
Linux’s socket buffer management became more sophisticated and started
to adjusting its socket buffer sizes based on the observed RTT (note
that the lower level bufferbloat may be inducing socket bufferbloat and
application latency as well, though I have no data to confirm this
hypothesis). At some point, the default value for txqueuelen was raised
to 1000; I don’t know the history or discussion that may have taken
place. There are also queues in the operating system required for
traffic classification; I haven’t had time to figure out if that is
where Linux implementss its classification algorithms or not; some
hardware also supports multiple queues for that purpose. Note this means
that many Linux based devices and home routers may have inherited
differing settings. Extreme bufferbloat is present on a number of the
common commercial home routers I have played with using modern hardware,
and the open source routers I’ve played with as well.

So even though the “right” solution is proper queue management on you
can tune the txqueuelen and (possibly) the NIC device driver rings to
more reasonable sizes, rather than the current defaults, which are
typically set for server class systems on recent hardware.

Once tuned, Linux’s latency (and the router’s latency) can be really
nice even under high load (even if I’ve not tried hard to get to the
theoretical minimums). But un-tuned, I can get many second latency out
of both Linux home routers and my laptop, just by heading to some part
of my house where my wireless signal strength is low (I have several
chimneys that makes this trivial). By walking around or obstructing your
wireless router, you should be easily able to reproduce bufferbloat in
either your router or in your laptop, depending on which direction you
saturate.

With an open source router on appropriate hardware and a client running
Linux, you can make bufferbloat very much lower in your home
environment, even when bufferbloat would otherwise cause your network to
become unusable. Nathaniel Smith in a reply to “Fun with Wireless” shows
what can be done when you both set the txqueuelen and change the driver
(in his case, a one line patch!)

Mac OSX

I’ve experimented on relatively recent Apple hardware: on Ethernet
showed what appears to be device driver ring bufferbloat, roughly
comparable to Linux. On my simple test on ethernet on a 100Mbps switch,
I observed 11ms latency, roughly, slightly more than Linux which was 8ms
on similar vintage hardware in the same comparable test. On Linux, the
transmit ring is set to 256, by default, and allowed me to set it as
small as 64. So I hypothesize a similar size buffer in it’s ethernet
driver (and possibly a small buffer in the OS above the driver). As I’m
not a Mac expert, I can’t tell you as I could on Linux how to reduce the
transmit ring size.

I have not tried to pry my son’s Mac out of his hands for Mac wireless
experiments: perhaps you would like to do so with your Mac, or I may get
around to the wireless experiment over the holidays. If you do, make
sure you arrange the bottleneck to be in the right place (the lowest
bandwidth bottleneck needs to be between your laptop and your test
system).\
Microsoft Windows

Experimenting with Microsoft Windows several weeks ago was a really
interesting experience. Plugged into a 100Mbps switch, there was no
bufferbloat in the operating system (both Windows XP and Windows 7) on
recent hardware. But neither Windows saturate a 100Mbps switch (you
expect to see about 93Mbps on that hardware, due to TCP and IP header
overhead). As soon as we set the NIC to run at 10Mbps, the expected
bufferbloat behavior occurred. Since in my tests, the medium no longer
is the bottleneck, it shifts to somewhere else in the path (in my test,
there was no bottleneck).

Here’s what I think is going on and I believe what happened.

With some googling, I discovered on Microsoft’s web site that Microsoft
has bandwidth shaped their TCP implementation to not run at full speed
by default, but to run probably just below what a 100Mbps network (I
observed mid 80 megabit). You have to go tune registry parameters to get
full performance on Microsoft Windows TCP implementation. There is an
explanation on their web site that this was to ensure that multimedia
applications not destroy the interactive performance of the system. I
think there is a grain (or block) of truth to this explanation: as soon
as you insert big buffers into the network, you’ll start to see bad
latency whether using TCP, UDP or other protocols, and one of the first
places you’ll notice is the UI interaction between users of a media
player and the media server (I’m an old UI guy; trust me when I say that
you start “feeling” latency at even 20ms). Any time they ran Windows on
hardware with big buffers, they had problems; certainly hardware has
supported much higher transmit buffers than makes any sense for most
user’s office or home environments for quite a few years. I suspect
Microsoft observed the bufferbloat problem and, as a simple mitigation
strategy was available to them, took it.

Microsoft does not have control of many/most of the drivers their
customers expect Windows to run well on (not true for Mac and Linux),
however. So I suspect that Microsoft and (some of their customers) have
a real headache on their hands, only soluble by updates to a large
number of drivers by many vendors.

On the other hand, on 100Mbps ethernet, still the most common bandwidth
ethernet, both Windows XP and Windows 7 ”just worked” as you might hope
with low latency (of order 1ms even while loaded). And Windows XP is
less likely to induce bloated buffers in broadband, though as bittorrent
showed, it still can, and as I’ll explain in details shortly, recent
changes in both web browsers and certain web servers can encourage XP to
fill buffers. I have not experimented with wireless. Please do so and
report back.

Alternate explanations and/or confirmations of this hypothesis are
welcome.

I do not happen to know the mechanisms, if any, to control driver
buffering size on Microsoft Windows, though it may be present in driver
dialog boxes somewhere.\
Why in the world does the hardware now have so much buffering, anyway?

On my Intel Ethernet NIC, the Linux driver’s ring buffer size is 256 by
default: but the hardware goes up to 4096 in size. That’s amazingly
huge. I’ve seen similar sizes on other vendor’s NIC’s as well. I
wondered why. I like the explanation that Ted T’so gave me when I talked
to him about bufferbloat a month ago: it stems from experience he has
when he was working for the Linux Foundation on real time. I think Ted
is likely right.

It can’t be for interrupt mitigation; most of your benefit is in the
first few packets; similarly for segmentation and reassembly. Even doing
a little transmit buffering can get you into a lot of trouble on
wireless, as I’ll show in a future post. I suppose that interrupt
latency could also be a problem on loaded systems, though this seems
extreme.

Ted’s theory is this is a result of the x86 processor’s SMM mode. To
quote Wikipedia: “System Management Mode (SMM) is an operating mode in
which all normal execution (including the operating system) is
suspended, and special separate software (usually firmware or a
hardware-assisted debugger) is executed in high-privilege mode.” Ted
noted there are motherboards/systems out there which go catatonic for of
order one or a few milliseconds at a time; yes, your N processor chip
motherboard consisting of C cores each may crowbar to a single thread on
a single processor for that length of time. The BIOS is ensuring your
CPU cores don’t over heat (you might think there should be a way to do
this at lower priority for things less time urgent, mighten you?) and
important (but not necessarily urgent) tasks. To paper over latencies
and hiccups of that length of time at 1 gigabit you indeed need hundreds
or conceivably small number of thousands of ring entries. And that’s the
size we see in current hardware.

Unless someone has a better theory, I like Ted’s.\
The General Operating System Problem

We now have commodity “smart” network devices, that may do lots of
features for us, to make the network “go fast” (forgetting that for many
people, operations/second and latency trumps bits per second and
throughput hands down; performance has multiple metrics of import, not
just one). For example, the devices may compute the TCP checksums,
segment the data, and so on; and similarly on the receive side of the
stack. To go fast, we may also be wanting to (and needing to) mitigate
interrupts, so the OS doesn’t necessarily get involved with every packet
transfer in each direction, on server systems (but often not on edge
systems at all). And, as opposed to a decade ago, we now have widespread
deployment of networking technologies that span one or more orders of
magnitude of performance, while still only admitting to a “one size fits
all” tuning.

Here’s the rub: these same smart device designs are often/usually being
put into commodity hardware a generation or two later, and the same
device drivers are being used, set up for their use on high end servers.
But the operating environment that hardware is now in is in your laptop,
your handheld device or your router, running at low bandwidth, rather
than a big piece of iron in a data center, hooked up to a network
running at maximum speed. Rather, it is being used in devices that are
being used at a small fraction of their theoretical performance
capability. For example, my gigabit ethernet NIC much more often than
not is plugged into a 100megabit switch, with the results I noted. And,
of course, I’m seldom going anything like the speed of a server on my
laptop: at most, I might be copying files to a disk someplace, and going
of order 100Mbps.

Even more of a problem is wireless: not only is the bit rate of the
network not a 100Mbps (for 802.11N), or 20Mbps (for 802.11g), but the
bit rate may drop as low as 1 megabit/second. Remember also that those
networks are shared media. If you have a loaded wireless network, the
buffering of the other nodes also comes into play; you may only get 1/10
(or less) of the available bandwidth at whatever rate that wireless
network is operating at (and 802.11 likes to drop its speed to maximize
distance at the drop of a hat). I’ll discuss what happened to OLPC in a
future post, though we also had other problems in our mesh network. So
the effective “goodput” on wireless may easily vary by factors of 100 or
more on wireless, presenting even more of a challenge than for ethernet,
where typically we face a switched network and a factor of 10 in its
performance.

In general, I believe that hardware transmit buffer sizes should be kept
as small as possible. ”As possible”, will depend strongly upon the
network media and circumstances. One of the mistakes here, I suspect, is
that the operating system driver implementers, not understanding that
transmit and receive are actually quite different situations, set the
transmit and receive buffering to the same amount. After all, I’m never
going to lose a packet I haven’t transmitted yet; it’s only receive I
could have a problem on. And as I showed previously, some packet drop
(or use of ECN) is necessary when congested for the proper functioning
of Internet protocols, and indeed, for the health of the Internet
overall. And this is indeed be a form of congestion. Ideally, we should
always mark packets with ECN whenever/wherever congestion occurs, no
matter where the excessive queues are forming.

And since the network delays are anywhere from almost zero to several
hundred milliseconds (for planetary paths), the delay/bandwidth product
is also very large, along with the workload of the systems. There is no
single right answer possible for buffering: our operating systems need
to become much more intelligent about handling buffering in general.

I certainly do not pretend to have a clue as to the right way to solve
this buffer management problem in multiple operating systems; but it
seems like a tractable problem. That will be fun for the OS and
networking subsystem implementers to figure out, and help keep them
employed.

The general challenge for operating systems is we want a system which
both can run like a bandit in the data center, and also work well in the
edge devices. I believe it possible for us to “have it both ways”, and
to “have our cake and eat it too”. But it will take work and research to
get there. In the short term, we can tune for different situations to
mitigate the problem.\
Coming Installments

\* After action report of 802.11 network meltdown at OLPC\
\* RED in a different light\
\* corporate and ISP networks\
\* 802.11 and 3g networks\
\* where to from here?

Conclusions

Since any number you pick for buffering is guaranteed to be wrong for
many use cases we care about, the general solution will await operating
systems implementers revisiting buffering strategies to deal with the
realities of the huge dynamic range of today’s networks, but we can
mitigate the problem (almost) immediately by tuning without waiting for
nirvana to arrive.
