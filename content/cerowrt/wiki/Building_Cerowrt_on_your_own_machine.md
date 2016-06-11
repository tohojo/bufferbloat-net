
---
title: Building Cerowrt on your own machine
date: 2011-07-31T10:33:54
lastmod: 2013-06-27T12:31:45
type: wiki
---
Building Cerowrt on your own Linux machine
==========================================

**NOTE:** These instructions are totally out of date and have been
replaced with a new script.

Prerequisites
-------------

You need some packages that you may download the sources. Then you need
some build dependencies to be satisfied. Then you need to checkout the
sources.

    sudo apt-get install git-all subversion build-essential flex libncurses5-dev libz-dev gawk gettext bison texinfo
    mkdir -p ~/src/prep ~/src/cerowrt
    cd ~/src/prep
    git clone git://github.com/dtaht/cerofiles-3.3.git

There will be a **build\_cero.sh** script in that checkout. There is
also a **cero\_config** file here. Copy **cero\_config** to **\~/.cero**
and then edit it to suit your preferences.

    cp cerofiles-3.3/cero_config ~/.cero
    vim ~/.cero # use the editor you are comfortable with

This example assumes the use of folder **\~/src/cerowrt** as main
directory so you should change the **CERO\_DIR** variable to

    CERO_DIR=~/src/cerowrt

then run

    ~/src/prep/cerofiles-3.3/build_cero.sh init
    cd ~/src/cerowrt
    # in there will be your checked out dir, usually wndr3700v2, cd into that
    make # But please see note below for an extra step to save on download hassles

The first time you run this it will take a VERY long time to build the
toolchains, etc. I have generally found -jX to fail on large numbers of
processors, so just build it in series and go to a long dinner or lunch.
Or...

    make -jX
    make V=s

Subsequent runs will be much faster, and -jX usually works. When it
doesn't...

    make package/the_breaking_package/{clean,compile,install} V=99 

usually will work or show the problem.

**NOTE** With kernel.org down last year it was impossible to get a build
to summon and compile all the needed packages. There is a temporary
mirror of the needed packages available via rsync. It's still faster to
just snag all the tarballs this way, so... inside the build dir above:

     
    mkdir dl; cd dl; rsync -av huchra.bufferbloat.net::dl .

(this is a temporary expedient and not actually necessary in normal use)

Check your build
----------------

If the wndr3700's bin/ar71xx/ has images that are less than 5MB, you
didn't get a good .config file, and/or some major packages are missing,
and/or the phase of the moon was wrong.

Your final images should be about the same size as on huchra.

Notes:
------

Given that this builds most of cerowrt against the main git head trees,
your build will differ somewhat from what we are making available as
[release candidates](http://huchra.bufferbloat.net/~cero1/) at present.
After we get stable, we will tag and freeze the relevant trees.

We note that due to this difference, there may be slight (or even major)
differences in the default .config file. It helps to repeatedly cp
env/.config onto .config and run make defconfig, and install packages,
etc, until they more closely match.

We will improve this script as time goes on, and if you run into
trouble, please contact the \#bufferbloat irc channel and/or the mailing
lists.

Keeping updated
---------------

The procedure above makes it possible to track all or parts of openwrt
and cerowrt, by keeping multiple repositories around.\
You can,for example, merely track ceropackages, by doing a git pull in
the ceropackages directory and a ./scripts/feeds update in your build
directory. Or setup something to track the mainline repos (this is what
I do), do integration, and builds, and not bother the ongoing work in
your release process. Doing continuous integration is difficult, but
necessary if you wish to advance the state of the art.

[changing your cerowrt ip addresses]({{< relref "cerowrt/wiki/Changing_your_cerowrt_ip_addresses.md" >}}) <link>changing your dns
domain</link>
