
---
title: Tuning your CeroWrt default gateway
date: 2014-03-26T09:56:40
lastmod: 2014-03-26T10:46:49
type: wiki
---
Tuning your CeroWrt default gateway (External Gateway Router - EGR)
===================================================================

CeroWrt **routes** by default, not bridges. This brings in some
complexity in setup but large improvements in latency and jitter.

If you want multiple routers see also: [Setting up an interior gateway router]({{< relref "cerowrt/wiki/Setting_up_an_interior_gateway_router.md" >}}).

For information on bridging, rather than routing, see <link>Setting up
CeroWrt to bridge</link>.

This section is about tuning a cerowrt box to work better as a default
gateway and working better with internal routers.

CHANGE THE PASSWORD
-------------------

There is no point in running things over SSL or secure sockets if you
have a default password. Change it. Also upload an ssh key.

Renumber & rename
-----------------

For starters, you need to renumber so each router is on a unique IP
address, and serves up unique IP addresses to hosts connected to it.

What I typically do is pick a subnet (172.20.0.0/16 in this example) and
renumber EVERYTHING by this scheme (this makes it easy to add more
routers)

I strongly encourage everybody to renumber their networks in this way,
and get off the tyranny of everything being on 192.168.0.1 and double
and triple nat. If you get off the 172.30.42 network for everything but
newly flashed CeroWrt routers, it makes booting up more routers easy,
they will boot and mesh automagically.

