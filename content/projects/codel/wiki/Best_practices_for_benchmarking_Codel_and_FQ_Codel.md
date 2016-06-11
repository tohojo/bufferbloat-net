
---
title: Best practices for benchmarking Codel and FQ Codel
date: 2012-12-11T05:35:13
lastmod: 2015-05-26T16:19:09
type: wiki
---
Best Practices for Benchmarking CoDel and FQ CoDel (and almost any other network subsystem!)
============================================================================================

Document version: 1.5, May 26, 2014.

The bufferbloat project has had trouble getting consistent repeatable
results from other experimenters, due to a variety of factors. This page
attempts to identify the most common omissions and mistakes. There be
land mines here. Your data will be garbage if you don't avoid them!

Hardware/Software Traps for the Unwary
--------------------------------------

Network hardware (even in cheap hardware!) has grown "smart", with
offload engines of various sorts. Modern network hardware has often
sprouted various "offload" engines, unfortunately now often enabled by
default, which tend to do more damage than good except for extreme
benchmarking fanatics, often primarily on big server machines in data
centers. If you are trying to emulate a router's behavior, turning off
offloads like TSO/GSO/GRO/LFO is a good start. In the case of a host,
there have been mods to TCP's behavior to make it less bursty and to
more sanely use these offloads post Linux 3.13 with the sch\_fq and
pacing options added to it.

### Enabling Byte Queue Limits

