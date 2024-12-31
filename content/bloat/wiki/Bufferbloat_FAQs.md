---
title: Bufferbloat FAQs
date: 2024-12-01T09:10:12
lastmod: 2024-12-01T09:10:12
type: wiki
---
# Bufferbloat FAQs
 
We get these questions all the time.
First some background questions, then actual questions
from various forums.
 
---
 
**Q: What is Bufferbloat?**

**A:** [Wikipedia says](https://en.wikipedia.org/wiki/Bufferbloat),
"Bufferbloat is the undesirable latency that comes from a
router or other network equipment buffering too many data packets." 

**Q: What does _that_ mean? How could that happen?**

**A:** If a router doesn't use a better algorithm,
it will happily place every new packet at the end
of a single FIFO queue
before sending them to your ISP.

If packets arrive at the router faster than they can
be transmitted to the ISP, the queue builds up.
It could wind up with dozens (or hundreds) of packets,
potentially causing multiple seconds of latency or "lag".
Those buffered packets are "the bloat" in Bufferbloat.
  
**Q: How can I tell whether I'm experiencing bufferbloat?**
 
**A:** There are a number of web-based tests that measure latency
_during_ the download and upload:
 
* [Speedtest.net](https://www.speedtest.net/)
* [Waveform Bufferbloat and Speed Test](https://www.waveform.com/tools/bufferbloat)
* [Cloudflare Speed Test](https://speed.cloudflare.com/)

If the test shows an increase of latency under load
of less than 15-25 msec, then the latency is well under control.

**Q: Where do people see bufferbloat?**

**A:** Bufferbloat is _everywhere_.
It occurs when there's a bottleneck -
a place where a fast link feeds into a slow link.
When a lot of packets arrive at the bottleneck,
the router queues those packets.
One or two queued packets can be beneficial
so that the slow link never "starves".
But queueing more packets only adds latency (delay) to
the transit time of those packets.

**Q: Where does bufferbloat happen in the real world?**

**A:** These large queues build up in the router's connection to an ISP
(the outbound link tends to be slower than the local LAN interfaces)
and also in the Wifi interfaces (again, the computers can create
packets faster than the wireless link can carry them).

**Q: You say there can be high latency in Wi-fi?**

**A:** Yes. Wi-Fi drivers can often queue
hundreds of milliseconds of packets,
which adds another layer of delay to the data.

**Q: How can I measure Wi-Fi latency?**

**A:** Check out the [Crusader](https://github.com/Zoxc/crusader) application.
You'll need two computers: connect the first by Ethernet
to a LAN switch port on your router and start the Crusader Server,
then run the Crusader Client from a second computer.
This measures the latency on Wi-fi or a hardwired connection.

**Q: Is there a fix for bufferbloat?**

**A:** Yes - a router can implement one of several algorithms.
In essence, they all:

1. Separate every traffic flow’s arriving packets into their own queue.
2. Remove a small batch of packets from a queue, round-robin style,
    and transmit that batch through the (slow) bottleneck link.
    When each batch has been fully sent, remove a batch from the next queue, and so on.
3. Offer back pressure to flows that are sending “more than their share” of data.

Check out
[How OpenWrt Vanquishes Bufferbloat](https://forum.openwrt.org/t/how-openwrt-vanquishes-bufferbloat/189381)
for a list of the techniques a router can employ.

**Q: But, that's not "bufferbloat" - it's just ordinary behavior.
Of course things will be slower when there’s more traffic...** 

**A:** It seems you're ignoring the
order of magnitude increase in latency.
That's far more than expected if the network is "just busy".

**Q: But I’m the only one using the internet...**

**A:** It may be true that you're the only _human_ in the house.
But does your phone ever upload photos?
Does your computer fire off any automated process?
Does your Tesla (or your refrigerator) get updates?
Or do you browse the web, or otherwise use the internet?
Any of those can generate traffic that induces latency.

**Q: It only happens some of the time...**

**A:** Exactly - bufferbloat is transitory.
You probably notice it when someone's uploading photos,
or your computer is doing something in the background.

**Q: Those bufferbloat tests you hear about are bogus. They artificially add load, which isn’t a realistic test.**

**A:** Yes, the tests do add load.
But what would you expect to happen
if you actually were uploading or downloading a file?

**Q: Bufferbloat only happens when the network is 100% loaded.**

**A:** This is related to the previous answer.
When you open a web page or open an email attachment,
your computer briefly uses 100% of the link.
Is this enough to cause momentary lag?

**Q: It’s OK. I just tell my kids/spouse not to use the internet when I’m gaming.**

**A:** Really?

**Q: But, I have gigabit service from my ISP** 

**A:** That helps, but if you’re reading this
because you're worried about a “slow network”
you still must rule out bufferbloat as the cause.

**Q: I can’t believe that router manufacturers
would ever allow such a thing to happen.**

**A:** In the 2010 time period, no one understood this phenomenon. In 2011, Jim Gettys reported on his work with other network experts (in [Dark Buffers in the Internet](https://mirrors.bufferbloat.net/Talks/BellLabs01192011/110126140926_BufferBloat12.pdf)) to show how surprising it was that routers would queue far more data than they could send in a reasonable time. 

In 2012, CoDel was invented in response the newly-named "bufferbloat". In the decade since, we've seen fq_codel, CAKE, and cake-autorate - all open-source algorithms for minimizing latency.
  
Today, there's no excuse for router vendors not to incorporate this technology. But still, they haven't done it.

**Q: I mean… wouldn’t router vendors want
to provide the best for their customers?**

**A:** Not necessarily – implementing any new code requires engineering effort.
They’re selling plenty of routers using the decade-old software.
The Boss asks, “Would we sell more routers if we make those changes?" (Probably not, so the vendors don't change.)

But if everyone started writing reviews saying Vendor X has bufferbloat
and games are unplayable, but Vendor Y doesn't...

**Q: Why would they sell me a router that gave crappy service?
They’re a big company - they must know about this stuff.**

**A:** Maybe. We have reached out to lots of vendors.
But remember they profit if you decide to upgrade to a higher capacity device/plan.

**Q: But couldn’t I just tweak the QoS on my router?**

**A:** Maybe. It's a fiddly process, and doesn't always work.
See [Why not simply configure QoS?](https://www.bufferbloat.net/projects/bloat/wiki/More_about_Bufferbloat/#why-not-simply configure-qos)
for more information.

**Q: Besides, I just spent $300 on a “gaming router”.
It was the most expensive/best possible solution on the market.**

**A:** Maybe that router's not as good as their advertising says...

**Q: I can't believe you’re telling me that
a bunch of academics have come up with
a better algorithm than commercial router developers -
that company who sold me that $300 router?**

**A:** Well, the fq_codel/CAKE algorithms seem to solve the problem when they replace vendor firmware…

**Q: And then you say that I should throw away that gaming router
and install some “open source firmware”?
What the heck is that? And why should I believe you?** 

**A:** Same answer as above.

**Q: What if it doesn’t solve the problem?
Who will give me support?
And how will I get back to a vendor-supported system?**

**A:** This is a valid point - see the next question.

**Q: Aren’t there any commercial solutions I can just buy?**

**A:** Yes. The
[What Can I Do About Bufferbloat?](https://www.bufferbloat.net/projects/bloat/wiki/What_can_I_do_about_Bufferbloat/)
page list several vendors who have figured out
how to implement these algorithms.

**Q: All the foregoing makes it sound as if bufferbloat
only happens on upload (from my local network toward my ISP).
Does Bufferbloat ever happen on download?**

**A:** Absolutely. There's a bottleneck at your ISP as well. 
The head end/DSLAM/etc. is where the high-speed lines supplying your ISP
send traffic to the (slower) link coming toward you.
That fast-to-slow transition is another place that
can build up significant queues.

**Q: How do the bufferbloat algorithms work for the download direction?**

**A:** They introduce an internal "download interface"
_within the local router_ that acts as the bottleneck.
Like the upload direction, that internal download interface
is configured to be slightly slower than the ISP link
(typically 5%-10% slower).
That lets the queue build up within the local router,
where the bufferbloat algorithm can control it.

**Q: A question about "Traffic Shaper Queue Limiters not helping with Bufferbloat"**
([Original post on Reddit](https://www.reddit.com/r/PFSENSE/comments/1ecu16f/traffic_shaper_queue_limiters_not_helping_with/))
 
> ... Wondering if anyone could help me out with this configuration, again the whole purpose of this is to have the lowest latency as possible when gaming. I understand that the bufferbloat test is designed to see how the network handles high stress loads and when considering for online gaming (eg. COD MW3) I understand it doesn’t use anywhere near by max bandwidth. Even under lower loads I still get the same latency values.   

**A:** Despite the confident assurances from other posters that it's not bufferbloat, it sounds as if you're seeing latency/lag when gaming. Here's what could be going on. 

1. Bufferbloat is transitory. You can have very low ping times when the link is idle,
but if someone else starts using the network (reading the web,
watching a movie, uploading photos from their phone),
their bursts of traffic can momentarily load the network to 100%.
Could that be enough to make you miss your shot?
 
2. You're right - bufferbloat tests "artificially load the network".
They do this to see how your network performs under those moments of 100% load.
 
3. You didn't say, but at ISP speeds above 300-500mbps,
  the bufferbloat in the Wi-Fi system can become important.
  This is a solved problem (see
  [Ending the Anomaly](https://arxiv.org/pdf/1703.00064)),
  but not universally deployed in routers.
 
> Bufferbloat is not your problem on a gig symmetrical link unless you are smashing the upload.

This is _exactly_ the definition of bufferbloat.
If sending a lot of traffic causes your latency to increase significantly,
something is wrong, likely bufferbloat.
 
**Q: A question about "Extreme Bufferbloat on fibre connection"** ([Original post on Reddit](https://www.reddit.com/r/HomeNetworking/comments/1eclgmh/extreme_bufferbloat_on_fibre_connection/))
 
**A:** I'm glad you're working with QoS turned on. To answer your question:
 
> ... I'm playing competitive games and it feels like im desynced to the server 70 % of my matches. First image is with no QOS in the router, the second one is when im limiting my bandwith to 85 % up and down. With QOS its ok, but i just dont understand why jitter and latency is that high without QOS on a fibre connection.
 
Garden variety commercial routers (even "gaming routers") frequently don't have guard rails to prevent them from queueing too much data. All the traffic goes "into the queue" (technically, they use a FIFO). A burst of bulk packets (photos from your phone, reading a web page, etc.) delay smaller packets such as gaming updates, voice and videoconference traffic.
 
QoS helps (as you've seen), but it [won't entirely solve the problem.](https://www.bufferbloat.net/projects/bloat/wiki/More_about_Bufferbloat/#what-s-wrong-with-simply-configuring-qos)
 
However, this is a solved problem if you have a good router. See [What can I do about Bufferbloat?](https://www.bufferbloat.net/projects/bloat/wiki/What_can_I_do_about_Bufferbloat/) for more details
 
**Q: A question about Bufferbloat on Wifi** ([Original post on Reddit](https://www.reddit.com/r/Ubiquiti/comments/1euwu0c/bufferbloat_on_u6_and_u7_aps/))

>> Given the focus of latency in the Wi-Fi 6 and Wi-Fi 7 standards, has anyone tested the bufferbloat behavior of these AP? I'm particularly interested in U6+.
>
> ... The amount of packet buffer they will have on board will be trivial.
 
**A:** And yet, WiFi bufferbloat can easily exceed hundreds of milliseconds. See the
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

**Q: An Edgerouter solves latency, but seems not to handle the speed...**
[(Original post on Reddit)](https://www.reddit.com/r/opnsense/comments/1h6rh3u/fixing_buffer_bloat_what_is_going_on_new_update/)

> ... Whenever my Tesla started updating, my ping went to crap...
> Finally, I threw my hands up in the air, 
> configured an edgerouter I had here and enabled smart queue.
> Instantly I was getting A+ scores,
> with +0ms on both incoming and outcoming. 
> 
> Do I need new hardware? If so what is recommended? 
> Should I just give up and use the edge router.

A couple thoughts. My mentor once said, "If you can't tell the difference,
it doesn't make a difference".
How does that apply to the situation you describe?

1. If you're happy with the way your network performs,
   you can declare victory.
   If the Edgerouter gives near zero additional latency,
   it seems like a win.

2. You didn't mention the rated speed for your ISP,
   but do you ever notice that it's "not fast enough"
   when using the Edgerouter?
   If not, you might consider dropping your ISP contract
   to a lower tier and save a few bucks per month.

3. You can then use the time you've saved by not horsing
   around more with your network to do useful things.

**Q: Consider a lower tier plan from your ISP** ([Original post on Reddit](https://www.reddit.com/r/HomeNetworking/comments/1h9n7zl/comment/m179gh7/))

>    ... I'd like a plug and play QoS router with a 5gb/s WAN port and at least 1 5gb/s LAN port (future proofing) ...

A 5Gbps-capable router is going to cost serious money.
(I don't know your budget, but it'll be a lot.)

Your ISP has probably been wooing you to get a
higher and higher speed plan,
especially if you say "it's not fast enough".
But if your router is adding latency,
then everything feels slow, regardless of the speed.

Surprising, the "speed to deliver" normal data
doesn't increase by much for a faster link.
See the charts in
[The Latency Effect](https://www.afasterweb.com/2015/05/17/the-latency-effect/)
that show that increasing "speed" doesn't make pages load much faster.
_Decreasing_ latency always made pages load faster.

So 250mbps or 300mbps could be plenty unless you want bragging rights.

Here is a bit of contrarian advice.
If you don't actually need 5Gbps service,
consider these options:

* Get a lower tier plan from your ISP
* Get a router that understands modern algorithms
  for minimizing latency/bufferbloat. See
  [What can I do about Bufferbloat?](https://www.bufferbloat.net/projects/bloat/wiki/What_can_I_do_about_Bufferbloat/)
  for a list of suitable routers
* You'll see the latency drop with no apparent
  difference in your perceived speed
* And save a bunch of money per month on your ISP bill
