
---
title: Experimental_patches
date: 2011-04-17T07:57:26
lastmod: 2011-04-17T07:57:26
---
Experimental patches
====================

<nbd> if you want to play with this, copy these two patches to\
package/mac80211/patches and rebuild the kernel: \[20:12\]\
<nbd> http://nbd.name/570-ath9k\_aggr\_cleanup.patch\
http://nbd.name/571-ath9k\_limit\_qlen.patch\
<nbd> then you can go to /sys/kernel/debug/ieee80211/phy\*/ath9k/\
<nbd> and write queue length limits to qlen\_aggr and qlen\_single
\[20:13\]\
<nbd> (default is 0: disabled)

btw. here's my latency comparison (with one iperf TCP stream)\
<nbd> http://pastebin.com/CQh9AjkN
