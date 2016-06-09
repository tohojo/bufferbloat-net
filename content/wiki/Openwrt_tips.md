
---
title: Openwrt tips
date: 2011-05-08T10:45:26
lastmod: 2011-05-08T10:45:26
---
Openwrt tips
============

Finding out what packages you have installed from your feeds
------------------------------------------------------------

find package/feeds/ -type l -print | while read x; do basename \$x; done
