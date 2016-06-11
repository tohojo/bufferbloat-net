
---
title: Experiment - QoS
date: 2011-05-28T10:11:51
lastmod: 2011-05-29T09:20:08
type: wiki
---
Experiment - QoS
================

Here is an example of QoS doing it's job, with a setting of 1Mbit\
using pdsh to control the testbed in the <link>testlab</link>
------------------------------------------------------------------

(this is also a demonstration on how to use <link>pdsh</link>
effectively)

pdsh -lroot -grouters 'iperf -w 1M -t 60 -c metis.noise.gatech.edu'

Aitne, in this case, is applying QoS to the other routers, and also
participating in the test.

`aitne: [ ID] Interval       Transfer     Bandwidth
aitne: [  3]  0.0-60.0 sec   773 MBytes   108 Mbits/sec
leda: [ ID] Interval       Transfer     Bandwidth
leda: [  3]  0.0-60.2 sec  1.75 MBytes   244 Kbits/sec
elara: [ ID] Interval       Transfer     Bandwidth
elara: [  3]  0.0-63.2 sec  1.88 MBytes   249 Kbits/sec
io: [ ID] Interval       Transfer     Bandwidth
io: [  3]  0.0-64.2 sec  1.88 MBytes   245 Kbits/sec
thebe: [ ID] Interval       Transfer     Bandwidth
thebe: [  3]  0.0-62.8 sec  1.75 MBytes   234 Kbits/sec`

Let's disable QoS on Aitne, temporarily:
----------------------------------------

ssh -lroot aitne 'PATH=/usr/bin:/bin:/sbin:/usr/sbin /etc/init.d/qos
stop'

And re-run the test, this time with a huge (220k) window...

`pdsh -lroot -grouters 'iperf -w 1M -t 60 -c metis.noise.gatech.edu'`

This hangs! And...

`root`metis:/home/dtaht\# ip route\
unreachable 172.16.22.1 proto babel metric -1 onlink\
unreachable 192.168.115.186 proto babel metric -1 onlink\
unreachable 172.16.23.1 proto babel metric -1 onlink\
unreachable 192.168.115.171 proto babel metric -1 onlink\
unreachable 143.215.131.240 proto babel metric -1 onlink\
unreachable 192.168.34.1 proto babel metric -1 onlink\
192.168.134.1 via 192.168.132.1 dev eth0 proto babel onlink\
unreachable 192.168.32.1 proto babel metric -1 onlink\
192.168.133.1 via 192.168.132.1 dev eth0 proto babel onlink\
unreachable 130.207.97.22 proto babel metric -1 onlink\
unreachable 192.168.33.1 proto babel metric -1 onlink\
192.168.132.1 via 192.168.132.1 dev eth0 proto babel onlink\
unreachable 192.168.22.216 proto babel metric -1 onlink\
unreachable 192.168.110.1 proto babel metric -1 onlink\
unreachable 192.168.22.223 proto babel metric -1 onlink\
unreachable 192.168.111.1 proto babel metric -1 onlink\
unreachable 172.16.23.105 proto babel metric -1 onlink\
unreachable 172.16.23.110 proto babel metric -1 onlink\
unreachable 192.168.105.1 proto babel metric -1 onlink\
unreachable 192.168.106.1 proto babel metric -1 onlink\
unreachable 172.16.23.115 proto babel metric -1 onlink\
unreachable 192.168.107.1 proto babel metric -1 onlink\
unreachable 192.168.116.1 proto babel metric -1 onlink\
unreachable 192.168.23.1 proto babel metric -1 onlink\
unreachable 192.168.117.1 proto babel metric -1 onlink\
unreachable 192.168.22.1 proto babel metric -1 onlink\
unreachable 192.168.112.1 proto babel metric -1 onlink\
unreachable 192.168.22.32 proto babel metric -1 onlink\
unreachable 192.168.115.1 proto babel metric -1 onlink\
unreachable 192.168.120.1 proto babel metric -1 onlink\
unreachable 192.168.121.1 proto babel metric -1 onlink\
unreachable 172.16.23.254 proto babel metric -1 onlink\
unreachable 172.16.22.254 proto babel metric -1 onlink\
unreachable 192.168.24.1 proto babel metric -1 onlink\
unreachable 192.168.116.0/24 proto babel metric -1 onlink\
unreachable 192.168.23.0/24 proto babel metric -1 onlink\
unreachable 172.16.22.0/24 proto babel metric -1 onlink\
unreachable 192.168.117.0/24 proto babel metric -1 onlink\
unreachable 192.168.22.0/24 proto babel metric -1 onlink\
unreachable 172.16.23.0/24 proto babel metric -1 onlink\
unreachable 192.168.112.0/24 proto babel metric -1 onlink\
130.207.97.0/24 dev eth1 proto kernel scope link src 130.207.97.23\
unreachable 192.168.115.0/24 proto babel metric -1 onlink\
192.168.132.0/24 dev eth0 proto kernel scope link src 192.168.132.240\
unreachable 192.168.110.0/24 proto babel metric -1 onlink\
unreachable 192.168.111.0/24 proto babel metric -1 onlink\
unreachable 192.168.105.0/24 proto babel metric -1 onlink\
unreachable 192.168.106.0/24 proto babel metric -1 onlink\
unreachable 192.168.107.0/24 proto babel metric -1 onlink\
unreachable 192.168.24.0/24 proto babel metric -1 onlink\
default via 130.207.97.1 dev eth1 @

**Wow** what happened? The routing tables got blown up on metis.

Even on aitne, they vanished.

root@aitne:\~\# ip route\
192.168.132.240 via 192.168.132.240 dev br-lan proto 42 onlink\
130.207.97.23 via 192.168.132.240 dev br-lan proto 42 onlink\
192.168.134.0/24 dev wlan4 proto kernel scope link src 192.168.134.1\
192.168.133.0/24 dev wlan1 proto kernel scope link src 192.168.133.1\
192.168.132.0/24 dev br-lan proto kernel scope link src 192.168.132.1@

