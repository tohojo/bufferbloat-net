
---
title: Experiment-Fun_with_wireless
date: 2011-02-02T17:02:24
lastmod: 2011-04-11T09:14:08
---
Experiment-Fun with wireless
============================

I encourage you to perform this experiment, which many of you open
source readers can likely perform as you read this entry.

By the end of this exercise, you’ll agree with my conclusion: Your home
network can’t walk and chew gum at the same time.

You can perform all but parts of experiment 3 on commercial routers;
I’ve seen similar results on a Cisco e3000, Dlink DIR-825revA and
others. An open source router, however, will allow us to diagnose (at
least part of) the problem more definitively. I suspect more recent home
routers may behave worse than old home routers; but as my old routers
have been blown up by lightning, I can’t test this hypothesis.

Here’s my experiment configuration:

computer 802.11 &lt;~~802.11~~&gt; Router &lt;~~ethernet~~&gt; server
computer

Seems pretty simple, doesn’t it? For completeness sake, I’ll more
carefully document the configuration, not that I think it matters much,
though may change the details of the results; feel free to substitute
your own gear arbitrarily:

\* The server system is connected to the router via GigE.\
\* The test computer is an HP EleteBook 2540p running Linux 2.6.36-rc5,
and uses a Intel Centrino Advanced-N 6200 AGN, REV=0×74

The test computer was sitting about 4 feet away from the router; my
local radio environment is quiet; you will see the most interesting
results for reasons I cover in the next installments on such a quiet
network. A commercial home router should suffice for experiment 2:
you’ll need an open source router (or be able to log in to your router)
to perform parts of experiment 3 below.

Experiment 2a:
--------------

ping -n server & scp YourFavoriteBigFile server:

YourFavoriteBigFile needs to be large, say 100Mbytes or more, so the
copy will take more than a few seconds. You can use nttcp as well if you
have installed it in Experiment 1 (but it will take a bit longer to
reach full effect, I believe). Your favorite distro’s ISO image will do
fine.

How much buffering should we expect to keep TCP busy? For a single flow
like this, over 802.11g (presuming we can actually get about 25Mbps, and
a delay of 1ms, we’d expect to need no more than the bandwidth x delay
product. This is about 2 packets; it makes sense we need to always have
a second packet available to keep the wireless link busy. You’d expect
an extra millisecond of queuing delay for the ICMP ping packet (which
has an almost negligible size)

What do you observe?

I observe latencies that increase the longer the TCP session goes on,
reaching up to about 600 or more milliseconds after about 20 seconds on
Linux, but with very high jitter. Pinging the server from a second
machine shows little increase in latency.

Why is this occurring? Ah, dear Watson, that is the question….

Experiment 2b:
--------------

As in Experiment 1, reduce your txqueuelen to zero in several steps
(e.g.”ifconfig wlan0 txqueuelen 0“). What do you observe? I observe
about 100ms latency, with significant jitter.

Unfortunately, my wireless NIC does not support the “-g” and “-G”
options we explored in Experiment 1. So I cannot try reducing the
transmit ring. If yours does, I encourage you to to try twisting that
knob as in the first experiments. hypothesize my wireless NIC has a
transmit ring of order the same size as the ethernet NIC we explored in
Experiment

Experiment 2c:
--------------

Move the test computer further from the router, until, say, you can only
6 Mbps of bandwidth (your actual
[goodput](http://en.wikipedia.org/wiki/Goodput) will be less; remember,
just because your radio is signalling at 6Mbps doesn’t mean you are able
to get that much actual wireless bandwidth).

Remember to set your txqueuelen back to its original value (e.g.
﻿﻿”ifconfig wlan0 txqueuelen 1000“, for my laptop).

Run the experiment again. What do you observe? Why? I observe up to
several seconds of latency; the lower the bitrate, the higher the
latency.

Experiment 2d:
--------------

Third experiment (while still remote enough the bandwidth available is
low).

Try web browsing in another window, during the copy. What do you think
of this result? I don’t think you will like it at all. I sure don’t.

Experiment 2e:
--------------

As in Experiment 1, reduce your txqueuelen to zero in several steps
(e.g.”ifconfig wlan0 txqueuelen 0“). What do you observe?

I observe the latency drop to only a bit over a hundred milliseconds
(but with substantial jitter.

Unfortunately, my wireless Intel NIC does not support the “-g” and “-G”
options So I cannot try reducing the transmit ring in the wireless
device as I could on ethernet. I hypothesize a similarly large ring for
the wireless chip.

Experiment 3a-3d:
-----------------

Repeat experiment 2, but copy YourFavoriteBigFile from your server back
to your system. Make sure that there is more bandwidth from where you
are copying from than the wireless link.

On a Linksys E3000 router running commercial firmware, my latencies
reach 500ms or more, with high jitter at 54Mbps data-rate, with high
ping packet loss when pinging from the transmitting direction. ﻿﻿On a
Netgear WNDR3700, running OpenWRT 10.03, changing txqueuelen seems to
have no effect, but the latency is stuck at around 200ms. In a quick
test at 6Mb/second, I observed 4 second (highly variable) latency; at
12Mb/second, I observe about 2 second (highly variable) latency.

Note that twisting the txqueuelen knob (and/or transmit rings) on your
laptop has no effect, but by logging into your router and twisting the
knob, you may (or may not be able to) eliminate most of the latency. On
a Linksys WRT-54TM running <link>Gargoyle</link> router code version
1.3.8, I can reduce the latency (when at 54Mbps) from of order 1 second
(with high jitter) to around 20ms by setting txqueuelen to 10 on wl0
(you can’t go to zero on this hardware, I surmise). This is still higher
than it should be from first principles, but closer to something
tolerable.

Conclusion of Experiments 1-3
-----------------------------

Your home network can’t walk and chew gum at the same time.

See Also
========
