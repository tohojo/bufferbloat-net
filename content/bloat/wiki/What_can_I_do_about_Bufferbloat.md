---
title: What Can I Do About Bufferbloat?
date: 2017-03-10T09:10:12
lastmod: 2020-01-08T09:07:12
type: wiki
aliases:
    - /bloat/wiki/What_to_do_about_Bufferbloat/
    - /cerowrt/wiki/What_to_do_about_Bufferbloat/
---
# What Can I Do About Bufferbloat?

Bufferbloat is high latency (or lag) that occurs when there's other
traffic on your network. 

**TL;DR** [Use the DSLReports Speed Test](http://dslreports.com/speedtest)
to see if you have bufferbloat.
*Longer answer:* read the [Tests for Bufferbloat](./Tests_for_Bufferbloat.md) page.

If the DSLReports test shows a letter grade worse than a B, you probably have bufferbloat.
That means the device at your bottleneck link (most
likely your router) is letting bulk traffic (uploads/downloads) interfere with
(and slow down) your time-sensitive traffic (gaming, Skype, Facetime, etc.)
Twiddling with QoS might help, and a faster internet connection probably won't
help at all. You need to find a way to fix the **router.**

**To Eliminate Bufferbloat in your Network...**

You will need a router whose manufacturer understands the principles of
bufferbloat, and has updated the firmware to use one of the Smart Queue
Management algorithms such as cake, fq_codel, PIE, or others.

1.  If your router has SQM settings, you can measure latency under load without SQM, 
    then turn on SQM and iterate: adjust the router settings and measure latency 
    until the latency gets as low as possible while retaining good speeds.
    See, for example, this [tuning session.](Getting_SQM_Running_Right)
2.  Several commercial router vendors offer SQM in their stock firmware. 
    Here is a list of those we found:
    * [IQrouter](http://evenroute.com) provides a good setup wizard for
    configuring SQM, and automatically tunes its settings. 
    It's good to about 200-250 mbps.
    * [Ubiquiti gear](https://help.ubnt.com/hc/en-us/articles/220716608-EdgeRouter-Advanced-queue-CLI-examples) has fq_codel settings. People say its EdgeRouter will handle over 400 mbps.
    * [Untangle NG Firewall](https://wiki.untangle.com/index.php/Bufferbloat) has fq_codel settings.
    * [ipfire.org](https://wiki.ipfire.org/configuration/services/qos) has fq_codel settings.
3.  Install the [OpenWrt 18.06](https://OpenWrt.org) (or newer) firmware
    on your current router. These builds are now
    stable and include the luci-app-sqm package.
    There's a guide at the OpenWrt web site:
    https://openwrt.org/docs/guide-user/network/traffic-shaping/sqm .  
    Or install suitable DD-WRT (www.dd-wrt.com) or
    Gargoyle (www.gargoyle-router.com) firmware. We understand that
    current builds of both products support fq_codel.
5.  Finally, if none of these seem to be options, call your router
    vendor's support line. With the information from the DSLReports
    Speed Test or the Quick Test for Bufferbloat in hand, you can
    mention that the ping times get really high when up/downloading
    files, and that it really hurts your network performance. Ask if
    they're working on the problem, and when they're going to release a
    firmware update that solves it.

Read More:

* [Why does SQM work so well?](More_about_Bufferbloat#why-does-sqm-work-so-well)
* [What's wrong with simply configuring QoS?](More_about_Bufferbloat#what-s-wrong-with-simply-configuring-qos)
* [Setting up SQM on a Router Manually](More_about_Bufferbloat#setting-up-a-router-manually)
