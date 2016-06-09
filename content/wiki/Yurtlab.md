
---
title: Yurtlab
date: 2012-10-01T21:55:12
lastmod: 2012-10-22T14:48:20
---
Campground Field Test
=====================

![](http://huchra.bufferbloat.net/~cero1/yurtlab_sm.jpg)

Over the course of the past year, we searched for a location devoid of
wifi signals, so that we could explore, test, and benchmark wifi without
interference from other signals. This proved remarkably hard. No matter
where we went in the world, there was ALWAYS at least one AP with a
competing signal on the channel. We gradually devolved into testing 5ghz
only, where we could usually find clear air on some channel or another.
2.4ghz was simply not benchmarkable with any consistency.

Testing with competing wifi signals is definitely on the agenda, but
first getting a clean setup was not optional.

Then summer hit, [bloatlab 1]({{< relref "wiki/BloatLab_1.md" >}}) became too hot to inhabit, and
campground with 110 acres high in the Santa Cruz mountains, asked if we
could fix their wifi, so long as it didn't cost them anything. SCORE!

-   Convienent location to the Valley
-   No competing wifi signals
-   Multiple (mostly comcast) connections to the internet
-   Challenging terrain: Various areas can be isolated from each other,
    and wifi fiddled with at varying distances
-   Range of random multi-platform workloads from nearly nothing (during
    the week) to hundreds (weekends)
-   Overnight facilities for guests
-   Onsite pool, piano, and hottub

So this site ended up being the site of the first-ever test fq\_codel
and quagga-babeld deployment on wifi and ethernet, on real hardware, in
June of 2012. It was moderately successful, and feedback from various
use patterns and tests resulted in a serious push to make cerowrt more
stable than it was, and the fq\_codel algorithm less memory intensive.

The June-August campground testbed consisted of 5 directional 5ghz
nanostation 5MPs, 3 picostation 2HPs, 4 cerowrt wndr3700s, 1 cerowrt
wndr3800. All the devices were upgraded to then-current openwrt + the
current cerowrt kernels, excercised heavily, and various workloads
analyzed.

The plan was to expand the network to a ring of 8-10 5MPs covering the
entire property, 6 picostation 2HPs, and add a fully fq\_codel'd set of
firewalls and RTT simulators using donated vyatta hardware... as well as
a parallel test backbone and produce a multi-exit-fq-codel - but [money
ran out in August](http://www.teklibre.com/cerowrt/subscribe.html), and
we ran into some pesky bugs that are now mostly resolved as of the
"sugarland" release of cerowrt.

A revamped design along the above lines is being put together for
deployment early in 2013.

NOTE: To preserve the privacy of the site and the users, raw data
regarding various tests will not be made available.
