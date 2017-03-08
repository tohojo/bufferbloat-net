---
title: CakePerformance
date: 2017-03-07T00:00:00
type: wiki
---
CAKE Packet Scheduler - Performance Evaluation
==============================================

Introduction
------------

Bufferbloat is the phenomenon of large, unmanaged queues in network equipment causing significant *induced delay* when the network is loaded to capacity.  There are many potential solutions to bufferbloat in the literature, including congestion signalling by active queue management (AQM), flow isolation (or fair queuing), and simple buffer-sizing strategies.

Unfortunately, many large, unmanaged queues remain deployed in practice, with equipment vendors remaining mostly oblivious to the problem and its solutions.  End-users thus need to deploy *quality of service* (QoS) systems separately from the hardware, typically using a wifi router.  Such separated QoS deployments need to combine a *queue discipline* (qdisc) with a *shaper*, the latter taking control of the path bottleneck and, in theory, keeping the true bottleneck’s unmanaged queue empty.

CAKE (Common Applications Kept Enhanced) is a combined network packet scheduler and shaper, aiming for the ideal of a *comprehensive queue management* system in a single package.  It is designed to offer excellent latency and throughput performance in network-edge applications, out of the box, with very little configuration or expertise required of the end-user.

To achieve these design goals, CAKE includes several layered packet-scheduling algorithms, implementing rate limiting, Diffserv priority, flow isolation with host fairness, and congestion signalling.  Each of these algorithms contains novel features, which are fully described in separate papers.  The purpose of this paper is to examine the performance of the complete ensemble compared to commonly-used alternatives.

Most available alternatives consist of qdiscs which implement a single function from the above list, or in some cases a combination of two functions.  To achieve the closest equivalent functionality to CAKE using these, it is necessary to combine several qdiscs in a hierarchy, which incurs significant configuration complexity.  Doing so reliably and efficiently is well beyond the expertise of most end-users or even consumer-level IHVs, and significant mistakes are often observed, degrading or even negating the benefit of QoS.  We also hypothesise that passing packets through this hierarchy incurs CPU overhead, which restricts the throughput of consumer-grade CPE when bufferbloat mitigation is enabled.


Test Setup
----------

We arranged five Linux hosts as follows, using Ethernet cables throughout:

      A
      |
      R
      |
    switch
    | |  |
    B C  D

Host R served as both the bottleneck shaper (ie. the QoS system under test) and the network emulator (injecting delay to simulate Internet paths), and was an AMD A10-7850K fitted with two independent GigE NICs.  All changes of configuration were made here during the tests.  Rather than set up routing or NAT, the two NICs were simply bridged.  Ethernet configuration was left at default settings, while the txqueuelen of the IFB virtual interfaces was increased to 1000 to prevent uncommanded packet drops.

The test runs were all launched from host A, an AMD E-450, using a series of Flent invocations.  As with all the endpoint machines, the “fq” qdisc was set up to provide TCP pacing, ECN negotiation was explicitly switched on, and we ensured CUBIC was the default congestion control algorithm.  Ethernet parameters were left at their defaults.

Host B, an early-model EeePC, served as a Netperf endpoint for TCP flows, running Linux Mint from a live Flash drive.  Host C, a late-model PowerBook G4, served as a second Netperf endpoint running Gentoo Linux.  Host D, a ThinkPad A20p, ran D-ITG to serve as a VoIP endpoint, also on Gentoo.  All three were configured the same way as host A.  Hosts B and D had Fast Ethernet hardware rather than GigE, which influenced our choice of test bandwidths to avoid spurious effects.  As Host C was the most powerful endpoint on its side of the bottleneck, it was made the target for all of the single-host test runs.

Due to limited time, we were able to test only one link bandwidth configuration.  We chose a 20/3 Mbit asymmetric configuration to represent a domestic Annex-M ADSL2 last-mile link, and added 45ms latency in each direction to simulate a typical 90ms Internet RTT.  The effects of ATM encapsulation were not simulated.


Contenders
----------

As ease of configuration is one of CAKE’s primary design goals, we considered only QoS systems which could be set up with minimal expertise and verbosity.  Due to the need for a separate shaper with existing qdiscs, the practical minimum is two tc invocations - one for the shaper, and one for the qdisc itself.  We selected HTB as the common shaper, since it is widely used and reliable, and used it with brief settings typically found in QoS tutorials - merely a bandwidth parameter and “burst 15k”.  All qdiscs were used with settings as close to defaults as would allow fair comparisons.

