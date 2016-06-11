
---
title: Iscwrt build
date: 2011-04-16T09:48:06
lastmod: 2011-04-30T23:25:04
type: wiki
---
Iscwrt build
============

NOTE: The build of iscwrt is TOO LARGE to fit in less than 8MB flash.
Only the wndr3700v2 is supported.

Get it from: http://huchra.bufferbloat.net/\~each/iscwrt/ar71xx/

This build is a lot closer to the final <link>Build Configuration</link>
than the others, at present.

(and consequently, more borken)

Features
--------

ISC bind9 with DNSSEC and dynamic dns support\
ISC DHCP and DHCPv6 support\
IPv6\
NTP supplied via local server\
Qos\
Reduced TXQUEUELENs\
An Open Radio SSID\
A private radio SSID\
Reverse DNS on the 2002: prefix\
Lighttpd Web Server\
Port forwarding for Phone and printer

Left to do
----------

2002 working\
2001 policy routing

v4 and v6 ddns working correctly\
Renumbering the network for different ACLs\
Secure NTP\
SIP proxy\
Rawstat parser\
DMZ\
Local (wireless) QoS support
