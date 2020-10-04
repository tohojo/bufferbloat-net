---
title: CakeFAQ
date: 2015-11-19T03:19:20
lastmod: 2020-10-07T14:10:00
type: wiki
---
Cake FAQ
========

[Cake](Cake.md) is the comprehensive queue management system the bufferbloat
project has been working on since 2013 and now in general release, circa release 4.19. It is the
rollup of 3 years of deployment experience using the htb + fq\_codel
based <link>sqm</link>-scripts.

What was the origin of the name?
--------------------------------

Initially it came from the movie 2010 where an American was trying to
explain the idioms "Easy as pie", and "Piece of cake" to a Russian, who
kept getting it wrong. Where it started was when Dave Taht tried to
explain the need for a comprehensive queue management system to an
audience in the ietf aqm working group, and was basically booed off the
stage.

Later on it became a reference to the game "portal" - where, at the
conclusion of the game, the AI promises that: "everyone will have cake".

It is also (in a grand tradition of RED vs Blue) a backhanded reference
to "Pie", which is a competing AQM algorithm missing many of the
features of cake.

The backronym invented for it became "Common Applications Kept Enhanced"
- which is also, actually, exactly what it does.

Despite our affection for the name there is still time to change it to
something else - googling for "cake shaper" does not result in anything
useful. CQM, SQM would seem to have more useful google-fu, but...

<!-- not yet answered
When should I use cake?
-----------------------

cake vs fq\_codel
-----------------

-->

enabling cake
-------------
### Changing to the cake qdisc: ###
```
tc qdisc replace dev eth0 root cake ethernet bandwidth 1gbit
```  
Any unmentioned parameter will be set to 
a sane default.
It assumes you have cake available in your kernel.

### Changing settings in real time: ###
```
tc qdisc change dev eth0 handle 1: cake bandwidth 1Mbit
```   
This does _not_ cause packet loss.
