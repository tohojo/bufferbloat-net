---
title: Bloated Driver List
date: 2011-01-27T06:59:17
lastmod: 2012-11-20T12:48:36
type: wiki
---
Bloated Device Drivers
======================

Reducing your [Dark Buffers](Dark_buffers.md) requires some work analyzing the
device drivers involved. The amount of default buffering the device
driver does can be deduced from looking at the source code, or inferred
by performing [Experiments](Experiments.md) on your systems.

Please help us improve this list!

-   THIS PAGE IS TOTALLY OBSOLETE \* Learn about BQL fq\_codel

Linux
-----

Under Linux, you can measure your dark buffers by turning the txqueuelen
parameter on the ethernet interface to 0.

A good number for txqueuelen used to be dependent what <link>traffic
shapers|traffic shaping</link> you are doing and the depth of your
device driver buffers as detailed below. If you aren't doing any - 4 -
seems to be a good starting figure for home gateways and wireless
laptops.

ifconfig eth0 txqueuelen 4\
ifconfig wlan0 txqueuelen 4

However in the case of ethernet,current (3.5 and later) linux kernels
use BQL, which eliminates the need for the above hack. Then you can
layer fq\_codel on top of it.

Wifi is still a mess however.

But that is just the start. The real problem lies underneath these
buffers, at the device driver layer.

### Ethernet

  Driver    | Where found                    | Buffers  | Mitigation             | Patches
  ----------| -------------------------------| ---------| -----------------------| ---------
  e1000e    | Laptops                        | 256      | ethtool -G eth0 tx 64  | None
  kirkwood  | Openrd,Various Plug computers  | 256      | ethtool -G ethX tx 20  | None
  ar7100    | WNDR5700, Nanostation M5       | 64       | None                   | None

### Wireless

  Driver     | Where found               | Buffers               | Mitigation  | Patches
  -----------| --------------------------| ----------------------| ------------| ---------------------------------------------
  ath9k[^1]  | WNDR5700, Nanostation M5  | 512, multiple queues  | 32 w/patch  | Much better in cerowrt, out of tree patches
  IWL        | Laptops                   | 256                   | None        | In progress

Mac
---

Windows
-------

Notes
-----

[^1]: The effective queue depth per each of the 10 queues, with this
    patch, is 3.