Obviously we induced a problem with the routing by flooding the network.

After a few minutes the network recovers...\
@\
172.16.22.1 via 192.168.132.1 dev eth0 proto babel onlink\
192.168.115.186 via 192.168.132.1 dev eth0 proto babel onlink\
172.16.23.1 via 192.168.132.1 dev eth0 proto babel onlink\
192.168.115.171 via 192.168.132.1 dev eth0 proto babel onlink\
143.215.131.240 via 192.168.132.1 dev eth0 proto babel onlink\
192.168.34.1 via 192.168.132.1 dev eth0 proto babel onlink\
192.168.134.1 via 192.168.132.1 dev eth0 proto babel onlink\
192.168.32.1 via 192.168.132.1 dev eth0 proto babel onlink\
192.168.133.1 via 192.168.132.1 dev eth0 proto babel onlink\
130.207.97.22 via 192.168.132.1 dev eth0 proto babel onlink\
192.168.33.1 via 192.168.132.1 dev eth0 proto babel onlink\
192.168.132.1 via 192.168.132.1 dev eth0 proto babel onlink\
192.168.22.216 via 192.168.132.1 dev eth0 proto babel onlink\
192.168.110.1 via 192.168.132.1 dev eth0 proto babel onlink\
192.168.22.223 via 192.168.132.1 dev eth0 proto babel onlink\
192.168.111.1 via 192.168.132.1 dev eth0 proto babel onlink\
172.16.23.105 via 192.168.132.1 dev eth0 proto babel onlink\
172.16.23.110 via 192.168.132.1 dev eth0 proto babel onlink\
192.168.105.1 via 192.168.132.1 dev eth0 proto babel onlink\
192.168.106.1 via 192.168.132.1 dev eth0 proto babel onlink\
172.16.23.115 via 192.168.132.1 dev eth0 proto babel onlink\
192.168.107.1 via 192.168.132.1 dev eth0 proto babel onlink\
192.168.116.1 via 192.168.132.1 dev eth0 proto babel onlink\
192.168.23.1 via 192.168.132.1 dev eth0 proto babel onlink\
192.168.117.1 via 192.168.132.1 dev eth0 proto babel onlink\
192.168.22.1 via 192.168.132.1 dev eth0 proto babel onlink\
192.168.112.1 via 192.168.132.1 dev eth0 proto babel onlink\
192.168.22.32 via 192.168.132.1 dev eth0 proto babel onlink\
192.168.115.1 via 192.168.132.1 dev eth0 proto babel onlink\
192.168.120.1 via 192.168.132.1 dev eth0 proto babel onlink\
192.168.121.1 via 192.168.132.1 dev eth0 proto babel onlink\
172.16.23.254 via 192.168.132.1 dev eth0 proto babel onlink\
172.16.22.254 via 192.168.132.1 dev eth0 proto babel onlink\
192.168.24.1 via 192.168.132.1 dev eth0 proto babel onlink\
192.168.116.0/24 via 192.168.132.1 dev eth0 proto babel onlink\
192.168.23.0/24 via 192.168.132.1 dev eth0 proto babel onlink\
172.16.22.0/24 via 192.168.132.1 dev eth0 proto babel onlink\
192.168.117.0/24 via 192.168.132.1 dev eth0 proto babel onlink\
192.168.22.0/24 via 192.168.132.1 dev eth0 proto babel onlink\
172.16.23.0/24 via 192.168.132.1 dev eth0 proto babel onlink\
192.168.112.0/24 via 192.168.132.1 dev eth0 proto babel onlink\
130.207.97.0/24 dev eth1 proto kernel scope link src 130.207.97.23\
192.168.115.0/24 via 192.168.132.1 dev eth0 proto babel onlink\
192.168.132.0/24 dev eth0 proto kernel scope link src 192.168.132.240\
192.168.110.0/24 via 192.168.132.1 dev eth0 proto babel onlink\
192.168.111.0/24 via 192.168.132.1 dev eth0 proto babel onlink\
192.168.105.0/24 via 192.168.132.1 dev eth0 proto babel onlink\
192.168.106.0/24 via 192.168.132.1 dev eth0 proto babel onlink\
192.168.107.0/24 via 192.168.132.1 dev eth0 proto babel onlink\
192.168.24.0/24 via 192.168.132.1 dev eth0 proto babel onlink\
default via 130.207.97.1 dev eth1@

Let's do that again! This time...

Let's drop aitne out of the test here, leave QoS on, and just try the routers.
------------------------------------------------------------------------------

`pdsh -lroot -grouters -xaitne 'iperf -w 1M -t 60 -c metis.noise.gatech.edu'`

`elara: [ ID] Interval       Transfer     Bandwidth
elara: [  3]  0.0-60.0 sec  1.75 MBytes   245 Kbits/sec
io: [ ID] Interval       Transfer     Bandwidth
io: [  3]  0.0-61.1 sec  1.75 MBytes   240 Kbits/sec
thebe: [ ID] Interval       Transfer     Bandwidth
thebe: [  3]  0.0-64.1 sec  1.75 MBytes   229 Kbits/sec
leda: [ ID] Interval       Transfer     Bandwidth
leda: [  3]  0.0-62.7 sec  1.75 MBytes   234 Kbits/sec`

OK, let's disable QoS again on aitne and see what happens, making sure
it's dead:

