
---
title: VPN solutions under evaluation
date: 2011-05-27T17:47:46
lastmod: 2011-05-27T19:18:55
---
VPN solutions under evaluation
==============================

There are multiple VPN solutions for routers and clients in this world.

The double reverse tunnel mechanism currently being used:

-   Tunnels TCP/ip over TCP/ip which is very slow
-   Does not scale well to hundreds of routers
-   Does not support other ports, such as SNMP
-   May be somewhat insecure \#59
-   Keys are embedded in the image \#185
-   IP addresses are embedded in the image \#185
-   Doesn't help someone that needs a real VPN

Alternatives
------------

Alternatives exist that may be more robust and flexible, which include
the basic ipsec tools, openvpn, strongswan, utunnel, etc

Test plan
---------

Since openvpn is available as an optional package already for bismark it
may prove a good starting point. However, strongswan as one example has
more support for in-kernel hardware based encryption and an alternative,
ipsec-tools, just put out a promising looking, lighter weight release.

1.  Establish a working certificate authority on
    <link>bismark-testbed:callisto</link>
2.  Establish a server on a x86 and/or bismark router. Currently there
    is one on [jupiter]({{< relref "wiki/Jupiter.md" >}}), it may make sense to
    try <link>bismark-testbed:metis</link>
3.  Establish working tunnels in the
    [testlab]({{< relref "wiki/Testlab.md" >}}) (there is already an openvpn
    tunnel using psk at teklibre.com)
4.  Establish working tunnels to other locations
5.  Test performance, scalability, security and reliability
6.  What sort of web interfaces are available

At the moment this work is stopped at part 1 - getting a working cert
authority - as all the documentation regarding openvpn on openwrt has
been obsoleted by a change to openssl and openwrt regarding how to
generate client certs properly.

openvpn appeared to be working with psk between
[jupiter]({{< relref "wiki/Jupiter.md" >}}) and
<link>bismark-testbed:aitne</link>. Certs are better, as in particular,
they can be revoked after a compromise. Theoretically.

Open questions
--------------

1.  Is there a hardware RNG available on the routers that needs a
    driver?
2.  What level of hardware encryption is available
3.  How fast can the router hardware go, while encrypting
4.  How many simultaneous clients can a given server withstand (also
    useful to know for the ssh solution)
5.  Can the solution be spread geographically?
6.  How well can we punch through various port numbers?
7.  How can we cleanly implement two-factor authentication (a user signs
    up, THEN goes live)
8.  How scalable is the solution?
9.  Is it worth switching at all?

Testers
-------

Evan Hunt\
Jim Gettys\
Dave Taht\
Paul Royal
