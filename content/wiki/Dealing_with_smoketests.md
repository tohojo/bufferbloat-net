
---
title: Dealing_with_smoketests
date: 2011-09-15T17:06:20
lastmod: 2011-09-15T17:06:20
---
Dealing with smoketests, release candidates and the final release
=================================================================

The cerowrt development process is broken up into three phases -
smoketests, release candidates, and eventual release.

Smoketests
----------

The smoketests will one day be daily automated builds. At present they
are tests against fixed bugs, mostly.\
YMMV. Do NOT work against a smoketest for anything serious.

A principal problem with smoketests is that they are totally unsupported
and the package database\
points at the rc catagory they will be. To get the additional packages
you will need to point /etc/opkg.conf to the correct\
the smoketest build directory.

Release candidates
------------------

Release candidates are the more polished, fully tested versions of
cerowrt as we march down towards a release.

When will we get Cerowrt 1.0?
-----------------------------

When all priority 1 and 2 bugs are fixed on the roadmap. Our hope was
september 15, but we've missed that date considerably.

Oct 15 would be a good date to aim for.
