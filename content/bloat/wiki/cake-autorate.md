---
title: cake-autorate
date: 2024-07-21T08:30:13
lastmod: 2024-07-21T10:00:13
type: wiki
aliases:

---
# _cake-autorate_ for variable rate links


**Background:** The CAKE algorithm
controls bufferbloat well on constant rate links
by using fixed upload and download rate parameters to control
the amount of queued data.
But many links, such as
LTE cell-phones, cable modems, and Starlink
have rates that vary from morning to evening,
or even from minute to minute.
Because CAKE uses fixed parameters, 
it forces an 
[unpalatable compromise](https://github.com/lynxthecat/cake-autorate/blob/master/README.md#the-problem-cake-on-variable-speed-connections-forces-an-unpalatable-compromise)
because it can't adapt to these varying-rate links.

**Solution:** The **cake-autorate** algorithm continually measures
the current latency and adjusts the parameters
of CAKE to minimize latency.

The **cake-autorate** repo is on 
[Github](https://github.com/lynxthecat/cake-autorate/tree/master)
with an active community on the
[OpenWrt forum](https://forum.openwrt.org/t/cake-w-adaptive-bandwidth/191049).
Here's an excerpt from the
[README](https://github.com/lynxthecat/cake-autorate/blob/master/README.md)

> **cake-autorate** is a script that automatically adjusts CAKE
bandwidth settings based on traffic load and one-way-delay or
round-trip-time measurements. cake-autorate is intended for variable
bandwidth connections such as LTE, Starlink, and cable modems and is
not generally required for use on connections that have a stable,
fixed bandwidth.
> 
> [CAKE](https://www.bufferbloat.net/projects/codel/wiki/Cake/) is an
algorithm that manages the buffering of data being sent/received by a
device such as an [OpenWrt router](https://openwrt.org) or an
[Asus Merlin router](https://www.asuswrt-merlin.net/) so that no more
data is queued than is necessary, minimizing the latency
("bufferbloat") and improving the responsiveness of a network. An
instance of cake on an interface is set up with a certain bandwidth.
Although this bandwidth can be changed, the cake algorithm itself has
no reliable means to adjust the bandwidth on the fly.
**cake-autorate** bridges this gap.
> 
> **cake-autorate** presently supports installation on devices running
OpenWrt and Asus Merlin.
> 
> ### Status
> 
> This is the **development** (`master`) branch. New work on
cake-autorate appears here. It is not guaranteed to be stable.
> 
> The **stable version** for production/every day use is
<span id="version">3.2.1</span> available from the
[v3.2 branch](https://github.com/lynxthecat/cake-autorate/tree/v3.2).
