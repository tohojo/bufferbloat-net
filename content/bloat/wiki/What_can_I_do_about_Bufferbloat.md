---
title: What Can I Do About Bufferbloat?
date: 2017-03-10T09:10:12
lastmod: 2024-03-21T08:29:01
type: wiki
aliases:
    - /bloat/wiki/What_to_do_about_Bufferbloat/
    - /cerowrt/wiki/What_to_do_about_Bufferbloat/
---
# What Can I Do About Bufferbloat?

Bufferbloat is high latency (or lag) that occurs when there's other
traffic on your network.
This means that your network isn't responsive under normal working conditions.
It's wasting your time.

**How does bufferbloat apply to me?**

Watch the [Bufferbloat Video](https://www.youtube.com/watch?v=UICh3ScfNWI) 
which presents an intuitive description of of Bufferbloat.
Or read the somewhat more detailed
[Best Bufferbloat Analogy - Ever](https://randomneuronsfiring.com/best-bufferbloat-analogy-ever/)
blog post.

**Most important - How do I get rid of Bufferbloat?**

**1. Measure the Bufferbloat:**
Use the [Waveform Bufferbloat Test](https://www.waveform.com/tools/bufferbloat)
or [Speedtest.net](https://speedtest.net))
to measure the latency under load.
If Waveform shows a letter grade worse than a B,
or if Speedtest.net shows more than 75 msec in either download or upload,
you probably have bufferbloat.
Some device at your bottleneck link
(usually your router) is letting bulk traffic (uploads/downloads) interfere with
(and delay) your time-sensitive traffic (gaming, video calls, Facetime, etc.)
For more details about testing,
read the [Tests for Bufferbloat](./Tests_for_Bufferbloat.md) page. 

**2. Possible Solutions:** There are lots of ways to throw time or money at this problem.
Most won't work.

* Your ISP would love to sell you a faster connection, but link speed isn't the problem -
it's your router buffering more data than necessary.
* Buying an expensive router (even one for "gaming") won't necessarily help,
since many commercial, off-the-shelf router manufacturers are clueless about Bufferbloat.
* Twiddling the router's QoS might make a difference,
[but it's a hassle, and only helps a bit.](More_about_Bufferbloat#what-s-wrong-with-simply-configuring-qos)
* Instead...

**3. Take Control of Your Network:**
No one else (not your router manufacturer,
nor your ISP) has a strong incentive to fix Bufferbloat.
But once you take control, the network will stay fixed for all time, 
and you can adapt to changing practices at your ISP or other vendors.

You need to find a router vendor that "understands"
latency/responsiveness/bufferbloat,
and has firmware that uses one of the
Smart Queue Management algorithms such as 
cake, fq_codel, PIE, or others. 
Here are some options, from easy to harder:

- **Enable SQM settings** if your router already has them.

    First, measure the link speed _without_ SQM
using [Waveform](https://www.waveform.com/tools/bufferbloat)
or [Speedtest.net](https://speedtest.net).
Each of these is good because they display latency when the line is idle
_and_ when there's upload or download traffic.
Then turn on SQM, setting the up and down speed to the measured values above.
Keep running your speed test and adjusting the SQM speed settings
until the latency remains low while achieving good speeds.
See, for example, this description of a [tuning session.](Getting_SQM_Running_Right)

- **Install an off-the-shelf router with SQM** Several commercial router vendors have a clue. 
    Here is a list of those we have found:
    * [Ubiquiti gear](https://help.ubnt.com/hc/en-us/articles/220716608-EdgeRouter-Advanced-queue-CLI-examples) has fq_codel settings. 
    People say its EdgeRouter will handle over 400 mbps.
    * The [eero mesh routers](https://support.eero.com/hc/en-us/articles/360000709886-What-is-eero-Labs-)
"optimize for conferencing and gaming" (their term for SQM.)
Their third generation devices
[support SQM at speeds up to a gigabit/second.](https://www.reddit.com/r/eero/comments/qxbkcl/66_is_out/hl9nw1m/)
    * All [Comcast/Xfinity](https://comcast.net)
DOCSIS 3.1 RDK-B-based gateway models have now been updated
with DOCSIS-PIE AQM and all are achieving dramatically
improved working latency.
(See Footnote 59 of
[_Improving Latency with Active Queue Management (AQM) During COVID-19_](https://arxiv.org/ftp/arxiv/papers/2107/2107.13968.pdf)
for model numbers.)
    * If you can find one, the [IQrouter](http://evenroute.com) provides a good setup wizard for
    configuring SQM, and automatically tunes its settings. 
    IQrouter v3 is good to about 350 mbps. (Version 2 was good for 200-250 mbps.)
    * Many other mesh router vendors claim to solve bufferbloat.
    Check their spec's or ask them about latency.
    * [Untangle NG Firewall](https://wiki.untangle.com/index.php/Bufferbloat) has fq_codel settings.
    * [ipfire.org](https://wiki.ipfire.org/configuration/services/qos) has fq_codel settings.
    * [pfsense](https://www.pfsense.org/) and [OPNsense](https://opnsense.org/)
have fq\_codel and fq\_PIE settings, courtesy of FreeBSD and
[ipfw/dummynet](https://www.freebsd.org/cgi/man.cgi?query=ipfw&sektion=8&apropos=0&manpath=FreeBSD+13.0-RELEASE+and+Ports)
    

-  **Upgrade your current router with a custom firmware.**
    * [OpenWrt](https://OpenWrt.org) ([supported devices list](https://openwrt.org/toh/start), version 22.03 or newer).

      The [Smart Queue Management guide](https://openwrt.org/docs/guide-user/network/traffic-shaping/sqm)
      tells how to configure the *luci-app-sqm* package.
    * [Asuswrt-Merlin](https://www.asuswrt-merlin.net) (ASUS routers only).

      In Web GUI follow to **Adaptive QoS → QoS**.

      More customizations via Web GUI is available with [CakeQOS-Merlin](https://github.com/ttgapers/cakeqos-merlin).
    * [DD-WRT](https://www.dd-wrt.com).
    * [Gargoyle](https://www.gargoyle-router.com).
    * [Tomato](https://freshtomato.org) firmware, all of which support some kind
      of queue management based on FQ-CoDel and/or Cake.

-  **Call your router vendor's support line**
if none of the above are possible.
You have the information from the latency tests.
Mention that the ping times get really high when someone is up/downloading
files, and that it really hurts your network performance.
Ask if they're working on the problem.
Ask when they're going to release a firmware update that solves it.

Your network's responsiveness is in _your_ hands...

**Read More...**

* [Why does SQM work so well?](More_about_Bufferbloat#why-does-sqm-work-so-well)
* [What's wrong with simply configuring QoS?](More_about_Bufferbloat#what-s-wrong-with-simply-configuring-qos)
* [Setting up SQM on a Router Manually](More_about_Bufferbloat#setting-up-a-router-manually)
* [Best Bufferbloat Analogy &mdash; Ever](https://randomneuronsfiring.com/best-bufferbloat-analogy-ever/)
