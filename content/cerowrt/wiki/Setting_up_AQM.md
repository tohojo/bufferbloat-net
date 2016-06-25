---
title: Setting up AQM
date: 2013-03-25T19:07:32
lastmod: 2014-03-18T10:17:15
type: wiki
---
Setting up AQM - THIS PAGE IS DEPRECATED for current builds of CeroWrt
======================================================================

**If you are using CeroWrt 3.10.24-8 (December 2013) or newer,** Use the
SQM setup instructions at:
http://www.bufferbloat.net/projects/cerowrt/wiki/Setting\_up\_SQM\_for\_CeroWrt\_310

**If you're using the older CeroWrt 3.8.8-4**, you should definitely
upgrade to the current version. It offers much better performance, more
features, and better stability. Nonetheless, here's the info about the
new Network/SQM tab built into the GUI. If you just want to try out
CeroWrt:

-   Set the Queuing discipline to "fq\_codel"
-   Set the Queue setup script to "simplest.qos"
-   Set the up and download speeds to something less than the full rated
    speed of your internet provider. Entering a value that's 85% of the
    full speed (in each direction) is definitely safe.

If you want to experiment, try different queueing disciplines or setup
scripts, or set the link speeds to a higher percentage and the run tests
to see when the latency starts to get worse.

**If you're using a 3.7 or earlier build**

CeroWrt defaults to using the Active Queue Management that comes from
OpenWrt. It's pretty good. But CeroWrt provides a `simple_qos.sh` script
that's better in that it uses smaller quantums and supports ipv6 fully.
You need to edit three files, then restart the router to invoke it.

**1. Edit the simple\_qos.sh file** to match your actual bandwidth up
and down. To do this, edit the file at `/usr/sbin/simple_qos.sh`, and
find the two lines below. Change the numbers to match your link's speed.
NB: The numbers are in kbps (e.g., indicate a 3 megabit link with 3000;
768kbps with 768, etc.)

If you are using some forms of ADSL, you will also need to fiddle with
the overhead figure to calculate in the ATM overhead.

    UPLINK=2000
    DOWNLINK=20000

**2. Edit the /etc/rc.local file** by adding the following line before
the last line (`exit 0`):

<pre>
<code>/usr/sbin/simple\_qos.sh</code>

</pre>
**3. Edit the /etc/hotplug.d/iface/00-debloat file** by adding the
following line to the "ifup" stanza. 

    [ "$DEVICE" = "ge00" ] && /usr/sbin/simple_qos.sh

It will look something like this when you're done:

    [ "$ACTION" = "ifup" ] && {
         IFACE=$DEVICE QMODEL=nfq_codel_ll /usr/sbin/debloat >> $DEBLOAT_LOG 2>> $DEBLOAT_LOG2
         [ "$DEVICE" = "ge00" ] && /usr/sbin/simple_qos.sh
    }

**4. Restart your router,** and the simple\_qos.sh will take effect.

We do plan to make this available as a gui option in the future, unless
it gets ported into C.

Note that we default to about 5% reserved for "background traffic". In
practice it appears reserving 20% or so is closer to correct, and you
can fix that by going into /usr/sbin/debloat and changing in the egress
function the background traffic calculation to be 1/6 rather than 1/9.
