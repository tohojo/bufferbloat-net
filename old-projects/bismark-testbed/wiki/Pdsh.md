
---
title: Pdsh
date: 2011-05-28T11:35:15
lastmod: 2011-05-28T11:51:22
type: wiki
---
Pdsh
====

The parallel distributed shell:

https://computing.llnl.gov/linux/pdsh.html

To use it, your public key needs to be in authorized\_keys on the
routers for 'root',\
and you need to set several variables appropropriately via

. /etc/profile.d/pdsh

configured (at present) with a /etc/genders file of:

    dtaht@metis:~$ cat /etc/genders 
    # slc cluster genders file
    # '%n' substitutes nodename into value
    #slci,slcj,slc[0-15]  eth2=e%n,cluster=slc,all
    dp4  squeeze
    metis,callisto  squeeze
    metis,callisto  mgmt,debian
    # There are still two routers MIA
    aitne,io,thebe,leda,elara             routers,openwrt
    jupiter gw,openwrt

See <link>Experiment - QoS</link> as one example of advanced usage.
