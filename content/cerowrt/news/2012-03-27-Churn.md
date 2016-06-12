
---
title: "Churn"
date: 2012-03-27T20:32:19
type: news
author: Dave Täht
---
While builds continue for the linux 3.3.0 series, enough bugs have shown
up in it for me to encourage new users to stick with the last known
stable(ish) release, which was 3.3rc7-5.

I froze cerowrt on march 14th, got a little distracted by a demo of
static deterministic nat and the port control protocol (PCP) as part of
the on-going ietf meeting, and fell behind on keeping up on patches to
openwrt.

When I got caught up today, patches had landed which touched every major
subsystem in cerowrt - the ethernet driver, the wireless driver, the
kernel, scripting and the gui. Enough broke in the last two weeks of me
not paying attention to the continuous integration process to make going
forwards or backwards very difficult. Right now, most noticeable, wifi
doesn't come up by default.

I am pleased to say that dnsmasq has made great progress in AAAA dns
integration, that iptables and iproute 3.3 have landed, and that I think
I've made a dent in bug \#113 (dnssec), but there's enough broken thus
far to force me to pull all the 3.3.0 related releases until some of the
stuff flying in loose formation congeals into one piece. That may not be
until 3.3.1 is released.

Also making a bit of progress on dhcp-dp, I think.

Hopefully early next week I'll have the pieces pulled together again to
where new builds of cerowrt are useable, rather than merely debuggable.
And the sources are as available as possible, on github,if you want to
chip in. There's plenty of bugs left to fix...

I look forward to having a more serious code freeze sometime towards the
middle of April.
