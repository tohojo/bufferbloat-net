
---
title: Cerowrt_flashing_instructions
date: 2011-07-09T09:25:57
lastmod: 2014-10-01T10:49:37
---
CeroWrt flashing instructions from a Linux, Mac, or Windows 7 based host
========================================================================

This is how you get CeroWrt running on top of the factory firmware on a
WNDR3800 (or WNDR3700v2, if you can find one. Note - ONLY the
WNDR3700\*v2\* is supported of the 3700 series. Do not attempt to use
the WNDR3700 v1, v3, or v4: they will not work.) The WNDR3800 is still
sold (July 2014), although it seems that mostly refurb units are
available

NOTE: The fastest way to flash a router is to upload the factory cerowrt
image via the default netgear web interface. You can reflash an already
flashed-router using CeroWrt or OpenWrt via the gui interface and the
"sysupgrade" image, but we **strongly** encourage unchecking the
"preserve settings" box when doing so. The syntax of the configuration
databases changes regularly.

You should take a backup before reflashing - the simplest way is to do a
`scp -r root`the.router.ip.addess:/overlay@ which will copy all the
changed files so you can inspect them for differences from a clean
flash. Alternatively, use the config-cerowrt.sh script from
[CeroWrtScripts](https://github.com/richb-hanover/CeroWrtScripts#config-cerowrtsh)
to re-configure your router repeatedly to a known good configuration
each time you flash it.

If you have trouble reflashing from the gui: The tftp method documented
below **always** works...

What image to use?
------------------

Although the CeroWrt build process creates two firmware images, the
truly supported firmware upgrade process is using **TFTP** to load the
**factory** image with **squashfs**. Examples of suitable images for
WNDR3800 and WNDR3700v2 are:

-   openwrt-ar71xx-generic-wndr3800-squashfs-factory.img
-   openwrt-ar71xx-generic-wndr3700v2-squashfs-factory.img

Flashing instruction for Linux
------------------------------

1.  Install a tftp client. 'atftp" seems to work well. *apt-get install
    atftp*
2.  Download the
    [firmware](http://snapon.lab.bufferbloat.net/~cero2/cerowrt/wndr)
    from the current release candidate. Get the "factory" image
    with squashfs.
3.  Temporarily remove your Ethernet port from Network
    Manager's control. To do this:
    -   Right-click the Network Manager icon on your toolbar
    -   Select "Edit Connections"
    -   In the combo box, select your Ethernet port (usually eth0)
    -   Uncheck the "Connect Automatically" box
    -   Click the Apply button (and feed your root password to the
        popup dialog).

4.  Configure an ethernet port on your machine to 192.168.1.2. (command
    is usually *ifconfig eth0 192.168.1.2/24*); *note that if you have
    an USB ethernet device, the device name may not be eth0, but
    something else entirely.*
5.  Connect port 1 on the router to the ethernet port of your computer
    (make sure you are connecting to the router's ethernet port 1, not
    its WAN port!)
6.  Power on the router and force into tftp mode using the following
    sequence:
    1.  Turn over the router and press the "Restore Factory Settings"
        button with a thin object like a paper clip until this sequence
        is complete.
    2.  Turn on the power.
    3.  The light for the port 1, or the port you are plugged into, will
        light up.
    4.  The "connection" light will light up yellow, then flash yellow,
        then turn green and then flash green. This will take a minute
        or more.
    5.  The router is now in "tftp mode" and you can release the
        "Restore Factory Settings" button.

7.  Open terminal on your Linux box and type the following commands to
    flash the router
    -   atftp 192.168.1.1
    -   put <image-file>\
        A successful tftp will simply return no message, a failed one
        will eventually time out and tell you so.

8.  If you see "source port mismatch, check bypassedtimeout:
    retrying...", this probably means that Network Manager has messed
    with your Ethernet port behind your back. Disable it, manually set
    the Ethernet port as before, and try again.
9.  After you have successfully downloaded the image **waiting at least
    5 minutes is KEY**; The router needs to rewrite a lot of flash which
    is very slow... If impatient, go for a walk, have some coffee... or
    do another router. After the tftp succeeds you can disconnect your
    laptop's network cable with no issues, so this will speed your life
    up if you are doing multiple routers. Depending on quantum
    fluctuations, the router may or may not reset - you will see the
    light go solid green in this case...
10. A good indicator of completion is a steady green or yellow light for
    the port you cabled to, together with a steady green power light and
    steady green or blue wireless lights.
11. When you have successfully downloaded the image, hand the port back
    to Network Manager by repeating the steps give above for reaching
    the "Connect automatically" checkbox; check it, and apply
    the change.
12. To test the router's function, Use Network Manager to attempt to
    make a wired connection via your Ethernet port. To do this:
    -   Left-click on your Network Manager icon
    -   Disconnect from your wireless network
    -   Select Auto eth0\
        You should quickly get a notification "Auto eth0:
        Connection established". This indicates that you have
        successfully acquired a DHCP address from the router you just
        flashed, and it is functioning normally.\
        Note: In this state, you probably have no Internet; you will
        want to reconnect to your wireless network in order to get
        it back.

13. (re)Enable dhcp on your machine, get a new address. (it should be in
    the 172.30.42.2-31 range). Or manually assign 172.30.42.11/27 It may
    take a while to get a DHCP address, and you may temporarily see a
    link-local (e.g. 169.254.x.x) address.
14. Continue reading the
    <link>Cerowrt\_flashing\_instructions\#Final-Setup-Steps|Final Setup
    Steps</link> (below).

Flashing Instructions for Mac
-----------------------------

1.  Get a tftp client. There's one on most macs already. Make sure you
    have it first.
2.  Download the [firmware](http://snapon.lab.bufferbloat.net/~cero2/)
    from the current release candidate. Get the "factory" image
    with squashfs.
3.  Configure an ethernet port on your machine to 192.168.1.2.
4.  Connect port 1 on the router to the ethernet port of your computer
    (make sure you are connecting to the router's ethernet port 1, not
    its WAN port!)
5.  Power on the router and force into tftp mode using the following
    sequence:
    1.  Turn over the router and press the "Restore Factory Settings"
        button with a thin object like a paper clip until this sequence
        is complete.
    2.  Turn on the power.
    3.  The light for the port 1, or the port you are plugged into, will
        light up.
    4.  The "connection" light will light up yellow, then flash yellow,
        then turn green and then flash green. This will take a minute
        or more.
    5.  The router is now in "tftp mode" and you can release the
        "Restore Factory Settings" button.

6.  Open terminal on mac and type the following commands to flash the
    router
    -   tftp 192.168.1.1
    -   binary
    -   put <image-file>\
        A successful tftp will usually tell how many bytes were
        transferred and quit. A failed one will eventually time out and
        tell you so.

7.  After you have successfully downloaded the image **waiting at least
    5 minutes is KEY**; The router needs to rewrite a lot of flash which
    is very slow... If you're impatient, go for a walk, have
    some coffee... or do another router. After the tftp succeeds you can
    disconnect your laptop's network cable with no issues, so this will
    speed your life up if you are doing multiple routers. Depending on
    quantum fluctuations, the router may or may not reset - you will see
    the light go solid green in this case...
8.  A good indicator of completion is a steady green or yellow light for
    the port you cabled to, together with a steady green power light and
    steady green or blue wireless lights.
9.  (re)Enable dhcp on your machine, get a new address - it should be in
    the 172.30.42.2-31 range. Or manually assign 172.30.42.11/27 It may
    take a while to get a DHCP address, and you may temporarily see a
    link-local (e.g. 169.254.x.x) address.
10. Continue reading the
    <link>Cerowrt\_flashing\_instructions\#Final-Setup-Steps|Final Setup
    Steps</link> (below)

Flashing Instructions for Windows 7
-----------------------------------

1.  Install a tftp client. Windows 7 includes a basic tftp client, but
    it is not installed by default. To do this:
    1.  Open the Windows Control Panel.
    2.  Select "Programs"
    3.  Select "Turn Windows features on or off" under the heading
        "Programs and Features"
    4.  Check the "TFTP Client" feature and click on "Ok". A window will
        appear for some time saying "Please wait while Windows makes
        changes to features. This might take several minutes." No reboot
        is necessary.

2.  Download the [firmware](http://snapon.lab.bufferbloat.net/~cero2/)
    from the current release candidate. Get the "factory" image
    with squashfs.
3.  Connect port 1 on the router to the ethernet port of your computer
    (make sure you are connecting to the router's ethernet port 1, not
    its WAN port!)
    1.  To be safe, you probably don't want your PC plugged into
        anything else, or on a wireless network, especially one that
        will conflict with the networks that the router may be
        configured with.
        -   192.168.1.0 - The default network that the factory firmware
            defaults to.
        -   172.30.42.0 - The default network that the Cerowrt firmware
            defaults to.

4.  Open a cmd.exe window and navigate to the directory with the
    downloaded firmware.
5.  Prepare a command for running the tftp client with the
    correct parameters. Substitute the IP address and filename in the
    following example appropriately.
    -   tftp -i 192.168.1.1 put
        openwrt-ar71xx-generic-wndr3700v2-squashfs-factory.img

6.  Power on the router and force into tftp mode using the following
    sequence:
    1.  Turn over the router and press the "Restore Factory Settings"
        button with a thin object like a paper clip until this sequence
        is complete.
    2.  Turn on the power.
    3.  The light for the port 1, or the port you are plugged into, will
        light up.
    4.  The "connection" light will light up yellow, then flash yellow,
        then turn green and then flash green. This will take a minute
        or more.
    5.  The router is now in "tftp mode" and you can release the
        "Restore Factory Settings" button.

7.  Configure the ethernet port on your PC to a static IP address
    of 192.168.1.2. To do this:
    1.  Open the Windows start menu using the "Windows" key on your
        keyboard or with the mouse.
    2.  Type "network connections" into the "Search program and
        files" field.
    3.  Select "View network connections" in the search results.
    4.  Right-click on "Local Area Connection" to bring up the context
        menu and select "Properties". If your ethernet port is something
        different, then bring up the properties for that device.
    5.  On the "Network" tab that should appear as the default, select
        "Internet Protocol Version 4 (TCP/IPv4)" in the list labeled
        "This connection uses the following items:" and then click on
        the "Properties" button.
    6.  Under the "General" tab that should have appeared in the
        "Internet Protocol Version 4 (TCP/IPv4) Properties" dialog,
        select the radio button "Use the following IP address:" and set
        the following:
        -   IP address: 192.168.1.2
        -   Subnet mask: 255.255.255.0
        -   Default gateway: 192.168.1.1

    7.  Click on the "Ok" button.
    8.  Leave the property dialog for "Local Area Connection" open to
        make it easier to restore the interface to the
        original configuration.
    9.  You are now ready to upload the firmware to the router

8.  Switch to the pre-configure command line in the "cmd.exe" window and
    run the tftp command. It should only take a couple of seconds
    to complete.
9.  After you have successfully downloaded the image **waiting at least
    5 minutes is KEY**; The router needs to rewrite a lot of flash which
    is very slow... If you're impatient, go for a walk, have
    some coffee... or do another router. After the tftp succeeds you can
    disconnect your laptop's network cable with no issues, so this will
    speed your life up if you are doing multiple routers. Depending on
    quantum fluctuations, the router may or may not reset - you will see
    the light go solid green in this case...
10. A good indicator of completion is a steady green or yellow light for
    the port you cabled to, together with a steady green power light and
    steady green or blue wireless lights.
11. Restore the PC network connection to use DHCP.
    1.  Switch to the property dialog for the "Local Area Connection"
    2.  On the "Network" tab that should appear as the default, select
        "Internet Protocol Version 4 (TCP/IPv4)" in the list labeled
        "This connection uses the following items:" and then click on
        the "Properties" button.
    3.  Under the "General" tab that should have appeared in the
        "Internet Protocol Version 4 (TCP/IPv4) Properties" dialog,
        select the radio button "Obtain and IP address automatically"
        and click on the "Ok" button.

12. If everything went well, your PC should receive a lease from the
    DHCP server on the router. (It should be in the
    172.30.42.2-31 range). Or manually assign 172.30.42.11/27 . It may
    take a while to get a DHCP address, and you may temporarily see a
    link-local (e.g. 169.254.x.x) address.
13. Continue reading the
    <link>Cerowrt\_flashing\_instructions\#Final-Setup-Steps|Final Setup
    Steps</link> (below)

Final Setup Steps
-----------------

1.  Point your Web browser at http://gw.home.lan If that doesn't work,
    try http://172.30.42.1:81
    -   Note: It can take six or seven minutes for the router to
        complete its flash procedure. Don't worry.
    -   Note: You may need to do a shift-refresh (to defeat the
        browser's resolver caching) in order to make the front page come
        up properly.

2.  Click on the 'Administer' Tab. You can safely ignore any SSL Errors
    from your browser: CeroWrt uses a self-signed SSL certificate.
    Proceed to login: the default username is 'root', the default
    password is 'Beatthebloat'. You can also ssh in as root with that
    password, or continue using the web interface. If ssh is being
    refused, or the web interface doesn't come up, it's generally still
    rewriting flash. Be patient...
3.  But if none of this works, power cycle the router and try again. If
    that doesn't work, proceed to step 3 of the procedure for your
    computer to re-flash the router.
4.  Connect the WAN port on the router to your ISP uplink and reboot
    the router.
5.  Return to the <link>Installation Guide</link> for the next steps.

Flashing Instructions "from the router"
---------------------------------------

The following instructions will be helpful if you want to avoid the tftp
install method. It assumes that you can ssh to the router and the
sysupgrade utility is also installed in your router.

1.  Get the image file from
    http://snapon.lab.bufferbloat.net/\~cero2/cerowrt/wndr Choose a
    candidate version number, then download
    openwrt-ar71xx-generic-wndr3800-jffs2-factory.img (or the
    3700v2 version).
2.  If you have an existing openwrt firmware in your router, you will
    need the sysupgrade version from
    http://snapon.lab.bufferbloat.net/\~cero2/cerowrt/wndr (choose
    a candidate)
    openwrt-ar71xx-generic-wndr3700v2-squashfs-sysupgrade.bin, but right
    now you want to wipe out everything, so use the "factory"
    version, above). <link>sysupgrade</link> instructions are elsewhere.
3.  Configure your wired interface to DHCP
4.  Connect port 1 on the router to the ethernet port (make sure you are
    connecting to the router's ethernet port 1, not its WAN port!)
5.  Copy the firmware image to the router's tmp folder. Make sure that
    you copy in the tmp folder, otherwise you'll run out of memory : scp
    openwrt-blah-blah.bin root:/tmp/
6.  Login to the router using ssh.
7.  Go to /tmp/ and upgrade your firmware
8.  sysupgrade -n name-of-your-firmware.bin
9.  Wait for the links to blink. After 2-3 minutes your router
    will install. First boot will take a bit (\~5 minutes), and there
    you go.
10. Make sure you don't unplug the router's power during the upgrade
    process!
11. Point your Web browser at http://gw.home.lan . Click on the
    'Administer' Tab. If that doesn't work, try http://172.30.42.1:81 .
    The default password is 'Beatthebloat'. You can also ssh in as root
    with that, or continue using the web interface. If ssh is being
    refused, or the web interface doesn't come up, it's generally still
    rewriting flash. Be patient...
12. But if none of this works, power cycle the router and try again. If
    that doesn't work, proceed to step 2.
13. Connect the WAN port on the router to your ISP uplink and reboot
    the router.
14. Return to the <link>Installation Guide</link> for the next steps.