`root`aitne:\~\# /etc/init.d/qos stop\
root@aitne:\~\# tc qdisc\
qdisc pfifo\_fast 0: dev eth0 root refcnt 2 bands 3 priomap 1 2 2 2 1 2
0 0 1 1 1 1 1 1 1 1\
qdisc pfifo\_fast 0: dev eth1 root refcnt 2 bands 3 priomap 1 2 2 2 1 2
0 0 1 1 1 1 1 1 1 1\
qdisc mq 0: dev wlan0 root\
qdisc mq 0: dev wlan2 root\
qdisc mq 0: dev mon.wlan0 root\
qdisc mq 0: dev wlan1 root\
qdisc mq 0: dev wlan3 root\
qdisc mq 0: dev wlan5 root\
qdisc mq 0: dev mon.wlan3 root\
qdisc mq 0: dev wlan4 root\
qdisc pfifo\_fast 0: dev ifb0 root refcnt 2 bands 3 priomap 1 2 2 2 1 2
0 0 1 1 1 1 1 1 1 1@

OK, lets watch it go boom... maybe... with a 10 second test. wow. thebe
gets starved, and it takes forever to connect to leda.

`pdsh -lroot -grouters -xaitne 'iperf -w 1M -t 10 -c metis.noise.gatech.edu'`

`elara: [ ID] Interval       Transfer     Bandwidth
elara: [  3]  0.0-10.0 sec  74.4 MBytes  62.4 Mbits/sec
io: [ ID] Interval       Transfer     Bandwidth
io: [  3]  0.0-10.0 sec  49.3 MBytes  41.3 Mbits/sec
thebe: [ ID] Interval       Transfer     Bandwidth
thebe: [  3]  0.0-13.4 sec   384 KBytes   234 Kbits/sec
leda: ------------------------------------------------------------
leda: Client connecting to metis.noise.gatech.edu, TCP port 5001
leda: TCP window size:  220 KByte (WARNING: requested 1.00 MByte)
leda: ------------------------------------------------------------
leda: [  3] local 192.168.115.1 port 39834 connected with 130.207.97.23 port 5001
leda: [ ID] Interval       Transfer     Bandwidth
leda: [  3]  0.0-10.0 sec   109 MBytes  90.9 Mbits/sec`

Let's rerun that for 60 seconds instead, while pinging... KABOOM!

`root`metis:/home/dtaht\# ping jupiter\
PING jupiter (192.168.22.1) 56(84) bytes of data.\
From metis.local (192.168.132.240) icmp\_seq=1 Destination Host
Unreachable\
From metis.local (192.168.132.240) icmp\_seq=2 Destination Host
Unreachable\
From metis.local (192.168.132.240) icmp\_seq=3 Destination Host
Unreachable\
From metis.local (192.168.132.240) icmp\_seq=4 Destination Host
Unreachable\
From metis.local (192.168.132.240) icmp\_seq=5 Destination Host
Unreachable\
From metis.local (192.168.132.240) icmp\_seq=6 Destination Host
Unreachable\
From metis.local (192.168.132.240) icmp\_seq=7 Destination Host
Unreachable\
From metis.local (192.168.132.240) icmp\_seq=8 Destination Host
Unreachable\
From metis.local (192.168.132.240) icmp\_seq=9 Destination Host
Unreachable@

And the routes have disappeared again:

`root`metis:/home/dtaht\# ip route\
unreachable 172.16.22.1 proto babel metric -1 onlink\
unreachable 192.168.115.186 proto babel metric -1 onlink\
unreachable 172.16.23.1 proto babel metric -1 onlink\
unreachable 192.168.115.171 proto babel metric -1 onlink\
unreachable 143.215.131.240 proto babel metric -1 onlink\
unreachable 192.168.34.1 proto babel metric -1 onlink\
unreachable 192.168.134.1 proto babel metric -1 onlink\
unreachable 192.168.32.1 proto babel metric -1 onlink\
unreachable 192.168.133.1 proto babel metric -1 onlink\
unreachable 130.207.97.22 proto babel metric -1 onlink\
unreachable 192.168.33.1 proto babel metric -1 onlink\
unreachable 192.168.132.1 proto babel metric -1 onlink\
unreachable 192.168.22.216 proto babel metric -1 onlink\
unreachable 192.168.110.1 proto babel metric -1 onlink\
unreachable 192.168.22.223 proto babel metric -1 onlink\
unreachable 192.168.111.1 proto babel metric -1 onlink\
unreachable 172.16.23.105 proto babel metric -1 onlink\
unreachable 172.16.23.110 proto babel metric -1 onlink\
unreachable 192.168.105.1 proto babel metric -1 onlink\
unreachable 192.168.106.1 proto babel metric -1 onlink\
unreachable 172.16.23.115 proto babel metric -1 onlink\
unreachable 192.168.107.1 proto babel metric -1 onlink\
unreachable 192.168.116.1 proto babel metric -1 onlink\
unreachable 192.168.23.1 proto babel metric -1 onlink\
unreachable 192.168.117.1 proto babel metric -1 onlink\
unreachable 192.168.22.1 proto babel metric -1 onlink\
unreachable 192.168.112.1 proto babel metric -1 onlink\
unreachable 192.168.22.32 proto babel metric -1 onlink\
unreachable 192.168.115.1 proto babel metric -1 onlink\
unreachable 192.168.120.1 proto babel metric -1 onlink\
unreachable 192.168.121.1 proto babel metric -1 onlink\
unreachable 172.16.23.254 proto babel metric -1 onlink\
unreachable 172.16.22.254 proto babel metric -1 onlink\
unreachable 192.168.24.1 proto babel metric -1 onlink\
unreachable 192.168.116.0/24 proto babel metric -1 onlink\
unreachable 192.168.23.0/24 proto babel metric -1 onlink\
unreachable 172.16.22.0/24 proto babel metric -1 onlink\
unreachable 192.168.117.0/24 proto babel metric -1 onlink\
unreachable 192.168.22.0/24 proto babel metric -1 onlink\
unreachable 172.16.23.0/24 proto babel metric -1 onlink\
unreachable 192.168.112.0/24 proto babel metric -1 onlink\
130.207.97.0/24 dev eth1 proto kernel scope link src 130.207.97.23\
unreachable 192.168.115.0/24 proto babel metric -1 onlink\
192.168.132.0/24 dev eth0 proto kernel scope link src 192.168.132.240\
unreachable 192.168.110.0/24 proto babel metric -1 onlink\
unreachable 192.168.111.0/24 proto babel metric -1 onlink\
unreachable 192.168.105.0/24 proto babel metric -1 onlink\
unreachable 192.168.106.0/24 proto babel metric -1 onlink\
unreachable 192.168.107.0/24 proto babel metric -1 onlink\
unreachable 192.168.24.0/24 proto babel metric -1 onlink\
default via 130.207.97.1 dev eth1 @

