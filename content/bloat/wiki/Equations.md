---
title: Equations
date: 2011-04-26T04:11:32
lastmod: 2011-04-26T04:11:32
type: wiki
---
Equations
=========

Impacts of delay on TCP throughput
----------------------------------

The throughput of a single TCP session is not only constrained by the
available bandwidth, but also by delay and packet loss rate. Any layer 2
error correction method needs to find the right balance between adding
delay and accepting packet loss.

The Mathis formula gives an upper bound:

    Max DATA throughput rate < (MSS/RTT)*(1 / sqrt(p))

-   MSS: maximum segment size
-   RTT: round trip time
-   p: packet loss rate

RfC 3819, Section 8.5 gives a more accurate estimate:

                                             MSS
               BW = --------------------------------------------------------
                    RTT*sqrt(1.33*p) + RTO*p*[1+32*p^2]*min[1,3*sqrt(.75*p)]

       where

               BW   is the maximum TCP throughout achievable by an
                    individual TCP flow
               MSS  is the TCP segment size being used by the connection
               RTT  is the end-to-end round trip time of the TCP connection
               RTO  is the packet timeout (based on RTT)
               p    is the packet loss rate for the path
                    (i.e., .01 if there is 1% packet loss)
