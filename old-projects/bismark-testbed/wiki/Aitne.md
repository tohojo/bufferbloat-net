
---
title: Aitne
date: 2011-05-28T22:56:05
lastmod: 2011-05-28T23:07:53
type: wiki
---
Aitne
=====

Aitne is presently unconfigured as a bridge, doing pure routing and QoS
between <link>metis</link> and the <link>testlab</link>.

The openwrt bridge code was assigning a mac address to the first
wireless\
interface that was the same as the ethernet interface, thus messing up
normal routing.

This problem prevents the device from working properly in unbridged
mode.

So a semi-random MAC has been assigned. The wireless has been entirely
disabled...

It is possible there IS no official mac assigned to the ethernet
interface

Even with a semi-random mac,

unreachable 192.168.24.0/24 proto babel metric -1 onlink\
default via 130.207.97.1 dev eth1\
dtaht@metis:\~\$\
dtaht@metis:\~\$ ping 192.168.130.1\
connect: Network is unreachable

dtaht@metis:\~\$ ip route\
192.168.130.0/24 dev eth0 proto kernel scope link src 192.168.130.2\
130.207.97.0/24 dev eth1 proto kernel scope link src 130.207.97.23\
default via 130.207.97.1 dev eth1\
dtaht@metis:\~\$ arp -a\
-bash: arp: command not found\
dtaht@metis:\~\$ /sbin/![]()\
/sbin/arp -a\
-bash: /sbin/arp: No such file or directory\
dtaht@metis:\~\$ /usr/sbin/arp -a\
\^C

eth0 Link encap:Ethernet HWaddr C4:3D:C7:B0:AE:36\
inet addr:192.168.130.1 Bcast:192.168.130.255 Mask:255.255.255.0\
inet6 addr: fe80::c63d:c7ff:feb0:ae36/64 Scope:Link\
UP BROADCAST RUNNING MULTICAST MTU:1500 Metric:1\
RX packets:62 errors:0 dropped:53 overruns:0 frame:0\
TX packets:6 errors:0 dropped:0 overruns:0 carrier:0\
collisions:0 txqueuelen:16\
RX bytes:6110 (5.9 KiB) TX bytes:1521 (1.4 KiB)\
Interrupt:4
