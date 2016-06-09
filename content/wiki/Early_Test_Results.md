
---
title: Early_Test_Results
date: 2012-04-14T21:28:23
lastmod: 2012-04-26T20:55:10
---
Early Test Results
==================

Native IPv6 vs IPv4 fairness test... passed.
--------------------------------------------

Tested with a 40Mbit uplink setting, RTT of \~5ms\
(sfqred with the front-of-queue patch)

(it would be good to get a tunnelled results for 6in4 and 6to4)

    #!/bin/sh

    # Test three bins in the simple_qos script, ipv4 and ipv6 equally

    netperf -4 -Y CS1,CS1 -l 120 -H huchra.bufferbloat.net >> /tmp/CS1.log &
    netperf -4 -Y EF,EF -l 120 -H huchra.bufferbloat.net >> /tmp/EF.log &
    netperf -4 -Y BE,BE -l 120 -H huchra.bufferbloat.net >> /tmp/BE.log &
    netperf -6 -Y CS1,CS1 -l 120 -H huchra.bufferbloat.net >> /tmp/CS1_6.log &
    netperf -6 -Y EF,EF -l 120 -H huchra.bufferbloat.net >> /tmp/EF_6.log &
    netperf -6 -Y BE,BE -l 120 -H huchra.bufferbloat.net >> /tmp/BE_6.log &

    tail -f /tmp/*.log

### Result


    ==> /tmp/BE.log <==
    MIGRATED TCP STREAM TEST from 0.0.0.0 () port 0 AF_INET to lists.bufferbloat.net () port 0 AF_INET : demo
    Recv   Send    Send                          
    Socket Socket  Message  Elapsed              
    Size   Size    Size     Time     Throughput  
    bytes  bytes   bytes    secs.    10^6bits/sec  

     87380  65536  65536    120.02     10.56   

    ==> /tmp/BE_6.log <==
    MIGRATED TCP STREAM TEST from :: (::) port 0 AF_INET6 to lists.bufferbloat.net () port 0 AF_INET6 : demo
    Recv   Send    Send                          
    Socket Socket  Message  Elapsed              
    Size   Size    Size     Time     Throughput  
    bytes  bytes   bytes    secs.    10^6bits/sec  

     87380  65536  65536    120.01     10.43   

    ==> /tmp/CS1.log <==
    MIGRATED TCP STREAM TEST from 0.0.0.0 () port 0 AF_INET to lists.bufferbloat.net () port 0 AF_INET : demo
    Recv   Send    Send                          
    Socket Socket  Message  Elapsed              
    Size   Size    Size     Time     Throughput  
    bytes  bytes   bytes    secs.    10^6bits/sec  

     87380  65536  65536    120.08      2.13   

    ==> /tmp/CS1_6.log <==
    MIGRATED TCP STREAM TEST from :: (::) port 0 AF_INET6 to lists.bufferbloat.net () port 0 AF_INET6 : demo
    Recv   Send    Send                          
    Socket Socket  Message  Elapsed              
    Size   Size    Size     Time     Throughput  
    bytes  bytes   bytes    secs.    10^6bits/sec  

     87380  65536  65536    120.08      2.10   

    ==> /tmp/EF.log <==
    MIGRATED TCP STREAM TEST from 0.0.0.0 () port 0 AF_INET to lists.bufferbloat.net () port 0 AF_INET : demo
    Recv   Send    Send                          
    Socket Socket  Message  Elapsed              
    Size   Size    Size     Time     Throughput  
    bytes  bytes   bytes    secs.    10^6bits/sec  

     87380  65536  65536    120.03      6.34   

    ==> /tmp/EF_6.log <==
    MIGRATED TCP STREAM TEST from :: (::) port 0 AF_INET6 to lists.bufferbloat.net () port 0 AF_INET6 : demo
    Recv   Send    Send                          
    Socket Socket  Message  Elapsed              
    Size   Size    Size     Time     Throughput  
    bytes  bytes   bytes    secs.    10^6bits/sec  

     87380  65536  65536    120.04      6.27   

### tc output

    root@OpenWrt:~# tc -s qdisc show dev ge00
    qdisc htb 1: root refcnt 2 r2q 10 default 12 direct_packets_stat 0
     Sent 1387076657 bytes 918754 pkt (dropped 0, overlimits 2197603 requeues 598) 
     backlog 0b 0p requeues 598 
    qdisc sfq 110: parent 1:11 limit 200p quantum 1514b depth 42 headdrop divisor 1024 
     ewma 4 min 3000b max 18000b probability 0.2 ecn 
     prob_mark 0 prob_mark_head 10244 prob_drop 0
     forced_mark 0 forced_mark_head 0 forced_drop 0
     Sent 397807758 bytes 263694 pkt (dropped 0, overlimits 10244 requeues 0) 
     backlog 0b 0p requeues 0 
    qdisc sfq 120: parent 1:12 limit 300p quantum 1514b depth 42 headdrop divisor 1024 
     ewma 4 min 3000b max 18000b probability 0.2 ecn 
     prob_mark 1 prob_mark_head 15657 prob_drop 0
     forced_mark 0 forced_mark_head 0 forced_drop 0
     Sent 783087099 bytes 518868 pkt (dropped 0, overlimits 15658 requeues 0) 
     backlog 0b 0p requeues 0 
    qdisc sfq 130: parent 1:13 limit 150p quantum 1514b depth 42 headdrop divisor 1024 
     ewma 4 min 3000b max 18000b probability 0.2 ecn 
     prob_mark 0 prob_mark_head 4597 prob_drop 0
     forced_mark 0 forced_mark_head 0 forced_drop 0
     Sent 206181800 bytes 136192 pkt (dropped 0, overlimits 4597 requeues 0) 
     backlog 0b 0p requeues 0 

    root@OpenWrt:~# tc -s class show dev ge00
    class htb 1:11 parent 1:1 leaf 110: prio 1 rate 32000bit ceil 13333Kbit burst 1600b cburst 1599b 
     Sent 397810468 bytes 263718 pkt (dropped 0, overlimits 0 requeues 0) 
     rate 264bit 0pps backlog 0b 0p requeues 0 
     lended: 1313 borrowed: 262405 giants: 0
     tokens: 5937500 ctokens: 14250

    class htb 1:1 root rate 40000Kbit ceil 40000Kbit burst 1600b cburst 1600b 
     Sent 1387094521 bytes 918853 pkt (dropped 0, overlimits 0 requeues 0) 
     rate 3000bit 2pps backlog 0b 0p requeues 0 
     lended: 686264 borrowed: 0 giants: 0
     tokens: 4750 ctokens: 4750

    class htb 1:10 parent 1:1 prio 0 rate 40000Kbit ceil 40000Kbit burst 1600b cburst 1600b 
     Sent 0 bytes 0 pkt (dropped 0, overlimits 0 requeues 0) 
     rate 0bit 0pps backlog 0b 0p requeues 0 
     lended: 0 borrowed: 0 giants: 0
     tokens: 5000 ctokens: 5000

    class htb 1:13 parent 1:1 leaf 130: prio 3 rate 4444Kbit ceil 39936Kbit burst 1599b cburst 1597b 
     Sent 206181800 bytes 136192 pkt (dropped 0, overlimits 0 requeues 0) 
     rate 0bit 0pps backlog 0b 0p requeues 0 
     lended: 87685 borrowed: 48507 giants: 0
     tokens: -32342 ctokens: 4735

    class htb 1:12 parent 1:1 leaf 120: prio 2 rate 6666Kbit ceil 39936Kbit burst 1599b cburst 1597b 
     Sent 783102253 bytes 518943 pkt (dropped 0, overlimits 0 requeues 0) 
     rate 2736bit 1pps backlog 0b 0p requeues 0 
     lended: 143591 borrowed: 375352 giants: 0
     tokens: 28590 ctokens: 4782

### Ping. Flat.


    Before:

    root@OpenWrt:~# ping 8.8.8.8
    PING 8.8.8.8 (8.8.8.8): 56 data bytes
    64 bytes from 8.8.8.8: seq=0 ttl=50 time=19.947 ms
    64 bytes from 8.8.8.8: seq=1 ttl=50 time=19.970 ms

    ...

    During:
    root@OpenWrt:~# ping 8.8.8.8
    PING 8.8.8.8 (8.8.8.8): 56 data bytes
    64 bytes from 8.8.8.8: seq=0 ttl=50 time=20.411 ms
    64 bytes from 8.8.8.8: seq=1 ttl=50 time=20.758 ms
    64 bytes from 8.8.8.8: seq=2 ttl=50 time=20.959 ms
    64 bytes from 8.8.8.8: seq=3 ttl=50 time=20.746 ms

    ...

tc during (different run)


    root@OpenWrt:~# tc -s qdisc show dev ge00
    qdisc htb 1: root refcnt 2 r2q 10 default 12 direct_packets_stat 0
     Sent 707469403 bytes 468141 pkt (dropped 0, overlimits 1119667 requeues 278) 
     backlog 0b 22p requeues 278 
    qdisc sfq 110: parent 1:11 limit 200p quantum 1514b depth 42 headdrop divisor 1024 
     ewma 4 min 3000b max 18000b probability 0.2 ecn 
     prob_mark 0 prob_mark_head 6337 prob_drop 0
     forced_mark 0 forced_mark_head 0 forced_drop 0
     Sent 235716510 bytes 156182 pkt (dropped 0, overlimits 6337 requeues 0) 
     backlog 10598b 7p requeues 0 
    qdisc sfq 120: parent 1:12 limit 300p quantum 1514b depth 42 headdrop divisor 1024 
     ewma 4 min 3000b max 18000b probability 0.2 ecn 
     prob_mark 0 prob_mark_head 10292 prob_drop 0
     forced_mark 0 forced_mark_head 0 forced_drop 0
     Sent 392692535 bytes 259730 pkt (dropped 0, overlimits 10292 requeues 0) 
     backlog 13626b 9p requeues 0 
    qdisc sfq 130: parent 1:13 limit 150p quantum 1514b depth 42 headdrop divisor 1024 
     ewma 4 min 3000b max 18000b probability 0.2 ecn 
     prob_mark 0 prob_mark_head 2168 prob_drop 0
     forced_mark 0 forced_mark_head 0 forced_drop 0
     Sent 79060358 bytes 52229 pkt (dropped 0, overlimits 2168 requeues 0) 
     backlog 9084b 6p requeues 0 

Ingress/Egress Shaper Test
--------------------------

30Mbit down, 4Mbit up.

    netperf -4 -l 60 -H huchra.bufferbloat.net -t TCP_STREAM &
    netperf -6 -l 60 -H huchra.bufferbloat.net -t TCP_MAERTS &
    netperf -4 -l 60 -H huchra.bufferbloat.net -t TCP_MAERTS &

    netperf -Y AF42,AF42 -6 -l 30 -H huchra.bufferbloat.net -t TCP_RR >> tcp.rr &
    netperf -Y AF42,AF42 -4 -l 30 -H huchra.bufferbloat.net -t TCP_RR >> tcp.rr &

    netperf -6 -l 60 -H huchra.bufferbloat.net -t TCP_STREAM &

    root@OpenWrt:~# Recv   Send    Send                          
    Socket Socket  Message  Elapsed              
    Size   Size    Size     Time     Throughput  
    bytes  bytes   bytes    secs.    10^6bits/sec  

     87380  16384  16384    60.06      14.51   
    Recv   Send    Send                          
    Socket Socket  Message  Elapsed              
    Size   Size    Size     Time     Throughput  
    bytes  bytes   bytes    secs.    10^6bits/sec  

     87380  16384  16384    60.04      14.31   
    Recv   Send    Send                          
    Socket Socket  Message  Elapsed              
    Size   Size    Size     Time     Throughput  
    bytes  bytes   bytes    secs.    10^6bits/sec  

     87380  65536  65536    60.15       1.39   
    Recv   Send    Send                          
    Socket Socket  Message  Elapsed              
    Size   Size    Size     Time     Throughput  
    bytes  bytes   bytes    secs.    10^6bits/sec  

     87380  65536  65536    60.18       1.38   

The first tcp.rr result is from a previous test of TCP\_RR without AF42
enabled.


    root@OpenWrt:~# cat tcp.rr 
    MIGRATED TCP REQUEST/RESPONSE TEST from 0.0.0.0 () port 0 AF_INET to lists.bufferbloat.net () port 0 AF_INET : demo : first burst 0
    Local /Remote
    Socket Size   Request  Resp.   Elapsed  Trans.
    Send   Recv   Size     Size    Time     Rate         
    bytes  Bytes  bytes    bytes   secs.    per sec   

    65536  87380  1        1       30.01     266.69   
    16384  87380 
    MIGRATED TCP REQUEST/RESPONSE TEST from :: (::) port 0 AF_INET6 to lists.bufferbloat.net () port 0 AF_INET6 : demo : first burst 0
    Local /Remote
    Socket Size   Request  Resp.   Elapsed  Trans.
    Send   Recv   Size     Size    Time     Rate         
    bytes  Bytes  bytes    bytes   secs.    per sec   

    65536  87380  1        1       30.00     251.46   
    16384  87380 

This is TCP\_RR, repeated, but this time with AF42 set, at the same time
as the previous data

Note: huchra is configured as a drop tail system. I would suspect better
performance with both sides running sfq.


    MIGRATED TCP REQUEST/RESPONSE TEST from 0.0.0.0 () port 0 AF_INET to lists.bufferbloat.net () port 0 AF_INET : demo : first burst 0
    Local /Remote
    Socket Size   Request  Resp.   Elapsed  Trans.
    Send   Recv   Size     Size    Time     Rate         
    bytes  Bytes  bytes    bytes   secs.    per sec   

    65536  87380  1        1       30.00     353.20   
    16384  87380 
    MIGRATED TCP REQUEST/RESPONSE TEST from :: (::) port 0 AF_INET6 to lists.bufferbloat.net () port 0 AF_INET6 : demo : first burst 0
    Local /Remote
    Socket Size   Request  Resp.   Elapsed  Trans.
    Send   Recv   Size     Size    Time     Rate         
    bytes  Bytes  bytes    bytes   secs.    per sec   

    65536  87380  1        1       30.00     313.90   
    16384  87380 
