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
tc qdisc replace dev eth0 root cake docsis ack-filter nat bandwidth 150mbit
```   
* _dev_ is the device, eth0 in this case
* _root_ means this is the "top" qdisc
* _docsis_ says tune for a cable-tv uplink: cable TV follows the 
docsis standards
* _ack-filter_ skips sending redundant acknowlegements
* _nat_ tells cake network address translation is happening on _this_ 
machine, not a separate router.
* _bandwidth_ is the down-bound bandwidth of your link, often taken 
from DSLReport's speed test


Internet over Telephone Lines
-----------------------------
```
TBD
```   
* _adsl_ is one of the two forms of "digital subscriber line", 
the asymmetrical kind (faster down than up)
* _vdsl2_ is a newer DSL


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


