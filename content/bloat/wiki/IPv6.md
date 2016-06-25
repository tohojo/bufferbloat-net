---
title: IPv6
date: 2011-02-02T18:51:43
lastmod: 2011-04-11T09:59:16
type: wiki
---
IPv6 and Bufferbloat.net
========================

Bufferbloat.net's core services are fully IPv6 enabled.

Open Questions
--------------

Do you have Ipv6 to your home or business/university? Native? Or can you
get 6to4 to work? 6rd? Or a tunnelbroker.net tunnel? Or?

For those ssh users that lack easy access to IPv6, I plan a "jump" box
that is dual-stack, and it's only the core bufferbloat servers that need
to be dual stacked - obviously most of the edge boxes will be ipv4. IF
there are websites that need to run on a virtual, I plan to run them
through a proxy.

The main folk I've been dealing with (jg, linville) both have native
IPv6 support, and I've been using 6to4 tunneling with reasonable
success. In fact, the voip calls we've been making over linphone
directly over IPv6 have been the best quality voip calls I've ever
experienced.

Comcast's example
-----------------

Based on comcast's example of running their entire monitoring stack on
IPv6, and the relative lack of easy access to ipv4 for our virtual
servers, I have been making a big push to IPv6 enable everything at
least on the monitoring side, rather than use private (RFC1918)
addressing.

The prospect of coping with private addressing across the planet for
virtual servers strikes me as far more difficult than coaxing IPv6 to
work well.

So far I haven't found any service majorly broken, at least on Linux.
Tested thus far are apache, fcgi, snmpd, the web interfaces to cacti,
mrtg, redmine, ssh (of course) and multiple other services. In fact, I
haven't found anything that broke thus far besides:

IPv6 Minuses
------------

-   our soon to be abandoned DNS provider returns invalid IPv6 addresses
    instead of NXDOMAIN (name.com, see \#25)

<!-- -->

-   Over the last 5 years, people have stopped shipping /etc/gai.conf
    files that default to using IPv6 first (See below)

<!-- -->

-   Shapers, across all of Linux, are horribly broken when it comes
    to IPv6.

<!-- -->

-   I'm told there are issues with BSD and snmpd.

<!-- -->

-   It's turned out that finding native IPv6 on the east coast of the US
    has been a real problem. I'm under the impression that MIT has
    issues with it, and I'm working up the chain at gatech to get native
    IPv6 there, as they have EXCELLENT coast-2-coast IPv6 connectivity
    from california, 64ms, which is very close to theoretical.

??shipka.bufferbloat.net \$: ping6 ipv6.gatech.edu

64 bytes from 2610:148:fd8f:d7fc:203:baff:fe8f:29d: icmp\_seq=3 ttl=58
time=64.2 ms??

Traffic shaping
---------------

Very few traffic shapers "do the right thing" when it comes to IPv6
traffic. It is likely that your interactive traffic usually shaped by a
traffic shaper like wondershaper, won't be.

To my knowledge, none of these Linux traffic shapers "do the right
thing" when confronted with IPv6 or IPv6 encapsulated traffic.

-   [ADSL-optimizer](http://www.adsl-optimizer.dk)
    http://netoptimizer.blogspot.com/2011/01/bufferbloat-wireless-is-worse-than.html
-   [wondershaper](http://lartc.org/wondershaper/)
-   Openwrt Qos-Scripts
-   hsfc
-   Gargoyle

Preferring IPv6 over IPv4 for glib systems
------------------------------------------

put the following as your /etc/gai.conf

`label ::1/128 0
label ::/0 1
#label 2002::/16 2 
label ::/96 3
label ::ffff:0:0/96 4
label fec0::/10 5
label fc00::/7 6
label 2001:0::/32 7`

I don't know why this works, nor do I think it's entirely correct.
