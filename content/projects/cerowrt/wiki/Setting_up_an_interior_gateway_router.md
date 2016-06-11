
---
title: Setting up an interior gateway router
date: 2014-03-26T09:01:50
lastmod: 2014-09-12T13:23:36
type: wiki
---
Setting up an interior gateway router (IGR)
===========================================

CeroWrt **routes** by default, not bridges. This brings in some
complexity in setup but large gains in latency.

For information on bridging, rather than routing, see <link>Setting up
CeroWrt to bridge</link>. See also [Tuning your CeroWrt default gateway]({{< relref "wiki/cerowrt/Tuning_your_CeroWrt_default_gateway.md" >}}).

Nobody remembers how the Internet works. *Internet addressing without
NAT requires unique IP addresses.* Always has. Don't forget.

Let's say you want a second router upstairs in your home, where you have
run an ethernet cable, what do you do? (Wireless only meshes, or
failover from ethernet to wireless is also possible, in CeroWrt).

CHANGE THE PASSWORD
-------------------

A default password is an invitation to be pownd, and existing malware
sometimes does target home routers. Change it! Even better, upload an
ssh key.

Renumber & rename
-----------------

First, renumber so each router is on a unique IP address, and serves up
unique IP addresses to hosts connected to it.

By renumbering EVERYTHING to a subnet (172.20.0.0/16 in this example)
you can make it easy to add more routers. If you get off the 172.30.42
network for everything but new CeroWrt routers, it makes booting up more
routers easy...

We strongly encourage everybody to renumber their networks in this way,
and get off the tyranny of everything being on 192.168.0.1 using double
and triple nat.

