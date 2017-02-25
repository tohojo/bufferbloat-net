---
title: Introduction
date: 2011-04-11T07:00:24
lastmod: 2015-05-16T12:54:51
type: wiki
---
Introduction
============

Bufferbloat is the undesirable latency that comes from a router or other
network equipment buffering too much data. It is a huge drag on Internet
performance created, ironically, by previous attempts to make it work
better. The one-sentence summary is "Bloated buffers lead to
network-crippling latency spikes."

The bad news is that bufferbloat is everywhere, in more devices and
programs than you can shake a stick at. The good news is, bufferbloat is
now, after 4 years of research, development and deployment, relatively
easy to fix. See: fq\_codel: [wiki](/codel/wiki/index.md). The even better
news is that fixing it may solve a lot of the service problems now
addressed by bandwidth caps and metering, making the Internet faster and
less expensive for both users and providers.

The introduction below to the problem is extremely old, and we recommend
learning about bufferbloat via van jacobson's
[fountain](http://www.bufferbloat.net/projects/cerowrt/wiki/Bloat-videos)
model instead. Although the traffic analogy is close to what actually
happens... in the real world, you can't evaporate the excessive cars on
the road, which is what we actually do with systems like fq\_codel
[wiki](/codel/wiki/index.md).

Still, onward to the blow.

Packets on the Highway
----------------------

To fix bufferbloat, you first have to understand it. Start by imagining
vehicles traveling down an imaginary road. They're trying to get from
one end to the other as fast as possible, so they travel nearly bumper
to bumper at the road's highest safe speed.

Our "vehicles" are standing in for Internet packets, of course, and our
road is a network link. The 'bandwidth' of the link is like the total
mount of stuff the cars can carry from one end to the other per second;
the 'latency' is like the amount of time it takes any given car to get
from one end to the other.

One of the problems road networks have to cope with is traffic
congestion. If too many cars try to use the road at once, bad things
happen. One of those bad things is cars running off the road and
crashing. The Internet analog of this is called 'packet loss'. We want
to hold it to a minimum - however we do not want to eliminate it
entirely.

There's an easy way to attack a road congestion problem that's not
actually used much because human drivers hate it. That's to interrupt
the road with a parking lot.

You drive in, a traffic cop at the exit tells you when you can leave,
and then you drive out. If there's nobody using the parking lot, you can
just zip right through.

But, as the parking lot fills the cop at the exit becomes ever more
necessary.

He has to control the timing and rate by which vehicles exit the parking
lot, so he can hold the number of vehicles in the road downstream of the
lot at sane levels. He looks at the upstream road he's protecting
occasionally, to make sure he's not causing problems here.

We only have one cop managing the lot in this case, so the other thing
that has to be true is that the lot doesn't exceed its maximum capacity.
That is, cars leave often enough relative to the speed at which they
come in that there's always space in the lot for incoming cars.

The Internet analog of our parking lot is a packet buffer. People who
build network hardware and software have been raised up to hate losing
packets the same way highway engineers hate auto crashes. So they put
lots of huge buffers everywhere on the network.

In network jargon, this optimizes for bandwidth. That is, it maximizes
the amount of stuff you can bulk-ship through the network in constant
time. The problem is that it does horrible things to latency. To see
why, let's go back to our cars in the parking lot.

It's rush hour now, and vehicles of all types enter the parking lot,
faster than they can exit. Emergency vehicles, cars, vans, food trucks,
all pile up in the order they arrived. (This is called FIFO - first IN,
First Out order).

Our bufferbloated parking lot is so big that our cop can't see from one
end to the other. He can't see what vehicles are important, and which
ones are not.

Our poor traffic cop overloads - he's so busy sorting out the traffic
jam in front of him, he can't look upstream anymore, either. He gets
distracted by the mess in front of him; people start driving over the
berm, smooth traffic flows become clumpy, and the highway he's trying to
manage gets overloaded.

When this happens to the Internet, the parking lot - the buffer - adds
latency to the connection. Packets get large time delays, just like you
would when stuck in a real-world traffic jam. Smooth network traffic
turns into a herky-jerky stuttering thing; cars try to find alternate
routes, and often fail.

A constantly spaced string of vehicles coming in tends to turn into a
series of clumps coming out, with size of each clump controlled by the
width of the exit from the parking lot. This is a problem, because car
clumps tend to cause car crashes.

Performance becomes worse than if the buffer weren't there at all. And -
this is an important point - the larger (more bloated) the buffer is,
the worse the problems are.

The Bufferbloat Project has found some really, really, really oversized
parking lots on the Internet. May Internet connections have buffers
that, if the connections were highways, would be the proportional size
of the state of Texas.

From Highway to Network
-----------------------

Now imagine a huge network of roads and highways, each with parking lots
at their intersections. Cars trying to get through will experience
multiple cascading delays, and initially smooth traffic will become
clumpy and chaotic. Clumps from upstream buffers will clog downstream
buffers that might have handled the same volume of traffic as a smooth
flow, leading to serious and sometimes unrecoverable packet loss.

As the total traffic becomes heavier, network traffic patterns will grow
burstier and more chaotic. Usage of individual links will swing rapidly
and crazily between emptiness and overload cascades. Latencies, and
total packet times, will zig from instantaneous to
check-again-next-week-please and zag back again in no predictable
pattern.

Packet losses - the very problem all those buffers were put in to
prevent - will begin to increase dramatically once all the buffers are
full, because the occasional thousand car pileup is the only thing that
can currently tell Internet routers to slow down their sending.

Bad consequences of this are legion. One of the most obvious is what
latency spikes do to the service that converts things like website names
to actual network addresses - DNS lookups get painfully slow.
Voice-over-IP services like Skype and video streamers like YouTube
become stuttery, prone to dropouts, and painful to use. Gamers get
fragged more.

The way these latency-sensitive services degrade illustrates a general
point. Perceived speed of the Internet is much more a function of
latency (time to get a response) than of bandwidth (ability to
bulk-ship). Thus, bufferbloat hammers the performance characteristic
users care about most.

For the more technically-inclined reader, there are several other
important Internet service protocols that degrade badly in an
environment with serious latency spikes: NTP, ARP, DHCP, SSH, and
various routing protocols. Yes, things as basic as your system clock
time can get messed up!

And - this is the key point - the larger and more numerous the buffers
on the network are, the worse these problems get. This is the
bufferbloat problem in a nutshell.

One of the most insidious things about bufferbloat is that it easily
masquerades as something else: underprovisioning of the network. But
buying fatter pipes doesn't fix the bufferbloat cascades, and buying
larger buffers actually makes them worse!

Three Cures and a Blind Alley
-----------------------------

Now that we understand the bufferbloat problem, what can we do about it?

We can start by understanding how we got into this mess; mainly, by
equating "The data must get through!" with zero packet loss.

Hating packet loss enough to want to stamp it out completely is actually
a bad mental habit. Unlike real cars on real highways, the Internet's
foundational TCP/IP protocol is designed to respond to crashes by
resending an identical copy when a packet send is not acknowledged. In
fact, the Internet's normal mechanisms for avoiding congestion rely on
the occasional packet loss to trigger them. Thus, the perfect is the
enemy of the good; some packet loss is essential.

But, historically, the designers of network hardware and software have
tended to break in the other direction, bloating buffers in order to
drive packet losses to zero. Undoing this mistake will pay off hugely in
improved network performance.

There are three main tactics:

First, we can **pay attention**! Bufferbloat is easy to test for once
you know how to spot it. Testing for bufferbloat and fixing it needs to
be part of the normal duties of every device designer, software driver
author, and every network administrator. Some fixes are easy enough for
Aunt Tilly to install.

Second, we can decrease unmanaged buffer sizes. This cuts the delay due
to buffering and decreases the clumping effect on the traffic. It can
increase packet loss, but that problem is coped with pretty well by the
Internet's normal congestion-avoidance methods. As long as packet losses
remain unusual events (below the levels produced by\
bufferbloat cascades), resends will happen as needed and the data will
get through.

Third, we can use smarter rules than FIFO for when and by how much a
buffer should try to empty itself. That is, we need buffer-management
rules that we can expect to statistically smooth network traffic rather
than clumpifying it. The reasons smarter rules have not been universally
deployed already are mainly historical; now, this can and\
should be fixed.

Next we need to point out one tactic that won't work by itself.

Some people think the answer to Internet congestion is to turn each link
into a multi-lane highway, with toll booths, fast lanes, slow lanes and
carpooling. The theory of QoS ("Quality Of Service") is that you can put
priority traffic in fast lanes and bulk traffic in slow ones.

This approach has historical roots in things telephone companies used to
do. It doesn't work well for Internet traffic. To return to the roads
and highway analogy, only a few spots have carpool lanes, and rest of
the roads are still jammed. Once the special lanes are gone (you get to
another part of the network), there's still dozens of overstuffed
parking lots administered by cops with different rules...

Explicit QoS may have a place in our overall strategy for network
performance, but the right order to do things is this: first, reduce the
size of the parking lots, then get buffer management right, then
implement QoS on top of that.

 How Hard Is It? 

We started by asserting that bufferbloat is easy to fix. First we'll lay
out the reasons for optimism, then the problems:

First, it's easy to detect once you understand it - and verifying that
you've fixed it is easy, too.

Second, many fixes are cheap and give direct benefits as soon as you've
applied them. You don't have to wait for other people to fix bufferbloat
in their devices to improve the performance of your own.

Third, you'll usually only have to fix it once per device; continual
tuning isn't necessary.

Fourth (and importantly!), trying to fix bufferbloat won't significantly
increase your risk of a network failure. If you fumble the first time,
it's reversible.

The hard problems are these:

First, we don't yet know how to write good buffer-management rules for
networks with variable bandwidth. This is a research area, as we write
in early 2011 good results seem likely soon.

Second, lots of devices and device drivers need to get debloated, their
fixes tested, and the manufacturers convinced field upgrades are
worthwhile. This is going to take some time.

Third, a lot of devices (especially consumer-grade routers, but also
wireless access points, switches, DSLAMs, and cable modems) are
difficult enough to upgrade firmware on that they will need to be
replaced. Since the IPv6 transition is bearing down on us, however, it
may be possible to fold our upgrade wave into that one.

The Stakes Are High
-------------------

Those of us who have been studying bufferbloat believe that many of the
problems now attributed to under-capacity and bandwidth hogging are
actually symptoms of bufferbloat. We think fixing the bufferbloat
problem may well make many contentious arguments about usage metering,
bandwidth caps, and tiered pricing unnecessary. At the very least, we
think networks should be systematically audited for bufferbloat before
more resources are plowed into fixing problems that may be completely
misdiagnosed.

We also have some worries about the future. For various reasons
(including the gradual retirement of Windows XP) more and more Internet
traffic is now running over saturated links. In this new environment, we
think there is a possibility that bufferbloat cascades and defects in
buffer-management strategies might produce self-synchronising behaviour
in network traffic - packet floods and network resonance on a local,
regional or global scale that could be a greater threat to the Internet
than the congestion-driven near-collapse of the NSF backbone in 1986.

This is a classic "black swan" situation in Nassim Taleb's sense; in
today's Internet-dependent economy there is a potential for nearly
incalculable havoc in the worst case, but we don't even know in
principle how to estimate the overall risk. Bufferbloat mitigation might
keep us out of some very serious trouble, and is worth pursuing\
on those grounds alone.
