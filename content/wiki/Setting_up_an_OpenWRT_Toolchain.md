
---
title: Setting up an OpenWRT Toolchain
date: 2011-04-08T13:19:36
lastmod: 2011-05-28T06:39:07
---
Setting up an OpenWRT Toolchain (on huchra)
===========================================

[Repository structure]({{< relref "wiki/Repository_structure.md" >}})

These instructions are for setting up a toolchain assuming you have an
account on huchra.bufferbloat.net.\
If you wish to do development on your laptop or another machine, here
are instructions for [setting up a wndr3700 toolchain at home]({{< relref "wiki/Setting_up_a_wndr3700_toolchain_at_home.md" >}}).

Go to wherever you want the toolchain (on huchra) and run the following
commands:

    mkdir src
    cd src/
    git clone /home/bismark/src/wndr3700 wndr3700
    cd wndr3700/
    ln -s /home/bismark/dl/ .
    cp /home/bismark/src/wndr3700/feeds.conf ./
    less feeds.conf

    /home/bismark/bin/install_std_packages

    (this script basically installs the following, and may be more up to date)
    # ./scripts/feeds install bash webif webif-theme-xwrt radvd polipo samba3 curl bing
    # ./scripts/feeds install babeld qos-scripts fping tcpdump  tcptraceroute netperf
    # ./scripts/feeds install ntpd-ssl ntpdate l7-protocols ddns-scripts iperf gnupg ipv6calc

    cp /home/bismark/src/wndr3700/.config ./ # this makes sure your packages will be built
    make menuconfig
    echo make -j8 | batch
    # wait for email to your account there, Or setup a .forward file to send elsewhere
