---
title: RRUL Rogues Gallery
date: 2013-01-14T13:13:11
lastmod: 2013-08-11T17:28:30
type: wiki
---
RRUL Rogues Gallery
===================

This is a web page dedicated to showing off and explaining some results
obtained via (early) prototypes of the [RRUL test suite](RRUL_test_suite.md).

Yurtlab testing (comcast 20Mbit up 8Mbit down)
----------------------------------------------

Various fq\_codel based rate shaping prototypes are under test at the
[Yurtlab](/cerowrt/wiki/Yurtlab.md).

### NFQ\_Codel with HTB rate limiting vs PFIFO\_FAST

An initial test of the comcast based connection, using standard drop
tail and no other optimizations:

![](/attachments/campground/campground_pfifo_fast.svg)

After rate shaping was employed via [this HTB + nfq\_codel
script](/attachments/campground/lupin_qos.sh) ,
which gives EF packets a max of 33% of the bandwidth, and background
traffic a max of 20% under contention, this is what that network now
looks like:

![](/attachments/campground/campground_lupin_qos.svg)

Bandwidth went up, and more importantly the increase in latency under
load dropped to less than 4ms on average. However averages are
misleading, and a RRUL CDF plot is more accurate.

![](/attachments/campground/cdf1.svg)

It was actually impossible to get an accurate measure of the actual
bandwidth available using the non-rate shaped version! Using the RRUL
test and changing the rate shaping parameters, it became possible to get
an accurate measurement of what was actually available on this link. IT
was rated for 22 Mbit down, 2Mbit up, and the actual performance
achieved was very, very different, closer to 20Mbit down, 8 up.

This is fq\_codel, by itself, without rate shaping, on this link:

![](/attachments/campground/campground_fq_codel.svg)

Although the results are more "fair", they aren't very much more fair.
Most of the buffering moved into the cable modem and CMTS where it was
unmanaged. You have to take back control of the buffering into your own
device in order for this stuff to work, by setting your rate a little
bit below the provided rate.

### Two RRUL tests, competing

It is perhaps more illustrative than RRUL alone, to run it twice. In
this test series a second copy of the RRUL test was run at T+30 seconds,
and the first RRUL test extended to run for 120 seconds (-H 120)

![](/attachments/campground/campground_lupin_qos-competing-120.svg)

As you can see, the second test kicks in quite rapidly, and when
complete, the other test scales back up to full bandwidth, quite
rapidly.

![](/attachments/campground/campground_pfifo_fast-competing-120.svg)

In the above test the second test doesn't ramp up to full bandwidth for
over 20 seconds after test start, and the TCP streams are very "unfair"
relative to each other.

For more detail on these tests see
http://snapon.lab.bufferbloat.net/\~d/campground/

Verizon FIOS Testing at 25Mbit up and 25Mbit down
-------------------------------------------------

Before a fq\_codel enabled shaper is deployed:

![](/attachments/verizon-noshaper-ipv4-icei.svg)

Verizon seems to have egress buffering under control, but probably has
an ingress buffer set to a good value for their highest end 300Mbit
service.

After a fq\_codel enabled shaper is deployed:

![](/attachments/verizon-finalshaper-ipv4-icei.svg)

5 times the upload bandwidth, and roughly 1/7 the observed latency.

TCP Global Synchronization
--------------------------

One interesting result obtained along the way was a textbook case of
[TCP Global
Synchronization](http://en.wikipedia.org/wiki/TCP_global_synchronization)
where multiple streams would synchronize, collapse, and restart at the
same time. This is the behavior that the RED algorithm and successors in
particular were designed to avoid... if they had ever been deployed. The
second chart in this image shows what TCP global sync looks like.

![](http://huchra.bufferbloat.net/~d/denmark-germany-wired-2.png)

These results were obtained over a 40ms link between Denmark and
Germany, on a device that probably had a very short TXQUEUE. So this is
what can happen if buffers are too small, rather than "just right".

Different forms of TCP
----------------------

Competing RTT
-------------

IPv6 vs IPv4
------------
