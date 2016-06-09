
---
title: Bobbie
date: 2015-04-14T07:57:48
lastmod: 2015-05-19T12:31:51
---
Bobbie
======

This is a placeholder. Dave Täht writes this brief intro to Bobbie in
http://www.bufferbloat.net/projects/cerowrt/wiki/Wondershaper\_Must\_Die

     ## I have come to understand that we can, actually make better policers now, 
     ## and that inbound shaping is not the answer to all things. I call the core idea "bobbie" 
     ## as that's what the unarmed police in England are called, and as it uses ideas from fq_codel that
     ## will make the actual rate "bob" up and down, in a kinder, gentler fashion, hopefully
     ## lighter weight than shaping, and support ECN - so it doesn't need to shoot packets, just tap them.
     ## That said, I despair of even writing it, given that where it needs to deploy is in places
     ## that linux does not currently touch.

To try and explain the (as yet unimplemented) idea better: Codel uses
control theory principles - measure, do something, wait, measure, do
something else against the observed delay in the flow(s).

Bobbie would also use control theory but instead of aiming for a target
delay, aim for a target rate. A rate, unfortunately, is two values-
data/interval, and we would probably have to use two estimators for the
appropriate interval (one slow - say 200ms - one fast - say 20ms) to get
a smoothed rate, and furthermore account for all data sent in excess of
the setpoint in order to "bob" below the setpoint long enough to clear
the backlog in a shaper or policer upstream.

The principal problem that has to be solved is that when you are trying
to hold inbound rate limits below what the upstream shaper is limited
to, that a burst can overwhelm the aqm algorithms, leading to buffers
accumulating, still, in the upstream shaper, that are delivered at the
base rate. The differential between the upstream rate and the locally
shaped rate (say, 10%) is not enough to get the upstream buffers to
drain, RTTs grow, and the aqm is never able to reduce the rate to it's
set rate. The local policer or shaper has to "bob" down below it's set
rate for long enough to fully account for all the accumulated data in
the burst upstream, and no policer, shaper or aqm (that I know of!?)
presently does that.

Most policers today are brick wall filters and just drop everything
above the set rate. These do very poorly in short RTT situations in
particular.

Another idea in bobbie is to use FQ-like techniques to shoot at multiple
flows - gently! to get a more drastic rate reduction, faster, while
impacting them minimally.

so we would start hashing the 5 tuple when the rate is exceeded, and
shoot at/mark no more than one packet per flow as a starting point, and
measure, then shoot again on a changed interval against more or less or
different packets. The hard part in bobbie would be to find a stable
algorithm that did all this, and we don't have one. However something
that was still quite brick wall, but shot at multiple flows gently,
would be a significant improvement on what we have today in the linux
policing system, and adding mark capability would be a boon...

A third idea for all this is to measure the "smoothness" of the
delivered flow from the upstream shaper. When it goes smooth, it
indicates it has found it's set rate and is buffering. Doing this well
requires relative insensitivity to the native burstyness of the
underlying mac layer.

Technically it would be much simpler for the upstream devices (cmtses
and dslams, etc) to adopt a better shaping/fq/aqm technique in the first
place!
