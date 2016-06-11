
---
title: Measurement-brainstorm
date: 2011-07-14T13:35:40
lastmod: 2011-07-16T07:49:44
type: wiki
---
Measurement-brainstorm
======================

-   Measurements
    -   Wireless performance in the home
    -   Streaming performance
    -   Low-overhead bandwidth measurements
    -   Passive measurements (what kinds, and how?)
    -   Network neutrality / application performance monitoring
    -   Wireless mesh networking (e.g., getting bismark running on mesh
        potatoes, area deployments)

Inside the Home
---------------

-   Wireless performance
    -   Throughput to wireless devices in the home
    -   Other wireless networks that exist in the "neighborhood" and how
        much traffic is being sent on these networks
-   User behavior
    -   What does "normal" user behavior look like?
-   Application behavior
    -   Automated vs. human-generated traffic (What does "ambient"
        traffic look like?)
    -   How much traffic is inside the home (internal: mDNS, bonjour,
        ARP, internal application traffic) vs. external?
    -   How much traffic is cacheable? (as a follow-up: how would
        caching any or all of this content improve performance?)
    -   How much traffic belongs to different applications? (e.g., is it
        true that 20% of traffic at peak time is NetFlix?)
-   Device inventory and characterization/fingerprinting, including home
    automation devices
-   Do people modify the router itself? (configuration changes?)
-   What other information do applications leak? (monitoring set-top
    boxes for data leaks, etc.)
    -   How much sensitive information is leaked in plaintext?
-   Does the use of a particular application affect the performance of
    others (e.g., on the access link)?
-   Security
    -   "HomeIDS" - perform active and passive measurements to detect
        anomalies (e.g., compromised hosts) inside the home
    -   Splitting snort/bro: generate signatures, but perform signature
        matching "in the cloud". Note: these signatures might have to be
        based on flow statistics if they are exported from the box.
-   Factoring/locating bottlenecks: host, home network, access link,
    peering, server

On the Access Link
------------------

-   Application performance (e.g., Skype, Netflix)
    -   Passive monitoring
    -   Active measurements (of statistics that are relevant to
        the application)
-   Effects of NAT on performance
-   Effects of split TCP on performance (Jacopo is working on this)
-   Are the ISP policies static or dynamic? Within the access network,
    where is each policy applied?
    -   Time-based?
    -   Based on user behavior? Do the ISPs build profiles of users and
        treat each user's traffic differently?
    -   Based on destination? (e.g., do users behind the same head end
        experience different performance/policies than those in
        different locations?)

Topology and Applications
-------------------------

-   What does the topology of the access network look like (e.g., by
    tracerouting from Bismark node to Bismark node)?
    -   Mapping out sup-IP topologies in a region
    -   Which access ISPs peer with one another? Does peering vary by
        region?
-   CDN Performance (Srikanth and Walter are working on this)
    -   What types of tricks do CDNs play in mapping clients to servers?
        What does DNS resolution look like from different geographies
        and providers?
    -   How does a CDN's peering affect the performance that users in
        different access ISPs see?
-   Does fetching content from a peer yield better or worse performance
    than fetching from an origin?
-   Quantifying, measuring, and monitoring
    <link>info-bubbles|"information bubbles"</link> (region-specific
    content, filtering, etc.).
    -   action item: add some wgets to bismark-active for different Web
        servers, somehow do "diffs", upload the results to a portal

Extensions
----------

-   Combination of heavyweight and lightweight bandwidth tests to
    achieve more continuous measurements?
-   Could the same set of measurements be applied on a mobile device?

Next Steps and Other Ideas
--------------------------

-   Get TIE integrated with Bismark
-   Identifying human-generated vs. automated traffic
-   Identifying internal vs. external
    -   Kandula: Expose (learning communication patterns by grouping
        related flows)

