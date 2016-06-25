---
title: Janitorial Tasks
date: 2015-06-16T10:00:26
lastmod: 2015-06-16T15:06:51
type: wiki
---
Janitorial Tasks to clean up the bufferbloat
============================================

There are a ton of tiny code improvements that can be made across the
tens of thousands of applications "out there" to reduce their
bufferbloat, far more than any one person can do. But it is extremely
simple for someone to pick up a given codebase, make a small, basically
mechanical change, test it, and submit back to mainline. It had
generally been my hope that this would happen on everything - or that
many, many folk, would "scratch their itch" to fix something right in
front of them. A worldwide bufferbloat-reducing hackathon, with 1000
people participating, would knock out a goodly chunk of the problem in a
day!

A daydream was to see an university class (or dozens) tackle a dozen
applications with bufferbloat-fighting measures like the below, do them,
and measure before and after.

<link>BQL</link> on everything
------------------------------

BQL has generally been shown to be a win on every driver it has been
implemented on. It is a very few lines of code to add, however that code
requires having the device in front of you and rigorous testing, thus
BQL support entering the kernel has been fairly slow, with only a few
dozen [BQL enabled drivers](BQL_enabled_drivers.md) out of the hundreds of devices
"out there". Scratching this itch is a good introduction to kernel
programming, and a net win for fighting bufferbloat, and thus folk doing
a teeny bit of work on this here and there will gradually make a
difference (especially by fixing the driver(s) you are actually using in
front of you).

TCP\_NOTSENT\_LOWAT on interactive tcp applications
---------------------------------------------------

