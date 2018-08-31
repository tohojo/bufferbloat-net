---
title: Dave Taht's Stance on ECN
date: 2018-08-31T15:38:14
lastmod: 2018-08-24T15:38:14
type: wiki
tags: ecn-yellow

---

# Dave Taht's take on ECN

When it comes to ECN, I am firmly on the yellow team: I'm *chicken*.

I just used rigorous argument and moral authority on what is now probably the worlds largest active ecn in the edge deployment, to [block systemd's attempt at universal enablement in Linux](https://github.com/systemd/systemd/issues/9748). As an accidental co-author of what is now the largest edge-user ecn-enabled fq + aqm deployment in fq_codel, the sqm-scripts, and the newest implementation in the ath9k and athk wifi code... and now sch_cake... I lose sleep over the ecn component only.

I have a ton of data on it. It's mixed.

What I see with lots of ECN traffic on a fq_codel'd link is that other valuable packets are delayed (slightly) or lost and am always saying "ECN has mass" to anyone that will listen. This is made up for by nearly eliminating retransmits, however ECN'd flows can bloat up the link and inflate RTTs enormously when I feel they shouldn't. ECN is a huge win for interactive tcp traffic, which is why apple adopted it (and - helpfully - their reno tcp is far less aggressive than linux cubic). I worry about lockout at low speeds and that one day we'd have to mark all packets of all types of flows (including voip and dns) as ecn capable, *unless tcps evolve appropriately towards an agreed upon response curve*.

One really interesting side-effect of ecn on is that fq_codel, running locally on the server, can self congest and start marking packets locally, thus regulating the behavior of the server better after a rtt.(try 128 flows coming out of a short path at a gbit). But local fq_codel induced loss (currently) on the other hand is sometimes not lost there but signals the local stack to immediately to reduce cwnd without actually losing the packet. Others might view either behavior as a problem and prefer that that server serve 100s more flows at ever increasing self inflicted local delay (as sch_fq does) until you run out of cpu. 

I certainly wish we'd come up with a more robust response to overload in fq_codel for ecn, as currently a malicious ecn sender, or too many ECN'd flows can push fq_codel to its memory limit before being dropped robustly. (pie drops ecn at overload). fq_codel (and now sch_cake) can continue to evolve as can everything else of course!

In my mind ECN MAY be a good idea at very short rtts(sub 2ms), and IS good very long ones(>150ms), for interactive traffic. It's good for doing things like protecting video iframes from loss. I use it to protect routing babel protocol packets from being dropped. I helped put it into mosh. Etc. I think the use cases where it is actually needed generally are far more limited than most think.

Others (in the bbr, l4s, dctcp communities) want to change the definition of ECN to mean a multi-bit rate reduction and obsolete rfc3168, where a loss is equivalent to a mark and the recommended rate reduction is 1/2. But: fq_codel, pie, red, and all other deployed ecn capable aqm systems essentially implement rfc3168 behavior and it's what apple's tcp - and linux cubic - and bsd's - and windows - general deployment expects. I had hoped with wider deployment of AQMS that dealt with ECN at all properly that we'd see more servers also enabling it... and we'd see TCPs evolve to treat aqms doing multiple ecn marks per rtt yet *per rfc3168* more sanely than they do today as it is a stronger signal of congestion than loss.

Instead... well, see BBR, which currently more or less ignores packet loss on its quest to own the link, and currently has no ecn response. There's a thread on the bbr list that talks about how they are leaning towards not respecting that rfc. The L4S folk vehemently defend the idea that some form of dctcp can run outside the datacenter, based on bigbuckbunny based demos, combined with a custom and patented AQM, never tested against wifi or 3g, who create a lot of noise in the IETF, where I am dubious of the accuracy required in ACKs in asymmetric networks, and against other forms of real traffic, among other things.

I've run most of the the DCTCP based stuff over simulations and over the internet, and thus far, fq-codel's basic response has been adaquate for low numbers of flows. I've thus spent the last several years avoiding thinking about ECN at all.

Nearly every time I've quit smoking, an ecn debate started me up again, and instead of continuing to deal with it, I left the ietf, leaving the folk there to plot amongst themselves with no actual deployment to deal with. I'm so frustrated with the "make tcp go fast at any cost" people that periodically I fiddle with something called tcp-fu (for users), that has an adjustable response curve to fq_codel's ecn marks from background (torrent-like) to "gentle", rather than "rabid". Despite the enormous success of fq_codel and BQL in eliminating bufferbloat and network latency - I feel bad about [essentially obsoleting the entire field of LPCC with our work on fq_codel](https://perso.telecom-paristech.fr/drossi/paper/rossi14comnet-b.pdf) and would like to do something about it.

I used to take glee in how fq techniques generally beat dctcp's, even in the datacenter... at how even the guy that invented dctcp moved onto fq...

I really resented repeated attempts to closely couple AQM deployment to ECN deployment. DOCSIS-PIE shipped without it. And FQ+AQM alone led to nearly two orders of magnitude reduction in latency under load across the internet, and I wished everyone could get behind that. Instead the IETF AQM mailing list devolved into an endless bikeshed, and I ended up calling for the closure of that working group rather than continue to deal with it. It still took 6 years to get fq_codel - the first solution proposed - through the IETF process to become RFC8290, and I still approve - even after all that time stuck within the IETF process - to consider that and [all the other products of the working group](https://tools.ietf.org/wg/aqm/) - to be "experimental" in scope until we saw more widespread deployment.

I once got so frustrated with the ECN advocates that I suggested [they get a sysadmin drunk enough at their university to deploy it fully](https://www.ietf.org/mail-archive/web/aqm/current/msg01047.html). None ever did. I believe in early adoptors, in knowledgable users and limited deployments along the edge to get real world data, in a careful deployment.

ECN is the wet paint of the congestion control universe. You have to touch it, feel it, use it, explore it, day and day out - as I have for over 5 years - to worry about the long term effects on the health of the Internet, as I do.


