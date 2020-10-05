---
title: Cake
date: 2015-04-11T11:10:42
lastmod: 2020-10-05T15:46:00
type: wiki
---
Cake - Common Applications Kept Enhanced
========================================

**Development on Cake was orignally sponsored by**
[IIS](http://www.iis.se) and is now sponsored by
[NLnet](http://nlnet.nl) We appreciate their support... and could always
use more help from others that care about speeding up the internet.

Cake is the rollup of 3 years of deployment experience of the htb +
fq\_codel based sqm-scripts [SQM](/cerowrt/wiki/SQM.md) for aqm/fq/qos
inbound and outbound bufferbloat management. For input into the design
and implementation, please join the [cake mailing
list](https://lists.bufferbloat.net/listinfo/cake) . For an alternative
approach to inbound traffic management, see [Bobbie](Bobbie.md).

[CAKE FAQ](CakeFAQ.md) - Frequently Asked Questions.

[CAKE Recipes](CakeRecipes.md) - Example settings.

Slides from a talk on Cake, at Battlemesh v8:
attachment:cake-battlemesh-v8.pdf

Features and enhancements of cake over htb + fq\_codel
------------------------------------------------------

### 8 way set associativity

This makes the hash collision problem Toke pointed out in fq\_codel at
the ietf meeting previous **go away** even for REALLY large numbers of
flows. We note that this is not a panacea in that it means that the
codel portion of the algorithm gets less chance to run and proves
problematic... (cake stablizes at a much higher delay than we would like
right now) but it does mean that we get way better flow isolation in
general, which may lead to a more ideal aqm implementation.

### An integral shaper (that can be on or off or tuned dynamically)

Is much "tighter" than htb - uses about 30% less cpu on low end hardware
(don't take that as a final or even accurate figure!) , and is less
"bursty".

### TSO/GSO/GRO "peeling"

![](https://www.iis.se/docs/iis_logo-160x160.png)\
![](https://nlnet.nl/logo/banner-320x120.jpg)

Many ethernet device drivers and tcp stacks bulk up multiple packets for
one destination into a offloaded "superpacket" that is handed off to the
hardware. This dynamic range of 1000x1 is very hard on aqm and fq
algorithms which seek to have minimal drops and maximal fairness.

And yet, at higher rates (&gt;100mbit), present day hardware requires
those offloads be present in order to achieve maximum utilization.

So cake, when shaping to a lower rate than gigE, will peel apart large
superpackets back into packets again, and thus fq and aqm them better
than fq\_codel did.

Preliminary indications are that not doing GRO "peeling" is where the
first generation of fq\_codel enabled 802.11ac routers went wrong in
their QoS systems.

### Command line interface is WAY simpler than htb + fq\_codel


    tc qdisc add dev eth2 root cake bandwidth 50mbit
    Usage: ... cake [ bandwidth RATE | unlimited* | autorate_ingress ]
                    [ rtt TIME | datacentre | lan | metro | regional | internet* | oceanic | satellite | interplanetary ]
                    [ besteffort | squash | precedence | diffserv8 | diffserv4* ] # diffserv variants including none
                    [ flowblind | srchost | dsthost | hosts | flows* ] # hash algorithm on what fields
                    [ atm | noatm* ] [ overhead N | conservative | raw* ]
        (* marks defaults)

    (squash) removes DSCP from packets and applies 'besteffort' to the result
    (flowblind) gives pure single queue codel aqm behavior, useful for testing the new codel implementation
    (autorate_ingress) is very experimental

### ECN always on with overload protection

(so it cannot be easily gamed)

### ECN also done more right when in overflow mode

(drop then mark for an immediate congestion signal)

### Better codel model

(tighter recovery algorithm, more accurate invsqrt, earlier kick in on
overload)

### Packet limit management done with bytes rather than packets

Despite these new algorithms tightly controlling the queue size,
practical circumstances (available memory) and resistance to attacks
requires there be some outside limit at which point the qdisc
arbitrarily drops packets. fq\_codel, codel, pie, and others all use a
per packet limit.

Per packet limits has a dynamic range of roughly 1000x1 (64k to 64
bytes). This is really hard to cope with. A small limit might run you
short on keeping the device fed (for small packets) yet completely
overwhelm the memory on big (offloaded with GRO/TSO/GSO) packets.

A sensible byte limit, on the other hand has a dynamic range of about
4x1 in the worst case (each packet has about 256 bytes of overhead
associated with it, so a 64 byte packet is 5x bigger than it should be,
but a 1500 byte packet only a few percent). Additionally, when cake is
handed a bandwidth argument, it is possible to come up with a reasonable
size based on the BDP and a few heuristics, to come up with a reasonable
outer limit. To what degree cake is coming up with reasonable outer
limits right now, is still a matter of debate and coding.

### Extensive framing compensation (for DSL/ATM/PPPoe)

The initial cake-overhead patch included only “raw” and “conservative”
shortcut keywords, alongside the numeric “overhead” parameter for
experts. I’ve now worked out an extended set of keywords which, I think,
takes care of all the normal cases.

There are eight new keywords which deal with the basic ADSL
configurations. These switch on ATM cell-framing compensation, and set
the overhead based on the raw IP packet as a baseline.

ipoa-vcmux (8)\
ipoa-llcsnap (16)\
bridged-vcmux (24)\
bridged-llcsnap (32)\
pppoa-vcmux (10)\
pppoa-llc (14)\
pppoe-vcmux (32)\
pppoe-llcsnap (40)

Note that “pppoa-llc” is not a typo - it really doesn’t involve SNAP,
and is thus a little more compact than if it did.

Two more new keywords deal with the basic VDSL2 configurations. Again,
the overheads use IP as a baseline, but this time ATM cell-framing is
turned off.

pppoe-ptm (27)\
bridged-ptm (19)

For those interested in shaping ethernet links the following keywords
are defined.

ether-phy (20) - pre-amble, inter-frame gap\
ether-all (24) - pre-amble, inter-frame gap & Frame Check Sequence

The final three keywords are not for standalone use, but act as
modifiers to some previous keyword. They can be specified more than
once, which is probably only useful for “ether-vlan”.

via-ethernet (-14)\
ether-fcs (+4)\
ether-vlan (+4)

### Diffserv support

Based on the efforts of the ietf "Dart" working group, we have a rough
set of classifications that make sense into 4 bins of priority, but
getting this right, too, is a matter of debate. Certainly 8 seems like
overkill. Pure precedence is in cake as an option also, based on the
CSX-CS7 set of priorities but it should not be used in a modern diffserv
installation.

The only way we know how to "fix" bittorrent is to classify it somewhat,
somehow, as "background".

sqm-scripts used 3 tiers of priority pretty successfully as does
free.fr. - de-prioritization seems a good idea, prioritization not so
much.

Some of the history
-------------------

We have been discussing/working on this for about two years. Work
stalled out on the first two versions in september 2014 (after we hit
some major snags also). Jonathan could not work for free anymore
either... As of April 2015, he was committed to 2-3 months work (via
a donation), and we made some serious progress.

At line (native) rate cake uses more cpu than what fq\_codel does.

At a shaped rate, it does much better than htb + fq\_codel does. There
are a lot of easy cpu speed up mods left to make, but we prefer to work
on fixing two problematic bits of codel right now... adding other
features, and fixing bugs.

CAKE is largely Jonathan Morton's work, based on extensive discussions
with Dave Taht, Toke, and Eric Dumazet and fragments of the various
codel and fq\_codel stuff Dave Taht had done over the last 3 years. In
particular, the set associative hash, shaper, and diffserv code
innovations are all Jonathan's contributions.

Some Statistics
---------------

Here are tons of statistics tested live on a comcast 115Mbit/12Mbit
connection. You can see both drops and marks (as the new overload
protection kicks in).

The Pk delay is the ewma of the delay being experienced by the fat flow.
Av is average. sp is the delay experienced by "sparse" flows - typical
voip dns etc that fq\_codel already did so well that we have always
found hard to measure.\
You do not see anything real for pk,av, etc because the tc dump was
taken after the test.

The "way" stuff is related to the 8 way set associative hash. We never
had a collision on this test - it is going to take serious work to
create a test that will create one!

### Inbound rate limiter:


    qdisc cake3 8021: root refcnt 2 bandwidth 115Mbit diffserv4 flows
     Sent 854846030 bytes 601627 pkt (dropped 3, overlimits 502755 requeues 0) 
     backlog 0b 0p requeues 0
               Class 0     Class 1     Class 2     Class 3
      rate       115Mbit  107812Kbit   86250Kbit   28750Kbit
      target       5.0ms       5.0ms       5.0ms       5.0ms
    interval     105.0ms     105.0ms     105.0ms     105.0ms
    Pk delay        28us       165us       171us         0us
    Av delay         2us         3us         4us         0us
    Sp delay         0us         2us         3us         0us
      pkts        279494           6           6           0
    way inds           0           0           0           0
    way miss         126           2           4           0
    way cols           0           0           0           0
      bytes    854849821         702         763           0
      drops            3           0           0           0
      marks           65           0           0           0

I note that this is 1 minute of the rrul test to get this drop/mark
rate. It is useful to get a feel for what is a "good" drop rate is by
plunking these into a spreadsheet and to factor in the actual bandwidth
and bytes transferred, AND to use varying numbers of flows. Most people
do not have intuition here.

### Outbound rate limiter

    qdisc cake3 8020: root refcnt 9 bandwidth 12Mbit diffserv4 flows
     Sent 89763694 bytes 252935 pkt (dropped 29, overlimits 446956 requeues 0) 
     backlog 0b 0p requeues 0
               Class 0     Class 1     Class 2     Class 3
      rate        12Mbit   11250Kbit       9Mbit       3Mbit
      target       5.0ms       5.0ms       5.0ms       6.1ms
    interval     105.0ms     105.0ms     105.0ms     106.1ms
    Pk delay       6.4ms        33us         0us       5.4ms
    Av delay       1.7ms         2us         0us       1.7ms
    Sp delay         0us         0us         0us         0us
      pkts         50193       86214           0       98744
    way inds           0           0           0           0
    way miss           7         137           0           6
    way cols           0           0           0           0
      bytes     14462333    52805488           0    22497221
      drops           20           1           0           8
      marks          294          86           0         621
    qdisc ingress ffff: parent ffff:fff1 ----------------
     Sent 830112863 bytes 601877 pkt (dropped 0, overlimits 0 requeues 0)
     backlog 0b 0p requeues 0

Installing "CAKE" out of tree on Linux
--------------------------------------

CAKE is included in upstream Linux as of kernel v4.19. This means it is
available out of the box on most modern Linux distributions. If you're running
an older kernel, you can compile the out-of-tree version as follows:

Do a:

**IF you have kernel source installed to leverage, adding cake is as
easy as**


    git clone https://github.com/dtaht/sch_cake.git

    cd sch_cake
    make; sudo make install

To use it properly, you will also need to build and install the iproute
with cake support:


    git clone https://github.com/dtaht/tc-adv
    cd tc-adv
    ./configure
    make
    sudo make install

    #Then:

    tc qdisc add dev whatever root cake # and whatever options

As with the kernel, odds are this is also available on your distro already.

Configuring CAKE
----------------

We had found that a ton of edge cases involving very low (sub 2.5mbit)
bandwidths, and PPPoe and ATM framing compensation were bothersome in
fq\_codel, so cake includes built-in modes for this.

There are numerous other traps for the unwary, documented in
[Best practices for benchmarking Codel and FQ Codel](Best_practices_for_benchmarking_Codel_and_FQ_Codel.md)
- we are trying to make those traps less dangerous in cake, for example,
we came up with a way to "peel" apart TSO/GSO/GRO offloads to deal with
packets rather than superpackets.

### Outbound configuration under linux

While we have published some mods to make cake easy to configure under
the existing sqm-scripts (cake eliminates many, many lines of code
there) and GUI, cake is also quite simple to configure manually from the
command line.

Configuration of outbound is easy, the simplest default setting is:

    tc qdisc add dev eth2 root cake bandwidth XXmbit # where XX is your mbit. You can do kbit also. substitute your outbound interface for eth2.

If you are interested in what pure AQM alone accomplishes, try the
"flowblind" option. If you do not want classification, specify
"besteffort". IF you want to run at line rate for your device, relying
instead on backpressure from the ethernet driver (and hopefully
<link>BQL</link>) don't specify the bandwidth.

### Inbound configuration under linux

Inbound is mildly more difficult because you have to setup an IFB
(intermediate functional block) device, and re-route inbound traffic to
it. A simple configuration (sqm-scripts example below) would be:

    ip link add name ifb4eth2 type ifb
    tc qdisc del dev eth2 ingress
    tc qdisc add dev eth2 handle ffff: ingress
    tc qdisc del dev ifb4eth2 root
    tc qdisc add dev ifb4eth2 root cake bandwidth 110000kbit besteffort
    ip link set ifb4eth2 up # if you don't bring the device up your connection will lock up on the next step.
    tc filter add dev eth2 parent ffff: matchall action mirred egress redirect dev ifb4eth2

We have generally found that most diffserv inbound priorities are wrong,
so we tend to specify besteffort here, and may add a "squash" option
directly to cake to remove the diffserv markings entirely.

Some example results while a rrul test was running:
---------------------------------------------------


    d at nuc-client:~/git/iproute2-cake$ ./tc/tc -s qdisc show dev eth0
    qdisc cake 8002: root refcnt 2 unlimited diffserv4 flows
     Sent 13895939355 bytes 9605458 pkt (dropped 194, overlimits 0 requeues 0)
     backlog 318798b 26p requeues 0
               Class 0     Class 1     Class 2     Class 3
      rate          0bit        0bit        0bit        0bit
      target       5.0ms       5.0ms       5.0ms       5.0ms
    interval     105.0ms     105.0ms     105.0ms     105.0ms
    Pk delay       6.0ms       5.0ms         1us       2.3ms
    Av delay       1.5ms       1.4ms         0us       654us
    Sp delay       317us       201us         0us       141us
      pkts        128068      316663          56      236467
    way inds           0           0           0           0
    way miss           3          40           3           7
    way cols           0           0           0           0
      bytes     45317244 11531124242        5524  2320607748
      drops          173          21           0           0
      marks            0           0           0           0

A problem I have is in reconciling the Flent plots which hit a
minimum of 2ms for sparse flows, where I typically see \~200us delay in
the qdiscs themselves. I have generally not cared at all about about
anything less than 3ms prior to now.


    qdisc cake 8003: root refcnt 2 bandwidth 920Mbit diffserv4 flows
     Sent 2298586363 bytes 1826648 pkt (dropped 45, overlimits 474931 requeues 0)
     backlog 468331b 25p requeues 0
               Class 0     Class 1     Class 2     Class 3
      rate       920Mbit  862500Kbit     690Mbit     230Mbit
      target       5.0ms       5.0ms       5.0ms       5.0ms
    interval     105.0ms     105.0ms     105.0ms     105.0ms
    Pk delay       4.6ms       3.2ms         0us       5.2ms
    Av delay       1.5ms       1.2ms         0us       1.6ms
    Sp delay       303us       290us         0us       191us
      pkts        110498      111953           0      181478
    way inds           0           0           0           0
    way miss           3          31           0           6
    way cols           0           0           0           0
      bytes    347279080  1377499174           0   574954712
      drops           14           0           0          31
      marks            0           0           0           0

Have I mentioned how much I hate offloads? see the backlog relative to
the number of "packets".

Installing CAKE on OpenWrt
--------------------------

CAKE is included in all recent versions of OpenWrt, and is quite simple to
install. Simple install the 'luci-app-sqm' package, and it will pull in all
needed dependencies (or just 'sqm-scripts' if you don't want the GUI). After
this you can edit the sqm config in `/etc/config/sqm`, or find the "SQM QoS"
menu point under "Network" in the Luci GUI.

### Attachments
{{< attachment name="cake-battlemesh-v8.pdf" type="application/pdf" description="Slides shown at Battlemesh v8" filename="150817135028_cake-battlemesh-v8.pdf" >}}

