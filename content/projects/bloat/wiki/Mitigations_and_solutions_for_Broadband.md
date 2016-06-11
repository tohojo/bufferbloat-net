
---
title: Mitigations and solutions for Broadband
date: 2011-02-02T17:46:00
lastmod: 2011-02-02T17:46:00
type: wiki
---
Mitigations and solutions for Broadband
=======================================

Mitigations versus Solutions of Bufferbloat in Broadband\
By gettys\
I have distinguished in my writing between what I call “mitigations” and
“solutions”.

\* mitigations are actions we can take, often immediately, which make
the situation better, and improve (possibly greatly) the current grim
situation. Since they may only work some of the time, and may require
conscious thought tuning and action by network operators and users, or
have other limitations that are often far from optimal, they won’t work
in some circumstances or necessarily be implemented everywhere. Often
these mitigations will come at some cost, as in the case today’s posting
below.\
\* solutions are full solutions for a problem that get behavior to
something approximating optimal. Sometimes they may be mitigations that
can be widely applied in an ISP, even though though they may require
thought there. The “just work” for everyone.

But observed facts (e.g. RED or other AQM is far from universally used;
more about this in a future post) shows that anything that does not
“just work” is often distrusted and under-used (and seldom enabled by
default), so such a solution is seldom the optimal solution we should be
looking for: really “solving” the problem once and for all. As good
engineers and scientists, we should always be striving for “just works”
quality solutions, which we don’t have for bufferbloat in all its forms.

The full “solution” for the entire Internet is going to be hard; we need
to solve too many different problems (as you will see) at too many
points in all paths your data may traverse, to wave a wand eliminate
bufferbloat overnight. Some of the point solutions will actually require
replacement of hardware, and time to research and engineer such hardware
along with economics will often take time. Does that mean we should do
nothing? Of course not: we can immediately make the situation much
better than it is, particularly for consumer home Internet service. And
remember, your competitor will eventually beat you if you sit on your
hands.

Gamers and others have been mitigating bufferbloat in broadband for
years. Read on. You’ll suffer much less. Mitigation of home router
bufferbloat itself will be tomorrow’s installment.\
Mitigating Broadband Bufferbloat in the Home Router

The best solution will be to remove the grossly bloated buffers
properly, and not to have to hack around this problem in our home
router. ISP’s and their vendors may be able to mitigate existing
equipment partially (by cutting buffers to something closer to sane
points in the CPE); these mitigations will take time, and are not
something you can go do today, yourself. Those are also technology
dependent; and what can be done there is probably best taken up by the
equipment vendors and standards bodies. As in many mitigations, they may
come with costs. In the downstream direction, ISP’s not running RED on
their head ends may turn it on. So when your network changes, you will
need to repeat this process.

