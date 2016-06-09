
---
title: Tuning_Cerowrt
date: 2012-06-08T08:02:01
lastmod: 2012-06-08T08:02:01
---
Tuning Cerowrt
==============

Cerowrt contains some advanced features that are disabled by default due
to in part lack of easy means to enable them.

Using DNS forwarders
--------------------

DNS servers throughout the globe are often badly implemented, and do not
support advanced features\
such as IPv6 and DNSSEC. However, most ISPs do provide a local DNS
server for use that caches a significant amount of data, thus reducing
latencies for DNS lookups by a lot. It is best to leverage that DNS
server if possible.

We have supplied an example forwarders.conf file with fixed pointers to
comcasts' DNSSEC enabled servers, however they do not work if you are
not on comcast's network.

So, find out the DNS servers your ISP provides pass DNSSEC data, and if
so, enter those servers into\
the forwarders.conf file, and enable using it by uncommenting the
relevant line in named.conf.

Your DNS lookups will remain secure, and speed up by a lot.
