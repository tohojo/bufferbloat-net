
---
title: Getting time from gpsd
date: 2012-03-01T11:12:42
lastmod: 2012-03-01T11:13:36
type: wiki
---
Getting time from gpsd
======================

One concern with bufferbloat is that we would like to analyze the
current performance of ntp's filtering system for 'getting good time',
and also be able to more directly compare the performance of the
internet at the edge to other sampling boxes.

This concept we call 'the cosmic background bufferbloat detector'

A way to do that is to integrate ntp and a set of monitoring tools with
a non-network based timed source, such as gps.

We have got a setup where gpsd can be used to feed time data into a
cerowrt box. We are not at the point where we can actually process that
data, and we have an issue in that getting hyper-accurate time requires
PPS support which so as we can tell, 100% of all gpses no longer
provide... but we're getting there. Regrettably the jitter we get
without PPS support is kind of poor.

To configure gps as a time source...

\# Get a supported gps

\# Locate it near a window that can 'see' enough sats to get a lock

\# install gpsd on a recent cerowrt

    opkg update
    opkg install gpsd
    opkg install cgps # this is optional - you can use this to monitor gpsd on the router itself
    opkg install kmod kmod-usb-serial-ftdi # note - some gpses use kmod-usb-serial-pl2303
    # edit /etc/config/gps and enable listen_globally (and then you can use cgps from anywhere on the network, even over ipv6)

\# Add it as a network time source to /etc/ntp.conf and enable stats
collection

    statsdir /tmp/ntpstats/

    statistics loopstats peerstats clockstats rawstats
    filegen loopstats file loopstats type day enable
    filegen peerstats file peerstats type day enable
    filegen clockstats file clockstats type day enable
    filegen rawstats file rawstats type day enable

    server 127.127.28.0 prefer # this is for a non-pps reference
    fudge 127.127.28.0 time1 0.420 refid GPS
    server 127.127.28.1 # prefer if PPS is working
    fudge 127.127.28.1 refid GPS1

\# Edit /etc/init.d/ntp and add the following lines near the top

    mkdir -p /tmp/ntpstats
    chown ntp.ntp /tmp/ntpstats

\# Restart ntp, restart gpsd

    /etc/init.d/ntpd restart
    /etc/init.d/gpsd restart

There will be two ways to see if it is working. The first is to run cgps
to see if you are getting time, and the second is to look at ntpq to see
if ntp considers it valid. It will take many seconds before it will do
so.

A valid connection will look something like this, where reach is
non-zero.

    ntpq> peers
         remote           refid      st t when poll reach   delay   offset  jitter
    ==============================================================================
    xSHM(0)          .GPS.            0 l    7   64  377    0.000  -9584.2 187.194
     SHM(1)          .GPS1.           0 l    -   64    0    0.000    0.000   0.000
     shipka.bufferbl .STEP.          16 -    -  512    0    0.000    0.000   0.000
    *montblanc.arbor 208.66.175.36    2 u   28   64    7   34.027  -24.421   6.790
    -jefferson.mattw 13.92.113.222    3 u   25   64   17   80.645  -30.243   8.527
    +you.dontlike.us 128.4.40.12      3 u   24   64   17   13.073  -25.993   8.616
     javanese.kjsl.c .STEP.          16 -    -  512    0    0.000    0.000   0.000
    +w1-wdc.ipv4.got 10.0.77.54       4 u   21   64   17   10.738  -28.668   8.759
    -208.94.240.2    108.76.168.146   2 u   20   64   17   53.232  -33.752   8.709
     data0213-1-pt.t .STEP.          16 -    -  512    0    0.000    0.000   0.000

This setup logs data to /tmp/ntpstats which will need to be uploaded and
cleaned out\
periodically.
