---
title: Bismark Tools
date: 2012-03-31T09:00:33
lastmod: 2012-03-31T09:00:33
type: wiki
---
Bismark Tools
=============

### Bismark-active

bismark-active (and its dependencies) is probably the only package\
that's generally relevant. All of the other ones are fairly BISmark\
specific or have privacy/human subjects research implications. You may\
find some of them (i.e. bismark-lua) interesting, however.

Let us know if you've got any questions.

--steve

We've spent some effort making it easier to load packages containing\
temporary experiments on the router, from a changing set of experiments\
published by Georgia Tech, as well as allowing users to opt
into/install\
these packages on their own. This is provided by:

bismark-experiments-manager\
bismark-updater

Packages with names ending with '-tmpfs' are installed on /tmp, and so\
can be installed/updated frequently. bismark-updater handles updating\
experiments packages and other packages identified for update\
automatically.

Active measurements are essentially the same, except we have a -tmpfs\
package for the experiment manager above:

bismark-active\
bismark-active-tmpfs

We've ditched scp in favor of a POST to an HTTP URL for data\
transmission back to Georgia Tech. This is provided by:

bismark-data-transmit

BISmark on-router web pages -- same idea as cerowrt-chrome:

bismark-chrome

Our Lua libraries (bmlua.\*):

bismark-lua

Management/remote control stuff -- bdm prober, ssh key, and ssh tunnel\
setup stuff, as before:

bismark-mgmt

Metapackages to pull in a bunch of network measurement tool packages
and\
other useful tools, respectively -- see the DEPENDS:

bismark-netexp\
bismark-extras

\#\#\# NOTE WELL -- PLEASE *DO NOT* BUILD THE FOLLOWING:\
\#\#\#

\#\#\# The following three packages, containing 'passive' in their name,

\#\#\# require documented consent of users to participate in a Georgia
Tech

\#\#\# research project associated with software packages. Please do not

\#\#\# build these or make them available. If you know of someone

\#\#\# interested in these projects, please have them contact us to

\#\#\# participate.\
\#\#\#

\#\#\# These two packages gather information passively from traffic
passing

\#\#\# through br-lan, including MAC addresses, packet size and arrival

\#\#\# times, and volumes of traffic to/from particular ports and

\#\#\# particular (whitelisted) domains. "http-url" also includes a hash
of

\#\#\# the URL for HTTP traffic.\
\#\#\#

\#\#\# bismark-passive-http-url-tmpfs

\#\#\# bismark-passive-tmpfs\
\#\#\#

\#\#\# ucap is a tool that allows users to manage bandwidth caps in the
home

\#\#\# network using openflow -- it also does passive traffic analysis.\
\#\#\#

\#\#\# bismark-passive-ucap

Deprecated (and we should remove them):

bismark-chrome-new\
bismark-lite
