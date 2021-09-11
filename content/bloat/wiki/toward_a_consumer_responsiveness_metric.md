---
title: Toward a Consumer Responsiveness Metric
date: 2021-09-10T09:10:12
lastmod: 2021-09-10T09:10:12
type: wiki
aliases:
    - /bloat/wiki/Toward_A_Consumer_Responsiveness_Metric/
    - /cerowrt/wiki/Toward_A_Consumer_Responsiveness_Metric/
---
# Toward a Consumer Responsiveness Metric

*At a recent videoconference, I advocated strongly for a consumer-facing measurement of latency/responsiveness.
I had not planned to speak, so I gave off-the-cuff comments.
This is an organized explanation of my position.
I offer these thoughts for consideration at the
[IAB Workshop "Measuring Network Quality for End-Users, 2021"](https://www.iab.org/activities/workshops/network-quality/) - Rich Brown*

I hunger for a day when vendors (router manufacturers and service providers) compete on the
basis of "responsiveness" in the same way that they compete on speed -
"Up to X megabits per second, and Y responsiveness!"

I have been working on the "Bufferbloat Project" [1] since 2011,
trying to find layman's terms for what was happening, and what to do about it. [2] [3]
The delay goes by the name "lag", "latency under load", or "bufferbloat".
At first, the effects seemed mysterious and non-intuitive.
Even to knowledgeable individuals, the magnitude of the delay caused by queueing was astonishing.
No matter what name you use, it makes people say, "the internet is slow today".

My router at home has solved this problem.
I enjoy the fruits of the intense research from the mid 2010's that led to
well-understood solutions such as fq_codel, cake, PIE, and airtime fairness.
Even using 7 mbps DSL, my network was quite usable, and very responsive.

My frustration in 2021 is that this remains a problem for nearly everyone else.
The market has not provided solutions.
Every day, people purchase brand name equipment that happily queues hundreds of msec of traffic.

I postulate that vendors have not considered responsiveness to be an important characteristic
of their offerings.
Consequently, they have not prioritized the engineering resources to
incorporate the well-tested solutions listed above.

My hope, from this note, and from our on-going efforts, is that we can come up with
a test tool that consumers can use to raise awareness of the problem of bad responsiveness.

## Characteristics of a Responsiveness Tool

I seek a "responsiveness tool" with these characteristics:

1. Easy to use. People need an easy way to measure responsiveness so they
can give feedback to their vendors.
2. A single number, so it's easy to report and compare.
3. Bigger must be better. High latency means bad responsiveness.
People have no intuitive feel for a millisecond: "Is 100 msec bad? Isn't that really short...?"
4. An approximate measure is OK. Consumers won't mind separate runs varying 20% or 30%,
especially since poor responsiveness could be an order of magnitude different from good.
5. Resistant to cheating. Vendors sometimes optimize pings to make latency look lower.
But real people's traffic doesn't use pings.
The responsiveness test must use protocols that match actual traffic patterns.
6. Vendor and technology independent. People should use and get similar results from
their phone, their desktop, on the web, or using an app.
7. "Good enough". A widely implemented and promoted metric that substantially
matches people's real experience is vastly superior to a host of competing metrics
that muddy the waters in consumer's minds.

## A Proposed Metric - RPM

Apple has produced an Internet Draft "Responsiveness under Working Conditions" [4] and implementation.
It defines a procedure for continually making short HTTPS transactions on a path to a
server that has been fully loaded in both directions.
The number of transactions in a fixed time is expressed as the number of "round-trips per minute",
which is given the name "RPM", a wink to the "revolutions per minute" that we use for cars.

The RPM measurement satisfies all my concerns.

## Non-requirements

It is **not** a requirement for the responsiveness test to provide:

* Strict reproducibility. The wider internet has widely varying conditions, with
bottlenecks moving around by time of day or adjacent traffic.
It is not reasonable/feasible to expect that any measure used by consumers will be exactly reproducible.

* Detailed statistics or distributions of measurements. This is not a diagnostic tool.
A nuanced data set with medians and percentiles may excite techies, but for others,
it's hard to understand the implications.

* Performance of any particular protocol. The responsiveness tool must measure a broad
variety of typical traffic.

* Data to be used as input for vendors to design solutions.
The responsiveness measure needs to be used the same way we say to our mechanic,
"The car makes a funny noise when I ...".
I expect the specialist to work to reproduce the symptom, using the provided equipment,
and come up with an appropriate solution.

## Summary

The research of the last decade has developed a wide variety of solutions.
There are plenty of corner-cases where these solutions aren't perfect.
I encourage vendors and researchers to study the field and advance our knowledge further.
I would be delighted if they found practices even better than the current state of the art.

But "the rest of the internet" (including my neighbors and family members,
for whom I'm the support person) would all benefit from a world where
off-the-shelf equipment already incorporated well-known, best practice solutions.

## References

[1] **Bufferbloat Project** [https://bufferbloat.net](https://bufferbloat.net)

[2] **Bufferbloat and the Ski Shop** [https://randomneuronsfiring.com/bufferbloat-and-the-ski-shop/](https://randomneuronsfiring.com/bufferbloat-and-the-ski-shop/)

[3] **Best Bufferbloat Analogy - Ever** [https://randomneuronsfiring.com/best-bufferbloat-analogy-ever/](https://randomneuronsfiring.com/best-bufferbloat-analogy-ever/)

[4] **Responsiveness under Working Conditions** - Internet-Draft at:
[https://github.com/network-quality/draft-cpaasch-ippm-responsiveness/blob/master/draft-cpaasch-ippm-responsiveness.md](https://github.com/network-quality/draft-cpaasch-ippm-responsiveness/blob/master/draft-cpaasch-ippm-responsiveness.md)
*Full disclosure: I am one of the editors of the "Responsiveness Under Working Conditions I-D"*

[5] **draft-cpaasch-ippm-responsiveness-00** PDF of current internet draft. [https://randomneuronsfiring.com/internet-draft-responsiveness-under-working-conditions/](https://randomneuronsfiring.com/internet-draft-responsiveness-under-working-conditions/)

[6] This note was first published at [https://randomneuronsfiring.com/toward-a-consumer-responsiveness-metric/](https://randomneuronsfiring.com/toward-a-consumer-responsiveness-metric/)