The [TCP\_NOTSENT\_LOWAT](https://lwn.net/Articles/560082/) option has
been shown to improve interactivity on quite a few application types,
notably [screen
sharing](https://developer.apple.com/videos/wwdc/2015/?id=719) and
[interactive web
traffic](https://insouciant.org/tech/prioritization-only-works-when-theres-pending-data-to-prioritize/)

It is a matter of a few minutes coding to add to various apps and
services that could use it, but more than a few minutes to see if it is
useful or not.

It is not a standard socket option as yet in Linux and only recently
exported in OSX. A good setting is in the range 16-128k.

It can also be set globally to a good figure for all applications. This
is useful on desktops and servers that have few context switch related
issues:

And: See \#450

TCP Congestion control selection
--------------------------------

Most applications do not allow for setting what congestion control
algorithm is used. Being able to select a lower priority, delay based
CC, is of benefit to some apps - for example, file uploads to flickr or
facebook. You can enable a different congestion control algorithm via:

    #ifdef TCP_CONGESTION
        char  cong_have[16];
        int my_len = 15;
        const char cong_control[] = "cdg"; // others might be reno, vegas,westwood, dctcp, cubic, etc
        setsockopt(socket, protocol, TCP_CONGESTION, cong_control, strlen(cong_control));
        if(getsockopt(socket, protocol, TCP_CONGESTION, cong_have, &my_len) ==
               SOCKET_ERROR) { perror("can't get cong control"); } 
        if (strncmp(cong_control,cong_have,strlen(cong_control)) != 0) {
               perror("can't set desired %s congestion control algorithm",cong_control);
        }
    #endif

Most OSes do not have a wide variety of TCP congestion control
algorithms available, so you should also check for success or failure as
per the above. Under linux you can see and set the available and enabled
congestion control algorithms via:

    cat /proc/sys/net/ipv4/tcp_available_congestion_control 
    cat /proc/sys/net/ipv4/tcp_allowed_congestion_control 

Some may need to be modprobed before being able to use. Usually that is
modprobe tcp\_X where X= the congestion control algorithm desired.

Correct classification
----------------------

The internet is rife with applications that actually do try to apply the
diffserv field, but either select something out of the old style TOS
bits, or do not work correctly with IPv6 (using IP\_TOS rather than
IPV6\_TCLASS).

Any place where you see IP\_TOS being set, and not IPV6\_TCLASS you
should put in a:

    #ifdef IPV6_TCLASS
        const int dscp = 0xc0 // CS6 network control in this example, CS1 is background...
        rc = setsockopt(s, IPPROTO_IPV6, IPV6_TCLASS, &dscp, sizeof(dscp));
    #endif

It is OK if this call is applied to a IPv4 socket (and fails) - and dscp
should be an int, rather than a char, as in IP\_TOS.

Some OSes allow you to use ECN (2) on udp packets, which should be used
very carefully, as in mosh. Extracting the received IP headers
appropriately to deal with ECT is beyond the current scope of this
document.

[TCP\_FAST\_OPEN](https://en.wikipedia.org/wiki/TCP_Fast_Open)
--------------------------------------------------------------

TCP fast open is a socket option that allows for sending data in the
initial syn portion of a TCP transaction. It requires that both servers
and clients [support it properly](https://lwn.net/Articles/508865/) -
notably that the connection's intent be idempotent.

ECN generation and awareness
----------------------------

Over 54% of the alexa top 1m (and all modern linux distros) will enable
ECN if asked for.

Apple [is enabling ECN support universally across iOS and
OSX](https://developer.apple.com/videos/wwdc/2015/?id=719) in the hope
that this will also drive demand and deployment of network queueing
algorithms that will mark, rather than drop, packets.

ECN can be [easily enabled for many OSes](/cerowrt/wiki/Enable_ECN.md).

But without a qdisc on the bottleneck links that respect it, turning it
on on the tcps has little effect.

fq\_codel enables ECN by default, but this is presently turned off in
openwrt's qos-scripts and in some circumstances in the
[sqm](/cerowrt/wiki/SQM.md) case, and off by default in pie and red.
Particularly on higher bandwidth links, we are reasonably confident that
ecn marking behaviors are sane in fq\_codel, pie, and red, (but not
codel by itself as presently implemented). [Cake](/codel/wiki/Cake.md) does
ecn marking by default with good overflow protection and is also on by
default. As more ecn rolls out, we expect to have to improve ECN
behaviors across all queue algorithms.

ECN has great applicability in DCTCP environments, for which a new
CE\_THRESHOLD option just landed for codel and fq\_codel.

TCP Pacing where appropriate
----------------------------

[TCP
pacing](http://www.ietf.org/proceedings/88/slides/slides-88-tcpm-9.pdf)
has become a very attractive option, especially in conditions where the
new [sch\_fq](https://lwn.net/Articles/564825/) qdisc can be applied on
an outward facing server.

When the application has a fixed maximum rate, applications can
[override the (pretty reasonable)
defaults](http://www.spinics.net/lists/netdev/msg251368.html) to get
better behavior.

    u32 val = 1000000;
    setsockopt(sockfd, SOL_SOCKET, SO_MAX_PACING_RATE, &val, sizeof(val));

Moving Quic along
-----------------

A great deal of google generated traffic has moved away from tcp to the
quic protocol. Standardization efforts are being started in the IETF. If
you are running chrome, Quic is enabled by default in many
circumstances, and can be enabled [easily if not already
enabled](https://en.wikipedia.org/wiki/QUIC)

A quic server handles thousands (millions ?) of flows. Having one kernel
socket per flow would be way too expensive, so having sch\_fq here does
not help as much as you might want it to, but it and sch\_fq or
fq\_codel remain a good combination. Also the rx path in UDP is not
optimized for 4-tuple hashing.

Quic uses an initial burst of 10 packets (IW10) followed by 22 paced
packets in it's initial configuration, all managed from userspace, no
sch\_fq needed. While this may seem large, quic also tends to use less
distinct flows overall than http users use.

Internally to the server application there are 2 hash tables, one lookup
on destination\_IP:destination\_port, and one on \*:destination\_port.
For a quic server, all sockets would share same keys.

Public work on quic is in the chrome web browser codebase and public
work on a [library, client and server is taking place on
github](https://github.com/devsisters/)

Fq\_codel or [cake](/codel/wiki/Cake.md) on edge routers
----------------------------------------------------

We've spent tons of time on trying to get [smart queue management](/cerowrt/wiki/SQM.md)
[right](http://snapon.lab.bufferbloat.net/~d/Presos/nznog-dave-taht-bufferbloat-jan-28.pdf)
- most recently defeated by GRO offloads in new routers, which is only
fixed in sch\_tbf and [cake](/codel/wiki/Cake.md), as yet.
