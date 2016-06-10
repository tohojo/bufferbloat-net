
---
title: Bloat-videos
date: 2012-12-07T22:01:15
lastmod: 2015-09-06T04:14:58
---
Videos about Bufferbloat, Codel and FQ\_codel
=============================================

Over the last couple years, there have been a number of video
presentations created to describe bufferbloat and the solutions to it.
This is a collection of links to these resources, in roughly date
order...

Jim Gettys (of Alcatel) Bufferbloat: Dark Buffers in the Internet, April 26, 2011
---------------------------------------------------------------------------------

[Jim Gettys'](http://en.wikipedia.org/wiki/Jim_Gettys) Google Tech Talk.
This is a very detailed look into Jim's discovery of the problem, as
well as a full early description of the problem.
[YouTube](http://www.youtube.com/watch?v=qbIozKVz73g)

Fred Baker (of CISCO) explains bufferbloat at LACNIC, July 2012 (Español only video)
------------------------------------------------------------------------------------

[Obesity, it's not just a human
problem](http://www.youtube.com/watch?v=uQ9ziQg_1zU)

Van Jacobson (of Google) introduces the codel solution and the packet fountain analogy at the IETF84 conference, July-August 2012
---------------------------------------------------------------------------------------------------------------------------------

[Van
Jacobson](http://www.wired.com/wiredenterprise/2012/05/van-jacobson/)
speaking about [TCP, Congestion, and CoDel
cure](http://recordings.conf.meetecho.com/Recordings/watch.jsp?recording=IETF84_TSVAREA&chapter=part_3)
. The quality of the video is sadly poor, and his slides
([here](https://plus.google.com/u/0/107942175615993706558/posts/eG8wZh7Qshs)
) not in sync, but follow along, if you can.

IETF demo side-by-side of a normal cable modem vs fq\_codel
-----------------------------------------------------------

IETF: [Demonstration of web page load reduction
times](http://www.circleid.com/posts/20130418_bufferbloat_demo_see_how_much_faster_internet_access_can_be/)

Jesper Dangaard Brouer (of RedHat) leverage’s Van Jacobson's analogy
--------------------------------------------------------------------

in his [in depth look at codel - Have we found the cure for
Bufferbloat?](http://www.circleid.com/posts/20130506_video_have_we_found_the_cure_for_bufferbloat/)

Eric Dumazet (of Google) at the Linux Plumbers conference
---------------------------------------------------------

He (author of fq\_codel) takes a shot at explaining [How fq\_codel
works](http://linuxplumbers.ubicast.tv/videos/codel-and-fq_codel-fighting-the-delays/)

Stephen Hemminger's (of Vyatta) Bufferbloat from a Plumbers Point of view, 25 March 2013
----------------------------------------------------------------------------------------

Stephen has put together an increasingly high energy talk and
demonstrations about how [various queue theories
work](http://www.youtube.com/watch?v=y5KPryOHwk8) - in friendly
competition with Dave's talks...

Toke Høiland-Jørgensen
----------------------

-   [Steady state, fairness and transient behaviour of modern
    AQMs](http://www.bufferbloat.net/attachments/222/abstract-aqm-algorithms.pdf)
    filmed at:\
    [Stanford netseminar](http://netseminar.stanford.edu/)
    http://netseminar.stanford.edu/

Dave T&auml;ht's "Water Videos", November 2012
----------------------------------------------

Dave T&auml;ht (Hindmost, Bufferbloat.net) gave a lecture at the
University of Modena in late November 2012, where he managed to cover 30
years of network queueing theory in 80 minutes. Here are selected video
segments from the lecture showing various queueing techniques. Full rate
video (.mp4), an .mp3 of the audio, and the .odp presentation are
available at http://www.teklibre.com/\~d/talks/video/ or get a [PDF
version of the
slides](http://www.bufferbloat.net/attachments/download/147/Not_every_packet_is_sacred-Fixing_Bufferbloat_Codel_Fq_Codel.pdf)

-   **Bufferbloat \#1/TCP 101**\
    [Raw
    .mp4](http://www.teklibre.com/~d/talks/video/20121128_143953.mp4)
    [YouTube](http://www.youtube.com/watch?v=KD5TwLQnq_8)
-   **Bufferbloat \#2/Tail-drop queueing**\
    [Raw
    .mp4](http://www.teklibre.com/~d/talks/video/20121128_144744.mp4)
    [YouTube](http://www.youtube.com/watch?v=PgFcqRMDqlk)
-   **Bufferbloat \#3/FIFO, RED, Blue, and Fair Queueing**\
    [Raw
    .mp4](http://www.teklibre.com/~d/talks/video/20121128_150143.mp4)
    [YouTube](http://www.youtube.com/watch?v=Y9xJbwb28Zc)
-   **Bufferbloat \#4/Wifi, Netalyzr, SFQ, SFQRED**\
    [Raw
    .mp4](http://www.teklibre.com/~d/talks/video/20121128_151516.mp4)
    [YouTube](http://www.youtube.com/watch?v=ol_BcKA9Ohg)
-   **Bufferbloat \#5/CoDel and Drop Head Queueing**\
    [Raw
    .mp4](http://www.teklibre.com/~d/talks/video/20121128_152757.mp4)
    [YouTube](http://www.youtube.com/watch?v=R8Esi0zjNdE)
-   **Bufferbloat \#6/More details on FQ-Codel**\
    [Raw
    .mp4](http://www.teklibre.com/~d/talks/video/20121128_153327.mp4)
    [YouTube](http://www.youtube.com/watch?v=bi-jumVNVGk)
-   **Bufferbloat \#7/Questions and Answers**\
    [Raw
    .mp4](http://www.teklibre.com/~d/talks/video/20121128_154620.mp4)
    [YouTube](http://www.youtube.com/watch?v=JFH5fGNzBJU)

Dave T&auml;ht's "FQ\_codel World Tour", March-June 2013
--------------------------------------------------------

Dave then went on a world tour to try and find ways of explaining the
fq\_codel solution to bufferbloat in depth, to a variety of audiences.

-   Stanford: [Inside Codel and FQ
    Codel](http://netseminar.stanford.edu/)
-   MIT: [What's wrong with
    wifi?](http://www.youtube.com/watch?v=Wksh2DPHCDI&feature=youtu.be)
-   The Gathering: [How to really fix your
    lag](http://technet.gathering.org/2013/03/31/tg13-preso/)
-   RIPE 66: [CeroWrt against an uncaring
    Universe](https://ripe66.ripe.net/archives/video/1200/)
-   UKNOF 25: [Beating Bufferbloat with
    fq\_codel](http://www.youtube.com/watch?v=quAaZKBHvs8)

Dave T&auml;ht's "Make-wifi-fast Tour", Jul - ?? 2015
-----------------------------------------------------

-   Battlemesh: [How to make wifi fast
    again](https://www.youtube.com/watch?v=-vWrFCZXOWk)
-   Battlemesh: [Fixing IoT and the space
    program](https://www.youtube.com/watch?v=QWdL2Wu7M-8)

