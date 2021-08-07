---
title: What Can I Do About Bufferbloat?
date: 2017-03-10T09:10:12
lastmod: 2021-08-06T18:29:01
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
Here's what you can do:

**1. Measure the Bufferbloat:**
[Use the DSLReports Speed Test](http://dslreports.com/speedtest) to see if you have bufferbloat.
If the DSLReports test shows a letter grade worse than a B, you probably have bufferbloat.
That means the device at your bottleneck link (most
likely your router) is letting bulk traffic (uploads/downloads) interfere with
(and slow down) your time-sensitive traffic (gaming, Skype, Facetime, etc.)
For more details, read the [Tests for Bufferbloat](./Tests_for_Bufferbloat.md) page.

Keep the results of the test handy as a baseline for your experiments. 

**2. Possible Solutions:** There are lots of ways to throw money at this problem.
Most won't work.

* Your ISP would love to sell you a faster connection, but link speed isn't the problem -
it's your router buffering more data than necessary.
* Buying an expensive router (even one for "gaming") won't necessarily help,
since most commercial, off-the-shelf router manufacturers are clueless about Bufferbloat.
* Twiddling the router's QoS might make a difference,
[but it's a hassle, and only helps a bit.](More_about_Bufferbloat#what-s-wrong-with-simply-configuring-qos)

**3. Eliminate Bufferbloat in *Your* Network:**
Instead, you are going to have to take charge.
Once you fix it for your own network, it'll stay fixed for all time, 
and you won't be subject to changing practices at your ISP or other vendors.

You need to find a router whose manufacturer understands the principles of
bufferbloat, and has updated the firmware to use one of the Smart Queue
Management algorithms such as cake, fq_codel, PIE, or others. 
Here are some resources:

1.  If your router already has SQM settings, you can measure latency under load 
    (say, with [DSLReports](http://dslreports.com/speedtest)) without SQM, 
    then turn on SQM and measure again. 
    Keep adjusting the up and down speed settings (that's it!) and measuring 
    until the latency gets as low as possible while retaining good speeds.
    See, for example, this [tuning session.](Getting_SQM_Running_Right)
2.  Several commercial router vendors have a clue, and offer SQM in their stock firmware. 
    Here is a list of those we have found:
    * [IQrouter](http://evenroute.com) provides a good setup wizard for
    configuring SQM, and automatically tunes its settings. 
    IQrouter v3 is good to about 350 mbps. (Version 2 was good for 200-250 mbps.)
    * [Ubiquiti gear](https://help.ubnt.com/hc/en-us/articles/220716608-EdgeRouter-Advanced-queue-CLI-examples) has fq_codel settings. 
    People say its EdgeRouter will handle over 400 mbps.
    * Many of the "mesh" home router vendors seem to solve bufferbloat.
    Check their spec's or ask them about latency.
    * [Untangle NG Firewall](https://wiki.untangle.com/index.php/Bufferbloat) has fq_codel settings.
    * [ipfire.org](https://wiki.ipfire.org/configuration/services/qos) has fq_codel settings.
    * If you're a [Comcast/Xfinity](https://comcast.net) customer, see if you can get the XB6 / CGM4140COM cable modem that has PIE enabled.
Read p13 of [Improving Latency with Active Queue Management (AQM) During COVID-19.](https://arxiv.org/ftp/arxiv/papers/2107/2107.13968.pdf) for details.
3.  Upgrade your current router.
Install [OpenWrt firmware](https://OpenWrt.org) (version 21.02, 19.07, or 18.06).
The [Smart Queue Management guide](https://openwrt.org/docs/guide-user/network/traffic-shaping/sqm)
tells how to configure the *luci-app-sqm* package.
    Or install suitable [DD-WRT](https://www.dd-wrt.com),
    [Gargoyle](https://www.gargoyle-router.com) or
    [Tomato](https://freshtomato.org) firmware, all of which support some kind
    of queue management based on FQ-CoDel and/or Cake.
5.  Finally, if none of these seem to be options, call your router
    vendor's support line.
    With the information from the DSLReports Speed Test in hand, you can
    mention that the ping times get really high when up/downloading
    files, and that it really hurts your network performance. Ask if
    they're working on the problem, and when they're going to release a
    firmware update that solves it.

**Read More...**

* [Why does SQM work so well?](More_about_Bufferbloat#why-does-sqm-work-so-well)
* [What's wrong with simply configuring QoS?](More_about_Bufferbloat#what-s-wrong-with-simply-configuring-qos)
* [Setting up SQM on a Router Manually](More_about_Bufferbloat#setting-up-a-router-manually)
* [Best Bufferbloat Analogy &mdash; Ever](https://randomneuronsfiring.com/best-bufferbloat-analogy-ever/)
