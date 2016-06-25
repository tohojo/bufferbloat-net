---
title: HOWTO
date: 2012-06-07T10:01:23
lastmod: 2012-06-12T09:15:14
type: wiki
---
HOWTO
=====

Simplest possible demo
======================

To demonstrate the effect of the fq\_codel scheduler, set up a fully
saturated network and then observe fq\_codel's effect on ping time
latency, as follows.

The effect can be clearly observed with a 10Mbps Ethernet connection:

    sudo ethtool -s eth0 advertise 0x002   # restrict to 10Mbps for demo

In a terminal window, run a continuous ping to some other machine on the
local network (the other machine does not need to have fq\_codel) and
leave it running:

    ping othermachine

In another terminal window, start up a dd pipe to the other machine to
fully saturate the network -- you should see the adverse effect on the
ping times:

    dd if=/dev/urandom | ssh othermachine dd of=/dev/null

Now enable fq\_codel -- observe the beneficial effect on the ping times
-- about 30X reduction in latency on a saturated 10Mbps network!:

    sudo tc qdisc add dev eth0 root fq_codel

Disable fq\_codel and wait a moment for the buffers to get bloated again
-- the ping times go back up again:

    sudo tc qdisc del dev eth0 root fq_codel

Remember to remove the demonstration 10Mbps restriction when you're all
done testing:

    sudo ethtool -s eth0 advertise 0xFFF