Obviously, we have a problem here, that only happens under heavy load.
It may be multicast packets being dropped or overly delayed, it may be
excessive packet queuing in the switch, it may be anything... it may be
bufferbloat, it may be a need for ECN...

Wait 2 minutes for the network to recover... still waiting... might need
to reboot stuff... Finally get back on, iperf is hung on leda...

I can also conclude that some level of QoS is needed on the internal
network.

Let's blow this up ONE MORE TIME
--------------------------------

Iperf was hung on leda, so let's make sure it's dead everywhere:

`pdsh -lroot -grouters 'killall iperf'`

And reduce txqueuelen on metis

`ifconfig eth0 txqueuelen 4`

A reference ping to jupiter:

64 bytes from jupiter (192.168.22.1): icmp\_req=8 ttl=62 time=0.839 ms\
64 bytes from jupiter (192.168.22.1): icmp\_req=9 ttl=62 time=0.715 ms

And fire up the test

`pdsh -lroot -grouters -xaitne 'iperf -w 1M -t 10 -c metis.noise.gatech.edu'`

io: \[ ID\] Interval Transfer Bandwidth\
io: \[ 3\] 0.0-60.9 sec 1.75 MBytes 241 Kbits/sec\
thebe: \[ ID\] Interval Transfer Bandwidth\
thebe: \[ 3\] 0.0-61.0 sec 1.75 MBytes 241 Kbits/sec\
elara: \[ ID\] Interval Transfer Bandwidth\
elara: \[ 3\] 0.0-64.1 sec 1.75 MBytes 229 Kbits/sec\
leda: \[ ID\] Interval Transfer Bandwidth\
leda: \[ 3\] 0.0-62.5 sec 1.88 MBytes 252 Kbits/sec

Wow, during the test, ping jitters all over the place and is enormous!

64 bytes from jupiter (192.168.22.1): icmp\_req=15 ttl=62 time=124 ms\
64 bytes from jupiter (192.168.22.1): icmp\_req=16 ttl=62 time=109 ms\
64 bytes from jupiter (192.168.22.1): icmp\_req=17 ttl=62 time=110 ms\
64 bytes from jupiter (192.168.22.1): icmp\_req=19 ttl=62 time=137 ms\
64 bytes from jupiter (192.168.22.1): icmp\_req=20 ttl=62 time=174 ms\
64 bytes from jupiter (192.168.22.1): icmp\_req=21 ttl=62 time=103 ms\
64 bytes from jupiter (192.168.22.1): icmp\_req=24 ttl=62 time=99.1 ms\
64 bytes from jupiter (192.168.22.1): icmp\_req=25 ttl=62 time=149 ms\
64 bytes from jupiter (192.168.22.1): icmp\_req=26 ttl=62 time=119 ms\
64 bytes from jupiter (192.168.22.1): icmp\_req=27 ttl=62 time=170 ms\
64 bytes from jupiter (192.168.22.1): icmp\_req=29 ttl=62 time=115 ms\
64 bytes from jupiter (192.168.22.1): icmp\_req=30 ttl=62 time=165 ms\
64 bytes from jupiter (192.168.22.1): icmp\_req=31 ttl=62 time=108 ms\
64 bytes from jupiter (192.168.22.1): icmp\_req=32 ttl=62 time=172 ms\
64 bytes from jupiter (192.168.22.1): icmp\_req=33 ttl=62 time=142 ms\
64 bytes from jupiter (192.168.22.1): icmp\_req=34 ttl=62 time=112 ms\
64 bytes from jupiter (192.168.22.1): icmp\_req=35 ttl=62 time=135 ms\
64 bytes from jupiter (192.168.22.1): icmp\_req=37 ttl=62 time=176 ms\
64 bytes from jupiter (192.168.22.1): icmp\_req=38 ttl=62 time=146 ms

But it survives, and we have ping packet loss.

--- jupiter ping statistics ---\
136 packets transmitted, 124 received, 8% packet loss, time 135142ms\
rtt min/avg/max/mdev = 0.706/57.325/176.773/65.420 ms

So we have buffering either in metis's driver, or the switch, that is in
EXCESS of 100ms, on a network\
that should have gigE capability, but appears to be running only at
100Mbit, through the router.

Two followups while running iperf
---------------------------------

### Finding where the overbuffering is:

pinging from metis, through aitne, through leda, to io.

64 bytes from io (192.168.110.1): icmp\_req=23 ttl=62 time=186 ms\
64 bytes from io (192.168.110.1): icmp\_req=24 ttl=62 time=116 ms\
64 bytes from io (192.168.110.1): icmp\_req=25 ttl=62 time=154 ms\
64 bytes from io (192.168.110.1): icmp\_req=26 ttl=62 time=150 ms\
64 bytes from io (192.168.110.1): icmp\_req=27 ttl=62 time=161 ms\
\^C\
--- io ping statistics ---\
27 packets transmitted, 24 received, 11% packet loss, time 26031ms\
rtt min/avg/max/mdev = 0.702/95.733/186.610/64.807 ms

root@metis:/home/dtaht\# traceroute io\
traceroute to io (192.168.110.1), 30 hops max, 60 byte packets\
1 aitne (192.168.132.1) 0.192 ms 0.242 ms 0.273 ms\
2 leda (192.168.115.1) 137.086 ms 137.955 ms 138.789 ms\
3 io (192.168.110.1) 139.734 ms 140.623 ms 141.460 ms\
root@metis:/home/dtaht\# ping leda

