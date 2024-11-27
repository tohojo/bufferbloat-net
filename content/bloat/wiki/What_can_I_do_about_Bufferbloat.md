---
title: What Can I Do About Bufferbloat?
date: 2017-03-10T09:10:12
lastmod: 2024-07-21T08:29:01
type: wiki
aliases:
    - /bloat/wiki/What_to_do_about_Bufferbloat/
    - /cerowrt/wiki/What_to_do_about_Bufferbloat/
---
# What Can I Do About Bufferbloat?

Bufferbloat is high latency (or lag) that occurs when there's other
traffic on your network.
This means that your network isn't always responsive - 
it's wasting your time.

**How does bufferbloat apply to me?**

Watch the [Home Internet Connections Are Unfair! (Bufferbloat)](https://www.youtube.com/watch?v=UICh3ScfNWI) 
video which gives an intuitive description of Bufferbloat.
Or read the more detailed
[Best Bufferbloat Analogy - Ever](https://randomneuronsfiring.com/best-bufferbloat-analogy-ever/)
blog post.

**OK - How do I get rid of Bufferbloat?**

**1. Measure the Bufferbloat:**
Use any of the tests below that measure latency both when
the line is idle _and_ during upload or download traffic.

* [Waveform Bufferbloat Test](https://www.waveform.com/tools/bufferbloat)
* [Speedtest.net Test](https://speedtest.net)
* [Cloudflare Speed Test](https://speed.cloudflare.com)

If the latency increases when there's traffic,
you have bufferbloat.
If the increase is small
(less than 20-30 msec),
bufferbloat is well under control.
For more details about testing,
read the [Tests for Bufferbloat](./Tests_for_Bufferbloat.md) page. 

**2. Possible Solutions:** There are lots of ways to throw time or money at this problem.
Most won't work.

* Your ISP would love to sell you a faster connection, but link speed isn't the problem -
it's your router buffering more data than necessary.
This adds _delay_ that can never be cured by faster transmission rates.
* Buying an expensive router (even one for "gaming") won't necessarily help,
since many commercial, off-the-shelf router manufacturers are clueless about excess buffering in their routers.
* Twiddling the router's QoS might make a difference,
[but it's a hassle, and only helps a bit.](More_about_Bufferbloat#what-s-wrong-with-simply-configuring-qos)

Instead...

**3. Take Control of Your Network:**
No one else (not your router manufacturer,
not your ISP) has a strong incentive to fix Bufferbloat.
But once you take control, the network will stay fixed for all time, 
and you can adapt to changing practices at your ISP or other vendors.

You need to find a router vendor that understands
the relationship between 
latency/responsiveness and bufferbloat,
and has firmware that uses one of the
Smart Queue Management algorithms such as 
cake, fq_codel, PIE, or others to eliminate it. 
Here are some options, from easy to harder:

- **Enable SQM settings** if your router already has them.

    First, measure the link speed _without_ SQM
using one of the speed tests above.
Then turn on SQM, setting the up and down speed to the measured values above.
Keep running your speed test and adjusting the SQM speed settings
until the latency remains low while achieving good speeds.
See, for example, this description of a [tuning session.](Getting_SQM_Running_Right)

- **Install an off-the-shelf router with SQM** Several commercial router vendors have a clue. 
    Here is a list of those we have found:
    * [Ubiquiti gear](https://help.ubnt.com/hc/en-us/articles/220716608-EdgeRouter-Advanced-queue-CLI-examples) has fq_codel settings. 
    People say its EdgeRouter will handle over 400 mbps.
    * [Mikrotik's RouterOS supports fq_codel](https://help.mikrotik.com/docs/spaces/ROS/pages/328088/Queues) 
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
    * Many other mesh router vendors claim to solve bufferbloat.
    Check their spec's or ask them about latency.
    * [Untangle NG Firewall](https://wiki.untangle.com/index.php/Bufferbloat) has fq_codel settings.
    * [ipfire.org](https://wiki.ipfire.org/configuration/services/qos) has fq_codel settings.
    * [pfsense](https://www.pfsense.org/) and [OPNsense](https://opnsense.org/)
have fq\_codel and fq\_PIE settings, courtesy of FreeBSD and
[ipfw/dummynet](https://www.freebsd.org/cgi/man.cgi?query=ipfw&sektion=8&apropos=0&manpath=FreeBSD+13.0-RELEASE+and+Ports)
    * _(Regrettably, the IQrouter from Evenroute.com is no longer on the market.)_

- **Upgrade your current router with custom firmware.** All the projects below support some kind
of queue management based on FQ-CoDel and/or Cake.

    - [OpenWrt](https://OpenWrt.org) (version 22.03 or newer,
[supported device list](https://openwrt.org/toh/start)).
The [Smart Queue Management guide](https://openwrt.org/docs/guide-user/network/traffic-shaping/sqm)
tells how to configure the *luci-app-sqm* package.
    - [Asuswrt-Merlin](https://www.asuswrt-merlin.net) (ASUS routers only).
In Web GUI follow to **Adaptive QoS → QoS**.
More customizations via Web GUI is available with [CakeQOS-Merlin](https://github.com/ttgapers/cakeqos-merlin).
    - [DD-WRT](https://www.dd-wrt.com)
    - [Gargoyle](https://www.gargoyle-router.com)
    - [Tomato](https://freshtomato.org)  

-  **Call your router vendor's support line**
if none of the above are possible.
You have the information from the latency tests.
Mention that the ping times get really high when someone is up/downloading
files, and that it really hurts your network performance.
Ask if they're working on the problem.
Ask when they're going to release a firmware update that solves it.

-  **Consider cake-autorate for variable-rate ISP links.**
    LTE, cable modems, and Starlink can all change rate
    from morning to evening, or even from minute to minute.
    The [cake-autorate](cake-autorate)
    algorithm adapts to the current conditions to 
    minimize latency.

Your network's responsiveness is in _your_ hands...

**Read More...**

* [Why does SQM work so well?](More_about_Bufferbloat#why-does-sqm-work-so-well)
* [What's wrong with simply configuring QoS?](More_about_Bufferbloat#what-s-wrong-with-simply-configuring-qos)
* [Setting up SQM on a Router Manually](More_about_Bufferbloat#setting-up-a-router-manually)
* [Best Bufferbloat Analogy &mdash; Ever](https://randomneuronsfiring.com/best-bufferbloat-analogy-ever/)