As a baseline, we reconstructed a typical early SFQ-based QoS scheme, using HTB for shaping.  Priority queuing was not configured.  The default SFQ parameters allowed 127 packets in a 1024-bucket queue, with perturbation of the hash function every 10 seconds.  We increased the packet limit to 1000, but left everything else alone; in particular we did not attempt to configure the embedded RED AQM, as the correct parameters for RED remain difficult to determine.

DOCSIS 3.1 specifies that new cable modems must support the PIE AQM algorithm for uploads.  We therefore included a HTB+PIE combination, leaving PIE at its default settings except for ensuring that ECN support was enabled.  PIE does not handle priority queuing or flow isolation, only congestion signalling; this is nevertheless a signal improvement over a plain, tail-drop FIFO.

To represent a very common arrangement in current use, we combined HTB with fq_codel, also at default settings.  This performs both flow isolation using a simple 1024-bucket hash function and DRR++, and AQM on each flow separately using the Codel algorithm.  Priority queuing was not configured.

We also included the combination of HTB with Codel, without the flow-isolation functionality of fq_codel.  We ensured that ECN was enabled, as that is not the default for this qdisc.  Codel’s default parameters are tuned for Internet-scale latencies of around 100ms RTT, as are those of fq_codel.

For completeness, we also included HTB+SFB.  Stochastic Fair BLUE appeared shortly before fq_codel, and has an unusual approach to flow isolation: flows are not directed to individual queues, but the BLUE AQM algorithm is made flow-aware, and thus signals more strongly to saturating flows than to sparse ones.  This was considered to be a good solution at the time of its introduction, but was quickly eclipsed by fq_codel.

Finally, the subject of this comparison, CAKE.  Because CAKE includes its own shaper, it was not necessary to combine it with HTB.  We used the “bandwidth” option to configure the shaper, and left everything else at defaults.  This configuration therefore used a 3-way priority queue based on well-known Diffserv codepoints (with bulk, best-effort and voice classes), advanced triple flow isolation, and our COBALT AQM tuned for Internet-scale path latencies.

We also included a reconfigured CAKE without priority queuing, and with only basic flow isolation rather than its special triple-isolation feature.  This allowed direct comparison with the combination of HTB and fq_codel.  To do so, we added “besteffort flows” to the CAKE parameters through tc.  We refer to this configuration as “CAKE-Lite” henceforth.


Single Flow Throughput & Latency
--------------------------------

The simplest and easiest test of a QoS scheme is to saturate the link with a single TCP flow, measure its throughput, and simultaneously measure the induced latency on parallel sparse streams representing latency-sensitive traffic.  We used the ready-made tcp_upload, tcp_download, and tcp_bidirectional tests in Flent for this purpose, using Host C as the remote endpoint.  The tcp_bidirectional test, which provides one flow in each direction, covers the case where the TCP ack stream must compete with saturating traffic in the opposite direction.

NB: Each of the graph thumbnails is a link to a bigger version.

{{< figure src="../cake-charts/up-sfq-small.png" link="../cake-charts/up-sfq.png" caption="SFQ Upload" >}}
{{< figure src="../cake-charts/down-sfq-small.png" link="../cake-charts/down-sfq.png" caption="SFQ Download" >}}
{{< figure src="../cake-charts/bidi-sfq-small.png" link="../cake-charts/bidi-sfq.png" caption="SFQ Bidirectional" >}}

SFQ showed the best average throughput of all qdiscs tested, and also showed only moderate impact (about 30ms peak) on the measurement flows.  However, this was marred by significant head-of-line blocking events, which show in the graphs as long gaps in the throughput graph followed by very sharp bursts.  This is symptomatic of tail-dropping on queue overflow, requiring retransmissions.

{{< figure src="../cake-charts/up-pie-small.png" link="../cake-charts/up-pie.png" caption="PIE Upload" >}}
{{< figure src="../cake-charts/down-pie-small.png" link="../cake-charts/down-pie.png" caption="PIE Download" >}}
{{< figure src="../cake-charts/bidi-pie-small.png" link="../cake-charts/bidi-pie.png" caption="PIE Bidirectional" >}}

PIE mostly did well here too, maintaining good throughput and sub-30ms induced latency in each of the unidirectional tests.  However, the download throughput was rather inconsistent when an upload bulk flow was also present, and in this case the induced latency reached 85ms, almost doubling the baseline RTT.