64 bytes from leda (192.168.115.1): icmp\_req=1 ttl=63 time=130 ms\
64 bytes from leda (192.168.115.1): icmp\_req=2 ttl=63 time=127 ms\
64 bytes from leda (192.168.115.1): icmp\_req=3 ttl=63 time=165 ms\
\^C\
--- leda ping statistics ---\
3 packets transmitted, 3 received, 0% packet loss, time 2001ms\
rtt min/avg/max/mdev = 127.337/140.934/165.281/17.257 ms\
root@metis:/home/dtaht\# ping aitne\
PING aitne (192.168.132.1) 56(84) bytes of data.\
64 bytes from aitne (192.168.132.1): icmp\_req=1 ttl=64 time=0.208 ms\
64 bytes from aitne (192.168.132.1): icmp\_req=2 ttl=64 time=0.206 ms\
64 bytes from aitne (192.168.132.1): icmp\_req=3 ttl=64 time=0.225 ms

### OK, so lets try aitne to io, through leda:

root@aitne:\~\# ping 192.168.110.1\
PING 192.168.110.1 (192.168.110.1): 56 data bytes\
64 bytes from 192.168.110.1: seq=0 ttl=63 time=141.142 ms\
64 bytes from 192.168.110.1: seq=1 ttl=63 time=165.623 ms\
64 bytes from 192.168.110.1: seq=2 ttl=63 time=109.392 ms\
64 bytes from 192.168.110.1: seq=3 ttl=63 time=174.408 ms\
64 bytes from 192.168.110.1: seq=5 ttl=63 time=155.456 ms\
64 bytes from 192.168.110.1: seq=6 ttl=63 time=126.857 ms\
64 bytes from 192.168.110.1: seq=7 ttl=63 time=124.508 ms

Wow. OK, so we have buffering going on at the sources of the tests (the
two routers) that is insane.

Let's blow 'em up again... Let's make sure qos is dead everywhere, and
blow up the network again.

Make sure Qos is gone

`pdsh -lroot -grouters 'PATH=/usr/bin:/bin:/sbin:/usr/sbin tc qdisc'`

Start the test, as before...

It knocks aitne offline immediately!

root@aitne:\~\# ping 192.168.110.1

64 bytes from 192.168.110.1: seq=264 ttl=63 time=0.571 ms\
64 bytes from 192.168.110.1: seq=265 ttl=63 time=0.555 ms\
64 bytes from 192.168.110.1: seq=266 ttl=63 time=0.596 ms

Started the test here, before the next ping went out, aitne stopped
working entirely.

Eventually the ssh session on aitne broke:

Write failed: Broken pipe

unreachable 192.168.106.0/24 proto babel metric -1 onlink\
unreachable 192.168.107.0/24 proto babel metric -1 onlink\
unreachable 192.168.24.0/24 proto babel metric -1 onlink

I think this demonstrates any one or several possible problems.

1.  There is most likely truly excessive buffering in the switch (the
    driver was somewhat debloated)
2.  Some form of fair queuing above and beyond the pfifo\_fast qdisc is
    needed (nagle, 89) on internal ethernet interfaces
3.  There may be problems with connection tracking or iptables - after a
    lockup, ssh drops, but it can be restarted
4.  Multicast packets fail under heavy load
5.  these routers may have a driver issue in general
6.  Some form of fair queuing seems desirable on the switch, too.
7.  Bufferbloat SUCKS

Testing with packet captures is needed.

See also:

http://metis.noise.gatech.edu/cacti/graph\_view.php?action=preview&host\_id=3&graph\_template\_id=0&filter=\
login and password of guest

Some background info
--------------------

The routing interface is set to 5.

thebe:\
dtaht@metis:\~\$ pdsh -lroot -grouters '/sbin/ifconfig eth1' | grep
txqueuelen\
aitne: collisions:0 txqueuelen:5\
io: collisions:0 txqueuelen:5\
leda: collisions:0 txqueuelen:5\
elara: collisions:0 txqueuelen:5\
thebe: collisions:0 txqueuelen:5

no errors were reported, either.

The internal interfaces are set to 16

dtaht@metis:\~\$ pdsh -lroot -grouters '/sbin/ifconfig eth0' | grep
txqueuelen\
aitne: collisions:0 txqueuelen:16\
elara: collisions:0 txqueuelen:16\
thebe: collisions:0 txqueuelen:16\
io: collisions:0 txqueuelen:16\
leda: collisions:0 txqueuelen:16

a `pdsh -lroot -grouters '/sbin/logread | tail -20'`

was unrevealing, as was dmesg.

Future directions
-----------------

Repeat tests with a smaller MSS size\
Repeat tests with a smaller window\
Repeat tests with instrumentation\
Repeat tests with latest build\
Repeat tests with a larger txqueuelen\
Repeat tests with wireless\
Repeat tests with simplified QoS\
Repeat tests without babel\
Repeat tests without vlan - THIS WORKED - see last entry

Repeat test with QoS on aitne set to 100Mbit or 90Mbit (crashes)\
60Mbits works, with ping times in the 40 to 50 ms range
-----------------------------------------------------------------

elara: \[ ID\] Interval Transfer Bandwidth\
elara: \[ 3\] 0.0-60.0 sec 135 MBytes 18.9 Mbits/sec\
io: \[ ID\] Interval Transfer Bandwidth\
io: \[ 3\] 0.0-60.0 sec 105 MBytes 14.7 Mbits/sec\
leda: \[ ID\] Interval Transfer Bandwidth\
leda: \[ 3\] 0.0-60.0 sec 80.3 MBytes 11.2 Mbits/sec\
thebe: \[ ID\] Interval Transfer Bandwidth\
thebe: \[ 3\] 0.0-60.1 sec 86.4 MBytes 12.1 Mbits/sec

Repeat with 16k window size and no QoS
--------------------------------------

Works:

