
---
title: Save the Ants
date: 2011-06-19T19:16:01
lastmod: 2011-06-30T12:34:37
type: wiki
---
(Qos) Save the ANTS, cope with MICE, and shoot the ELEPHANTS
------------------------------------------------------------

HTB is probably the most commonly root qdisc in use today.

The shapers below it often "shoot" and drop packets in an indiscriminate
fashion, paying no attention to traffic type whatsoever, except as
configured by the person designing the QoS system.

Shooting the statistically rare yet system critical packets - call them
'ANTS' - ARP, DNS, NTP, various routing protocols, DHCP, VPN, and
various forms of icmp and (especially) icmp6 has no real effect on the
overall load on a router, nor does it reduce bandwidth requirements, and
in fact, in many cases (DHCP, VPN, DNS) results in MORE traffic, later,
being sent, and often a reduction in user experience that can be quite
noticeable (in the case of dns, dhcp, and vpns, in particular. DNS can
fall back to TCP....)

Shooting (or, better, marking) a TCP packet instead can reduce bandwidth
requirements by huge factors, and there are other protocols where
shootdowns (SCTP, etc), has similarly multiplied effects.

Also, TCP MICE are hard to shoot right and have a desirable effect.

Here are some [traffic analyses]({{< relref "wiki/bloat/Diffserv_statistics.md" >}}), which
can give you a feel for the ratios in one (atypical) home network.

So most shapers should make mildly greater efforts to avoid shooting
system critical packets, choosing another packet whenever possible.
Simply adding a two or three try mechanism for shoot-downs would nearly
eliminate random loss of these types of packets. On the second (or
third) try, shoot to kill, however, to avoid gaming the mechanism.

While correct usage of HTB would reduce this problem, by using multiple
buckets for multiply classified targets, few classifiers/shapers in the
field (try hard enough) (or have the tools to take better aim), so
implementing better policy in the kernel would immediately improve the
quality of userspace and linux networking.

Similarly, being able to clearly distinguish between Ants, mice and
elephants is hard...

Ants
----

Basically ! tcp suffices as an early match, except when it doesn't.
Further classification gets complex, rapidly.

TCP Mice
--------

The existing conntrack mechanism has the interesting ability to measure
the length of a TCP flow. It however, does not do a weighted average or
some other 'mouse detection' feature like packets/quantum, so as a TCP
flow that speeds up and down, cannot migrate from mouse to elephant and
back again. Conntrack can only go from mouse to elephant and stay there,
which is inappropriate for many protocols such as nfs/cifs filesharing,
ssh, etc. That said, it's soooo close, and effective classification of
mice to elephants would aid many shapers, several of which do try to use
conntrack in this way.

A common hack in the field (openwrt, at least) is to rate limit syns,
(often at very low values (25-50/sec are the openwrt defaults. Syn/ack
pairs could be used as a predictor of future work load, or syns could be
matched to fins.

Coping with the mice is a hard problem.

### Google Test - a,b,c,d,e

A very revealing test is what I call the google 'a,b,c,d,e' test - turn
on 'google interfactive', start capturing packets, and hit a - wait,
backspace b.... wait... c... d... e...

And look at the ants, mice, and elephants. Note especially the ratios
between successful synacks, the overall length of streams, the start
times, the delays, and the other packet losses.

### Elephants

Once you can clearly distinguish between ants, mice and elephants,
traffic shaping becomes easy. Shooting one elephant can save thousands
of other packets... once you choose the right elephant from the herd.

Enhancing ECN
-------------

Furthermore, ECN could be used in more cases by more shapers.

so adding a function, drop\_or\_mark\_packet(skb, flag), where flag has
the range 0 = SHOOT TO KILL, and 1..X where this marks what to not kill,
would be a boon. Return values would be -1 error, 0 if dropped, 1 if
marked, 2 if already marked 3..X if one of the reserved packet types.

Psuedocode for the logic would be:

    if (v = drop_or_mark_packet(skb,0xFFFFFFFF) > 1) 
    { 
      skb = choose_another_packet(somehow);
      if ( v = drop_or_mark_packet(skb,0xFFFF) > 1) {
         skb = choose_another_packet(somehow);
         v = drop_or_mark_packet(skb,0);
      }    
    }

    switch(v) {
        -1) Do something about the error;
         0) Log as dropped;
         1) Log as marked; /* Adding a comprehensive 'marking' 
                              structure to the existing 'drop' 
                              statistics is beyond the scope of 
                              this proposal, so you can log as 
                              dropped for now */
    }

</code>

drop\_or\_mark\_packet would make some attempts (matching against port
number and protocol type) to not shoot the aforementioned packet types,
except in the case where <link>ECN</link> marking can be used. It might
be good to have a more flexible means of controlling this behavior
rather than encoding this policy directly in the kernel, as no matter
how good the default, the real world is more complex.

and again - this would merely try harder to not shoot the system control
packets, ants and mice, but it will if it has to.

choose\_another\_packet(somehow) may be a non-trivial exercise for some
shapers.

Coping with TCP mice is a long difficult subject that needs to be dealt
with in some other way, except that shooting fins and fin/acks seems
rather counterproductive....
