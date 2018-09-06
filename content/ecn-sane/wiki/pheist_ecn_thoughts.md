---
title: Pete Heist's Thoughts on ECN
date: 2018-09-06T23:28:00
lastmod: 2018-09-06T23:28:00
type: wiki
tags: ecn-purple

---

# Pete Heist's Thoughts on ECN

Although I feel the usual pull of team Grey, I think I'll call myself a
**Purple** for this, possibly overly simplistic reason:

> In theory, the ECN bits only give congestion control algorithms more information
> than they would otherwise have, and in a perfect world, dropping packets would
> be a measure of last resort.

Purple should lose if it can be shown that nothing can (practically) be done to
come up with an agreed upon treatment of ECN bits that results in “better”
congestion control with less packet loss, most of the time. Or if there are
commonly observed, demonstrably harmful pathologies that are not reasonably
possible to overcome.

Presently, I’m more interested in what happens to traffic for regular people and
small to medium sized ISPs, say 5-200ms RTTs and 1-100Mbit bitrates, than what
happens in the data centers of trillion dollar companies.

Lastly, my interest in ECN is to understand better what tools and metrics can be
used on real-world traffic to evaluate its impacts. If I can contribute anything
to this project, I hope it will be to bring some unsettled contradictions to
slightly earlier resolutions...
