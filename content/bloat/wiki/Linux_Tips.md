
---
title: Linux Tips
date: 2011-02-02T07:37:05
lastmod: 2013-07-27T11:50:28
type: wiki
---
Linux Tips
==========

The [Dogfood Principle]({{< relref "projects/bloat/wiki/Dogfood_Principle.md" >}}) page covers the settings on the
bufferbloat.net servers, which run Linux.

Some people note that in some bufferbloat experiments we set the
transmit queue length (txqueuelen) to zero on Linux.

Note that this is **at best** a short term hack to reduce pain, and the
wrong answer in general, and on some hardware will cause your system to
go completely catatonic. On others (notably some of the "smartest" which
generally aren't but that's another story) it IS the right thing...

Please, please, don't just blindly go twisting knobs without
understanding what you are doing... and we've mostly settled on
fq\_codel as being the best answer yet, see the
[Bloat-videos]({{< relref "projects/cerowrt/wiki/Bloat-videos.md" >}}) page for some details on that.

So the remainder of this web page is very old... and we haven't actually
updated the main bufferbloat web servers to any huge extent lately,
we're running the [Yurtlab]({{< relref "projects/cerowrt/wiki/Yurtlab.md" >}}) instead, (and we are
doing several large scale test deployments...)

... so for historical reasons... read on...

There are many potential places where buffers may hide today. These
include (at least):

1.  the Linux transmit queue (which txqueuelen controls)
2.  device drivers themselves may hide one or more packets (e.g. the
    Libertas driver) internally, which simplified its implementation
3.  Most current hardware has very large DMA ring buffers, often
    allowing for up to 4096 packets/queue in the hardware itself; in the
    drivers we've examined, the default size seems to be in the 200-300
    packet range (also true on some Mac and Windows ethernet drivers
    we've played width).
4.  Sometimes the hardware itself may also have packet buffers buried
    in them. Again, from OLPC, the wireless module there has 4 packets
    of buffering hidden out in the device.\
    (?) encryption buffers.
5.  Old hardware often has very limited buffering in the drivers and
    hardware; this is part of the history as to how we got to where
    we are.

Some buffering is necessary for your network stack to work properly. The
only reason txqueuelen could be set to zero from 1000 was that that
hardware was known to have additional 256 packets of buffering in the
Intel wireless and ethernet drivers the tests were run on. Normally, for
classification to be able to work, we'd like to have the Linux transmit
queue set to some reasonable (small value), so that we can play nice
traffic games of various sorts.

Now the question is: how much buffering is "enough"?

And the answer is, unfortunately, not simple. The buffering that should
be present depends upon the bandwidth (which may vary by orders of
magnitude) and the delay (which is anywhere from 10ms to a couple
hundred if you are going around the world). The rule of thumb has been
the bandwidth delay product, where the delay has been presumed to be
around 100ms. And it also depends on workload. The rub is that ethernet
spans 3 orders of magnitude in bandwidth, and on wireless, it's even
worse, where moving your laptop a few inches can change your performance
by orders of magnitude.

What a server system's buffering needs on 1G or 10G networks is very
different than what you will need on an 802.11g network (which at best
runs about 20Mbps, and often runs much more slowly). But right now, the
knobs, for historical reasons, were often set to maximize bandwidth
performance for such server systems without regard to latency under load
on computers in most people's homes.

So whatever we set these knob(s) to, it is guaranteed to be wrong much
of the time for some systems. At best, until we have better tools at
hand, we can mitigate our pain a bit by twisting the knobs to something
that may make more sense for the environment where you are running most
of the time, and some of our default values in our operating systems and
device drivers may need tuning in the short term to the bandwidth. So
some short term mitigation is possible by being slightly more clever.

The real long term solution, however, is AQM (active queue management)
in the most general sense: the buffering at all layers of the system
needs proper integration and management (not just router queues), and it
needs to be very dynamic in nature: ergo the interest we have in eBDP,
SFB, algorithms and we hope RED Light soon. We need to signal the end
points to slow down appropriately. And getting the operating systems to
manage both their buffering in concert with the underlying device
drivers and hardware is why this is going to be an interesting problem
(as in the Chinese curse).

Loaded guns can hurt if you aim them at your foot and pull the trigger.
So please do be careful, and think...

Enable <link>ECN</link>, <link>SACK</link>, and <link>DSACK</link>
------------------------------------------------------------------

These sysctl settings can be stored in the main /etc/sysctl.conf file,
or in a file in the /etc/sysctl.d directory.

@ net.ipv4.tcp\_ecn=1\
net.ipv4.tcp\_sack=1\
net.ipv4.tcp\_dsack=1@

Note that there is still some broken ECN CPE (e.g. home router)
equipment out there; if you have problems in some environments, please
let us know.

Set the size of the ring buffer for the network interface
---------------------------------------------------------

NOTE: THIS HACK IS NO LONGER NEEDED on many ethernet drivers in Linux
3.3, which has Byte Queue Limits instead, which does a far better job.

In modern devices, the dma tx queue often defaults to settings suitable
for transmission on a pure GigE (or faster) network.

If your network has significant bottlenecks (such as a 3Mbit home
gateway or wireless), this is the most important knob to twist to reduce
your bufferbloat.

Once data hits the dma tx queue, it cannot be controlled or shaped. In
many cases ethtool is not supported, however, if you can, reduce these
buffers to the bare minimum for good performance. Few devices support
going as low as this:

@ ethtool -G eth0 tx 4\
ethtool -G wlan0 tx 4@

But many can get to 20 or below. See also: [Known Bloated Drivers]({{< relref "projects/bloat/wiki/Bloated_Driver_List.md" >}}) for more information and patches.

You can observe your existing settings with:

@ ethtool -g eth0\
ethtool -g wlan0@

Reduce transmit queue length
----------------------------

NOTE: with [codel]({{< relref "projects/codel/wiki/Wiki.md" >}}), this is no longer needed
either.

This is a separate setting for each network interface. Examples:

@ ifconfig wlan0 txqueuelen 16\
ifconfig eth0 txqueuelen 50@

(50 is the default transmit queue length on FreeBSD.)

Assuming your dma tx queue is under control, you can also <link>Traffic
Shaping|shape</link> the traffic using an appropriate
<link>qdisc</link>, and have a larger txqueuelen.

More Adventures
---------------

Note: the debloat-testing kernel is not in use at present. We may
resurrect it soon.

If you want to start running a recent Linux kernel with eBDP, SFB, and
start more serious testing of such attacks on the problem, then you are
a customer of the [debloat-testing kernel
tree](http://git.infradead.org/debloat-testing.git) maintained by John
Linville.

This tree has a (possibly frequently changing) set of kernel patches
that start to attack the bufferbloat problem in less naive ways. We hope
to get more automated builds for multiple distro's going soon (help
gratefully appreciated!). In the very short term, if you don't mind dead
puppies (like your laptop) you may find this [Ubuntu 10.10 kernel (64
bit) useful](http://mirrors.bufferbloat.net/Builds/)). Note that this
kernel is also built preempt, as Dave likes to do music. Additionally,
you might like something more graceful to set your wireless queue length
to something more sensible for that kernel; a Debian
/etc/networks/if-up.d [wlan script]({{< relref "projects/bloat/wiki/Wlan_script.md" >}}) for this is available.

References
----------

[Home Router Puzzle Piece One – Fun with your
switch](http://gettys.wordpress.com/2010/11/29/home-router-puzzle-piece-one-fun-with-your-switch/)
