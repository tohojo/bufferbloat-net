
---
title: Flashing instruction for Linux
date: 2011-05-28T07:47:25
lastmod: 2011-07-18T15:06:42
type: wiki
---
Flashing Instructions for Linux
===============================

1.  Get the image file - **pay attention to the version number**. (It's
    on the back of the router, after WNDR3700. If no v\#, then v1)
2.  Image file for North-America is \*~~NA\*~~ see
    http://www.networkdashboard.org/downloads/capetown/capetown-wndr3700v2/
    for the files (remember that you need a different image for the two
    different models. If you are doing a sysupgrade you will need the
    sysupgrade version, if you want to wipe out everything, use the
    "factory" version) (and if you are overseas, don't use the
    NA version)
3.  Configure an ethernet port on your machine to 192.168.1.2.
4.  Connect port 1 on the router to the ethernet port (make sure you are
    connecting to the router's ethernet port 1, not its WAN port!)
5.  Hold down the "factory reset" button on the bottom of the router.
6.  Turn on the router. Light 1 will light up green; the connection
    light will light up yellow, flash yellow, turn green, then
    flash green. This takes over a minute.
7.  Release reset button
8.  Open terminal on your Linux box and type the following commands to
    flash the router
    -   atftp 192.168.1.1
    -   put <image-file>\
        A successful tftp will simply return no message, a failed one
        will eventually time out and tell you so. **Waiting at least 5
        minutes is KEY**; The router needs to rewrite a lot of flash
        which is very slow... If impatient, go for a walk, have
        some coffee... or do another router (after the tftp succeeds you
        can disconnect your laptop's network cable with no issues, so
        this will speed your life up if you are doing multiple routers)
        Depending on background radiation, the router may or may not
        reset - you will see the light go solid green in this case...

9.  Configure an Ethernet port on your machine to 192.168.42.2
10. Point your Web browser at http://192.168.42.1:81 . It will ask you
    to create a new password. If that doesn't work, power cycle the
    router and try again. If that doesn't work, proceed to step 2. The
    router will ask you to create a new password. After you set the
    password, telnet is disabled. You can ssh in as root with password
    or continue using the web interface
11. Connect the WAN port on the router to your ISP uplink and reboot
    the router.
12. See <link>Further Configuration for wndr3700</link> for the next
    steps

