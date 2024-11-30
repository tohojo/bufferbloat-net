# Bufferbloat FAQs

We get (and answer) these questions all the time...

---
**Reddit:** [https://www.reddit.com/r/PFSENSE/comments/1ecu16f/traffic_shaper_queue_limiters_not_helping_with/](https://www.reddit.com/r/PFSENSE/comments/1ecu16f/traffic_shaper_queue_limiters_not_helping_with/)

1) Bufferbloat is transitory. You can have very low ping times when the link is idle, but if someone else starts using the network (reading the web, watching a movie, uploading photos from their phone), their bursts of traffic can (WILL!) load the network to 100% momentarily. Could that be enough to make you miss your shot?

2) You're right - bufferbloat tests "artificially load the network". They do this to see how your network performs under those moments of 100% load.

3) You didn't say, but at ISP speeds above 300-500mbps, all the bufferbloat moves into the Wi-Fi system. This is a solved problem (see [Ending the Anomaly](https://arxiv.org/pdf/1703.00064)), but not universally deployed in routers. 

4) > Bufferbloat is not your problem on a gig symmetrical link unless you are smashing the upload. 

This is *exactly* the definition of bufferbloat: If sending a lot of traffic causes your latency to increase by more than 20-30 msec, something is 

---
**Reddit:** [https://www.reddit.com/r/HomeNetworking/comments/1eclgmh/extreme_bufferbloat_on_fibre_connection/](https://www.reddit.com/r/HomeNetworking/comments/1eclgmh/extreme_bufferbloat_on_fibre_connection/)

I'm glad you're working with QoS turned on. To answer your question:

> ...but i just dont understand why jitter and latency is that high without QOS on a fibre connection. 

Garden variety commercial routers (even "gaming routers") frequently don't have guard rails to prevent them from queueing too much data. All the traffic goes "into the queue" (technically, they use a FIFO). A burst of bulk packets (photos from your phone, reading a web page, etc.) delay smaller packets such as gaming updates, voice and videoconference traffic.

QoS helps (as you've seen), but it [won't entirely solve the problem.](https://www.bufferbloat.net/projects/bloat/wiki/More_about_Bufferbloat/#what-s-wrong-with-simply-configuring-qos)

However, this is a solved problem if you have a good router. See [What can I do about Bufferbloat?](https://www.bufferbloat.net/projects/bloat/wiki/What_can_I_do_about_Bufferbloat/) for more details

---
**Reddit:** [https://www.reddit.com/r/Ubiquiti/comments/1euwu0c/bufferbloat_on_u6_and_u7_aps/](https://www.reddit.com/r/Ubiquiti/comments/1euwu0c/bufferbloat_on_u6_and_u7_aps/)

> The amount of packet buffer they will have on board will be trivial. 

And yet, WiFi bufferbloat can easily exceed hundreds of milliseconds. See the [Ending the Anomaly](https://www.usenix.org/system/files/conference/atc17/atc17-hoiland-jorgensen.pdf) and
[Bufferbloat mitigation in the WiFi stack](https://www.netdevconf.org/2.2/session.html?jorgensen-wifistack-talk) talks from 2017 that document this.

Fortunately, that paper also presents a solution involving individual transmit queues for each station, AirTime Fairness, and Airtime Queue Lengths to drop latency by an order of magnitude. These techniques are described in [How OpenWrt Vanquishes Bufferbloat](https://forum.openwrt.org/t/how-openwrt-vanquishes-bufferbloat/189381). 

Can someone from Ubiquiti state whether those techniques are implemented in the U6/U7 gear?

I also want to second the recommendation for [Crusader](https://github.com/Zoxc/crusader). Be sure to get the 0.1.0-dev version (follow the link for Releases) since it's a significant improvement over the earlier release. To measure my WiFi latency, I run the Crusader server on a Raspberry Pi4 on Ethernet to a switch port on my router, then test from other hard-wired or laptop computers.

---
From RandomNeuronsFiring.com

*    This is just the ordinary behavior: Of course things will be slower when there’s more traffic (Willfully ignoring orders of magnitude increase in delay.)
*     Besides, I’m the only one using the internet. (Except when my phone uploads photos. Or my computer fires off some automated process. Or I browse the web. Or …)
*    It only happens some of the time. (Exactly. That’s probably when something’s uploading photos, or your computer is doing stuff in the background.)
*    Those bufferbloat tests you hear about are bogus. They artificially add load, which isn’t a realistic test. (…and what do you experience if you actually are downloading a file?)
*    Bufferbloat only happens when the network is 100% loaded. (True. But when you open a web page, your browser briefly uses 100% of the link. Is this enough to cause momentary lag?)
*    It’s OK. I just tell my kids/spouse not to use the internet when I’m gaming. (Huh?)
*    I have gigabit service from my ISP. (That helps, but if you’re complaining about “slowness” you still need to rule out bufferbloat in your router.)
*    I can’t believe that router manufacturers would ever allow such a thing to happen in their gear. (See the Jim Gettys story above.)
*    I mean… wouldn’t router vendors want to provide the best for their customers? (Not necessarily – implementing this (new-ish) code requires engineering effort. They’re selling plenty of routers using the decade-old software. The Boss says, “would we sell more if we make these changes? Probably not.”)
*    Why would my ISP provision/sell me a router that gave crappy service? They’re a big company, they must know about this stuff. (Maybe. We have reached out to all the vendors. But remember they profit if you decide your network feels too slow and you upgrade to a higher capacity device/plan.)
*    But couldn’t I just tweak the QoS on my router? (Maybe. But see [5])
*    Besides, I just spent $300 on a “gaming router”. I just bought the most expensive/best possible solution on the market. (And you’re concerned that you still have lag?)
*    You’re telling me that a bunch of pointy-headed academics are smarter than commercial router developers – who sold me that $300 router? I can’t believe it. (Well, these fixes seem to solve the problem when it replaces vendor firmware…)
*    And then you say that I should throw away that gaming router and install some “open source firmware”? What the heck is that? And why should I believe you? (Same answer as above.)
*    What if it doesn’t solve the problem? Who will give me support? And how will I get back to a vendor-supported system? (Valid point – the first valid point)
*    Aren’t there any commercial solutions I can just buy? (Not at the moment. IQrouter was a shining light here – available from Amazon, simple setup, worked a treat – but they have gone out of business. And of course, for the skeptic, this is proof that the “fq_codel-stuff” isn’t really a solution – it seems just like snake oil.)
