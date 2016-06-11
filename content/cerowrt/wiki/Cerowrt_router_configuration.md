
---
title: Cerowrt router configuration
date: 2012-03-01T17:28:16
lastmod: 2013-03-27T17:00:16
type: wiki
---
Cerowrt router configuration
============================

Setting QoS Properly
--------------------

**Note:** This process is no longer needed in CeroWrt. See the
[Setting up AQM]({{< relref "cerowrt/wiki/Setting_up_AQM.md" >}}) page for a better procedure.

Open the Web LuCI interface. Go to the Network -&gt; QoS page.

1.  Uncheck the Enable box to turn off QoS
2.  Use a speed test (such as http://speedtest.net) to get your
    network's speed.
3.  Set Upload and Download to a value a value 95% of the speeds
    you measured.
4.  Check the Enable box to turn QoS back on again
5.  Click Save and Apply button at the lower right.

The image below shows the controls

![](CeroWrt-QoS-steps.png)

### Attachments
{{< attachment name="CeroWrt-QoS-steps.png" type="image/png" description="" filename="120301173253_CeroWrt-QoS-steps.png" >}}
