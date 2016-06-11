
---
title: Using the testlab
date: 2011-05-28T09:31:39
lastmod: 2011-05-28T11:50:40
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

On <link>metis</link>, run

`iperf -s`

On <link>metis</link>, run

`pdsh -lroot -grouters 'iperf -t 60 -c metis.noise.gatech.edu'`

Boom, all the routers will start running iperf simultaneously. You can,
after <link>setting your routing</link>,\
set up various tests of <link>QoS</link>, or <link>different TCP/ip
stacks</link>, or <link>changing your window size</link>,\
slam the whole system while doing other things, and capture the results
with tshark or wireshark.

For example this will test a larger cwin:

`pdsh -lroot -grouters 'iperf -w 1M -t 60 -c metis.noise.gatech.edu'`

which was the subject of <link>Experiment - QoS</link>, which has many
more examples
