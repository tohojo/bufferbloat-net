---
title: What Can I Do About Bufferbloat?
date: 2017-03-10T09:10:12
lastmod: 2017-03-10T09:20:12
type: wiki
aliases:
    - /bloat/wiki/What_to_do_about_Bufferbloat/
    - /cerowrt/wiki/What_to_do_about_Bufferbloat/
---
# What Can I Do About Bufferbloat?

Bufferbloat is high latency (or lag) that occurs when there's other
traffic on your network. 
Use the [DSLReports Speed Test](http://dslreports.com/speedtest) 
or run one of the [Tests for Bufferbloat](Tests_for_Bufferbloat.md) to see if it's present.

**TL;DR** - if tests show bufferbloat, your router is letting bulk
traffic (uploads/downloads) interfere with (and slow down) your
time-sensitive traffic (gaming, Skype, Facetime, etc.) Twiddling with
QoS might help, but a faster internet connection probably won't help at all. You
will need to find a way to fix the **router.**

## How Can I Tell if My Router Has Bufferbloat?

-   Use [DSL Reports Speed Test](http://dslreports.com/speedtest) or any of the other tests on [Tests for Bufferbloat](Tests_for_Bufferbloat/)
-   A good router that protects against bufferbloat will hold the
    induced latency (extra latency above the no-traffic levels) below
    30 msec.
-   Above 100 msec, people will notice that the network feels slow:
    voice calls begin to sound bad, web browsing feels sticky, and
    you start to lag out when gaming.
-   If ping times/latency gets high while the speed test is running and drop back
    down when the speed test completes, it means your router is bloated.
    You have probably noticed that the network feels draggy or slow when
    other people use the network.

## To Eliminate Bufferbloat in your Network...

You will need a router whose manufacturer understands the principles of
bufferbloat, and has updated the firmware to use one of the Smart Queue
Management algorithms such as cake, fq_codel, PIE, or others.

1.  If your router has SQM settings, you can measure latency under load without SQM, 
    then turn on SQM and iterate: adjust the router settings and measure latency 
    until the latency gets as low as possible while retaining good speeds.
    See, for example, this [tuning session.](Getting_SQM_Running_Right)
2.  We continue to be hopeful that commercial router vendors will offer
    SQM in their stock firmware. Here is a list of those that do:
    * The [IQrouter](http://evenroute.com) provides a good setup wizard for
    configuring SQM, and automatically tuning its settings.
    * The [Untangle NG Firewall](https://wiki.untangle.com/index.php/Bufferbloat) has fq_codel settings
    * [Ubiquiti](https://help.ubnt.com/hc/en-us/articles/220716608-EdgeRouter-Advanced-queue-CLI-examples) has fq_codel settings
    * [ipfire.org](http://wiki.ipfire.org/en/configuration/services/qos) has fq_codel settings
3.  Install the [LEDE 17.01](https://lede-project.org) or 
    [OpenWrt Chaos Calmer](http://openwrt.org/) firmware
    on your current router. These builds are now
    stable and include the luci-app-sqm package.
    There's a guide at the LEDE web site:
    https://lede-project.org/docs/user-guide/sqm
4.  Or install suitable DD-WRT (www.dd-wrt.com) or
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
