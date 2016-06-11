
---
title: Experiment - BismarkECNDNSGOOGLE
date: 2011-05-21T13:46:03
lastmod: 2011-05-21T14:40:11
type: wiki
---
Experiment - BismarkECNDNSGOOGLE
================================

tests
-----

single file wget\
googleabcde - a search with google interactive turned on\
dns cache

http://gw.lab.bufferbloat.net/captures/series1

Some top level notes:

DNS
---

The number of dns queries issued on google's interactive pages is
extraordinary. And the level of dns caching,\
shockingly bad. As one example:

;; ANSWER SECTION:\
investing.businessweek.com. 60 IN A 209.234.234.146

;; AUTHORITY SECTION:\
investing.businessweek.com. 6266 IN NS gtm03.wallst.com.\
investing.businessweek.com. 6266 IN NS gtm02.wallst.com.\
investing.businessweek.com. 6266 IN NS gtm01.wallst.com.

;; ADDITIONAL SECTION:\
gtm01.wallst.com. 191 IN A 209.234.224.42\
gtm02.wallst.com. 191 IN A 209.234.234.42\
gtm03.wallst.com. 191 IN A 66.150.28.2

http 1.1
--------

ECN
---
