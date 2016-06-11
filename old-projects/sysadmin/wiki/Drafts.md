
---
title: Drafts
date: 2011-02-01T17:42:18
lastmod: 2011-02-01T17:42:18
type: wiki
---
Drafts
======

hdescription+xml" href="http://wordpress.com/opensearch.xml"
title="WordPress.com" /&gt;

<style type='text/css'>
<!--
body { background: url("http://s0.wp.com/wp-content/themes/default/images/kubrickbgcolor.gif?m=1273203575g"); }
#page { background: url("http://s0.wp.com/wp-content/themes/default/images/kubrickbgwide.gif?m=1273203575g") repeat-y top !important; border: none; }
#header { background: url("http://s0.wp.com/wp-content/themes/default/images/kubrickheader.gif?m=1273203575g") no-repeat bottom center; }
#footer { background: url("http://s0.wp.com/wp-content/themes/default/images/kubrickfooter.gif?m=1273203575g") no-repeat bottom; border: none;}
#header { margin: 0 !important; margin: 0 0 0 1px; padding: 1px; height: 198px; width: 758px; }
#headerimg { margin: 7px 9px 0; height: 192px; width: 740px; }
#headerimg h1 a, #headerimg h1 a:visited, #headerimg .description { color: ; }
#headerimg h1 a, #headerimg .description { display:  }

    -->
</style>
<style type="text/css">
.recentcomments a{display:inline
![](important;padding: 0 )important;margin: 0 !important;}

</style>
<meta name="application-name" content="jg&#039;s Ramblings" /><meta name="msapplication-window" content="width=device-width;height=device-height" /><meta name="msapplication-tooltip" content="Jim Gettys&#039; ramblings on random topics, and occasional rants." /><meta name="msapplication-task" content="name=Subscribe;action-uri=http://gettys.wordpress.com/feed/;icon-uri=http://s1.wp.com/i/favicon-stacked.ico" /><meta name="msapplication-task" content="name=Sign up for a free blog;action-uri=http://wordpress.com/signup/;icon-uri=http://s2.wp.com/i/favicon.ico" /><meta name="msapplication-task" content="name=WordPress.com Support;action-uri=http://support.wordpress.com/;icon-uri=http://s2.wp.com/i/favicon.ico" /><meta name="msapplication-task" content="name=WordPress.com Forums;action-uri=http://forums.wordpress.com/;icon-uri=http://s2.wp.com/i/favicon.ico" />

</head>
<body>
<div id="page">
<div id="header">
<div id="headerimg" onclick=" location.href='http://gettys.wordpress.com';" style="cursor: pointer;">
<h1>
<a href="http://gettys.wordpress.com/">jg's Ramblings</a>

</h1>
<div class="description">
Jim Gettys' ramblings on random topics, and occasional rants.

</div>
</div>
</div>
<hr />
<div id="content" class="widecolumn">
<div class="navigation">
<div class="alignleft">
«
<a href="http://gettys.wordpress.com/2010/12/09/bufferbloat-and-congestion-collapse-back-to-the-future/" rel="prev">Bufferbloat
and congestion collapse – Back to the&nbsp;Future?</a>

</div>
<div class="alignright">
<a href="http://gettys.wordpress.com/2010/12/17/red-in-a-different-light/" rel="next">RED
in a Different&nbsp;Light</a> »

</div>
</div>
<div class="post-360 post type-post status-publish format-standard hentry category-bufferbloat category-networking category-puzzle clear" id="post-360">
<h2>
Mitigations and Solutions of Bufferbloat in Home Routers and
Operating&nbsp;Systems

</h2>
<small>By gettys</small>