I remind you that bufferbloat can occur elsewhere in your path as you
make these tests: some ISP’s and content providers do not run with any
queue management enabled, so you may have bottlenecks beyond your
broadband connection in your path beyond the last mile broadband
connection to help confound you (your wireless hop to your home network,
and anywhere beyond your broadband headend. My observations of Comcast’s
network beyond the CMTS has been very, very clean, confirming what I was
told to expect when I had lunch with Comcast. You may not be so lucky
with your ISP. That my test site is on a well run network at MIT,
peering directly with Comcast has certainly made my life easier. More on
the core Internet topic in the future.

Our quest here is to try to overcome what has already happened: we
usually have gross bufferbloat in the broadband provider’s equipment,
which may or may not be customer replaceable. If it is customer
replaceable (e.g. cable modems) we can hope that in a year or three that
the market may start to provide routers and broadband gear that
implement some rational queue management and behave better.

Here’s what you can do today, if your router supports it. If not, you
can go buy a new home router (or install open source router software)
today that can mitigate the problem for little cost (\$100 or less).
You’ll see why this is a mitigation at best, rather than a solution: it
isn’t something you’re going to ask your aged parents to try.

Many mid-range or high end home routers have traffic shaping features.
They may be called traffic shaping, or “QOS” (Quality of Service). Some
routers I’ve seen (I’ve seen quite a few over the last years) have a
single knob to set bandwidth on both directions; they aren’t
particularly useful. You want one which lets you adjust bandwidth in
both directions. I’ve experimented with several routers: your mileage
will vary. Some commercial routers work really well, some less so.
Sometimes these routers are marketed as ”gamer routers.” There is
probably some gamer’s web site someplace that goes into this in gory
detail, with reviews of different routers. If so, please let me know.
Facilities also exist in the open source router projects of various
sorts, e.g. OpenWRT, DDWRT, Tomato, and Gargoyle. More on this topic
below.

The WISEciti research project is also researching the behavior of home
routers: if you have an old router, they may be interested in giving it
a home.

Our goal is to keep buffers in your upstream broadband link from filling
and turn them back into “dark buffers”. We can try to avoid bufferbloat
in the broadband device this by transmitting data to it slightly less
fast than the broadband device will accept, and ensuring the router
forwards data slightly less fast than the broadband device will transmit
it. Formally, this is called “traffic shaping”. Gamers have been doing
this for years, as they are very latency sensitive and empirically
discovered that limiting your bandwidth in this way will have good
effects on observed latency. Note you should do traffic shaping before
you worry about classifying data (e.g. ensuring your voip gets priority
over TCP flows), as the goal here is to mitigate the upstream broadband
device’s faults as much as possible.

Some ISP’s provide a home router as part of their service that their
wires plug into directly. I have no idea if these routers are usable for
the following process. I presume not in the discussion below. In either
case, you need the ability to perform traffic shaping.

Plug your router into the ethernet on broadband gear, or at worst, into
the ethernet jack of your home router if that is included in your
broadband service. We’re trying to mitigate the broadband link problem
here, not fix the router’s bufferbloat, which is a later topic.

I recommend monitoring your home connection via smokeping while you try
this process. It isn’t clear to me that the bandwidth you get from a
broadband carrier is a constant over time, as load occurs. I haven’t
explored carefully what happens when my ISP’s network gets busy.

Start “pinging” some nearby site (best is not an ISP router, if only
because they may be loaded at times and process ping on the slow path).
Note the latency. Saturate the link in an upstream direction (e.g. by
copying a file someplace, or uploading a video somewhere; you will
probably be able to figure out some way to do so. Note it’s behavior:
you’ll very likely find that the latency grows to some value of hundreds
of milliseconds or even seconds. You’ll see the latency climb gradually,
and then start varying (that’s the behavior you see in my TCP traces).

By using traceroute and ping on the path traceroute exposes, you can
figure out which hop is the bottleneck. If it is not the broadband hop,
then you need to find some other site to work against.

Next, find out what your provisioned bandwidth is for both directions,
nominally. This is what you pay for.

Enter half these values into your home router in the the bandwidth
shaping or QOS form, as per your router, having enabled this feature.
You may or may not have to reboot your router whenever you adjust the
values. Some routers attempt to determine the available bandwidth in
some fashion automatically; I have no idea how successful they may be,
and expect that features like Comcast’s PowerBoost will confuse them, so
manual use is recommended unless you find the router “does the right
thing” automatically . I also expect that some routers work better than
others in this area.

Again load your link.

Your latency should be only slightly higher than when your line is idle.
Exactly how much seems to depend on the router.

You can try approaching or even exceeding your provisioned bandwidth by
binary search; when you exceed the available bandwidth, you’ll see the
latencies start to rise (slowly). Since the rate at which the buffers
will fill is determined by the difference between the broadband
bandwidth and your router’s bandwidth to the router, patience is in
order to tune the value. Complicating this testing is that some ISP’s
dynamically change the available bandwidth (e.g. Comcast’s PowerBoost).
You actually do often have more bandwidth temporarily available (if it
is available) early in a connection, requiring yet further patience. Did
I tell you that you need patience?

Do the same process for downstream bandwidth. There may or may not be
similar buffers in the downstream direction in the broadband plant (head
end and CPU), and ISP’s may or may not be running RED to control queues
in the broadband “head end” equipment itself. Your mileage may vary.

This process works better on some routers than on others. What value you
should try is not clear. With one router I tried, the behavior on
Comcast was exactly what I would want (low latency) when the router was
set to the provisioned bandwidth (Comcast claims they slightly
over-provision their customer’s accounts); on another router, I have to
reduce the values used by more than 30% from my provisioned bandwidth
(which may or may not reflect reality). Even so, I end up on the router
I am using today with 20ms latency (I get less than 10ms when idle).
Contrast this smokeping with the one in the previous posting: during
this one today, I was performing the same kind rdist to MIT that I
performed when I found the smoking gun. Not perfect, but way more than
an order of magnitude improvement, and also note the packet loss has
stopped.\
Smokeping of my house after broadband bufferbloat mitigation

Mitigated broadband smokeping

Different routers may not shape the bandwidth to the values you
nominally set; before complaining to an ISP that you are not getting
what you pay for, please do your homework and verify the actual
bandwidth you get out of your router (this is easier said than done: but
Dualcomm Technologies makes a cheap port mirroring switch you can
afford). The router may not have computed the transformation from the UI
to the operating system correctly, and/or forgotten to compensate for
packet overhead, or bandwidth shaping may just be broken, and remember,
your ISP’s bandwidth includes your packet overhead; your “goodput”
should be slightly lower than the marketing BPS of the ISP.

Educating all vendors and network operators about bufferbloat is in
order, and exercising your pocket book when selecting hardware and
services is essential to recovery from bufferbloat. But let’s only
complain about the right problem, in the right directions, and politely
please; the mistake is so widespread we are all Bozos on this bus.
Please report problems to the router vendor if they are at fault, and
only bug the ISP they aren’t giving you what you pay for if you
determine they aren’t actually providing what you pay for. No one
appreciates angry support calls, and ones that aren’t people’s fault and
over which they have no control are very frustrating. I am hoping and
presuming my audience is primarily technical, and will be a part of
bufferbloat mitigation and solution, rather than creating a support
nightmare problem for all involved.

Note that this mitigation may also be partial; congestion on the network
interconnecting the broadband head-ends might be reflected into the
broadband hop itself at times of congestion.

This mitigation has come at a cost: you have defeated any PowerBoost
style bandwidth boost your ISP has been kind enough to give you, and
possibly a fraction of your rated bandwidth. This hurts, as the Internet
tradition is to share when resources are available, and be fair when to
everyone when there is not enough resources available. Short of some
attempts (which I haven’t had time to try), such as Paul Bixel’s active
QOS control implementation found in the Gargoyle open source router, you
are out of luck. I’ll report back on my experiences with Gargoyle when I
have time. Alternative mitigations, such as Remote Active Queue
Management as mentioned in Nick Weaver‘s comments to a previous entry
here, may become feasible with time.

For me, the mitigation is a no-brainer: the network th home actually
**works** even when others are using it in my house. With no mitigation,
we would periodically be stepping on each other. Additional bandwidth at
the cost of tolerating a broken network that I can’t use for some of my
essential services is a very poor trade. And if you are a gamer, it may
save your life ;-) .\
QOS and Telephony

If you succeed at mitigating bufferbloat in your broadband connection,
you have further challenges. You may have bufferbloat in the home router
itself, particularly over wireless hops (as I have observed and noted
earlier). Running an open source router may allow further mitigation of
problems in your home router; but this post is long enough as it is and
dinner time is fast approaching, so I’ll leave discussing mitigation of
bufferbloat in home routers for another day.

Let’s first talk about QOS for telephony for a moment. Note that all
this is essentially what Ooma is doing: they put their box in ahead of
your home network, reserve bandwidth for VOIP, and classify VOIP traffic
ahead of other traffic. I used one of these before it was repetitively
damaged by lightning.

Before you have mitigated broadband bufferbloat, any QOS policy you may
set in the router may very well (almost certainly is) ineffective when
your broadband connection is saturated. And the router itself may also
suffer from bufferbloat. (which is why this all can be so confusing;
this bear of little brain has often been very confuzed in this quest).
But once you have successfully mitigated broadband bufferbloat by
bandwidth shaping the broadband hop, you can hope that you to enable QOS
for your non-carrier provided VOIP and Skype might work OK (when the
home router itself is not feeling bloated). I expect it is wise to do so
even though it should not be necessary, for reasons alluded to in a
previous entry, that I will elaborate on in a future blog entry.
Browsers can cause serious jitter, much more than in past years, and are
so worrying they are part of what I lose sleep over. I’ll circle back to
the browser problem in a week or so.

Some of the open source routers (and Linux itself) have very fancy
traffic classification, queue management and allocation facilities;
these may not be enabled even in the open source routers, or properly
set up (depending on the distro). Go wild. Have fun. Find and fix
bufferbloat bugs with and in the open source routers (since I’ve found
that they have the same problems I found on my laptop as covered in fun
with your switch, and fun with wireless, particularly since they seem to
have only worried about the broadband link). Show everyone what can be
done, so the industry catches up faster (and more are free software
converts!).
