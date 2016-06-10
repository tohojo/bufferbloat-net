
---
title: Cool things to do with a cerowrt router
date: 2012-02-04T18:15:00
lastmod: 2012-04-08T10:27:43
---
Cool things to do with a CeroWRT router
=======================================

-   Attach a USB drive for extra disk space, and turn your router into a
    web server. The default server included in CeroWRT, 'lighttpd',
    supports multihoming, URL rewriting, and CGI scripting; the Lua
    language is installed by default, and Python can be added easily. (I
    have a CeroWRT router hosting two websites with CGI, using an 8G
    thumb drive for storage space.)
-   Run an authoritative DNS server -- it supports dynamic DNS and fully
    automatic DNSSEC signing. (The same CeroWRT router hosts about a
    dozen signed domains.)
-   Use it as a [tunnel endpoint]({{< relref "wiki/IPv6_Tunnel.md" >}}) and get your
    house running IPv6
-   Install your favorite shell and editor and use it as a shell server

