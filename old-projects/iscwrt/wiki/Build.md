
---
title: Build
date: 2011-05-03T10:35:55
lastmod: 2011-05-03T10:43:35
type: wiki
---
Build
=====

Iscwrt build
============

NOTE: The build of iscwrt is TOO LARGE to fit in less than 8MB flash.
Only the wndr3700v2 is supported.

Get it from: http://huchra.bufferbloat.net/\~each/iscwrt/

This build is a lot closer to the final <link>uberwrt:Build
Configuration</link> than the others, at present.

(and consequently, more borken)

Working Features
----------------

ISC bind9 with DNSSEC and dynamic dns support\
ISC DHCP and DHCPv6 support\
IPv6 (native, 6to4, 6in4)\
NTP supplied via local server\
Qos\
Reduced TXQUEUELENs\
An Open Radio SSID\
A private radio SSID\
Reverse DNS on the 2002: prefix\
Lighttpd Web Server\
Python!\
Port forwarding for Phone and printer

Left to do
----------

2002 working (seems to be firewalled out)\
2001 policy routing (need to send 2001

v4 and v6 dyndns working correctly (ALMOST THERE)

Renumbering the network for different ACLs\
Secure NTP\
SIP proxy\
Rawstat parser\
DMZ\
Local (wireless) QoS support
