---
title: CAKE-Maint
date: 2025-02-19T15:38:14
lastmod: 2025-02-19T15:38:14
type: wiki
tags: ecn-yellow

---

# The CAKE-Maint project
##  The lower latency Internet is here… it just needs a little maintenance. 

Bufferbloat.net is proud to announce the CAKE-MAINT project, with funding (so far) from NLnet/NGI0 and data center support from Equinix Metal. With the explosion of fq_codel and CAKE enabled devices in production today (now numbered in the billions) since we last worked on the codebases 7 years ago, many bugs have cropped up in the field, many new features have been requested, and new research is needed to manage new network requirements. 

The goals of this project are to try and organize and test those bug fixes, establish reference benchmarks, and then attempt to move the technologies forward once again.

“This is a KEY open source project in the Internet, and needs sufficient funding to continue maintenance of the code itself as Linux changes, but also to incorporate improvements.” - Dave Reed

Like any open source project, further donations, support in-kind, and testing are all appreciated.

From Kathleen Nichols - "We live in a world where codebases need to be constantly updated or else die. Great to see that work can continue to keep fq_codel alive."

From Michiel Leenaars, director of Strategy at NLnet Foundation: “Sometimes more reliable and more performant internet isn’t just a luxury. The original Bufferbloat project made a big leap possible already, but now it is time to revisit that work with the lessons learned since. It is great to see CAKE used as the default shaper in OpenWrt and within major efforts like LibreQoS - but we need to make sure its benefits are available more consistently across chipsets and operating systems.“

From John Carmack - "Despite the high bandwidths our systems are often delivering today, picky low-level details sometimes make the delivered experience much worse than it could be. Besides the obvious latency and jitter sensitive applications like gaming and videoconferencing, the tide of technology has pushed (for better or worse) almost everything towards distributed computing at some level, and we accept weirdly variable performance as "just the way things are". These are not marketing friendly metrics, and fighting for improvements has been a hard and largely thankless job, but progress has been made, and more is available."

There are bugs in the fq_codel versions on FreeBSD, OpenBSD, and MacOS, and multiple bugs in the fq_codel for wifi versions for OpenWrt. Cake itself is too slow to push 1Gbit on A53 cores - and some of CAKE´s features should end up in fq_codel! And In WiFi. Backward compatibility with L4S is also needed. And to truly scale CAKE, it needs to shape across multiple cores!

“If you hate it when apps or users sharing a link interfere with each other so badly that they create more congestion than throughput, you need stricter and smarter queue disciplines and you need all other networks to have the same. Fq_codel and cake and libreqos everywhere is how we can do that.” - Paul Vixie

