
---
title: CAPETOWN_INSTALLATION_GUIDE
date: 2011-05-18T11:34:47
lastmod: 2011-09-05T11:21:47
---
CAPETOWN INSTALLATION GUIDE
===========================

It would be a good idea to print out these instructions before
proceeding. If you are in the first pilot deployment in Gary Marsden's
lab, chances are we are giving you a router that has already been
flashed with Bismark firmware, so you can proceed to Step 1
("Configuring and Installing the Router") below.

Step 0. Flashing the router
---------------------------

If you are not installing a preflashed <link>Capetown</link> release of
the router hardware, please see the <link>Capetown flashing
instructions|flashing instructions</link> for how to install the
Capetown Bismark build on your <link>Wndr3700v2</link> Router.

Step 1. Configuring and Installing the Router
---------------------------------------------

1.  **Power on your router.** The router should boot in under
    two minutes. The router itself comes up on 192.168.42.1. The router
    serve IP addresses on the 192.168.42.0/24 network by default. (see
    <link>why .42</link>?)
2.  **Connect to your router.** Plug in a laptop or computer to one of
    the 4 LAN ports on the router, and refresh your laptop/computer's
    DHCP IP address. Alternatively, connect via wireless by setting your
    SSID to "BISMARK" (no SSID passowrd). Your machine should get an IP
    address from the 192.168.42.0/24 subnet.
3.  **Configure your router's default password.** In your web browser,
    go to the router configuration screen at http://192.168.42.1:81 (see
    also <link>why 81</link>?) Enter in a new password for the router.
    **Write this password down somewhere.** The login will be "root",
    and the password that you set should be something difficult.
4.  **Secure your wireless interfaces** Go to the *Network-&gt;Wireless*
    configuration page, and change the SSIDs of the various interfaces
    to suit your liking. (See also <link>Capetown FAQ|FAQ</link>) Enable
    WPA2 encryption on the LAN interfaces, and if you wish your guest
    interfaces to be secured, do the same there, too. Choose unique
    passwords for the lan and guest interfaces.
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
-   <link>QoS</link> is turned **ON** by default.(see <link>Capetown
    FAQ|FAQ</link>). You should address this issue after connecting to
    the internet.

Step 2. Fine-tuning your QoS Settings
-------------------------------------

By default, the Cape Town Bismark Router is configured for slow Internet
connections. See the <link>Capetown FAQ|FAQ</link> for how to set it
appropriately for your network connection. This is a very important
step!

Step 3. Register for the Bismark Study
--------------------------------------

You can sign up to receive updates for the Bismark project at the
[Project BISMark Web site](http://projectbismark.net)

Changing your default IP addresses
----------------------------------

If you wish to use other default IP addresses, now is the time to change
them. (We recommend against using 192.168.0.1 and 192.168.1.1 for
historical reasons). Go to the *Network* screen on the router and change
to suit. By default the interfaces come up on the 192.168.42.1,
192.168.43.1 and 192.168.44.1 addresses.

*Important:* If you change the default IP address, your Web interface
will change at this point to be whatever-you-chose:81 after doing a save
and apply, and you will need to change the url in your browser
accordingly.

Thanks!
-------

You should now be on the Internet using the latest and greatest code
from the <link>bismark:Wiki|Bismark</link> Project, the
<link>cerowrt:Wiki|Bufferbloat Cerowrt</link> project, and
[OpenWrt](http://www.openwrt.org) .

We hope that your experience will be exceptional. Please send us your
feedback and comments by registering and posting to the
[bismark-users](http://lists.noise.gatech.edu/listinfo/bismark-users)
mailing list. You can also file bugs and feature requests in our [Bug
Tracker](http://www.bufferbloat.net/projects/bismark/issues)

See also the <link>Capetown FAQ|FAQ</link>, the <link>CAPETOWN RELEASE
NOTES</link> and <link>Cool things to do with your Bismark
router</link>.
