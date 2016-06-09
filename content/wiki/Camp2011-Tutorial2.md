
---
title: Camp2011-Tutorial2
date: 2011-07-12T08:04:19
lastmod: 2011-07-12T09:32:44
---
Tutorial Day 2
==============

### Package Overview

-   Operating systems in the room: Ubuntu 10.04, 10.10, 11.04, Debian
    Squeeze
-   Packages in the source tree
    -   bismark-packages (on github)
    -   Dave's repositories (welcome to clone, but don't call it cerowrt
        if you tweak it beyond recognition)
        -   cerowrt (Dave Taht maintains; read-only is available,
            read-write available on proving yourself): derived from
            OpenWRT
        -   cerofiles
    -   luci (written in lua)
    -   openwrt: core OS (things needed to boot)
    -   packages: part of the openwrt project

### Differences between OpenWRT and CeroWRT

-   overview of git show and recent changes to OpenWRT (currently, 8
    patches differences)
    -   support for reno, bic, cubic, DRR, choke, SFB, etc.
    -   publish the top-most commit of what version you use, and people
        will be able to duplicate your results
-   recommendation: track changes to OpenWRT
-   in openwrt logs: nbd/felix is one of the main openwrt developers
-   to read the logs, cd into each directory and "git log" to see the
    changes

### Pulling Updates and Merging

-   git configuration file: .git/config
    -   what to fetch, and URL to fetch from. can name different
        branches (e.g., openwrt, cerowrt, etc.)
    -   defines a new remote repository "openwrt"
    -   "git pull openwrt master" into the cerowrt directory pulls the
        openwrt patches into the cerowrt directory. (pulls from
        master branch)
-   Presenting example of how to pull openflow into the source tree
    -   feeds.conf sets up pointers to other feeds
        -   e.g., src-git openflow
            git://gitosis.stanford.edu/openflow-openwrt
    -   ./scripts/feeds update pulls all of the packages from things in
        feeds.conf
-   the "env/files" directory: default configuration files into this
    directory
    -   lib/wifi/mac80211.sh" (script that brings up wireless
        by default)
    -   etc/opkg.conf points to Dave's package repository. when doing
        your own build, will have to change this.
    -   ./scripts/env is a useful script for managing different
        environments for the files directory
-   make defconfig
-   make menuconfig (menu-based configuration)
-   vi .config
    -   CONFIG\_PACKAGE\_bismark-active=m (install as module, not as
        part of the build)
-   feed overview (how to get this list?)
    -   bird routing daemon (worth trying out): has BGP, other routing
        protocols
    -   collectd (system statistics monitoring)
    -   busybox: most UNIX utilities bundled into a single executable
        file (10s of MB of utilities into about 600k). can always pull
        from coreutils if you absolutely need it
    -   freeswitch (SIP server)
    -   VPNs: stongswan, etc.
-   ./scripts/feeds install openflow (still has bug) \[or some other
    package\]
-   fire off the build
    -   make -j8 V=99

[Lab Users]({{< relref "wiki/Lab_Users.md" >}})