You need a unique DNS subdomain, and SSID, and to disable the avahi's
mdns forwarding. The gui makes this tedious; the sed command and default
ip address scheme in cerowrt makes this a snap:

    sed -i s/172.30.42/172.20.0/g /etc/config/* # my main router is 172.20.0 the next router would be 172.20.1, 172.20.2, etc
    sed -i s/home.lan/mygw.hm.example.org/g /etc/config/* # use your vanity domain name for something!
    sed -i s/CEROwrt/MYGW/g /etc/config/wireless # "Daaaaad... CEROwrt" is down... "Which Cerowrt, son?" the "MYGW."
    /etc/init.d/avahi-daemon disable # regrettably mdns does not work yet

You can elide the snarky comments after the "\#". And don't copy/paste
unless you really want to be living in example.org and on that subnet.\
(valid ranges are slices of 10.0.0.0/8, 192.168.0.0/16 and
172.16.0.0/12)

The way the above domain naming scheme works is that you would have
example.org and things like www.example.org hosted somewhere else,\
and delegate dns naming for hm.example.org to your main router, and then
create subdomains off of that for each router.

Rename the router and set the correct timezone
----------------------------------------------

/etc/config/system has the default name of the router and the timezone
(it's easiest to change this via the web interface)

/etc/config/dhcp has various names and aliases for the router (and other
devices on your network)

Fix Firewall rules
------------------

The default firewall rules are designed to work on your external gateway
router with no modification.

Tell the routing daemon to supply a default route to other routers.
-------------------------------------------------------------------

In /etc/config/babel change these two stanzas from true to false.

    config filter                                                                   
            option 'ignore' 'false' # change from the default "true" to false 
            # Type                                                                  
            option 'type' 'redistribute'                                            
            # Selectors: ip, eq, le, ge, neigh, id, proto, local, if                
            option 'ip' '0.0.0.0/0'                                                 
            option 'le' '0'                                                         
            option 'proto' '0'                                                      
            # Action                                                                
            option 'action' 'metric 96'                                             

    # if you are an ipv6 source specific gateway un-ignore                          
    config filter                                                                   
            option 'ignore' 'false' # change from the default "true" to false.                                             
            # Type                                                                  
            option 'type' 'redistribute'                                            
            # Selectors: ip, eq, le, ge, neigh, id, proto, local, if                
            option 'src_ip' '::/0'                                                  
            option 'src_ge' '0'                                                     
            option 'proto' '0'                                                      
            # Action                                                                
            option 'action' 'metric 96'                                             
    #       These distribute all the routes on all the interfaces                   
    #       For both ipv6 and ipv4   

Don't do this on interior routers, only on routers with direct access to
the internet. Since the advent of <link>source specific routing</link>
you can actually have multiple connections to the internet and each one
can provide a default route to the rest of your network, which is cool,
but...

If you supply a default route from an interior router, routing loops
happen. Never supply default routes from interior routers.

Reboot
------

You should reboot at this point. No matter how everything is connected,
be it wifi or ethernet or both, the router will pick the best path to\
the gateway and you should be able to ssh or access the web
configuration interface to the new IP address you assigned it and the
new domain\
name you assigned it.

Further tuning
--------------

Install the box wherever it goes.

Configure [SQM]({{< relref "cerowrt/wiki/SQM.md" >}})
--------------------------

Can't stress that more. Fix your bufferbloat! see: [Setting up SQM for CeroWrt 310]({{< relref "cerowrt/wiki/Setting_up_SQM_for_CeroWrt_310.md" >}}).

You can make your network perform [like
this](http://snapon.lab.bufferbloat.net/~cero2/jimreisert/results.html)

Tune ssh access
---------------

The default access policy for some router services is in
/etc/xinetd.conf. I use a jump box in the cloud (never mind where),\
with a fixed IP, so I can ssh into the routers I maintain from there. It
is generally not a good idea to allow generic\
ssh access to your router from the whole internet.

You will end up attracting ssh dictionary attackers tediously pounding
away at common logins and password.

Make dns subdomains match
-------------------------

In /etc/config/dhcp there is support for adding each internal subdomain
to your network and the correct resolving nameserver.

Select unique wifi channels
---------------------------

Do a scan of your neighborhood via the gui and choose channels not in
use nearby.

IF you are not meshing via wifi, choose a new unique channel for the
wireless interfaces, one of 1,6, or 11 for the 2.4ghz radio, and
whatever is legal for the 5ghz radio for your country. In the usa, legal
5ghz channels for HT40+ modeare 36, 44, 157, and 165. If you are using
ht20 mode more channels are available but only half the bandwidth.

If you are meshing via wifi, whatever you choose to connect the routers
together on needs to be on the same channel. IF you have enough signal\
strength it makes more sense to mesh together over 5ghz than 2.4. You
can do both, babel will pick the best one. You can even do all three,\
wired, 2.4ghz, and 5ghz, the routing protocol will pick the best route
for you.

IPv6
----

### Stable IPv6 addressing

If you are fortunate enough to have stable IPv6 addressing (for example
via a HE tunnel), you can allocate ipv6 addresses for each internal
router out\
of your /48 subnet easily in /etc/config/network:

config interface wan6\
option ifname @ge00\
option proto dhcpv6\
option 'broadcast' '1'\
option 'metric' '2048'\
option 'reqprefix' '60' \# by default cerowrt wants 6 networks\
option 'ip6prefix' '2001:db8:0:0::/61' \# this is an example address!
use whatever given you, and get 8 /64s for your second router.\
\# increase the 4th stanza by 8 for every new router.

### Unstable IPv6 addressing

CeroWrt supports the dhcpv6-pd protocol for getting an IPv6 subnet from
providers such as comcast, and it is enabled by default.\
If your provider supports dhcp-pd, the below should hopefully "just
work"!

config interface wan6\
option ifname @ge00\
option proto dhcpv6\
option 'broadcast' '1'\
option 'metric' '2048'\
option 'reqprefix' '60' \# by default cerowrt wants 6 networks. Comcast
provides 16. Other providers do more. Feel free to agitate for more.

Known problems with routing in the home
---------------------------------------

Plenty! (although a lot less than when we started)

### Nobody remembers how the internet works

Internet addressing without nat requires unique IP addresses. Always
has. Don't forget. If you have two machines on the same IP address bad
things happen. If you have two natted networks on the same ip address
range, bad things happen. Don't do that. Renumber, always.

### UPNP only works on the main router

Gaming consoles, etc, like to try and open ports via the upnp protocol.
This works fine on the\
main router, but not on internal routers.

### Scanning for resources outside the local network does not work

If you scan for a printer that is upstairs while you are downstairs,
scanning does not work. You should\
make a static IP entry for it, give it a name, and use that instead.

There is a new protocol on its way for fixing browsing across multiple
subnets, it's called\
[mdns hybrid
proxy](http://tools.ietf.org/html/draft-cheshire-mdnsext-hybrid-02)

There is an optional package for this in the cerowrt packages database
called "ohybridproxy"\
but it isn't fully baked yet.

### Some devices don't like /27 subnets

The sony line of blue-ray players are known to not like the /27 subnets
cerowrt uses. This is discussed on the [Sony BlueRay Bugs]({{< relref "cerowrt/wiki/Sony_BlueRay_Bugs.md" >}})
page.
