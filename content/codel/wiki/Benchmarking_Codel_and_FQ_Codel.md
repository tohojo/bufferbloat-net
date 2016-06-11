
---
title: Benchmarking Codel and FQ Codel
date: 2012-10-01T15:15:31
lastmod: 2014-09-02T09:45:33
type: wiki
---
Benchmarking Codel and FQ Codel
===============================

Please see the complete [Best practices for benchmarking Codel and FQ Codel]({{< relref "codel/wiki/Best_practices_for_benchmarking_Codel_and_FQ_Codel.md" >}}) page for extensive details.

Benchmark tool issues
---------------------

Benchmarks such as netperf, speedtest.net, and netanalyzer are all
flawed in that they tend to test single stream behavior, rather than
multi-stream. Most of the web based tests peak out at 20Mbits, and none
run long enough to generate a statistically valid result.

The core bufferbloat benchmarks all test "latency under load", for
multiple streams. The kind of testing you should do while optimizing
your network connection would be, for example, A speedtest.net test,
WHILE doing a ping. A netperf, WHILE making a phone call, trying to hold
the latency and jitter of the smaller stream (ping or voip)small.

We have developed the
[netperf-wrapper](https://github.com/tohojo/netperf-wrapper) tool suite
to make benchmarking these various network attributes easier, with
results that can be easily shared and graphed several dozen ways. It is
available for Linux, BSD, and BSD-derived systems such as OSX.

Also:

The codel algorithm uses buffering as a "shock absorber", and thus,
short term udp flooding tests such as netalyzer, show the actual
physical amount of buffering, not the amount codel eventually converges
on for a single stream. So netanalyzer in particular, will show you have
excessive buffering, when a better test would be measuring latency of a
second stream.

Unmeasured by anything, fq\_codel gives the first packet in each stream
priority, so that small streams jump to the front of the queue, allowing
for much higher parallelization and utilization. We keep hoping to be
able to benchmark this effect on web applications in particular, but
haven't come up with a way to do so.

The fq\_codel version of codel won the accolades of codel's co-designer,
[Van
Jacobson](http://recordings.conf.meetecho.com/Recordings/watch.jsp?recording=IETF84_TSVAREA&chapter=part_3)
:

> fq\_codel provides great isolation... if you've got low-rate
> videoconferencing and low rate web traffic they never get dropped. A
> lot of the issues with iw10 go away, because all that other traffic
> sees is the front of the queue and you don't know how big its window
> is and you don't care because you are not affected by it. And:
> fq\_codel increases utilization across your entire networking fabric
> especially for bidirectional traffic... If we're sticking code into
> boxes to deploy codel, don't do that. Deploy fq\_codel. It's just an
> across the board win." - Van Jacobson

And since then, we've been working on deploying it, rather than refining
it.

Third party benchmarks
----------------------

[fq\_codel and pie vs
cable](http://burntchrome.blogspot.com/2014_05_01_archive.html)

http://planet.ipfire.org/post/ipfire-2-13-tech-preview-fighting-bufferbloat
