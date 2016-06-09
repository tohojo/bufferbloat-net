
---
title: Jupiter
date: 2011-08-11T15:25:26
lastmod: 2011-08-11T15:25:26
---
Jupiter
=======

Jupiter is a Cerowrt router configured to act as a gateway to the
[testlab]({{< relref "wiki/Testlab.md" >}}).

It has a real internet connection, has ipv6 support, provides a subnet
to 3 other routers, and has a USB stick mounted that serves as a local
cache of the release images and package database. The USB stick can also
be used to store long-running measurements of traffic.

QoS is disabled at present. It is also the default gw of the
<link>client routers</link>

Yes, it has a visible to the world webserver, which will one day be used
to document how to use the testlab.

http://jupiter.lab.bufferbloat.net.
