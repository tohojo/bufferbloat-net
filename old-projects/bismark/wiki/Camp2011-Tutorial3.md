
---
title: Camp2011-Tutorial3
date: 2011-07-13T09:03:55
lastmod: 2011-07-13T10:17:20
type: wiki
---
Tutorial Day 3
==============

### Setting Up OpenWRT Toolchain and Building Your Own Packages From Scratch

-   Grab git repositories to create a local version of the repository
    -   openwrt
    -   packages
    -   openflow
-   Update feeds.conf to point to local repositories (use src-link to
    point to local file repositories)
-   Update your feeds
    -   ./scripts/feeds update - updates feeds in the feeds directory
        using {svn, git, local filesystem, etc.}
-   Install some feeds
    -   ./scripts/feeds install {openflow, bismark}
    -   ./scripts/feeds install -p custom ditg
-   set up "files" for any files to be installed on the root filesystem
-   make menuconfig
-   make -j8

### Setting Up OpenWRT Toolchain on dp4.gtnoise.net

-   Update feeds.conf to point to local repositories
-   Update and Install feeds
-   Symlink files to /data/users/bismark/

