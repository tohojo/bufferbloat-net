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
of a single FIFO queue.

If packets are arriving much faster than they can
be transmitted, the queue could end up holding
dozens (or hundreds) of packets.
Those buffered packets are "the bloat" in Bufferbloat.
This leads to multiple seconds of latency or "lag".
  
**Q: Where do people see bufferbloat?**

**A:** Bufferbloat is _everywhere_.
It may occur wherever a fast link feeds a slow link,
where a queue of packets can form.
This can happen in the router's connection to an ISP
(the outbound link tends to be slower than the local LAN interfaces)
and in the Wifi interfaces (again, the computers can create
packets faster than the wireless link can carry them).

**Q: Is there a fix for bufferbloat?**

**A:** Yes - an algorithm in the router can create a queue for _each_
flow of traffic, and then offer back-pressure for flows
that are using "more than their share" of the link capacity.

Check out
[How OpenWrt Vanquishes Bufferbloat](https://forum.openwrt.org/t/how-openwrt-vanquishes-bufferbloat/189381)
for a list of the techniques a router can employ.

**Q: How can I measure whether I'm experiencing bufferbloat?**
 
**A:** There are a number of web-based tests that measure latency
_during_ the download and upload:
 
* [Speedtest.net](https://www.speedtest.net/)
* [Waveform Bufferbloat and Speed Test](https://www.waveform.com/tools/bufferbloat)
* [Cloudflare Speed Test](https://speed.cloudflare.com/)

**Q: You say there can be latency in Wi-fi? Can I measure it?**

**A:** Check out the [Crusader](https://github.com/Zoxc/crusader) test. You'll need two computers: connect the first by Ethernet
to a switch port on your router and start the Crusader Server,
then test with the Crusader Client from a second computer.
This measures the latency on Wi-fi or a hardwired computer.

**Q: But, that's not "bufferbloat" - it's just ordinary behavior.
You'd expect things to be slower when there’s more traffic** 

**A:** It seems you're ignoring that
there's an order of magnitude increase in latency.
That's far more than expected if the network is "just busy".

**Q: But I’m the only one using the internet...**

**A:** It may be true that you're the only _human_ in the house. But does your phone ever upload photos? Does your computer fire off any automated process? Or do you browse the web, or otherwise use the internet? Any of those can generate traffic that induces latency.

**Q: It only happens some of the time...**

**A:** Exactly - Bufferbloat is transitory.
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

**A:** That helps, but if you’re reading this and
complaining about “slowness”
you still going to have to rule out bufferbloat as the cause.

**Q: I can’t believe that router manufacturers would ever allow such a thing to happen.**

**A:** In the 2010 time period, no one understood this phenomenon. In 2011, Jim Gettys reported on his work with other network experts (in [Dark Buffers in the Internet](https://mirrors.bufferbloat.net/Talks/BellLabs01192011/110126140926_BufferBloat12.pdf)) to show how surprising it was that routers would queue far more data than they could send in a reasonable time. 

In 2012, CoDel was invented in response the newly-named "bufferbloat". In the decade since, we've seen fq_codel, CAKE, and cake-autorate - all open-source algorithms for minimizing latency.
  
Today, there's no excuse for router vendors not to incorporate this technology. But still, they haven't done it.

**Q: I mean… wouldn’t router vendors want to provide the best for their customers?**

**A:** Not necessarily – implementing any new code requires engineering effort. They’re selling plenty of routers using the decade-old software. 
The Boss asks, “Would we sell more
routers if we make those changes?" _Probably not, so the vendors don't change. But if everyone started writing reviews saying Vendor X has bufferbloat and games are unplayable, but Vendor Y doesn't..._

**Q: Why would my ISP sell me a router that gave crappy service? They’re a big company: they must know about this stuff.**

**A:** Maybe. We have reached out to lots of vendors. But remember they profit if you decide your network feels too slow and you upgrade to a higher capacity device/plan.

**Q: But couldn’t I just tweak the QoS on my router?**

**A:** Maybe. It's a fiddly process, and doesn't always work.
See [Why not simply configure QoS?](https://www.bufferbloat.net/projects/bloat/wiki/More_about_Bufferbloat/#why-not-simply configure-qos)
for more information.

**Q: Besides, I just spent $300 on a “gaming router”. It was the most expensive/best possible solution on the market.**

**A:** And you’re looking here because you still have lag?
Maybe that router's not as good as their advertising says...

**Q: I can't believe you’re telling me that a bunch of academics have come up with a better algorithm than commercial router developers - that company who sold me that $300 router?**

**A:** Well, the fq_codel/CAKE algorithms seem to solve the problem when they replace vendor firmware…

**Q: And then you say that I should throw away that gaming router and install some “open source firmware”? What the heck is that? And why should I believe you?** 

**A:** Same answer as above.

**Q: What if it doesn’t solve the problem? Who will give me support? And how will I get back to a vendor-supported system?**

**A:** This is a valid point - see the next question.

**Q: Aren’t there any commercial solutions I can just buy?**

**A:** Yes. The [What Can I Do About Bufferbloat?](https://www.bufferbloat.net/projects/bloat/wiki/What_can_I_do_about_Bufferbloat/) page list several vendors who have figured out how to implement these algorithms.

**Q: A question about "Traffic Shaper Queue Limiters not helping with Bufferbloat"**
([Original post on Reddit](https://www.reddit.com/r/PFSENSE/comments/1ecu16f/traffic_shaper_queue_limiters_not_helping_with/))
 
**A:** Despite the confident assurances from other posters that it's not bufferbloat, it sounds as if you're seeing latency/lag when gaming. Here's what could be going on. 

1) Bufferbloat is transitory. You can have very low ping times when the link is idle, but if someone else starts using the network (reading the web, watching a movie, uploading photos from their phone), their bursts of traffic can load the network to 100% momentarily. Could that be enough to make you miss your shot?
 
2) You're right - bufferbloat tests "artificially load the network". They do this to see how your network performs under those moments of 100% load.
 
3) You didn't say, but at ISP speeds above 300-500mbps, the bufferbloat in the Wi-Fi system can become important. This is a solved problem (see [Ending the Anomaly](https://arxiv.org/pdf/1703.00064)), but not universally deployed in routers.
 
4) > Bufferbloat is not your problem on a gig symmetrical link unless you are smashing the upload.

This is *exactly* the definition of bufferbloat: If sending a lot of traffic causes your latency to increase significantly,
something is wrong, likely bufferbloat.
 
**Q: A question about "Extreme Bufferbloat on fibre connection"** ([Original post on Reddit](https://www.reddit.com/r/HomeNetworking/comments/1eclgmh/extreme_bufferbloat_on_fibre_connection/))
 
**A:** I'm glad you're working with QoS turned on. To answer your question:
 
> ...but i just dont understand why jitter and latency is that high without QOS on a fibre connection.
 
Garden variety commercial routers (even "gaming routers") frequently don't have guard rails to prevent them from queueing too much data. All the traffic goes "into the queue" (technically, they use a FIFO). A burst of bulk packets (photos from your phone, reading a web page, etc.) delay smaller packets such as gaming updates, voice and videoconference traffic.
 
QoS helps (as you've seen), but it [won't entirely solve the problem.](https://www.bufferbloat.net/projects/bloat/wiki/More_about_Bufferbloat/#what-s-wrong-with-simply-configuring-qos)
 
However, this is a solved problem if you have a good router. See [What can I do about Bufferbloat?](https://www.bufferbloat.net/projects/bloat/wiki/What_can_I_do_about_Bufferbloat/) for more details
 
**Q: A question about "Bufferbloat on U6 and U7 APs"** ([Original post on Reddit](https://www.reddit.com/r/Ubiquiti/comments/1euwu0c/bufferbloat_on_u6_and_u7_aps/))
 
  > The amount of packet buffer they will have on board will be trivial.
 
**A:** And yet, WiFi bufferbloat can easily exceed hundreds of milliseconds. See the [Ending the Anomaly](https://www.usenix.org/system/files/conference/atc17/atc17-hoiland-jorgensen.pdf) and
[Bufferbloat mitigation in the WiFi stack](https://www.netdevconf.org/2.2/session.html?jorgensen-wifistack-talk) talks from 2017 that document this.
 
Fortunately, that paper also presents a solution involving a) individual transmit queues for each station,
b) AirTime Fairness, and c) Airtime Queue Lengths to drop latency by an order of magnitude. These techniques are described in [How OpenWrt Vanquishes Bufferbloat](https://forum.openwrt.org/t/how-openwrt-vanquishes-bufferbloat/189381).
