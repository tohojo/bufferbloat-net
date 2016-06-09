
---
title: Bismark-steps-jul15
date: 2011-07-15T12:19:49
lastmod: 2011-07-15T16:13:31
---
Bismark Next Steps
==================

**Agenda**

-   DNS-based redirection / Geolocation / BIND+GeoIP
    -   Requirements: Easy to use
-   KVM
-   Router flashing
    -   <link>Parallel device flashing from factory firmware</link>
-   TIE/passive measurement packaging
-   Level3 Deployment
-   Data format/Protobuf
-   TIE + OpenFlow
-   TCP connection splitting w/Polipo
    -   Browser add-on to detect Polipo and set automatically
-   Web 10G Kernel Patch into OpenWRT
-   Wireless measurement: kismet (preferable to airodump-ng)

**Logistics**

-   DNS-based redirection / Geolocation / BIND+GeoIP
    -   Requirements: Easy to use
    -   Is anyone actually maintaining DONAR now? (Jacopo will ask)
-   KVM (or virtual machines)
    -   http://huchra.bufferbloat.net/\~cerowrt/cerowrt-kvm/
    -   http://www.linux-kvm.org/page/Main\_Page
-   TIE/passive measurement packaging: http://tie.comics.unina.it/
-   Router flashing
    -   Need steady supply of WNDR 3700v2 routers for the lifetime of
        the project (18-24 m?)
    -   Free routers?
    -   What routers are coming down the pipe. Broadcom stuff contains
        binary blobs in wifi driver. Will the next version be open?
    -   We love the 3700v2. What’s the direct successor to that?
    -   Can Dave drop in as well?
-   Data format/Protobuf
-   Database
-   Archival
-   TIE + OpenFlow

<!-- -->

-   When, where, and how many to ship routers?
    -   50 initial shipments, as that works, start shipping out more
    -   First shipment: August 7 target, September 1 release date
    -   US near MLab servers/cities, Amsterdam, Paris, Italy, Australia
    -   First publication deadline: Mid-November

**Research on Bismark**

-   Level3 Deployment

<!-- -->

-   TCP connection splitting w/Polipo
    -   Browser add-on to detect Polipo and set automatically
    -   http://www.pps.jussieu.fr/\~jch/software/polipo/
-   Turn connection splitting on and off to see performance difference
    -   Web 10G Kernel Patch into OpenWRT
    -   http://www.web10g.org/index.php?option=com\_content&view=article&id=46&Itemid=67
    -   Wireless measurement: kismet (preferable to airodump-ng)
    -   http://www.dd-wrt.com/wiki/index.php/Kismet\_Server/Drone\#Server\_or\_Drone
    -   http://www.kismetwireless.net/documentation.shtml
    -   What is different from earlier work in the 90s?
        -   Asymmetric access link
        -   Home network wireless
        -   Multiple radios on the home
    -   Initial experiment:
        -   Host web server
        -   wget from home(s) to nearby server
        -   objects of different sizes
        -   explore effects of turning splitting on and off, in terms of
            page download time
        -   start with the experiment in a lab (i.e., here)
        -   explore the effects of different TCP variants in a wireless
            setting

<!-- -->

-   Idea for project: Home network lab in the lab. Simulate Comcast,
    AT&T, WiMax, other effects (powerboost, distance from central
    office, etc.)
    -   Emulating/modeling the home network based on traces gathered in
        the field from Bismark
    -   Use some of Keith’s consumer devices to run inside this type of
        environment

<!-- -->

-   Explore different TCP variants on the router itself (Westwood+,
    Bic, Cubic)
-   Experimenting with different QoS systems
    -   Simulate a family with two teenagers (and all of the activity
        associated with that)
    -   Coexistence of VoIP, BitTorrent, NetFlix, Facebook photo upload
    -   Investigate LEDBAT:
        http://tools.ietf.org/html/draft-ietf-ledbat-congestion-05

**Other bismark features**

-   rsynch of /etc directory - http://kitenet.net/\~joey/code/etckeeper/
-   web toolkit ?

