---
title: CeroWall
date: 2012-04-09T23:41:54
lastmod: 2014-12-01T13:19:39
type: wiki
---
CeroWall
========

What if we started with the idea that we wanted to use more protocols
than just a port 80 and 433 of tcp, and port 53 of udp, that we've been
able to effectively NAT? Hip, PIM, IGMP, sctp, dccp, udp-lite, rtp,
multicast, name it, it could all get tested now, and made to work with
ipv6, at the very least. We could share networks, and deploy different
solutions, if only we had a base to start with that didn't start with
the assumptions of ipv4 + nat.

So I sat down one day last year (june, 2011), and tried to design a
firewall architecture that did ipv6 first, and treated NAT as an
afterthought, allowing for security within a home, but a nearly default
free zone to share with guests. Part of it is the [device naming scheme](Device_naming_scheme.md), and the other part is the limited pattern matching
facility in iptables (the "+" symbol for a tail match). I'd also hoped
to get to where upnp and pcp could be made to work correctly, and
sanely.

The big goal was to have a firewall that never had to reload its rules
(and break connection tracking among other things). With the rise of
highly dynamic ipv6 addressing and prefix distribution it would be nice
to have the firewall just successfully add and subtract addresses
without ever having to reload. Unfortunately doing that easily requires
mangling interface names into one scheme to rule them all, which does
not play well with naming vlans (eth0.2) or various virtual tunneled
interfaces (ipv6-vtun), etc. Presently in most firewalling systems
devices are named after their function, not their level of security.

I've not got a chance to finish CeroWall, and coping with 15 years of
accumulated cruft around nat - port forwarding, menu driven guis,
zillions of useful features, and user preconceptions, and my own
workload! seems to make it unlikely I will. Perhaps nftables will make
it easier, but it breaks the + syntax in favor of doing vmaps.

But this is as far as I had got a few years back.

The logic is easy to parse. With 6 interfaces it's about 1/10th as
complex as what openwrt generates, and the rules are sorted by frequency
of protocol, so they are very fast. And **all** protocols are supported
out of the box, except for ipv4 on the natted interface. And due to the
pattern match, the rules never need to be taken down and reloaded, you
just create a named interface that fits the rule.

The rules work. I use them, in the lab. Where I don't have to deal with
nat.

IPv6 section

    #!/bin/sh

    ip6tables -t mangle -F
    ip6tables -F

    ip6tables -N F_TCP
    ip6tables -N F_UDP
    ip6tables -N F_ICMP
    ip6tables -N F_LAN

    # Generic Rules against ingress to the home secure zone

    ip6tables -A F_TCP -p tcp -m multiport ! --ports 139,445,81 -j ACCEPT
    ip6tables -A F_TCP -j REJECT

    ip6tables -A F_UDP -p udp -m multiport ! --ports 137,138 -j ACCEPT
    ip6tables -A F_UDP -j REJECT

    ip6tables -A F_ICMP -j ACCEPT

    ip6tables -A F_LAN -p tcp -g F_TCP
    ip6tables -A F_LAN -p udp -g F_UDP
    ip6tables -A F_LAN -p icmpv6 -g F_ICMP
    ip6tables -A F_LAN -p 0 -j ACCEPT

    ip6tables -A FORWARD ! -i s+ -o s+ -g F_LAN
    ip6tables -A FORWARD -j ACCEPT

    # Don't allow anyone from the internet to access samba or conf on the router

    ip6tables -I INPUT -p tcp ! -i s+ -m multiport --ports 139,445,81 -j REJECT

    # Grey areas
    # SNMP should be blocked

    # Classification

The IPv4 rules are nearly identical, but I never got around to finishing
the nat side

    #!/bin/sh
    MASQ=ge00

    [ -s "$MASQ" ] && iptables -t nat -F
    iptables -t mangle -F
    iptables -F

    iptables -N F_TCP
    iptables -N F_UDP
    iptables -N F_ICMP
    iptables -N F_LAN

    # Generic Rules against ingress to the secure zone

    iptables -A F_TCP -p tcp -m multiport ! --ports 139,445,81 -j ACCEPT
    iptables -A F_TCP -j REJECT

    iptables -A F_UDP -p udp -m multiport ! --ports 137,138 -j ACCEPT
    iptables -A F_UDP -j REJECT

    iptables -A F_ICMP -j ACCEPT

    #no workie
    #iptables -A MASQ -i $MASQ -o ! $MASQ -m state --state RELATED,ESTABLISHED -j ACCEPT
    #iptables -A MASQ ! -i $MASQ -o $MASQ -j ACCEPT

    iptables -A F_LAN -p tcp -g F_TCP
    iptables -A F_LAN -p udp -g F_UDP
    iptables -A F_LAN -p icmp -g F_ICMP
    iptables -A F_LAN -p 0 -j ACCEPT

    iptables -A FORWARD ! -i s+ -o s+ -g F_LAN

    # Don't allow anyone from the internet to access samba on the router

    iptables -I INPUT -p tcp ! -i s+ -m multiport --ports 139,445,81 -j REJECT

    # But I've never finished the nat rules

    if [ -s $MASQ ]
    then
       iptables -t nat -A POSTROUTING -o $MASQ -j MASQUERADE
    else
       iptables -A FORWARD -j ACCEPT
    fi

Routing ipv6 with ipv4 natted interfaces
----------------------------------------

It is impossible at present to detect if nat is on an interface. CeroWrt
assumes that ge00 is natted, and that there is nobody listening for ipv6
routes on the outside interface. In [Bloatlab 1](BloatLab_1.md), that's not
the case, and uncommenting the ge00 interface in /etc/config/babel, and
prepending these two lines here to the /etc/babeld.conf file

    out if ge00 ip 0.0.0.0/0 deny
    in if ge00 ip 0.0.0.0/0 deny

Lets the internal ipv6 routes 'escape' onto the same switch ge00 is on,
but not the natted ipv4 routes.

That switch in my case, has a dozen+ machines and router on it. It's
darn useful to be able to share that wire. Nearly every machine in the
lab is capable of routing (both with babel native and quagga-re), and if
one is down, the next best one takes over.

You'll note, incidentally, that opening up ge00 for routing breaks part
of the above firewall rules (blocking several ports by incoming
interface) in a fairly unsolvable way.

In a microcosm, this is one of the problems of ipv6. It would be rather
awesome if two people sharing the same wire (cable modems, anyone?)
could route to each other with a minimum of hops and inherent latency.
