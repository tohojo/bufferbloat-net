
---
title: Hardware Plan
date: 2014-08-09T10:29:34
lastmod: 2014-09-03T12:39:37
type: wiki
---
Hardware Plan
=============

Presently the most open wifi drivers are those based on the ath9k
chipset. All other drivers contain binary blobs in precisely the places
we need to hack on, and are currently unsuitable for further
development.

We MAY acquire a firmware license to deal with one or more 802.11ac
chips.

The initial work will be x86 based, as the compile, test, debug cycle is
shorter on that sort of hardware, and we envision several new features
that might require a faster processor than what is commonly found in
existing access points.

A [RFP]({{< relref "projects/make-wifi-fast/wiki/RFP.md" >}}) or two will be issued to find more suitable hardware
in the long run, and it may turn out that custom hardware will be
necessary.

While the initial work will be focused on 802.11n and later, some
resources will be expended to look harder at 802.14 based systems, as
well as LTE, in the hope of unifying the stack and requirements.

Hardware options
----------------

We are evaluating several platforms for future work:

### x86\_64 (rangeley)

http://www.supermicro.nl/products/motherboard/Atom/X10/A1SRi-2558F.cfm\
http://www.compex.com.sg/productdetailinfo.asp?model=WLE350NX&acc1Panel=1\
http://www.zcomax.co.uk/products/index.php/products/wlan-module/802-11ac-minipci-e-module\
http://www.streakwave.com/Itemdesc.asp?ic=RB14e&eq=&Tp=

### Qualcom/Atheros

### RALINK

### Lantiq
