
---
title: Huchra_openwrt_build_procedure
date: 2011-05-13T07:08:39
lastmod: 2011-05-13T07:11:18
---
Huchra openwrt build procedure
==============================

When working on a bismark package on huchra
-------------------------------------------

Login as bismark\
cd \~bismark/src/bismark-packages\
make the change to the package\
update the version number in its makefile\
git commit -a \# the change\
cd \~bismark/src/capetown-wndr3700v2\
./scripts/feeds update \# you will see your package pulled\
make package/whateveritis/{compile,install} V=99

(e.g. Wash, rinse, repeat until it compiles and installs)

to get it into the package repo\
echo make -j 8 | batch
--------------------------------

1.  wait for email to the bismark account, read email in mutt with the
    log\
    On your client box

opkg update the\_package @ FROM HUCHRA in your opkg repo @

AFTER you are shure it is working, push it out to the main repositories

`echo ~bismark/bin/sync_repos | batch`

UPDATE THE BUG on the wiki
