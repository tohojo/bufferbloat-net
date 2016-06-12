
---
title: "Codel on Cerowrt-3.3.6-2"
date: 2012-05-14T13:56:28
type: news
author: Dave Täht
---
A test release of CeroWrt is now available that has support for Kathie
Nichols' and Van Jacobson's new AQM,
[Codel](http://www.bufferbloat.net/projects/codel/) , and Eric Dumazet's
new fair queuing implementation on top of that, fq\_codel.

fq\_codel is enabled on all interfaces by default. It is vastly simpler
than what we were using before (sfqred) and draws upon and improves on
the same body of ideas (head drop, fq, timestamping) but now tied to
Kathie and Van's blinding insights as to a good drop strategy, and
Eric's successor ideas as towards head of queue behavior and cache line
optimizations.

There is a simple\_qos.sh script that can be set to your uplink and
downlink speeds, but no uci interface for it as yet, nor gui. (help on
finishing aqm-scripts and the luci interface gladly accepted)

To see all the chocolately goodness of what fq\_codel can do to wired
and wireless latency, it would be good for more to play with it.

Benchmarks have been very good thus far, and more benchmarks and
analysis are highly desired.

Caveat:

This release suffers from an unrelated bug ( \#379 ) and should NOT be
installed as your main router. I would love to beat this bug because
it's the only prio 1 remaining but thus far, no luck. Under lighter
loads CeroWrt appears to work just fine, but that's for me. YMMV.

Get it here: http://huchra.bufferbloat.net/\~cero1/3.3/3.3.6-2/
