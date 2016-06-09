
---
title: BloatLab_1
date: 2011-08-11T15:19:24
lastmod: 2012-10-01T21:27:18
---
BloatLab 1
==========

This is one of the several <link>public labs</link> dedicated to fixing
bufferbloat.

This lab is at the offices of the [Internet Systems
Consortium](http://www.isc.org) which is the home of the f-root server,
ntp.org, the internet archive and many other wonderful projects. They
have 10GigE connectivity to the internet.

Presently much of this lab has been dissembled and moved to
<link>yurtlab</link>.

IPv4, native IPv6 and 6to4 are being tested on a cluster of 7 routers, 2
switches, a pair of PDUs and a perfsonar machine, and a network
measurement box, equipped with multiple gigE and wireless-n interfaces.
There are also various other random (and growing) pieces of test gear -
olpcs, windows XP boxes, 802.11b gear, etc.

In addition to the normal core machines, there are also 2 meshed cerowrt
routers spread throughout their (very large) building, doing network
measurements as well.

All machines are in the .lab.bufferbloat.net subdomain. DNS for the lab
is served by jupiter.lab.bufferbloat.net, signed with dnssec, which is,
of course, a cerowrt router, also.

The principal public facing routers
([jupiter](http://jupiter.lab.bufferbloat.net) and
[europa](http://europa.lab.bufferbloat.net) ) are equipped with
strongswan and web and rsync servers for network measurements. Jupiter
acts as a real-world native ipv6 gateway, europa used to act as a 6to4
gateway, and is now testing quagga-re. There is also a stock netgear
router, also public-facing.

There is a native IPv6 /48 network in place behind the routers, with
quagga doing BGP multi-homing (one day). We are in the process of adding
snmp monitoring tools.

io.lab.bufferbloat.net is an x86 box equipped with multiple gigE cards
and a wireless card for comparison purposes on the same wire.

Huchra.bufferbloat.net and shipka.bufferbloat.net, in the same data
center are also in use for testing, but are used for production
purposes.

All these machines have iperf and netperf running, although not
configured the same all the time.

A [babelweb instance](http://io.lab.bufferbloat.net:8080) was used on
"io" to monitor the health of the routers.

Testlab Design
==============

All internal IP addresses are of the form: 172.29.X.Y.

For router's main addresses, Y=1 (cerowrt 3.3 and later) or Y=33. The
NETworks are the 172.29.X.Z networks they serve.

The ipv6 subnets follow a similar scheme, except in hexadecimal

2001:4f8:fff8:0X00::/56 per router, where X = the X in the ipv4 address.

<link>What's the naming scheme</link>? Some more details on the
<link>machines|testlab machines</link>

Note this document becomes inaccurate about 5 minutes after written.

See also <link>using the testlab</link>

Servers
-------

  ----------------------- -------------- -------------------- ------------- ------------------------------- -------------------------------------- -------- -------------------------------- ----------
  Name                    EXT IP         EXT IPv6             IP            NET                             MAC                                    STATUS   Purpose                          PDU PORT
  <link>Jupiter</link>    149.20.63.18   2001:4f8:3:203::2    172.29.0.33   16                                                                     UP       Cerowrt GW, primary DNS server   
  <link>Europa</link>     149.20.63.19   2001:4f8:3:203::13   172.29.1.33   22                                                                     UP       Cerowrt GW                       
  <link>Io</link>         149.20.63.20   2001:4f8:3:203::14   172.29.X.Z    UP                              Ubuntu 11.10 test/measurement server   
  <link>Carpo</link>                                                        IN progress - underconfigured   Perfsonar x86 data collection box      
  <link>Carme</link>                                                        IN progress - underconfigured   freeswitch and load generator          
  <link>Callisto</link>                                                     IN progress - underconfigured   openwrt build bot                      
  ----------------------- -------------- -------------------- ------------- ------------------------------- -------------------------------------- -------- -------------------------------- ----------

  ------------------- -- ------------- -- -- ------------ ----- -- --
  <link>Sol1</link>      172.29.0.34         Lab          PDU      
  <link>Sol2</link>      172.29.6.34         Lab Office   PDU      
  ------------------- -- ------------- -- -- ------------ ----- -- --

Clients
-------

  ---------------------------------------------------- ---- ----- ----- -------- --------- -------- ----------
  Name                                                 IP   NET   MAC   STATUS   Purpose   PDU      Assigned
  <link>Thebe</link>                                        2           UP                          
  <link>Leda</link>                                         19          UP                          
  <link>Elara</link>                                        20          UP                          
  <link>Aitne</link>                                        22          UP                 Testgw   Dtaht
  <link>Netgear-stock</link>                           21                                           
  "veryremote":http://veryremote.lab.bufferbloat.net   21                                           
  "rc6smoke":http://rc6smoke.lab.bufferbloat.net       21                                           
  ---------------------------------------------------- ---- ----- ----- -------- --------- -------- ----------

TBD
---

  ------ ---- ----- ----- ------------------------
  Name   IP   NET   MAC   STATUS
  TBD                     NETGEAR stock Firmware
  TBD                     Buffalo Stock Firmware
  ------ ---- ----- ----- ------------------------

![](attached_t.svg)
