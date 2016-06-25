---
title: Enabling dnssec
date: 2011-09-07T00:27:59
lastmod: 2011-09-07T00:27:59
type: wiki
---
Enabling dnssec
===============

The website at dlv.isc.org requires you to place a text record in the
zone to prove that you control the zone. This is how to do that, in a
DDNS-enabled zone:

    root@shipka:/etc/bind# nsupdate -l
    > zone bufferbloat.net
    > ttl 0
    > update add dlv.bufferbloat.net in txt ""
    > send
