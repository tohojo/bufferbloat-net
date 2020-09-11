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
* dev is the device, eth0 in this case
* root means this is the "top" qdisc
* docsis says tune for a cable-tv uplink: cable TV follows the 
_docsis_ standards
* The ack-filter skips sending redundant acknowlegements
* nat tells cake network address translation is happening on _this_ 
machine, not a separate router
* bandwidth is the downbound bandwidth of your link, often taken 
from DSLReport's speed test


Internet over Telephone Lines
-----------------------------
```
TBD
```   
* ADSL is one of the two forms of "digital subscriber line", asymmetrical
* VDSL2 is a newer and faster DSL


Internet from a Preexisting Ethernet
------------------------------------
```
tc qdisc replace dev eth0 root cake ethernet bandwidth 1gbit
```   
* ethernet says to tune for ethernet
* bandwidth 1Gbit is typical of a small data center network, substantially 
faster than is commonly seen in offices


