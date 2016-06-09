
---
title: BQL_enabled_drivers
date: 2012-10-01T14:20:32
lastmod: 2015-06-26T07:09:34
---
BQL enabled drivers
===================

Queue Disciplines such as
[fq\_codel](http://www.bufferbloat.net/projects/codel/wiki/Wiki) and fq
need the underlying buffering of the device and device driver well
controlled. Under Linux, the mechanism to do so is called [Byte Queue
Limits](http://lwn.net/Articles/454390/) (BQL), which needs a small
amount of driver support to enable.

This is a partial list of the known BQL-enabled device drivers for Linux
as of version 3.14. Also see the list at
<link>codel:Best\_practices\_for\_benchmarking\_Codel\_and\_FQ\_Codel\#Enabling-Byte-Queue-Limits</link>

-   Intel e1000e, e1000, ixgbe, ivb40evf,i40e
-   Atheros ar71xx, alx
-   Nvidia forcedeath
-   Marvell sky2, skge
-   Broadcom bnx2, tg3, b44
-   Mellanox mlx4
-   Freescale gianfar
-   Realtek 8139
-   Isilicon hix5hd2

Highly desirable to BQL enable
==============================

-   Cisco, AMD, Xilinx and other manufacturers
-   Kirkwood (dreamplug, guruplug etc)
-   net-usb (patch discussed on cerowrt-devel) (raspery pi uses usb
    to network)
-   r8169 (buggy in 3.6 and earlier, currently reverted)
-   niu (same problem basically as r8169, also currently reverted)

There are 7 out of tree BQL drivers here that could use testing and
integration: http://www.mcmilk.de/projects/linux-bql/

Other subsystems
================

BQL is desirable for devices running at line rate. It is not required
for soft rate shapers such as hfsc and htb, which are independent of the
underlying wire rate.

Similar techniques to BQL could be used at other layers in the stack,
such as various forms of wireless, usb network devices, and adsl. But
adding this technique is going to be [really hard for
wireless](http://www.bufferbloat.net/projects/cerowrt/wiki/Fq_Codel_on_Wireless)
.
