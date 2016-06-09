
---
title: Changing your cerowrt ip addresses
date: 2011-09-15T16:42:56
lastmod: 2014-09-23T03:55:17
---
Changing your CeroWrt IP Addresses, DNS settings, SSID
======================================================

Changing interfaces, router name, your ip addresses or SSID are tedious
using the default web interface, and it is much faster to do it at the
command line.

The <link>Automated Configuration of CeroWrt</link> page provides a
script that systematically changes these addresses, as well as
configuring other aspects of the router in a single step.

Changing your IP subnets using sed
----------------------------------

    NEWIP=your.new.ip
    REVIP=ip.new.your

    sed -i s#172.30.42#$NEWIP#g /etc/config/* /etc/babel* 

Say, for example, you wanted to have a 192.168.1 layout (not that we
recommend you do this):

    sed -i s#172.30.42#192.168.1#g /etc/config/* /etc/babel* 

Note that this preserves the /27 networks (so that ethernet devices need
to be in the 1-31 range) which we think is a good idea regardless, due
to the multicast issue.

Changing your CeroWrt domain via sed
------------------------------------

You can also change the default 'home.lan' domain to something else
using sed.

    NEWNAME=your.domain
    sed -i s#home.lan#$NEWNAME#g /etc/config/* /etc/hosts 

Changing your SSID globally
---------------------------

CeroWrt has a multitude of network interfaces enabled. The SSIDs all
contain the string "CEROwrt", and it's hard to change the SSID via the
web interface. However, if you want your own SSIDs, another sed command
will get you there.

    sed -i s#CEROwrt#YOURNEWSSID#g /etc/config/wireless

**Note:** After doing any of these modifications your router will be
thoroughly confused unless you reboot, so reboot.

**Update 23Sep2014:** Removed `/etc/chroot/named/etc/bind/*/*` from the
DNS and subnet examples as we no longer use bind.
