
---
title: Wondershaper Must Die
date: 2013-12-29T01:50:36
lastmod: 2015-05-25T18:37:25
type: wiki
---
Wondershaper Must Die (editorial by Dave Taht)
==============================================

*Note: This editorial was written in December 2013, and has been updated
from time to time. But what should you use instead of Wondershaper?
CeroWrt's full suite of SQM shaping is now available in OpenWrt Barrier
Breaker and Chaos Calmer builds - http://openwrt.org Use SQM - it works
great.*

Wondershaper was great for its time (2002). It was one of the first
integrated [Smart Queue Management](Smart_Queue_Management.md) systems, incorporating
packet scheduling (SFQ), rate limiting, policing, and QoS in a tiny
amount of easily understandable code. It spread around the internet like
wildfire back then. Nearly every cybercafe I've been in, from the US to
Sri Lanka to Nicaragua, deploys it or some variant thereof to keep
latencies low and web/gaming/voice traffic optimal for dozens of users.
Dozens of more sophisticated [Smart Queue Management](Smart_Queue_Management.md) scripts
are descended from it. It worked well in its target environments. And
yet, WonderShaper's currently wrong, so wrong, for today's internet.
Much better alternatives exist.

To a huge extent the eventual development of fq\_codel was driven by
systematically addressing the faults in wondershaper, and coming up with
new techniques to handle today's wider variety of environments and
bandwidths. Our thinking ultimately led to the publication of the [smart
queue-ing
manifesto](http://gettys.wordpress.com/2013/07/10/low-latency-requires-smart-queuing-traditional-aqm-is-not-enough/)
.

Recently I've seen new activity making wondershaper (wondershaper "NG")
easier to use, and getting it into more distros, without addressing the
underlying faults. I am VERY GLAD people are trying to update it, as it
has a well-deserved reputation, and I sure wish we could update the
original definition of it, or create a wondershaper2, that was actually
more correct for today's environments, AND fix all the web references to
it.

But: the flaws are so legion and in nearly every line of code, that the
best I can hope for is to get the newer maintainers to at least address
the low lying fruit in it, and for my own efforts to continue with the
alternate line of work that is in CeroWrt's [SQM](SQM.md) system.

Wondershaper is a fine example of tight, well written, undercommented
code that doesn't work right anymore. So I'm going to paste the original
code here and comment on it in the hope that one day a better example
emerges, and as an object lesson that a smart network queue-ing system
that worked well yesterday may not work tomorrow.

Ironically... when the bufferbloat project started in 2011, I'd called
up Jim Gettys, told him I understood him, and volunteered to write this
article explaining all that was wrong with wondershaper (that I had
learned from a decade of using derivatives) I also agreed to loan him a
server... It's now 3 years of nearly full time work on bufferbloat later
and I'm just now getting around to writing the original intended rant.
My comments on the code are in \#\#s.

Wondershaper annotated source code
==================================

    #!/bin/bash
    # Wonder Shaper
    # please read the README before filling out these values 
    #
    # Set the following values to somewhat less than your actual download
    # and uplink speed. In kilobits. Also set the device that is to be shaped.

    DOWNLINK=800
    UPLINK=220
    DEV=ppp0

    ## At the time wondershaper was developed, DSL MTUs were typically 584 bytes
    ## and encapsulation-aware techniques that compensated for ATM and PPPoE didn't
    ## exist. An entire masters thesis got written by Jesper Brouer on fixing htb to
    ## to work right with ATM framing and the code landed in the kernel in 2005.
    ## http://www.adsl-optimizer.dk/

    ## Wondershaper was pretty optimal at 800kbit down 220 up, in 2002. That was when
    ## IW2 (Sending 2 584 byte packets in TCP's Initial Window) was used... and
    ## web pages averaged in size of 70k, and coexisted with ssh traffic and voip.
    ## It didn't scale up then, and doesn't work well at all now, at any bandwidth.
    ## See the plots at the bottom of this set of comments

    # low priority OUTGOING traffic - you can leave this blank if you want
    # low priority source netmasks
    NOPRIOHOSTSRC=

    ## NAT was not widely deployed at the time. Optimizing for source addresses
    ## doesn't WORK for Natted hosts in this code.

    # low priority destination netmasks
    NOPRIOHOSTDST=

    # low priority source ports
    NOPRIOPORTSRC=

    ## Same problem with NAT as the above

    # low priority destination ports
    NOPRIOPORTDST=

    # Now remove the following two lines :-)

    echo Please read the documentation in 'README' first
    exit

    ## Wondershaper was *demo* code intended to be READ and understood before
    ## using.

    if [ "$1" = "status" ]
    then
        tc -s qdisc ls dev $DEV
        tc -s class ls dev $DEV
        exit
    fi


    # clean existing down- and uplink qdiscs, hide errors
    tc qdisc del dev $DEV root    2> /dev/null > /dev/null
    tc qdisc del dev $DEV ingress 2> /dev/null > /dev/null

    if [ "$1" = "stop" ] 
    then 
        exit
    fi


    ###### uplink

    # install root HTB, point default traffic to 1:20:

    tc qdisc add dev $DEV root handle 1: htb default 20

    ## I have seen variants that use an incorrect default. Some use 0, which
    ## bypasses htb entirely for packets that aren't classified correctly.
    ## Doesn't handle ATM or PPPoE framing correctly as per the linklayer
    ## code in newer versions of htb

    # shape everything at $UPLINK speed - this prevents huge queues in your
    # DSL modem which destroy latency:

    tc class add dev $DEV parent 1: classid 1:1 htb rate ${UPLINK}kbit burst 6k

    ## The burst size was correct for 2002 internet which used TCP in IW2 and IW4
    ## (2 or 4 initial packets), at 584 bytes each.
    ## Today's internet is migrating to IW10, with a MTU of 1500 bytes prevailing,
    ## leading to a burst size far greater than 6k. And for all that, the "htb" 
    ## burst is actually a function of how fast your processor can schedule packet
    ## delivery. If you can schedule packets at 1.5k per burst, that's better than 6k. 

    # high prio class 1:10:

    tc class add dev $DEV parent 1:1 classid 1:10 htb rate ${UPLINK}kbit \
       burst 6k prio 1

    ## burst size wrong. Furthermore packets that match the highest priority 
    ## class can starve all the other classes.

    # bulk & default class 1:20 - gets slightly less traffic, 
    # and a lower priority:

    tc class add dev $DEV parent 1:1 classid 1:20 htb rate $[9*$UPLINK/10]kbit \
       burst 6k prio 2

    ## Same problem with burst size. Also, shaping at 90% for best effort made 
    ## sense if you were trying to reserve space for a classifiable VOIP call or
    ## ssh or dns when you only had 220kbit uploads... 
    ## but if you have a fatter uplink, say 10Mbit, you are just wasting
    ## available bandwidth for no reason. 

    tc class add dev $DEV parent 1:1 classid 1:30 htb rate $[8*$UPLINK/10]kbit \
       burst 6k prio 2

    # all get Stochastic Fairness:

    tc qdisc add dev $DEV parent 1:10 handle 10: sfq perturb 10
    tc qdisc add dev $DEV parent 1:20 handle 20: sfq perturb 10
    tc qdisc add dev $DEV parent 1:30 handle 30: sfq perturb 10

    ## SFQ was a breakthrough and why wondershaper became so popular so fast.
    ## However, the perturbation idea causes fat TCP flows
    ## to deliver out of order packets, often triggering a window reduction at the
    ## very least, costing bandwidth and latency. Perturbation was "improved" to 
    ## not deliver out of order packets in Linux 3.6. We didn't realize until much
    ## later that this rehashing was acting as a "poor man's AQM" - reordering/scrambling 
    ## fat tcp flows, which on most OSes, causes a reduction or reset of cwnd.
    ## (Linux TCP, around 3.9, gained much more robust reordering compensation
    ##  as well, mostly negating the scrambling of perturb 10)
    ## Comparing SFQ pre 3.2 to SFQ now would be a worthwhile exercise.

    ## (?) Still, periodically
    ## rehashing a stable system every 10 seconds seems to be a bad idea.
    ## fq_codel merely uses a unique hash per invocation, and shoots at
    ## latency causing flows to make them slow down

    ## Furthermore SFQ by default is limited to a buffer depth of
    ## 127 packets, which is too short for higher bandwidths.
    ## We "fixed that" allowing for larger flows and depth parameters
    ## but that led to too much buffering for lots of flows, and not
    ## enough for only one, at higher bandwidths. It was clear that
    ## to get SFQ to scale, we needed an aqm component, and thus
    ## SFQRED was born... and that also proved hard to tune.

    ## Also...
    ## I have seen people trying 7 bands of sfq queueing, which leads
    ## to the worst case buffering for the lowest priority flow to be 889 packets.
    ## To translate that into time, at 1Mbit, that translates to over 11 seconds
    ## of potential buffering in that case, well over any sane timeout for most
    ## protocols.

    ## If you impose a maximum depth of X on a flow, it might be too short
    ## if that flow is all you have. Or X will be inevitably too large
    ## if you have lots of flows... and if max-packets-in-queue is your
    ## only way of ever dropping packets, using multiple bands of 
    ## separate queues gradually makes your worst case results worse...

    ## After that exercise it was obvious that "X" needed to be an
    ## equation, and buffer space needed to be shared among queues.

    ## We later worked on "sfqred" which combined the RED AQM with SFQ
    ## which tried to hold queue depth to saner levels.

    ## It worked pretty good! Never got around to finishing the ARED version
    ## because then codel arrived...

    ## fq_codel automatically manages depth. It looks directly at the latency
    ## in the flow(s) and shoots at the fattest flows to get them to slow down.
    ## Codel can be combined with many other packet scheduling techniques to
    ## achieve the desired results, but so far the fq_codel variant is the winner.

    ## It's not perfect yet! At lower rates it helps to 
    ## fiddle with fq_codel's target and quantum. A smaller quantum (300)
    ## is useful for giving smaller packets a slight boost over bigger packets.

    ## You can easily swap out fq_codel for sfq in wondershaper and get a benefit.
    ## Between Linux 3.4 and Linux 3.6 Eric Dumazet did a lot of work implementing 
    ## ideas in SFQ that had been discarded as too hard back in 1992. See:
    ## http://www.rdrop.com/~paulmck/scalability/paper/sfq.2002.06.04.pdf‎

    # TOS Minimum Delay (ssh, NOT scp) in 1:10:

    tc filter add dev $DEV parent 1:0 protocol ip prio 10 u32 \
          match ip tos 0x10 0xff  flowid 1:10

    ## the 0xff only matches against non-ecn enabled flows. I think a correct version
    ## is 0xfc (or is it 0xcf?). IF you are going to use ECN, it's a good idea to use
    ## it on your latency and loss sensitive flows. ECN was standardized in 2002.
    ## Furthermore many ssh's don't use this marking.
    ## and this filter (and those that follow) do not apply against ipv6! Sure, go
    ## ahead, make ipv6 behave worse than ipv4 than it already does! 

    # ICMP (ip protocol 1) in the interactive class 1:10 so we 
    # can do measurements & impress our friends:
    tc filter add dev $DEV parent 1:0 protocol ip prio 10 u32 \
            match ip protocol 1 0xff flowid 1:10

    ## Impressing your friends is good for a demo, but in the real world you want
    ## to *deprioritize* icmp, not prioritize it. Putting it in your priority flow
    ## list, as is done here leaves you subject to ping flood attacks among other things
    ## Change to flowid 1:30.

    # To speed up downloads while an upload is going on, put ACK packets in
    # the interactive class:

    tc filter add dev $DEV parent 1: protocol ip prio 10 u32 \
       match ip protocol 6 0xff \
       match u8 0x05 0x0f at 0 \
       match u16 0x0000 0xffc0 at 2 \
       match u8 0x10 0xff at 33 \
       flowid 1:10

    ## There have been a lot of variants of this line in various implementations.
    ## One variant only prioritized 64 byte packets, which, as the TCP timestamp
    ## became common over the last decade, missed those (66 bytes).
    ## This also doesn't work against ipv6, nor against protocols like mptcp or sctp or QUIC.
    ## In reading this bit of magic today, I'm not sure what the whole string in this version
    ## really does. (?) ACK prioritization is very common in many devices and I'm pretty
    ## sure it's wrong in nearly all of them.

    # rest is 'non-interactive' ie 'bulk' and ends up in 1:20

    # some traffic however suffers a worse fate
    for a in $NOPRIOPORTDST
    do
        tc filter add dev $DEV parent 1: protocol ip prio 14 u32 \
           match ip dport $a 0xffff flowid 1:30
    done

    ## Explicitly deprioritizing some stuff is still a pretty good idea. However
    ## in an age where everything runs over port 80 and 443, not helpful.

    for a in $NOPRIOPORTSRC
    do
        tc filter add dev $DEV parent 1: protocol ip prio 15 u32 \
           match ip sport $a 0xffff flowid 1:30
    done

    ## doesn't work with NAT or ipv6

    for a in $NOPRIOHOSTSRC
    do
        tc filter add dev $DEV parent 1: protocol ip prio 16 u32 \
           match ip src $a flowid 1:30
    done

    ## doesn't work with NAT or ipv6. Note that some tc filters have gained
    ## the ability to look at pre-natted values in modern linux releases

    for a in $NOPRIOHOSTDST
    do
        tc filter add dev $DEV parent 1: protocol ip prio 17 u32 \
           match ip dst $a flowid 1:30
    done

    ## Still reasonable but not very useful

    # rest is 'non-interactive' ie 'bulk' and ends up in 1:20

    tc filter add dev $DEV parent 1: protocol ip prio 18 u32 \
       match ip dst 0.0.0.0/0 flowid 1:20

    ## No IPv6. And it's not necessary in light of the catchall rule
    ## for htb tossing unmatched packets into flowid 1:20

    ## Wondershaper needed this for the non-htb version.

    ########## downlink #############
    # slow downloads down to somewhat less than the real speed  to prevent 
    # queuing at our ISP. Tune to see how high you can set it.
    # ISPs tend to have *huge* queues to make sure big downloads are fast
    #
    # attach ingress policer:

    tc qdisc add dev $DEV handle ffff: ingress

    # filter *everything* to it (0.0.0.0/0), drop everything that's
    # coming in too fast:

    tc filter add dev $DEV parent ffff: protocol ip prio 50 u32 match ip src \
       0.0.0.0/0 police rate ${DOWNLINK}kbit burst 10k drop flowid :1

    ## The ingress policer doesn't work against ipv6, so if you have mixed traffic
    ## you are not matching all of it, and the policer fails entirely
    ## A correct, modern line for this would be:
    ## tc filter add dev ${DEV} parent ffff: protocol all match u32 0 0 \
    ## police rate ${DOWNLINK}kbit burst 100k drop flowid :1
    ## 
    ## Even if it did work, the police burst size is too small for higher speed 
    ## connections and what I suggest above for a burst size needs to be 
    ## a calculated figure.(that one works ok at 100mbit)

    ## My tests at 20Mbit showed the wondershaper default burst cut transfer rates in HALF.
    ## The modern day replacement for this is the IFB and mirred commands, tied
    ## to a htb implementation with fq_codel.
    ## Inbound policing was a useful idea made bad by the available technologies at the time.
    ## I have come to understand that we can, actually make better policers now, 
    ## and that inbound shaping is not the answer to all things. I call the core idea "bobbie"
    ## as that's what the unarmed police in England are called, and as it uses ideas from fq_codel that
    ## will make the actual rate "bob" up and down, in a kinder, gentler fashion, hopefully
    ## lighter weight than shaping, and support ECN - so it doesn't need to shoot packets, just tap them.
    ## That said, I despair of even writing it, given that where it needs to deploy is in places
    ## that linux does not currently touch.

I could sit here and rewrite wondershaper to keep the strength of it as
a coding example of how to use filtering, etc. OR: I could point you at
the [SQM](SQM.md) code in cerowrt, or the [traffic shaping example in
gentoo](https://wiki.gentoo.org/wiki/Traffic_shaping) .

Or I could show you a benchmark of what happens if you naively run
wondershaper rather than a modern fq\_codel based shaper. All benchmarks
were run on CeroWrt 3.10.24-4 or later.

Benchmarking Wondershaper vs CeroWrt's SQM
==========================================

WonderShaper at 25Mbit down, 4Mbit up
-------------------------------------

![](http://www.bufferbloat.net/attachments/198/149.20.63.30.rrul_noclassification-wondershaper-fixedecn.svg)

The black line is an average of the fat streams and does not account for
acks in the opposite direction or the measurement flows. In the latency
test (third part of the chart), the black line is also an average, and
each measurement stream stops at the first packet loss. (See
[RRUL test suite](/codel/wiki/RRUL_test_suite.md) for more details on this benchmark
and these plots.

Using wondershaper at this speed inbound bandwidth is less than HALF of
what has been specified, and the outbound streams - despite being
optimized, still get 12ms of extra induced latency. The SFQ tail drop
buffering scheme causes huge swings in data delivery, too. Somewhere
around here I have an example of what permutation used to do to tcp in
older Linux versions. It isn't pretty.

CeroWrt's fq\_codel based SQM at 25Mbit down, 4Mbit up
------------------------------------------------------

![](http://www.bufferbloat.net/attachments/199/149.20.63.30.rrul_noclassification-ethernet.svg)

Here you can see over twice the incoming bandwidth, 60% less induced
latency in the measurement streams,\
and much "tighter" behavior of the tcp streams. Note this is also
against the simplest shaper in CeroWrt, were this\
to be against the three band one, the EF and ICMP streams would be
prioritized.

In short: Wondershaper is thoroughly obsolete. Yes, it can be improved.
But if you improve it you end up with something else entirely.

Some additional graphs:
=======================

WonderShaper configured at 800kbit down 220kbit up on the same test.
--------------------------------------------------------------------

![](http://www.bufferbloat.net/attachments/200/wshaper-800-220.svg)

The graph is spotty as tcp up is really, really hurting, and downloads
aren't as good as they could be. And you can see the buffer depth in sfq
causing nearly 300ms latency for the measurement streams. But ping?
Ping, oh man, that's optimized. Just what you need to impress your
friends, right?

800x220, with CeroWrt fq\_codel SQM
-----------------------------------

Note: fq\_codel here has target of 60ms and is ecn enabled.

![](http://www.bufferbloat.net/attachments/201/3band-800-220.svg)

We still have problems with the graphing tool... but we do considerably
better across the board. However we still lose the measurement streams
due to collateral damage from ecn and the DRR based system fq\_codel
uses.

800x220 nfq\_codel based CeroWrt SQM
------------------------------------

(nfq\_codel is fq\_codel modified to behave more like SFQ for lower
bandwidths. Despite the filename ecn was disabled)

![](http://www.bufferbloat.net/attachments/202/nfq_codel-800-220-ecn.svg)

(nfq\_codel, because it is more sfq-like is better at preserving low
rate flows than fq\_codel is.)

NOTE: It would be good for me to re-run these benchmarks at
wondershaper's original speed range and mtu.\
A comparison vs htb with and without atm compensation would be good too.

### Attachments
{{< attachment name="149.20.63.30.rrul_noclassification-wondershaper-fixedecn.svg" type="image/svg+xml" description="wondershaper" filename="131229042406_149.20.63.30.rrul_noclassification-wondershaper-fixedecn.svg" >}}
{{< attachment name="149.20.63.30.rrul_noclassification-ethernet.svg" type="image/svg+xml" description="ceroshaper" filename="131229042558_149.20.63.30.rrul_noclassification-ethernet.svg" >}}
{{< attachment name="wshaper-800-220.svg" type="image/svg+xml" description="wondershaper at 800kbit 220 kbit" filename="131229050304_wshaper-800-220.svg" >}}
{{< attachment name="3band-800-220.svg" type="image/svg+xml" description="" filename="131229050543_3band-800-220.svg" >}}
{{< attachment name="nfq_codel-800-220-ecn.svg" type="image/svg+xml" description="nfq_codel" filename="131229051851_nfq_codel-800-220-ecn.svg" >}}
