
---
title: Using oprofile
date: 2011-06-04T05:27:50
lastmod: 2011-06-04T05:35:04
type: wiki
---
Using oprofile
==============

There is a development build of <link>cerowrt:wiki|Cerowrt</link>
available at:

http://huchra.bufferbloat.net/\~cerowrt/cerowrt-dbg

Installation on the router
--------------------------

`opkg update
opkg install oprofile`

Setup
-----

Oprofile by default wants to write to a location on flash memory. This
is slow and can skew the test.\
Better is to write to ram. Also, you will need a kernel to look at in
order to see the symbols.

(Naturally, by using a ramdisk, this information will be lost on boot)

`cd /tmp
mkdir /tmp/op
wget http://huchra.bufferbloat.net/~cerowrt/cerowrt-dbg/vmlinux
opcontrol --setup --vmlinux=/tmp/vmlinux --session-dir=/tmp/op`

Running oprofile (basic performance counters
--------------------------------------------

`opcontrol --init
opcontrol --start`

Do your test

`opcontrol --stop
 opcontrol --dump`

Analyzing results
-----------------

`opreport -a --symbols --session-dir=/tmp/op`

Notes
-----

Oprofile is a development tool and can make a system slower (thus
skewing your test) and more fragile.

Some sample oprofiles
---------------------

<link>wireless oprofile</link>

<link>wired oprofile with alignment trap</link>