{{< figure src="../cake-charts/up-codel-small.png" link="../cake-charts/up-codel.png" caption="Codel Upload" >}}
{{< figure src="../cake-charts/down-codel-small.png" link="../cake-charts/down-codel.png" caption="Codel Download" >}}
{{< figure src="../cake-charts/bidi-codel-small.png" link="../cake-charts/bidi-codel.png" caption="Codel Bidirectional" >}}

Codel achieved reasonably good throughput, adopting a distinctive periodic pattern on the download test which kept the peak induced latency remarkably low, at 10ms, for a non-flow-isolating AQM.  This clear pattern disappeared with bidirectional traffic, and the induced latency rose to 55ms peak, but throughput remained good overall.

{{< figure src="../cake-charts/up-sfb-small.png" link="../cake-charts/up-sfb.png" caption="SFB Upload" >}}
{{< figure src="../cake-charts/down-sfb-small.png" link="../cake-charts/down-sfb.png" caption="SFB Download" >}}
{{< figure src="../cake-charts/bidi-sfb-small.png" link="../cake-charts/bidi-sfb.png" caption="SFB Bidirectional" >}}

SFB had considerable difficulty with even this most basic series of tests, which does not bode well for its performance on more complex traffic.  Throughput was both very poor and inconsistent, while induced latency peaked near 400ms on both the upload and bidirectional tests.

{{< figure src="../cake-charts/up-fq_codel-small.png" link="../cake-charts/up-fq_codel.png" caption="FQ_Codel Upload" >}}
{{< figure src="../cake-charts/down-fq_codel-small.png" link="../cake-charts/down-fq_codel.png" caption="FQ_Codel Download" >}}
{{< figure src="../cake-charts/bidi-fq_codel-small.png" link="../cake-charts/bidi-fq_codel.png" caption="FQ_Codel Bidirectional" >}}

FQ_Codel shows the same periodic pattern as Codel on the unidirectional tests, confirming that it uses the same AQM algorithm.  Its DRR++ flow isolation makes its mark, compared to Codel alone, by limiting induced latency to 20ms in the bidirectional test, 6ms in the upload test, and a barely-measurable 1ms in the download test.

{{< figure src="../cake-charts/up-cake-small.png" link="../cake-charts/up-cake.png" caption="CAKE Upload" >}}
{{< figure src="../cake-charts/down-cake-small.png" link="../cake-charts/down-cake.png" caption="CAKE Download" >}}
{{< figure src="../cake-charts/bidi-cake-small.png" link="../cake-charts/bidi-cake.png" caption="CAKE Bidirectional" >}}

CAKE and CAKE-Lite produced identical results on this simple test.  Like Codel, a distinctive periodic pattern emerges in the throughput, but it has a different shape and remains closer to the maximum on average.  This is an intriguing result, given that CAKE’s COBALT AQM is closely derived from Codel, and may be a side-effect of CAKE’s more accurate deficit-mode shaper, as compared to HTB’s traditional token-bucket mechanism.  In the bidirectional test, CAKE also improved the peak induced latency to 5ms, while retaining fq_codel’s excellent performance in the unidirectional tests.

The above results are summarised and directly compared in the box-plots below.  Here, the latency plot is inverted so that higher is better.

{{< figure src="../cake-charts/up-all-small.png" link="../cake-charts/up-all.svg" caption="TCP Upload Summary" >}}
{{< figure src="../cake-charts/down-all-small.png" link="../cake-charts/down-all.svg" caption="TCP Download Summary" >}}
{{< figure src="../cake-charts/bidi-all-small.png" link="../cake-charts/bidi-all.svg" caption="TCP Bidirectional Summary" >}}


Realtime Response Under Load
----------------------------

The RRUL test runs four TCP flows in each direction, one using each of CS0, CS1, CS5 and EF DSCPs.  A similar variety of DSCPs is used for the UDP latency-measuring flows.  An RRUL-BE test does the same, except that it leaves all the flows at the default CS0.

{{< figure src="../cake-charts/rrul-total-sfq-small.png" link="../cake-charts/rrul-total-sfq.png" caption="SFQ RRUL Totals" >}}
{{< figure src="../cake-charts/rrul-detail-sfq-small.png" link="../cake-charts/rrul-detail-sfq.png" caption="SFQ RRUL Details" >}}

