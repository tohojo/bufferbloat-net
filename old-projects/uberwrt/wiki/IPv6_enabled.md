
---
title: IPv6 enabled
date: 2011-04-27T09:12:53
lastmod: 2011-04-27T09:12:53
type: wiki
---
IPv6 enabled
============

Enabling basic 6to4 on this router is straightforward. Simply add to
/etc/config/network

config interface v6\
option proto 6to4

And it will automagically figure out what interface is connected to the
internet, establish a 6to4 tunnel, and advertise addresses to your
internal network.
