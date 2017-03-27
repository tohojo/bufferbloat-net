---
title: Tests for Bufferbloat
date: 2013-12-20T14:59:13
lastmod: 2015-05-16T11:09:17
type: wiki
aliases:
  - /cerowrt/wiki/Quick_Test_for_Bufferbloat
---
# Tests for Bufferbloat

Does the quality of your web browsing, voice call, or gaming degrade
when someone's downloading or uploading files? It may be that your
router has "bufferbloat" - unnecessary latency/lag created by your
router buffering too much data.

If the tests below show high latency (say, above 50 msec), 
read our recommendations at
[What can I do about Bufferbloat](What_can_I_do_about_Bufferbloat.md)

## _Easy_ Test for Bufferbloat

The [DSL Reports Speed Test](http://DSLReports.com/speedtest)
    makes accurate measurements of the download and upload speeds 
    along with the latency *during* the test. 
    The "Results + Share" button lets you see the numerical results 
    or pass along a link to your friends. Watch the
    [Bloat](https://youtu.be/EMkhKrXbjxQ) / [No
    Bloat](https://youtu.be/Fq9nQf1yEm4) videos at
    [Youtube](https://youtu.be/EMkhKrXbjxQ) to see how the test works.

## A Quick Test for Bufferbloat

Other speed test sites only measure latency when the link is idle - and
that only tells part of the story. You **can** get numeric latency measurements with
those other speed test sites if you run a ping test simultaneously. To do this:

1.  Start a ping to google.com. You'll see a series of lines, one per
    ping, typically with times in the 20-100 msec range.
2.  Run a speed test simultaneously. To do this, start one of the speed
    test services below:
    -   http://speedtest.net
    -   http://testmy.net
    -   http://speedof.me

3.  Watch the ping times while the speed test is running. If the times jump
    up when uploading or downloading, then your router is probably bloated.

## The Best Tests for Bufferbloat

The suite of tests we developed to diagnose bufferbloat and other
connectivity problems are good to 40GigE, but require the
[Flent RRUL test suite](https://flent.org) 
(Flent was previously named "netperf-wrapper".) 
Using the Flent tools, it is possible to get a good feel for how the connection is
behaving while you tune your settings. 

## Other network performance and latency tools

1.  The **[Quick Test](#a-quick-test-for-bufferbloat)** (described above) does a rudimentary job of
    measuring performance. Although it doesn't run long enough to avoid
    the effects of Powerboost or other special cases implemented by
    ISPs, it can definitely point out situations where
    you're "bufferbloated".
2.  **[betterspeedtest.sh](https://github.com/richb-hanover/CeroWrtScripts/blob/master/betterspeedtest.sh)** from [CeroWrtScripts bundle](/cerowrt/wiki/CeroWrtScripts.md)
    is a script you can run on Linux/OSX or on CeroWrt to get
    concrete, repeatable tests of your network. It performs the same
    kind of download/upload test that is available from speedtest.net.
    It is better, though, because it continually measures your ping
    latency, and thus lets you know the performance and latency of each
    direction of data transfer. 
3.  The **[netperfrunner.sh](https://github.com/richb-hanover/CeroWrtScripts/blob/master/netperfrunner.sh)** script (also part of the CeroWrtScripts bundle) 
    simulates the [RRUL test](https://www.bufferbloat.net/projects/codel/wiki/RRUL_test_suite)
    by creating four simultaneous upload and download streams. This
    measures latency during heavy load.
4.  [**Flent**](https://flent.org) is a tool designed to make
    consistent and repeatable network measurements. Its suite of tests, 
    including RRUL, log the data, and produce attractive
    graphs of the results. (RRUL specifies that multiple netperf
    sessions run simultaneously to heavily load the network in
    both directions.)
5.  The [**netperf**](http://netperf.org/netperf/) program underlies
    _betterspeedtest.sh_, _netperfrunner.sh_, and Flent, and is built into
    the CeroWrt firmware. netperf drives traffic through a network and measures its performance.
6.  **[Netalyzr](http://netalyzr.icsi.berkeley.edu/)** from icsi.berkeley.edu is a powerful network
    measurement and diagnostic tool that contributes its data to a large
    survey of network conditions. However, we have seen its estimate of bufferbloat
    can be inaccurate: even though netalyzr reports a 1000 msec
    "buffer measurement", a concurrent ping test does not show an
    appreciable change to the responsiveness.
    