SFQ again showed very good average throughput and reasonable flow isolation, but all four flows in the upload direction experienced a head-of-line blocking event lasting 20 seconds towards the end of the 60-second test.  There were also large fluctuations in goodput in the download direction, apparently oscillating around the true throughput.  Peak induced latency reached 40ms.

{{< figure src="../cake-charts/rrul-total-pie-small.png" link="../cake-charts/rrul-total-pie.png" caption="PIE RRUL Totals" >}}
{{< figure src="../cake-charts/rrul-detail-pie-small.png" link="../cake-charts/rrul-detail-pie.png" caption="PIE RRUL Details" >}}

PIE achieved good throughput without any gaps in goodput, but the induced latency was considerable, with some samples showing over 170ms, and varied considerably over the course of the test.  The individual throughputs of each flow also wandered up and down in comparison to its peers, though there didn’t appear to be any long-term bias.  This is still much better than a plain FIFO would have shown, but with as few as four simultaneous bulk flows it is clear that some form of flow isolation is necessary.

{{< figure src="../cake-charts/rrul-total-codel-small.png" link="../cake-charts/rrul-total-codel.png" caption="Codel RRUL Totals" >}}
{{< figure src="../cake-charts/rrul-detail-codel-small.png" link="../cake-charts/rrul-detail-codel.png" caption="Codel RRUL Details" >}}

Codel also achieved good throughput with the same type of “wandering” share between flows.  Induced latency was improved over PIE, with a peak of about 90ms, and was generally lower on average and in variability.

{{< figure src="../cake-charts/rrul-total-sfb-small.png" link="../cake-charts/rrul-total-sfb.png" caption="SFB RRUL Totals" >}}
{{< figure src="../cake-charts/rrul-detail-sfb-small.png" link="../cake-charts/rrul-detail-sfb.png" caption="SFB RRUL Details" >}}

SFB continued its trend of poor performance with a peak induced latency of 200ms, and wildly variable throughput in the download direction.  The individual flow graphs corresponding to this were difficult to interpret, but appear to indicate significant burst packet loss.

{{< figure src="../cake-charts/rrul-total-fq_codel-small.png" link="../cake-charts/rrul-total-fq_codel.png" caption="FQ_Codel RRUL Totals" >}}
{{< figure src="../cake-charts/rrul-detail-fq_codel-small.png" link="../cake-charts/rrul-detail-fq_codel.png" caption="FQ_Codel RRUL Details" >}}

FQ_Codel again raised the bar by achieving 33ms peak induced latency.  In the download direction, the overall throughput was consistently very good and the individual flows were also kept fairly tightly equal.  The individual upload flows were much more variable, but appeared to achieve roughly equal throughput on average, as well as consistently reaching maximum total throughput.  Overall, a competent performance.

{{< figure src="../cake-charts/rrul-total-cake-be-small.png" link="../cake-charts/rrul-total-cake-be.png" caption="CAKE-Lite RRUL Totals" >}}
{{< figure src="../cake-charts/rrul-detail-cake-be-small.png" link="../cake-charts/rrul-detail-cake-be.png" caption="CAKE-Lite RRUL Details" >}}

CAKE-Lite, having been intended for direct comparison with fq_codel, managed to outperform it comprehensively.  The peak induced latency came down to just 8ms, overall throughput in both directions remained very good and consistent, and the variability between individual flows in the upload direction was significantly reduced.  In the download direction, the individual flows show periodic fluctuations, out of phase with each other, around a common average.

{{< figure src="../cake-charts/rrul-total-cake-ds3-small.png" link="../cake-charts/rrul-total-cake-ds3.png" caption="CAKE RRUL Totals" >}}
{{< figure src="../cake-charts/rrul-detail-cake-ds3-small.png" link="../cake-charts/rrul-detail-cake-ds3.png" caption="CAKE RRUL Details" >}}

CAKE in default configuration additionally made use of the Diffserv markings of the RRUL traffic, unlike the other contenders.  It therefore shared the available bandwidth between the individual flows very differently.

The CS1 flows received only a small fraction, intended to be 1/16th, as they were assigned to the Bulk traffic class to operate in the background.  The EF flows were assigned to the Voice class, and were thus given priority up to 1/4 of the available bandwidth, but deprioritised as soon as they exceeded it; they also got more aggressive AQM treatment, intended to reduce intra-flow induced latency.  The CS0 and CS5 flows remained in the Best Effort class, and shared the remaining 11/16ths of the bandwidth.  The results show that, with some short-term fluctuation, these relationships were broadly maintained as designed.