Transmit and receive rings are now ubiquitous, to get the CPU's out of
the business of handling interrupts on a per packet basis when running
at high bandwidths with small packets. There is a potential dynamic
range of a "packet" of 64 bytes to 64k bytes in modern systems with TSO
enabled. This is often a large source of bufferbloat, as the drivers
have managed the rings in the most primitive possible way.
[BQL](https://lwn.net/Articles/454390/) (byte queue limits) is **the
first step** in putting sanity back into Ethernet driver transmit ring
management.

There are now over 24 BQL enabled Ethernet drivers in Linux 4.1, many of
which apply to many card models, and most are well tested. They are:

    As of the last kernel we looked at, support for BQL was in the following multi-queued (and mostly 10GigE) drivers:

    find drivers/net/ -name '*.c' -exec fgrep -l \
    netdev_tx_completed_queue {} \;

    drivers/net/ethernet/broadcom/bnx2.c
    drivers/net/ethernet/broadcom/bnx2x/bnx2x_cmn.c
    drivers/net/ethernet/broadcom/tg3.c
    drivers/net/ethernet/intel/igb/igb_main.c
    drivers/net/ethernet/intel/i40e/i40e_txrx.c
    drivers/net/ethernet/intel/ixgbe/ixgbe_main.c
    drivers/net/ethernet/intel/fm10k/fm10k_main.c
    drivers/net/ethernet/intel/i40evf/i40e_txrx.c
    drivers/net/ethernet/mellanox/mlx4/en_tx.c
    drivers/net/ethernet/sfc/tx.c
    drivers/net/ethernet/freescale/gianfar.c
    drivers/net/ethernet/amd/xgbe/xgbe-drv.c


    And in the following (most GigE and lower) drivers:

    find drivers/net/ -name '*.c' -print | \
    xargs fgrep -l netdev_completed_queue

    drivers/net/ethernet/nvidia/forcedeth.c
    drivers/net/ethernet/atheros/alx/main.c
    drivers/net/ethernet/broadcom/b44.c
    drivers/net/ethernet/broadcom/bgmac.c
    drivers/net/ethernet/intel/e1000/e1000_main.c
    drivers/net/ethernet/intel/e1000e/netdev.c
    drivers/net/ethernet/realtek/8139cp.c
    drivers/net/ethernet/via/via-rhine.c
    drivers/net/ethernet/stmicro/stmmac/stmmac_main.c
    drivers/net/ethernet/marvell/sky2.c
    drivers/net/ethernet/marvell/skge.c
    drivers/net/ethernet/hisilicon/hip04_eth.c
    drivers/net/ethernet/hisilicon/hix5hd2_gmac.c

If your driver is NOT BQL enabled, you will need to use HTB to emulate
rates correctly. (or, better! take the time to add the 4-8 lines of code
needed for BQL for your devices's driver)

Beware that other network interfaces have often sprouted similar "smart"
hardware (e.g. some DSL hardware, all USB to Ethernet devices); no help
for them is yet available. Worse than that, software offloads emulating
TSO (GSO) have now appeared, saving a little bit on interrupt processing
at higher bandwidths, and bloating up packets at all bandwidths,
including lower ones. We would really like to see GRO and GSO be
disabled entirely at 100Mbit and below. Let packets be PACKETS!

The GRO problem is so common now (and so needed in now-shipping devices)
that in [Cake]({{< relref "projects/codel/wiki/Cake.md" >}}) we added offload "peeling" to turn
superpackets back into packets.

Consequently, you **must** understand the device drivers you are using
before benchmarking.

### Ethernet BQL (Byte Queue Limits) Driver Enablement

BQL rate limits packet service to the device in terms of bytes on
Ethernet. BQL was initially developed and tuned at 1 and 10Gbps. Its
estimator is often wrong at speeds below 100Mbit, usually double or more
what is needed (and see the last note here about how this further
damages CoDel behavior. 100Mbit and below 3K suffices. 10Mbit and below
1514 is as low as you can go and it should be even lower.

Common experimental errors: Leaving BQL at autotuning, setting it to too
high a value for the bandwidth available, etc.

We would like BQL to autotune better, but as of Linux 4.1, it does not.
Perhaps BQL can be fixed to have a lower limit and just periodically
exceed it for larger packets.

We are looking into other algorithms than BQL for other network types,
which have often sprouted similarly "smart" hardware to Ethernet, e.g.
ADSL/VDSL, which must cover a bandwidth range of 250Kbps to 100Mbps.

### Coping with offloads

Littered through this document presently are the evils of offloads, and
a future re-org of this document will call them out in a dedicated
section. This "problem" (it is also a needed optimization to run at gigE
speeds on much modern hardware) has become so prevalent in both testing
and the real world that a fix for codel's maxpacket calculation arrived
in linux 4.1, and compensatory mechanisms are also now in TBF and
[Cake]({{< relref "projects/codel/wiki/Cake.md" >}}).

### Dealing with NAPI

The linux NAPI subsystem defers receive interrupt processing for
(usually) up to 64 packets. This is quite a lot at 100Mbit and it does
not autotune. Even drivers targeted at 100Mbit devices tend to
copy/paste the typical default of 64 (where 16 would be more sane) for
the NAPI default.

### Dealing with sleep states

Aggressive sleep state behavior in intel nics was a problem - we saw
jitter and oddities in the 2-3ms range in one recent Linux kernel,
solved by disabling power save in the BIOS.

### Hardware Rate Limiting

Adjusting the ethernet card to a different line rate is useful, but
several other variables inside the stack must be adjusted. Those are
turning off all network offloads on ALL cards, and setting BQL to an
appropriate rate for the set bandwidth.

The
[debloat.sh](https://github.com/dtaht/deBloat/blob/master/src/debloat.sh)
and [debloat](https://github.com/dtaht/deBloat/blob/master/src/debloat)
scripts try their best to eliminate those variables, but do not always
succeed.

We have found that 3000 is a reasonable setting for BQL on a 100Mbit
system and 1514 is reasonable for 10Mbit, *if configured with a low
latency kernel*. We note that unlike experimenters leveraging what
hardware and kernels they have lying around, a router maker should make
these choices by default...

On some devices, you can also reduce the ethernet tx ring down to 2, at
10Mbit, with no ill effects, however you should measure this
optimization's affect on throughput.

Note that most home routers have an internal switch that runs at a fixed
rate. Turning down CeroWrt's rate on it's internal ethernet device
**doesn't work** and for tests that try to use hardware rate limiting
there, you are driving buffering into the switch, not the (ne)fq\_codel
algorithms, and most drops happen **in the switch**, thus invalidating
your test.

Leave the switch out of your testbeds. If you must have one, measure its
behaviour thoroughly, while under saturating load from two ports going
into one. You may be surprised by how much buffering has crept into
switches - one GigE switch we've seen has 50ms of buffering (at gigE!).
What is more, your switch, which might or might not be properly buffered
at 1Gbps, will likely have ten times too much buffering if used at
100Mbps, and 100 times too much buffering when used at 10Mbps.

### Hardware Flow Control

Many devices (notably DSL modems and some Homeplug devices) will exert
ethernet hardware flow control frames, which are sometimes recognized
and sometimes not, recognized by the NIC. When a latency sensitive AQM
is in play, this can work marvellously well. When a fixed lenth fifo is,
well... see what happens on [homeplug
networks](http://caia.swin.edu.au/reports/130417A/CAIA-TR-130417A.pdf) -
and [powerline with pause
frames](http://caia.swin.edu.au/reports/130121A/CAIA-TR-130121A.pdf)

Some NICs will attempt to exert hardware flow control when the rx buffer
overflows. This could also be a goodness, except that rx rings are
generally quite large in the first place - and we have seen many devices
running out of cpu to handle the workload actually just losing packets
at the rx ring rather than the qdisc.

### Software Rate Limiting

Use of HTB to rate limit connections to a given speed is to be
preferred, as HTB buffers up one, and only one packet. Note that HTB is
timer based; default Linux kernels are often compiled with HZ=250 (or
even lower), causing burstyness and non-uniform delivery of packets;
building your kernels at HZ=1000 will reduce this effect. Very important
also is that your kernel have support for hi resolution timers (hpet or
better).

Still, use of other hardware in your setup can bit you - debloat all
devices thoroughly (as per the debloat scripts) in a routing - or
routing emulating - setup.

Common experimental error:

    ethtool -s eth0 advertise 0x002 # set one interface to 10Mbit

This would allow for [GRO](https://lwn.net/Articles/358910/) to happen
on another interface. (and TSO, GSO, GRO, UFO, LRO) offloads to happen
on all interfaces, bloating up packet sizes). *Turn all offloads off on
**all** interfaces always* - unless you are using the new
[Cake]({{< relref "projects/codel/wiki/Cake.md" >}}) or revised TBF.

We use multiple variants of HTB and HFSC shaper scripts from Dave Täht
and Dan Siemon and others. Configuring HTB can be tricky, and simple
errors will result (usually) in you directing a shaper bin into a
pfifo\_fifo fast queue rather than where you wanted it.

[sqm-scripts](https://github.com/dtaht/ceropackages-3.10/blob/master/net/sqm-scripts/files/usr/lib/sqm/)
might be a good starting place to for hacking. Please see also
[wondershaper must die]({{< relref "projects/cerowrt/wiki/Wondershaper_Must_Die.md" >}}) for some insight on how **not** to do
the hacking.

### Know Your Bottlenecks!

Switches have buffering; sometimes excessive (particularly on improperly
configured enterprise switches). And Ethernet flow control may move the
bottleneck in your path to somewhere you didn't expect, or cause the
available bandwidth to be very different than you expect (particularly
in switched networks that mix different Ethernet speeds). Most Linux
Ethernet drivers honor flow control by default. Cheap consumer Ethernet
switches typically generate pause frames; enterprise switches typically
do not. There is no substitute for packet capture, mtr, and wireshark!

It's not just ethernet that has had issues. Try homeplugs... and of
course DSL, wifi, and other technologies also have bad buffering
strategies that we have not beaten yet, in most cases.

Kernel Versions and Configuration is Important
----------------------------------------------

We try to provide a modern, precompiled kernel (usually with several
advanced versions of codel and fq\_codel derived schedulers) on our
website, along with patches and the config used to build it.

There are two differences from this kernel's config than a normal
"desktop" or "server" configuration. It is configured for low latency
and a high clock interrupt rate. Faster interrupt response makes smaller
buffers feasible on a conventional x86 machine.

### The NetEm qdisc *does not work in conjunction with other qdiscs.*

The Linux network emulator qdisc, "netem", in its current incarnation,
although useful for inserting delay and packet loss, **cannot** be
effectively used in combination with other queueing disciplines. If you
intend to insert delays or other forms of netem based packet
manipulation, an entirely separate machine is required. *A combination
of netem + any complex qdisc (such as htb + fq\_codel or RED, or qfq)
WILL misbehave.* Don't do it; your data is immediately suspect if you
do.

Note: netem has been improving of late... and some are using mininet and
other tools.

Example of a flawed use: a netem queue has a default 1000 packet limit -
if it is too small (say, you insert a 200ms delay on a gig link), it
will drop packets when in excess of the queue limit. If your packet
limit is too big and netem is the actual bottleneck link, it will accrue
all the packets there, not in the qdisc supposedly managing the link.

### Tuning txqueuelen on pfifo\_fast

The default txqueuelen was set to 1000 in Linux, in 2006. This is
arguably wrong, even for gigE. Most network simulations at 100Mbit and
below use 100, or even 50 as their default. Setting it below 50 is
generally wrong, too, at any speed, except on wireless.

There is no right size for buffering!

There is a bfifo queue type in linux that is worth playing with to more
closely emulate dsl and cablemodem behavior.

Tuning These Algorithms
-----------------------

Having a sane, parameter less algorithm is very important to us. The
world (and current Linux implementation), however, is not yet
co-operating as well as we (or the algorithms) would like.

### Tuning CoDel for Circumstances it Wasn't Designed for

CoDel is designed to attempt to be "no knobs" at the edge of the
Internet (where most people are). At high speeds (10GigE), using a
larger packet limit than 1000 is recommended. Also at those speeds, in a
data center (not the open internet) the target and interval are often
reduced to 500us and 20ms respectively by those attempting to use CoDel
in those environments. At really low speeds (below 2.5mbit), we've found
an interaction with htb means you need to increase the codel target to
above a single MTU's transmit speed (13ms at 1Mbit).

To date, no one has invented a truly "no knobs" algorithm that works in
all environments in the Internet.

Secondly, codel is a "drop strategy", and is meant to be used in
conjunction with another qdisc, such as DRR, QFQ, or (as we use it),
several variants of (n,e)fq\_codel. While available as a standalone
qdisc this is intended primarily to be able to test variants of the
algorithm. There is a patch for most of the current ns2 model available.

### Tuning fq\_codel

By default fq\_codel is tuned to run well, and with no parameters, at
10GigE speeds.

However, today's Linux implementation of CoDel is imperfect: there are
typically (at least) one or more packets of buffering **under** the
Linux qdisc, in the device driver (or one packet in htb) even if BQL is
available. This means that the "head drop" of CoDel's design is not
actually a true head drop, but several packets back in in the actual
queue (since there is no packet loss at the device driver interface),
and that CoDel's square root computation is not exactly correct. These
effects are vanishingly small at 1Gbps or higher, but when used at low
speeds, even one packet of buffering is very significant; today's
fq\_codel and codel qdiscs do not try to compensate for what can be
significant sojourn time of these packets at low bandwidth. So you might
have to "tune" the qdiscs in ways (e.g. the target) that in principle
the CoDel algorithm should not require when used at low bandwidths. We
hope to get this all straightened out someday soon, but knowing exactly
how much buffering is under a qdisc is currently difficult and it isn't
clear when this will happen.

When running it at 1GigE and lower, today it helps to change a few
parameters given limitations in today's Linux implementation and
underlying device drivers.

The default packet limit of 10000 packets is crazy in any other
scenario. It is sane to reduce this to a 1000, or less, on anything
running at gigE or below. The over-large packet limit leads to bad
results during slow start on some benchmarks. Note that, unlike
txqueuelen, CoDel derived algorithms can and DO take advantage of larger
queues, so reducing it to, say, 100, impacts new flow start, and a
variety of other things.

We tend to use ranges of 800-1200 in our testing, and at 10Mbit,
currently 600.

We have generally settled on a quantum of 300 for usage below 100mbit as
this is a good compromise between SFQ and pure DRR behavior that gives
smaller packets a boost over larger ones.

#### ECN Issues

ECN is enabled by default. ECN is useful in the data center but far less
so today on the open internet. Current best practice is to turn off ECN
on uplinks running at less than 4Mbit (if you want good VOIP
performance; a single packet at 1Mbps takes 13ms, and packet drops get
you this latency back).

ECN *IS* useful on downlinks on a home router, where the terminating hop
is only one or two hops away, and connected to a system that handles ECN
correctly (all current OS's are believed to implement ECN correctly, but
this assumption bears a need for greater testing!).

#### Broadband Links

Fq\_codel runs extremely well on asymmetric links such as your commonly
available 24.5/5.5 service from a cable modem provider like Comcast. (in
conjunction with setting a shaper to your providers's rates and [htb
rate
limiting](https://github.com/dtaht/ceropackages-3.3/blob/master/net/debloat/files/simple_qos.sh))

We have tons and tons of [published benchmarks on cable
modems](http://burntchrome.blogspot.com/2014_05_01_archive.html) at this
point, as well as benchmarks against DSL, and other technologies.

We are finding that [low end hardware has trouble doing inbound rate
limiting at speeds above
50Mbit](http://burntchrome.blogspot.com/2014_08_01_archive.html)

#### nfq\_codel and efq\_codel

We now have a new versions of fq\_codel [under
test](http://snapon.lab.bufferbloat.net/~cero1/deb/patches-3.6.2/) .
nfq\_codel is an implementation the experimental ns2 model of codel +
what is standard fq\_codel, and efq\_codel is nfq\_codel that takes much
better advantage of the quantum size and interleaves small packets
better at low bandwidths...

However, it helps to reduce the quantum slightly on efq\_codel to
improve downlink performance while not compromising upload performance.
It appears that a ratio of 3x1 (500) is reasonable for most traffic in a
6x1 scenario. A quantum of 300 isn't bad either, and works for many
kinds of interactive traffic.

Life gets dicy in 12x1 as quantums below 256 disable a few key things
efq\_codel does to get good (for example) VOIP performance. Stay at 300
or above.

Anyway, a commonly used configuration line is this:

    tc qdisc add dev your_device root efq_codel quantum 300 limit 1000 noecn

NOTE: An earlier version of this page identified nfq\_codel as having
the quantum optimization. Also note that "sfq\_codel" in the ns2
distribution is packet oriented, the variants of (e,n)fq\_codel have
various degrees of byte orientation.

Research continues. Also fq\_codel in Linux 3.5 did not do fate sharing,
and Linux 3.6 fq\_codel reduces cwnd without packet drop on buffer
overload on a tcp stream enqueue.

### When not in control of the bottleneck link:

*Lastly, just running fq\_codel by itself, does not help you very much
when the next device in line is overbuffered (as in a home router next
to today's cable modems).* (it DOES help break up microbursts, however,
and generally "does no harm") In that case, using HTB to rate limit your
router to below the next gateway device and then applying fq\_codel will
work. See the note above about limitations to HTB.

Fq\_codel needs a bit of tuning below 4Mbit and on ADSL links. Basically
accounting for a single MTU's speed in the target parameter suffices in
the former case, and correctly doing linklayer ATM cell framing in the
second case, is what you need.

Work on Making codel and fq\_codel Implementations Better Continues
-------------------------------------------------------------------

The time in packets spend in device drivers is not taken into account in
CoDel's control law computation, resulting in the need for tuning with
CoDel target, particularly at low speeds where even one packet is highly
significant latency. This is a current implementation limitation as we
have no way to find out how much time is being spent in a device driver;
and several other possible bugs lurk. Let us know what you discover.

Improving BQL and other algorithms for driver ring buffer control is
needed. Ideally, being able to run delay based AQM algorithms across
coupled queues such as OS queuing system & drivers as a unified queue
would be best, but today's driver interfaces (and possibly hardware)
make this difficult (or impossible).

NS2 Simulation Traps with TCP
-----------------------------

ns2 does not support ECN, or cubic (correctly), or [proportional rate
reduction](http://research.google.com/pubs/pub37486.html) . For that
matter it doesn't support TCP compound, or any of numerous tweaks to TCP
that exist in the field such as TCP timestamps, syn cookies or TFO.
There is a built in assumption in most simulations that there is no tx
ring, or mac layer buffering at the hardware layer (interfaces to DOCSIS
or ATM), or software rate limiting enforced at the ISP. Also there is
rarely accounting for ATM overhead. ns2 doesn't even support port
numbers, making accurately benchmarking the various "fq" algorithms
difficult and dicey to do right.

Most home links use asymmetric rate limiting (e.g. 20Mbit down, 4Mbit
up) , and most simulations assume bidirectional symmetry. Simulations of
10Mbit links are still too high for the vast majority of the real world
consumer links, and yet too low for many modern links. Higher bandwidths
**need** tcp timestamps, in particular, to work well...

ns3 has similar problems, but recent efforts have added support for tcp
timestamps, port numbers, cubic, and validated versions of codel and
fq\_codel which should appear\
in the mainline ns3 code by december, 2014.

It would be useful if more sims came much closer to modeling the real
world.