elara: \[ ID\] Interval Transfer Bandwidth\
elara: \[ 3\] 0.0-60.0 sec 225 MBytes 31.4 Mbits/sec\
thebe: \[ ID\] Interval Transfer Bandwidth\
thebe: \[ 3\] 0.0-60.0 sec 33.9 MBytes 4.73 Mbits/sec\
io: \[ ID\] Interval Transfer Bandwidth\
io: \[ 3\] 0.0-60.0 sec 168 MBytes 23.5 Mbits/sec\
leda: \[ ID\] Interval Transfer Bandwidth\
leda: \[ 3\] 0.0-61.0 sec 278 MBytes 38.3 Mbits/sec

We survive, but this is crazy

64 bytes from 192.168.22.1: seq=31 ttl=63 time=0.547 ms\
64 bytes from 192.168.22.1: seq=32 ttl=63 time=155.124 ms\
64 bytes from 192.168.22.1: seq=33 ttl=63 time=1.414 ms\
64 bytes from 192.168.22.1: seq=34 ttl=63 time=3.404 ms\
64 bytes from 192.168.22.1: seq=35 ttl=63 time=2.137 ms\
64 bytes from 192.168.22.1: seq=36 ttl=63 time=150.703 ms\
64 bytes from 192.168.22.1: seq=37 ttl=63 time=1.528 ms\
64 bytes from 192.168.22.1: seq=38 ttl=63 time=0.667 ms\
64 bytes from 192.168.22.1: seq=39 ttl=63 time=4.756 ms\
64 bytes from 192.168.22.1: seq=40 ttl=63 time=0.636 ms\
64 bytes from 192.168.22.1: seq=41 ttl=63 time=23.574 ms\
64 bytes from 192.168.22.1: seq=42 ttl=63 time=4.236 ms\
64 bytes from 192.168.22.1: seq=43 ttl=63 time=0.830 ms\
64 bytes from 192.168.22.1: seq=44 ttl=63 time=0.595 ms\
64 bytes from 192.168.22.1: seq=45 ttl=63 time=39.417 ms\
64 bytes from 192.168.22.1: seq=46 ttl=63 time=1.269 ms\
64 bytes from 192.168.22.1: seq=47 ttl=63 time=0.881 ms\
64 bytes from 192.168.22.1: seq=48 ttl=63 time=3.035 ms\
64 bytes from 192.168.22.1: seq=50 ttl=63 time=476.244 ms\
64 bytes from 192.168.22.1: seq=51 ttl=63 time=6.557 ms\
64 bytes from 192.168.22.1: seq=52 ttl=63 time=124.569 ms\
64 bytes from 192.168.22.1: seq=53 ttl=63 time=0.665 ms\
64 bytes from 192.168.22.1: seq=54 ttl=63 time=2.205 ms

64kb window size
----------------

elara: \[ ID\] Interval Transfer Bandwidth\
elara: \[ 3\] 0.0-60.2 sec 221 MBytes 30.8 Mbits/sec\
io: \[ ID\] Interval Transfer Bandwidth\
io: \[ 3\] 0.0-60.1 sec 173 MBytes 24.1 Mbits/sec\
leda: \[ ID\] Interval Transfer Bandwidth\
leda: \[ 3\] 0.0-60.0 sec 288 MBytes 40.2 Mbits/sec\
thebe: \[ ID\] Interval Transfer Bandwidth\
thebe: \[ 3\] 0.0-60.2 sec 30.3 MBytes 4.22 Mbits/sec

64 bytes from 192.168.22.1: seq=178 ttl=63 time=1.758 ms\
64 bytes from 192.168.22.1: seq=179 ttl=63 time=3.140 ms\
64 bytes from 192.168.22.1: seq=180 ttl=63 time=1.052 ms\
64 bytes from 192.168.22.1: seq=181 ttl=63 time=1.021 ms\
64 bytes from 192.168.22.1: seq=182 ttl=63 time=6.305 ms\
64 bytes from 192.168.22.1: seq=183 ttl=63 time=0.737 ms\
64 bytes from 192.168.22.1: seq=184 ttl=63 time=17.062 ms\
64 bytes from 192.168.22.1: seq=185 ttl=63 time=11.222 ms\
64 bytes from 192.168.22.1: seq=186 ttl=63 time=26.823 ms\
64 bytes from 192.168.22.1: seq=187 ttl=63 time=1.043 ms\
64 bytes from 192.168.22.1: seq=188 ttl=63 time=29.655 ms\
64 bytes from 192.168.22.1: seq=189 ttl=63 time=8.440 ms\
64 bytes from 192.168.22.1: seq=190 ttl=63 time=1.943 ms\
64 bytes from 192.168.22.1: seq=191 ttl=63 time=0.565 ms\
64 bytes from 192.168.22.1: seq=192 ttl=63 time=4.093 ms\
64 bytes from 192.168.22.1: seq=193 ttl=63 time=3.671 ms\
64 bytes from 192.168.22.1: seq=194 ttl=63 time=52.116 ms\
64 bytes from 192.168.22.1: seq=195 ttl=63 time=5.638 ms

### greater than 64k window size

boom.

Bridging disabled on the vlan interface (no wireless)
-----------------------------------------------------

After fixing \#186 ...

### Qos set to 60Mbit on aitne, 128k window size

pdsh -lroot -grouters -xaitne 'iperf -w128k -t 60 -c
metis.noise.gatech.edu'

thebe: \[ ID\] Interval Transfer Bandwidth\
thebe: \[ 3\] 0.0-60.0 sec 85.3 MBytes 11.9 Mbits/sec\
elara: \[ ID\] Interval Transfer Bandwidth\
elara: \[ 3\] 0.0-60.0 sec 131 MBytes 18.3 Mbits/sec\
io: \[ ID\] Interval Transfer Bandwidth\
io: \[ 3\] 0.0-60.0 sec 103 MBytes 14.4 Mbits/sec\
leda: \[ ID\] Interval Transfer Bandwidth\
leda: \[ 3\] 0.0-60.0 sec 96.1 MBytes 13.4 Mbits/sec

