---
title: ECN-Sane Project
date: 2018-09-03T15:38:14
lastmod: 2018-09-03T15:38:14
type: wiki
aliases:
    - /ecn-sane/wiki/Wiki
---

# About the ecn-sane project

As the accidental co-authors of what may well become the world's largest ECN-enabled AQM deployment, our ecn-sane project is started in the hope that a clear, safe, sane path forward for ECN enablement across the edge of the Internet will emerge. 

## What is ECN?

[Explicit Congestion Notification](https://en.wikipedia.org/wiki/Explicit_Congestion_Notification) is a means to do network congestion control
without dropping packets. 

## Why are we concerned about it?

Neither the original codel or pie AQM research covered ECN.

Howerver, the fair queueing variants of these algorithms, the 'fq_pie' and 'fq_codel' qdiscs enabled ECN by default, because, in
*very* limited tests by bufferbloat.net members in 2012, it seemed to work well. 
FQ_Codel, in particular, is in increasingly wide deployment. We've long encouraged individual users to try it out... and then, in 2017... Apple enabled it universally across their devices and stacks.

ECN'd behaviors are observably different than drop, and different
AQMs treat it differently.  The pie algorithm starts dropping ecn enabled packets once the drop probability cracks 10. RED behaves similarly. Codel does not drop until it runs out of packet space. 

Our limited tests showed codel alone to be somewhat ineffective
against ECN, and in both pie and codel's single queue implementations
in Linux we left it disabled by default.  [Cake](/codel/wiki/Cake)
developed a more refined approach to ECN
management. The [sqm-scripts](https://github.com/tohojo/sqm-scripts)
enable ECN for inbound universally and disable it for outbound. Our
[FQ_Codel implementation for WiFi](https://www.usenix.org/system/files/conference/atc17/atc17-hoiland-jorgensen.pdf), now shipping in quantity millions, enables it
universally. Inconsistencies in ECN behavior abound in both AQMs and
TCPs.

Much of this project will be focused on analyzing and reducing any
additional congestion caused by modern protocols with ecn enabled, as
well as examining potential side-effects on other protocols.

We expect much work to take place on the mailing list. Like all
[bufferbloat.net lists](https://lists.bufferbloat.net), ecn-sane is an open mailing list, however,
given the level of religious advocacy of ecn elsewhere on the Internet,
it has [several policies](rules) that are new to bufferbloat.net.

People will be banned, after 3 warnings, from the email list, for the following reasons:

* Unwillingness or inability to repeat experiments against modern versions of cubic, bbr and reno
* Non-publication of sufficient code required for others to repeat your experiments
* Unbridled advocacy OR outright hatred of ecn

Additionally:

* Project members should identify themselves and flag experiments as part of the [red, blue, yellow and purple teams](rules), but it is not required. 

Scientific skepticism of [both negative and positive results](https://conferences.sigcomm.org/sigcomm/2014/doc/slides/137.pdf) is utterly required here.

We are hoping that these rules here are sufficient to keep the noise level 
low, and to make progress forward on this sensitive topic.

# ECN-Sane Project Plans

## Explore the possible negative effects of a partially or fully ecn-enabled internet on

* Gaming, voice, and DNS traffic
* Explore improvements to voip (higher bit resolutions, 2.5ms sample rates, etc)
* Analyze Unresponsive senders
* ECN-enabled DDOS attacks
* What does it do VOIP MOS scores?
* Side effects on routing protocols (such as Babel, ISIS and ARP)
* Effects of deploying it on protocols such as bittorrent
* Discover what of rfcXXXXes holds in today's IW10 environment

## What new can be accomplished by constructive use of ECN?

* QUIC
* MFTP
* DCCP
* ECN for iframes (NADA, redux)
* Can low priority congestion control be made to work again?

## Explore constructive means of coping with ECN for traditional UDP applications

* defensive measures for an overwhelmingly ecned network
(an example would be to ecn mark two out of five voip packets)

## Explore fixes for tcp cubic, reno, and BBR and what other TCPs may apply
 
* Recognising "loss and mark" as an even stronger signal than either
* Dynamically reducing mss size at cwnd 2
* Treating an ecn mark even more strongly than loss or reordering (reducing cwnd growth as either would)
* Exponential & cubic backoff verses strict AIMD
* Initial spreading for IW10 based ecn transports
* Improving packet pacing to cope with sub cwnds
* Explore dctcp behaviors on unreliable, jittery networks such as wifi
* Explore behaviors against ack-filters and random ack drop

## Other sub-projects

* A setsocket option to selectively enable ecn
* Explore improvements to existing deployed AQMs that more or less follow rfc3168
* Create repeatable experiments
* Create dual-licensed implementations of alternate AQM proposals such as l4s and dualQ
* Attempt to incorporate working ideas from these proposals in pie, codel, fq_codel, and fq_pie.