The induced latency figures for this configuration merit special attention, as the measurement flows were themselves differentiated by DSCP marking.  The CS1 induced latency thus appears alarmingly high at first sight, though it must be remembered that this traffic class has very little bandwidth in the upload direction, and is competing with a bulk flow; at 70ms peak, this is still lower than any of the non-flow-isolating qdiscs achieved.  The CS0 induced latency peaked at 13ms, while EF peaked at 22ms.  Since the Voice traffic class included a bulk flow and was therefore deprioritised due to reaching its allocated bandwidth, the higher latency relative to Best Effort traffic is expected for this test.

For RRUL, we have both box-plots and an ICMP CDF graph to summarise the above results.

{{< figure src="../cake-charts/rrul-all-small.png" link="../cake-charts/rrul-all.svg" caption="RRUL Summary" >}}
{{< figure src="../cake-charts/rrul-icmp-small.png" link="../cake-charts/rrul-icmp.svg" caption="RRUL Latency CDF" >}}


Asymmetric Bulk Overload
------------------------

Flent includes two complementary tests, rrul_50_up and rrul_50_down, which bombard one direction of the link with 50 bulk flows, and run just a single flow in the opposite direction.  On typical asymmetric home broadband links, such as the one we simulated, this tends to result in the TCP acks for the single flow (in the more plentiful download direction) requiring more bandwidth than the individual flows among the set of 50 (which are on the more restricted upload direction).  We have found this to be a very tough test for flow-isolating AQM qdiscs, as the AQM must drop a very large number of TCP acks to keep the single flow near maximum throughput.  Non-flow-isolating qdiscs often do better on the single flow, but at the expense of aggregate throughput of the 50 flows and of inter-flow latency.

When interpreting the results of this test, we looked only at the overall throughput in each direction, and the induced latency.  Applications which use large flow counts tend to be relatively robust to differences in throughput between individual flows.

{{< figure src="../cake-charts/rrul-50-sfq-small.png" link="../cake-charts/rrul-50-sfq.png" caption="SFQ Bulk" >}}

SFQ gave good throughput in the upload direction, but variable throughput in the download direction, and induced up to 230ms of latency in the sparse measurement flows.  After a protracted startup phase, the download flow achieved about 12Mbps on average, which is somewhat short of what the 20Mbps bandwidth available could ordinarily support.  Nevertheless, this is a better result than we expected from SFQ under these severe conditions.

{{< figure src="../cake-charts/rrul-50-pie-small.png" link="../cake-charts/rrul-50-pie.png" caption="PIE Bulk" >}}

PIE also achieved surprisingly good results here.  During a 5-second startup phase, induced latency climbed to 245ms and download throughput was very low.  After this, PIE appeared to bring the many upload flows under control, making room for the download flow’s acks and controlling induced latency to under 60ms.  Download throughput rose to about 16 Mbps and remained steady for the remainder of the test.

{{< figure src="../cake-charts/rrul-50-codel-small.png" link="../cake-charts/rrul-50-codel.png" caption="Codel Bulk" >}}

The test run using Codel yielded a very incomplete data set, from which no firm conclusions could be drawn.

{{< figure src="../cake-charts/rrul-50-sfb-small.png" link="../cake-charts/rrul-50-sfb.png" caption="SFB Bulk" >}}

SFB performed with typical inconsistency, achieving a reasonable download throughput of about 14Mbps for short periods but then reverting to much lower throughput.  Periods of relatively low induced latency coincided with these periods of relatively good download throughput, but in general SFB’s control of latency was poor, with well over 200ms typically being induced.

{{< figure src="../cake-charts/rrul-50-fq_codel-small.png" link="../cake-charts/rrul-50-fq_codel.png" caption="FQ_Codel Bulk" >}}

FQ_Codel managed to keep induced latency down to about 50ms, even during the startup phase.  However, throughput in the download direction was relatively low and variable, averaging about 7Mbps.  An explanation for this is that Codel uses a sub-optimal rule for determining the drop rate after a short period of sufficiently controlled latency, a deficiency which has been addressed in COBALT.

{{< figure src="../cake-charts/rrul-50-cake-small.png" link="../cake-charts/rrul-50-cake.png" caption="CAKE Bulk" >}}

