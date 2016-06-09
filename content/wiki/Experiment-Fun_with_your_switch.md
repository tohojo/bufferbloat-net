
---
title: Experiment-Fun with your switch
date: 2011-02-02T17:08:40
lastmod: 2011-02-02T17:10:51
---
Experiment-Fun with your switch
===============================

As enough pieces have fallen into place to make actual predictions, (and
the quarry’s spoor noticed), I decided to perform more deliberate
experiments to see if I could capture more henchmen of the mastermind. I
did.

I’ll start to provide puzzle pieces I’ve discovered here regularly, so
you can help with the conviction of the criminal and repair of the
damage they have caused. Today’s simple experiments only involve your
router’s switch. We’ll do some experiments on the wireless side of the
router next.

Conclusion: something stinks in operating system’s network stacks. Linux
is often worst, with two different but related problems, followed by Mac
OSX; Microsoft Windows manages to obfuscate much of it’s problems, but
also demonstrably suffers. After mitigation, Linux may be able to
perform much better than either.

Experiment Setup
================

If your home router has a gigabit switch (a few do, these days), you’ll
want to find a 100 meg switch to perform this experiment with. You may
be able to achieve the same effect using “ethtool” and setting your
ethernet link speed to 100Mbps. I presume your machines all have gigabit
network interfaces; most have for a while.

Hook up your laptop directly to the switch’s ethernet port. Hook a
second machine up to a second port to act as your server. In case one or
the other of your computers is wimpy, let’s use nttcp for our testing.
The point here is to transfer data over the link as fast as you can.

Install “nttcp“. Run “nttcp -i” on the machine you designate as your
server.

Experiment 1a:
--------------

Run “nttcp -t -D -n2048000 server & ping-n server” on your laptop.

What do you observe after, say, 20 seconds? Is this what you would
expect, given that a packet of 1500 bytes takes only .13 milliseconds to
pass through a 100Mbps switch?

Experiment 1b:
--------------

Issue the command “ifconfig eth0“; look at the txqueuelen value. On my
laptop, it is set by Linux to 1000.

Is the latency constant, or variable, as you manipulate the txqueuelen
parameter?

Set the txqueuelen parameter to half of its initial size (e.g. “ifconfig
eth0 txqueuelen 500“. What happens to the observed latency?

What do you observe? How does it differ from Experiment 1a?

Try playing with different values of txqueuelen while continuing to
observe the ping latency. On most current hardware, you can set the
txqueuelen to zero; on some older hardware, you may have problems if you
do so.

Experiment 1c:
--------------

Install the command “ethtool” if you don’t have it installed.

Set the txqueuelen to the minimum operating value (0 on my laptop) for
this experiment.

Execute the command “ethtool -g” and note the current hardware settings
for your ethernet interface. Note that not all device drivers support
this interface. On my laptop, the ring size is 256 by default.

Run “nttcp -t -D -n2048000 server & ping -n server” on your laptop. What
do you observe? Why?

Try playing with different values for the ring parameters (e.g.
“﻿ethtool -G eth0 tx 64” , and observe the ping latency. Your hardware
will probably have some limit minimum ring size that you cannot go
below. On my laptop, this is 64 entries.

Is the latency constant, or variable? Why?

Experiment 1d:
--------------

Note that you can perform similar experiments on Mac OSX and Windows,
both of which behave much better than Linux “out of the box” (though
Linux is better than OSX once the transmit queue is truncated). Note
that the details of the hardware matter here: you should use the same
hardware, or hardware using the same ethernet chip if possible.

For extra credit, explain why Windows default behavior is so much better
than either Linux or OSX on 100Mbps Ethernet. (Hint: try setting the
transmit speed on the Windows machine to 10Mbps; and search Windows
technical notes about multimedia playing). Do you now believe
Microsoft’s explanations? Or is there a different explanation given
these experiments that makes more sense?

See Also: [Experiment-Fun with wireless]({{< relref "wiki/Experiment-Fun_with_wireless.md" >}})

Extracted from: [Fun with your
Switch](http://gettys.wordpress.com/2010/11/29/home-router-puzzle-piece-one-fun-with-your-switch/)
