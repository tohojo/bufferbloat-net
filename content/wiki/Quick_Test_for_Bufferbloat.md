
---
title: Quick_Test_for_Bufferbloat
date: 2013-12-20T14:59:13
lastmod: 2015-05-16T11:09:17
---
Quick Test for Bufferbloat
==========================

Does the quality of your web browsing, voice call, or gaming degrade
when someone's downloading or uploading files? It may be that your
router has "bufferbloat" - unnecessary latency/lag created by your
router buffering too much data.

***Easy* Tests for Bufferbloat**

-   The speed test at [DSL Reports.com](http://DSLReports.com/speedtest)
    measures the download and upload speeds along with the latency
    *during* the test. The "Results + Share" button lets you see
    numerical results or pass along a link to your friends. Watch the
    [Bloat](https://youtu.be/EMkhKrXbjxQ) / [No
    Bloat](https://youtu.be/Fq9nQf1yEm4) videos at
    [Youtube](https://youtu.be/EMkhKrXbjxQ) to see how the test works.

<!-- -->

-   The speed test at
    [ThinkBroadBand](http://www.thinkbroadband.com/speedtest.html)
    provides latency measurements during the download and upload, also
    with sharable links.

**A Quick Test for bufferbloat:**

Other speed test sites only measure latency when the link is idle - but
that only tells part of the story. You **can** measure bufferbloat with
those other sites if you run a ping test simultaneously. To do this:

1.  Start a ping to google.com. You'll see a series of lines, one per
    ping, typically with times in the 20-100 msec range.
2.  Run a speed test simultaneously. To do this, go to one of the speed
    test services below and start the test.
    -   http://speedtest.net
    -   http://testmy.net
    -   http://speedof.me

3.  Watch the ping times while the speed test is running.

The Best Tests for bufferbloat:
-------------------------------

The suite of tests we developed to diagnose bufferbloat and other
connectivity problems are good to 40GigE, but require the
[netperf-wrapper rrul test
suite](https://github.com/tohojo/netperf-wrapper) . Using the tools
therein it is possible to get a good feel for how the connection is
behaving while [you tune a shaper to fix
it](http://snapon.lab.bufferbloat.net/~cero2/jimreisert/results.html).

**Is My Router Bufferbloated?**

-   A good router that protects against bufferbloat will hold the
    induced latency (extra latency above the no-traffic latency) below
    30 msec.
-   Above 100 msec, people will notice that the network feels slow:
    voice calls will begin to sound bad, web browsing feels sticky, and
    you start to lag out when gaming.
-   If ping times get high while the speed test is running and drop back
    down when the speed test completes, it means your router is bloated.
    You have probably noticed that the network feels draggy or slow when
    other people use the network.
-   What can you do? Read on...

What can I do about Bufferbloat?
--------------------------------

We have created a set of recommendations for eliminating Bufferbloat at
<link>What to do about Bufferbloat</link>

Other tools for measuring network performance and latency
---------------------------------------------------------

1.  The **Quick Test** (described above) does a rudimentary job of
    measuring performance. Although it doesn't run long enough to avoid
    the effects of Powerboost or other special cases implemented by
    ISPs, it can definitely point out situations where
    you're "bufferbloated".
2.  **<span
    style="text-align:left;">link&gt;CeroWrtScripts|betterspeedtest.sh</link></span>**
    is a script you can run on your computer or on CeroWrt to get
    concrete, repeatable tests of your network. It performs the same
    kind of download/upload test that is available from speedtest.net.
    It is better, though, because it continually monitors your ping
    latency, and thus lets you know the performance and latency of each
    direction of data transfer. It is part of the
    <link>CeroWrtScripts|CeroWrtScripts bundle.</link>
3.  The **netperfrunner.sh** script (also part of the
    <link>CeroWrtScripts|CeroWrtScripts bundle</link>) simulates the
    [RRUL
    test](https://www.bufferbloat.net/projects/codel/wiki/RRUL_test_suite)
    by creating four simultaneous upload and download streams. This
    measures latency during heavy load.
4.  Both betterspeedtest.sh and netperfrunner.sh use the
    [**netperf**](http://netperf.org/netperf/) program (built
    into CeroWrt) to drive traffic to see its performance.
5.  [**netperf-wrapper**](https://github.com/tohojo/netperf-wrapper) is
    a handy tool for running the RRUL test and producing attractive
    graphs of the results. (RRUL specifies that multiple netperf
    sessions run simultaneously to heavily load the network in
    both directions.)
6.  **Netalyzr** from icsi.berkeley.edu. This is a powerful network
    measurement and diagnostic tool that contributes its data to a large
    survey of network conditions. However, its estimate of bufferbloat
    is often inaccurate: even though netalyzr measures a 1000 msec
    "buffer measurement", a concurrent ping test does not show an
    appreciable change to the responsiveness. Try it at
    http://netalyzr.icsi.berkeley.edu/