64 bytes from 192.168.22.1: seq=104 ttl=63 time=35.741 ms\
64 bytes from 192.168.22.1: seq=105 ttl=63 time=38.569 ms\
64 bytes from 192.168.22.1: seq=106 ttl=63 time=41.837 ms\
64 bytes from 192.168.22.1: seq=107 ttl=63 time=45.428 ms\
64 bytes from 192.168.22.1: seq=108 ttl=63 time=42.983 ms\
64 bytes from 192.168.22.1: seq=109 ttl=63 time=25.225 ms\
64 bytes from 192.168.22.1: seq=110 ttl=63 time=31.912 ms

### Vlan, Qos disabled, 128k window size

dtaht@metis:\~\$ pdsh -lroot -grouters -xaitne 'iperf -w64k -t 60 -c
metis.noise.gatech.edu'\
elara: ------------------------------------------------------------\
elara: Client connecting to metis.noise.gatech.edu, TCP port 5001\
elara: TCP window size: 128 KByte (WARNING: requested 64.0 KByte)\
elara: ------------------------------------------------------------\
elara: \[ 3\] local 192.168.115.186 port 40091 connected with
130.207.97.23 port 5001\
thebe: ------------------------------------------------------------\
thebe: Client connecting to metis.noise.gatech.edu, TCP port 5001\
thebe: TCP window size: 128 KByte (WARNING: requested 64.0 KByte)\
thebe: ------------------------------------------------------------\
io: ------------------------------------------------------------\
io: Client connecting to metis.noise.gatech.edu, TCP port 5001\
io: TCP window size: 128 KByte (WARNING: requested 64.0 KByte)\
io: ------------------------------------------------------------\
thebe: \[ 3\] local 172.16.23.105 port 49502 connected with
130.207.97.23 port 5001\
io: \[ 3\] local 192.168.22.223 port 48909 connected with 130.207.97.23
port 5001\
leda: ------------------------------------------------------------\
leda: Client connecting to metis.noise.gatech.edu, TCP port 5001\
leda: TCP window size: 128 KByte (WARNING: requested 64.0 KByte)\
leda: ------------------------------------------------------------\
leda: \[ 3\] local 192.168.115.1 port 55528 connected with 130.207.97.23
port 5001\
elara: \[ ID\] Interval Transfer Bandwidth\
elara: \[ 3\] 0.0-60.0 sec 553 MBytes 77.3 Mbits/sec\
io: \[ ID\] Interval Transfer Bandwidth\
io: \[ 3\] 0.0-60.0 sec 361 MBytes 50.5 Mbits/sec\
thebe: \[ ID\] Interval Transfer Bandwidth\
thebe: \[ 3\] 0.0-62.5 sec 896 KBytes 117 Kbits/sec

leda: \[ ID\] Interval Transfer Bandwidth\
leda: \[ 3\] 0.0-64.5 sec 60.1 MBytes 7.82 Mbits/sec

64 bytes from 192.168.22.1: seq=17 ttl=63 time=4.490 ms\
64 bytes from 192.168.22.1: seq=18 ttl=63 time=5.133 ms\
64 bytes from 192.168.22.1: seq=19 ttl=63 time=70.439 ms\
64 bytes from 192.168.22.1: seq=20 ttl=63 time=41.900 ms\
64 bytes from 192.168.22.1: seq=21 ttl=63 time=17.971 ms\
64 bytes from 192.168.22.1: seq=22 ttl=63 time=32.655 ms\
64 bytes from 192.168.22.1: seq=23 ttl=63 time=35.967 ms\
64 bytes from 192.168.22.1: seq=24 ttl=63 time=21.027 ms\
64 bytes from 192.168.22.1: seq=25 ttl=63 time=14.933 ms\
64 bytes from 192.168.22.1: seq=26 ttl=63 time=11.854 ms\
64 bytes from 192.168.22.1: seq=27 ttl=63 time=25.158 ms\
64 bytes from 192.168.22.1: seq=28 ttl=63 time=3.590 ms\
64 bytes from 192.168.22.1: seq=29 ttl=63 time=7.905 ms\
64 bytes from 192.168.22.1: seq=30 ttl=63 time=1.676 ms\
64 bytes from 192.168.22.1: seq=31 ttl=63 time=2.639 ms\
64 bytes from 192.168.22.1: seq=32 ttl=63 time=23.146 ms\
64 bytes from 192.168.22.1: seq=33 ttl=63 time=0.585 ms\
64 bytes from 192.168.22.1: seq=34 ttl=63 time=4.390 ms\
64 bytes from 192.168.22.1: seq=35 ttl=63 time=0.571 ms\
64 bytes from 192.168.22.1: seq=36 ttl=63 time=0.574 ms

### vlan and bridge disabled, Qos disabled, 220k window size

dtaht@metis:\~\$ pdsh -lroot -grouters -xaitne 'iperf -w224k -t 60 -c
metis.noise.gatech.edu'\
elara: ------------------------------------------------------------\
elara: Client connecting to metis.noise.gatech.edu, TCP port 5001\
elara: TCP window size: 220 KByte (WARNING: requested 224 KByte)\
elara: ------------------------------------------------------------\
elara: \[ 3\] local 192.168.115.186 port 45234 connected with
130.207.97.23 port 5001\
thebe: ------------------------------------------------------------\
thebe: Client connecting to metis.noise.gatech.edu, TCP port 5001\
thebe: TCP window size: 220 KByte (WARNING: requested 224 KByte)\
thebe: ------------------------------------------------------------\
thebe: \[ 3\] local 172.16.23.105 port 49315 connected with
130.207.97.23 port 5001\
io: ------------------------------------------------------------\
io: Client connecting to metis.noise.gatech.edu, TCP port 5001\
io: TCP window size: 220 KByte (WARNING: requested 224 KByte)\
io: ------------------------------------------------------------\
io: \[ 3\] local 192.168.22.223 port 58270 connected with 130.207.97.23
port 5001\
leda: ------------------------------------------------------------\
leda: Client connecting to metis.noise.gatech.edu, TCP port 5001\
leda: TCP window size: 220 KByte (WARNING: requested 224 KByte)\
leda: ------------------------------------------------------------\
leda: \[ 3\] local 192.168.115.1 port 45996 connected with 130.207.97.23
port 5001

