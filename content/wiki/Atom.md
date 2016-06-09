
---
title: Atom
date: 2011-04-07T18:17:01
lastmod: 2011-04-07T18:17:01
---
Atom and BISMark
================

You will need to download the latest [images are
here](http://huchra.bufferbloat.net/atom)

And then install.

These are the wndr instructions, this needs to be rewritten for the
atom:

[Installation
instructions](http://wiki.openwrt.org/toh/netgear/wndr3700#oem.easy.installation)\
Specific <link>Flashing instruction for Mac</link>.

If you need additional packages, you will need to remove /etc/opkg/\*\
then edit the /etc/opkg.conf file to point to either
http://huchra.bufferbloat.net/atom instead of what it points to
currently, then do a

`opkg update
  opkg list
  opkg install your_package`

There will be a special <link>bismark feed</link> at some point

Please note that huchra will move to a saner name at some point in the
near future, and we hope to make these defaults somehow.
