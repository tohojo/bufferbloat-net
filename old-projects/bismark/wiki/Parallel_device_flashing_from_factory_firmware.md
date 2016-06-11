
---
title: Parallel device flashing from factory firmware
date: 2011-07-15T11:54:54
lastmod: 2011-07-15T14:41:05
type: wiki
---
Parallel device flashing from factory firmware
==============================================

### Brainstorming:

-   Use 48 port Pronto switch with unique VLANs for each interface
-   Connect linux box (VM) to the Pronto trunk/uplink port
-   Create virtual interfaces for each VLAN and statically number each
    interface from a separate /24 out of 172.16 or something
-   Statically configure IP routing table for each separate /24 as given
    above??
-   Use iptables MANGLE to rewrite source and destination addresses to
    be compatible with Netgear??
-   Run 48 processes (one per interface/IP address) that ping the device
    to check if it is up and then perform the upgrade/configuration/test

### Upgrade/configuration/test

-   the firmware upgrade/flash (using a scripted HTTP agent that logs
    into the Netgear admin interface and upgrades the device)
-   device-specific configuration (SSH keys, unique password,
    identifiers, etc.)
-   post-flash testing

