
---
title: Diffserv statistics
date: 2011-06-20T04:02:13
lastmod: 2011-06-20T05:53:34
---
Diffserv statistics
===================

Dave Taht's Network
-------------------

In this example - 10% of the ipv4 packets are network radio, \~88% are
BE, and less than 2% can be classified into other classes.

This is 24 hours of data, obviously somewhat skewed by the network not
being in use half that time...

After I improve performance of the diffserv classifier I will move
towards analyzing one of todays typical home network,\
over an hourly period.

\$ iptables -v -t mangle -L W80211e

    Chain W80211e (2 references)Chain W80211e (2 references)
     pkts bytes target     prot opt in     out     source               destination         
    1589K  975M CLASSIFY   all  --  any    any     anywhere             anywhere            /* All pkts */ CLASSIFY set 0:100 
     1455  712K CLASSIFY   all  --  any    any     anywhere             anywhere            DSCP match 0x08/* Background (BK)(BK) */ CLASSIFY set 0:102 
      731 55437 CLASSIFY   all  --  any    any     anywhere             anywhere            DSCP match 0x2e/*  Voice (VO)(EF) */ CLASSIFY set 0:107 
        3  1311 CLASSIFY   all  --  any    any     anywhere             anywhere            DSCP match 0x30/* Critical (VI) */ CLASSIFY set 0:106 
        0     0 CLASSIFY   all  --  any    any     anywhere             anywhere            DSCP match 0x18/* Video (VI) */ CLASSIFY set 0:104 
     1507  254K CLASSIFY   all  --  any    any     anywhere             anywhere            DSCP match 0x2a/* Mice(VO) */ CLASSIFY set 0:104 
        0     0 CLASSIFY   all  --  any    any     anywhere             anywhere            DSCP match 0x28/* Stuff (BK) */ CLASSIFY set 0:101 
     451K   95M CLASSIFY   all  --  any    any     anywhere             anywhere            DSCP match 0x22/* Net Radio(VI) */ CLASSIFY set 0:104 
     2312 1308K CLASSIFY   all  --  any    any     anywhere             anywhere            DSCP match 0x04/* Typing (VI) */ CLASSIFY set 0:104 
        0     0 CLASSIFY   all  --  any    any     anywhere             anywhere            DSCP match 0x09/* P2P (BK) */ CLASSIFY set 0:101 
        0     0 CLASSIFY   all  --  any    any     anywhere             anywhere            DSCP match 0x10/* Background (BK) */ CLASSIFY set 0:102 

But for ipv6, the ratios and volume are MUCH different. \~99% of the
traffic is control traffic (mostly babel in this case).\
While the total amount of traffic may be low compared to ipv4, the
amount of traffic relative to the mice category of ipv4\
is much higher, in fact, by volume, the ipv6 control packets are the
third largest class of packet.

\$ ip6tables -v -t mangle -L W80211e

    Chain W80211e (2 references)
     pkts bytes target     prot opt in     out     source               destination         
    91694   23M CLASSIFY   all      any    any     anywhere             anywhere            /* All pkts */ CLASSIFY set 0:100 
       38  3190 CLASSIFY   all      any    any     anywhere             anywhere            DSCP match 0x08/* Background (BK)(BK) */ CLASSIFY set 0:102 
       25  2400 CLASSIFY   all      any    any     anywhere             anywhere            DSCP match 0x2e/*  Voice (VO)(EF) */ CLASSIFY set 0:107       DSCP match 0x30/* Critical (VI) */ CLASSIFY set 0:106 
        0     0 CLASSIFY   all      any    any     anywhere             anywhere      
    87684   22M CLASSIFY   all      any    any     anywhere             anywhere            DSCP match 0x30/* Critical (VI) */ CLASSIFY set 0:106 
        0     0 CLASSIFY   all      any    any     anywhere             anywhere            DSCP match 0x18/* Video (VI) */ CLASSIFY set 0:104 
     3162  249K CLASSIFY   all      any    any     anywhere             anywhere            DSCP match 0x2a/* Mice(VO) */ CLASSIFY set 0:104 
        0     0 CLASSIFY   all      any    any     anywhere             anywhere            DSCP match 0x28/* Stuff (BK) */ CLASSIFY set 0:101 
        0     0 CLASSIFY   all      any    any     anywhere             anywhere            DSCP match 0x22/* Net Radio(VI) */ CLASSIFY set 0:104 
        0     0 CLASSIFY   all      any    any     anywhere             anywhere            DSCP match 0x04/* Typing (VI) */ CLASSIFY set 0:104 
        0     0 CLASSIFY   all      any    any     anywhere             anywhere            DSCP match 0x09/* P2P (BK) */ CLASSIFY set 0:101 
        0     0 CLASSIFY   all      any    any     anywhere             anywhere            DSCP match 0x10/* Background (BK) */ CLASSIFY set 0:102 

Your results (please identify the period, and number of users)
--------------------------------------------------------------
