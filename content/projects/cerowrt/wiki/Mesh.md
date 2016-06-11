
---
title: Mesh
date: 2011-08-24T05:03:54
lastmod: 2012-10-01T12:22:18
type: wiki
---
Mesh Networking
===============

The mesh networking component in CeroWrt has two components - AHCP,
which hands out IP addresses, and babel - which manages determining the
best routes available. A full blown mesh node can easily switch between
multiple wired and wireless interfaces without losing long term tcp
connections (notably ssh), and remain accessible via all interfaces via
basically a fixed IP adddress.

By default, in order to co-exist with existing IP address distribution
schemes, full mesh capability is not available, however, even partially
implemented, it's useful.

The examples below assume that you are on the default IP addresses
supplied by the router. Secondary nodes should have their entire subnets
be different than the other nodes.

Mesh networking in cerowrt is not limited to babel and ahcp. Other mesh
networking protocols are available as options, notably batman and olsr.
In fact many other routing protocols are supported too, all the way up
to and including BGP. The main rationale for babel and ahcp is that they
are (unlike batman) layer 3 routing protocols and it is much easier to
understand what is going on with those than layer 2 protocols. Some
things are easier with layer 2 protocols, some are harder, [all are
interesting](http://wirelesssummit.org) ....

Configuring mesh routing on the router(s)
-----------------------------------------

The CeroWrt routers are configured as server mesh nodes by default. This
may change in a future release.

You will need to set at least one router up as an [AHCP]({{< relref "wiki/cerowrt/AHCP.md" >}})
server in order for clients to obtain an ip address on the [babel SSID]({{< relref "wiki/cerowrt/Babel_SSID.md" >}}). If they are connected via other means (wired, or wireless
STA mode) the routers should have unique IP address ranges, and NAT
disabled.

### On the server machine:

Change /etc/config/ahcpd to have:

            option 'mode' 'server'
            list 'prefix' '172.30.42.225/27
            # list 'prefix' 'fde6:20f5:c9ac:358::1/64'
            # Usually when I have a /48 to deal with, I set aside something like
            # the:fourtyeight:prefix:bab5::1/64 for ahcp 
            ## You can also setup a real or 6to4 ipv6 address prefix
            ## and/or use site-local ipv6
            ## list 'name_server' 'fde6:20f5:c9ac:358::1'
            list 'name_server' '172.30.42.224'
            ## list 'ntp_server' '192.168.4.2'

You can have ahcp just distribute ipv6 addresses if you so desire. (this
is useful when you only have a /64 to deal with, and in that case you
have to disable radvd entirely and all ipv6 nodes have to run ahcp and
babel to see each other)

Change /etc/config/network to look like this (or just let ahcp assing
these with proto "ahcp", which is the default.

    config 'interface' 'gw11'   
            option 'proto' 'static'     
            option 'ipaddr' '172.30.42.224' 
            option 'netmask' '255.255.255.255'

    config 'interface' 'gw01'   
            option 'proto' 'static'
            option 'ipaddr' '172.30.42.224'
            option 'netmask' '255.255.255.255'

If you are using babeld: If you are not using the default IP address
ranges, you will need to modify /etc/babeld.conf to propagate the routes
to those IP address ranges too.

If you are using quagga: the default gw to the internet needs
"redistribute kernel" and "redistribute static" lines added to
/etc/quagga/babeld.conf. In the case of 6to4, you may need to add a ipv6
default route to zebra.

Restart networking and ahcpd. In the ahcp configuration file, you
created a lease address range, starting one above the base number, In
/etc/config/network, you will note that the IP address masks in are /32
masks, and the ip addresses assigned are that **same** base number. The
babel protocol figures out where to send data based on ip/interface
tuples in this case.

### On the client routers (or a server router, actually)

-   YOU WILL HAVE TO RENUMBER. Choose a unique subnet number per router.

<!-- -->

    cd /etc/config
    sed -i s#172.30.42#172.30.SOME_UNIQUE_NUMBER#g * ../babeld.conf /etc/chroot/*/etc/named/*/*
    sed -i s#42.30.172#SOME_UNIQUE_NUMBER.30.172#g /etc/chroot/*/etc/named/*/*

Note: the above script is also useful for renumbering a server router.

You will definately need to reboot after running that script.

Change the configuration to be client on /etc/config/ahcp (comment out
everything else)

The client routers will automatically pick up an address from AHCP
assuming at least one interface is on the same wireless channel as a
server,\
and then route via the best route to the other routers. Also, get ntp
and name service from the right place.

Note that you can just configure all your routers as servers on unique
ranges, serve up ahcp from all of them, and still have routes
distributed via babel.

Client machines can then just wander from node to node.

Using babel routing without ahcp
--------------------------------

There is no strict need to use AHCP to distribute IPs so long as your
address ranges are disjoint and babel is told what of the routers
addresses to distribute. You can, in that case, dynamically assign
addresses via dhcp - but make sure client routers have disabled NAT.

Distributing an ipv6 default route via the main server via quagga
-----------------------------------------------------------------

In quagga, there is an ongoing bug (\#406) a workaround is to add lines
like this to /etc/quagga/zebra.conf

    interface 6to4-ge01  ! the name of the 6to4 interface in this case
    ipv6 route ::/0 2002:c058:6301:: ! the 6to4 default gw

Other ipv6 mechanisms are similar, but you have to set the default gw
and device correctly!

Using ad-hoc mode under wireless on a linux laptop (simplest possible config)
-----------------------------------------------------------------------------

iwconfig the\_interface channel XX mode ad-hoc essid babel

I note that many older 5ghz machines do not do ad-hoc properly, and
2.4ghz needs to be used instead. Using ad-hoc mode, rather than managed,
gives the ability to move between the highest performing local access
points.

So as an example for 2.4 ghz, assuming you are on channel 11 on the mesh
router too, and you're not running Network Manager on this interface

    ifconfig wlan0 down
    iwconfig wlan0 mode ad-hoc channel 11 essid babel # some devices require this in another order
    ifconfig wlan0 up
    iwconfig wlan0 mode ad-hoc channel 11 essid babel
    # you can also toss these in the background using the -D option
    ahcpd -L some_log_file wlan0 &
    babeld -z3 -l wlan0 &

so if you get an address, you should then be able to see tons of routes
via:

    ip route
    ip -6 route

### Distributing your own default route

Routers that are connected to the internet can and should distribute
their default route via uncommenting the default route in the
/etc/babeld.conf file.

Mildly different procedure (as noted above) for quagga-babeld

### Co-existing with DHCP

Most network managers assume you can have the wired **or** wireless
network connected. AHCP + babel assume you can have **both** connected.
AHCP and DHCP can co-exist to some extent.

Furthermore most dhcp servers distribute a default route, which needs to
be disabled in order to failover properly. With ISC dhclient, that
involves changing the /etc/dhcp/dhclient.conf file\
to not request the 'route'.

I turn off network manager in Linux entirely, because of these
assumptions. You can leave it on if you want to co-exist with dhcp, but
it helps to be running babeld and disable getting the default route,
thusly:

Change from:

    request subnet-mask, broadcast-address, time-offset, *routers*,
            domain-name, domain-name-servers, domain-search, host-name,
            netbios-name-servers, netbios-scope, interface-mtu,
            rfc3442-classless-static-routes, ntp-servers;

to:

    request subnet-mask, broadcast-address, time-offset, 
            domain-name, domain-name-servers, domain-search, host-name,
            netbios-name-servers, netbios-scope, interface-mtu,
            rfc3442-classless-static-routes, ntp-servers;

You can also remove domain-name-servers and ntp-servers if you are
providing that information via ahcp.

### Firewalls, NAT and babel

NAT and Firewalling is a pain in the arse as it breaks the end to end
principle. Any place where you don't need a firewall or NAT (like on an
internal router)\
TURN IT OFF. the easiest way to disable firewalling on an interior
router is to change all your policies in /etc/config/firewall to
'ACCEPT'.

    config defaults
            option input 'ACCEPT'
            option output 'ACCEPT'
            option forward 'ACCEPT'
            option tcp_ecn '1'

To disable NAT change the masq and clamp mss settings in that file to 0.

If (and only if) you disable nat and firewalling and want the external
wan interface to be part of the mesh network, you will need to add the
ge00 interface to /etc/config/babel (or for quagga, uncomment the
relevant line in /etc/quagga/babeld.conf)

I have run into trouble with the default firewall even as it is. It
really, really, really wants to firewall stuff.

I have ended up slamming this into /etc/firewall.user on some versions
of cerowrt


    for i in gw11 gw01
    do
    for iptables in iptables ip6tables
    do
    $iptables -I FORWARD -o $i -j ACCEPT
    $iptables -I INPUT -i $i -j ACCEPT
    $iptables -I OUTPUT -o $i -j ACCEPT
    done
    done

### A laptop configured via dhcp

The complexities of the babel protocol are hidden in the router, there
is no need to run either ahcp or babel on any client machines. I
personally like to run babel so I can see the health of my network on
the laptop with a tool like
[babelweb](http://www.pps.jussieu.fr/~kerneis/software/babelweb/) -
here's the mesh network at [bloatlab 1]({{< relref "wiki/cerowrt/BloatLab_1.md" >}}) for example.
http://io.lab.bufferbloat.net:8080/

### A laptop configured to be a partial mesh node

You run babel across all the interfaces you have, and ahcp across only
the ones you want via ahcp. For example, in my case I have two radios in
my laptop, the radios use different channels and get their addresses via
ahcp, so as I move around, the best is chosen for routing...

### A laptop configured as a full mesh node would run

(Both of these can be configured in a conf file)

    ahcpd -d interface interface interface # to get ip addresses on each 'interface'
    babeld -z3 -l interface interface interface # to get routes across those interfaces

In this case the laptop also can and will act as a router itself.

Using mesh networking fully
---------------------------

You can serve AHCP across wired interfaces too. This makes moving
between wired and wireless modes entirely transparent. However, client
nodes also then need to run babel to get routes, as no default route is
distributed (default routes are evil).

Pure mesh networking
====================

**TO HECK WITH ALL THIS BACKWARD COMPATIBILITY STUFF** I just want a
pure mesh network.

Ya know, this used to be so much easier before I put in the backward
compatibility stuff and just set these boxes up as a pure mesh backbone
(as were my old nanostation M5s). You plugged it, you waved it around,
and you were online.

Retrofitting it into cerowrt, will require a uci script to convert all
the interfaces to AHCP only, among other things.

I want one button on the gui - make me a pure mesh node.
