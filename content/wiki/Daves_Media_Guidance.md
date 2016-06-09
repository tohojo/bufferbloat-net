
---
title: Daves_Media_Guidance
date: 2015-09-28T11:11:19
lastmod: 2015-10-15T09:33:20
---
Dave Taht's Media Guidance
==========================

{{&gt;toc}}

With the upcoming publication of the [CeroWrt letter to the FCC on the
Wifi lockdown
issue](http://fqcodel.bufferbloat.net/~d/fcc_saner_software_practices.pdf)
...

While I do not wish to enforce any rules on the 260 signers, these are
the guidelines I intend to follow, for myself, and have a bit of detail
below on how I, personally would like to interface with others... I
figure this doc should be split in two, and my personal stuff broken
out.

To make our points it would be helpful for anyone answering a press or
other inquiry, to try first to make the inquirer understand the problems
we face on fixing the internet from our perspectives, be it performance,
security, reliability, or whatever.

Among other things, we have asked the FCC's chief engineer to discuss
the issues with us [directly and publicly this
friday](https://plus.google.com/u/0/events/cp7g87eq2g5fde8b8i5bn2p8oo0)
.

Media inquiries email
---------------------

I have set up an alias, media@bufferbloat.net to handle media inquiries.
Feel free to direct media requests for access to signers of the FCC
letter there, and we'll handle it.

Still feel free to do your own outreach, blogging, tweeting, etc.

But, if you get into trouble on a question, PLEASE don't guess. Try to
ask the appropriate questions of the public bloat, make-wifi-fast or
cerowrt-devel mailing lists, cc-ing the questioner. Far too few in the
media use these as effectively as we do. Or forward the request to
media@bufferbloat.net and we'll handle it.

Reaching Dave
-------------

I can generally always be reached best via email, or google hangout.
Being partially deaf leads me to vastly prefer situations where I can
have high quality audio, or read lips, either one on one, or in a
videoconference. f2f, email or network chat are way better than a
conventional phone call or mass meeting.

My personal contact info:

email or hangout: dave.taht@gmail.com\
webrtc: https://appear.in/davetaht\
phone: +46 54 700 1161

I do have a skype account (davetaht) but best - always! - to reach me
first via email to set up a good time.

I am presently a guest researcher at karlstadt university, in sweden,
after a stay at the lincs, in paris, this summer. Prior to that I was
contracting for gfiber part time, but mostly working on getting
[make-wifi-fast off the
ground](http://www.bufferbloat.net/projects/make-wifi-fast/wiki/Wiki)

I plan to always show bufferbloat in action
-------------------------------------------

In doing an interview, first, always, make the interviewer open a new
browser window (chrome or firefox), and run
http://www.dslreports.com/speedtest/ - and send you his/her result!

The odds are extremely good that they will get a rating of B or worse
for bufferbloat. This leads naturally to explaining that **we fixed
that**, with some [new
theory](http://www.bufferbloat.net/projects/codel) , and **just
software** making possible better and more consistent voip, gaming, web,
and videoconferencing performance... and to the question, of, how, then,
do you upgrade or retrofit a billion devices to use the fixes, with
broken millions more shipped every day, with FCC approval?

This is a [chart of the worldwide scope of the bufferbloat problem on
uplinks](http://www.dslreports.com/speedtest/results/bufferbloat?up=1)
Downlinks are not as bad, but still bad. Everybody running the results
of the CeroWrt project's code is usually at 30ms or less of induced
delay. Everyone else can have delays measured in **seconds**. What a
productivity loss! What a bad fate for the future for voip and
videoconferencing!

You can also a [breakdown by
ISP](http://www.dslreports.com/speedtest/results/isp) , and other
drill-downs.

The results of this test are particularly devastating if they run this
test while in a video conference with you. If they don't get a bad
result, wave hands and suggest they try it elsewhere, in a coffee shop,
at home, etc.

The odds are certain that in several of those cases, bad network
behavior will happen, which you can talk to. How do you get added the
mere 50 lines of BQL code needed to the DSL blob firmware on 100s of
millions of devices? Or the 1000 lines of fq\_codel or cake to other
hardware, or the fairly tiny number of additional changes to wifi blob
firmware - to make it perform so much better than it ever did before.
This is a truly tiny amount of code to add to everything when compared
to the millions required to make it work in the first place.

In my experience **normal users** care a hell of a lot more about
performance than security, and most of the public security discussion is
security theater. Network performance **matters**.

On "open source" vs "public, maintained, and frequently updated source"
-----------------------------------------------------------------------

Throughout the letter you will only see open source mentioned once, and
specifically that we ask that the FCC "review and rescind" any rules
that interfere with open source best practices. We are not requiring
open source here, but asking that rules that make using open source
techniques difficult, or impossible, be reviewed and fixed. The core bit
of code we care about seeing made public - the "binary blob" at the
lowest level of the device driver or it's onboard firmware - is as big a
PITA for open source network stacks built on top of that blob as those
using more closed ones.

"open source' as we well know, since heartbleed, does not always get
**maintained**, automatically. There are far too maintainers and only a
[few orgs](http://icei.org) dedicated to maintenence. I (speaking on
behalf of the CeroWrt project and **not** all the 260 signers) do not
care what license be slapped on the firmware sources, only that the code
be **human-readable, public, maintained, and regularly updated**.

Sure, doing that as open source as per the OSI definitions would be
smart, but not having it be public, AND maintained is the far larger
problem.

if someone translates what you are saying into an open source rant, rant
back about getting the code public, maintained, etc.

Security and safety
-------------------

While I am of course mostly focused on the bufferbloat issue, there are
also all the public safety issues induced by un-updatable firmware, not
just on the internet but in cars and the like. Although the 5 mandates
in the letter are buried deep within it, those are the most important
parts of the letter to the FCC, as it is out of the box thinking that
needs to be considered by all regulators of software and hardware - and
is what needs to be discussed with the public and regulators. The
mandates are nearly done, and we will probably have to produce a faq,
and ultimately pursue legislation on the scale of the original clean air
and water act to get anywhere.

In the past 5 years, I have spent vastly more time dealing with the
larger problems of secure updates, ipv6, and system security in general
than I have actually spent on make-wifi-fast or bufferbloat. My answer
to these other problems are often hard to describe... for example my
answer to the persistent stack smashing and return oriented programming
attacks is to sink what spare time I can into helping fund and finalize
[millcomputing](http://millcomputing.com/docs/) 's new cpu - and I do
wish we had not needed to address all these also in the context of the
original CeroWrt project! We'd have fixed wireless-n by now!

Still, I am shifting all security related questions to someone(s) else,
with paul vixie taking the lead with the hopeful assistance of jim
gettys, nick feamster, bruce schneir, and others. If I thought about the
security nightmares of heartbleed, dnschanger, the moon worm, and the
100s of millions of dollars being spent to deal with DDOS and other
forms of attack, more than I already do, I would cease to be able to get
out of bed in the morning.

On wifi, david reed is our main go-to guy when going deep into EE-land.
andrew mcgregor is also good as is david lang, but at more practical
land. I'm not as good at the EE stuff, but better on all of
make-wifi-fast's stuff we outlined in the appendexes to the
make-wifi-fast design document mentioned in the letter.

Unburying the 5 mandates from the [fcc letter](http://huchra.bufferbloat.net/~d/fcc_saner_software_practices.pdf)
-----------------------------------------------------------------------------------------------------------------

> We advocate: that rather than denying users the ability to make any
> changes to the router whatsoever, router vendors be required to open
> access to their code (especially code that controls RF parameters) to
> describe and document the safe operating bounds for the software
> defined radios within the Wi­Fi router. In this alternative approach,
> the FCC could mandate that:

> 1\. Any vendor of SDR, wireless, or Wi­Fi radio must make public the full
> and maintained source code for the device driver and radio firmware in
> order to maintain FCC compliance. The source code should be in a
> buildable, change controlled source code repository on the Internet,
> available for review and improvement by all.

> 2\. The vendor must assure that secure update of firmware be working at
> shipment, and that update streams be under ultimate control of the owner
> of the equipment. Problems with compliance can then be fixed going
> forward by the person legally responsible for the router being in
> compliance.

> 3\. The vendor must supply a continuous stream of source and binary
> updates that must respond to regulatory transgressions and Common
> Vulnerability and Exposure reports (CVEs) within 45 days of disclosure,
> for the warranted lifetime of the product, or until five years after the
> last customer shipment, whichever is longer.

> 4\. Failure to comply with these regulations should result in FCC
> decertification of the existing product and, in severe cases, bar new
> products from that vendor from being considered for certification.

> 5\. Additionally, we ask the FCC to review and rescind any rules for
> anything that conflict with open source best practices, produce
> unmaintainable hardware, or cause vendors to believe they must only ship
> undocumented “binary blobs” of compiled code or use lockdown mechanisms
> that forbid user patching. This is an ongoing problem for the Internet
> community committed to best practice change control and error correction
> on safety ­critical systems. This path has the following advantages:

> ● Inspectability: ­ ​Skilled developers can verify the correctness of
> software drivers that are now hidden in binary “blobs”.

> ● Opportunity: for innovation ­ ​Many experiments can be performed to
> make the network “work better” without affecting compliance.

> ● Improved spectrum utilization: ­ ​A number of techniques to improve
> the use of Wi­Fi bands remain theoretical possibilities. Field trials
> with these proposed algorithms could prove (or disprove) their
> utility, and advance the science of networking.

> ● Fulfillment of legal (GPL) obligations: ­​ Allowing router vendors
> to publish their RF­ controlling source code in compliance with the
> license under which they obtained it will free them from the legal
> risk of being forced to cease shipping code for which they no longer
> have a license.

> Requiring all manufacturers of Wi­Fi devices to make their source code
> publicly available and regularly maintained, levels the playing field
> as no one can behave badly. The recent Volkswagen scandal with
> uninspected computer code that cheated emissions testing demonstrates
> that this is a real concern.

CeroWrt vs Make-wifi-fast
-------------------------

CeroWrt was a research project. When we got stability, we pushed all the
innovations up into linux and openwrt and elsewhere. fq\_codel, in
particular has been widely adopted across the entire industry.

make-wifi-fast as formerly structured has been my attempt to simplify
things enough to just focus on fixing wifi, as most of everything else
is now moving along smartly, but I am increasingly expecting we will
have to do another cerowrt (cerowrt v3!) scale project to get everything
right. My problem with doing that is that much of the theory work is
basically done and what remains is a "mere matter of engineering", the
cost estimate for which was in the millions, for which we only have
thousands. (I personally have support from the university of karstadt
and two small comcast research grants coming in next week - but it does
not compare to the scope of the task).

I do not have sufficient funding for a f/t build engineer, which is
partially why my [patreon page exists](https://www.patreon.com/dtaht) -
but also, for the last year, I was pouring every spare dime and all the
time I could into the theory bits of make-wifi-fast, working only part
time at my now former job a gfiber, and I do, keep hoping that some day,
the world will look up and be grateful for wifi enough for normal folk
to want to see it made better... despite the seeming desires of
governments and carriers to ruin it further.

I have slept on a [lot of great couches](http://esr.ibiblio.org/?p=4162)
during [this project](http://esr.ibiblio.org/?p=4566) , but I am not
scaling anymore inside my tight constraints, and huge demands on my
time.

Using social media
------------------

I am generally bad at using social media, but this time I intend to
tweet, g+, and facebook, and I encourage people to do the same, as\
well as post links to other valuable material such as the arstechnica
and wired articles. I don't know what hashtag to use: \#savewifi ?

Please feel free to point others at my old blog or
[g+](https://plus.google.com/u/0/107942175615993706558/posts) pages, but
I do tend to treat [my facebook](https://www.facebook.com/dtaht) as more
personal and private and ask that only genuine friends (and everyone
directly in the cerowrt/bufferbloat efforts I consider a friend by now,
do drop in!) try to friend me there.

Be yourself
-----------

People that I know well and trust keep telling me to just be myself. I
keep explaining to them that for every public appearance I make on
whatever subject I'm talking about, I spend weeks under the bed working
through every possible question and response, I always end up rewriting
the entire talk at 2am the previous night, and am a wreck afterwards for
weeks, also. This note here is basically the kind of stuff I usually
write for myself over the course of those weeks.... only usually it's
pages and pages longer!

... more notes to be added here ...

Avoid other politics
--------------------

Lastly, I really hate politics. I'd rather run the bufferbloat project,
(and write code once in a while!), and play piano, but this latest
outrage finally pushed me over the edge, (after two years of trying to
free up any 802.11ac firmware to work with)to where I am willing to go
to Washington, hand out routers, and explain the basics of how networks
really work and software engineering in front of the FCC and on the
floor of Congress, or if I have to, standing outside with guitar and
picket sign.

In the near term at least, I am not going to answer any questions about
my religion, political parties, or any of my personal background\
outside of the issues at hand. People that want to learn some of my
other views can read the 15 years of history [on my old blog, starting
here](http://the-edge.blogspot.se/2002_06_09_archive.html#77710440) . I
have a lot of stuff in the period 2002-2006 that was quite interesting
in now current contexts. (I am not going to revise a word of although I
do regret quite a few things), and even after reading those many may
remain confused by my usage of irony, sarcasm or humor, and I would
prefer people ask questions of ideas in my old material rather than take
them as givens.

In particular, I tracked the Ron Paul campaign for a while, but am not
by most measures, a libertarian. I have long believed that governments
make (functional or dysfunctional) markets possible, and I have no idea
to what party or vein of thought that belongs to!? I go where the data
takes me. Is there a political party for that?

What I was actually fascinated with, at the time (and since), was how
mass media attempts to wedge thinking into an A or B choice, both often
based on misinformation, or a tiny slice of the wrong part of the
problem. Which is what is happening here on so many technology fronts...

Being someone that always thinks out of the box, and perpetually aware
of or trying to create thousands of other choices, I have striven my
whole life to get people to escape simple frameworks like that, and use
critical thinking and conversations with conflicting thinkers to achieve
consensus solutions and clarity.

Choosing to always work on constructive safety and performance enhancing
things for the internet is how I cope with the endless\
barrage of scary clueless stupidity coming from elsewhere across the
social, corporate and political spectrum.

If I didn't have the skills and intelligence to persist at that,
sometimes at great personal and financial cost, I would have despaired
long ago, and worked harder on means for humanity to leave the planet
than I already have.

I still might sit down and compile answers to a few basic questions
about myself, and I'll try to be amusing about it. I don't think anyone
groks why I call myself a fugi chef on g+ for example....
