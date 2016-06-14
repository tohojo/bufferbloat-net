
---
title: Default network numbering
date: 2011-07-09T20:18:03
lastmod: 2013-03-16T11:19:33
type: wiki
---
Default network numbering
=========================

172.30.42.X range
-----------------

CeroWrt is a test platform, and as such we wanted it to co-exist within
existing networks as best as possible, without conflicting with an
existing network, and to not require NAT in order to function inside
that network. NAT skews some test results horribly.

Since there is no public IP address space left, 10.X.X.X networks are
being increasingly used as backbone networks, and 192.168.X is most
likely a number you are already using on your existing network, we chose
the 172.16.0.0/12 range to play in. The default address for the router
is 172.30.42.1.

It is ironic that this is the last piece of 'free' IP address space
left. See also [BANA]({{< relref "bloat/wiki/BANA.md" >}}).

If you find this IP hard to remember or type, DNS is enabled by default
for a virtual subdomain of *home.lan*. You should be able to get to it
via *gw.home.lan* if you get dhcp from the router and you can, of
course, change this to a REAL subdomain of your own otherwise vanity web
site name, if you want!

Changing the default ip address ranges is difficult to do via the web
interface and we suggest you stick with it for a while until you
understand the reasoning, firewall, routing, and naming rules. If you
really must, read [Changing your cerowrt ip addresses](Changing_your_cerowrt_ip_addresses.md).

If you are running CeroWrt inside your network, and not as your default
gw, configure your default gw to statically assign an ip address, and
route your subnet to the CeroWrt router, and turn off NAT.

/27 subnet
----------

The 'standard of 192.168.0.1' with a /24 netmask of 255.255.255.0 for a
home network is obsolete. EVERY piece of gear comes up on that. Yes,
it's simple, but:

1.  bridging together GigE (1000Mbit) with wireless (1Mbit
    for multicast) - doesn't work. One wired user can wipe out the
    entire wireless network with traffic. Once you concede this point...
    multiple networks are the only choice.
2.  Nobody has 255 machines on one network.
3.  CIDR has been a standard since 1992.
4.  We wanted to add more flexibility and security into a home or small
    business LAN
5.  A practical upper limit for wireless is about 30 devices per radio.

So we chose a different approach. Since /27 (255.255.255.224) netmasks
result in 30 usable IP addresses, we broke the network into 8 equivalent
pieces, laid out as follows:

  -------------------- ----------------- -----------------------------------
  =.**IPv4 address**   =.**Interface**   =.**Description**
  =.Public IP          =.ge00            Gateway Ethernet to Internet
  =.1-30               =.se00            Secure Ethernet for wired devices
  =.33-62                                No interface
  =.65-94              =.sw00            Secure Wireless (2.4 Ghz)
  =.97-126             =.sw10            Secure Wireless (5.x Ghz)
  =.129-158            =.gw00            Guest Wireless (2.4 Ghz)
  =.161-190            =.gw10            Guest Wireless (5.x Ghz)
  =.193-222            =.                Mesh
  =.225-254            =.                DMZ
  -------------------- ----------------- -----------------------------------

In practice you will hardly notice this setup on a new LAN, in fact, we
expect overall performance to be 'smoother', especially if you migrate
your newer devices to 5.x GHz and leave the 2.4GHz to legacy stuff like
bluetooth and microwave ovens.

Integrating it with an existing LAN is a bit more difficult. Multicast
(dns, service discovery, Windows filesharing, etc) is an issue - however
it can be solved with regular DNS, a multicast responder, and a Samba
WINS server. These are installed by default.

We want to make the integration problems easier to solve, out of the
box, over time, and we hope you will see enormous performance benefits
by leaving things split apart.

In the meantime, we'd love to know what current services don't work when
split across multiple subnetworks like this.

### See also

[Default naming scheme](Device_naming_scheme.md)\
[Changing IP, DNS, and SSID](Changing_your_cerowrt_ip_addresses.md)\
[Automated Configuration of CeroWrt](Automated_Configuration_of_CeroWrt.md)
