
---
title: Ssh configured on port 222
date: 2011-04-19T05:50:01
lastmod: 2011-04-19T05:52:02
type: wiki
---
Ssh configured on port 222
==========================

Script kiddies hammer the standard ssh port (22) these days. To
alleviate this, we have ssh on port 222, which will not stop directed
attacks but eliminates the automated ones.

Many things (shell access, git) depend on ssh being on a standard port,
and while you can specify the port as part of the url or command line,
there is an easier way that makes the port change transparent. Simply
add to your \~/.ssh/config file:

`Host *.bufferbloat.net
    Port 222`

If you are not in a position to do that, ssh -p 222 the\_site works, as
does scp -P 222 the\_site:whatever .\
(the -p vs -P issue is old cruft going back decades)

Similarly you can specify the port number as part of a git clone
ssh://huchra.bufferbloat.net:222/home/whatever operation...

but it's easier to modify your .ssh/config as per the above!
