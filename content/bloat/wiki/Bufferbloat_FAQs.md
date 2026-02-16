---
title: Bufferbloat FAQs
date: 2024-12-01T09:10:12
lastmod: 2026-02-16T09:10:12
type: wiki
toc: false
---
# Bufferbloat FAQs

We hear these questions all the time,
so we collect the answers here for reference.

Answers are grouped into
[solutions for bufferbloat](#tldr---solutions-for-bufferbloat),
then a [review](#about-bufferbloat)
of Bufferbloat and its causes,
then the [science behind the fixes](#the-science),
then ["objections"](#objections-we-hear),
and finally [actual questions from various forums](#real-world-questions).

---

## TL;DR - Solutions for Bufferbloat

### Question #1.1: Is there a fix for bufferbloat?

Yes. The science for solving bufferbloat is well understood.
Routers generally employ
[fq_codel](https://datatracker.ietf.org/doc/html/rfc8290) or
[CAKE](https://www.bufferbloat.net/projects/codel/wiki/Cake/)
algorithms for ISP connections and
[Tx Queue limits, AQL, and ATF](https://www.usenix.org/system/files/conference/atc17/atc17-hoiland-jorgensen.pdf)
algorithms to address bufferbloat in Wi-Fi.
The [cake-autorate](https://github.com/lynxthecat/cake-autorate)
algorithm handles links with varying rates, such as
4G/5G cell phones, cable modems, etc.

The OpenWrt Project - where all these algorithms were developed -
gives them the umbrella term "Smart Queue Management" (SQM).

### Question #1.2: Are there any commercial solutions I can just buy?

Yes. The
[What Can I Do About Bufferbloat?](https://www.bufferbloat.net/projects/bloat/wiki/What_can_I_do_about_Bufferbloat/)
page list several vendors who have figured out
how to include these algorithms into their products.

### Question #1.3: Are there other solutions?

There are a number of open-source projects
listed on the
[What Can I Do...](https://www.bufferbloat.net/projects/bloat/wiki/What_can_I_do_about_Bufferbloat/)
page above.
As noted above, the [OpenWrt Project](https://openwrt.org)
developed and tested all these algorithms
over the last decade.

### Question #1.4: Where can I read more?

Check out
[How OpenWrt Vanquishes Bufferbloat](https://forum.openwrt.org/t/how-openwrt-vanquishes-bufferbloat/189381)
for a list of the techniques a router can employ,
including ISP-bloat, WiFi-bloat, and bloat caused by variable speed links.

## About Bufferbloat...

### Question #2.1: What is Bufferbloat?

[Wikipedia says](https://en.wikipedia.org/wiki/Bufferbloat),
"Bufferbloat is the undesirable latency that comes from a
router or other network equipment buffering too many data packets."

### Question #2.2: What does _that_ mean? How could that happen?

If a router doesn't use a better algorithm,
it will happily place every newly-arriving packet at the end
of a single FIFO queue
waiting to be sent to your ISP.

If packets arrive at the router faster than they can
be transmitted to the ISP, a queue builds up.
From time to time, the queue might hold dozens
(or hundreds) of packets,
potentially causing multiple seconds of latency or lag.
Those buffered packets are "the bloat" in Bufferbloat.

### Question #2.3: Where can bufferbloat occur?

Bufferbloat can occur anywhere there's a _bottleneck_ -
a place where a fast link feeds into a slow link.
When many packets arrive at the bottleneck,
the router queues those packets.
One or two queued packets can be beneficial
so the slow link never starves.
But queueing more packets only adds latency (delay) to
the transit time of those packets.

### Question #2.4: Where does bufferbloat happen in the real world?

These large queues can build up in your router's
connection to the ISP
(because the outbound link tends to be slower
than the local LAN interfaces)
and also in Wifi interfaces (again, computers can create
packets faster than the wireless link can carry them).

### Question #2.5: How can I tell whether I'm experiencing bufferbloat?

There are a number of web-based tests that measure latency
_during_ the download and upload:

* [Speedtest.net](https://www.speedtest.net/)
* [Waveform Bufferbloat and Internet Speed Test](https://www.waveform.com/tools/bufferbloat)
* [Cloudflare Speed Test](https://speed.cloudflare.com/)

If the test shows an increase of latency under load
of less than 15-25 msec, then the latency is well under control.

To make more repeatable tests, consider
[Flent](https://flent.org/) or
[Crusader](https://github.com/Zoxc/crusader#crusader-network-tester).

### Question #2.6: You say there can be high latency in Wi-fi?

Yes. Wi-Fi drivers can often queue
hundreds of milliseconds of packets,
which adds additional delay to packet transit time
(round-trip time).

### Question #2.7: How can I measure Wi-Fi latency?

Check out the
[Crusader](https://github.com/Zoxc/crusader#crusader-network-tester)
application.
You'll need two computers: connect the first by Ethernet
to a LAN switch port on your router and start the Crusader Server;
run the Crusader Client from a second computer on Wi-Fi.

## The Science

### Question #3.1: How do those algorithms minimize latency?

A router can control latency using one
or more of the SQM algorithms.
In general, these algorithms use a variation of this technique:

1. Place the arriving packets of each traffic flow
   (each individual connection from each computer
   on the local network) into their own queue.
2. In a round-robin fashion, remove a
   small batch of packets from a queue
   and transmit those packets through the (slow) bottleneck link.
   When they have been fully sent,
   move to the next queue, remove and send a batch, and so on.
3. Offer back pressure to flows that are sending “more than their
   share” of data.

### Question #3.2: How does this lead to fair sharing of the bottleneck?

Each turn, the round-robin process doles out
a few packets from a queue,
generally 5-15 msec worth of traffic.
Low-traffic flows empty their queue "right away" -
in their next turn.
A single high-traffic flow gets to use the entire capacity
of the bottleneck, because no other queues have data to send.
When there are competing high-traffic flows,
the round-robin process cycles between all the queues that hold
packets, sending a "fair amount" from each in every turn.

### Question #3.3: These descriptions make it sound as if bufferbloat only happens on upload (from my local network toward my ISP). Does Bufferbloat ever happen on download?

Absolutely. There's also a bottleneck at your ISP.
Their high-speed lines feed traffic to the
(slower) link coming toward you.
That fast-to-slow transition within the ISP equipment
can also build up significant queues.

### Question #3.4: How do the bufferbloat algorithms work for the download direction?

The SQM algorithm creates a new "download interface" _within the router_
to act as the bottleneck.
As with the upload direction, this internal download interface
is configured to be slightly slower than the ISP link
(typically 5%-10% slower).
That lets the queue build up within the local router,
where the bufferbloat algorithm can control it.

### Question #3.5: How can latency be controlled in Wi-Fi?

WiFi bufferbloat can easily exceed hundreds of milliseconds. See the
[Ending the Anomaly](https://www.usenix.org/system/files/conference/atc17/atc17-hoiland-jorgensen.pdf) and
[Bufferbloat mitigation in the WiFi stack](https://www.netdevconf.org/2.2/session.html?jorgensen-wifistack-talk)
talks from 2017 that document this.

Fortunately, that paper also presents a solution involving
a) individual transmit queues for each station,
b) AirTime Fairness, and
c) Airtime Queue Lengths to drop latency by an order of magnitude.
These techniques are described in the papers cited above and
[How OpenWrt Vanquishes Bufferbloat](https://forum.openwrt.org/t/how-openwrt-vanquishes-bufferbloat/189381).

### Question #3.6: How can latency be controlled on variable-speed links?

My cable connection speed varies from daytime to evening.
And my 5G cell connection is even worse -
changing from minute to minute.
How can I choose a setting for the CAKE
download and upload speed parameters?

The [cake-autorate](https://github.com/lynxthecat/cake-autorate#cake-with-adaptive-bandwidth---cake-autorate)
algorithm continually monitors traffic and latency,
and adjusts the CAKE parameters up and down to give the
highest throughput while minimizing latency.

### Question #3.7: Won't all those queues "clog up" my router's memory?

No more than happens with a single FIFO queue.
(Those packets are already being buffered now.)
In fact, these algorithms can decrease memory use:
queues for low-traffic flows are almost always empty;
high-traffic flows - if they begin to build up a queue -
get back pressure either using
[ECN](https://www.bufferbloat.net/projects/ecn-sane/wiki/)
or by dropping packets.

### Question #3.8: Isn't dropping packets bad?

No. Packet loss is always required by the TCP protocol
to signal that there is congestion, or that the sender is
"sending too fast".
Anytime a TCP sender detects that signal,
they must decrease their rate of sending.

When a _router_ using SQM
notices that a significant queue is building for one of its flows,
it implies that the sender
is sending too fast for current conditions.
If the router didn't control it, the sender would attempt
to use more than its share of the limited bandwidth.
Consequently, the router occasionally drops a packet
from the head of that queue to signal the sender to slow down.

### Question #3.9: Can't I just tweak the QoS settings of my router?

Maybe. It's a fiddly process, and doesn't always work.
See
[What’s wrong with simply configuring QoS?](https://www.bufferbloat.net/projects/bloat/wiki/More_about_Bufferbloat/#why-not-simply configure-qos)
for more information.

### Question #3.10: How do I put a router "in front of" my ISP's router?

In a normal setting, your ISP's router is connected by
cable/phone/fiber to their equipment in their offices.
Your local devices connect either through
Ethernet or WiFi to the ISP router.

But if the ISP gear doesn't control Bufferbloat,
_you_ need to take control of your network.
A very common solution is to put a router with SQM "in front of"
the ISP gear, making it the primary router.
To do this:

1. Turn off WiFi in the ISP router
2. Connect the WAN/Internet port of the new router to one of the 
   LAN ports of the ISP router
3. Configure the new router's SQM or other latency control options
4. Connect _all_ your equipment to the new router.
   (Do not leave any equipment connected to the old device - it will
   throw off the anti-bufferbloat algorithms.)
5. As always, 
   [test the new connection](https://www.bufferbloat.net/projects/bloat/wiki/Tests_for_Bufferbloat/) to ensure that it's working.

## Objections We Hear

### Question #4.1: But, that's not "bufferbloat" - it's just ordinary behavior. Of course things will get slower when there’s more traffic...

It seems you're ignoring the
order of magnitude increase in latency.
That's far more than expected if the network were "just busy".

### Question #4.2: But I’m the only one using the internet...

It may be true that you're the only _human_ in the house.
But does your phone ever upload photos?
Does your computer fire off any automated process?
Does your Tesla (or your refrigerator) get updates?
Do you browse the web, or otherwise use the internet?
Any of those can generate traffic that,
in turn, induces latency.

### Question #4.3: It only happens some of the time...

Exactly - bufferbloat is transitory.
You probably notice it when someone's uploading photos,
or your computer is doing something in the background.

### Question #4.4: Those bufferbloat tests you hear about are bogus. They artificially add load, which isn’t a realistic test.

Yes, the tests do add load.
But what would you expect to happen to your network's performance
if you actually were uploading or downloading a file?

### Question #4.5: Bufferbloat only happens when the network is 100% loaded.

This is related to the previous answer.
When you open a web page or open an email attachment,
your computer - by design - briefly uses 100% of the link.
Is this enough to cause momentary lag?

### Question #4.6: It’s OK. I just tell my kids/spouse not to use the internet when I’m gaming.

Really?

### Question #4.7: But, I have gigabit service from my ISP

That helps, but if you’re reading this
because you're worried about a “slow network”
you still have to rule out bufferbloat.

### Question #4.8: I can’t believe that router manufacturers would ever allow such a thing to happen.

In the 2010 time period, no one understood this phenomenon.
In 2011, Jim Gettys reported on his work
with other network experts (see
[Dark Buffers in the Internet](https://mirrors.bufferbloat.net/Talks/BellLabs01192011/110126140926_BufferBloat12.pdf))
to show how surprising it was that routers would queue far more
data than they could send in a reasonable time.

In 2012, 
CoDel (for "controlled delay",
pronounced "coddle", because it treats network streams gently)
was invented in response the newly-named "bufferbloat".
In the decade since, the CoDel algorithm was enhanced to produce
the fq_codel, CAKE, and cake-autorate open-source algorithms
that have been proven to minimize latency.

Today, there's no excuse for router vendors not to
incorporate this technology.
But still, many have not done it.

### Question #4.9: I mean… wouldn’t router vendors want to provide the best for their customers?

Not necessarily – implementing any new code requires engineering effort.
They’re selling plenty of routers using their decade-old software.
The Boss asks, “Would we sell more routers if we make those changes?"
(Probably not, so the vendors don't change.)

But if everyone started writing reviews saying _Vendor X has bufferbloat
and games are unplayable, but Vendor Y doesn't..._
that might change the game.

### Question #4.10: Why would they sell me a router that gave crappy service? They’re a big company - they must know about this stuff.

Maybe. We have reached out to lots of vendors.
But remember they profit if you decide to upgrade to a higher capacity device/plan.

### Question #4.11: Besides, I just spent \$300 on a “gaming router”. It was the most expensive solution on the market...

Maybe that router's not as good as their advertising says...

### Question #4.12: I can't believe you’re telling me that a bunch of academics have come up with a better algorithm than commercial router developers - that company who sold me that \$300 router?

Well, the SQM algorithms seem to solve the problem
when they replace the vendor firmware…

### Question #4.13: And then you say that I should just install some “open source firmware”? What the heck is that? And why should I believe you?

Same answer as above.

### Question #4.14: What if it doesn’t solve the problem? Who will give me support? And how will I get back to a vendor-supported system?

This is a valid point - see
[What Can I Do About Bufferbloat?](https://www.bufferbloat.net/projects/bloat/wiki/What_can_I_do_about_Bufferbloat/)
for a list of commercial products.

## Real-world questions

### Question #5.1: Traffic Shaper Queue Limiters not helping with Bufferbloat

> ... Wondering if anyone could help me out with this configuration, again the whole purpose of this is to have the lowest latency as possible when gaming. I understand that the bufferbloat test is designed to see how the network handles high stress loads and when considering for online gaming (eg. COD MW3) I understand it doesn’t use anywhere near by max bandwidth. Even under lower loads I still get the same latency values.
> ([Original post on Reddit](https://www.reddit.com/r/PFSENSE/comments/1ecu16f/traffic_shaper_queue_limiters_not_helping_with/))

Despite the confident assurances from other posters that it isn't bufferbloat, it sounds as if you're seeing latency/lag when gaming. Here's what could be going on.

1. Bufferbloat is transitory. You can have very low ping times when the link is idle,
but if someone else starts using the network (reading the web,
watching a movie, uploading photos from their phone),
their bursts of traffic can momentarily load the network to 100%.
Could that be enough to make you miss your shot?

2. You're right - bufferbloat tests "artificially load the network".
They do this to see how your network performs during those moments of 100% load.

3. You didn't say, but at ISP speeds above 300-500mbps,
  the bufferbloat in the Wi-Fi system can become important.
  This is a solved problem (see
  [Ending the Anomaly](https://arxiv.org/pdf/1703.00064)),
  but not universally deployed in routers.

> Bufferbloat is not your problem on a gig symmetrical link unless you are smashing the upload.

This is _exactly_ the definition of bufferbloat.
If sending a lot of traffic causes your latency to increase significantly,
something is wrong, likely bufferbloat.

### Question #5.2: Extreme Bufferbloat on fibre connection

> ... I'm playing competitive games and it feels like im desynced to the server 70 % of my matches. First image is with no QOS in the router, the second one is when im limiting my bandwith to 85 % up and down. With QOS its ok, but i just dont understand why jitter and latency is that high without QOS on a fibre connection.
> ([Original post on Reddit](https://www.reddit.com/r/HomeNetworking/comments/1eclgmh/extreme_bufferbloat_on_fibre_connection/))

Garden variety commercial routers (even "gaming routers") frequently don't have guard rails to prevent them from queueing too much data. All the traffic goes "into the queue" (technically, they use a FIFO). A burst of bulk packets (photos from your phone, reading a web page, etc.) delay smaller packets such as gaming updates, voice and videoconference traffic.

QoS helps (as you've seen), but it [won't entirely solve the problem.](https://www.bufferbloat.net/projects/bloat/wiki/More_about_Bufferbloat/#why-does-sqm-work-so-well)

However, this is a solved problem if you have a good router. See [What can I do about Bufferbloat?](https://www.bufferbloat.net/projects/bloat/wiki/What_can_I_do_about_Bufferbloat/) for more details

### Question #5.3: Bufferbloat on Wifi

>> Given the focus of latency in the Wi-Fi 6 and Wi-Fi 7 standards, has anyone tested the bufferbloat behavior of these AP? I'm particularly interested in U6+.
>
> ... The amount of packet buffer they will have on board will be trivial.
> ([Original post on Reddit](https://www.reddit.com/r/Ubiquiti/comments/1euwu0c/bufferbloat_on_u6_and_u7_aps/))

And yet, WiFi bufferbloat can easily exceed hundreds of milliseconds. See the
[Ending the Anomaly](https://www.usenix.org/system/files/conference/atc17/atc17-hoiland-jorgensen.pdf) and
[Bufferbloat mitigation in the WiFi stack](https://www.netdevconf.org/2.2/session.html?jorgensen-wifistack-talk)
talks from 2017 that document this.

Fortunately, that paper also presents a solution involving
a) individual transmit queues for each station,
b) AirTime Fairness, and
c) Airtime Queue Lengths to drop latency by an order of magnitude.
These techniques are described in the papers cited above and
[How OpenWrt Vanquishes Bufferbloat](https://forum.openwrt.org/t/how-openwrt-vanquishes-bufferbloat/189381).

> ... An easy way to test that would be to use
> [Crusader](https://github.com/Zoxc/crusader).

The [Crusader](https://github.com/Zoxc/crusader) network tester
is terrific.
See the question above about using it to test Wifi latency.

### Question #5.4: An Edgerouter solves latency, but seems not to handle the speed...

> ... Whenever my Tesla started updating, my ping went to crap...
> Finally, I threw my hands up in the air,
> configured an edgerouter I had here and enabled smart queue.
> Instantly I was getting A+ scores,
> with +0ms on both incoming and outcoming.
>
> Do I need new hardware? If so what is recommended?
> Should I just give up and use the edge router.
> [(Original post on Reddit)](https://www.reddit.com/r/opnsense/comments/1h6rh3u/fixing_buffer_bloat_what_is_going_on_new_update/)

A couple thoughts. My mentor once said,
"If you can't tell the difference, it doesn't make a difference".
How does that apply to the situation you describe?

1. If you're happy with the way your network performs,
   you can declare victory.
   If the Edgerouter gives near zero additional latency,
   it seems like a win.

2. You didn't mention the rated speed for your ISP,
   but do you ever notice that it's "not fast enough"
   when using the Edgerouter?

3. If not, see the next question for more information...

### Question #5.5: Consider a lower tier plan from your ISP

> ... I'd like a plug and play QoS router with a 5gb/s WAN port and at least 1 5gb/s LAN port (future proofing) ... ([Original post on Reddit](https://www.reddit.com/r/HomeNetworking/comments/1h9n7zl/comment/m179gh7/))

A 5Gbps-capable router is going to cost serious money.
(I don't know your budget, but it'll be a lot.)

Your ISP has probably been offering a higher speed plan,
especially if you say "it's not fast enough".
But if your router is adding latency,
then everything will feel slow, regardless
of the "speed" of the link.

Surprisingly, the "speed to deliver" normal data
doesn't increase by much for a faster link.
See the charts in
[The Latency Effect](https://www.afasterweb.com/2015/05/17/the-latency-effect/)
that show that increasing ISP speed doesn't
make web pages load much faster.
_Decreasing_ latency always made pages load faster.

So 250mbps or 300mbps could be plenty unless you want bragging rights.

Here is a bit of contrarian advice.
If you don't actually need such high-speed service,
consider these options:

* Get a lower tier plan from your ISP
* Get a router with the SQM algorithms
  for minimizing latency/bufferbloat. See
  [What can I do about Bufferbloat?](https://www.bufferbloat.net/projects/bloat/wiki/What_can_I_do_about_Bufferbloat/)
  for a list of suitable routers
* You'll see the latency drop without much
  difference in your perceived speed
* ... and save a bunch of money per month on your ISP bill

### Question #5.6: I don't need SQM...

> @WWicketW writes:
> 
>  I'm on Flint2 also ...
>
> With SQM mine max speed was 1,2 ÷ 1,3 Gbps in download (and A+ on waveform), with HO+PS (Hardware offloading and Packet steer on all CPU) I've reach 2,2Gbps on download and A on waveform.
>
> I definitely can survive without SQM 😅
> [(Original post on Reddit)](https://www.reddit.com/r/openwrt/comments/1hts21t/comment/m5p3q6q/)

That sounds like a terrific solution.
No one asserts you _need_ SQM.
It's only useful if lag/latency is affecting you.
(In other words, "If you're happy, I'm happy.")

It's also valuable to know that Flint 2
(less than US$150 with coupon on Amazon)
can feed a 2Gbps+ link and keep up with the rated speed. Congratulations!

### Question #5.7: My ISP's router gives terrible bufferbloat...

> I have been struggling with an incredible sluggish and inconsistent video game experience on my computer. I have payed for a pc, I've paid to have it tweaked professionally, I've bought the best peripherals. I have done everything to fix this issue and none of it has worked, this has been going on for months... [(Original post on Reddit)](https://www.reddit.com/r/HomeNetworking/comments/1id9mm5/bufferbloat_needs_fixing_please_help)

You are going to need to take control of your network. See
[What Can I Do About Bufferbloat?](https://www.bufferbloat.net/projects/bloat/wiki/What_can_I_do_about_Bufferbloat/)
for more information.

TL;DR - you'll probably need to put another, smarter, router
in front of their router that can control the queueing/latency.
Consider the OpenWrt One - it's reasonably priced,
can handle your data rate, and it's the platform where
all these SQM algorithms were developed.
