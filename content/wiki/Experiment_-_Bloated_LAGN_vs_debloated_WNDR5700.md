
---
title: Experiment_-_Bloated_LAGN_vs_debloated_WNDR5700
date: 2011-02-03T07:25:31
lastmod: 2011-02-03T07:25:31
---
Experiment - Bloated LAGN vs debloated WNDR5700
===============================================

WARNING: THIS IS JUST NOTES, A DRAFT, FROM AN ONGOING EXPERIMENT

![](http://nex-6.taht.net/images/housenet.png)

NET2 (LAGN (bloated) ~~<span style="text-align:right;">WNDR5700 (debloated)</span>~~&gt; OPENRD
-----------------------------------------------------------------------------------------------

Connected at 36Mbit

### Uncontended

64 bytes from 192.168.176.1: icmp\_req=90 ttl=63 time=0.905 ms\
64 bytes from 192.168.176.1: icmp\_req=91 ttl=63 time=0.723 ms\
64 bytes from 192.168.176.1: icmp\_req=92 ttl=63 time=1.25 ms\
64 bytes from 192.168.176.1: icmp\_req=93 ttl=63 time=0.927 ms

Hey - gigE is actually useful on the router.

### under load - bloated to debloated

64 bytes from 192.168.176.1: icmp\_req=39 ttl=63 time=147 ms\
64 bytes from 192.168.176.1: icmp\_req=40 ttl=63 time=147 ms\
64 bytes from 192.168.176.1: icmp\_req=41 ttl=63 time=146 ms

### debloated to bloated

Going the other way, where I actually have a sane txqueue and dma
buffers

64 bytes from 192.168.176.1: icmp\_req=1 ttl=63 time=2.73 ms\
64 bytes from 192.168.176.1: icmp\_req=2 ttl=63 time=3.30 ms\
64 bytes from 192.168.176.1: icmp\_req=3 ttl=63 time=2.69 ms\
64 bytes from 192.168.176.1: icmp\_req=4 ttl=63 time=2.69 ms\
64 bytes from 192.168.176.1: icmp\_req=5 ttl=63 time=2.36 ms\
64 bytes from 192.168.176.1: icmp\_req=6 ttl=63 time=3.58 ms\
64 bytes from 192.168.176.1: icmp\_req=7 ttl=63 time=3.50 ms\
64 bytes from 192.168.176.1: icmp\_req=8 ttl=63 time=3.53 ms\
64 bytes from 192.168.176.1: icmp\_req=9 ttl=63 time=2.54 ms\
64 bytes from 192.168.176.1: icmp\_req=10 ttl=63 time=1.82 ms\
64 bytes from 192.168.176.1: icmp\_req=11 ttl=63 time=3.15 ms

And under contention (4 streams) it does start to exhibit about 4%
packet loss on pings

### debloated to bloated with TCP/vegas

NOTES:

TCP vegas actually outperformed veno 19.9Mbit vs 19.4Mbit for a single
transfer but this is well within the range of statistical variance.

-   NET1 e1000e ~~<span style="text-align:right;">nanostation
    M5</span>~~&gt; nanostation M5 -&gt; openrd

It's connected at 135MB-180MB 220k window size\
Empty: 1.9ms

\[ 3\] local 192.168.176.1 port 41965 connected with 192.168.23.20 port
5001\
64 bytes from 192.168.23.20: icmp\_req=2 ttl=62 time=5.82 ms\
64 bytes from 192.168.23.20: icmp\_req=3 ttl=62 time=5.39 ms\
64 bytes from 192.168.23.20: icmp\_req=4 ttl=62 time=10.5 ms\
64 bytes from 192.168.23.20: icmp\_req=5 ttl=62 time=14.4 ms\
64 bytes from 192.168.23.20: icmp\_req=6 ttl=62 time=8.62 ms\
64 bytes from 192.168.23.20: icmp\_req=7 ttl=62 time=4.31 ms\
64 bytes from 192.168.23.20: icmp\_req=8 ttl=62 time=9.03 ms\
64 bytes from 192.168.23.20: icmp\_req=9 ttl=62 time=5.30 ms\
64 bytes from 192.168.23.20: icmp\_req=10 ttl=62 time=6.56 ms\
64 bytes from 192.168.23.20: icmp\_req=11 ttl=62 time=5.72 ms\
64 bytes from 192.168.23.20: icmp\_req=12 ttl=62 time=14.4 ms\
64 bytes from 192.168.23.20: icmp\_req=13 ttl=62 time=11.4 ms\
64 bytes from 192.168.23.20: icmp\_req=14 ttl=62 time=10.9 ms

64 bytes from 192.168.176.1: icmp\_req=2 ttl=62 time=8.93 ms\
64 bytes from 192.168.176.1: icmp\_req=3 ttl=62 time=5.42 ms\
64 bytes from 192.168.176.1: icmp\_req=4 ttl=62 time=10.2 ms\
64 bytes from 192.168.176.1: icmp\_req=5 ttl=62 time=5.44 ms\
64 bytes from 192.168.176.1: icmp\_req=6 ttl=62 time=7.23 ms\
64 bytes from 192.168.176.1: icmp\_req=7 ttl=62 time=8.19 ms\
64 bytes from 192.168.176.1: icmp\_req=8 ttl=62 time=8.15 ms

Lets change the txqueuelen

PING 192.168.176.1 (192.168.176.1) 56(84) bytes of data.\
64 bytes from 192.168.176.1: icmp\_req=1 ttl=62 time=2.19 ms\
------------------------------------------------------------\
Client connecting to 192.168.176.1, TCP port 5001\
TCP window size: 16.0 KByte (default)\
------------------------------------------------------------\
\[ 3\] local 192.168.22.101 port 60572 connected with 192.168.176.1 port
5001\
64 bytes from 192.168.176.1: icmp\_req=2 ttl=62 time=9.20 ms\
64 bytes from 192.168.176.1: icmp\_req=3 ttl=62 time=3.14 ms\
64 bytes from 192.168.176.1: icmp\_req=4 ttl=62 time=9.45 ms\
64 bytes from 192.168.176.1: icmp\_req=5 ttl=62 time=9.25 ms\
64 bytes from 192.168.176.1: icmp\_req=6 ttl=62 time=9.29 ms\
64 bytes from 192.168.176.1: icmp\_req=7 ttl=62 time=8.55 ms\
64 bytes from 192.168.176.1: icmp\_req=8 ttl=62 time=7.34 ms\
64 bytes from 192.168.176.1: icmp\_req=9 ttl=62 time=12.8 ms\
64 bytes from 192.168.176.1: icmp\_req=10 ttl=62 time=9.41 ms\
64 bytes from 192.168.176.1: icmp\_req=11 ttl=62 time=10.4 ms\
64 bytes from 192.168.176.1: icmp\_req=12 ttl=62 time=6.47 ms\
64 bytes from 192.168.176.1: icmp\_req=13 ttl=62 time=8.90 ms\
64 bytes from 192.168.176.1: icmp\_req=14 ttl=62 time=10.5 ms\
64 bytes from 192.168.176.1: icmp\_req=15 ttl=62 time=9.85 ms\
64 bytes from 192.168.176.1: icmp\_req=16 ttl=62 time=12.0 ms\
64 bytes from 192.168.176.1: icmp\_req=17 ttl=62 time=8.86 ms\
64 bytes from 192.168.176.1: icmp\_req=18 ttl=62 time=8.98 ms\
64 bytes from 192.168.176.1: icmp\_req=19 ttl=62 time=9.00 ms\
64 bytes from 192.168.176.1: icmp\_req=20 ttl=62 time=9.92 ms\
64 bytes from 192.168.176.1: icmp\_req=21 ttl=62 time=7.48 ms\
64 bytes from 192.168.176.1: icmp\_req=22 ttl=62 time=6.63 ms\
64 bytes from 192.168.176.1: icmp\_req=23 ttl=62 time=3.86 ms\
64 bytes from 192.168.176.1: icmp\_req=24 ttl=62 time=8.86 ms

64 bytes from 192.168.23.20: icmp\_req=8 ttl=62 time=9.80 ms\
64 bytes from 192.168.23.20: icmp\_req=9 ttl=62 time=10.1 ms\
64 bytes from 192.168.23.20: icmp\_req=10 ttl=62 time=5.34 ms\
64 bytes from 192.168.23.20: icmp\_req=11 ttl=62 time=12.5 ms\
64 bytes from 192.168.23.20: icmp\_req=12 ttl=62 time=6.42 ms\
64 bytes from 192.168.23.20: icmp\_req=13 ttl=62 time=3.11 ms\
64 bytes from 192.168.23.20: icmp\_req=14 ttl=62 time=7.91 ms\
64 bytes from 192.168.23.20: icmp\_req=15 ttl=62 time=5.12 ms\
64 bytes from 192.168.23.20: icmp\_req=16 ttl=62 time=7.44 ms\
64 bytes from 192.168.23.20: icmp\_req=17 ttl=62 time=12.8 ms\
64 bytes from 192.168.23.20: icmp\_req=18 ttl=62 time=6.99 ms\
64 bytes from 192.168.23.20: icmp\_req=19 ttl=62 time=11.9 ms\
64 bytes from 192.168.23.20: icmp\_req=20 ttl=62 time=8.37 ms\
64 bytes from 192.168.23.20: icmp\_req=21 ttl=62 time=5.14 ms\
64 bytes from 192.168.23.20: icmp\_req=22 ttl=62 time=4.25 ms

root@cruithne:/media/c2e4f42e-9fdc-438c-998f-53c0abaf27f3/backups/cruithne/home/d/src/iperf-2.0.8\#
echo 16777216 &gt; /proc/sys/net/core/wmem\_max\
root@cruithne:/media/c2e4f42e-9fdc-438c-998f-53c0abaf27f3/backups/cruithne/home/d/src/iperf-2.0.8\#
echo 16777216 &gt; /proc/sys/net/core/rmem\_max

OK so on the wnder:

unloaded\
64 bytes from 192.168.176.1: icmp\_req=1 ttl=63 time=1.20 ms\
64 bytes from 192.168.176.1: icmp\_req=2 ttl=63 time=1.13 ms\
\^C

36Mb/sec

...

64 bytes from 192.168.172.181: icmp\_req=2 ttl=63 time=4.30 ms\
64 bytes from 192.168.172.181: icmp\_req=3 ttl=63 time=3.77 ms\
64 bytes from 192.168.172.181: icmp\_req=4 ttl=63 time=2.22 ms\
64 bytes from 192.168.172.181: icmp\_req=5 ttl=63 time=1.02 ms\
64 bytes from 192.168.172.181: icmp\_req=7 ttl=63 time=4.55 ms\
64 bytes from 192.168.172.181: icmp\_req=8 ttl=63 time=5.66 ms\
64 bytes from 192.168.172.181: icmp\_req=9 ttl=63 time=4.72 ms\
64 bytes from 192.168.172.181: icmp\_req=10 ttl=63 time=2.85 ms\
64 bytes from 192.168.172.181: icmp\_req=11 ttl=63 time=4.19 ms\
64 bytes from 192.168.172.181: icmp\_req=12 ttl=63 time=3.77 ms\
64 bytes from 192.168.172.181: icmp\_req=13 ttl=63 time=2.47 ms\
64 bytes from 192.168.172.181: icmp\_req=14 ttl=63 time=4.20 ms\
64 bytes from 192.168.172.181: icmp\_req=15 ttl=63 time=4.31 ms\
64 bytes from 192.168.172.181: icmp\_req=17 ttl=63 time=1.79 ms\
64 bytes from 192.168.172.181: icmp\_req=18 ttl=63 time=4.19 ms\
64 bytes from 192.168.172.181: icmp\_req=19 ttl=63 time=3.80 ms\
64 bytes from 192.168.172.181: icmp\_req=20 ttl=63 time=2.16 ms\
64 bytes from 192.168.172.181: icmp\_req=21 ttl=63 time=3.43 ms\
64 bytes from 192.168.172.181: icmp\_req=22 ttl=63 time=2.67 ms\
64 bytes from 192.168.172.181: icmp\_req=23 ttl=63 time=3.10 ms\
64 bytes from 192.168.172.181: icmp\_req=24 ttl=63 time=8.62 ms

64 bytes from 192.168.172.181: icmp\_req=59 ttl=63 time=3.39 ms

--- 192.168.172.181 ping statistics ---\
60 packets transmitted, 54 received, 10% packet loss, time 59046ms\
rtt min/avg/max/mdev = 0.958/3.517/8.623/1.369 ms\
\[ 3\] 0.0-61.1 sec 139 MBytes 19.0 Mbits/sec

PING 192.168.176.1 (192.168.176.1) 56(84) bytes of data.\
64 bytes from 192.168.176.1: icmp\_req=1 ttl=63 time=44.5 ms\
64 bytes from 192.168.176.1: icmp\_req=2 ttl=63 time=48.3 ms\
64 bytes from 192.168.176.1: icmp\_req=3 ttl=63 time=74.9 ms\
64 bytes from 192.168.176.1: icmp\_req=4 ttl=63 time=111 ms\
64 bytes from 192.168.176.1: icmp\_req=5 ttl=63 time=84.7 ms\
64 bytes from 192.168.176.1: icmp\_req=6 ttl=63 time=121 ms\
64 bytes from 192.168.176.1: icmp\_req=7 ttl=63 time=139 ms\
64 bytes from 192.168.176.1: icmp\_req=8 ttl=63 time=141 ms
