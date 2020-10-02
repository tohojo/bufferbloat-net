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

The recipes are annotated combinations of settings that have been used for 
particular kinds of networks, organized from most common to most unusual. 
The detailed reference for all the parameters is tc-cake(8) 



Internet over TV Cable
----------------------
```
tc qdisc replace dev eth0 root cake docsis ack-filter bandwidth 150mbit
```   
* _dev_ is the device, eth0 in this case
* _root_ means this is the "top" qdisc
* _docsis_ says tune for a cable-tv uplink: cable TV follows the 
docsis standards
* _ack-filter_ skips sending redundant acknowledgements 
* _bandwidth_ is the down-bound bandwidth of your link, often taken 
from speed tests like http://www.dslreports.com/speedtest.


Internet over Telephone Lines
-----------------------------
```
tc qdisc replace dev eth0 root cake pppoe-ptm ack-filter bandwidth 61mbit
```  
* _pppoe-ptm_ is one of the DSL (digital subscriber line) variants
 used by telcos such as British Telecommunications
 
 There are numerous dsl options: if your ISP doesn't publicise which they use, 
 there is also _conservative_ which sets the expected overhead to a safely high value


Internet from a Preexisting Ethernet
------------------------------------
```
tc qdisc replace dev eth0 root cake ethernet bandwidth 1gbit
```   
* _ethernet_ says to tune for ethernet
* _bandwidth 1GBit_ is substantially faster than is commonly seen in 
offices. The example is from an office 
connected upstrfeam to a datacenter with a 10Gbit network.
* _bandwidth unlimited_ would suit an upstream which is equally fast.