elara: \[ ID\] Interval Transfer Bandwidth\
elara: \[ 3\] 0.0-60.0 sec 526 MBytes 73.6 Mbits/sec\
leda: \[ ID\] Interval Transfer Bandwidth\
leda: \[ 3\] 0.0-60.0 sec 233 MBytes 32.6 Mbits/sec\
io: \[ ID\] Interval Transfer Bandwidth\
io: \[ 3\] 0.0-64.5 sec 204 MBytes 26.5 Mbits/sec\
thebe: \[ ID\] Interval Transfer Bandwidth\
thebe: \[ 3\] 0.0-82.0 sec 512 KBytes 51.2 Kbits/sec

64 bytes from 192.168.22.1: seq=165 ttl=63 time=1.418 ms\
64 bytes from 192.168.22.1: seq=166 ttl=63 time=54.550 ms\
64 bytes from 192.168.22.1: seq=167 ttl=63 time=86.666 ms\
64 bytes from 192.168.22.1: seq=168 ttl=63 time=9.092 ms\
64 bytes from 192.168.22.1: seq=169 ttl=63 time=54.473 ms\
64 bytes from 192.168.22.1: seq=170 ttl=63 time=131.407 ms\
64 bytes from 192.168.22.1: seq=171 ttl=63 time=8.612 ms\
64 bytes from 192.168.22.1: seq=172 ttl=63 time=53.086 ms\
64 bytes from 192.168.22.1: seq=173 ttl=63 time=1.622 ms\
64 bytes from 192.168.22.1: seq=174 ttl=63 time=0.913 ms\
64 bytes from 192.168.22.1: seq=175 ttl=63 time=69.206 ms\
64 bytes from 192.168.22.1: seq=176 ttl=63 time=6.242 ms\
64 bytes from 192.168.22.1: seq=177 ttl=63 time=13.658 ms\
64 bytes from 192.168.22.1: seq=178 ttl=63 time=1.645 ms\
64 bytes from 192.168.22.1: seq=179 ttl=63 time=19.966 ms\
64 bytes from 192.168.22.1: seq=180 ttl=63 time=24.278 ms\
64 bytes from 192.168.22.1: seq=181 ttl=63 time=5.844 ms\
64 bytes from 192.168.22.1: seq=182 ttl=63 time=41.513 ms\
64 bytes from 192.168.22.1: seq=183 ttl=63 time=10.450 ms\
64 bytes from 192.168.22.1: seq=184 ttl=63 time=20.323 ms\
64 bytes from 192.168.22.1: seq=185 ttl=63 time=179.199 ms\
64 bytes from 192.168.22.1: seq=186 ttl=63 time=34.255 ms\
64 bytes from 192.168.22.1: seq=187 ttl=63 time=11.795 ms\
64 bytes from 192.168.22.1: seq=188 ttl=63 time=51.354 ms\
64 bytes from 192.168.22.1: seq=189 ttl=63 time=4.369 ms

Why did thebe do so badly and take 83 seconds to complete?

Run the same test for longer
----------------------------

dtaht@metis:\~\$ . /etc/profile.d/pdsh\
dtaht@metis:\~\$ pdsh -lroot -grouters -xaitne 'iperf -w220k -t 600 -c
metis.noise.gatech.edu'\
elara: ------------------------------------------------------------\
elara: Client connecting to metis.noise.gatech.edu, TCP port 5001\
elara: TCP window size: 220 KByte\
elara: ------------------------------------------------------------\
elara: \[ 3\] local 192.168.115.186 port 41316 connected with
130.207.97.23 port 5001\
io: ------------------------------------------------------------\
io: Client connecting to metis.noise.gatech.edu, TCP port 5001\
io: TCP window size: 220 KByte\
io: ------------------------------------------------------------\
thebe: ------------------------------------------------------------\
thebe: Client connecting to metis.noise.gatech.edu, TCP port 5001\
thebe: TCP window size: 220 KByte\
thebe: ------------------------------------------------------------\
leda: ------------------------------------------------------------\
leda: Client connecting to metis.noise.gatech.edu, TCP port 5001\
leda: TCP window size: 220 KByte\
leda: ------------------------------------------------------------\
leda: \[ 3\] local 192.168.115.1 port 43984 connected with 130.207.97.23
port 5001\
thebe: \[ 3\] local 172.16.23.105 port 38976 connected with
130.207.97.23 port 5001\
io: \[ 3\] local 192.168.22.223 port 38365 connected with 130.207.97.23
port 5001

elara: \[ ID\] Interval Transfer Bandwidth\
elara: \[ 3\] 0.0-600.0 sec 5.14 GBytes 73.6 Mbits/sec\
leda: \[ ID\] Interval Transfer Bandwidth\
leda: \[ 3\] 0.0-600.0 sec 3.73 GBytes 53.5 Mbits/sec\
thebe: \[ ID\] Interval Transfer Bandwidth\
thebe: \[ 3\] 0.0-605.6 sec 384 KBytes 5.19 Kbits/sec\
io: \[ ID\] Interval Transfer Bandwidth\
io: \[ 3\] 0.0-685.3 sec 476 MBytes 5.83 Mbits/sec

Next up - recall the topology of the network
--------------------------------------------

I am thinking, based on these results, that thebe and io are behind
other routers, and being starved by the switches involved.\
I'd meant to write a ip route to graphviz parser to do that sort of
thing, I guess it's past time.