<div class="entry">
<p>
<a href="http://gettys.files.wordpress.com/2010/10/jigsawfish2.png"><img class="alignright size-thumbnail wp-image-114" title="jigsawfish2" src="http://gettys.files.wordpress.com/2010/10/jigsawfish2.png?w=90&#038;h=82" alt="" width="90" height="82" /></a>As
discussed
<a title="Mitigations versus Solutions of Bufferbloat in Broadband" href="http://gettys.wordpress.com/2010/12/08/bufferbloat-mitigations/">several
days ago</a> we can mitigate (but not solve) broadband bufferbloat to a
decent, if not ideal, degree by using bandwidth shaping facilities found
in many recent home routers. Unfortunately, life is more complicated and
home routers themselves are often typically at fault (if you find a
recently designed home router that works right, it may want to be
enshrined in a museum where its DNA and evolution analyzed, and its
implementors both admired for their accomplishment and despised, for not
telling us about what they discovered. Complete robust solutions,
unfortunately, will be difficult in the short term (wireless makes it an
“interesting” problem) for reasons I’ll get to in this and future posts.

</p>
<p>
Confounding the situation further, your computer’s/ smartphone/
netbook’s/ tablet’s operating system may also be suffering from
bufferbloat, and the its severity may/almost certainly does depend upon
the hardware. Your mileage <em>will</em> vary.

</p>
<p>
You may or may not have enough access to the devices to even manipulate
the bufferbloat parameters. Locked down systems come back to bite you.
But again, you can probably make the situation much better for you
personally, if you at a minimum understand what is causing your pain,
and are willing to experiment.

</p>
<h2>
Conclusions

</h2>
<p>
Since any number you pick for buffering is guaranteed to be wrong for
many use cases we care about, the general solution will await operating
systems implementers revisiting buffering strategies to deal with the
realities of the huge dynamic range of today’s networks, but we can
mitigate the problem (almost) immediately by tuning without waiting for
nirvana to arrive.

</p>
<p>
<span id="more-360"></span>

</p>
<p>
As an end user, you may suffer in your home router or your computer
anytime when the bandwidth (“goodput”) you get over a wireless hop is
less than the provisioned and actually provided broadband bandwidth.
This is why I immediately saw problems on the Verizon FIOS wireless
routers (the traces show both problems on the wired and wireless side;
but the wireless side is much worse). On that typically symmetric
service at my in-law’s FIOS 20/20 service, 802.11g is usually running
more slowly than the broadband connection. I also see bufferbloat
regularly at home on my router using my Comcast service, which I
recently changed to 50/10 service; there are parts of my house where it
is now easy to get enough insufficient bandwidth over wireless.
Bufferbloat is nothing if not elusive. It’s been like hunting the
<a title="Will o the wisp wikipedia entry" href="http://en.wikipedia.org/wiki/Will-o'-the-wisp" target="_blank">will
o’ the wisp</a> on wireless, until I had a firm mental grasp on what was
happening.

</p>
<p>
<em>Remember: you see bufferbloat only on the buffers adjacent to the
bottleneck in the path you are using. Buffers elsewhere in the path you
are probing remain invisible, unless and until they become the
bottleneck hop.</em>

</p>
<h2>
Mitigating the inbound home router wireless bufferbloat problem

</h2>
<p>
Whenever the bandwidth from your ISP exceeds that of your wireless
“goodput”, you’ll likely see bufferbloat in your home router (since the
bottleneck is the wireless hop between you and the router). Full
solutions to the problem are beyond the scope of today’s posting (coming
soon), and will require some research, though ways forward exist. In
short, complete solutions will require active queue management (e.g. RED
or similar algorithms), since the mitigation strategy of bandwidth
shaping to “hide” the buffer we showed in a previous post will not lend
itself well to the highly variable bandwidth & goodput of wireless.
Outbound, it is very likely in your operating system where the bloat
will occur (since your router is generally connected to the broadband
gear either internally (as in the FIOS router I experimented with) or
via a 100Mbps or 1Gps ethernet. You’ll most likely experience this, as
one of the replies to this posting points out, when uploading large
files, doing backups, or similar operations. I only realized OS
bufferbloat occurs after I started investigating home routers and did
not get the results I expected immediately. With some disbelief, I got
confirmation with the simple experiments I reported on.

</p>
<p>
If you can “log in” to a shell prompt on your wireless router (many are
running Linux, and a few have known ways to break into them), or are
willing to
<a title="Wireless router firmware projects from Wikipedia" href="http://en.wikipedia.org/wiki/List_of_wireless_router_firmware_projects">install
open source firmware on your router</a>, you can go further, by
mitigating the excessive buffering in the ways explained below for
Linux. Remember, that this only affects the down stream direction (home
router to your laptop). Note that the only one of these open source
projects I have found that has close to turnkey classification and
mitigation of broadband bufferbloat is
<a title="Gargoyle router wikipedia entry" href="http://en.wikipedia.org/wiki/Gargoyle_Router_Firmware" target="_blank">Gargolye</a>.
Paul Bixel has worked hard on mitigating broadband bufferbloat, but has
not attempted wireless bufferbloat mitigation.
<a title="Mitigations versus Solutions of Bufferbloat in Broadband" href="http://gettys.wordpress.com/2010/12/08/bufferbloat-mitigations/">As
noted in a previous post</a>, many mid to high end home routers have
enough capability to mitigate broadband bufferbloat.

</p>
<p>
<span style="font-size:26px;font-weight:bold;">OS Bufferbloat
Mitigation</span>

</p>
<p>
As explained in
<a title="Home Router Puzzle Piece One - Fun with your switch" href="http://gettys.wordpress.com/2010/11/29/home-router-puzzle-piece-one-fun-with-your-switch/">fun
with your switch</a>,
<a title="Home Router Puzzle Piece Two - Fun with wireless" href="http://gettys.wordpress.com/2010/12/02/home-router-puzzle-piece-two-fun-with-wireless/">fun
with wireless</a>, and the
<a title="The criminal mastermind: bufferbloat!" href="http://gettys.wordpress.com/2010/12/03/introducing-the-criminal-mastermind-bufferbloat/">criminal
mastermind</a> postings, and in future blog postings, we have bad
behavior all over the Internet, though I focused on the home environment
in most of the postings so far. In all of the common operating systems,
there is at least one, if not two places (and maybe more undiscovered)
where bloat has been demonstrated. Please go find and fix them. All OS’s
therefore suffer to some extent or another.

</p>
<p>
Your most immediate mitigation may be to literally move either your
laptop or your home router to where the bandwidth equation is different,
shifting bufferbloat to a (possibly) less painful point. But there are
also potentially some quick mitigations you can perform on your laptop,
and as some others in replies to previous postings have demonstrated,
that are more general. The first order mitigation is to set your
buffering in your operating system to something reasonable, as explained
below (details of the Linux commands can be found in
“<a title="Home Router Puzzle Piece One – Fun with your switch" href="http://gettys.wordpress.com/2010/11/29/home-router-puzzle-piece-one-fun-with-your-switch/">fun
with your switch</a>” and
“<a title="Home Router Puzzle Piece Two – Fun with wireless" href="http://gettys.wordpress.com/2010/12/02/home-router-puzzle-piece-two-fun-with-wireless/">fun
with wireless</a>“.

</p>
<h2>
Linux

</h2>
<p>
I’ll discuss Linux first, as in my testing, it has problems that may
affect you even if you don’t run Linux, as Linux is often used in home
routers. But then again, as I use Linux for everything, there may be
more buffers on other operating systems that I have not run into; my
testing on Mac and Windows has been very small relative to Linux. <em>We
all live in a glass house; don’t go throwing stones. Be polite.</em>
Demonstrate real problems.
<a title="Bufferbloat and congestion collapse – Back to the Future?" href="http://gettys.wordpress.com/2010/12/09/bufferbloat-and-congestion-collapse-back-to-the-future/">But
be insistent, for the health of the internet.</a>

</p>
<p>
Note the total amount of buffering causes TCP and other congestion
avoiding protocols indigestion: in Linux’s case, it is both the device
driver rings (which I believe I see in other operating systems) and the
“transmit queue” buffering. I gather some of the BSD systems may have
unlimited device driver buffering. Some hardware may also be doing
further buffering below the register level in smart devices (I susped
the Marvell wireless device we used on OLPC might, for example).

</p>
<p>
As discussed in
<a title="Home Router Puzzle Piece One – Fun with your switch" href="http://gettys.wordpress.com/2010/11/29/home-router-puzzle-piece-one-fun-with-your-switch/">fun
with your switch</a>, I detected two different sources of excessive
buffering in Linux, both typically resulting from device drivers
(therefore shared in common with other operating systems). Device
drivers hint to the operating system a “transmit queue length”, which is
controllable on Linux by use of the “txqueuelen” parameter settable
using the “ifconfig” command. By default, many/most modern ethernet and
wireless NIC’s are telling Linux to be willing to buffer up to 1000
packets. In my experiments on (most) of my hardware, since the ethernet
and wireless rings are both at a minimum quite large, I could set
txqueuelen to zero without causing any immediate problems.

</p>
<p>
<em>But note that if you set buffering to zero in both device drivers
(and the transmit queue), if there is no other buffering you don’t
happen to know about, your system will just stop transmitting entirely;
so some care is in order. This depends on the exact details of the
hardware. </em>Buffering is necessary; just not the huge amounts
currently common, particularly at these speeds and low latencies.

</p>
<p>
Also note that many device drivers (e.g. the Intel IWL wireless driver)
do not support the controls to set the ring buffer sizes, and at least
one device I played with it seemed to have no effect whatsoever
(implying buffering present, but no control over the size of those
buffers).

</p>
<p>
A possible reason for the transmit queue (others with first hand
knowledge of the history, please chime in), is that on some old
hardware, e.g.old serial devices being used with modems, had essentially
no buffering, and you might experience excessive packet loss on those
devices. It may have also been really necessary for performance before
Linux’s socket buffer management became more sophisticated and started
to adjusting its socket buffer sizes based on the observed RTT (note
that the lower level bufferbloat may be inducing socket bufferbloat and
application latency as well, though I have no data to confirm this
hypothesis). At some point, the default value for txqueuelen was raised
to 1000; I don’t know the history or discussion that may have taken
place. There are also queues in the operating system required for
traffic classification; I haven’t had time to figure out if that is
where Linux implementss its classification algorithms or not; some
hardware also supports multiple queues for that purpose. Note this means
that many Linux based devices and home routers may have inherited
differing settings. Extreme bufferbloat is present on a number of the
common commercial home routers I have played with using modern hardware,
and the open source routers I’ve played with as well.

</p>
<p>
So even though the “right” solution is proper queue management on you
can tune the txqueuelen and (possibly) the NIC device driver rings to
more reasonable sizes, rather than the current defaults, which are
typically set for server class systems on recent hardware.

</p>
<p>
Once tuned, Linux’s latency (and the router’s latency) can be really
nice even under high load (even if I’ve not tried hard to get to the
theoretical minimums). But un-tuned, I can get many second latency out
of both Linux home routers and my laptop, just by heading to some part
of my house where my wireless signal strength is low (I have several
chimneys that makes this trivial). By walking around or obstructing your
wireless router, you should be easily able to reproduce bufferbloat in
either your router or in your laptop, depending on which direction you
saturate.

</p>
<p>
With an open source router on appropriate hardware and a client running
Linux, you can make bufferbloat very much lower in your home
environment, even when bufferbloat would otherwise cause your network to
become unusable. Nathaniel Smith in a reply to
“<a title="Home Router Puzzle Piece Two – Fun with wireless" href="http://gettys.wordpress.com/2010/12/02/home-router-puzzle-piece-two-fun-with-wireless/">Fun
with Wireless</a>” shows what can be done when you both set the
txqueuelen and change the driver (in his case, a one line patch!)

</p>
<p>
<span style="font-size:20px;font-weight:bold;">Mac OSX</span>

</p>
<p>
I’ve experimented on relatively recent Apple hardware: on Ethernet
showed what appears to be device driver ring bufferbloat, roughly
comparable to Linux. On my simple test on ethernet on a 100Mbps switch,
I observed 11ms latency, roughly, slightly more than Linux which was 8ms
on similar vintage hardware in the same comparable test. On Linux, the
transmit ring is set to 256, by default, and allowed me to set it as
small as 64. So I hypothesize a similar size buffer in it’s ethernet
driver (and possibly a small buffer in the OS above the driver). As I’m
not a Mac expert, I can’t tell you as I could on Linux how to reduce the
transmit ring size.

</p>
<p>
I have not tried to pry my son’s Mac out of his hands for Mac wireless
experiments: perhaps you would like to do so with your Mac, or I may get
around to the wireless experiment over the holidays. If you do, make
sure you arrange the bottleneck to be in the right place (the lowest
bandwidth bottleneck needs to be between your laptop and your test
system).

</p>
<h2>
Microsoft Windows

</h2>
<p>
Experimenting with Microsoft Windows several weeks ago was a really
interesting experience. Plugged into a 100Mbps switch, there was no
bufferbloat in the operating system (both Windows XP and Windows 7) on
recent hardware. But neither Windows saturate a 100Mbps switch (you
expect to see about 93Mbps on that hardware, due to TCP and IP header
overhead). As soon as we set the NIC to run at 10Mbps, the expected
bufferbloat behavior occurred. Since in my tests, the medium no longer
is the bottleneck, it shifts to somewhere else in the path (in my test,
there was no bottleneck).

</p>
<p>
Here’s what I think is going on and I believe what happened.

</p>
<p>
With some googling, I discovered on Microsoft’s web site that Microsoft
has bandwidth shaped their TCP implementation to not run at full speed
by default, but to run probably just below what a 100Mbps network (I
observed mid 80 megabit). You have to go tune registry parameters to get
full performance on Microsoft Windows TCP implementation. There is an
explanation on their web site that this was to ensure that multimedia
applications not destroy the interactive performance of the system. I
think there is a grain (or block) of truth to this explanation: as soon
as you insert big buffers into the network, you’ll start to see bad
latency whether using TCP, UDP or other protocols, and one of the first
places you’ll notice is the UI interaction between users of a media
player and the media server (I’m an old UI guy; trust me when I say that
you start “feeling” latency at even 20ms). Any time they ran Windows on
hardware with big buffers, they had problems; certainly hardware has
supported much higher transmit buffers than makes any sense for most
user’s office or home environments for quite a few years. I suspect
Microsoft observed the bufferbloat problem and, as a simple mitigation
strategy was available to them, took it.

</p>
<p>
Microsoft does not have control of many/most of the drivers their
customers expect Windows to run well on (not true for Mac and Linux),
however. So I suspect that Microsoft and (some of their customers) have
a real headache on their hands, only soluble by updates to a large
number of drivers by many vendors.

</p>
<p>
On the other hand, on 100Mbps ethernet, still the most common bandwidth
ethernet, both Windows XP and Windows 7 ”just worked” as you might hope
with low latency (of order 1ms even while loaded). And Windows XP is
less likely to induce bloated buffers in broadband, though as bittorrent
showed, it still can, and as I’ll explain in details shortly, recent
changes in both web browsers and certain web servers can encourage XP to
fill buffers. I have not experimented with wireless. Please do so and
report back.

</p>
<p>
Alternate explanations and/or confirmations of this hypothesis are
welcome.

</p>
<p>
I do not happen to know the mechanisms, if any, to control driver
buffering size on Microsoft Windows, though it may be present in driver
dialog boxes somewhere.

</p>
<h2>
Why in the world does the hardware now have so much buffering, anyway?

</h2>
<p>
On my Intel Ethernet NIC, the Linux driver’s ring buffer size is 256 by
default: but the hardware goes up to 4096 in size. That’s amazingly
huge. I’ve seen similar sizes on other vendor’s NIC’s as well. I
wondered why. I like the explanation that
<a title="Ted T'so's Wikipedia entry." href="http://en.wikipedia.org/wiki/Ted_T'so" target="_blank">Ted
T’so</a> gave me when I talked to him about bufferbloat a month ago: it
stems from experience he has when he was working for the Linux
Foundation on real time. I think Ted is likely right.

</p>
<p>
It can’t be for interrupt mitigation; most of your benefit is in the
first few packets; similarly for segmentation and reassembly. Even doing
a little transmit buffering can get you into a lot of trouble on
wireless, as I’ll show in a future post. I suppose that interrupt
latency could also be a problem on loaded systems, though this seems
extreme.

</p>
<p>
Ted’s theory is this is a result of the x86 processor’s
<a title="System Management Mode in Wikipedia" href="http://en.wikipedia.org/wiki/System_Management_Mode" target="_blank">SMM
mode</a>. To quote Wikipedia: “<strong>System Management Mode</strong>
(SMM) is an operating mode in which all normal execution (including the
operating system) is suspended, and special separate software (usually
firmware or a hardware-assisted debugger) is executed in high-privilege
mode.” Ted noted there are motherboards/systems out there which go
catatonic for of order one or a few milliseconds at a time; yes, your N
processor chip motherboard consisting of C cores each may crowbar to a
single thread on a single processor for that length of time. The BIOS is
ensuring your CPU cores don’t over heat (you might think there should be
a way to do this at lower priority for things less time urgent, mighten
you?) and important (but not necessarily urgent) tasks. To paper over
latencies and hiccups of that length of time at 1 gigabit you indeed
need hundreds or conceivably small number of thousands of ring entries.
And that’s the size we see in current hardware.

</p>
<p>
Unless someone has a better theory, I like Ted’s.

</p>
<h2>
The General Operating System Problem

</h2>
<p>
We now have commodity “smart” network devices, that may do lots of
features for us, to make the network “go fast” (<em>forgetting that for
many people, operations/second and latency trumps bits per second and
throughput hands down</em>; performance has multiple metrics of import,
not just one). For example, the devices may compute the TCP checksums,
segment the data, and so on; and similarly on the receive side of the
stack. To go fast, we may also be wanting to (and needing to) mitigate
interrupts, so the OS doesn’t necessarily get involved with every packet
transfer in each direction, on server systems (but often not on edge
systems at all). And, as opposed to a decade ago, we now have widespread
deployment of networking technologies that span one or more orders of
magnitude of performance, while still only admitting to a “one size fits
all” tuning.

</p>
<p>
Here’s the rub: these same smart device designs are often/usually being
put into commodity hardware a generation or two later, and the same
device drivers are being used, set up for their use on high end servers.
But the operating environment that hardware is now in is in your laptop,
your handheld device or your router, running at low bandwidth, rather
than a big piece of iron in a data center, hooked up to a network
running at maximum speed. Rather, it is being used in devices that are
being used at a small fraction of their theoretical performance
capability. For example, my gigabit ethernet NIC much more often than
not is plugged into a 100megabit switch,
<a title="Home Router Puzzle Piece One – Fun with your switch" href="http://gettys.wordpress.com/2010/11/29/home-router-puzzle-piece-one-fun-with-your-switch/">with
the results I noted</a>. And, of course, I’m seldom going anything like
the speed of a server on my laptop: at most, I might be copying files to
a disk someplace, and going of order 100Mbps.

</p>
<p>
Even more of a problem is wireless: not only is the bit rate of the
network not a 100Mbps (for 802.11N), or 20Mbps (for 802.11g), but the
bit rate may drop as low as 1 megabit/second. Remember also that those
networks are shared media. If you have a loaded wireless network, the
buffering of the other nodes also comes into play; you may only get 1/10
(or less) of the available bandwidth at whatever rate that wireless
network is operating at (and 802.11 likes to drop its speed to maximize
distance at the drop of a hat). I’ll discuss what happened to OLPC in a
future post, though we also had other problems in our mesh network. So
the effective “goodput” on wireless may easily vary by factors of 100 or
more on wireless, presenting even more of a challenge than for ethernet,
where typically we face a switched network and a factor of 10 in its
performance.

</p>
<p>
In general, I believe that hardware transmit buffer sizes should be kept
as small as possible. ”As possible”, will depend strongly upon the
network media and circumstances. One of the mistakes here, I suspect, is
that the operating system <em>driver</em> implementers, not
understanding that transmit and receive are actually quite different
situations, set the transmit and receive buffering to the same amount.
After all, I’m never going to lose a packet I haven’t transmitted yet;
it’s only receive I could have a problem on. And as I showed previously,
<a title="Whose house is of glasse, must not throw stones at another." href="http://gettys.wordpress.com/2010/12/06/whose-house-is-of-glasse-must-not-throw-stones-at-another/">some
packet drop (or use of ECN) is necessary</a> when congested for the
proper functioning of Internet protocols, and indeed,
<a title="Bufferbloat and congestion collapse – Back to the Future?" href="http://gettys.wordpress.com/2010/12/09/bufferbloat-and-congestion-collapse-back-to-the-future/">for
the health of the Internet overall</a>. And this is indeed be a form of
congestion. Ideally, we should always mark packets with ECN
whenever/wherever congestion occurs, no matter where the excessive
queues are forming.

</p>
<p>
And since the network delays are anywhere from almost zero to several
hundred milliseconds (for planetary paths), the delay/bandwidth product
is also very large, along with the workload of the systems. There is no
single right answer possible for buffering: our operating systems need
to become much more intelligent about handling buffering in general.

</p>
<p>
I certainly do not pretend to have a clue as to the right way to solve
this buffer management problem in multiple operating systems; but it
seems like a tractable problem. That will be fun for the OS and
networking subsystem implementers to figure out, and help keep them
employed.

</p>
<p>
The general challenge for operating systems is we want a system which
both can run like a bandit in the data center, and also work well in the
edge devices. I believe it possible for us to “have it both ways”, and
to “have our cake and eat it too”. But it will take work and research to
get there. In the short term, we can tune for different situations to
mitigate the problem.

</p>
<h2>
Coming Installments

</h2>
<ul>
<li>
After action report of 802.11 network meltdown at OLPC

</li>
<li>
<a title="RED in a Different Light" href="http://gettys.wordpress.com/2010/12/17/red-in-a-different-light/">RED
in a different light</a>

</li>
<li>
corporate and ISP networks

</li>
<li>
<a title="Bufferbloat in 802.11 and 3G Networks" href="http://gettys.wordpress.com/2011/01/03/aggregate-bufferbloat-802-11-and-3g-networks/">802.11
and 3g networks</a>

</li>
<li>
where to from here?

</li>
</ul>
<h1>
Conclusions

</h1>
<p>
Since any number you pick for buffering is guaranteed to be wrong for
many use cases we care about, the general solution will await operating
systems implementers revisiting buffering strategies to deal with the
realities of the huge dynamic range of today’s networks, but we can
mitigate the problem (almost) immediately by tuning without waiting for
nirvana to arrive.

<div class="snap_nopreview sharing robots-nocontent">
<ul>
<li class="sharing_label">
Share this:

</li>
<li class="share-print share-regular">
<a rel="nofollow" class="share-print share-icon" href="http://gettys.wordpress.com/2010/12/13/mitigations-and-solutions-of-bufferbloat-in-home-routers-and-operating-systems/#print" title="Click to print">Print</a>

</li>
<li class="share-custom">
<a href="#" class="sharing-anchor">Share</a>

</li>
<li class="share-end">
</li>
</ul>
<div class="sharing-hidden">
<div class="inner" style="display: none;">
<ul>
<li class="share-twitter">
<div class="twitter_button">
<iframe allowtransparency="true" frameborder="0" scrolling="no" src="http://platform.twitter.com/widgets/tweet_button.html?url=http%3A%2F%2Fwp.me%2FpfzIQ-5O&#038;counturl=http%3A%2F%2Fgettys.wordpress.com%2F2010%2F12%2F13%2Fmitigations-and-solutions-of-bufferbloat-in-home-routers-and-operating-systems%2F&#038;count=horizontal&#038;text=Mitigations%20and%20Solutions%20of%20Bufferbloat%20in%20Home%20Routers%20and%20Operating%20Systems: " style="width:97px; height:20px;">
</iframe>
</div>
</li>
<li class="share-digg">
<a rel="nofollow" class="share-digg share-icon" href="http://gettys.wordpress.com/2010/12/13/mitigations-and-solutions-of-bufferbloat-in-home-routers-and-operating-systems/?share=digg" title="Click to Digg this post">Digg</a>

</li>
<li class="share-end">
</li>
<li class="share-facebook">
<a rel="nofollow" class="share-facebook share-icon" href="http://gettys.wordpress.com/2010/12/13/mitigations-and-solutions-of-bufferbloat-in-home-routers-and-operating-systems/?share=facebook" title="Share on Facebook">Facebook</a>

</li>
<li class="share-stumbleupon">
<a rel="nofollow" class="share-stumbleupon share-icon" href="http://gettys.wordpress.com/2010/12/13/mitigations-and-solutions-of-bufferbloat-in-home-routers-and-operating-systems/?share=stumbleupon" title="Click to share on StumbleUpon">StumbleUpon</a>

</li>
<li class="share-end">
</li>
<li class="share-email">
<a rel="nofollow" class="share-email share-icon" href="http://gettys.wordpress.com/2010/12/13/mitigations-and-solutions-of-bufferbloat-in-home-routers-and-operating-systems/?share=email" title="Click to email this to a friend">Email</a>

</li>
<li class="share-reddit">
<a rel="nofollow" class="share-reddit share-icon" href="http://gettys.wordpress.com/2010/12/13/mitigations-and-solutions-of-bufferbloat-in-home-routers-and-operating-systems/?share=reddit" title="Click to share on Reddit">Reddit</a>

</li>
<li class="share-end">
</li>
<li class="share-end">
</li>
</ul>
</div>
</div>
<div class="sharing-clear">
</div>
</div>
<p class="postmetadata alt">
<small>

This entry was posted on December 13, 2010 at 5:15 pm and is filed under
<a href="http://en.wordpress.com/tag/bufferbloat/" title="View all posts in Bufferbloat" rel="category tag">Bufferbloat</a>,
<a href="http://en.wordpress.com/tag/networking/" title="View all posts in Networking" rel="category tag">Networking</a>,
<a href="http://en.wordpress.com/tag/puzzle/" title="View all posts in Puzzle" rel="category tag">Puzzle</a>.
You can follow any responses to this entry through the
<a href='http://gettys.wordpress.com/2010/12/13/mitigations-and-solutions-of-bufferbloat-in-home-routers-and-operating-systems/feed/'>RSS
2.0</a> feed.\
You can <a href="#respond">leave a response</a>, or
<a href="http://gettys.wordpress.com/2010/12/13/mitigations-and-solutions-of-bufferbloat-in-home-routers-and-operating-systems/trackback/" rel="trackback">trackback</a>
from your own site.

</small>

</p>
</div>
</div>
<div id="wpl-likebox">
<div id="wpl-button">
<a href='http://gettys.wordpress.com/2010/12/13/mitigations-and-solutions-of-bufferbloat-in-home-routers-and-operating-systems/?like=1&amp;_wpnonce=b1bdd34cdc' title='I like this post' class='like needs-login' rel='nofollow'><span>Like</span></a>

</div>
<div id="wpl-count">
One blogger likes this post.

</div>
<div id="wpl-avatars">
<a href="http://gravatar.com/webhat" title="webhat"><img src='http://0.gravatar.com/avatar/4eacee3eac6699a3050af074bc5d90ed?s=35&amp;d=&amp;r=G' class='avatar avatar-35' alt='webhat' width='30' height='30' />
</a>

</div>
</div>
<!-- You can start editing here. -->
<h3 id="comments">
31 Responses to “Mitigations and Solutions of Bufferbloat in Home
Routers and Operating&nbsp;Systems”

</h3>
<ol class="commentlist">
<li class="comment even thread-even depth-1" id="comment-1623">
<img alt='' src='http://0.gravatar.com/avatar/86f87d633decc5cb62627232a45d94cf?s=32&amp;d=&amp;r=G' class='avatar avatar-32' height='32' width='32' />
<cite>Justin Smith</cite> Says: <br />

<small class="commentmetadata"><a href="#comment-1623" title="">December
13, 2010 at 6:50 pm</a> |
<a class='comment-reply-link' href='/2010/12/13/mitigations-and-solutions-of-bufferbloat-in-home-routers-and-operating-systems/?replytocom=1623#respond' onclick='return addComment.moveForm("comment-1623", "1623", "respond", "360")'>Reply</a>
</small>
