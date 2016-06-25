---
title: CeroWrt and BCP38
date: 2014-03-22T15:03:27
lastmod: 2014-03-22T16:09:18
type: wiki
---
CeroWrt and BCP38
=================

CeroWrt 3.10.32-12 and later incorporate a module that implements the
Best Common Practices 38 (BCP38) internet specification. This
specification is discussed in detail at:
http://www.bcp38.info/index.php/Main\_Page

BCP38 prevents devices on the LAN side of the CeroWrt from spoofing
source addresses. By default, CeroWrt filters out spoofed addresses on
packets before they are sent into the Internet.

The implementation goes to some lengths to detect the multiple-router
case, so that you can have a primary and secondary router in your home.
The image below shows the GUI in the CeroWrt web interface. Find it from
the Network &gt; Firewall &gt; BCP38 tab.

![](/attachments/140322150351_CeroWrtTorontoBCP38.png)

### Attachments
{{< attachment name="CeroWrtTorontoBCP38.png" type="image/png" description="" filename="140322150351_CeroWrtTorontoBCP38.png" >}}
