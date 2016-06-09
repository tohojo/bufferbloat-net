
---
title: ACK_prioritization
date: 2011-06-20T05:43:13
lastmod: 2011-06-20T05:43:32
---
ACK prioritization
==================

In today's asymmetric internet environment up and download ratios can be
as poor as 1 to 11. While this works well for situations where downloads
predominate, it can cause terrible side effects on an otherwise healthy
network when an upload saturates the connection, starving the downloads
of needed ACK packets.

Ratios worse than 11 to 1 appear to touch closely to the theoretical
limit of \~23 to 1 that TCP/IP invokes in it's control stream.\
This is why, in part, worse ratios haven't appeared in vendor offerings,
as downloads are effectively throttled by upload bandwidth.

Since ack packets are very small (less than 72 bytes in ipv4 and less
than 140 bytes in IPv6, depending on encapsulation), shaping methods
that depend more on packets than bytes tend to suffer. 23 (ipv4) ack
packets can fit into the same amount of buffer space as a single upload
packet.

It is helpful from a policing perspective to look more at bytes than
packets, for uploads in an asymmetric network, to determine what packets
to best 'shoot'. Even then, the side effects of shooting an upload
packet instead of 23 ack packets tend to be more beneficial than often
realized.

Lastly, no shaping system takes into account the up/download ratio in
its decision making particularly well.

Several tries exist - notably, wondershaper, which pioneered the concept
of doing ACK prioritization for interactive ssh traffic back in 2002.

-   Note also that IPv6 changes the ack equation markedly - an
    encapsulated IPv6 6in4 ack packet can be as large as 140
    (reference needed)

