---
title: " 3.3.8-6: A reasonably stable CeroWrt version with fq_codel"
date: 2012-06-19T11:59:22
type: news
author: Dave Täht
aliases:
    - /news/37
---
I just put out http://huchra.bufferbloat.net/\~cero1/3.3/3.3.8-6/ and
deployed it as my default gw and ran a bunch of tests that it survived.

This is a version after 5 development releases and I'm hoping it proves
out stable enough for more deploy.

I'd prefer to test 24 hours but I'm about to start a trip and can't do
that. Hopefully after some more testers leap on it we can declare it
stable later this week and move on...

Also the source tree is mostly pushed out but a bit of a mess, I don't
know if I'll be able to get Cero independently buildable before late
next week.

Features:

+ update to linux 3.3.8\
+ Fix for bind9 CVE\
+ switch to netifd\
+ a complete resync with openwrt - this includes much new stuff,\
including wireless-testing - way too many updates to talk about\
without pulling in the commit log\
+ memory problem with ath9k appears gone\
+ ECN dropping instituted under load\
+ fq\_codel packet limits\
+ There is now 6rd support, totally untested and unconfigured;\
+ transmission bittorrent is in there, too\
+ fq\_codel on all interfaces by default, on wireless using all 4
subqueues

-s on this release: I went for "stable" rather than new features after
it cost me too much time.

- I had to rip out opkg signing support, and some ipv6/diffserv
classification support in transmission that wasn't fully baked.

- re-running simple\_qos.sh with new values appears to require a reboot
first

-The default gui for AQM doesn't work, the one for "qos" uses hfsc +
fq\_codel (but lacks ipv6 and diffserv support), and the command line
simple\_qos.sh has ipv6 and diffserv, but has to be edited and run
manually. And perhaps it's use of htb etc can be improved. I get pretty
good results on comcast with simple\_qos, see speedtest results here:

http://pastebin.com/Fq6G5Q4u

but not **quite** as good as I hoped for. However, under heavier loads
the fq\_codel stuff is working great under netperf with various numbers
of threads and classifications and users.

I would hope some folk here run some benchmarks against various things
but some cautions - for example - chrome's benchmark tends to hit dns\
hard, and cero by default is not using your most local forwarder so it
can bottleneck on dns - ways to fix that if you have dnssec is to edit\
forwarders.conf to point to your local forwarder, and uncomment the
forwarders line in named.conf. If your ISP doesn't\
do dnssec yet, disable dnssec and point forwarders.conf to their
nameservers - but I otherwise am getting good results.

Also: I would really prefer people clearly identify when they are
testing over wireless vs ethernet and until you have a fq\_codel and\
debloat-script enabled kernel on your laptop, too, I am finding most of
the time the bloat is coming from the testing box rather than cerowrt\
itself!

There are now fq\_codel enabled kernels for ubuntu 12.4 and fedora 16
available here:

http://www.bufferbloat.net/projects/codel/wiki

I look forward to analyzing htb vs hfsc and further tuning of
qos-scripts and the simple\_qos script. I'm too stupid apparently to\
come up with a way to run simple\_qos out of the aqm gui... (help
wanted)

The new version of quagga-babeld is available in the opkg repository and
it has been confirmed to work right with ipv4 mesh interfaces. I\
am really looking forward to people trying this and the authentication
code now in quagga so we can migrate off of the existing babeld.

Have fun. I am traveling the rest of this week. Patches, benchmarks and
data gladly accepted (preferably on the cerowrt-devel list)﻿
