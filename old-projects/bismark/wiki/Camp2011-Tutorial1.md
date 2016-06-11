
---
title: Camp2011-Tutorial1
date: 2011-07-11T08:49:33
lastmod: 2011-07-11T09:10:05
type: wiki
---
Tutorial Day 1
==============

-   **Goal:** Get familiar with router, familiarize with build

### Overview and Setup

-   Current build at: http://143.215.100.236/\~d/cerowrt-wndr3700/
-   Grab build\_cero.sh from here:
    http://143.215.100.236/\~d/gatech/build\_cero.sh
-   Notes about images:
    -   factory-NA image no longer functions. v2 bootloader only
        functions with the regular factory image
    -   squashfs is read-only. jffs is read-write

### Initiate build

-   make sure the following development tools are installed:
    -   build-essential
    -   gawk
    -   flex
    -   at
-   set up git username
    -   git config --global user.name "Your Name" (replace with
        your name)
    -   git config --global user.email "user@host.com" (replace with
        your email address)
-   ./build\_cero.sh init
    -   (temporary bug fix): cp blessed\_config src/cerowrt/.config
-   cd src/cerowrt/
-   make (use batch to be nice)
    -   make -j8 V=99
    -   make V=99
-   wait (build can take 45-60 minutes on huchra)

### Install the build

-   Use the image you just built, or pull down from the bufferbloat site
-   Follow [these
    instructions](http://www.bufferbloat.net/projects/cerowrt/wiki/OCEAN_CITY_INSTALLATION_GUIDE)

