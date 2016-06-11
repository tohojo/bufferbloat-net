
---
title: Australian IPV6 RTTs
date: 2011-03-20T22:34:05
lastmod: 2011-03-21T16:39:57
type: wiki
---
Australian IPV6 RTTs
====================

Submitted by Kim/adhoc from University of Adelaide. No native IPv6 here
at UoA, so the following are run from this Desktop over a sit tunnel to
the AARNET tunnel broker...\
TSP\_CLIENT\_ADDRESS\_IPV4=129.127.x.y\
TSP\_CLIENT\_ADDRESS\_IPV6=2001:0388:f000:0000:0000:0000:0000:1455\
TSP\_SERVER\_ADDRESS\_IPV4=202.158.196.131\
TSP\_SERVER\_ADDRESS\_IPV6=2001:0388:f000:0000:0000:0000:0000:1454

tracepath6, traceroute6 & ping6 to the following hosts;
-------------------------------------------------------

1.  shipka.bufferbloat.net
2.  backup.bufferbloat.net
3.  ipv6.gatech.edu
4.  mirror.ipv6.internode.on.net

\$ tracepath6 shipka.bufferbloat.net\
1?: \[LOCALHOST\] 0.024ms pmtu 1280\
1: 2001:388:f000::1454 27.192ms\
1: 2001:388:f000::1454 23.991ms\
2: 2001:388:1:5001::1 24.542ms asymm 3\
3: tengigabitethernet2-1.pe1.c.syd.aarnet.net.au 24.515ms\
4: 6453.syd.equinix.com 24.671ms\
5: 2405:2000:ffb0::1 93.462ms\
6: POS12-1-1.core1.TV2-Tokyo.ipv6.as6453.net 125.158ms\
7: no reply\
8: 2001:5a0:1200::35 228.456ms asymm 7\
9: 2001:5a0:1200::a 208.697ms asymm 4\
10: int-0-0-1-0.r2.sql1.isc.org 223.135ms asymm 5\
11: each2.isc.org 206.149ms reached\
Resume: pmtu 1280 hops 11 back 59

\$ traceroute6 shipka.bufferbloat.net\
traceroute to shipka.bufferbloat.net (2001:4f8:3:36::52), 30 hops max,
80 byte packets\
1 2001:388:f000::1454 (2001:388:f000::1454) 24.334 ms 24.313 ms 25.083
ms\
2 2001:388:1:5001::1 (2001:388:1:5001::1) 26.694 ms 26.685 ms 26.669 ms\
3 tengigabitethernet2-1.pe1.c.syd.aarnet.net.au
(2001:388:1:d:222:90ff:fe5f:2740) 26.967 ms 26.955 ms 27.185 ms\
4 6453.syd.equinix.com (2001:de8:6::6453:1) 26.909 ms \* \*\
5 2405:2000:ffb0::1 (2405:2000:ffb0::1) 105.621 ms \* \*\
6 POS12-1-1.core1.TV2-Tokyo.ipv6.as6453.net (2001:5a0:2200::3d) 145.881
ms 135.655 ms 136.232 ms\
7 if-15-0-0.804.core2.S9R-Singapore.ipv6.as6453.net (2001:5a0:2200::12)
247.915 ms 248.133 ms 248.105 ms\
8 2001:5a0:1200::35 (2001:5a0:1200::35) 246.706 ms 2001:5a0:1200::31
(2001:5a0:1200::31) 247.808 ms 246.678 ms\
9 2001:5a0:1200::a (2001:5a0:1200::a) 228.879 ms 229.121 ms 229.068 ms\
10 int-0-0-1-0.r2.sql1.isc.org (2001:4f8:1b:1::8:2) 228.777 ms 208.276
ms 207.700 ms\
11 each2.isc.org (2001:4f8:3:36::52) 205.339 ms 204.509 ms 205.336 ms

\$ ping6 -c 8 shipka.bufferbloat.net\
PING shipka.bufferbloat.net(each2.isc.org) 56 data bytes\
64 bytes from each2.isc.org: icmp\_seq=1 ttl=59 time=205 ms\
64 bytes from each2.isc.org: icmp\_seq=2 ttl=59 time=206 ms\
64 bytes from each2.isc.org: icmp\_seq=3 ttl=59 time=209 ms\
64 bytes from each2.isc.org: icmp\_seq=4 ttl=59 time=205 ms\
64 bytes from each2.isc.org: icmp\_seq=5 ttl=59 time=222 ms\
64 bytes from each2.isc.org: icmp\_seq=6 ttl=59 time=205 ms\
64 bytes from each2.isc.org: icmp\_seq=7 ttl=59 time=205 ms\
64 bytes from each2.isc.org: icmp\_seq=8 ttl=59 time=206 ms

