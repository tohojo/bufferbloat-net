
---
title: Capetown FAQ
date: 2011-05-18T10:43:58
lastmod: 2011-05-18T12:02:13
---
Capetown FAQ
============

Why is my to-the-internet connection slow with a Bismark router?
----------------------------------------------------------------

A: The router is configured with <link>QoS</link> (Quality of service)
**ON**, and set to a default more suitable for South Africa than
elsewhere. You should go to the Network-&gt;Qos screen on the
<link>capetown router configuration</link> page, turn off
<link>QoS</link>, run a suitable [bandwidth performance
test](http://speedtest.net) and then re-enable QoS with more suitable
up/download values a few percentage points less than what the bandwidth
test shows you.

Enabling QoS (with sane values) will make it more possible for you and
your family to do more work simultaneously - doing uploads while your
son is downloading and your daughter is making phone calls and your
spouse is playing games, with fewer complaints from everyone.

Disabling QoS will make single stream downloads run nearly as fast as
possible at the expense of other activities. Sometimes. See:
<link>bloat:Daddy why is my Internet Slow Today</link>?

QoS set to good values is best.

Does capetown "phone home"?
---------------------------

A: Yes, it does. If you do not wish to participate in the bismark study,
DO remove the bismark packages from your installation, or install
[Wiki]({{< relref "wiki/Wiki.md" >}}) instead. If, instead, you wish to help
the bismark project identify more problems on the edge of the internet,
please register your router and information at the [Network
Dashboard](http://networkdashboard.org)

Why so many Interfaces? <link>\#148</link>
------------------------------------------

A: The characteristics of wired and wireless, as well as the
<link>uberwrt:guest</link> and <link>uberwrt:babel</link> concepts, are
sufficiently different to warrant making a clear distinction between
them for <link>uberwrt:internal QoS</link> to work well.

Why so many SSIDs on the wireless interfaces?
---------------------------------------------

A: 2.4 ghz spectrum tends to be polluted by many other wireless devices.
If your client (laptop, whatever) supports 5Ghz operation, you might
want to use that SSID (clearly delineated by a "5" postfix) to get
higher performance operation.

You can make all the SSIDs be the same if you like in the <link>capetown
router configuration</link> pages, but it helps to know which one is on
"5".

Why guest interfaces?
---------------------

A: Wireless spectrum is intrinsically shared. It makes sense to share it
when possible, and also keep your own network safe.

What's this babel thing?
------------------------

A: [Wiki]({{< relref "wiki/Wiki.md" >}}). It doesn't work
(yet) in this release.

How do I disable the guest/babel interfaces? <link>\#148</link>
---------------------------------------------------------------

A: Firewalling is a complex problem not adequately handled by the web
interface. "Guest" networks are for visitors to your lan, they do not
have access to the wired or primary wireless lan (unless unsecured), but
do have access to the Internet. You can grant access to guest networks
that does not extend to your primary network.

To secure (rather than disable entirely) your guest networks, the
simplest method is merely to assign WPA2 keys to the guest networks that
guests won't know.

OR, you can remove the guest networks entirely. Removing the interfaces
entirely (which is doable) also requires removing the firewall rules for
the guest interfaces in order to work right, as well as a reboot, and
recreating them will be difficult.

Some things are easier to do by ssh-ing into the router. This is one of
them.

This is more complex than I'm used to!
--------------------------------------

A: This is a research project. We hope to make things simpler through
use of a universal [Network Dashboard](http://networkdashboard.org)

This is cool! What else can this puppy do?
------------------------------------------

A: See: [Cool things to do with a bismark router]({{< relref "wiki/Cool_things_to_do_with_a_bismark_router.md" >}})
