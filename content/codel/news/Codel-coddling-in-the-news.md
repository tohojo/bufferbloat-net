
---
title: "Codel (coddling) in the news"
date: 2012-07-03T08:09:00
type: news
author: Dave Täht
---
Kamal Mostafa built an [Ubuntu 12.4
PPA](https://launchpad.net/~kamalmostafa/+archive/bufferbloat), and
wrote: "The result is **very** impressive: I see a 30X reduction in ping
latency on a fully saturated 10Mbps network, just by switching on the
new fq\_codel scheduler. For an interactive ssh session over that same
saturated 10Mbps network, fq\_codel totally eliminates the laggy
keyboard response — it feels like there’s no other network traffic at
all!"

Steve Gibson, on [Steve Gibson's Security Now
podcast](http://www.grc.com/sn/sn-359.htm) said:

"They show charts where they show the throughput under these varying
conditions, even though they're discarding intelligently, and it's right
up between 90 and 100 percent; whereas the traditional algorithms
collapse down into the low 10s of percent of overall throughput. It's
just - it's fantastic. "

Jim Gettys outlined how [The internet is broken, **and** how to fix
it](http://gettys.wordpress.com/2012/06/26/the-internet-is-screwed-up-and-how-to-fix-it)
...

Dave Miller [installed
CeroWrt](https://plus.google.com/101384639386588513837/posts/Cgvfn8m9XuC)

[And then there was the truly mind-bending
praise](http://rajeeshknambiar.wordpress.com/2012/05/27/on-bufferbloat-and-shoulders-of-the-giants/)

"These extra-ordinary people, today, are silently fixing tomorrow’s
internet. And they deserve big props for that. All you technologists who
didn’t get a chance to appreciate Nikola Tesla or Dennis Ritchie, here
is your chance to do that for some of the real heroes of our time."

I'm not going to let this last bit of exuberance get to me - as I
remember how Tesla ended up, after suffering through decades of patent
battles. I'm glad Van and Kathie **didn't patent codel** - and equally
glad the reference implementations and sims we did are available under a
dual BSD/GPL license, so anyone can use them.

Because we **all** need a better internet.

And that said, much work remains - analysis and improvements to codel
with ecn continues, wifi is still troublesome, 95% of the linux drivers
don't have BQL support, and so on.

We're keeping links to useful code and data on
http://www.bufferbloat.net/projects/codel/wiki - if you are doing any
serious analysis of codel and fq\_codel, or have it running on a new OS,
please let us know.
