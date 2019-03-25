---
title: Dave Taht's Take on TCP
date: 2019-03-21T15:38:14
lastmod: 2019-03-21T15:38:14
type: wiki
tags: ecn-yellow

---

# Dave Taht's take on TCP

TCP is done. It's baked. It's finished. With the arrival of BQL,
TSQ, and pacing, there is very little left we
can do to improve it, and we should move on to improving new
transports such as QUIC which have option space left. However,
 a recent development has caused me to change my mind.

Ever since [RFC6013](https://tools.ietf.org/html/rfc6013) failed in favor of tcp
fast open, I'd given up on tcp. RFC6013 was a lousy rfc in that it didn't
make clear its best use case was in giving dns servers a safe and fast
way to use tcp, which would have helped reduce the amount of DDOS and
reflection attacks, speed things up, and so on. It wasn't until I had
a long discussion with Paul Vixie about this use case and worldwide
problem with dns that I understood it's intent to add a good stable
3way handshake to dns was so good.... and by then it was too late.

Instead, tcp fast open was standardized for the limited (IMHO) use case
of making web traffic better. Web traffic has a terrible interaction
with TCP, in that it tends to start up 6 or more simultaneous
connections and slam the link with stuff in slow start simultaneously.
Other standards that I opposed, like [IW10](https://tools.ietf.org/html/draft-gettys-iw10-considered-harmful-00)
, also got adopted, and
we (as part of the cake project) tried to get an AQM (cobalt) that
responded faster to stuff in slow start. Which we succeeded at, and
that paper is progress, but it's still not good enough.

It makes me really crazy that seemingly all the other TCP researchers in the
world tend to focus on improving TCP behavior in congestion avoidance
mode - because the statistics are easy to measure! - instead of
focusing on the 95% of flows that never manage to get out of slow
start. Yea, it's hard to look at slow start. That's why we've been
looking at it hard for 5+ years in the bufferbloat project - trying to
get linux, flent, irtt, to be able to look in detail at sub 4ms
intervals, among other things.

There are so many other problems with TCP as a transport - it requires
a stateful firewall for ipv4 + nat, and more stuff than I have time to
go into today...

One item off that long list:

QUIC and Wireguard have a really nice 1 RTT reconnect over crypto
time. I like it a lot. I have not had time to poke much into the DOH
working group at the ietf, but my take on it was that we needed to
make dns better, not replace it.

[1] Up until about 6 months ago, I really felt that we couldn't
improve tcp anymore. DCTCP was a dead end. However the SCE idea makes
it possible to have selectable behaviors on the receiver side -
notably, a low priority background transport application (for
backups/bittorrent) can merely overreact to SCE markings by sending
back ECE to the tcp sender thus getting them to back off faster and be
invisible to other applications. Or something more complicated (in
slow start phase) could be used. ACCUECN also seemed feasible. And
dctcp like approaches to another transport than tcp seemed very
feasible.

But to me, the idea was that we'd improve low latency applications
such as gaming and videoconferencing and VR/AR with SCE, not "fix"
tcp, overall. Goal in life was to have 0 latency for all flows - if it
cost a little bandwidth, fine - 0 latency. The world is evolving to
"enough" bandwidth for everything, but still has too much latency. The
whole l4s thing conflating the benefits low latency with an
ecn-enabled tcp has makes me crazy because it isn't true, as loss is
just fine on most paths - lordy I don't want to go into that here,
today. loss hurts gaming and videoconferencing more.

Another ietf idea that makes me crazy is the motto of "no host
changes" in homenet, and "dumb endpoints" - when we live in an age
where we have quad cores and AI coprocessors in everybody's hands.

The whole QUIC experiment shows what can be done when you have smart
endpoints, along with a network that is as dumb as possible, but no
dumber.

See also: [Dave Taht's take on ECN](dtaht_ecn_editorial).

