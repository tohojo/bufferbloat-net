
---
title: Useless hardware
date: 2011-03-20T09:58:58
lastmod: 2011-09-27T02:54:58
---
Useless or difficult to utilize wireless hardware
=================================================

Netgear's "Open Source Routers"
-------------------------------

All 5 of netgear's marketed-as-"open source" routers to date are not
fully open source, as the broadcom wifi chip is a binary blob that is
VERY hard to deal with. There is as yet incomplete openwrt support for
the most current model(s).

Yet... The **not-marketed-as-open-source** NETGEAR
[wndr3700v2]({{< relref "wiki/Wndr3700v2.md" >}}) is MUCH easier to deal with. It has full
openwrt support in git head. Go figure!? Would it hurt to market the
good and truly open source router to the open source folk? The
[wndr3700v2]({{< relref "wiki/Wndr3700v2.md" >}}) is best in class for quality, speed,
functionality and open-sourceness, and is our first choice for
[Cerowrt]({{< relref "wiki/Wiki.md" >}}), [ISCwrt]({{< relref "wiki/Wiki.md" >}}),
[Wisp6]({{< relref "wiki/Wiki.md" >}}), and [Bismark]({{< relref "wiki/Wiki.md" >}})
development.

But: Avoid the other "open source" models like the plague they are.

Linksys e3000
-------------

**AVOID**

Linksys e4000
-------------

Not a lot is known at present on this hardware. It is being used, with
some success, by comcast, in their 6rd trials.

Broadcom based chipsets
-----------------------

Most broadcom based products are using a binary blob. Although broadcom
is trying to work better with the community on creating a usable open
source driver, the work progresses slowly.

**Re-evaluate in Nov, 2012**

Marvell based chipsets
----------------------

### Guruplug

With terrible thermals and a very loud fan, this is unusable.

**AVOID**

### Dreamplug

While otherwise excellent hardware (512MB of ram, 512MB of flash), and
kernel support for the remainder of the CPU's features is rock solid...
the wireless chip is not dual band and is presently a binary blob. If
marvell can free up the source to this chip, and it's not too horrible,
we can put it back on the table.

The freedombox project plans to use this hardware and have high hopes of
doing this.

After dealing with marvell's wireless stuff for a decade now we're
decidedly more pessmistic.
