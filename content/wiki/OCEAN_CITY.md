
---
title: OCEAN CITY
date: 2011-07-09T08:20:38
lastmod: 2012-03-17T09:32:25
---
OCEAN CITY - READ THIS FIRST!
=============================

The Ocean City release was intended to be an massive release, fixing all
known bugs and implementing all desired features. Our desire exceeded
our reach, and we chose to pursue significantly scaled back (but still
important) goals described elsewhere. These documents - devoted to the
Ocean City release - are now obsolete:

-   [OCEAN CITY]({{< relref "wiki/OCEAN_CITY.md" >}})
    (This page)
-   [OCEAN CITY README]({{< relref "wiki/OCEAN_CITY_README.md" >}})
-   [OCEAN CITY RELEASE REQUIREMENTS]({{< relref "wiki/OCEAN_CITY_RELEASE_REQUIREMENTS.md" >}})
-   [OCEAN CITY RELEASE NOTES]({{< relref "wiki/OCEAN_CITY_RELEASE_NOTES.md" >}})
-   [OCEAN CITY INSTALLATION GUIDE]({{< relref "wiki/OCEAN_CITY_INSTALLATION_GUIDE.md" >}})
-   [OCEAN CITY FAQ]({{< relref "wiki/OCEAN_CITY_FAQ.md" >}})
-   [OCEAN CITY old News Item - rc7 slipping]({{< relref "wiki/OCEAN_CITY_old_News_Item_-_rc7_slipping.md" >}})
-   [OCEAN CITY old News item - rc6 (beta 2) is suitable for beta testing]({{< relref "wiki/OCEAN_CITY_old_News_item_-_rc6_(beta_2)_is_suitable_for_beta_testing.md" >}})
-   [OCEAN CITY old News Item - rc5 is suitable for testing]({{< relref "wiki/OCEAN_CITY_old_News_Item_-_rc5_is_suitable_for_testing.md" >}})

ALL CURRENT INFORMATION ABOUT CEROWRT IS ON THE MAIN [WIKI]({{< relref "wiki/Wiki.md" >}})
PAGE.

How CeroWrt is different from OpenWrt
-------------------------------------

Our goal is to build more of a test tool for the internet edge than a
home router - although it can be used as such. We encourage you to
install the software on a spare router before committing to using it day
to day - and compare it against your existing router.

The [Onboard
documentation](http://jupiter.lab.bufferbloat.net/cerowrt/about.html)
has far more detail as to what's in the software.

Major differences between OpenWrt and CeroWrt - all interfaces are
routed, not bridged, there is a full blown dns server, and the ip
address scheme and device naming scheme differ significantly from what
you may be used to.

Aside from that, most of the core stuff in CeroWrt is now in OpenWrt.

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
left. See also [BANA]({{< relref "wiki/BANA.md" >}}).

~~If you find this IP hard to remember or type, dns is enabled by
default for a virtual subdomain of 'home.lan. You should be able to get
to it via gw.home.lan if you get dhcp from the router. Changing the
default ip address ranges is difficult to do via the web interface and
we suggest you stick with it for a while until you understand the
reasoning, firewall, routing, and naming rules.~~ (See DNS note below).

If you are running this inside your network, and not as your default gw,
configure your default gw to statically assign an ip address, and route
your subnet to the CeroWrt router, and turn off NAT.

### Device/Interface Naming

We use an unusual [device naming scheme]({{< relref "wiki/Device_naming_scheme.md" >}}) to manage multiple
kinds of wireless devices. Instead of using eth0, eth1, etc. the
interfaces have names that more accurately reflect their actual use.
Prefixes use Wireless vs. Ethernet and Secure, Guest/Gateway, or DMZ. As
noted above, each of these interfaces has a /27 subnet assigned. Thus:

-   ge00 is the gateway ethernet;
-   se00 is the first LAN ethernet interface;
-   sw00 is the first secure wireless interface at 2.4GHz;
-   gw10 is a guest wireless interface at 5.x GHz;
-   etc.

### IPv6 is enabled **BY DEFAULT**.

If - when connected to a real ip address on a gw, it doesn't 'just
work', we want to know about it.

### Security

The bind9 DNS installation is as hardened as possible, running in a
chroot jail, respawning from xinetd. (but see DNS note below).

Multiple services are enabled 'in' by default, notably http, https, ssh,
& rsync. DNS allows in the entire 2002 address range into the 'us' DNS
view, this should be restricted to just your 2002/48 lan.

From here, please move on to the [OCEAN CITY INSTALLATION GUIDE]({{< relref "wiki/OCEAN_CITY_INSTALLATION_GUIDE.md" >}}).

### NB re: DNS

The bind/DNS code of recent builds of CeroWrt (e.g., bql and rc8 builds)
is not functional. For example, these builds do not support the
\*.home.lan dns names.
