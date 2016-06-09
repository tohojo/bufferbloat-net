
---
title: CeroWrt 37 Release Notes
date: 2013-03-11T07:13:57
lastmod: 2014-07-25T02:46:56
---
CeroWrt 3.7 Release Notes
=========================

This release is obsolete. Please See the <link>CeroWrt 310 Release
Notes</link> for the current release.

CeroWrt is a routing OS built on the [OpenWrt
firmware](http://openwrt.org) . It is a research project intended to
resolve the bufferbloat epidemic in home networking today, and to push
forward the state of the art of edge networks and routers. Subprojects
include proper IPv6 support, tighter integration with DNSSEC, and most
importantly, reducing bufferbloat in both the wired and wireless
components of the stack.

The current CeroWrt release is code-named "Modena", version
[3.7.5-2](http://snapon.lab.bufferbloat.net/~cero2/cerowrt/wndr/3.7.5-2/)
, built on 3 February 2013\
Download the latest build from from
http://snapon.lab.bufferbloat.net/\~cero2/cerowrt/wndr/3.7.5-2/

CeroWrt Modena has proven to be highly stable, both from an ordinary
operational standpoint as well as being able to survive heavy load
testing. A number of people are using it as their primary router.

**Features**

The CeroWrt 3.7 series of builds include the following features and
capabilities:

-   Linux 3.7.5 kernel. Many of the fixes for bufferbloat are being
    implemented in this 3.7 kernel, so we are tracking these
    developments carefully. http://kernel.org
-   The [CoDel](http://www.bufferbloat.net/projects/codel/wiki)
    algorithm from Kathie Nichols and Van Jacobson along with Eric
    Dumazet's adaptation of Fair Queueing (fq\_codel) on top. These in
    turn rely on the Byte Queue Limits that were implemented in the
    Linux 3.3 kernel. These techniques replace earlier Active Queue
    Management fixes for bufferbloat including: Stochastic Fair
    Queueing-Random Early Drop (SFQRED), but for comparison previous
    technologies such as SFQ and RED continue to be included.
-   Test releases of ns2\_codel and nfq\_codel - built on top of the
    current ns2 models of the code and not yet in mainline linux.

<!-- -->

-   IPv6 support. Another major goal of CeroWrt is to make IPv6
    networking in the home as simple as IPv4.
-   Babel mesh routing protocol (Quagga-babeld). Other protocols such as
    ra, ospf, and bgp are also available.
-   DNSSEC and DNSSEC proxying - Secure extensions to the DNS system.
    Proxying is currently in testing.
-   OpenWrt features. Because we track the OpenWrt code base carefully,
    we incorporate most of the capabilities of that distribution. We
    actively push our changes/enhancements back toward the
    OpenWrt trunk. http://openwrt.org
-   An attractive web GUI for configuration - LuCI
-   CeroWrt has the following packages either built-in and enabled, or
    optionally loaded:

**IPv6 packages:**\
- radvd has been obsoleted as the new features in dnsmasq replace it\
- dhcpv6-pd support\
- dhcpv6 server support\
- 6to4 version 9-1 - IPv6 tunnel through IPv4 (not turned on by
default)\
- 6in4 version 11-1 - IPv6 tunneling (not turned on by default)\
- 6rd\
- wide-dhcpv6-client replaced with the new features in dnsmasq

**Other modules:**\
- strongswan4 4.5.3-2 - IPsec VPN http://www.strongswan.org/\
- avahi-daemon 0.6.30-4 - reflector for zeroconf/mDNS-SD/Bonjour names
http://avahi.org/\
- samba36-server 3.6.5-2 - file and printer service
http://www.samba.org\
- ntp 4.2.7p256-1 - network time client http://www.ntp.org/\
- enhancements to the LuCI web GUI\
- iptables 1.4.12.2-1git-5 - framework for packet filtering and network
address/port translation http://www.netfilter.org/\
- iproute2 - utilities for controlling TCP/IP traffic in a Linux kernel
http://www.linuxfoundation.org/collaborate/workgroups/networking/iproute2\
- dnsmasq 2.66-13beta - DNS forwarder and DHCP server designed for home
routers and NAT http://www.thekelleys.org.uk/dnsmasq/doc.html

**Other measurement tools are available for installation:**\
- snmpd 5.4.2.1-5 - for monitoring network traffic\
- fprobe 1.1-1 for monitoring NetFlow traffic\
- iperf 2.0.5-1\
- scamper

Releases
--------

### 3.7.5-2 "Modena"

Bind9 is obsoleted\
Openvpn will be available in a later release

Experimental stuff

- ns2\_codel, nfq\_codel, efq\_codel available optionally\
- wifi queuing boosted from very low values to a compromise that
preserves more bandwidth\
- debloat change to lower target to 5ms, quantums to 1000

### 3.7.5-2

- bind removed\
- 6to4 fixes for interface assignment\
- 6to4 route propagation workaround (\#406)\
- AQM gui module removed (too confusing, wasn't working stuff)

Experimental Stuff

- wifi queuing kept at low values\
- debloat change to lower target to 5ms, quantums to 256 (from mtu)
