---
title: Papers
date: 2011-01-26T20:22:48
lastmod: 2013-01-19T11:32:43
type: wiki
---
Papers
======

In the discussions on bufferbloat so far, an astounding number of papers
have been referenced:

Motorola has a [very clear management level presentation on the need for
fair
queuing](http://www.cascaderange.org/presentations/DOCSIS_1_1_QoS.pdf)

Read the slides starting with "If RED is not good enough, what is?".

http://gettys.files.wordpress.com/2010/12/uplink\_buffer\_all.pdf

[Netalyzr: Illuminating The Edge
Network](http://www.icir.org/christian/publications/2010-imc-netalyzr.pdf)\
As outlined in the [IMC Netalyzr
paper](http://conferences.sigcomm.org/imc/2010/papers/p246.pdf)
section 5.2, the structure you see is very useful to see what buffer
sizes and provisioned bandwidths are common. The diagonal lines indicate
the latency (in seconds!) caused by the buffering. Both wired and
wireless Netalyzer data are mixed in the above plots. The structure
shows common buffer sizes that are sometimes as large as a megabyte.
Note that there are times that Netalyzr may have been under-detecting
and/or underreporting the buffering, particularly on faster links; the
Netalyzr group have been improving its buffer test.

http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.65.6825&amp;amp;rep=rep1&amp;amp;type=pdf

--

[Battling
Bufferbloat](http://akira.ruc.dk/~tohojo/bufferbloat/bufferbloat-final.pdf)

http://simula.stanford.edu/sedcl/files/dctcp-final.pdf

[Fast Object-Based data transfer
System(FOBS)](http://www.umcs.maine.edu/~dickens/pubs/HPDC.FINAL.pdf)

[Simple Available Bandwidth Utilization
Library(SABUL)](http://pubs.rgrossman.com/dl/journal-028.pdf)

[Reliable Blast UDP
(RBUDP)](http://www.evl.uic.edu/files/pdf/cluster2002.pdf)

[Bittorrent
Broadnets](http://www.cs.clemson.edu/~jmarty/papers/bittorrentBroadnets.pdf)
- with buffers of 20-40 packets (32-64 KB buffers). As soon as the
common uplink saturated, everything went to heck

[Comcast's kill bittorrent 'solution' did only target
uploads](http://www.isoc.org/isoc/conferences/ndss/09/pdf/08.pdf)

[Flow Splitting with Fate Sharing in a Next-Generation Transport
Services Architecture](http://dedis.cs.yale.edu/2009/tng/) - also
[available on arXiv](http://arxiv.org/pdf/0912.0921v1)

http://www.usenix.org/event/nsdi09/tech/full\_papers/sanaga/sanaga.pdf

http://guido.appenzeller.net/pubs/sigcomm-extended.pdf

[Optimization of TCP/IP Traffic Across Shared
ADSL](http://www.adsl-optimizer.dk/thesis/main_final_hyper.pdf)

[Understanding Bandwidth-Delay-Product in wireless mesh
networks](http://cairo.cs.uiuc.edu/publications/papers/elsevier2004-bdp.pdf)

http://yuba.stanford.edu/\~nickm/papers/

[Characterizing Residential Broadband
Networks](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.65.6825&rep=rep1&type=pdf)

[Buffer Bloat
Calculations](http://netoptimizer.blogspot.com/2010/12/buffer-bloat-calculations.html)

[RAQM (REMOTE Active Queue
Management](http://www.cs.purdue.edu/homes/eblanton/publications/raqm.ps)\
h2. More unsorted papers

Marina Thottan has been very kind to send me pointers to recent work on
router buffer sizing. As you will see, there are good reasons to believe
much conventional wisdom is far from the mark.

She is co-author of a survey paper that covers work done by different
groups on router buffer sizing. Here is a link to it:\
http://portal.acm.org/citation.cfm?id=1517487&CFID=13973251&CFTOKEN=48745519&qualifier=LU1007961

Nick Mckeown @ Stanford has several talks on buffers for routers.\
Here is the link to his web page:\
http://tiny-tera.stanford.edu/\~nickm/talks/index.html

The specific talks are on this page:\
"Internet Routers: Past Present and Future."\
"Buffers: How we fell in love with them, and why we need a divorce."\
"Sizing Router Buffers"\
"Network Processors and their memory"\
"Designing Packet Buffers for Internet Routers"\
"Memories for Internet Routers"

TCP Veno papers
---------------

[Veno](http://wwwbk.ie.cuhk.edu.hk/fileadmin/staff_upload/soung/Journal/J3.pdf)

[Veno And
RED](http://www.ie.cuhk.edu.hk/fileadmin/staff_upload/soung/Conference/C12.pdf)

[Fluid based modeling of
Veno](http://web.mysites.ntu.edu.sg/aschfoh/public/Shared%2520Documents/pub/06777512-GC08.pdf)

Bad, outdated advice (should be corrected in the field)
-------------------------------------------------------

http://fasterdata.es.net/TCP-tuning/linux.html