CAKE and CAKE-Lite achieved identical results, as expected since there is no Diffserv marking in play in this test.  Remarkably, induced latency was kept down to about 5ms throughout.  Steady-state in download throughput was reached only after about 20-25 seconds, during which a steady ramp-up was observed as COBALT determined how many of the download flow’s acks needed to be dropped.  Thereafter, a reasonably steady 12Mbps was delivered in the download direction, as well as a full complement of upload throughput.

{{< figure src="../cake-charts/rrul-50-all-small.png" link="../cake-charts/rrul-50-all.svg" caption="Bulk Summary" >}}
{{< figure src="../cake-charts/rrul-50-icmp-small.png" link="../cake-charts/rrul-50-icmp.svg" caption="Bulk Latency CDF" >}}



Multi-Traffic Workload
----------------------

We constructed a custom Flent workload, to simulate a variety of traffic combinations in sequence, as might be experienced in a typical multi-user household.

During the usual 10-second baseline latency measurement, we additionally begin a VoIP transmission to Host D, which runs throughout the remainder of the test.  This serves as an isochronous load with detailed latency, jitter and packet loss statistics.

We then begin gently with a single basic bulk TCP flow in each direction to Host B.  One minute later, a simulated BitTorrent session is started, using 20 LEDBAT TCPs with the CS1 DSCP set, in each direction, to Host C.  After a further minute, the first bulk TCP stops, leaving the BitTorrent session uncontended for one minute.  Thereafter, first one, then two, then nine basic bulk TCPs start up in both directions, again maintaining stable conditions for one minute each.  These are then joined by a tenth bulk TCP, inappropriately using the EF codepoint.  One minute later, the nine basic TCPs stop, followed a further minute later by the BitTorrent session, and another minute later by the EF flow.  This leaves just the VoIP flow running, which we observe for the final minute of the test as the qdisc returns to quiescence.

None of the above conditions are at all unusual in practical shared-uplink deployments.  We consider that a good QoS system must be able to handle them reasonably.  Ideally, the BitTorrent session should (as its configured LEDBAT algorithm and DSCP intend) be kept largely out of the other traffic while not being completely starved.  Also ideally, the VoIP session should retain low latency, jitter and packet loss throughout.

The test script recorded the VoIP absolute and induced one-way delays (subject to clock drift), VoIP jitter and packet loss, individual basic TCP flow throughputs, total basic TCP throughput, total BitTorrent throughput, and EF flow throughput.  These represent the performance metrics of interest to end-users in the simulated scenarios.

{{< figure src="../cake-charts/multitraffic-sfq-up-small.png" link="../cake-charts/multitraffic-sfq-up.png" caption="SFQ Multitraffic Upload" >}}
{{< figure src="../cake-charts/multitraffic-sfq-down-small.png" link="../cake-charts/multitraffic-sfq-down.png" caption="SFQ Multitraffic Download" >}}
{{< figure src="../cake-charts/multitraffic-sfq-voip-small.png" link="../cake-charts/multitraffic-sfq-voip.png" caption="SFQ Multitraffic VoIP" >}}

SFQ exhibited chaotic behaviour in this test, especially regarding the BitTorrent traffic.  In the “download” direction with plenty of bandwidth available, the BitTorrent session used only a fraction of it even when uncontended, yet competing flows were unable to fill the gap.  In the “upload” direction, the BitTorrent throughput was often recorded wildly in excess of the actual bandwidth available, probably due to the instantaneous releases of pent-up data after head-of-line blocking.  However, the VoIP session was reasonably well protected, incurring no packet loss at all, and gaining a steady 10ms of latency and jitter during the whole period of the BitTorrent session.

{{< figure src="../cake-charts/multitraffic-pie-up-small.png" link="../cake-charts/multitraffic-pie-up.png" caption="PIE Multitraffic Upload" >}}
{{< figure src="../cake-charts/multitraffic-pie-down-small.png" link="../cake-charts/multitraffic-pie-down.png" caption="PIE Multitraffic Download" >}}
{{< figure src="../cake-charts/multitraffic-pie-voip-small.png" link="../cake-charts/multitraffic-pie-voip.png" caption="PIE Multitraffic VoIP" >}}

