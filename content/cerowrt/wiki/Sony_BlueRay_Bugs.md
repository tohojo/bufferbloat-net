---
title: Sony BlueRay Bugs
date: 2014-03-26T10:39:41
lastmod: 2014-03-26T10:41:21
type: wiki
---
Sony BlueRay player bugs with non /24 networks
==============================================

Despite
[CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)
being an internet standard since 1993, most sony blueray players we've
tried do not like anything besides a /24 (255.255.255.0) netmask and
network. The flaw shows up in particular when attempting firmware
updates. Other blueray applications like netflix appear to work ok...

The only workaround is to present the sony device with a /24 network.
For example, if the sony blueray player is on the se00 ethernet
interface,\
you will need to give that entire interface a distinct /24 to play in.

    config interface se00
            option 'ifname' 'se00'
            option 'proto'  'static'
            option 'ipaddr' '172.20.4.1' # must be unique across the network
            option 'netmask'        '255.255.255.0'
            option 'ip6assign' '64'

For wifi on the 2.4ghz network instead:


    config interface gw00
            option 'ifname' 'gw00'
            option 'proto'  'static'
            option 'ipaddr' '172.20.5.1' # must be unique across the network
            option 'netmask'        '255.255.255.0'
            option 'ip6assign' '64'

You should also change the allowable dhcp range so you can have up to
254 devices by changing the "start" and "limit"\
parameters appropriately in /etc/config/dhcp. For se00:


    config dhcp 'se00'
            option interface 'se00'
            option start '20' # save some room below 20 for static addresses
            option limit '220' # serve up 200 possible addresses
            list dhcp_option '42,0.0.0.0'
            list dhcp_option '44,0.0.0.0'
            list dhcp_option '45,0.0.0.0'
            list dhcp_option '46,8'
            option leasetime '24h'
            option domain 'mygw.hm.example.org' # whatever subdomain you wish to serve
            option ra 'server'
            option dhcpv6 'server'

And so on. After making these changes you will need to reboot, and
probably reboot every device on this network to get the right address
and netmask.

Note 1: IPv6 appears to work just fine with modern players with a /64
netmask.

Note 2: most everything else we've tried, including the sony playstation
and microsoft xbox and google chromecast products, work with a /27 just
fine.\
If you want more than 30 devices on a given network you can also do the
same as above for getting 254 devices
