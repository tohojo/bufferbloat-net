
---
title: Everything you wanted to know about Link Layer Adaptation
date: 2014-01-11T07:30:01
lastmod: 2014-01-11T08:43:18
type: wiki
---
Everything you wanted to know about Link Layer Adaptation
=========================================================

***This is a skeleton for the fully-expanded page***

Linked from:
http://www.bufferbloat.net/projects/cerowrt/wiki/Setting\_up\_AQM\_for\_CeroWrt\_310

However, certain link types have smaller overheads, and if you can
ascertain your link types (whether it’s LLC or VC-Mux based), you can
use these smaller overheads: Try the [Quick Test for Bufferbloat]({{< relref "cerowrt/wiki/Quick_Test_for_Bufferbloat.md" >}}) after making the change.

**LLC-based Overheads:**

-   PPPoA - 14 (PPP - 2, ATM - 12)
-   PPPoE - 40+ (PPPoE - 8, ATM - 18, ethernet 14, possibly FCS -
    4+padding)
-   Bridged - 32 (ATM - 18, ethernet 14, possibly FCS - 4+padding)
-   IPoA - 16 (ATM - 16)

**VC-Mux based Overheads:**

-   PPPoA - 10 (PPP - 2, ATM - 8)
-   PPPoE - 32+ (PPPoE - 8, ATM - 10, ethernet 14, possibly FCS -
    4+padding)
-   Bridged - 24+ (ATM - 10, ethernet 14, possibly FCS - 4+padding)
-   IPoA - 8 (ATM - 8)

*Need to incorporate some discussion of VDSL?*

- Sebastian Moeller says
in https://lists.bufferbloat.net/pipermail/cerowrt-devel/2014-January/001953.html\
- Not simple (response to original note) maybe use 44 bytes?\
- Discussion of names

- Sebastian Moeller
at https://lists.bufferbloat.net/pipermail/cerowrt-devel/2014-January/001963.html\
- Details all the complexities of DSL links to the internet
