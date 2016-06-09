
---
title: How is CeroWrt different from OpenWrt
date: 2013-03-16T11:51:40
lastmod: 2014-07-29T14:56:05
---
How is CeroWrt different from OpenWrt
=====================================

Our goal is to build a test tool for the internet edge rather than a
home router. Although CeroWrt can be used as such, it is not our primary
goal. We encourage you to install the software on a spare router before
committing to using it day to day - and compare it against your existing
router, first. In the extensive testing, CeroWrt has been extremely
reliable, faster than stock router firmware, and provides a good
proof-of-concept that Bufferbloat can be conquered by simple, but
powerful algorithms.

CeroWrt has incorporated the latest Linux 3.10 kernel modifications
which have many defenses against bufferbloat. Other major differences
between OpenWrt and CeroWrt:

-   all interfaces are routed, not bridged,
-   there is a full blown dnssec enabled server, with mDNS/Bonjour
    enabled for ease of device/service discovery,
-   the <link>device\_naming\_scheme|default naming scheme</link> and
    <link>default\_network\_numbering|default numbering scheme</link>
    differ significantly from what you may be used to.

The [Onboard
documentation](http://cero2.bufferbloat.net/cerowrt/about.html) has far
more detail as to what's in the software.

Core things you should know
---------------------------

### Default Password

The router has a default, rather than empty, password.

login: root\
password: Beatthebloat

Do change it on installation, and even better, put your ssh key on it
and disable password access entirely.

### IP addresses & DNS

CeroWrt is a test platform, and as such we wanted it to co-exist within
existing networks as best as possible, without conflicting with an
existing network, and to not require NAT in order to function inside
that network. NAT skews some test results horribly.

Since there is no public IP address space left, 10 networks are being
increasingly used as backbone networks, and 192.168.X is most likely a
number you are already using on your existing network, we chose the
172.16.0.0/12 range to play in. The default address for the router is
172.30.42.1. Each of the interfaces has a /27 subnet from this range by
default - this allows 30 addresses per interface, a sensible limit for
home/edge routers.

It is ironic that this is the last piece of 'free' IP address space
left. See also <link>bloat:BANA</link>.

If you find this IP hard to remember or type, dns is enabled by default
for a virtual subdomain of 'home.lan. You should be able to get to it
via gw.home.lan if you get dhcp from the router. Changing the default ip
address ranges is difficult to do via the web interface and we suggest
you stick with it for a while until you understand the reasoning,
firewall, routing, and naming rules. (See DNS note below).

If you are running this inside your network, and not as your default gw,
configure your default gw to statically assign an ip address, and route
your subnet to the CeroWrt router, and turn off NAT.

See also the <link>device\_naming\_scheme|default naming scheme</link>
and <link>default\_network\_numbering|default numbering scheme</link>
pages for more information.

### Device/Interface Naming

We use an unusual <link>device naming scheme</link> to manage multiple
kinds of wireless devices. Instead of using eth0, eth1, wlan0, etc. the
interfaces have names that more accurately reflect their actual use.
Prefixes use Wireless vs. Ethernet and Secure, Guest/Gateway, or DMZ. As
noted above, each of these interfaces has a /27 subnet assigned. Thus:

-   ge00 is the Gateway Ethernet;
-   se00 is the first Secure Ethernet (LAN) interface;
-   sw00 is the first Secure Wireless interface at 2.4GHz;
-   gw10 is a Guest Wireless interface at 5.x GHz;
-   etc.

See also the <link>device\_naming\_scheme|default naming scheme</link>
and <link>default\_network\_numbering|default numbering scheme</link>
pages for more information.

### QoS - You NEED to set it

OpenWrt needs to set QoS for best performance. The defaults of CeroWrt
work pretty well. Use the <link>Setting Up SQM for CeroWrt 3.10</link>
procedure for better results.

### IPv6 is enabled **BY DEFAULT**

When connected to a real IPv6 address on a gateway, if CeroWrt doesn't
'just work', we want to know about it.
