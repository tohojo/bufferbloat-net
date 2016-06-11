
---
title: Using CPE home gateways and settop boxes
date: 2012-05-26T18:53:52
lastmod: 2012-05-26T18:53:52
type: wiki
---
Using CPE home gateways and settop boxes
========================================

On Thu, May 24, 2012 at 8:43 PM, Fred Baker wrote:\
&gt; You want my opinion, it **could** be put on a CPE Router, but would
be even better on a set-top box. CalTech/USGS mentioned the set-top
model to us a couple of years ago, along the lines of "a \$2 seismometer
is not very accurate, but if you got a single un-repeated (eg, so half
og them get lost, half don't) UDP message from each of the homes within
a certain radius of the epicenter saying "I felt it" with a number, you
could work out the issues.""

Oh, sure! I note when I left the country, accelerometers were very\
expensive, and although I'd had this idea back in jg's 'unobtanium'\
days, I'd felt it was impossible to do...

I came back to the US last year, and they'd dropped to 3mm in size and\
cost under 2 bucks, and are\
easily interfaced with i2c or a simple D/A converter.

The reasoning for putting one on a cpe router, is that it can do\
things like intercept dns and pop up a web page alert, or have a local\
jabber server that will send a message (I have a small jabber server\
built into cerowrt). Similarly, the software for doing the work can\
live on the router and not have to deal with NAT as much, although I\
thought hip or something similar could be used.

Intercepting web and dns page access on an earthquake alert is\
basically what the japanese do, except they do it on their web\
servers, which has a large latency, and that kind of is too much of a\
pull model for my taste - I'd like an alert to flash out on irc,\
jabber, dns, home audio gear, etc -

Certainly having it on a settop box would allow for audio and visual
alarms.

And it could be done this way with minimal udp traffic.

I've been working this problem for a while, there are many other ways\
to accomplish it on the cheap\
in useful scenarios.

http://nex-6.taht.net/posts/Heroic\_Engineering\_In\_Japan/
