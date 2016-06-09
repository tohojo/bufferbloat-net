
---
title: OCEAN CITY INSTALLATION GUIDE
date: 2011-06-24T13:40:51
lastmod: 2012-06-20T05:49:32
---
CeroWrt 'Ocean City' INSTALLATION GUIDE
=======================================

![](flanders320fade.jpg)

### THIS DOCUMENT IS OBSOLETE

OCEAN CITY was a milestone release for late 2011. For more information
about its goals, see the <link>OCEAN CITY</link> page.

It would be a good idea to print out these instructions before
proceeding. If your router has already been flashed with Cerowrt
firmware, so you can proceed to Step 1 ("Configuring and Installing the
Router") below.

Step 0. Flashing the router
---------------------------

Please see the <link>Cerowrt flashing instructions</link> for how to
install the current CeroWrt build on your
<link>bismark:Wndr3700v2</link> Router from your platform of choice
(windows, osx, linux).

Step 1. Configuring and Installing the Router
---------------------------------------------

1.  **Power on your router.** The router should boot in under
    two minutes. It takes a lot longer the first time as it has to fully
    check flash for errors. The router itself comes up on 172.30.42.1.
    (**NOTE** RC6 and prior releases come up on .33!) The router serves
    IP addresses on 172.30.42.0/27 networks by default. (see
    <link>bismark:why .42</link>?)
2.  **Connect to your router.** Plug in a laptop or computer to one of
    the 4 LAN ports on the router, and refresh your laptop/computer's
    DHCP IP address. Alternatively, connect via wireless by setting your
    SSID to "CEROwrt" (no SSID password) or "CEROwrt5". Your machine
    should get an IP address from the 172.30.42.0/27 subnet in the first
    case, other networks in the second and third.
3.  **Configure your router's default password.** In your web browser,
    go to the router configuration screen at http://172.30.42.1:81 (see
    also <link>bismark:why 81</link>?). The default password
    is 'Beatthebloat'. Go to the System/Administration screen and enter
    in a new password for the router. **Write this password
    down somewhere.** The login will be "root", and the password that
    you set should be something difficult. Note you can also just go to
    gw.home.lan for most things, once DNS is up.
4.  **Secure your wireless interfaces** Go to the *Network-&gt;Wireless*
    configuration page, and change the SSIDs of the various interfaces
    to suit your liking. (See also <link>OCEAN\_CITY\_FAQ|FAQ</link>)
    Enable WPA2 encryption on the LAN interfaces, and if you wish your
    guest interfaces to be secured, do the same there, too. Choose
    unique passwords for the lan and guest interfaces.
5.  **Set your country.** If you are not in the US, please set your
    country for both radios to the correct country in order to ensure
    regulatory compliance.
6.  **SAVE and APPLY.** At the bottom part of the Web interface, *save*
    and *apply* the changes (these are two distinct steps).
7.  **Reboot the router.** You will need to reboot the router for SSH
    and the Internet to come up. Reboot and connect the WAN interface to
    the Internet (i.e., to your DSL or Cable modem). Wait a few minutes,
    and refresh your laptop/computer's DHCP address.

Hopefully at this point you are on the Internet.

Important Configuration Notes:

-   The wireless interfaces are configured as **open** (no password)
    by default. They are also set to the **United States regulatory
    wireless spectrum** by default. You should address these issues
    before connecting the router to the Internet.
-   <link>QoS</link> is turned **OFF** by default.(see
    <link>OCEAN\_CITY\_FAQ|FAQ</link>). You should address this issue
    after connecting to the internet.

Step 2. Fine-tuning your QoS Settings
-------------------------------------

By default, the Ocean City release CeroWrt Router is configured for slow
Internet connections. See the <link>OCEAN CITY FAQ|FAQ</link> for how to
set it appropriately for your network connection. This is a very
important step!

Changing your default IP addresses
----------------------------------

We really don't recommend you change the <link>default network
numbering</link> unless you know what you are doing. Seriously. Don't
mess with it.

But: If you wish to use other default IP addresses... we recommend
against using 192.168.0.1 and 192.168.1.1 for historical reasons. It
would be cool if you would co-ordinate with us on a <link>172.16.0.0/12
allocation|Bloat-net</link> to make vpns easier to play with...

Go to the *Network* screen on the router and change to suit. By default
the secured interfaces come up on the 172.30.42.32/27 (33),
172.30.42.64/27 (65), 172.30.42.96/27 (97). addresses, and the guest
networks come up on 172.30.42.129 and 160 - the mesh network is disabled
by default.You will also need to change the firewall rules, the
/etc/xinetd.conf file and many files below /etc/chroot/named/etc/bind/

It is FAR easier to change these via editing the relevant files directly
on the router, or <link>Changing\_your\_cerowrt\_ip\_addresses|with a
sed script</link>, or, as we have DNS, just use that and don't worry
about the numbers.... (have we scared you enough yet? There will be a
better web interface for renumbering at some point. If you must change
the addresses or dns, here is a
<link>Changing\_your\_cerowrt\_ip\_addresses|link to how to
comprehensively change your ips on the command line</link>.

*Important:* If you change the default IP address, your Web interface
will change at this point to be whatever-you-chose:81 after doing a save
and apply, and you will need to change the url in your browser
accordingly.

Thanks!
-------

You should now be on the Internet using the latest and greatest code
from the <link>cerowrt:Wiki|Cerowrt</link> Project, the
<link>bloat:Wiki|Bufferbloat uberwrt</link> project, and
[OpenWrt](http://www.openwrt.org) .

We hope that your experience will be exceptional. Please send us your
feedback and comments by [registering on the
wiki](http://www.bufferbloat.net/register) and posting to the
[bloat-devel](http://lists.bufferbloat.net/listinfo/bloat-devel) mailing
list. You can also file bugs and feature requests in our [Bug
Tracker](http://www.bufferbloat.net/projects/cerowrt/issues)

See also the <link>OCEAN CITY FAQ|FAQ</link>, the <link>OCEAN CITY
RELEASE NOTES</link> and <link>Cool things to do with your Cerowrt
router</link>.

*NB:* The rc6 build also supported a connection to http://gw.home.lan -
the bql-smoketests builds do not have a working bind module, so this has
been disabled in the newer versions.
