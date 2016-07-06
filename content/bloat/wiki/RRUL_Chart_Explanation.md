---
title: RRUL Chart Explanation
date: 2016-07-06T11:00:00-04:00
lastmod: 2016-07-06T11:00:00-04:00
type: wiki
---

# Explaining RRUL Charts

The [Realtime Response Under Load (RRUL)](RRUL_Spec.md) test performs accurate, automated, and repeatable measurements of network performance. RRUL is especially well suited to measuring induced latency when heavy traffic is present. This latency is often called "bufferbloat".

The charts on this page were created by [Flent,](http://flent.org) a Python program that runs the RRUL (and other) tests and creates graphs of the result. This page is a tutorial for understanding the test results as shown in the RRUL chart.

An RRUL test run saturates the network by initiating eight data connections to/from a netperf server at a remote location (four simultaneous connections sending data in each direction). Each connection has a different diffserv class to compare their performance and fairness. In addition, the RRUL test measures latency across the network with ICMP or UDP pings.

## Sample RRUL Chart before tuning

Here is a sample RRUL chart - it has these plots:

- **Download plot** showing the average download speed (Mbits/sec, in black) of the four diffserv connections (individual colors.) 
- **Upload plot** showing the average upload speed (Mbits/sec, black) of the four diffserv class connections (individual colors) 
- **Latency plot** showing the average latency (msec, in black) of all the connections.
- **Horizontal axis** for all plots is seconds, showing the test duration.

_Note:_ The Download and Upload plots show speeds for _each_ connection: multiply the average by four to get the actual link speeds.

_Note:_ The measured download and upload rates tend to be lower than the full rated speed of the connection. This is because the TCP Ack traffic uses a significant fraction (often as much as 20%) of the capacity in the opposite direction. This does not skew RRUL results, because all tests will have the same testing conditions.

![](/attachments/rrul_chart_campground_pfifo_fast.svg)

**Explanation of the pfifo chart (above)**

The chart above shows results from testing an ordinary cable modem (nominally 20 Mbit/s down, 8 MBit/s up) that uses the common pfifo queueing which does not do any traffic or queue management. It shows several areas of poor performance: 

1. The Download plot shows the average starting around 2.5 Mbit/s. By 30 seconds into the test, it falls to about 0.5 Mbit/s. Only at the end of the test at 60 seconds does the average peak around 4.0 Mbit/s. The average rate across the 60-second test is below 2.0 Mbit/s, or a total of about 8 Mbit/s.
2. The Upload speed is much more consistent, showing about 2 Mbit/s (~8 Mbit/s total) for the entire test run.
3. The Latency plot starts at a few msec when the link is idle, but it rapidly jumps to between 150-250 msec when there is traffic. This latency is the "bufferbloat" that harms network performance.

## After Installing and Configuring SQM

We configured the Smart Queue Management (SQM) facility on the router to control queue lengths within the router. This results in a huge improvement in latency *and* download speeds while sacrificing a very small amount of upload capacity.

![](/attachments/rrul_chart_campground_lupin_qos.svg)

**Explanation of the fq_codel chart (above)**

After applying suitable settings for the SQM in the router (that then feeds the cable modem), the performance is considerably better:

1. The Download speed average is higher, and far more consistent - around 4.2 Mbit/s (total of 16.8 Mbit/s, double the pfifo average of ~8 Mbit/s). 
2. In addition, the bandwidth (download and upload) is shared more evenly between each of the connections (in colors).
3. The Upload speed average is about 1.8 Mbit/s (a bit lower than the 2 Mbit/s of pfifo).
4. The big win is in latency: there is a small increase of 4-8 msec over the baseline idle latency of 16-18 msec during the entire test run. This is a 25x improvement (8 msec vs 200 msec), and would result in dramatically better "feel" to the network.