PIE did much better in terms of total link utilisation in both directions, but gave the BitTorrent traffic far too much of the available bandwidth, effectively causing it to compete on equal terms on a per-flow basis.  Because it does not perform flow isolation, the VoIP delay varied by over 100ms over short time periods, and the AQM signals intended for bulk flows also caused a steady rate of packet loss; this would have noticeably affected call quality.  However, this ceased as soon as the bulk flows were no longer present, demonstrating rapid adaptation to conditions.

{{< figure src="../cake-charts/multitraffic-codel-up-small.png" link="../cake-charts/multitraffic-codel-up.png" caption="Codel Multitraffic Upload" >}}
{{< figure src="../cake-charts/multitraffic-codel-down-small.png" link="../cake-charts/multitraffic-codel-down.png" caption="Codel Multitraffic Download" >}}
{{< figure src="../cake-charts/multitraffic-codel-voip-small.png" link="../cake-charts/multitraffic-codel-voip.png" caption="Codel Multitraffic VoIP" >}}

Codel showed qualitatively similar throughput statistics to PIE in the “upload” direction, but for some reason it demonstrated such poor performance in the “download” direction that large gaps appeared in the Flent data.  In particular, the VoIP stream uniquely recorded several multi-second dropouts with complete packet loss.  We have not identified an explanation for this behaviour.

{{< figure src="../cake-charts/multitraffic-sfb-up-small.png" link="../cake-charts/multitraffic-sfb-up.png" caption="SFB Multitraffic Upload" >}}
{{< figure src="../cake-charts/multitraffic-sfb-down-small.png" link="../cake-charts/multitraffic-sfb-down.png" caption="SFB Multitraffic Download" >}}
{{< figure src="../cake-charts/multitraffic-sfb-voip-small.png" link="../cake-charts/multitraffic-sfb-voip.png" caption="SFB Multitraffic VoIP" >}}

SFB, despite its attempt at pseudo flow-isolation, was unable to protect the VoIP flow adequately.  VoIP packet loss was confined to a short period near the beginning of the BitTorrent session, but induced latency was just as high and variable as with PIE; some latency spikes reached 150ms.  This severe impact on VoIP traffic seems to be a fundamental limitation of AQMs used without true flow isolation.  Link utilisation was also generally poor, with single flows oscillating wildly between full throughput and a small fraction thereof, and there was no discernible advantage given to non-BitTorrent flows.  It is possible that different BLUE parameters might perform better, but investigating this possibility is beyond the scope of this paper since this level of expertise is not reasonably expected of end-users.

{{< figure src="../cake-charts/multitraffic-fq_codel-up-small.png" link="../cake-charts/multitraffic-fq_codel-up.png" caption="FQ_Codel Multitraffic Upload" >}}
{{< figure src="../cake-charts/multitraffic-fq_codel-down-small.png" link="../cake-charts/multitraffic-fq_codel-down.png" caption="FQ_Codel Multitraffic Download" >}}
{{< figure src="../cake-charts/multitraffic-fq_codel-voip-small.png" link="../cake-charts/multitraffic-fq_codel-voip.png" caption="FQ_Codel Multitraffic VoIP" >}}

FQ_Codel behaved considerably better, achieving zero packet loss and a completely negligible induced latency in the VoIP stream.  The bulk flows approached full link utilisation in aggregate, and per-flow equality was firmly enforced during contention, confirming the well-known result with excessive bandwidth allocated to the BitTorrent session.  Single bulk flows tended to oscillate slightly below full link utilisation, a trait apparently common to Codel-based qdiscs.  In comparison to the other qdiscs above, it’s easy to see why fq_codel is widely used, both with and without a priority-queuing layer.

{{< figure src="../cake-charts/multitraffic-cake-be-up-small.png" link="../cake-charts/multitraffic-cake-be-up.png" caption="CAKE-Lite Multitraffic Upload" >}}
{{< figure src="../cake-charts/multitraffic-cake-be-down-small.png" link="../cake-charts/multitraffic-cake-be-down.png" caption="CAKE-Lite Multitraffic Download" >}}
{{< figure src="../cake-charts/multitraffic-cake-be-voip-small.png" link="../cake-charts/multitraffic-cake-be-voip.png" caption="CAKE-Lite Multitraffic VoIP" >}}

CAKE-Lite behaved exactly like fq_codel in all important respects on this test, as expected.  The baseline VoIP delay appears higher, but this is entirely due to clock drift between the two hosts between these two runs; the induced delay and jitter remain negligible and the VoIP packet loss remains nil.  COBALT also appears to be slightly friendlier to single flows than the Codel algorithm embedded in fq_codel, which is interesting in that COBALT is mostly a direct reimplementation of Codel using more concise coding techniques.

