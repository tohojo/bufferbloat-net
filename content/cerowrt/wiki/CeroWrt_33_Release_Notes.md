---
title: CeroWrt 33 Release Notes
date: 2012-03-17T07:41:45
lastmod: 2013-03-16T10:21:33
type: wiki
---
CeroWrt 3.3 Release Notes
=========================

CeroWrt is a routing OS built on the [OpenWrt
firmware](http://openwrt.org) . It is a research project intended to
resolve the bufferbloat epidemic in home networking today, and to push
forward the state of the art of edge networks and routers. SubProjects
include proper IPv6 support, tighter integration with DNSSEC, and most
importantly, reducing bufferbloat in both the wired and wireless
components of the stack.

The final CeroWrt 3.3 "Sugarland" build is
[3.3.8-26](http://huchra.bufferbloat.net/~cero1/3.3/3.3.8-26/) , built
on 18 Sept 2012.\
Download from http://huchra.bufferbloat.net/\~cero1/3.3/3.3.8-26/

**Note:** The Sugarland set of builds has been superceded by the [Modena
(3.7) set of
builds](http://www.bufferbloat.net/projects/cerowrt/wiki/CeroWrt_37_Release_Notes)

**Features**

The CeroWrt 3.3 series of builds include the following features and
capabilities:

-   Linux 3.3.8 kernel. Many of the fixes for bufferbloat are being
    implemented in this 3.3 kernel, so we are tracking these
    developments carefully. http://kernel.org
-   The [CoDel](http://www.bufferbloat.net/projects/codel/wiki)
    algorithm from Kathie Nichols and Van Jacobson along with Eric
    Dumazet's adaptation of Fair Queueing on top. These in turn rely on
    the Byte Queue Limits that were implemented in the Linux 3.3 kernel.
    These techniques replace earlier Active Queue Management fixes for
    bufferbloat including: Stochastic Fair Queueing-Random Early Drop
    (SFQRED), but for comparison previous technologies such as SFQ and
    RED continue to be included.

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
- radvd 1.8.3-3 - router advertisement daemon
http://www.litech.org/radvd/\
- 6to4 version 9-1 - IPv6 tunnel through IPv4 (not turned on by
default)\
- 6in4 version 11-1 - IPv6 tunneling (not turned on by default)\
- 6rd\
- wide-dhcpv6-client 20080615-11 - DHCPv6 support for IPv6

**Other modules:**\
- strongswan4 4.5.3-2 - IPsec VPN http://www.strongswan.org/\
- openvpn 2.2.2-2 - SSL VPN http://openvpn.net/\
- avahi-daemon 0.6.30-4 - reflector for zeroconf/mDNS-SD/Bonjour names
http://avahi.org/\
- samba36-server 3.6.5-2 - file and printer service
http://www.samba.org\
- bind 9.9.1-P1-19 - fast, stable DNS support
http://www.isc.org/software/bind\
- ntp 4.2.7p256-1 - network time client http://www.ntp.org/\
- enhancements to the LuCI web GUI\
- iptables 1.4.12.2-1git-5 - framework for packet filtering and network
address/port translation http://www.netfilter.org/\
- iproute2 - utilities for controlling TCP/IP traffic in a Linux kernel
http://www.linuxfoundation.org/collaborate/workgroups/networking/iproute2\
- dnsmasq 2.62-4 - DNS forwarder and DHCP server designed for home
routers and NAT http://www.thekelleys.org.uk/dnsmasq/doc.html

**Other measurement tools are available for installation:**\
- snmpd 5.4.2.1-5 - for monitoring network traffic\
- fprobe 1.1-1 for monitoring NetFlow traffic\
- iperf 2.0.5-1\
- scamper

Releases
--------

### 3.3.8-26 "Sugarland"

- bind-9.9.1-P3 CVE fix

Experimental stuff

- ns2\_codel, nfq\_codel, efq\_codel available optionally\
- wifi queuing boosted from very low values to a compromise that
preserves more bandwidth\
- debloat change to lower target to 5ms, quantums to 1000

### 3.3.8-17

- bind-9.9.1-P2 CVE fix\
- 6to4 fixes for interface assignment\
- 6to4 route propagation workaround (\#406)\
- AQM gui module removed (too confusing, wasn't working stuff)

Experimental Stuff

- wifi queuing kept at low values\
- debloat change to lower target to 5ms, quantums to 256 (from mtu)
