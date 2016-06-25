---
title: Using the testlab
date: 2011-08-11T15:27:25
lastmod: 2011-09-13T14:15:47
type: wiki
---
Using the testlab
=================

Cluster control
---------------

Experiment - thrash the network hard
------------------------------------

Here's a simple way to get all the routers sending lots of data at the
same time.

On <link>io</link>, run

`iperf -s`

On <link>io</link>, run

`pdsh -lroot -grouters 'iperf -t 60 -c io.lab.bufferbloat.net'`

Boom, all the routers will start running iperf simultaneously. You can,
after <link>setting your routing</link>,\
set up various tests of <link>QoS</link>, or <link>different TCP/ip
stacks</link>, or <link>changing your window size</link>,\
slam the whole system while doing other things, and capture the results
with tshark or wireshark.

For example this will test a larger cwin:

`pdsh -lroot -grouters 'iperf -w 1M -t 60 -c metis.lab.bufferbloat.net'`

which was the subject of <link>Experiment - QoS</link>, which has many
more examples

[Machines](Machines.md)
