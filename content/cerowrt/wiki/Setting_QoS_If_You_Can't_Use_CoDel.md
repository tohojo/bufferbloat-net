
---
title: Setting QoS If You Can't Use CoDel
date: 2013-04-03T13:52:15
lastmod: 2014-03-18T11:05:42
type: wiki
---
Setting QoS Properly if you can't use fq\_codel (CoDel + SFQ)
=============================================================

***Note:** This process is no longer needed in CeroWrt. See the
[Setting up SQM for CeroWrt 310](Setting_up_SQM_for_CeroWrt_310.md) page for a better
procedure.*

But if your router doesn't support these new algorithms for Active Queue
Management, you can still make your internet performance a little
better. You need to turn on the Quality of Service (QoS) settings within
your router. This artificially limits the speed that your router sends
data, therefore decreasing the effect of bloated buffers. You lose a
little speed to gain a whole lot of performance.

To do this with the OpenWrt firmware, open the Web LuCI interface. Go to
the Network -&gt; QoS page.

1.  Uncheck the Enable box to turn off QoS, then click Save & Apply
2.  Use a speed test (such as http://speedtest.net) to get your
    network's speed.
3.  Set Upload and Download to a value a value 95% of the speeds
    you measured.
4.  Check the Enable box to turn QoS back on again
5.  Click Save and Apply button at the lower right.

The image below shows the controls:

![](/attachments/130403135421_CeroWrt-QoS-steps.png)

### Attachments
{{< attachment name="CeroWrt-QoS-steps.png" type="image/png" description="" filename="130403135421_CeroWrt-QoS-steps.png" >}}
