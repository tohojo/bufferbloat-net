
---
title: Sandbox
date: 2011-01-23T20:12:55
lastmod: 2011-01-31T20:57:45
type: wiki
---
Sandbox
=======

-   Optimimum buffering according to Kleinrock

{{mathjax( bandwidth \\times delay \\times \\sqrt(flows))}}

-   Bufferbloat Equation vs Kleinrock

{{mathjax( bandwidth \\times delay \\times \\sqrt(flows) + {(dark
buffers) \\over (luck \* hacks)})}}

where luck is in the range 0..1 and rapidly approaching 0.

The congestion window of TCP/Cubic is determined by the following
function:

{{Mathjax(W\_{cubic} = C (t − K)\^3 + W\_{max})}} where C is a scaling
factor, t is the elapsed time from the last window reduction) W\_max is
the window size just before the last window reduction, and

{{Mathjax( K = \\sqrt\[3\]{(W\_{max} β/C)})}} where β is a constant
multiplication decrease factor applied for window reduction at the time
of loss event (i.e., the window reduces to βW\_m\_a\_x at the time of
the last reduction).

I had tested inline images before, and they just worked.

This doesn't,

![](jigsawfish_small.png)

Attachment?

![](attachment_jigsawfish_small.png)

Does a full url work?

![](http://www.bufferbloat.net/attachments/14/jigsawfish-small.png)

Does a mirrored url work?

![](http://mirrors.bufferbloat.net/jigsawfish-small.png)

Partial url?

![](attachments/14/jigsawfish-small.png)

Url with a link?

![](/images/jigsawfish-small.png):http://www.lwn.net

-   Macro List

{{macro\_list}}
