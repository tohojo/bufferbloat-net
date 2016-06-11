
---
title: Setting up a wndr3700 toolchain at home
date: 2011-04-16T07:23:25
lastmod: 2011-04-29T19:19:08
type: wiki
---
Setting up a wndr3700 toolchain at home
=======================================

These instructions are for setting up a toolchain on your **own**
machine assuming you have an <link>account on
huchra.bufferbloat.net</link> and <link>ssh configured on port
222</link>.

    cd ~
    mkdir src
    cd src/
    git clone --bare git://nbd.name/openwrt.git openwrt
    git clone --reference openwrt ssh://bismark@huchra.bufferbloat.net/home/bismark/src/wndr3700 wndr3700
    git clone ssh://bismark@huchra.bufferbloat.net/home/bismark/bin bismark-bin
    #If you are planning on doing multiple branches it pays to have a common download directory
    mkdir ~/dl ~/bin
    cd wndr3700
    ln -s ~bismark/dl .
    ln -s ~bismark/bin/install_std_packages ~/bin
    scp bismark@huchra.bufferbloat.net:/home/bismark/src/wndr3700/feeds.conf .

    #less feeds.conf #if you wish to look at what's in there
    ~/bin/install_std_packages
    #(this script basically installs the following, and may be more up to date)
    # ./scripts/feeds update
    # bash webif webif-theme-xwrt radvd polipo samba3 curl bing babeld qos-scripts
    # fping tcpdump  tcptraceroute netperf install ntpd-ssl ntpdate l7-protocols 
    # ddns-scripts iperf gnupg ipv6calc
    # copying this late this makes sure your packages will be built 
    scp bismark@huchra.bufferbloat.net:/home/bismark/src/wndr3700/.config .
    make menuconfig # look around and save new version
    echo make -jHOWEVER_MANY_CPUS_YOU_WANT_TO_USE_UP | batch

1.  Wait for email to your account on your machine, Or setup a
    \~/.forward file to send elsewhere (using batch lowers the priority
    somewhat so your machine will still be usable... but the first build
    takes a VERY long time... go to lunch... batch will NOT start if
    your machine is already busy with other work. running the atq
    utility will show your job with a "=" sign if it is running)
2.  You must remain connected to the internet for the first build, and
    any time you update packages or trees

Coping with updates
-------------------

Periodically you should do a

    cd ~/src
    cd bismark-bin; git pull; cd ..
    cd openwrt; git pull; cd .. #optionally do a git log to see what has changed before and after
    cd wndr3700; git pull; ./scripts/feeds update
    # and also look at the .config in the main repo and 

Note that for serious changes to openwrt you will obsolete the kernel on
the router and will no longer be able to use opkg to install your
generated packages. You can usually do a feeds update safely without
breaking an existing router.

You can customize your <link>uberwrt:openwrt build overlays</link> to
make your default install come closer to "just working".

See also <link>Working within the bismark feed</link> and <link>Pushing
out changes to bismark</link> for details on how to get your package
updates into the\
main repos.
