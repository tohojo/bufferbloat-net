
---
title: Dogfood Principle
date: 2011-01-27T06:29:23
lastmod: 2012-03-27T09:10:15
type: wiki
---
Applying the Dogfood Principle
==============================

The current set of bufferbloat.net servers are configured according to
the [dogfood
principle.](http://patternlanguagenetwork.myxwiki.org/xwiki/bin/view/Patterns/DogFoodPrinciple)
We're practicing what we preach, to what extent possible. Some of the
knobs we are twisting are not well tested in the field, so we might as
well test them somewhere! Admittedly a primary goal is to keep the
service(s) running, so if we encounter problems, we will modify what is
in place, and eventually move into the cloud. Until then, the dogfood
principle applies. There will be a set of formal test servers and
routers up at some point, too.

<link>ECN</link> is turned on. Using ECN does little good unless one of
the routers on the path actually uses it. Work is ongoing to see if it
can be enabled in the general case. In the meantime feel free to try it.

<link>SACK</link> and <link>DSACK</link> are enabled. These do help.

It's very easy to enable these three options, under various forms of
Linux. Into your /etc/sysctl.conf you can put\
@ net.ipv4.tcp\_ecn=1\
net.ipv4.tcp\_sack=1\
net.ipv4.tcp\_dsack=1@

[IPv6](IPv6.md) is enabled in primary DNS and as part of the main
website(s) themselves. IPv6 behavior is potentially worse, as IPv6
doesn't get anywhere near as much attention from developers, ISPs, or
hardware vendors. It's potentially better in that less stuff (NAT,
shapers) muck with it.

<link>TXQUEUELEN</link> is reduced to 64. This is (probably) the wrong
thing for a server, but for one that is not doing traffic shaping (yet)
and handling multiple flows, it makes sense as it does push more
decision making back into the tcp portion of the buffer stack, where it
belongs.

<link>Driver Buffers</link> is currently unknown. These are older
servers however, so we suspect they are non-bloated.

There is (currently) no outgoing traffic shaping in place, however
<link>Qdiscs\#SFB|SFB</link>, <link>Qdiscs\#RED|RED</link> are under
consideration.

The apache servers are using
[Apache-mpm-event](http://httpd.apache.org/docs/2.2/mod/event.html)
instead of the more common
[Apache-mpm-worker](http://httpd.apache.org/docs/2.2/mod/worker.html) -
theoretically improving <link>HTTP 1.1</link> performance.

There is also a fix to MSIE recognition:

http://blogs.msdn.com/b/ieinternals/archive/2011/03/26/https-and-connection-close-is-your-apache-modssl-server-configuration-set-to-slow.aspx

All major bits of code (e.g. redmine) are running under a form of
fastcgi (fcgid), which load balances and scales up and down well with
minimal memory use.

[TCP Vegas](Experiment_-_TCP_cubic_vs_TCP_vegas.md) is
under consideration.

The (low-power) dedicated servers currently running are donated by
[ISC](http://www.isc.org) and [Teklibre](http://www.teklibre.com) .

If you encounter problems, please send an email to support AT
bufferbloat.net, detailing your configuration, and a traceroute.You can
also take steps to [Diagnose your bufferbloat](Experiments.md).