{{< figure src="../cake-charts/multitraffic-cake-ds3-up-small.png" link="../cake-charts/multitraffic-cake-ds3-up.png" caption="CAKE Multitraffic Upload" >}}
{{< figure src="../cake-charts/multitraffic-cake-ds3-down-small.png" link="../cake-charts/multitraffic-cake-ds3-down.png" caption="CAKE Multitraffic Download" >}}
{{< figure src="../cake-charts/multitraffic-cake-ds3-voip-small.png" link="../cake-charts/multitraffic-cake-ds3-voip.png" caption="CAKE Multitraffic VoIP" >}}

CAKE in default configuration, with its priority queues active, was the only tested qdisc to correctly deprioritise the BitTorrent session, making use of its CS1 DSCP marking.  It achieved this in both directions simultaneously, with no measurable effect on the VoIP stream (even though this was not specially marked), and while rapidly adapting to the presence or absence of competing traffic to ensure full link utilisation and inter-flow fairness within each traffic class.  Notably, it did so *without* requiring explicit configuration of a set of traffic classes and DSCP recognition filters, as an equivalent HTB+fq_codel system would.

{{< figure src="../cake-charts/multitraffic-icmp-small.png" link="../cake-charts/multitraffic-icmp.svg" caption="Multitraffic Latency CDF" >}}


Conclusions
-----------

The design of CAKE aimed to provide the best of several existing types of QoS system in a single, easily-configured package.  Some improvement in efficiency relative to an equivalent collection of component qdiscs was also hoped for, though not tested for this report.  The results obtained show that design goal has been met, and even exceeded in the cases tested.  This is attributable to the novel combination of tuned algorithms employed in concert.

The performance of PIE, Codel and SFB demonstrates clearly that AQM by itself is insufficient for a home Internet connection, where the high degree of statistical multiplexing commonly relied on in core networks is unavailable.  This applies even with a carefully-tuned, state-of-the-art algorithm (as both PIE and Codel are), or with measures to separate congestion signalling rates per flow (as with SFB).

Likewise, while the venerable SFQ holds up surprisingly well in these tests, it lacks several crucial features needed to attain optimal performance.  Chief among these is the explicit “sparse flow bonus” pioneered in fq_codel and inherited by CAKE, which minimises the likelihood that a latency-sensitive packet will need to wait for several bulk packets before its queue is serviced.  SFQ’s periodic hash perturbation is also something of a liability, and while it has gained an embedded RED implementation relatively recently, the difficulty of configuring this is well-known.

FQ_Codel showed that the combination of flow-isolation and AQM was not only feasible but optimal, and in fact served as the base for CAKE’s implementation.  It does suffer a few shortcomings, such as a high probability of hash collisions, which were not directly exposed by the tests we ran here.  More seriously, it relies on external prompts (such as a separate shaper, or a device driver) to inform it when packets can be delivered, which are usually imperfect.  It is also highly vulnerable to gaming by applications which open several flows for data transfer, and thereby outcompete applications which open connections conservatively.

HTB is the most popular of the external shapers used for implementing QoS schemes on Linux.  We did not use its more advanced features, only its basic functionality as a token-bucket filter with a free choice of child qdisc.  We were able to observe, in even the simplest tests, effects traceable to one of the fundamental limitations of token-bucket shapers - that they cannot be perfectly accurate on short timescales, due to their reliance on a fixed-size “credit pool” which must be exhausted before rate control is achieved.  This is why fq_codel, relying on HTB, repeatedly overcorrected and forced single TCP flows to back off well below the optimum level.  And, of course, a shaper does not by itself constitute a QoS system.

In comparison, CAKE provides a novel deficit-mode shaper which does perform accurately on short timescales, a similar combination of flow-isolation and AQM to fq_codel, and two independent mitigations against the multi-flow gaming problem: a straightforward Diffserv-based priority scheme which requires no end-user expertise, and a “triple-isolation” scheme dividing hosts’ traffic from each other.

Detailed discussions of CAKE’s individual algorithms, in comparison to their common alternatives, will be left to other reports.  It suffices to note that CAKE significantly outperformed, in its default configuration, all challengers we considered, in all of the tests we performed - either in terms of inter-flow induced latency, or average throughput, or the correct allocation of available bandwidth to particular traffic.

