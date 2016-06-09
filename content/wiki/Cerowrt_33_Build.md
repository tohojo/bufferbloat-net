
---
title: Cerowrt 33 Build
date: 2012-02-11T09:29:35
lastmod: 2012-02-11T09:47:03
---
Cerowrt 33 Build
================

THIS IS A DRAFT on a rapidly changing procedure

what is feeds.conf?
===================

Openwrt uses multiple package databases, which gives you flexibility as
to what software you use, where.\
Feeds.conf is a pointer to each package database wherever it might live.
In my case I tend to use\
a staging area for each package database, rather than pulling directly
from the main repositories.\
This lets me do multiple different builds for different hardware without
having to 'push up'\
potentially incorrect packages to the mainline.

What did you do when you edited it?
-----------------------------------

I changed the paths to point to your home dir rather than mine

what do 'feeds update' and 'feeds install' do exactly?
------------------------------------------------------

./script/feeds update calls the appropriate update utility for each
package repository, to get the freshest bits.\
for example, it calls 'git pull' for git repos, and 'svn up' for svn
repos.

./script/feeds install package package package

installs symbolic links to the build system for each package

feeds install -p feedname package

at least in theory installs a package that is a duplicate of some other
package in some other repo.\
It's usable for when you have a more advanced package in a different
repo and want to use that instead.

what is "env new each"?
=======================

This created your own branch of the filesystem to play in. For example,
you\
might want to change the default download dir for packages in your own
build\
by editing env/files/etc/opkg.conf

what is stuff.tgz?
------------------

This was a temporary tarball of the current cerowrt filesystem. In the
future\
it and it's tags and branches will be public.

when you did the git add; git commit -m 'each tree', what was that about?
-------------------------------------------------------------------------

what is 'dl'?
=============

The dl directory is where tarballs of sourcecode lives. Openwrt does not
carry copies of all the source it builds. It relies on external
repositories to keep the 2+ gbyte of that. In order to speed up builds,
I tend to symlink this directory to ONE directory elsewhere, so that I
can maintain multiple versions of the cerowrt builds\
and only one copy of this huge directory.

what did you do in .config?
===========================

Checked for correctness. I think I also added a few packages that are
not in the main packages.list.

what's make menuconfig?
=======================

Menuconfig lets you via a menu interface add packages to build, remove
packages, and configure various options.\
It is a very good idea when making manual changes to .config to run make
menuconfig to make sure all the\
dependencies are pulled in correctly. It also does essential syntax
checking.

if you just want something scriptable, make (can't remember) - will
rebuild the dependencies for you without\
invoking any menus.

why did you run make menuconfig multiple times?
===============================================

It's a good idea to clean up and compare the .config file vs the
supplied one until it is correct.

what you were editing in linux/ar71xx?
======================================

In this case, I am building against 3.3, not 3.2.5, so I changed the
makefile to point at the current release candidate for Linux 3.3 -
3.3-rc3

Basic steps to build cerowrt-3.3
================================


    mkdir src
    cd src
    git clone git://nbd.name/openwrt.git # the main openwrt repository
    git clone git://nbd.name/packages.git # the main additional packages database 
    git clone git@github.com:dtaht/ceropackages.git # cerowrt's added packages
    git clone git@github.com:dtaht/cerowrt-luci.git luci # cerowrt's web gui interface
    git clone git://github.com/bismark-devel/bismark-packages.git # bismark's monitoring tools 
    git clone git://github.com/yiannisy/openflow-openwrt-bismark.git # openflow tools
    git clone openwrt cerowrt-3.3
    mkdir patches
    cd patches
    cp /tmp/evanpatch/* .
    cd ..
    cd cerowrt-3.3/
    mkdir dl
    cp /tmp/feeds.conf .
    vi feeds.conf
    cd ..
    cd cerowrt-3.3/

    ./scripts/env new each  # create a new filesystem 
    cd env
    tar xvzf /tmp/stuff.tgz # presently the cerowrt filesystem is NOT in public git
    git add *
    # in the future the above two steps would be
    # git remote add wherever git://wherever
    # git pull remote wherever release-tag
    git commit -a -m 'each tree'
    cd ..
    chmod a+rwx dl
    cd dl
    ./scripts/feeds update
    cp env/config-wndr3700v2 .config # do this to keep openwrt's build unconfused
    git am ../patches/*
    vi target/linux/ar71xx/Makefile # Add current kernel version (3.3-rc3 in this case)
    ./scripts/feeds install -p cero `cat env/override.list`
    ./scripts/feeds install `cat env/packages.list`
    cp env/config-wndr3700v2 .config
    make menuconfig
    diff .config env/config-wndr3700v2
    vi .config # enable missing packages
    ./scripts feeds install whatever is missing
    wash, rinse, repeat
    make -j 8 
    make V=99
    fix errors
