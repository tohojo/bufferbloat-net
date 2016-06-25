---
title: RRUL test suite
date: 2013-01-14T13:27:14
lastmod: 2014-03-23T00:46:45
type: wiki
---
RRUL test suite
===============

What is the RRUL test suite?
----------------------------

The [Realtime Response Under Load (RRUL) test suite
specification](https://github.com/dtaht/deBloat/blob/master/spec/rrule.doc?raw=true)
is an attempt to provide useful tools for analyzing network performance
under the heavy workloads that typically induce bufferbloat and other
networking problems. By creating a well defined specification we hope to
one day create a standard for network testing that is a vast improvement
on what currently exists in the field, which is mostly "packets per
second" and "raw bandwidth" testing.

RRUL prototype
--------------

A rrul prototype is being developed as part of the
[netperf-wrappers](https://github.com/tohojo/netperf-wrapper) tests. As
the title suggests, the tests are being wrapped around the popular
[netperf](http://www.netperf.org) netperf network analysis tool.
Requirements are a recent version of netperf, python, matplotlib,
python-matplotlib, and fping.

It does your classic latency under load tests in a variety of ways, and
provides output data in json format, with plots in CDF (very helpful)
and combination format. For an explanation of the charting techniques
used,\
see the <link>RRUL charting methods</link> page, and/or the [RRUL Rogues Gallery](RRUL_Rogues_Gallery.md) for some example plots.

What tests exist so far?
------------------------

rrul: an 8 bidirectional stream test against icmp and udp traffic, that
uses classification to attempt to exercise qos queues such as those in
802.11e\
rrul\_be: The same test as rrul, but without classification - the
fairest test at all\
rrul46compete: the same test, but using ipv4 and ipv6 at the same time\
rtt\_fair: test tcp performance between two or more hosts to see if a
system is RTT-fair (meaning that connections to machines at different
distances eventually or not get a fair share of the bandwidth)\
reno\_cubic\_westwood\_ledbat: test performance of different TCPs (if
enabled on both systems) in the same test

There are also some simpler tests in the suite currently:

tcp\_bidirectional: a basic test intended to give a "textbook" result of
two competing streams against a ping\
tcp\_upload: test multiple tcp uploads against a ping\
tcp\_download: test multiple tcp downloads against a ping

What tests are planned?
-----------------------

A core component of the specification includes measuring one-way delays,
while under load. Measuring this well is very important for voice and
gaming traffic as well as shorter transactions. We will probably write
something new or adopt\
d-itg for that.

Another core component is measuring typical web workloads, while under
load\
And the last component is a tcp traceroute or mtr, showing the source(s)
of the bottleneck(s) affecting the test(s).

Who is RRUL for?
----------------

Early versions are targetted at:

-   OS developers and driver writers
-   Network theorists
-   CIOs and equipment buyers
-   Students
-   System administrators and IT staff

At some point (after the bugs are sorted out), a web driven version
suitable for end-user testing at the edge will be developed, similar to
speedtest.net.

As the available resources and funding for developing even this first
part of the test suite are slim, getting to the end result will take
time and resources we do not have.

rrul tests are all over the web at this point... google for them.
