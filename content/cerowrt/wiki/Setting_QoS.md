
---
title: Setting QoS
date: 2013-03-27T16:49:23
lastmod: 2013-03-27T17:01:15
type: wiki
---
Setting QoS and AQM
===================

**Note:** The instructions for setting QoS below were relevant for
CeroWrt prior to the Modena build (February 2013). We have preserved
them here for historical reasons.

Setting QoS: Improve latency problems with a CeroWrt router
-----------------------------------------------------------

**Note:** These have been superseded by the [Setting up AQM](Setting_up_AQM.md)
page.

CeroWrt has the ability to solve latency using a number of mechanisms.
One is our major focus: decreasing bufferbloat. Another technique is
AQM (active queue management) and bandwidth shaping: enabling AQM with
sane values will make it more possible for you and your family to do
more work simultaneously - doing uploads while your son is downloading
and your daughter is making phone calls and your spouse is playing
games, with fewer complaints from everyone.

AQM set to good values is best. Getting good values automatically is
hard. We're working on it.

Since it's hard to determine good values automatically, CeroWrt ships
with <link>QoS</link> (Quality of service) turned **OFF** by default.
This will make your router and network connection seem slow until you
use these steps to manually measure your network's speed and set good
values:

**To set up QoS for CeroWrt:**

-   Go to the Network-&gt;QOS screen on to see the [CeroWrt router configuration](Cerowrt_router_configuration.md) page.
-   Turn off <link>QoS</link> by un-checking the box labeled **Enable**
    and clicking **Save and Apply** at the lower-right corner. (It may
    already be unchecked: if so, skip this step.)
-   Run a suitable [bandwidth performance test](http://speedtest.net)
    such as http://speedtest.net to get your network's Download and
    Upload Speeds. Multiply each by 1000 to get the values
    in kilobits/second. For example, 2.45Mbps on the Speedtest.net site
    would be converted to 2450 kilobits per second (kbit/sec). You can
    ignore the Ping times.

A HUGE problem with most network tests is that they don't run for long
enough. Over a minute is required in order to get a reasonable value,
most run for less than 20 seconds, and many ISPs are now gaming that. We
use\
netperf to various sites supporting it to get a reasonable value.

-   Use these values to fill in the Download and Upload speed fields in
    the [CeroWrt web GUI.](Cerowrt_router_configuration.md) It is
    best to use values a few percentage points lower than what the
    bandwidth test shows you. For example, if the value is 2450
    kbit/sec, you could set it for 2300 kbit/sec.
-   Re-enable QoS by checking the **Enable** box in the GUI.
-   Click **Save and Apply** at the lower right.

AQM doesn't seem to do any good! I can't do a big upload/download and make a phone call!
----------------------------------------------------------------------------------------

Decrease the Upload and Download speeds somewhat [in the web GUI](Cerowrt_router_configuration.md) until you can do both. You should
make adjustments in 256kb increments (or do a binary search between 60%
and 100% of your provisioned bandwidth).

How accurate do these speeds need to be?
----------------------------------------

The values can be approximate, in the range suggested in the previous
question. AQM is "bandwidth" shaping, and attempts to limit the filling
of queues in the broadband equipment. Unfortunately, this can miss out
on the advantages of Comcast's PowerBoost, and it cannot take into
account other dynamic changes in availability of bandwidth caused by
your neighbors or even the temperature. We note that SPEEDTEST reports
misleading results on broad band service which provides temporary
bandwidth boosts such as Comcast's PowerBoost, and we are working on a
better test.

It's important to set some AQM speed settings. Although disabling AQM
can (sometimes) make single stream downloads run nearly as fast as
possible, it occurs at the expense of other activities. And it may not
always work.
