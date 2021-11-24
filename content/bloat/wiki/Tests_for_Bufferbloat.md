---
title: Tests for Bufferbloat
date: 2013-12-20T14:59:13
lastmod: 2021-11-24T08:03:00
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

## Easy: Web-based Tests

The web-based tests [DSL Reports Speed Test](http://DSLReports.com/speedtest) and
[Waveform Bufferbloat Test](https://www.waveform.com/tools/bufferbloat) 
make accurate measurements of the download and upload speeds 
along with the latency *during* the test. 
Share the "letter grade" with your friends. Watch the
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
    -   http://fast.com 
    -   http://speedtest.net
    -   http://testmy.net
    -   http://speedof.me
3.  Watch the ping times while the speed test is running. If the times jump
    up when uploading or downloading, then your router is probably bloated.

## The Best Tests for Bufferbloat

The suite of tests we developed to diagnose bufferbloat and other
connectivity problems are good to 40GigE, but require the
[Flent RRUL test suite](https://flent.org) 
Using the Flent tools, it is possible to get a good feel for how the connection is
behaving while you tune your settings. 

## Other network performance and latency tools

1. Apple's [**RPM Tool**](https://www.ietf.org/id/draft-cpaasch-ippm-responsiveness-01.html)
measures responsiveness directly by
fully loading the network and measuring the number of responses
received in a fixed time.
"Responsiveness" is the inverse of latency, and is more intuitive
since a large value indicates good responsiveness.
(As opposed to large _latency_ values that indicate _poor_ responsiveness.)
2.  The **[Quick Test](#a-quick-test-for-bufferbloat)** (described above) does a rudimentary job of
    measuring performance. Although it may not run long enough to avoid
    the effects of Powerboost or other special cases implemented by
    ISPs, it can definitely point out situations where
    you're "bufferbloated".
3.  **[betterspeedtest.sh](https://github.com/richb-hanover/OpenWrtScripts/blob/master/betterspeedtest.sh)** from [OpenWrtScripts bundle](https://github.com/richb-hanover/OpenWrtScripts/blob/master/README.md)
    is a script you can run on Linux/OSX or on OpenWrt to get
    concrete, repeatable tests of your network. It performs the same
    kind of download/upload test that is available from speedtest.net.
    It is better, though, because it continually measures your ping
    latency, and thus lets you know the performance and latency of each
    direction of data transfer. 
4.  The **[netperfrunner.sh](https://github.com/richb-hanover/OpenWrtScripts/blob/master/netperfrunner.sh)** script (part of the OpenWrtScripts bundle) 
    simulates the [RRUL test](https://www.bufferbloat.net/projects/codel/wiki/RRUL_test_suite)
    by creating four simultaneous upload and download streams. This
    measures latency during heavy load. (also originally part of the CeroWrtScripts bundle)
5.  [**Flent**](https://flent.org) is a tool designed to make
    consistent and repeatable network measurements. Its suite of tests, 
    including RRUL, log the data, and produce attractive
    graphs of the results. (RRUL specifies that multiple netperf
    sessions run simultaneously to heavily load the network in
    both directions.)
6. [**netperf**](https://hewlettpackard.github.io/netperf/)
creates traffic through a network and measures its performance.
netperf underlies _betterspeedtest.sh_, _netperfrunner.sh_, and Flent,
and can be installed in the the OpenWrt firmware.
7. [**iperf2**](https://sourceforge.net/projects/iperf2/) and
[**iperf3**](https://github.com/esnet/iperf#iperf3--a-tcp-udp-and-sctp-network-bandwidth-measurement-tool)
measure network performance.
Despite the similar names, they are not compatible.
Both are under active development:
check each tool's website for a comparison of their capabilities.
8. [**fast.com**](https://fast.com) now tests for latency under load
(cick the "Show more info" button.)
Also see their [press release.](https://media.netflix.com/en/company-blog/fast-com-now-measures-latency-and-upload-speed) 
