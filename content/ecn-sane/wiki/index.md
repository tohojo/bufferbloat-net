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

Neither the original codel or pie aqm research covered ECN. fq_pie and fq_codel,
enable ecn universally, because, in limited tests, it seemed to work.

Pie's starts dropping ecn enabled packets once the drop probability cracks 10.

The same limited tests showed codel alone to be somewhat ineffective against ecn.
sch_cake developed a more refined approach to ecn management. 

Much of this work will be focused on reducing the additional congestion potentially caused by modern tcps with ecn enabled.

ecn-sane is an open mailing list, however, given the level of religeous advocacy of ecn
elsewhere on the Internet it has several policies that are new to bufferbloat.net.

People will be banned, after 3 warnings, from the email list, for the following reasons:

* Unwillingness or inability to repeat experiments against modern versions of cubic, bbr and reno
* Non-publication of sufficient code required for others to repeat your experiments
* Unbridled advocacy OR outright hatred of ecn
* Project members will identify themselves as part of the red, blue, yellow and purple teams

Scientific skepticism of both negative and positive results is utterly required here.

We are hoping that these rules here are sufficient to keep the noise level 
low, and to make progress forward on this sensitive topic.

# This project will:

## Explore the possible negative effects of a partially or fully ecn-enabled internet on

* Gaming, voice, DNS traffic
* Explore improvements to voip (higher bit resolutions, 2.5ms sample rates, etc)
* Unresponsive senders
* ECN-enabled DDOS attacks
* What does it do VOIP mos score
* Side effects on routing protocols (such as Babel, ISIS and ARP)
* Effects of deploying it on protocols such as bittorrent

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
* dynamically reducing mss size at cwnd 2
* Treating an ecn mark even more strongly than loss or reordering (reducing cwnd growth as either would)
* exponential & cubic backoff verses strict AIMD
* Initial spreading for IW10 based ecn transports
* Improving packet pacing to cope with sub cwnds
* a setsocket option to selectively enable ecn
* explore dctcp behaviors on unreliable, jittery networks such as wifi
* explore behaviors against ack-filters and random ack drop

## Explore improvements to existing deployed AQMs that more or less follow rfc3168

## Create repeatable experiments

##  Create dual-licensed implementations of alternate AQM proposals such as l4s and dualQ

* Attempt to incorporate working ideas from these proposals in pie, codel, fq_codel, and fq_pie