--- shipka.bufferbloat.net ping statistics ---\
8 packets transmitted, 8 received, 0% packet loss, time 7008ms\
rtt min/avg/max/mdev = 205.427/208.363/222.304/5.394 ms

\$ tracepath6 backup.bufferbloat.net\
1?: \[LOCALHOST\] 0.033ms pmtu 1280\
1: 2001:388:f000::1454 48.350ms\
1: 2001:388:f000::1454 24.933ms\
2: 2001:388:1:5001::1 25.955ms asymm 3\
3: tengigabitethernet2-1.pe1.c.syd.aarnet.net.au 24.734ms\
4: 6453.syd.equinix.com 24.606ms\
5: 2405:2000:ffb0::1 93.569ms\
6: POS12-1-1.core1.TV2-Tokyo.ipv6.as6453.net 125.264ms\
7: no reply\
8: no reply\
9: 2001:5a0:1200:300::16 323.722ms asymm 18\
10: pos-1-14-0-0-cr01.sanjose.ca.ibone.comcast.net 341.039ms asymm 17\
11: pos-0-14-0-0-cr01.denver.co.ibone.comcast.net 335.282ms asymm 16\
12: no reply\
13: no reply\
14: no reply\
15: 2001:558:d0:1e::2 322.806ms asymm 20\
16: 2001:55c:62e5:6320::1 384.061ms asymm 18\
17: 2001:55c:62e5:6320:92fb:a6ff:fe85:d16c 366.462ms reached\
Resume: pmtu 1280 hops 17 back 46

\$ traceroute6 backup.bufferbloat.net\
traceroute to backup.bufferbloat.net
(2001:55c:62e5:6320:92fb:a6ff:fe85:d16c), 30 hops max, 80 byte packets\
1 2001:388:f000::1454 (2001:388:f000::1454) 23.269 ms 23.242 ms 23.225
ms\
2 2001:388:1:5001::1 (2001:388:1:5001::1) 23.637 ms 23.996 ms 23.985 ms\
3 tengigabitethernet2-1.pe1.c.syd.aarnet.net.au
(2001:388:1:d:222:90ff:fe5f:2740) 24.617 ms 24.608 ms 24.593 ms\
4 6453.syd.equinix.com (2001:de8:6::6453:1) 24.569 ms \* \*\
5 2405:2000:ffb0::1 (2405:2000:ffb0::1) 93.629 ms \* \*\
6 POS12-1-1.core1.TV2-Tokyo.ipv6.as6453.net (2001:5a0:2200::3d) 124.894
ms 123.130 ms 123.112 ms\
7 2001:5a0:1200:400::9 (2001:5a0:1200:400::9) 230.289 ms 229.382 ms
229.363 ms\
8 2001:5a0:1200:300::1 (2001:5a0:1200:300::1) 231.878 ms 229.175 ms
230.468 ms\
9 2001:5a0:1200:300::1a (2001:5a0:1200:300::1a) 321.465 ms
2001:5a0:1200:300::16 (2001:5a0:1200:300::16) 320.275 ms 321.427 ms\
10 pos-1-14-0-0-cr01.sanjose.ca.ibone.comcast.net (2001:558:0:f5c0::1)
322.872 ms 323.593 ms 320.804 ms\
11 pos-0-14-0-0-cr01.denver.co.ibone.comcast.net (2001:558:0:f560::1)
320.336 ms 320.218 ms 319.952 ms\
12 2001:558:0:f6c2::2 (2001:558:0:f6c2::2) 321.518 ms 322.593 ms 321.540
ms\
13 2001:558:d0:12::1 (2001:558:d0:12::1) 321.642 ms 321.162 ms 321.493
ms\
14 2001:558:d0:b::2 (2001:558:d0:b::2) 323.298 ms 324.036 ms 323.258 ms\
15 2001:558:d0:1e::2 (2001:558:d0:1e::2) 321.672 ms 323.016 ms 321.477
ms\
16 2001:55c:62e5:6320::1 (2001:55c:62e5:6320::1) 339.260 ms 338.168 ms
333.946 ms\
17 2001:55c:62e5:6320:92fb:a6ff:fe85:d16c
(2001:55c:62e5:6320:92fb:a6ff:fe85:d16c) 334.690 ms 337.048 ms 333.674
ms

