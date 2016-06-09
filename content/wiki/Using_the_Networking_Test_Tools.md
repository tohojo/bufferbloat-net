
---
title: Using_the_Networking_Test_Tools
date: 2012-03-30T12:47:04
lastmod: 2012-04-02T09:36:57
---
Using the Networking Test Tools in CeroWrt
==========================================

Alttcp
------

The alttcp package makes it possible to change the default congestion
control algorithm on the fly, as well as make other algorithms available
to user programs.

The list of available algorithms is in /etc/config/alttcp\
You can enable a change with /etc/init.d/alttcp start

It could use a gui.

Netperf (installed by default)
------------------------------

<link>CeroWrt</link> contains an advanced version of netperf which is
capable of exercising socket prioritization, diffserv (tos) setting, and
tcp congestion control algorithm selection. For the first time, these
options can be set and controlled via remote control, thus making
objective evaluations of the effect of these options in the real world,
possible.

However using it on, to, or from a non-cerowrt device requires building
it from svn sources at this time.

Example:

<code>\
netperf -l 60 -Y AF31,EF -H 172.30.42.1 ~~t TCP\_MAERTS -~~ -K
westwood,ledbat\
</code>

The above runs a test for 60 seconds, using AF31 classification in one
direction, EF in the other, talking to a router on 172.30.42.1, using a
reverse stream (TCP\_MAERTS is the reverse of TCP\_STREAM, both are
valid tests). The '--' ends the options to the test in particular, and
the -K controls what TCP algorithm is used on the local,remote sides.

Note: detecting bufferbloat generally requires running tests for
considerably longer than netperf's 10 second default.

Iperf (installed by default)
----------------------------

Rsync (installed by default)
----------------------------

CeroWrt contains a patched version of rsync that also supports Diffserv
classification and user selectable tcp algorithms.

ShaperProbe (installed by default)
----------------------------------

This tool is used to probe the available upstream bandwidth. It is still
imperfect (inaccuracies of over 20% as to the real bandwidth available
have been observed), and interacts badly with wireless hops, but seems
useful for directly connected wired uplinks.

httpping
--------

bwping
------

lft
---

fping
-----

fprobe
------

For more details, see <link>Monitoring CeroWrt</link>

snmpd
-----

For more details, see <link>Monitoring CeroWrt</link>

DitG (user installable)
-----------------------

Bismark related tools (user installable)
----------------------------------------

We co-operate with this project, although their focus is on measuring
the internet, and ours is on fixing it. As they use the same hardware as
cerowrt, we plan to make available at least some of the <link>Bismark
Tools</link>.
