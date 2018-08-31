---
title: ECN-Sane Project
date: 2018-08-24T15:38:14
lastmod: 2018-08-24T15:38:14
type: wiki
aliases:
    - /ecn-sane/wiki/Wiki
---

# About the ecn-sane project

This project is started in the hope that a clear path forward for ecn enablement across the edge of the Internet will emerge. 

Neither the original codel or pie aqm research covered ECN.

Howerver, 'fq_pie' and 'fq_codel', enable ecn by default, because, in
*very* limited tests in 2012, it seemed to work. 

But ECN'd behaviors are observably different than drop, and different
AQMs treat it differently. 

Pie starts dropping ecn enabled packets once the drop probability cracks 10.
RED behaves similarly.

Our same limited tests showed codel alone to be somewhat ineffective
against ecn, and in both pie and codel's single queue implementations
we left it disabled by default.  [wiki/codel/Cake](sch_cake) developed a more refined
approach to ecn management. The [sqm-scripts](FIXME)- enable ecn for inbound
universally and disable it for outbound. Inconsistencies in ecn
behavior abound in both AQMs and TCPs.

Much of this project will be focused on analyzing and reducing any
additional congestion potentially caused by modern tcps with ecn
enabled.

We expect much work to take place on the mailing list. Like all
bufferbloat.net lists, ecn-sane is an open mailing list, however,
given the level of religious advocacy of ecn elsewhere on the Internet,
it has [several policies](rules) that are new to bufferbloat.net.

People will be banned, after 3 warnings, from the email list, for the following reasons:

* Unwillingness or inability to repeat experiments against modern versions of cubic, bbr and reno
* Non-publication of sufficient code required for others to repeat your experiments
* Unbridled advocacy OR outright hatred of ecn

Additionally:

* Project members should identify themselves as part of the [red, blue, yellow and purple teams](rules)

Scientific skepticism of [both negative and positive results](https://conferences.sigcomm.org/sigcomm/2014/doc/slides/137.pdf) is utterly required here.

We are hoping that these rules here are sufficient to keep the noise level 
low, and to make progress forward on this sensitive topic.

# ECN-Sane Project Plans

## Explore the possible negative effects of a partially or fully ecn-enabled internet on

* Gaming, voice, DNS traffic
* Explore improvements to voip (higher bit resolutions, 2.5ms sample rates, etc)
* Analyze Unresponsive senders
* ECN-enabled DDOS attacks
* What does it do VOIP MOS score
* Side effects on routing protocols (such as Babel, ISIS and ARP)
* Effects of deploying it on protocols such as bittorrent
* Discover what of rfcXXXX holds in today's IW10 environment

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

