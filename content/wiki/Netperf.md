
---
title: Netperf
date: 2011-07-13T13:34:50
lastmod: 2011-07-14T15:18:44
---
Netperf
=======

Dtaht suggested that we consider netperf instead of or in addition to
iperf for the following reasons:

-   netperf doesn't require the server process to be running constantly,
    as it can be instantiated by xinetd.
-   netperf reports cpu usage on client and server which is useful in
    CPU-constrained environments
-   netperf rus tests over both TCP and UDP
-   netperf has a number of tests that can be run

Users on the internet have reported higher reported throughputs using
netperf than when using iperf, for the exact same setup and devices.

Using netperf
-------------

Porting and testing bleeding-edge netperf
-----------------------------------------

We downloaded the subversion HEAD
(http://www.netperf.org/svn/netperf2/trunk/) and created a netperf
package using this source, based on the existing openwrt netperf
package.

We installed this packaged netperf (netperf-latest) on two wndr3700v2
boxes, as well as netperf 2.4.4 as packaged by Ubuntu running in VMs on
the hardware specified below.

Ran netperf between the following: (see bottom for device
specifications)

1\) HOST1 -&gt; HOST2

    kyriakos@zenith:~/Desktop/bismark-summercamp/netperf/trunk/src$ ./netperf -H 172.31.8.115 -c -C
    MIGRATED TCP STREAM TEST from 0.0.0.0 (0.0.0.0) port 0 AF_INET to 172.31.8.115 (172.31.8.115) port 0 AF_INET 
    Recv   Send    Send                          Utilization       Service Demand
     Socket Socket  Message  Elapsed              Send     Recv     Send    Recv
     Size   Size    Size     Time     Throughput  local    remote   local   remote
     bytes  bytes   bytes    secs.    10^6bits/s  % S      % S      us/KB   us/KB

     87380  16384  16384    10.37         4.11   0.96     0.19     19.217  3.866  

2\) ROUTER1 -&gt; HOST2

    root@gw:/tmp# netperf -H 172.31.8.115 -c -C
    MIGRATED TCP STREAM TEST from 0.0.0.0 (0.0.0.0) port 0 AF_INET to 172.31.8.115 (172.31.8.115) port 0 AF_INET
    Recv   Send    Send                          Utilization       Service Demand
    Socket Socket  Message  Elapsed              Send     Recv     Send    Recv
    Size   Size    Size     Time     Throughput  local    remote   local   remote
    bytes  bytes   bytes    secs.    10^6bits/s  % S      % S      us/KB   us/KB

     87380  16384  16384    10.07         4.21   29.00    1.00     565.055  19.390 

3\) ROUTER1 -&gt; ROUTER2

    root@gw:/tmp# netperf -H 172.31.8.33 -c -C
    MIGRATED TCP STREAM TEST from 0.0.0.0 (0.0.0.0) port 0 AF_INET to 172.31.8.33 (172.31.8.33) port 0 AF_INET
    Recv   Send    Send                          Utilization       Service Demand
    Socket Socket  Message  Elapsed              Send     Recv     Send    Recv
    Size   Size    Size     Time     Throughput  local    remote   local   remote
    bytes  bytes   bytes    secs.    10^6bits/s  % S      % S      us/KB   us/KB

     87380  16384  16384    10.07         4.23   29.49    32.41    571.139  627.530 

iperf between HOST1 -&gt; HOST2 for comparison:

    kyriakos@zenith:~$ iperf -c 172.31.8.115
    ------------------------------------------------------------
    Client connecting to 172.31.8.115, TCP port 5001
    TCP window size: 16.0 KByte (default)
    ------------------------------------------------------------
    [  3] local 10.0.2.15 port 51176 connected with 172.31.8.115 port 5001
    [ ID] Interval       Transfer     Bandwidth
    [  3]  0.0-10.1 sec  5.20 MBytes  4.33 Mbits/sec

HOST1:\
Model Name: MacBook Pro\
Model Identifier: MacBookPro6,2\
Processor Name: Intel Core i5\
Processor Speed: 2.53 GHz\
Number Of Processors: 1\
Total Number Of Cores: 2\
L2 Cache (per core): 256 KB\
L3 Cache: 3 MB\
Memory: 4 GB\
Processor Interconnect Speed: 4.8 GT/s\
Boot ROM Version: MBP61.0057.B0C\
SMC Version (system): 1.58f16\
Serial Number (system): W8023204AGY\
Hardware UUID: 519F0E32-09F0-5FB2-9BEA-A5A410ECACE3\
Sudden Motion Sensor:\
State: Enabled\
Interfaces:

en1:\
Card Type: AirPort Extreme (0x14E4, 0x93)\
Firmware Version: Broadcom BCM43xx 1.0 (5.10.131.36.9)

virtualization:\
Sun VirtualBox, NATed network

HOST2:\
Model Name: MacBook\
Model Identifier: MacBook6,1\
Processor Name: Intel Core 2 Duo\
Processor Speed: 2.26 GHz\
Number Of Processors: 1\
Total Number Of Cores: 2\
L2 Cache: 3 MB\
Memory: 4 GB\
Bus Speed: 1.07 GHz

en1:\
Card Type: AirPort Extreme (0x14E4, 0x93)\
Firmware Version: Broadcom BCM43xx 1.0 (5.10.131.36.9)

virtualization:\
VMware Fusion, bridged network
