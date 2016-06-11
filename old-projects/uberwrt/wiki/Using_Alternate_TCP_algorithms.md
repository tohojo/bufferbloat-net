
---
title: Using Alternate TCP algorithms
date: 2011-07-23T06:55:17
lastmod: 2011-07-23T06:55:42
type: wiki
---
Using Alternate TCP algorithms
==============================

To see what TCP algorithms you can use:

    cat /proc/sys/net/ipv4/tcp_available_congestion_control

And you can change it via

    echo your_alternate_algorithm > /proc/sys/net/ipv4/tcp_congestion_control

Despite the path, this changes the algorithm for IPv6, too. By changing
the algorithm, and running tests, you can more accurately simulate the
behavior of the algorithms running on common desktop clients and
servers.

There is also an option we have not enabled yet - tcp\_low\_latency -
which appears to help reduce bufferbloat, but we have insufficient data
to turn it on, and turning it on will lower the degree to which we
emulate more normal boxes.

please feel free to turn it on and get back to us with your results.