You need a unique DNS subdomain, and SSID, and to disable the Avahi's
MDNS forwarding. The GUI makes this tedious; the sed command and default
ip address scheme in CeroWrt makes this a snap:

    sed -i s/172.30.42/172.20.1/g /etc/config/* /etc/firewall.user # my main router is 172.20.1 the next router would be 172.20.2, 172.20.3, etc
    sed -i s/home.lan/upstairs.hm.example.org/g /etc/config/* # use your vanity domain name for something!
    sed -i s/cerowrt/upstairs-gw/g /etc/config/* /etc/avahi/avahi-daemon.conf # rename the router to something unique
    sed -i s/CEROwrt/UPSTAIRS/g /etc/config/wireless # "Daaaaad... cerowrt is down!"... "Which Cerowrt, son?" "Upstairs."
    /etc/init.d/avahi-daemon disable # regrettably mdns does not work yet across multiple routers

You can elide the snarky comments after the "\#". Don't copy/paste
unless you really want to be living in example.org and on that subnet.
(valid ranges are slices of 10.0.0.0/8, 192.168.0.0/16 and
172.16.0.0/12)

Fix Firewall rules
------------------

On an interior router you can disable the firewall rules almost entirely
and let your external router take care of partitioning internal versus
public networks.

cp /etc/config/firewall /etc/config/firewall.old first and make
/etc/config/firewall look like this:

    config defaults
            option input 'ACCEPT'
            option output 'ACCEPT'
            option forward 'ACCEPT'

    config include
            option path '/etc/firewall.user'

    config include 'bcp38'
            option type 'script'
            option path '/usr/lib/bcp38/run.sh'
            option family 'IPv4'
            option reload '1'

At a minimum, disable NAT masquerading.

While [BCP38](http://tools.ietf.org/html/bcp38) is in theory optional on
interior routers, we find it suppresses enough traffic from mdns names
that it is worth keeping.

So leave bcp38 support on on your internal routers, but you must add
your local subnet choices to it as exceptions to the /etc/config/bcp38
ruleset. In this example we chose 172.20.0.0/16 as our "networks", so we
add a line in /etc/config/bcp38 on your interior router

            list nomatch '172.20.0.0/16'

You may want to add a line to allow access to your cable modem, and
don't forget that if you have other networks that you will have to allow
their use. For example, jg adds the following two lines as well:

            list nomatch '192.168.1.0/24'
            list nomatch '192.168.100.1/32'

since he has been foolish enough to not renumber his gateway network
away from 192.168.1; his cable modem is located at 192.168.100.1 and it
is convenient to be able to monitor its management page.

DO NOT do this on an external router (it defeats the purpose).

### No need for a default route

Disable the default route fetching in /etc/config/network, since we are
distributing routes via the babel protocol.

    config interface ge00
            option 'ifname' 'ge00'
            option 'proto'  'dhcp'
            option 'defaultroute' '0'

Tell the routing daemon to listen on everything
-----------------------------------------------

DO NOT connect the routers together via their LAN ports (you will end up
with conflicting dhcp addresses), connect a LAN port of the main router
to the WAN port of the interior router.

Change /etc/config/babeld for ge00 from true to false for this stanza.
Leave all the other lines the same.

    config interface ge00                                    
    option 'ignore' 'false'  

The main gateway needs to be supplying a default route, (which is
disabled by default in the babel config; adding this is covered in the
main gateway router case).

### If you really want some firewall rules

This section needs to move and become a more philosophical page. The
point of connecting to the internet is to have good connectivity, and
the point of a firewall is to protect machines within network
boundaries. Firewalling reduces connectivity, routing increases it, and
there are many times where a interior firewall creates difficult to
debug problems, and other times where having a firewall is a lifesaver.
So here are some basic tips, if you really want some firewall rules on
the interior gateway...

If you are meshing via WiFi, you should change the guest network in the
firewall to be just the gw10 and gw00 interfaces, and move the gw11 and
gw01 to the "secure" firewall zone... and hard code in DNS servers.

You can use your internal DNS server via specifying the ip number(s) in
a "dns" line for ge00.

(we used to use the [AHCP]({{< relref "wiki/cerowrt/AHCP.md" >}}) protocol to distribute DNS
servers. The <link>HNETD</link> replacement is not yet ready)

If you are going to connect your second router via the WAN port, you
would definitely need to disable NAT (masq 0) and need to go through
it's babel ruleset and enable ge00, which is a good idea anyway.

It is sanest to run internal routers with few firewall rules, at least
to start with.

IPv6 brings in new headaches...

### Set Name Server

We previously used the [AHCP]({{< relref "wiki/cerowrt/AHCP.md" >}}) protocol to distribute DNS
servers. The <link>HNETD</link> replacement is not yet ready,
unfortunately. So you have to manually configure your name services by
editing the file /etc/config/dhcp and add the line:

            option server '/gw.example.org/172.20.1.1/'

to the "config dnsmasq" stanza at the beginning of the file, where
gw.example.org is the name of your external router followed by its IP
address. It is faster to use your external router's cache for lookup,
possibly avoiding a trip to your external router's DNS server.

Reboot
------

You should reboot at this point. If you do anything else, it will end up
hopelessly confused, anyway. Just reboot.

No matter how everything is connected, be it WiFi or ethernet or both,
the router will pick the best path to the gateway and you should be able
to ssh or access the web configuration interface to the new IP address
you assigned it.

Further tuning
--------------

Install the box wherever it goes. Remember NOT to plug in a router to
another router via its LAN port, but via its WAN port, or dhcp chaos can
ensue.

Make DNS subdomains match
-------------------------

In /etc/config/dhcp there is support for adding each internal sub-domain
to your network and the correct resolving name server.

(we are working on making this saner)

Select unique WiFi channels
---------------------------

Do a scan of your neighborhood via the CeroWrt GUI and choose channels
not in use nearby.

IF you are not meshing via WiFi, choose a new unique channel for the
wireless interfaces, one of 1,6, or 11 for the 2.4ghz radio, and
whatever is legal for the 5ghz radio for your country. In the USA, legal
5ghz channels for HT40+ mode are 36, 44, 157, and 165. If you are using
ht20 mode more channels are available but only half the bandwidth each;
this can be a good trade-off in dense wireless areas.

If you are meshing via WiFi, whatever you choose to connect the routers
together on needs to be on the same channel. If you have enough signal
strength it makes more sense to mesh together over 5ghz than 2.4. You
can do both since babel will pick the best one. You can even use all
three networks: wired, 2.4ghz, and 5ghz wireless, as the babel routing
protocol will pick the best route for you.

IPv6
----

### Stable IPv6 addressing

If you are fortunate enough to have stable IPv6 addressing (for example
via a HE tunnel), you can allocate ipv6 addresses for each internal
router out of your /48 subnet easily in /etc/config/network:

    config interface wan6           
            option ifname   @ge00                    
            option proto    dhcpv6                   
            option 'broadcast' '1'                   
            option 'metric' '2048'                   
            option 'reqprefix' '61' # by default cerowrt wants 6 networks
            option 'ip6prefix' '2001:db8:0:8::/61' # this is an example address! use whatever given you, and get 8 /64s for your second router.
            # increase the 4th stanza by 8 hex for every new router. There is also a new hint feature which we should document...

### Unstable IPv6 addressing

We plan to make interior routers work dynamically via the new hnetd
protocol. Until then, it is hard to get a subnet from a dynamically
changing ipv6 prefix.

Known problems with routing in the home
---------------------------------------

Plenty! (although a lot less than when we started)

### upnp does not work

Gaming consoles, etc, like to try and open ports via the upnp protocol,
which does not work. We hypothesize that port forwarding the upnp
requests to the main router might work.

### Scanning for resources outside the local network does not work

If you scan for a printer that is on one router while you are on another
router, MDNS scanning will not work. You should make a static IP entry
for it, give it a name, and use that instead. There is work underway to
build a DNS hybrid proxy that should eventually solve this problem. We
cannot use Avahi on interior, as routing loops and packet storms can
occur if you try!

### Some devices don't like /27 subnets

The Sony line of blue-ray players are known to not like the /27 subnets
CeroWrt uses. This is discussed on the [Sony BlueRay Bugs]({{< relref "wiki/cerowrt/Sony_BlueRay_Bugs.md" >}})
page.

### Chromecast only works on the local WiFi interface

If you are using Chromecast you must connect to the WiFi interface it is
on. This is another instance that the DNS hybrid proxy will solve.

### May be problem with pimd

You may need to kill and disable pimd as it has been seen to loop. See
bug \#448.
