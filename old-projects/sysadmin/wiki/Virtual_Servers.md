
---
title: Virtual Servers
date: 2011-03-21T21:05:10
lastmod: 2011-03-22T06:47:50
type: wiki
---
Virtual Servers
===============

All servers are named of the form: name.virt.bufferbloat.net. All are
(at present) located on <link>huchra</link>. Most will only be available
via the web and ssh via IPv6. I will probably use names rather than
numbers in the future.

Please note that these are blocked by several other bugs/features \#35
\#36 \#32 \#29 and especially \#25 right now

To connect to the console:

virt-viewer --connect
qemu+ssh://YOUR\_LOGIN@huchra.bufferbloat.net:222/system vmNUMBER

  ----- ------------------------------------------------ -------------- ------ ------ ----------------------------------------- ----------------
  vm    Server                                           OS             Bits   CPUS   Purpose
  noc   noc                                              ubuntu 10.10   64     2      Site management
  11    "debian64":ssh://debian64.virt.bufferbloat.net   squeeze        64     2      Kernel Builds
  12    uberwrt                                          ubuntu 10.10   64     8      Building openwrt and <link>uberwrt:Wiki
  13    badluck                                                         
  14                                                                    
  15                                                                    
  16                                                                    
  17    arch32                                           arch           32     2      Kernel Builds
  18    arch64                                           arch           64     2      Kernel Builds
  ----- ------------------------------------------------ -------------- ------ ------ ----------------------------------------- ----------------

 not installed yet 

  ---- ---------- ------------ ---- --- ---------------
  19   centos32   centos 5.5   32   1   Kernel Builds
  20   freebsd                          
  ---- ---------- ------------ ---- --- ---------------

== Random Notes

https://help.ubuntu.com/community/KVM/Managing

http://www.howtoforge.com/kvm-guest-management-with-virt-manager-on-ubuntu-8.10

http://www.bytemark.co.uk/index
