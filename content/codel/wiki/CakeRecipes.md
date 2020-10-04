---
title: CakeRecipes
date: 2020-10-07T14:10:00
lastmod: 2020-10-07T14:10:00
type: wiki
---
Cake Recipes
============
[Cake](Cake.md) is the comprehensive queue management system the bufferbloat
project has been working on since 2013 and is now in general release. 

These recipes are annotated combinations of settings that have 
been used for particular kinds of networks, organized from 
most common to most unusual. 
The detailed reference for all the parameters is tc-cake(8).

Additional recipes invited! To edit this page, submit a pull request to the Github repository.

Internet over TV Cable
===

Outbound, General Case 
---
```
tc qdisc replace dev eth0 root cake docsis ack-filter bandwidth 150mbit
```   
* _dev_ is the device, eth0 in this case.
* _root_ means this is the "top" qdisc.
* _docsis_ says tune for a cable-tv uplink's overheads: 
cable TV follows the docsis standards.
* _ack-filter_ skips sending redundant acknowledgements. 
* _bandwidth_ is the download bandwidth of your link, often 
taken from speed tests like http://www.dslreports.com/speedtest.
<!-- That actually sounds _wrong_. I'm tuning the out/up 
direction. Dave C-B-->

Inbound, General case
---
This applies to most inbound cases, not just cable.
```
ip link add name ifb4eth0 type ifb
tc qdisc del dev eth0 ingress
tc qdisc add dev eth0 handle ffff: ingress
tc qdisc del dev ifb4eth0 root
tc qdisc add dev ifb4eth0 root cake bandwidth 11000kbit besteffort
ip link set ifb4eth0 up # important 
tc filter add dev eth0 parent ffff: protocol all prio 10 u32 match u32 0 0 flowid 1:1 action mirred egress redirect dev ifb4eth0
```   
This creates a named link for download/ingress and applies CAKE to it.
<!-- should the bandwidth here also be the inbound bandwidth
 from dslreports? Dave C-B -->


Internet over Telephone Lines
===

Outbound
---
```
tc qdisc replace dev eth0 root cake pppoe-ptm ack-filter bandwidth 61mbit
```  
* _pppoe-ptm_ is one of the DSL (digital subscriber line) variants
 used by telcos such as British Telecommunications.
     
 There are numerous dsl options: if your ISP doesn't publicise 
 which they use, there is also _conservative_ which sets 
 the expected overhead to a safely high value.
 
<!-- I rather expect to see a bunch of people contributing
cases for various telcos --> 


Internet from a Preexisting Ethernet
===

Outbound
---
```
tc qdisc replace dev eth0 root cake ethernet bandwidth 1gbit
```   
* _ethernet_ says to tune for ethernet's overheads.
* _bandwidth 1GBit_ is substantially faster than is commonly 
seen in offices. The example is from an office connected 
upstream to a datacenter with a faster 10Gbit network.
* _bandwidth unlimited_ suits an upstream which is the same 
speed as the office network.
<!-- the latter describes my office at work. Dave C-B -->
