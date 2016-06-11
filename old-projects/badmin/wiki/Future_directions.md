
---
title: Future directions
date: 2011-05-22T04:39:53
lastmod: 2011-05-22T07:58:24
type: wiki
---
Future directions
=================

History
-------

When I (dave taht) started at this, my task was "produce working
routers". Last week, it became "make the database\
work with postgres", then "make it work with django", later on it became
"get the web site running", and then "make it possible to ask useful
questions and get useful results", and yesterday \#171 "create working
defaults for QoS", proceeding thus, rapidly, from possible to impossible
in a matter of weeks, across several subfields (embedded, QA, web, and
database) that are hard to multi-task across.

A breather, and design step, and a design document, and a plan that
extends out at least a year... Are necessary.

My intent was to "produce working routers". You have a good version of
openwrt, with almost all the related patches required for your specific
project pushed into openwrt's head repository. You have a working build
system on huchra, and innumerable other pieces of infrastructure on
these wikis and server to support your further efforts.

The routers seem to be working well.

The routers can be further tested, using standard QA processes \#163, or
experimented with, in a <link>bismark-testbed:testlab</link>. Given how
late various packages landed, I'm rather unsatisfied with the testing
thus far, any given router and distribution needs to run for several
weeks, preferably months, or years. I'm glad, that **thus far**, we seem
to avoided a recurrence of anything like \#136 which cost me three days
of testing and would have rendered routers unusable in the field inside
of a day.

The month prior, I had trained three people to do packaging, they all
evaporated to a large extent. I had expected those people to be
available for testing, they were, barely. A new developer arrived, who
did nothing. When I'd agreed to try and pull this off in under two weeks
I did not anticipate resourcing problems this bad. Our bacon was saved
by 3 volunteers from openwrt.

I now have no time left. On monday I intend to meet with netops and
hopefully land the remainder of the DNS/server issues for
networkdashboard.org.

If I cannot, the <link>bismark-testbed:testlab</link> will be kind of
hard to deal with, given the number of machines that need names and a
coherent addressing scheme. I need to supply the passwords to someone,
and I fully expect the system to become a mess rapidly without someone
actively managing it.

The rest of the team needs to [close their
bugs](http://www.bufferbloat.net/projects/bismark/issues?query_id=1),
[review the
roadmap](http://www.bufferbloat.net/projects/bismark/roadmap), and
declare this a "baked" release or not.

That said, I have some feedback regarding the current structure and an
outline of some future directions.

### Database interface

The new backend database is almost completely untested. I do not know
what else will break and have little confidence it can be made to work
fully, even for development purposes, without my further involvement.

### Web interface

There is a huge impedance mismatch between the available web developer
and the data collected thus far. Django is not up to the job,\
and another toolkit and developer capable of working in it (or two) must
be chosen. Dojo as a javascript toolkit is not bad, but all that handles
is the actual presentation of the data, not interpretation.

### Tunneling mechanism

A TCP based transport running these distances results in latencies often
in the 10s of seconds. (as an example, I wrote the last three sentences
while waiting for a character to come back from the tunnel)

Using a udp based vpn such as strongswan or openvpn, would help
enormously, and also improve security overall. There ARE edge cases
where a vpn will not work, but I would hope, few of them.

### Test data & architecture

Most of the data appears to be overprocessed at the site(s). I've noted
a few problems:

-   timing the execution of something like ping is very different than
    actually getting ping time.
-   The same also applies to DNS. The original test was timing "host",
    which is a much larger binary than "nslookup"
-   I have not looked into the traceroute test, etc.
-   XML is a terrible transport mechanism

### Test gear

Routers are not working too bad. I'm happy about that. We'll see how
they survive a few weeks in the field. I expect problems.

### QoS

NOBODY has a good answer for QoS at the moment. It frustrates me too.
It's an excellent avenue for research.

Moving forward
==============

At least in low bandwidth places such as South Africa, it seems possible
to actually take packet dumps, rather than process the output\
of tools like ping, etc, and ship them back to Georgia for more
analysis, later.

Using package captures rather than processed data
-------------------------------------------------

By using filtered things like:

`tcpdump -i eth1 -s1500 -wnoqos.cap host gw.lab.bufferbloat.net &`

Very small captures can be created, that in most cases can also be
compressed, then shipped up to a central server where they can be
processed more, both in a database and in conventional tools such as
wireshark, xplot.org, etc.

Similar filters, measuring, for example, just DNS traffic, are also low
overhead.

Given that the up/dl bandwidth in the 3rd world is so low, using
tcpdump, especially with a filter like the above, which does most of the
processing near the hardware, does not appear to heisenbug the simpler
tests.

Bandwidth tests are feasible too (I'm using a USB stick on the lab to do
so) At speeds approximately 2Mbit or so or above, dumping is not
feasible.

For higher bandwidth sites or higher bandwidth tests, MIT has suggested
using their measurement box, attached to a mirrored port. There is some
support in the router's switch for this capability but I do not know if
it works at present.

Tools
-----

There are a variety of good tools in this release, including httping,
tcpdump, fping, bing.

There are a variety of good packages also available but not installed or
tested, such as openvpn, and snmpd.

There are innumerably other wonderful tools for managing routers.
Nagios... RT... name it, it already exists.

Network dashboard
=================

The core idea is good - however there exist many off the shelf tools
that you could just use, such as collectd, snmpd, big sister, etc, to
achieve a goal of making a useful service for the edge, rather than
re-inventing them.

Other projects
==============

As this project leveraged several of my own projects notably
<link>iscwrt:Wiki|iscwrt</link> and <link>uberwrt:Wiki|uberwrt</link>, I
would hope that tools and techniques from those will feed back into
this, and vice versa, in the classic open source manner.

Regrettably, I am out of time this summer to do much more than support
the distribution and help get the database AS WRITTEN working, but it
appears to be impossible to use django for it, and I'd like to rip out
the hacks in place to support django whenever another toolkit is chosen.

If you acquire additional resources and can prioritize the movement of
various bits located on bufferbloat.net to your own servers,\
I will provide estimates as to what it will take to do so and provide in
a SOW.

Regrets
-------

I should not have exceeded my SOW and attempted to fix \#104 and \#51,
despite gaining permission to do so. I ended up spending over 4 days on
it while slowly realizing that neither the mysql design nor the postgres
port were going to work with django. I have problem in tossing the work,
and not billing for it. I should have spent the time instead, working on
the bugs in [iscwrt](http://www.bufferbloat.net/projects/iscwrt/issues)
that also affect you.
