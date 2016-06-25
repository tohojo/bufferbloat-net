---
title: Bind9 chroot jail and xinetd
date: 2011-09-05T10:48:10
lastmod: 2011-09-05T10:48:10
type: wiki
---
Bind9 chroot jail and xinetd
============================

Many implementations of bind9 start it up in a chroot jail, so as to
reduce the chance of a root compromise.

Our implementation of bind9 not only starts it in a chroot jail, but
runs with reduced privileges AND out of xinetd AND has a configuration
file structure mildly better for usage with a web based interface (not
that we have one).

The xinetd trick is clever in that incoming requests to port 53 will
start bind9 if not already started (or it has crashed).
