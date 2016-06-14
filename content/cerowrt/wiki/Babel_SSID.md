
---
title: Babel SSID
date: 2012-08-17T14:14:01
lastmod: 2012-08-17T14:23:52
type: wiki
---
What's the babel SSID for?
==========================

The "babel" ssid is used for ad-hoc mesh networking in cerowrt. "babel"
is just a convention, any ad-hoc SSID would do. Other users use "mesh"
or something generic like that.

Cerowrt's mesh networking uses an alternative address distribution
protocol ([AHCP](AHCP.md)), rather than dhcp, which supports
distributing ipv4, ipv6, ntp, and dns server information. It is how
cerowrt routers (or any device using ahcp and babel) mesh together, if
two are in range of each other, and on the same channel.

While it would be possible to make "babel" be a hidden, rather than
announced, SSID, it seems to be best to make it visible and advertise
its availability. Note that although a "babel" SSID might be available,
you do have to set or autoselect the right wifi channel to use it from a
host.