\$ ping6 -c 8 backup.bufferbloat.net\
PING backup.bufferbloat.net(2001:55c:62e5:6320:92fb:a6ff:fe85:d16c) 56
data bytes\
From 2001:558:d0:1e::2 icmp\_seq=1 Destination unreachable: Address
unreachable\
64 bytes from 2001:55c:62e5:6320:92fb:a6ff:fe85:d16c: icmp\_seq=2 ttl=46
time=336 ms\
64 bytes from 2001:55c:62e5:6320:92fb:a6ff:fe85:d16c: icmp\_seq=3 ttl=46
time=346 ms\
64 bytes from 2001:55c:62e5:6320:92fb:a6ff:fe85:d16c: icmp\_seq=4 ttl=46
time=333 ms\
64 bytes from 2001:55c:62e5:6320:92fb:a6ff:fe85:d16c: icmp\_seq=5 ttl=46
time=337 ms\
64 bytes from 2001:55c:62e5:6320:92fb:a6ff:fe85:d16c: icmp\_seq=6 ttl=46
time=388 ms\
64 bytes from 2001:55c:62e5:6320:92fb:a6ff:fe85:d16c: icmp\_seq=7 ttl=46
time=339 ms\
64 bytes from 2001:55c:62e5:6320:92fb:a6ff:fe85:d16c: icmp\_seq=8 ttl=46
time=344 ms

--- backup.bufferbloat.net ping statistics ---\
8 packets transmitted, 7 received, +1 errors, 12% packet loss, time
7009ms\
rtt min/avg/max/mdev = 333.913/346.926/388.599/17.534 ms

\$ tracepath6 ipv6.gatech.edu\
1?: \[LOCALHOST\] 0.034ms pmtu 1280\
1: 2001:388:f000::1454 24.270ms\
1: 2001:388:f000::1454 23.696ms\
2: 2001:388:1:5001::1 24.297ms asymm 3\
3: so-0-1-0.bb1.a.hnl.aarnet.net.au 117.870ms asymm 4\
4: so-0-1-0.bb1.a.sea.aarnet.net.au 171.120ms asymm 5\
5: abilene-1-is-jmb-776.lsanca.pacificwave.net 194.801ms asymm 6\
6: 2001:468:ff:305::1 268.725ms asymm 7\
7: xe-2-3-0.0.rtr.atla.net.internet2.edu 245.626ms asymm 9\
8: 2001:468:ff:e43::2 245.984ms asymm 10\
9: 2610:148:fe00:c::2 246.676ms asymm 11\
10: no reply\
11: no reply\
12: no reply\
13: no reply\
14: no reply\
15: no reply\
16: no reply\
17: no reply\
18: no reply\
19: no reply\
20: no reply\
21: no reply\
22: no reply\
23: no reply\
24: no reply\
25: no reply\
26: no reply\
27: no reply\
28: no reply\
29: no reply\
30: no reply\
31: no reply\
Too many hops: pmtu 1280\
Resume: pmtu 1280

\$ traceroute6 ipv6.gatech.edu\
traceroute to ipv6.gatech.edu (2610:148:fd8f:d7fc:203:baff:fe8f:29d), 30
hops max, 80 byte packets\
1 2001:388:f000::1454 (2001:388:f000::1454) 24.464 ms 24.435 ms 24.413
ms\
2 2001:388:1:5001::1 (2001:388:1:5001::1) 25.081 ms 25.315 ms 25.288 ms\
3 so-0-1-0.bb1.a.hnl.aarnet.net.au (2001:388:1:1b::2) 118.217 ms 118.180
ms 118.155 ms\
4 so-0-1-0.bb1.a.sea.aarnet.net.au (2001:388:1:1c::2) 173.572 ms 173.836
ms 174.103 ms\
5 abilene-1-is-jmb-776.lsanca.pacificwave.net (2001:504:b:80::131)
195.750 ms 195.731 ms 196.031 ms\
6 2001:468:ff:305::1 (2001:468:ff:305::1) 227.375 ms 225.552 ms 225.532
ms\
7 xe-2-3-0.0.rtr.atla.net.internet2.edu (2001:468:ff:1c2::2) 243.722 ms
243.531 ms 243.515 ms\
8 2001:468:ff:e43::2 (2001:468:ff:e43::2) 243.856 ms 243.837 ms 243.818
ms\
9 2610:148:fe00:c::2 (2610:148:fe00:c::2) 244.618 ms 255.102 ms 244.395
ms\
10 \* \* \*\
11 \* \* \*\
12 \* \* \*\
13 \* \* \*\
14 \* \* \*\
15 \* \* \*\
16 \* \* \*\
17 \* \* \*\
18 \* \* \*\
19 \* \* \*\
20 \* \* \*\
21 \* \* \*\
22 \* \* \*\
23 \* \* \*\
24 \* \* \*\
25 \* \* \*\
26 \* \* \*\
27 \* \* \*\
28 \* \* \*\
29 \* \* \*\
30 \* \* \*

