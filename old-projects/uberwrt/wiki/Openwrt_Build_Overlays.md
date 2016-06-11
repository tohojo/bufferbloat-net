
---
title: Openwrt Build Overlays
date: 2011-04-19T09:54:41
lastmod: 2011-04-19T09:57:03
type: wiki
---
Openwrt Build Overlays
======================

You can customize your build for your environment by overriding the
default files by placing a\
files/ directory in your buildroot.

Then you can override the default /etc/opkg.conf (for example) by
placing your customized version under files/etc/ - this applies for ALL
files in a build image, including binaries!

Typically modified files include:

`etc/sysctl.conf
etc/defconfig/wndr3700v2/network
etc/rc.local
etc/opkg/whatever.conf # for alternate feeds`
