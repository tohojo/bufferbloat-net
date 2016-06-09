
---
title: Bismark
date: 2011-07-14T08:03:45
lastmod: 2011-07-14T08:09:08
---
Bismark
=======

Description
-----------

This consists of two different packages: bismark-mgmt, which talks to
the server and sets up remote tunnels (apart from other things), and
bismark-active, which conducts active measurements.

In bismark-mgmt, a probe runs every minute. This probe consists of a
single UDP packet to the probe server, and serves two purposes; one as a
heartbeat, so that the server knows it's alive, and also to punch a hole
in the NAT (if one exists), so that a reverse-ssh tunnel can be
established on-demand from the server.

The bismark-active script runs every 5 minutes. It conducts a subset of
the following tests: ping to one of a set of servers, ping to the
last-mile router, traceroute to the server, dns lookup time to a set of
servers, netperf upstream and downstream tests, ping to the last mile
router at the same time as the netperf tests, shaperprobe, and ditg for
measuring packet loss.

The output from the test is stored as an xml file in /tmp/bismark/ and,
upon completion of test, is immediately uploaded to the measurement
server and deleted upon upload.

Testing
-------

bismark-mgmt should report to bdm after first boot, and every minute
thereafter, as long as it's connected to the Internet. First probe takes
a few minutes after boot, perhaps up to 5 minutes. Once it reports, we
should be able to establish an ssh tunnel to it from the server.

bismark-active is tested by waiting for the data file on the measurement
server. The first file should contain **all** of the above measurement
tests; and should have sane values for them.
