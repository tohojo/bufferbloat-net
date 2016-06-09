
---
title: Enable ECN
date: 2014-03-23T00:41:56
lastmod: 2014-03-23T00:43:45
---
Enable ECN
==========

ECN (Explicit congestion notification) is a means to signal congestion
without dropping packets. It uses 2 bits in\
the IP packet header that can be modified by routers along the path. A
"2" in this field indicates that the protocol\
on the other side (usually TCP) is prepared to respond to congestion
notifications, and a "3" observed in this field\
means that congestion occured and the other side of the link should take
action.

See [Stuart Cheshire and Dave Taht's presentation at ietf
89](http://www.ietf.org/proceedings/89/slides/slides-89-tsvarea-1.pdf)

for some tcp trace analysis of how ECN works and can smooth delivery of
tcp data under congestion.

Enabling ECN does not much good unless both hosts on the path have it
enabled, and the congested router on the path is running
<link>SQM</link> and supports ECN. But see above for how good the end
result can be...

Many servers do support ECN negotiation already, but few clients do.

Enabling ECN on OSX
-------------------

    sudo sysctl -w net.inet.tcp.ecn_initiate_out=1  
    sudo sysctl -w net.inet.tcp.ecn_negotiate_in=1  

To make the settings persistent,  put the following lines in
/etc/sysctl.conf:

    net.inet.tcp.ecn_initiate_out=1 
    net.inet.tcp.ecn_negotiate_in=1

Enabling ECN on Windows
-----------------------

netsh interface tcp set global ecncapability=enabled

Enabling ECN on Linux
---------------------

    sudo sysctl -w net.ipv4.tcp_ecn=1   

Like Mac OS X, to make setting persistent,  add line in /etc/sysctl.conf

Using ECN in CeroWrt
====================

All the interfaces have ECN enabled by default for most queues. It is
disabled for the wireless voice queue (better to lose a packet than
suffer extra delay).

In CeroWrt, at least, is presently recommended that ECN be disabled on
low bandwidth links, and enabled for high bandwidth ones. Thus the
<link>SQM</link> system in CeroWrt, typically used in scenarios where
there is a high rate down and a slow rate up, enables ECN asymmetrically
by default - ECN is on on the high speed down, and off on the slow speed
up.
