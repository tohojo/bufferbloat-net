
---
title: Further Configuration for wndr3700
date: 2011-04-15T10:31:41
lastmod: 2011-04-22T11:52:46
type: wiki
---
Configuring the WNDR 3700
=========================

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
or static) do so... but remember that the BISMark gateway will also NAT
everything connected downstream from it.

**Enable the wifi interfaces.** Via the web interface, you need to go to
the network-&gt;wireless tab, turn on the radios, assign SSIDs and
channels, etc. WPA2 seems to be the best crypto setting. You should be
able to connect wirelessly and do stuff at this point, like surf the
web)

**Update the package database and install any additional needed
packages.** As we are doing our own build, the default location for
packages is currently incorrect, and we point to repos we are not
using.\
You should update to the package builds for the BISMark project. You can
also do this via the web interface. In the future, this process will be
automated.

**** Delete /etc/opkg/xWrt.conf

**** Edit /etc/opkg.conf and change it to point to
http://huchra.bufferbloat.net/wndr3700/packages

**** Run the following commands

****\* opkg update \# should do the right thing

****\* opkg list | less

****\* opkg install whatever\_else\_you\_want (tcpdump for example, is
useful, and there are multiple other packages in the pipeline)

It may be a good idea to change the default 192.168.42.1 to be something
not 1.1 or 42.1 if you are playing with multiple routers. Whatever you
choose will become the default for DHCP assigned addresses on the main 4
ports of the router. Choose well. If you want to do vpns and stuff like
that to other people, choose uniquely out of the 192.168.X range or from
the 10.X.X range.

There are a few outstanding bugs you should look at:\
http://www.bufferbloat.net/projects/bismark/issues
