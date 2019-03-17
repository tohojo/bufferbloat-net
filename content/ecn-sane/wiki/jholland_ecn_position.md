---
title: Dave Taht's Stance on ECN
date: 2019-03-17 01:14:22
lastmod: 2019-03-17 12:36:00
type: wiki
tags: ecn-blue

---

# Jake's ECN Position=Blue (+Yellow Stripes)

I think of myself as BLUE, with big yellow racing stripes.

I think ECN has a lot of important potential for improving the way
the internet operates.

In general, I think the sender can do great things with rate tuning
when it has just a little more information about the state of the
network than "there might have been some loss, I'm not quite sure".

(I worked on FastTCP for years and saw it there, and I'm seeing it
again from more of a distance in BBR.)

I mean, it's complicated.  No argument here.  The response depends
on the RTT in uncomfortable ways, and analyzing the performance
characteristics of competing flows with different parameters gets
you out into the weeds of insanity really fast, and that's before
you try to worry about the possibility of corner case issues in
the details of different implementations.

But the advantages of getting an explicit signal out of the network
are huge, compared to trying to infer guesses about the network out
of the ack patterns.  Night vs. day.  Forensics vs. surveillance
cameras.  Just because today's congestion controls don't nail the
optimal response yet doesn't mean the information isn't worth its
weight in bitcoins.

I think that to the extent we can get better at this, we can have
a better internet.  I'd love to see it out there and working. I'm
glad Apple and Linux have done their parts to get deployment
closer to a real possibility, and I'm glad this list is here and
the people on it are digging into the issues.  I hope other groups
working on middle boxes are doing so as well.

With a little luck and a lot more work, maybe we'll end up with
a more efficient internet one day.  My biggest fear is getting it
unfixably wrong.  But I have a pretty strong belief there's a good
answer in there somewhere.

[Mailing list post for reference.](https://lists.bufferbloat.net/pipermail/ecn-sane/2019-March/000089.html)
