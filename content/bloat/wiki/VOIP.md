---
title: VOIP
date: 2011-03-05T07:47:07
lastmod: 2011-04-26T04:51:37
type: wiki
---
Bufferbloat and VOIP
====================

At the host, VOIP packets are usually emitted at a multiple of 10ms
intervals. They are very small (usually less than 300 bytes), and very
delay sensitive. If you delay more than 10ms, it makes sense to simply
throw away the packet you have and send the next one, immediately.

There are those doing kernel development that think that 10-20ms jitter
or 40ms latency is OK. It's not, for VOIP. 10-20ms jitter translates out
(worst case) to throwing half of your packets away at the receiver, and
interpolating the other half. It is far better to aim for below 10ms
jitter, at which point voice quality is only dependent on packet loss.

Given that there is about a 4ms transmit window for wireless, I'd like
to go for 4ms maximum delay and jitter across the entire transmit range
of that technology.

That's on the host, which we can control. After voip escapes the host,
all sorts of delay and jitter can occur, but it usually evens out. The
problem with accepting high delays is that above 250ms or so is that
conversations flow badly; people step on each other.

The speed of light on fiber around the world is around half a second, so
no matter what you do, you're in a losing situation. Artificially adding
40ms delay, randomly, is like adding the 3/4ths the width of the
Continental USA to the conversation.

Due to its continuous nature, every delay spike will add to the delay
for the rest of the conversation. There are algorithms (eg WSOLA) that
enable the receiver to drain a full buffer by "talking faster", but even
if those algorithms were perfect, they would alter the meaning of a
spoken phrase at some point.

ITU T G.114 recommends a mouth-to-ear delay of under 150 ms.

![](/attachments/110426042225_m2e-delay.PNG)\
(source ITU T G.114)

Admittedly the real point is different; there is no single right answer,
and the right latency we have to strive for is of order 1 packet; but
that will take AQM we don't have yet. We're always reluctant to argue
against mitigation, when real solution still evades us.

However, plugging in the 4ms constraint into the network stack gives us
numbers to work with and goals to aim for.

### Attachments
{{< attachment name="m2e-delay.PNG" type="image/png" description="quality vs delay" filename="110426042225_m2e-delay.PNG" >}}
{{< attachment name="m2e-delay.zip" type="application/zip" description="" filename="110426042651_m2e-delay.zip" >}}
