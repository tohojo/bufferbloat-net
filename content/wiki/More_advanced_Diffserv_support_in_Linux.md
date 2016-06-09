
---
title: More_advanced_Diffserv_support_in_Linux
date: 2011-06-19T15:05:50
lastmod: 2011-06-20T05:06:27
---
More advanced Diffserv support in Linux
---------------------------------------

This part of the proposal becomes mildly more controversial in scope.

### Keeping good DSCP statistics

    -j DSCP --dscp-stats name

Getting a comprehensive view of traffic types can be done with a
sequence of 64 iptables rules, which is very inefficient. You can save
cpu and gain insight at a statistical level, for example, by having a
jump target for statistics collection of, say, every 100 packets, but,
still... It is very interesting and informative to have these statistics
available.

What is proposed with a --dscp-stats jump target is to have a table
generated much like how the existing match target functions,
incrementing 64 bit counters for each of the 64 traffic types and
presenting it in an easily parse-able format somewhere in /proc.

A problem is that the ipv6 and ipv4 namespaces are presently disjoint in
iptables, and dscp is basically an ip level match.

Perhaps it would be better to not do it at the iptables level but within
the kernel, enabled by a sysctl, as a per-device standard, so,\
for example, snmp could read it out of /{proc,sys}/net/device/something
to implement the diffserv-dscp-tc mib.

A problem introduced here is the (slight) added overhead of incrementing
one additional per-device offset counter all the time, and that usually
you are mangling incoming packets inside of iptables anyway, so the
place to do it is on output rather than input.

An alternative is to do it via tc, which is more hairy.

### Better classification into 8021.d and 802.11e QoS catagories

Once comprehensive classification is available, it is possible to map
distinct classes into their relevant 8 802.1d or 4 802.11e catagories.
In fact, it's nearly a direct match between 802.1d and 802.11e, so
classification into 802.1d could suffice to match\
802.11e. That leaves 3 bits worth of classification required per traffic
class, regardless of hardware QoS, and

Given the enhancements already discussed in this document, hardware
classification could be handled by a mere 7 matching rules for 8021.d
and 5 for 802.11e.

#### Example for 802.11e

    iptables -A P80211e -m dscp --dscp-classes EF,CS6 -j CLASSIFY --set-class 0:106
    iptables -A P80211e -m dscp --dscp-classes AF43,AF33,AF23,AF13,CS1 -j CLASSIFY --set-class 0:101
    iptables -A P80211e -m dscp --dscp-classes CS3,MICE -j CLASSIFY --set-class 0:104
    iptables -A P80211e -m dscp ! --dscp-classes CS3,MICE,AF43,AF23,AF13,AF33,EF,CS6 -j CLASSIFY --set-class 0:103

    iptables -A OUTPUT -o wlan+ -j P80211e

</code>

#### Better solution...

Would be to compress this into 3 bits per dscp value, for a lookup table
of 192 bits in length.

I don't have a suggested syntax for this, perhaps:

iptables -A OUTPUT -o wlan+ j CLASSIFY --from-dscp
CS3,MICE,AF43,AF23,AF13,AF33,EF,CS6 --to-priority 4,4,1,etc,etc

I don't really expect humans to enter these rules, as the command lines
are getting kind of long.

### Coping with multicast

Multicast on wireless can be especially devastating to the overall
health of the network. Even on wired, a significant amount of unfiltered
multicast can turn a GigE switch into a GigE hub. The overall effect of
bridging wired multicast to wireless is the equivalent of a self
inflicted DoS attack, at present. multicast IPTv requires special
handling, and there are no feedback mechanisms anywhere in the stack
that account for the monstrous difference in transmission rate for
example between 802.11n (up to 600Mbit) and multicast (2Mbit).

As for solutions... the solution is too long to fit in the corner of
this web site.
