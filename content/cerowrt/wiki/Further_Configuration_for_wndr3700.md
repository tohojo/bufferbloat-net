
---
title: Further Configuration for wndr3700
date: 2011-07-09T09:31:29
lastmod: 2011-07-09T09:37:15
type: wiki
---
Further Configuration for wndr3700v2
====================================

You can configure the router via its Web interface or at the command
line, via ssh.

**Get the box up on the internet.** If you are connecting to a cable
modem or some other dynamic IP providing host, just connect the WAN port
to the router, and reboot the router. This will do "most" of the right
thing. Some caveats:

**** In the event that your Internet connection is static, you will need
to supply the correct IP address, gateway, and DNS server information
via the Web interface on the gateway.

**** If you just want to add it to your existing network (supplying dhcp
or static) do so... but remember that the CeroWrt gateway will also NAT
everything connected downstream from it, unless you setup a static route
to it and explicitly turn NAT off.

**** DNSSEC will not work properly if the router cannot get the correct
time. It will disable itself until it can.\
\***Enable the wifi interfaces.** Via the web interface, you need to go
to the network-&gt;wireless tab, turn on the radios, assign SSIDs and
channels, etc. WPA2 seems to be the best crypto setting. You should be
able to connect wirelessly and do stuff at this point, like surf the
web)

Update the package database and install any additional needed packages.\*
-------------------------------------------------------------------------

Run the following commands

1.  opkg update \# should do the right thing
2.  opkg list | less
3.  opkg install whatever\_else\_you\_want (netperf and iperf for
    example, are useful, and there are multiple other packages in
    the pipeline)

There are a few outstanding bugs you should look at:
http://www.bufferbloat.net/projects/uberwrt/issues
