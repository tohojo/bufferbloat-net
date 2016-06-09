
---
title: Sysupgrade
date: 2011-07-09T09:47:51
lastmod: 2011-09-06T15:12:02
---
Sysupgrade
==========

Once a box already has openwrt or cerowrt on it, you can reflash via the
web based utility. Generally, to be safe, it's a good idea to use the
command line tool.

The *-sysupgrade.bin* image is always used when upgrading OpenWrt
(CeroWrt) images, e.g.
*openwrt-ar71xx-generic-wndr3700v2-jffs2-sysupgrade.bin*.

    cd /tmp
    wget the_image_file (located at http://huchra.bufferbloat.net/~cero1/_the release candidate_/
    sysupgrade -d 60 -n the_image_file 

Enough is in flux in CeroWrt for it to be a good idea to always reflash
from scratch, and then selectively install your customizations from a
backup of /etc.

**You do have a backup, don't you?**
