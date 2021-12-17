---
title: Tests for Bufferbloat
date: 2013-12-20T14:59:13
lastmod: 2021-12-07T08:03:00
type: wiki
aliases:
  - /cerowrt/wiki/Quick_Test_for_Bufferbloat
---
# Tests for Bufferbloat

Does the quality of your web conference, voice call, or gaming
get bad from time to time?
Do you ever tell others "Don't use the internet!"
because it might affect what you're doing?
If so, your router may have "bufferbloat" -
unnecessary latency/lag created by your
router buffering too much data.

The tests below check for the presence of bufferbloat.
If any show high latency (say, above 50 msec,
or a grade lower than "B"),
read our recommendations at
[What can I do about Bufferbloat?](What_can_I_do_about_Bufferbloat.md)

## Easy: Web-based Tests

The web-based tests
[DSL Reports Speed Test](http://DSLReports.com/speedtest) and
[Waveform Bufferbloat Test](https://www.waveform.com/tools/bufferbloat) and
[Fast.com](https:/fast.com) (click the "Show more info" button)
make accurate measurements of the latency *during*
the download and upload parts of the test.
This demonstrates the responsiveness of your network. 
Share the "letter grade" with your friends. Watch the
[Bloat](https://youtu.be/EMkhKrXbjxQ) /
[No Bloat](https://youtu.be/Fq9nQf1yEm4) videos at
[Youtube](https://youtu.be/EMkhKrXbjxQ) to see the test in action.

## Quick: Test for Bufferbloat

If you want to observe latency under load ("bufferbloat") for yourself,
try this:

1.  Start a ping to google.com. You'll see a series of lines, one per
    ping, typically with times in the 20-100 msec range.
2.  Start a speed test from one of the speed test services below
while the pings continue:
    -   [http://fast.com](http://fast.com) 
    -   [http://speedtest.net](http://speedtest.net)
3.  Watch the ping times while the speed test is running. If the times jump
    up when uploading or downloading, then your router is probably bloated.

## Best: Bufferbloat Tests

The suite of tests we developed to diagnose bufferbloat and other
connectivity problems are good to 40GigE, but require the
[Flent RRUL test suite.](https://flent.org) 
Using the Flent tools, it is possible to get a good feel
for how the connection behaves while you tune your settings. 

## Other network performance and latency tools

1. Apple's [**RPM Tool**](https://www.ietf.org/id/draft-cpaasch-ippm-responsiveness-01.html)
measures responsiveness directly by
fully loading the network and measuring the number of responses
received in a fixed time.
"Responsiveness" (measured in round-trips per minute - "RPM")
is a value ranging from around one hundred (poor) to a few thousand (good).
2.  [**Flent**](https://flent.org) is a tool designed to make
consistent and repeatable network measurements.
Its suite of tests 
log the data, and produce attractive graphs of the results.
Flent's [RRUL test](https://www.bufferbloat.net/projects/bloat/wiki/RRUL_Chart_Explanation/)
runs multiple netperf sessions simultaneously to heavily load 
the network in both directions.
3. [**netperf**](https://hewlettpackard.github.io/netperf/)
creates traffic through a network and measures its performance.
Various tools, such as _betterspeedtest.sh_, _netperfrunner.sh_, and Flent,
rely on netperf, which can be installed in the the OpenWrt firmware.
4.  **[betterspeedtest.sh](https://github.com/richb-hanover/OpenWrtScripts/blob/master/betterspeedtest.sh)**
from [OpenWrtScripts bundle](https://github.com/richb-hanover/OpenWrtScripts/blob/master/README.md)
    is a script you can run on Linux/OSX or on OpenWrt to get
    concrete, repeatable tests of your network. It performs the same
    kind of download/upload test that is available from speedtest.net.
    It is better, though, because it continually measures your ping
    latency, and thus lets you know the performance and latency of each
    direction of data transfer. 
5.  The **[netperfrunner.sh](https://github.com/richb-hanover/OpenWrtScripts/blob/master/netperfrunner.sh)**
script (part of the OpenWrtScripts bundle) simulates the
RRUL Test by creating four simultaneous upload and download streams.
This measures latency during heavy load in both directions.
6.  The **[Quick Test](#a-quick-test-for-bufferbloat)** (described above) does a rudimentary job of
    measuring performance. Although it may not run long enough to avoid
    the effects of Powerboost or other special cases implemented by
    ISPs, it can definitely point out situations where
    you're "bufferbloated".
7. [**iperf2**](https://sourceforge.net/projects/iperf2/) and
[**iperf3**](https://github.com/esnet/iperf#iperf3--a-tcp-udp-and-sctp-network-bandwidth-measurement-tool)
measure network performance.
Despite the similar names, they are not compatible.
Both are under active development:
check each tool's website for a comparison of their capabilities.
8. [**fast.com**](https://fast.com) now tests for latency under load
(cick the "Show more info" button.)
Also see their [press release.](https://media.netflix.com/en/company-blog/fast-com-now-measures-latency-and-upload-speed) 
