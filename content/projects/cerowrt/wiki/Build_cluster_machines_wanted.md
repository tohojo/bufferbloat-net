
---
title: Build cluster machines wanted
date: 2012-08-13T09:12:23
lastmod: 2012-08-13T09:15:48
type: wiki
---
Build cluster machine donations wanted
======================================

Got any spare multicore xeon or better boxes with tons of ram and disk?

When the build for openwrt breaks, everyone suffers. Development for
openwrt and subsidiary projects such as cerowrt, dd-wrt, gargoyle,
buffalo, etc - comes to a screeching halt. Worse when builds break it
tends to be a period of high volume of commits. Breakage can sometimes
take days to resolve, as individual builds can take as long as 20 hours
to build serially on non-optimized hardware (the record on top of the
line stuff is about 10 hours). During the breakage, dozens of developers
twiddle their thumbs and have to improvise around the problems in order
to get their individual tasks done.

So although the openwrt organization maintains [a buildbot
cluster](http://buildbot.openwrt.org/tgrid), it is sorely under-sized,
and always in need of expansion and love.

[ISC](http://www.isc.org) has set aside a portion of rack space for us,
but we lack machines to fill it. ISC has also loaned 3 machines to the
effort and Dave Taht (after being crippled one too many times by build
breakage) donated his top end 12 core desktop to the effort, too. Even
with these donations in play, much better results could be obtained by
10 or more high end machines in the cluster, reducing cycle time from 3
or more days to under a day. Presently there are about 4 other machines
loaned by individuals from their homes, in the cluster, too.

-   Hardware Requirements

Doing software builds is a very compute and disk intensive task. The ROI
on doing compute on an EC2 instance is much worse than doing it on a
string of dedicated nearly-top-of-the-line boxes.

If you have a decent machine you can loan, even part time to the effort,
please contact travis kemen (thepeople on irc, and thepeople *AT*
openwrt.org). However a celeron won't cut it!

An ideal box has at least 4 cores, 16GB of ram, and 2TB of disk. An SSD
is highly desirable, and with more ram, the bulk of a build can be done
in memory. Also, as the end result is over a gb of files that need to be
uploaded, reasonable upload bandwith is useful.

If we did sane cost accounting for electricity and rack space, a single
64GB box with 12 cores is far more cost effective than 3 boxes with 16GB
ram and 4 cores each, but we don't, and it's the up-front capital
expense here, not the ongoing expense, that is making this part hard.
(we've been trying to find a suitable donor for hardware for over a
year)

(We're not allergic to donated compute time on a cluster instance,
either, it's just not cost-effective from our perspective to actually
buy any ourselves.)
