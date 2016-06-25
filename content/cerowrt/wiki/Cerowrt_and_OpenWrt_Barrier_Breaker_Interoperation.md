---
title: Cerowrt and OpenWrt Barrier Breaker Interoperation
date: 2014-10-14T12:08:16
lastmod: 2014-10-14T12:08:16
type: wiki
---
Cerowrt and OpenWrt Barrier Breaker Interoperation
==================================================

CeroWrt was a research project intended to spin up new functionality
into a single, conventional, home router. Nearly everything in the
3.10.50-1 release (and later) was pushed into OpenWrt "Barrier Breaker",
which supports thousands of different router types, however a few things
are different, notably cerowrt routes, rather than bridges everything.

HOWTO Configuring an openwrt Barrier Breaker device to be more "cerowrt-like"
-----------------------------------------------------------------------------

Let's say you have an existing CeroWrt box, and you want to add an
Access Point elsewhere on your network. For the sake of this example,
we'll use a Ubnt Picostation, which is a good outdoor access point, with
a single ethernet interface, and that you are configuring it from a
linux laptop.

### First Steps

-   Download the nano-m factory firmware update and the babels package
    from the openwrt repositories

<!-- -->

-   Install openssh-server and telnet on your laptop.

<!-- -->

-   Generate an ssh-key for your router with "ssh-keygen" - you can make
    one specific to administration if you like

<!-- -->

-   Set your laptop to a static ip of 192.168.1.2/24 and then plug it
    into the pico.

<!-- -->

-   Boot the Pico. Install Barrier Breaker on the device.

via the firmware upload web interface (it's on 192.168.1.20) or via the
classic tftp update method.

This will get a basic load of the BB OS in place, which you can telnet
to on 192.168.1.1 or access via the (unencrypted by default) web gui

-   telnet to the device

<!-- -->

-   Install babels - note the s - on it.

scp from your laptop the babels package you downloaded earlier to /tmp.\
opkg install /tmp/babel\*\
/etc/init.d/babeld enable \# but don't start it yet

While you are here, take your generated ssh public key, and put it in
/etc/dropbear/authorized\_keys

-   Change the IP address range to suit

In this example I will use 172.20.6 throughout. pick your own address
range that doesn't conflict with the cerowrt setup, preferably one
inside the same /16 cero is in.

sed -i s/192.168.1/172.20.6/g /etc/config/\*

-   Disable dhcp serving (for now) and make it be a dhcp client
    (for now)

edit the /etc/config/dhcp file and tell it to "ignore '1'" on both
interfaces for now

-   Give it a name in /etc/config/system

<!-- -->

-   Kill the firewall

This is an interior router, no need to firewall, particularly during
setup.\
Feel free to copy the firewall script to a backup, you might want to do
some stuff later on it.

Make /etc/config/firewall look like this.

    config defaults
            option input 'ACCEPT'
            option output 'ACCEPT'
            option forward 'ACCEPT'

-   Reboot. Plug the ethernet into your cerowrt box, the device should
    now be routed and\
    on your network, with a new IP address you can derive from
    inspecting the /tmp/dhcp.leases file\
    or get to via local dns.

### Next Steps

-   ssh into the router, do a

<!-- -->

    opkg update # should grab the openwrt BB database if dns is working
    opkg install snmpd # if you intend to monitor the system with snmp
    opkg install netperf tcpdump-mini # also optional. I like to test with netperf and look at stuff with tcpdump

-   Break apart the AP and the wifi

By default openwrt bridges rather than routes. We want to route.

-   Setup the wifi

#### If you want to mesh via ethernet

#### If you want to mesh via wifi

IMPORTANT: The babel protocol uses the BSSID rather than the SSID to tie
radios together, so you need to specify the same one that's on cerowrt.

#### If you want to mesh via wifi AND provide service via wifi

### Customization

Hit the web gui and add in the appropriate time.

do an opkg list | less and see if there are other packages you'd like to
add

You can either disable the gui (I generally do this), or add ssl support
to it

-   Change the password

