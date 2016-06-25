---
title: READ THIS FIRST
date: 2012-01-28T15:24:24
lastmod: 2012-04-21T09:56:59
type: wiki
---
READ THIS FIRST!
================

How CeroWrt is different from OpenWrt
-------------------------------------

Our goal is to build a test tool for the internet edge rather than a
home router. Although CeroWrt can be used as such, it is not our primary
goal. We encourage you to install the software on a spare router before
committing to using it day to day - and compare it against your existing
router, first. Certainly we hope to be faster and more reliable that
most stock firmware can be, one of our earlier releases stayed up for
266 days...

With the 3.3 builds, CeroWrt has incorporated the Linux 3.3 kernel which
has many defenses against bufferbloat. Other major differences between
OpenWrt and CeroWrt:

-   all interfaces are routed, not bridged,
-   there is a full blown dns server, with mDNS/Bonjour enabled for ease
    of device/service discovery,
-   the [default naming scheme](Device_naming_scheme.md) and
    [default numbering scheme](Default_network_numbering.md)
    differ significantly from what you may be used to.

The [Onboard
documentation](http://jupiter.lab.bufferbloat.net/cerowrt/about.html)
has far more detail as to what's in the software.

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
left. See also [BANA](/bloat/wiki/BANA.md).

If you find this IP hard to remember or type, dns is enabled by default
for a virtual subdomain of 'home.lan. You should be able to get to it
via gw.home.lan if you get dhcp from the router. Changing the default ip
address ranges is difficult to do via the web interface and we suggest
you stick with it for a while until you understand the reasoning,
firewall, routing, and naming rules. (See DNS note below).

If you are running this inside your network, and not as your default gw,
configure your default gw to statically assign an ip address, and route
your subnet to the CeroWrt router, and turn off NAT.

See also the [default naming scheme](Device_naming_scheme.md)
and [default numbering scheme](Default_network_numbering.md)
pages for more information.

### Device/Interface Naming

We use an unusual [device naming scheme](Device_naming_scheme.md) to manage multiple
kinds of wireless devices. Instead of using eth0, eth1, wlan0, etc. the
interfaces have names that more accurately reflect their actual use.
Prefixes use Wireless vs. Ethernet and Secure, Guest/Gateway, or DMZ. As
noted above, each of these interfaces has a /27 subnet assigned. Thus:

-   ge00 is the Gateway Ethernet;
-   se00 is the first Secure Ethernet (LAN) interface;
-   sw00 is the first Secure Wireless interface at 2.4GHz;
-   gw10 is a Guest Wireless interface at 5.x GHz;
-   etc.

See also the [default naming scheme](Device_naming_scheme.md)
and [default numbering scheme](Default_network_numbering.md)
pages for more information.

### QoS - Be sure to set it

QoS processing is turned **off** by default in CeroWrt. Your performance
may be bad until you set the parameters as described in the first
question of the [FAQ](FAQ.md).

### IPv6 is enabled **BY DEFAULT**.

When connected to a real IPv6 address on a gateway, if CeroWrt doesn't
'just work', we want to know about it.

### Security & DNS

The bind9 DNS installation is as hardened as possible, running in a
chroot jail, respawning from xinetd.

Multiple services are enabled 'in' by default, notably http, https, ssh,
& rsync. DNS allows in the entire 2002 address range into the 'us' DNS
view, this should be restricted to just your 2002/48 lan.

From here, please move on to the [installation guide](Installation_Guide.md).
