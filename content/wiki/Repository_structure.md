
---
title: Repository_structure
date: 2011-05-28T06:39:42
lastmod: 2011-05-28T06:40:16
---
Repository structure
====================

Today
-----

Presently, the repository structure on huchra is as follows:

src/openwrt - a checkout originally from cerowrt, now a checkout from
openwrt

src/capetown-wndr3700 - a git repo that -references the openwrt repo but
has a few things of it's own that need to become pushed up to openwrt or
pushed back into cerowrt.

src/capetown-wndr3700/feeds/{xwrt,packages,bismark-packages,cerowrt}:
various sub checkouts of stuff included in the final build

src/bismark-packages - the packages specific to bismark

src/bismark-chrome - the web site on the router itself

src/dashboarddb - the database sql and some of the web site

The above are all in git. There are a jillion other repos no longer in
use, including the wndr one we started with, and (failed) attempts at
building capetown for the buffalo and others.

Additionally, there is an svn repo

src/bismark

from which the bismark-active and bismark-mgmt packages are generated.

...

Future
------

Making this mildly more sane would be useful.