\$ ping6 -c 8 ipv6.gatech.edu\
PING ipv6.gatech.edu(2610:148:fd8f:d7fc:203:baff:fe8f:29d) 56 data
bytes\
64 bytes from 2610:148:fd8f:d7fc:203:baff:fe8f:29d: icmp\_seq=1 ttl=53
time=310 ms\
64 bytes from 2610:148:fd8f:d7fc:203:baff:fe8f:29d: icmp\_seq=2 ttl=53
time=246 ms\
64 bytes from 2610:148:fd8f:d7fc:203:baff:fe8f:29d: icmp\_seq=3 ttl=53
time=244 ms\
64 bytes from 2610:148:fd8f:d7fc:203:baff:fe8f:29d: icmp\_seq=4 ttl=53
time=276 ms\
64 bytes from 2610:148:fd8f:d7fc:203:baff:fe8f:29d: icmp\_seq=5 ttl=53
time=275 ms\
64 bytes from 2610:148:fd8f:d7fc:203:baff:fe8f:29d: icmp\_seq=6 ttl=53
time=244 ms\
64 bytes from 2610:148:fd8f:d7fc:203:baff:fe8f:29d: icmp\_seq=7 ttl=53
time=244 ms\
64 bytes from 2610:148:fd8f:d7fc:203:baff:fe8f:29d: icmp\_seq=8 ttl=53
time=245 ms

--- ipv6.gatech.edu ping statistics ---\
8 packets transmitted, 8 received, 0% packet loss, time 7010ms\
rtt min/avg/max/mdev = 244.758/261.173/310.789/22.894 ms

\$ tracepath6 mirror.ipv6.internode.on.net\
1?: \[LOCALHOST\] 0.034ms pmtu 1280\
1: 2001:388:f000::1454 24.640ms\
1: 2001:388:f000::1454 24.081ms\
2: 2001:388:1:5001::1 24.563ms asymm 3\
3: tengigabitethernet2-1.pe1.c.syd.aarnet.net.au 25.232ms\
4: gi0-0-226.bdr1.syd6.internode.on.net 24.765ms\
5: te0-0-0.bdr1.syd6.internode.on.net 24.455ms\
6: pos15-0-0.bdr1.adl6.internode.on.net 46.256ms\
7: gi1-17.cor3.adl2.internode.on.net 48.026ms asymm 9\
8: gi1-17.cor3.adl2.internode.on.net 54.187ms !A\
Resume: pmtu 1280

\$ traceroute6 mirror.ipv6.internode.on.net\
traceroute to mirror.ipv6.internode.on.net (2001:44b8:8020:7a80::20), 30
hops max, 80 byte packets\
1 2001:388:f000::1454 (2001:388:f000::1454) 22.918 ms 23.231 ms 23.218
ms\
2 2001:388:1:5001::1 (2001:388:1:5001::1) 23.202 ms 23.186 ms 23.472 ms\
3 tengigabitethernet2-1.pe1.c.syd.aarnet.net.au
(2001:388:1:d:222:90ff:fe5f:2740) 23.704 ms 23.693 ms 23.679 ms\
4 gi0-0-226.bdr1.syd6.internode.on.net (2001:44b8:b060:2::4739:1) 23.873
ms \* \*\
5 te0-0-0.bdr1.syd6.internode.on.net (2001:44b8:b060:1::15) 24.514 ms \*
\*\
6 pos15-0-0.bdr1.adl6.internode.on.net (2001:44b8:8060:1::9) 46.939 ms
\* \*\
7 gi1-17.cor3.adl2.internode.on.net (2001:44b8:8060:16::2) 46.309 ms
46.294 ms 46.521 ms\
8 mirror.internode.on.net (2001:44b8:8020:7a80::20) 45.757 ms 45.747 ms
45.968 ms

\$ ping6 -c 8 mirror.ipv6.internode.on.net\
PING mirror.ipv6.internode.on.net(mirror.internode.on.net) 56 data
bytes\
64 bytes from mirror.internode.on.net: icmp\_seq=1 ttl=55 time=44.9 ms\
64 bytes from mirror.internode.on.net: icmp\_seq=2 ttl=55 time=44.9 ms\
64 bytes from mirror.internode.on.net: icmp\_seq=3 ttl=55 time=71.0 ms\
64 bytes from mirror.internode.on.net: icmp\_seq=4 ttl=55 time=45.1 ms\
64 bytes from mirror.internode.on.net: icmp\_seq=5 ttl=55 time=45.3 ms\
64 bytes from mirror.internode.on.net: icmp\_seq=6 ttl=55 time=50.7 ms\
64 bytes from mirror.internode.on.net: icmp\_seq=7 ttl=55 time=45.9 ms\
64 bytes from mirror.internode.on.net: icmp\_seq=8 ttl=55 time=60.2 ms

--- mirror.ipv6.internode.on.net ping statistics ---\
8 packets transmitted, 8 received, 0% packet loss, time 7010ms\
rtt min/avg/max/mdev = 44.912/51.036/71.015/9.025 ms

TODO; Please add more paths to trace to and I'll add them here.
