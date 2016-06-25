---
title: AHCP
date: 2012-08-17T14:20:22
lastmod: 2012-08-17T14:20:22
type: wiki
---
AHCP
====

ahcp is the [ad-hoc configuration
protocol](http://www.pps.univ-paris-diderot.fr/~jch/software/ahcp/)
created by [Juliusz
Chroboczek](http://www.pps.univ-paris-diderot.fr/~jch/) .

It uses link-local ipv6 multicast to distribute ipv4 and ipv6 addresses,
ntp and name server information. It differs from dhcp and dhcpv6 in that
it:

Uses one packet to distribute ipv4 and ipv6 information (dhcp and dhcpv6
require separate and more packets each)\
Distributes point to point addresses (/32 ipv4 and /128 ipv6)\
Lacks the backward compatability cruft in dhcp and dhcpv6

For more information, including the current specification and rfc,
please see the [ahcp web
site](http://www.pps.univ-paris-diderot.fr/~jch/software/ahcp/) .
